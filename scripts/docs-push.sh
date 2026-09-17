#!/usr/bin/env bash
# Push every docs worktree that is ahead of its upstream, one at a time,
# waiting for each branch's gh-pages deploy to finish before starting the next.
set -uo pipefail

dry_run=false
[[ "${1:-}" == "-n" || "${1:-}" == "--dry-run" ]] && dry_run=true

# An unattended run outlasts the idle-sleep timer. On 2026-09-17 the machine
# slept ten minutes in; the run took 94 minutes instead of 22 and one push died
# mid-pack with a broken pipe. -i blocks idle sleep only, so the display sleeps.
if [[ -z "${DOCS_PUSH_CAFFEINATED:-}" ]] && command -v caffeinate >/dev/null; then
  DOCS_PUSH_CAFFEINATED=1 exec caffeinate -i "$0" "$@"
fi

repo=$(git remote get-url origin | sed -E 's#^.*[:/]([^/]+/[^/]+)$#\1#; s#\.git$##')
main_dir=$(git rev-parse --show-toplevel)

# Fail fast rather than let a bad repo slug reach the pollers: their "treat an
# error as zero active runs" fallback would report quiet and skip every gap.
if ! gh run list --repo "$repo" --limit 1 >/dev/null 2>&1; then
  echo "Cannot read Actions runs for '$repo' — check gh auth and the origin remote." >&2
  exit 1
fi

# gh-pages writers. These are NOT redundant with each other: each publishes a
# different mike version, so a cancelled one loses that version's update. The
# Pages builder (pages-build-deployment) is excluded on purpose — it renders
# whatever is on gh-pages, so newest-wins is correct and needs no gap.
writers='Auto Publish Branch|Auto Sync Core'

active_writers() {
  gh run list --repo "$repo" --limit 40 --json workflowName,status \
    -q "[.[] | select(.status==\"in_progress\" or .status==\"queued\") | select(.workflowName | test(\"$writers\"))] | length" 2>/dev/null || echo 0
}

run_for_sha() {
  gh run list --repo "$repo" --limit 40 --json workflowName,headSha,status \
    -q "[.[] | select(.headSha==\"$1\") | select(.workflowName | test(\"$writers\"))] | length" 2>/dev/null || echo 0
}

# Wait for the deploy triggered by $sha, then for the repo to go quiet. The two
# phases are separate because push returns before GitHub registers the run: poll
# only for quiet and you would sail through the gap while the run is pending.
# Quiet also covers amplification — a core push syncs to its downstream engine
# branches, and each of those commits triggers its own publish.
wait_for_deploy() {
  local sha=$1 name=$2 waited=0
  while (( waited < 90 )); do
    [[ "$(run_for_sha "$sha")" != "0" ]] && break
    sleep 5; (( waited += 5 ))
  done
  if (( waited >= 90 )); then
    echo "  no deploy registered within 90s — branch likely has no auto-publish workflow"
    return
  fi
  while (( waited < 900 )); do
    [[ "$(active_writers)" == "0" ]] && break
    sleep 10; (( waited += 10 ))
  done
  echo "  deploy settled after ${waited}s"
}

# Core branches first: pushing one makes auto-sync-core commit onto its
# downstream engine branches, so a downstream push before that lands would be
# rejected non-fast-forward.
to_push=()
while read -r dir; do
  [[ "$dir" == "$main_dir" ]] && continue
  branch=$(git -C "$dir" rev-parse --abbrev-ref HEAD 2>/dev/null) || continue
  ahead=$(git -C "$dir" rev-list --count '@{u}..HEAD' 2>/dev/null) || continue
  (( ahead > 0 )) && to_push+=("$(if [[ $branch == core/* ]]; then echo 0; else echo 1; fi)	$branch	$dir	$ahead")
done < <(git -C "$main_dir" worktree list --porcelain | awk '/^worktree /{print $2}')

if (( ${#to_push[@]} == 0 )); then
  echo "Nothing ahead of remote in any worktree."
  exit 0
fi

mapfile -t to_push < <(printf '%s\n' "${to_push[@]}" | sort)

echo "Queued:"
for row in "${to_push[@]}"; do
  IFS=$'\t' read -r _ branch _ ahead <<<"$row"
  printf '  %-16s %s commit(s)\n' "$branch" "$ahead"
done
$dry_run && { echo; echo "(dry run — nothing pushed)"; exit 0; }

failed=()
for i in "${!to_push[@]}"; do
  IFS=$'\t' read -r _ branch dir _ <<<"${to_push[$i]}"
  echo; echo "Pushing $branch..."

  if ! git -C "$dir" pull --rebase --quiet; then
    echo "Pull failed in $branch — resolve before re-running."
    exit 1
  fi

  sha=$(git -C "$dir" rev-parse HEAD)
  if ! git -C "$dir" push --quiet; then
    # A dropped connection exits nonzero after the remote already took the pack
    # (seen 2026-09-17 on toolkit/v0.4). Ask the remote rather than trust $?.
    git -C "$dir" fetch --quiet
    if (( $(git -C "$dir" rev-list --count '@{u}..HEAD') > 0 )); then
      echo "  PUSH FAILED — $branch is still ahead of remote"
      failed+=("$branch"); continue
    fi
    echo "  push reported an error but the remote has the commits — continuing"
  fi
  echo "  pushed $sha"

  (( i < ${#to_push[@]} - 1 )) && wait_for_deploy "$sha" "$branch"
done

echo
if (( ${#failed[@]} > 0 )); then
  echo "Finished with failures: ${failed[*]}"
  exit 1
fi
echo "All pushes complete."

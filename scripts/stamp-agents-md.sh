#!/usr/bin/env bash
# Stamp AGENTS.md and CLAUDE.md from main onto every live content branch.
set -euo pipefail

dry_run=false
[[ "${1:-}" == "-n" || "${1:-}" == "--dry-run" ]] && dry_run=true

main_dir=$(git rev-parse --show-toplevel)
git -C "$main_dir" fetch --prune --quiet

# A branch is live if it carries an AGENTS.md without the frozen-branch notice
# the retirement recipe prepends. Branches predating AGENTS.md have no file to
# sync, so both retirement eras exclude themselves without a maintained list.
live=()
while read -r b; do
  text=$(git -C "$main_dir" show "origin/$b:AGENTS.md" 2>/dev/null) || continue
  [[ "$text" == *"This branch is frozen"* ]] && continue
  live+=("$b")
done < <(git -C "$main_dir" for-each-ref --format='%(refname:short)' refs/remotes/origin \
  | sed 's|^origin/||' \
  | grep -E '^((core|unity|unreal|websdk|api|toolkit)/v[0-9]+\.[0-9]+|home|internal)$')

declare -A tree
while read -r path; do
  branch=$(git -C "$path" rev-parse --abbrev-ref HEAD 2>/dev/null) || continue
  tree["$branch"]="$path"
done < <(git -C "$main_dir" worktree list --porcelain | awk '/^worktree /{print $2}')

missing=()
for b in "${live[@]}"; do [[ -n "${tree[$b]:-}" ]] || missing+=("$b"); done
if [[ ${#missing[@]} -gt 0 ]]; then
  echo "No worktree for these live branches — add one, then re-run:" >&2
  for b in "${missing[@]}"; do echo "  git worktree add ../beamable-docs-<name> $b" >&2; done
  exit 1
fi

for b in "${live[@]}"; do
  d="${tree[$b]}"
  if [[ -n "$(git -C "$d" status --porcelain)" ]]; then
    echo "SKIP $b — worktree is dirty"
    continue
  fi
  cp "$main_dir/AGENTS.md" "$main_dir/CLAUDE.md" "$d/"
  if git -C "$d" diff --quiet -- AGENTS.md CLAUDE.md; then
    echo "ok   $b — already current"
    continue
  fi
  if $dry_run; then
    git -C "$d" checkout -- AGENTS.md CLAUDE.md
    echo "WOULD STAMP $b"
  else
    git -C "$d" add AGENTS.md CLAUDE.md
    git -C "$d" commit --quiet -m "Sync AGENTS.md from main"
    echo "STAMP $b — $(git -C "$d" rev-parse --short HEAD)"
  fi
done

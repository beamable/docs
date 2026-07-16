# AGENTS.md

## Project Overview

Beamable Docs is a multi-version documentation site for Beamable SDKs (Unity, Unreal, WebSDK, Core, TypeScript, API). Documentation content lives on versioned Git branches, not on `main`. The `main` branch holds only the shared tooling, setup scripts, and CI/CD configuration.

## Branch Architecture

Each SDK version is maintained on its own branch with its own `mkdocs.yml`:

- `core/v*` — Shared Beamable concepts
- `unity/v*` — Unity SDK docs
- `unreal/v*` — Unreal SDK docs
- `websdk/v*` — WebSDK docs
- `api/v*`, `typescript/v*` — API and TypeScript docs
- `internal` — Internal Beamable staff guides (published but not publicly advertised; only accessible via direct URL)
- `gh-pages` — GitHub Pages deployment target (do not edit directly)

Two branches have no version component: `main` (shared tooling and CI/CD; the starting point for new contributors) and `internal`. All other content branches carry a version suffix.

To edit documentation, switch to the appropriate versioned branch before making changes.

## Core-owned paths (must not be edited on downstream branches)

These paths are auto-synced from core branches into unity and unreal branches by `.github/workflows/auto-sync-core.yml`:

- `docs/cli/guides/`
- `docs/cli/SUMMARY.md` (the CLI-section nav; synced as a single file so core-owned CLI guides carry their nav entry downstream — see below)
- `docs/includes/` (including `abbreviations.md`)
- `docs/portal/`

**Edit files in these paths only from a core worktree.** Editing them anywhere else is futile and silently lossy: `auto-sync-core` replaces the downstream copy of these paths with core's version wholesale on every run, so the next push to the feeding core branch discards whatever you changed downstream — with no warning, no PR, and no trace.

The rule applies even during a copyediting sweep that touches every other branch. Skip these paths on unity and unreal — they reach those branches automatically via the next core sync. (Under the earlier squash-merge sync, downstream edits produced hand-resolved conflict PRs such as #96 and #97; the current wholesale-overwrite sync discards them silently instead, which is easier to miss.) The rule is not optional.

Before committing on a unity or unreal worktree, verify nothing staged touches a core-owned path:

```bash
git diff --cached --name-only | grep -E '^docs/(cli/guides|includes|portal)/|^docs/cli/SUMMARY\.md$' && \
  echo "STOP: core-only path in staged changes — revert and re-apply on core"
```

A match means: `git restore --staged <path>`, `git checkout -- <path>`, switch to the relevant core worktree, re-apply the change there, and commit. Auto-sync-core handles propagation downstream.

Everything outside these paths is fair game for direct editing on the relevant downstream branch — unity-only edits on unity, unreal-only edits on unreal.

## Working with Worktrees

Because content lives on many branches simultaneously, `git worktree` is the recommended workflow. Check out each branch into a sibling directory of the main `docs/` clone, embedding the SDK name and version in the path so multiple versions can coexist on disk at once.

Suggested naming convention (siblings of `docs/` under `~/src/beamable/`, or wherever you clone it):

```
beamable-docs-unity-5.0    → unity/v5.0
beamable-docs-unity-5.1    → unity/v5.1
beamable-docs-core-7.0     → core/v7.0
beamable-docs-core-7.1     → core/v7.1
beamable-docs-core-7.2     → core/v7.2
beamable-docs-unreal-2.2   → unreal/v2.2
beamable-docs-unreal-2.3   → unreal/v2.3
beamable-docs-websdk-1.0   → websdk/v1.0
beamable-docs-api-1.0      → api/v1.0
beamable-docs-internal     → internal
```

Add a worktree:

```sh
git worktree add ../beamable-docs-unity-5.0 unity/v5.0
```

Adjacent minor versions (e.g. `v5.0` and `v5.1`) typically have little divergence, so the same copyediting change usually applies cleanly to both.

### Core → Unity pull-after-push

After pushing to a core branch, immediately `git pull` in the corresponding unity and unreal worktrees. The `auto-sync-core.yml` action copies core's core-owned paths onto downstream branches and commits them on push; without pulling afterward, your next push to those branches will be rejected as non-fast-forward.

### Staggered pushes

GitHub Actions serializes gh-pages deploys with a concurrency group (one active job, one pending). Pushing multiple branches in rapid succession causes queued jobs to be canceled. Push branches sequentially, waiting for each deploy to complete before pushing the next (typical run: 40–90 seconds).

The script below pushes all ahead worktrees with a 2-minute gap. Save it as a shell function or run it directly:

```bash
#!/usr/bin/env bash
to_push=()
for dir in ~/src/beamable/beamable-docs-*/; do
  dir="${dir%/}"
  ahead=$(git -C "$dir" rev-list --count '@{u}..HEAD' 2>/dev/null)
  [[ "$ahead" -gt 0 ]] && to_push+=("$dir")
done

if [[ ${#to_push[@]} -eq 0 ]]; then
  echo "Nothing ahead of remote in any beamable-docs worktree."
  exit 0
fi

echo "Queued:"; for d in "${to_push[@]}"; do echo "  $(basename "$d")"; done

# Push order relies on lexical glob expansion of beamable-docs-*/:
# api, core, internal, unity, unreal, websdk. This happens to place
# core/* before unity/* and unreal/*, which is required by the
# auto-sync-core dependency (core's core-owned paths are copied
# onto unity and unreal on push, so core must land first). If a future SDK
# is named alphabetically before "core" with a downstream sync
# relationship, replace this implicit ordering with an explicit
# priority sort.

for i in "${!to_push[@]}"; do
  echo; echo "Pushing $(basename "${to_push[$i]}")..."
  # Pull --rebase first to pick up any auto-sync-core sync commits
  # that landed while editing. Without this, the push fails as
  # non-fast-forward whenever a core branch was pushed upstream
  # of a downstream branch since the last local fetch.
  git -C "${to_push[$i]}" pull --rebase || { echo "Pull failed for $(basename "${to_push[$i]}") — resolve and re-run."; exit 1; }
  git -C "${to_push[$i]}" push
  [[ $i -ge 1 && $i -lt $((${#to_push[@]} - 1)) ]] && echo "Waiting 2 minutes..." && sleep 120
done
echo; echo "All pushes complete."
```

### Branch mapping

Auto-sync flows from a core branch into one or more engine branches, but the version numbers do **not** correspond arithmetically — the mapping is explicit and must be read, not inferred (`core/v7.0` → `unity/v5.0`; `core/v7.2` → `unity/v5.1`; `core/v7.1` → `unreal/v2.3`). Each core branch declares its own downstream targets in the `matrix.branch` list of `.github/workflows/auto-sync-core.yml` *on that core branch*; that file is the only authoritative source. Check it before assuming any relationship.

**Version-support policy:** maintain the current and previous version per engine. That currently means Unity `v5.1` (current) + `v5.0` (previous) and Unreal `v2.3` (current) + `v2.2` (previous), with a ceiling of four core branches in rotation at once. Unity's two versions each have a core feed (`core/v7.2` → `v5.1`, `core/v7.0` → `v5.0`); Unreal keeps only `core/v7.1` → `v2.3` because the current docs landed recently enough that no prior core branch pertains to `v2.2` (it takes core-owned fixes by direct edit or cherry-pick). When a new release ships, retire the core branch feeding the version that falls out of the current/previous window along with its engine branch.

Two invariants worth holding in context:

- **Each engine branch is fed by at most one core branch** (the matrices are disjoint), so a core edit never reaches the same file from two directions and auto-sync cannot self-conflict across core branches.
- **Not every engine branch has a core feed.** Branches with none (currently `unreal/v2.2`) take core-owned fixes by direct edit or cherry-pick from core.

### Agent-instructions files: AGENTS.md (canonical) + CLAUDE.md (include)

Project instructions live in **`AGENTS.md`** so every agent reads them. Codex, Cursor, and other non-Claude tools read `AGENTS.md` by default and ignore `CLAUDE.md`; Claude Code reads `CLAUDE.md`. To serve both from one source without duplicated content, `AGENTS.md` holds the instructions and `CLAUDE.md` is a single Claude Code import line:

```
@AGENTS.md
```

Claude Code expands that `@`-import to pull in `AGENTS.md`, so both toolchains see the same instructions and there is nothing to drift. Edit `AGENTS.md`, never `CLAUDE.md` (the one-liner is fixed).

Both files live on every content branch so agents working from any worktree see project-specific instructions. `main` holds the canonical `AGENTS.md`; all edits land there first. There is no automation propagating `main` → other branches. These files are **not** core-owned paths, so they do not ride `auto-sync-core` (which syncs only `docs/cli/guides`, `docs/cli/SUMMARY.md`, `docs/includes`, and `docs/portal`) — including the auto-sync targets `unity/v5.0`, `unity/v5.1`, and `unreal/v2.3`, which receive core-owned content downstream but not these. After editing `AGENTS.md` on main, stamp it (and the one-line `CLAUDE.md`) onto each worktree branch in the same session:

```bash
for d in beamable-docs-core-7.0 beamable-docs-core-7.1 beamable-docs-core-7.2 \
         beamable-docs-unity-5.0 beamable-docs-unity-5.1 \
         beamable-docs-unreal-2.2 beamable-docs-unreal-2.3 \
         beamable-docs-internal beamable-docs-api-1.0 \
         beamable-docs-websdk-1.0; do
  cp ~/src/beamable/docs/AGENTS.md ~/src/beamable/$d/AGENTS.md
  cp ~/src/beamable/docs/CLAUDE.md ~/src/beamable/$d/CLAUDE.md
  git -C ~/src/beamable/$d add AGENTS.md CLAUDE.md
  git -C ~/src/beamable/$d commit -m "Sync AGENTS.md from main"
done
```

Push these commits per the **Staggered pushes** procedure.

`CLAUDE.md` is a static one-liner identical on every branch, so in practice only `AGENTS.md` changes. When the branches already match `main`, `git cherry-pick`-ing the main commit onto each branch is a cleaner-history alternative to the `cp` stamp — it preserves the original message and author, and applies without conflict. Fall back to the `cp` stamp if a branch has drifted. `unity/v4.0` is excluded from propagation: the files are gitignored there and the branch has no standing worktree.

## Setup

Requirements: Python 3.12, git-lfs

```sh
# Install Python dependencies
bash setup.sh
```

`setup.sh` installs: `mkdocs-material`, `mkdocs-glightbox`, `mkdocs-autorefs`, `mkdocs-literate-nav`, `mike`, `mkdocs-swagger-ui-tag`

`mkdocs-swagger-ui-tag` is required only by the `api/v1.0` branch (its `mkdocs.yml` declares the `swagger-ui-tag` plugin for the OpenAPI reference page). It is installed for every branch so `mkdocs build` works uniformly; without it, builds on `api/v1.0` abort with a plugin-not-installed configuration error.

## Common Commands

```sh
# Preview docs locally (run from a content branch, not main)
mkdocs serve
# Opens at http://127.0.0.1:8000/Docs/

# Build static site
mkdocs build
```

## Frontend Apps (`/apps/`)

Two standalone Svelte + Vite apps embedded in the docs site:

- `apps/login/` — Login application
- `apps/try-it-out/` — Interactive demo app

Each has its own `package.json`. Build and serve each independently:

```sh
cd apps/login   # or apps/try-it-out
npm install
npm run dev     # or npm run build
```

## Deployment

Deployment is triggered manually via GitHub Actions (`Deploy Docs Branch` workflow). Inputs required:

- `branch` — The content branch to deploy (e.g., `unity/v5.0`)
- `sdk` — SDK type (`Unity`, `Unreal`, or `WebSDK`)
- `version` — Version string (e.g., `5.0`)

The workflow runs `mike deploy "{sdk}-{version}" --push`, which publishes to `gh-pages` and is served at `https://beamable.github.io/Docs/`.

## PR Workflow

1. Check with Vitor Balbio (Slack) before deciding which branch a new page belongs on.
2. Create a feature branch from the relevant subject-specific branch (not `main`).
3. Open a PR and always add Balbio as a reviewer.

### Merge strategy

**Automated core→unity sync** is handled by `auto-sync-core.yml` on the core branch. It replaces the target branch's copy of the core-owned paths (`docs/cli/guides`, `docs/cli/SUMMARY.md`, `docs/includes`, `docs/portal`) with core's version wholesale, then commits and pushes directly — it never opens a PR. The overwrite is path-scoped and stateless (not a merge), so it is conflict-free by construction: there is no frozen merge base to re-diff against, and nothing to resolve by hand. An earlier design squash-merged first and opened a conflict PR (e.g. `merge-core/v7.0-into-unity/v5.0`) whenever the merge reported conflicts, but it flagged spurious conflicts far more often than real ones; the wholesale-copy has run cleanly since replacing it.

For **feature and fix PRs**, prefer **squash-and-merge**. These are typically single-author, single-topic changes; squashing produces a clean, readable log without noise from intermediate work-in-progress commits. This is a de facto habit, not enforced by tooling. (The core→unity sync no longer opens PRs, so the older "merge commit for conflict-resolution sync PRs" convention is obsolete.)

### Backporting

Copyediting and style changes (grammar, punctuation, passive voice, style consistency) apply only to `unity/v5.x` branches and newer, `unreal/v2.x` and newer, and the corresponding core branches. Do not backport these to `unity/v4.0` or earlier. Only backport factual corrections pertinent to that specific version (SDK/CLI version table entries, bug fix notes, feature corrections, etc.).

For **Unreal**, apply copyediting changes to `unreal/v2.2` immediately after finishing each item on `unreal/v2.3` — do not defer all `v2.2` work to the end of the session. Applying each change while context is fresh is faster and less error-prone than a bulk pass later. Exception: if a `v2.3` item is flagged for SDK-team verification (Priority 3), hold off on `v2.2` until the `v2.3` fix is confirmed.

## SDK Source References

When verifying API names, event names, Blueprint node names, or
other code-level details referenced in documentation, consult the
appropriate SDK source repository:

- **Unity SDK** — `beamable/BeamableProduct` on GitHub
- **Unreal SDK** — `beamable/UnrealSDK` on GitHub

Local checkout paths vary by machine; contributors should record
their own paths in personal memory or shell config.

## Navigation

Documentation navigation is defined by `SUMMARY.md` files (using `mkdocs-literate-nav` plugin) in each content branch.

## Auto-generated Content

Three sections must not be edited directly in Markdown — make changes upstream in their respective sources:

1. **CLI command reference** — `docs/cli/commands/cli-command-reference/`
2. **Web SDK docs**
3. **API docs**

Internal team documentation lives at `https://help.beamable.com/Internal/internal/documentation/introduction/` (deployed but not publicly advertised).

## Style Guide

- **Bullet lists and table entries:** no terminal periods, regardless of whether items are sentences or fragments
- **Relative clauses:** use "that" for restrictive clauses; use ", which" (with comma) for non-restrictive clauses; omit the pronoun entirely where the sentence allows
- **"which allows/enables" constructions:** rewrite as active alternatives (e.g., "letting downstream projects reuse...")
- **Passive voice:** prefer active/imperative in setup and configuration instructions where "you" is the actor; passive is acceptable when the actor is the system or a type constraint. Within active voice, use bare imperative for direct instructions and sequential steps; use "you can" when the sentence announces a capability or sits in the consequent of a conditional ("if your game does X, you can do Y")
- **Code terms in prose:** backtick-fence class names, method names, property names, and attribute names when referring to the code entity (e.g., `` `BeamContext` ``, `` `PlayerId` ``). For .NET attributes, use the consumer-facing short form without the `Attribute` suffix (e.g., `[IgnoreContentField]`, not `[IgnoreContentFieldAttribute]`). Exception: `MonoBehaviour` must preserve Unity's spelling with the `u` regardless of American English preference elsewhere.
- **American English spelling:** use American forms throughout (-ize, -ization, single-L in "canceling", "canceled", "modeling", etc.). Exception: `MonoBehaviour` (Unity API name; spelling is fixed).
- **Product term capitalization:** Portal, Cloud Save, Content Manager, Admin Console, Beam Library (capitalized); see commit history for resolved cases
- **`docs/includes/abbreviations.md`:** provides hover tooltips for TLAs across all pages. Omit "SDK" and "API" — they appear too frequently in these docs for a tooltip to add value, and the constant underline creates visual noise. Add an acronym only when a reader encountering it cold would benefit from the expansion.
- **Definition list bullets:** bold the term but not the colon — `**Term**: description` not `**Term:** description`
- **Heading capitalization:** Sentence case at all levels (H1–H4) — capitalize only the first word and proper nouns/product terms. Applies to `unity/v5.0` and newer, `unreal/v2.2` and newer, and the corresponding core branches; `unity/v4.0` and earlier remain on their original Title Case convention and are not being converted. `scripts/sentence_case_headings.py` on `main` is the maintained enforcement tool — run it from a content-branch worktree to convert any newly-added Title Case headings, and extend its `MULTI_WORD` / `SINGLE_WORD` whitelists when a new proper-noun term enters the docs. **Title Case rules for legacy branches (`unity/v4.0` and earlier):** capitalize by part of speech — verbs, nouns, adjectives, and adverbs capitalize; articles, coordinating conjunctions, and prepositions stay lowercase regardless of length (*across*, *between*, *against*, *without*, *throughout*, etc.); for dash-separated segments (e.g., `Advanced - Beyond Hooks`), the first word after the dash capitalizes regardless of part of speech.
- **Path separators:** prefer forward slashes in prose paths (e.g., `.beamable/temp/plans`), even when the path is conceptually on a Windows filesystem. Two exceptions where backslashes stay: (1) **verbatim CLI/shell transcripts** inside fenced code blocks — these reproduce what the tool actually prints on Windows, so altering them misrepresents the output; (2) **paths with an explicit Windows drive prefix** like `C:\Program Files\...` or `F:\UnrealToolchains\...` — the drive letter signals "this is a Windows path", and Windows readers expect backslashes when they see `C:\`. Forward-slashifying a `C:\`-prefixed path produces a hybrid (`C:/Program Files/...`) that looks wrong to everyone. Drive-prefixed paths and CLI transcripts: backslashes. Everything else: forward slashes.
- **Reference style guides:** Google Developer Documentation Style Guide and Microsoft Writing Style Guide

## Working with Claude Code

- **Audits:** When scanning docs for style, grammar, spelling, or formatting issues, enumerate all findings and present a summary — do not edit content files until explicitly asked to address specific items.
- **This file:** Treat this AGENTS.md as a living document shared among contributors and agentic assistants. Suggest additions proactively when workflow improvements, conventions, or hard-won context come up.

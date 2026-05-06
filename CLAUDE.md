# CLAUDE.md

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

## Working with Worktrees

Because content lives on many branches simultaneously, `git worktree` is the recommended workflow. Check out each branch into a sibling directory of the main `docs/` clone, embedding the SDK name and version in the path so multiple versions can coexist on disk at once.

Suggested naming convention (siblings of `docs/` under `~/src/beamable/`, or wherever you clone it):

```
beamable-docs-unity-5.0    → unity/v5.0
beamable-docs-unity-5.1    → unity/v5.1
beamable-docs-core-7.0     → core/v7.0
beamable-docs-core-7.1     → core/v7.1
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

After pushing to a core branch, immediately `git pull` in the corresponding unity and unreal worktrees. The `auto-sync-core.yml` action squash-merges core changes onto downstream branches on push; without pulling afterward, your next push to those branches will be rejected as non-fast-forward.

### CLI guide edits and shared includes

Files under `docs/cli/guides/`, `docs/includes/` (including `abbreviations.md`), and `docs/portal/` are core-owned and auto-synced into unity/unreal. Edit them only in the relevant core worktree — do not copy changes by hand, even during a copyediting pass on a unity or unreal branch. Unity-only edits go directly to the unity worktree; Unreal-only edits (anything not in `docs/cli/guides/`, `docs/includes/`, or `docs/portal/`) go directly to the unreal worktree.

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

for i in "${!to_push[@]}"; do
  echo; echo "Pushing $(basename "${to_push[$i]}")..."
  git -C "${to_push[$i]}" push
  [[ $i -ge 1 && $i -lt $((${#to_push[@]} - 1)) ]] && echo "Waiting 2 minutes..." && sleep 120
done
echo; echo "All pushes complete."
```

### Branch mapping

The authoritative source is `.github/workflows/auto-sync-core.yml` on the core branch — verify there before assuming any auto-merge relationship.

| Core branch | Unity branch | Unreal branch | Notes |
|---|---|---|---|
| `core/v7.0` | `unity/v5.0` | `unreal/v2.3` | Auto-sync active |
| `core/v7.1` | — | `unreal/v2.3` | Auto-sync to unreal only |
| — | `unity/v5.1` | — | No auto-merge from any core branch; apply CLI guide fixes directly or cherry-pick from core |

## Setup

Requirements: Python 3.12, git-lfs

```sh
# Install Python dependencies
bash setup.sh
```

`setup.sh` installs: `mkdocs-material`, `mkdocs-glightbox`, `mkdocs-autorefs`, `mkdocs-literate-nav`, `mike`

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

**Automated core→unity sync** is handled by `auto-sync-core.yml` on the core branch. On a clean merge it squash-merges directly onto the target branch and pushes without opening a PR. It only opens a PR (e.g. `merge-core/v7.0-into-unity/v5.0`) when there are conflicts that need human review.

When landing a **conflict-resolution sync PR**, prefer **merge commit** over squash. The merge commit preserves the sync boundary in history and makes it possible to see at a glance which commits originated on core and which were added to resolve conflicts. Squashing would fold that signal into a single anonymous commit.

For **feature and fix PRs**, prefer **squash-and-merge**. These are typically single-author, single-topic changes; squashing produces a clean, readable log without noise from intermediate work-in-progress commits.

Neither convention is enforced by tooling — both are de facto habits. When in doubt, ask: "does the history of *how* this landed matter?" If yes, merge commit; if no, squash.

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
- **Reference style guides:** Google Developer Documentation Style Guide and Microsoft Writing Style Guide

## Working with Claude Code

- **Audits:** When scanning docs for style, grammar, spelling, or formatting issues, enumerate all findings and present a summary — do not edit content files until explicitly asked to address specific items.
- **This file:** Treat this CLAUDE.md as a living document shared among contributors and agentic assistants. Suggest additions proactively when workflow improvements, conventions, or hard-won context come up.

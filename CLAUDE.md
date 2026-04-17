# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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

## Navigation

Documentation navigation is defined by `SUMMARY.md` files (using `mkdocs-literate-nav` plugin) in each content branch.

## Style Guide

- **Bullet lists and table entries:** no terminal periods, regardless of whether items are sentences or fragments
- **Relative clauses:** use "that" for restrictive clauses; use ", which" (with comma) for non-restrictive clauses; omit the pronoun entirely where the sentence allows
- **"which allows/enables" constructions:** rewrite as active alternatives (e.g., "letting downstream projects reuse...")
- **Passive voice:** prefer active/imperative in setup and configuration instructions where "you" is the actor; passive is acceptable when the actor is the system or a type constraint. Within active voice, use bare imperative for direct instructions and sequential steps; use "you can" when the sentence announces a capability or sits in the consequent of a conditional ("if your game does X, you can do Y")
- **Code terms in prose:** backtick-fence class names, method names, property names, and attribute names when referring to the code entity (e.g., `` `BeamContext` ``, `` `PlayerId` ``). For .NET attributes, use the consumer-facing short form without the `Attribute` suffix (e.g., `[IgnoreContentField]`, not `[IgnoreContentFieldAttribute]`). Exception: `MonoBehaviour` must preserve Unity's spelling with the `u` regardless of American English preference elsewhere.
- **American English spelling:** use American forms throughout (-ize, -ization, single-L in "canceling", "canceled", "modeling", etc.). Exception: `MonoBehaviour` (Unity API name; spelling is fixed).
- **Product term capitalization:** Portal, Cloud Save, Content Manager, Admin Console, Beam Library (capitalized); see commit history for resolved cases
- **Reference style guides:** Google Developer Documentation Style Guide and Microsoft Writing Style Guide

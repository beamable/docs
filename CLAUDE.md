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
- `internal` — Internal Beamable guides
- `gh-pages` — GitHub Pages deployment target (do not edit directly)

To edit documentation, switch to the appropriate versioned branch before making changes.

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

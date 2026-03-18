# Auto-Publish Workflow Requirements

## Overview

A GitHub Actions workflow that automatically re-publishes Unity SDK documentation whenever a push is made to a `unity/<version>` branch — but **only if that version has already been published** via `mike`. This prevents accidental publishing of in-progress or unreleased documentation branches.

## Trigger

- **Event:** `push`
- **Branch pattern:** `unity/**` (matches any `unity/<version>` branch, e.g. `unity/v5.0`, `unity/v4.0`)
- **Scope:** Unity branches only. Other SDKs (Unreal, WebSDK) are out of scope for now.

## Core Logic

1. **Extract the version** from the pushed branch name (e.g. `unity/v5.0` → version = `v5.0`).
2. **Check whether `Unity-<version>` is already published** by reading `versions.json` from the `gh-pages` branch.
   - Mike maintains a `versions.json` file in `gh-pages` that lists all published version aliases.
   - The check is **case-insensitive** — e.g. `unity-v5.0` and `Unity-v5.0` are treated as the same.
   - If the version is **not** found in `versions.json`, the workflow exits silently (no deploy, no failure).
3. **If the version is already published**, re-deploy it using `mike deploy`, following the same steps as `deploy-branch.yml`.
4. **Post a Slack notification** after a successful deploy. No notification is sent for skipped deploys.

## Mike Version Key Convention

Published versions follow the pattern `Unity-<version>` (e.g. `Unity-v5.0`). The lookup against `versions.json` must be case-insensitive.

## Deploy Steps (mirrors `deploy-branch.yml`)

When the version is confirmed as already published:

1. Run `setup.sh` to install Python dependencies.
2. Fetch all remote branches.
3. Checkout the `gh-pages` branch (required for mike to read existing version state).
4. Checkout the pushed `unity/<version>` branch.
5. Configure git identity for mike.
6. Run: `mike deploy "Unity-<version>" --push`
7. Post a Slack message indicating which branch and version were published.

## Slack Notification

- **When:** After a successful `mike deploy` only. Skipped runs (unpublished branch) produce no notification.
- **Content should include:** the branch name that was pushed, the mike alias that was updated (e.g. `Unity-v5.0`), and a link to the deployed docs.
- **Mechanism:** Slack incoming webhook, stored as a GitHub Actions secret (e.g. `SLACK_WEBHOOK_URL`).

## What This Workflow Must NOT Do

- Must **not** publish a branch that has never been manually published before.
- Must **not** fail or error when a push is made to an unpublished branch — it should simply skip the deploy and exit cleanly.
- Must **not** create new mike version aliases; it only updates existing ones.
- Must **not** send Slack notifications for skipped runs.

Contributing to the Beamable Documentation Repository
=====================================================

At present, the state of the `docs` repo is mutable and in flux.
Always check with Vitor Balbio on Slack before deciding where a
new page should go.

When making modifications and corrections, check with Balbio about
which branch to start from and then follow PR procedures:
1. Make a new branch starting from the relevant subject-specific branch.
2. Commit your changes to your new branch
3. Push your changes and open a PR
4. Get reviews. Balbio should always be a PR reviewer
5. When approved, squash-and-merge your changes. Feature and fix PRs here are
   typically single-author and single-topic, so squashing keeps the log readable
   without noise from intermediate work-in-progress commits

## Style Reference

Primary style references for prose and formatting decisions:

- [Google Developer Documentation Style Guide](https://developers.google.com/style)
- [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/)

Project-specific rules (heading capitalization, code term formatting, product name
capitalization, code fence language tokens, etc.) are documented in the Style Guide
section of [`AGENTS.md`](AGENTS.md) on this branch. `AGENTS.md` is the canonical
instructions file for both humans and agentic tools; `CLAUDE.md` is a one-line
import of it and should not be edited directly.

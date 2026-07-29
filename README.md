# Beamable Docs Repository

This is the unified repository for Beamable Docs. Documentation content lives on
versioned branches, not on `main` — `main` holds only the shared tooling, setup
scripts, and CI/CD configuration.

Content branches:

- `core/v*` — shared Beamable concepts (CLI guides, Portal); synced into the engine branches
- `unity/v*` — Unity SDK documentation
- `unreal/v*` — Unreal SDK documentation
- `websdk/v*` — Web SDK documentation
- `api/v*` — Beamable API documentation
- `toolkit/v*` — Beamable Toolkit and Console documentation (MicroViews)
- `internal` — Beamable internal documentation and guides (published, but not publicly advertised)

Infrastructure branches:

- `home` — builds the product-chooser landing page at `help.beamable.com/`. A newly published product line is not discoverable from the top of the site until it has a card here
- `gh-pages` — the GitHub Pages deployment target; do not edit directly

See [`AGENTS.md`](AGENTS.md) for the full branch architecture, the core-to-engine
sync rules, and the contribution conventions.

# Cloning and Installing Dependencies:
- Clone the main branch of this repo (make sure you have git-lfs installed).
- Install [Python 3.12](https://www.python.org/downloads/release/python-31210/)
- Run the setup.sh script in a bash terminal to install the dependencies.

# Running the Docs:
- Go to the branch you want to run (e.g. core, unreal, unity).
- In a terminal run "mkdocs serve" in the root of the repo to start a local server.
- Open the Serve link in your browser http://127.0.0.1:8000/Docs/

# Next Steps:
You will find more details about the process of editing, building and deploying documents in the "Internal" documentation on the [website](https://help.beamable.com/Internal/) or by running the `internal` branch locally.

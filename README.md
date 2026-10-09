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

## Crawl and agent discovery

`site-assets/publication-policy.json` classifies the product families allowed in
public discovery. The generator reads Mike's published `versions.json`, including
the actual Latest aliases, rather than inferring version numbers from branch names.
Add a new product family to this policy when promoting it, and add its chooser card
on `home`. Internal and the unreleased Toolkit stay outside public discovery.
Robots rules express crawl preferences; they do not protect these published pages.

Publishing workflows check out shared tooling into `tooling` and content into
`content`. Run Mike locally without `--push`, then use the shared publisher:

```shell
python tooling/scripts/publish-site-assets.py --repo content
python tooling/scripts/publish-site-assets.py --repo content --push
```

The first command validates in a temporary worktree without updating refs or pushing.
The second generates discovery assets, commits them alongside the local Mike output,
and pushes `gh-pages` once. It never force-pushes. All writers use the existing
`gh-pages-deploy` concurrency group and `DOCS_PAT`, which triggers the branch-based
Pages build. Dispatch **Publish Site Assets** from `main` to preview or refresh assets
without rebuilding an SDK. A relevant push to `main` refreshes assets automatically.

Generated resources include `/robots.txt`, `/sitemap.xml`, filtered per-version
sitemaps, `/agents/docs-index.json`, Markdown article copies, the Agent Skills index,
and the AI catalog. Home exposes WebMCP tools when the browser supports the API.
The documentation index lists concrete versions and canonical page URLs; `latest`
is `null` when Mike has no Latest alias for a product. Choose a version explicitly
in that case.

Historical HTML supplies exports without rebuilding frozen branches. Known obsolete
`beamable.github.io/Docs/` canonical links receive a hostname repair in generated
HTML; the source branches and original per-version sitemaps remain unchanged.
Generated sitemaps omit build-time `lastmod` values because they do not establish
when an article actually changed. The generated-files manifest removes stale exports
while preserving original HTML and unrelated published resources.

GitHub Pages serves `.md` exports as static files; they are **not** HTML content
negotiation. HTML discovery links are **not** HTTP `Link` headers. DNS-AID/DNSSEC,
an RFC 9727 API catalog with its required media type, authentication discovery,
`auth.md`, and an MCP server card require the appropriate infrastructure or actual
services and remain deferred. WebMCP does not advertise an MCP transport.

Run the checks with the pinned toolchain and Node.js:

```shell
python -m unittest discover -s tests/site-assets -p 'test_*.py'
node --test tests/site-assets/webmcp.test.cjs
```

After Pages finishes publishing, verify GET/HEAD status, content types, JSON CORS,
referenced sitemaps, skill digests, Markdown homepages, and homepage behavior:

```shell
python scripts/check-site-discovery.py
```

Merge shared tooling on `main` first and wait for **Publish Site Assets** and Pages
to finish. Then squash-and-merge the publishing integration PRs one at a time,
waiting for each publish and any core synchronization before merging the next.
The content PRs require the shared publisher on `main` and should not land first.

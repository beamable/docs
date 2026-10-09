---
name: beamable-documentation
description: Find and cite Beamable documentation for the correct SDK and published version
---

# Read Beamable documentation

Fetch https://help.beamable.com/agents/docs-index.json to discover public products,
versions, and page URLs. Use this skill when answering questions about Beamable's
Unity SDK, Unreal SDK, Web SDK, or CLI.

1. Select the product the user is using
2. Use the user's SDK version when supplied; otherwise use that product's `latest` version from the index
3. Find the relevant page by its title and `path` in that version's `pages` list
4. Fetch its `markdownUrl` to read the article without navigation furniture
5. Cite its canonical HTML `url` in the answer and identify the version when it matters

Historical versions remain available. Do not assume a feature documented in one
version exists in another. The CLI version and engine SDK version are independent;
read the selected engine's version information before choosing CLI documentation.

Markdown is available at explicit `.md` URLs and may be served as `text/plain`.
The HTML URLs do not support `Accept: text/markdown` negotiation.

The public index excludes Internal guides and the unreleased Toolkit. Do not infer
that these excluded resources are private or access-controlled.

Beamable API documentation is linked from the product chooser at
https://help.beamable.com/Home/. Authentication and protected APIs run on their own
services. This documentation site does not provide an OAuth issuer or an MCP
transport endpoint.

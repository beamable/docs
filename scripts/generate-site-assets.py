#!/usr/bin/env python3
"""Generate origin-root discovery assets from an existing Mike publication."""

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit

from bs4 import BeautifulSoup
from markdownify import markdownify

ASSETS = Path(__file__).resolve().parents[1] / "site-assets"
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", NS)
MARKER = re.compile(r"\n?<!-- beamable-discovery:start -->.*?<!-- beamable-discovery:end -->\n?", re.S)
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]*\Z")


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def safe_path(root, relative):
    path = root / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Unsafe publication path: {relative}")
    return path


def managed_path(path):
    return path in {"robots.txt", "sitemap.xml", "index.html", "Home/index.html", "agents/generated-files.json"} or (
        path.startswith(("markdown/", "sitemaps/", "agents/", ".well-known/agent-skills/"))
    ) or path == ".well-known/ai-catalog.json" or public_html(path)


def public_html(path):
    return bool(re.fullmatch(r"(?:Unity|Unreal|CLI|WebSDK)-[A-Za-z0-9_.-]+/.+\.html", path))


def canonical_url(url, policy):
    for prefix in policy.get("legacy_origins", []):
        if url.startswith(prefix):
            return policy["origin"] + "/" + url[len(prefix):]
    return url


def selected_versions(registry, policy):
    if not isinstance(registry, list) or not registry:
        raise ValueError("versions.json must be a nonempty array")
    selected, names, aliases = [], set(), set()
    for item in registry:
        name = item["version"]
        if not isinstance(name, str) or not NAME.fullmatch(name) or name in names:
            raise ValueError(f"Invalid or duplicate version: {name}")
        names.add(name)
        item_aliases = item.get("aliases", [])
        if not isinstance(item_aliases, list) or any(not isinstance(alias, str) or not NAME.fullmatch(alias) for alias in item_aliases):
            raise ValueError(f"Invalid aliases for {name}")
        if len(set(item_aliases)) != len(item_aliases) or aliases.intersection(item_aliases):
            raise ValueError(f"Duplicate alias for {name}")
        aliases.update(item_aliases)
        product = name.split("-", 1)[0]
        if item.get("properties", {}).get("hidden") or name in policy["excluded_versions"] or product in policy["excluded_products"]:
            continue
        if name not in policy["standalone_versions"] and product not in policy["products"]:
            raise ValueError(f"Classify new product {product} in publication-policy.json before publishing")
        if name not in policy["standalone_versions"] and "-" not in name:
            raise ValueError(f"Expected a versioned product: {name}")
        selected.append((product, item))
    if names.intersection(aliases):
        raise ValueError("An alias cannot also be a concrete version")
    if not selected:
        raise ValueError("No public versions selected")
    return sorted(selected, key=lambda value: value[1]["version"])


def robots(policy):
    lines = ["# Crawl preferences; these rules do not provide access control."]
    for agents in [["*"], ["OAI-SearchBot", "Claude-SearchBot", "PerplexityBot"]]:
        lines.append("")
        lines.extend(f"User-agent: {agent}" for agent in agents)
        lines.append("Content-Signal: search=yes, ai-input=yes, ai-train=no")
        lines.extend(f"Disallow: {path}" for path in policy["disallow_paths"])
        lines.append("Allow: /")
    lines.extend(["", "User-agent: GPTBot", "User-agent: ClaudeBot", "User-agent: Google-Extended", "Disallow: /", ""])
    lines.extend([f"Sitemap: {policy['origin']}/sitemap.xml", f"Agentmap: {policy['origin']}/.well-known/ai-catalog.json"])
    return ("\n".join(lines) + "\n").encode()


def xml_bytes(element):
    ET.indent(element)
    value = ET.tostring(element, encoding="utf-8", xml_declaration=True) + b"\n"
    if len(element) > 50000 or len(value) > 52428800:
        raise ValueError("Sitemap exceeds the protocol limits; split this version's sitemap")
    return value


def language(element):
    for node in [element, *element.parents]:
        for css_class in node.get("class", []):
            if css_class.startswith("language-"):
                return css_class[len("language-"):]
    code = element.find("code")
    if code:
        for css_class in code.get("class", []):
            if css_class.startswith("language-"):
                return css_class[len("language-"):]
    return "text"


def markdown_article(article, title, url):
    for element in article.select("script, style, .headerlink, .md-content__button, .md-clipboard, .linenos, .linenodiv"):
        element.decompose()
    for element in article.find_all(True):
        for attribute in ("href", "src", "poster"):
            if element.has_attr(attribute):
                element[attribute] = urljoin(url, element[attribute])
    # Pygments tables contain layout cells and line numbers, not Markdown tables.
    for table in article.select("table.highlighttable"):
        pre = table.find("pre", recursive=True)
        code_cell = table.select_one("td.code")
        if code_cell:
            pre = code_cell.find("pre")
        if pre:
            table.replace_with(pre.extract())
    for media in article.find_all(["video", "audio"]):
        source = media.get("src") or (media.find("source") or {}).get("src")
        if source:
            link = BeautifulSoup("", "html.parser").new_tag("a")
            link["href"] = source
            link.string = "Video" if media.name == "video" else "Audio"
            media.replace_with(link)
    body = markdownify(str(article), heading_style="ATX", newline_style="BACKSLASH", code_language_callback=language)
    body = "\n".join(line.rstrip() for line in body.splitlines()).strip()
    metadata = f"---\ntitle: {json.dumps(title, ensure_ascii=False)}\ncanonical_url: {json.dumps(url)}\n---\n\n"
    return (metadata + body + "\n").encode()


def discovery_html(html, markdown_url, webmcp=False):
    html = MARKER.sub("", html)
    lines = ["<!-- beamable-discovery:start -->",
             '<link rel="sitemap" type="application/xml" href="/sitemap.xml">',
             '<link rel="ai-catalog" href="/.well-known/ai-catalog.json">',
             f'<link rel="alternate" type="text/markdown" href="{markdown_url}">']
    if webmcp:
        lines.append('<script src="/agents/webmcp.js" defer></script>')
    lines.append("<!-- beamable-discovery:end -->")
    if not re.search(r"</head\s*>", html, re.I):
        raise ValueError("Homepage has no closing head element")
    return re.sub(r"</head\s*>", lambda match: "\n" + "\n".join(lines) + "\n" + match[0], html, count=1, flags=re.I).encode()


def page_records(site, version, policy, write):
    origin = policy["origin"]
    sitemap = safe_path(site, f"{version}/sitemap.xml")
    if not sitemap.is_file():
        raise ValueError(f"Missing sitemap for public version {version}")
    tree = ET.parse(sitemap).getroot()
    if tree.tag != f"{{{NS}}}urlset":
        raise ValueError(f"Expected a urlset in {sitemap}")
    seen = set()
    for entry in tree:
        original_url = entry.findtext(f"{{{NS}}}loc")
        if not original_url:
            raise ValueError(f"Missing sitemap URL in {sitemap}")
        url = canonical_url(original_url, policy)
        parsed = urlsplit(url)
        if f"{parsed.scheme}://{parsed.netloc}" != origin or parsed.query or parsed.fragment or not parsed.path.startswith(f"/{version}/"):
            raise ValueError(f"Noncanonical sitemap URL: {url}")
        relative = unquote(parsed.path.lstrip("/"))
        components = Path(relative).parts
        if any(part.casefold() in {"summary", "summary.html", "includes"} for part in components):
            continue
        html_path = relative + "index.html" if relative.endswith("/") else relative
        file = safe_path(site, html_path)
        if not file.is_file():
            continue
        html = file.read_text(encoding="utf-8-sig")
        head_match = re.search(r"<head\b[^>]*>(.*?)</head\s*>", html, re.I | re.S)
        article_match = re.search(r"<article\b[^>]*>.*?</article\s*>", html, re.I | re.S)
        if not head_match:
            raise ValueError(f"Missing HTML head: {html_path}")
        head = BeautifulSoup(head_match[1], "html.parser")
        if head.find("meta", attrs={"http-equiv": re.compile("refresh", re.I)}):
            continue
        canonical = head.find("link", rel="canonical")
        if not canonical or canonical_url(canonical.get("href", ""), policy) != url:
            raise ValueError(f"Canonical link does not match sitemap: {html_path}")
        if original_url != url:
            # Factual hostname repair in generated output only. Preserve the
            # frozen branch, original sitemap, and all other page markup.
            canonical_tag = re.search(r'<link\b(?=[^>]*\brel=[\"\']canonical[\"\'])[^>]*>', head_match[1], re.I)
            if not canonical_tag:
                raise ValueError(f"Cannot repair legacy canonical link: {html_path}")
            tag = canonical_tag[0]
            new_tag = re.sub(r'(\bhref=[\"\'])[^\"\']*([\"\'])', lambda match: match[1] + url + match[2], tag, count=1, flags=re.I)
            repaired_head = head_match[1].replace(tag, new_tag, 1)
            write(html_path, (html[:head_match.start(1)] + repaired_head + html[head_match.end(1):]).encode())
        if not article_match:
            raise ValueError(f"Missing article: {html_path}")
        if url in seen:
            continue
        seen.add(url)
        article = BeautifulSoup(article_match[0], "html.parser").article
        title = article.find("h1")
        title = (title.get_text(" ", strip=True).removesuffix("¶") if title else head.title.get_text(strip=True)).strip()
        page_path = parsed.path[len(f"/{version}/"):]
        markdown_path = "markdown/" + html_path.removesuffix(".html") + ".md"
        yield {"path": page_path, "title": title.strip(), "url": url,
               "markdownUrl": f"{origin}/{quote(markdown_path, safe='/')}"}, markdown_path, markdown_article(article, title, url)


def build_assets(site, output, assets=ASSETS):
    policy = json.loads((assets / "publication-policy.json").read_text())
    origin = policy["origin"]
    if not re.fullmatch(r"https://[a-zA-Z0-9.-]+", origin):
        raise ValueError("Publication origin must be an HTTPS origin without a path")
    if not (site / ".nojekyll").is_file():
        raise ValueError(".nojekyll is required to serve .well-known on GitHub Pages")
    registry = json.loads((site / "versions.json").read_text())
    selected = selected_versions(registry, policy)
    generated = []

    def write(relative, data):
        if not managed_path(relative):
            raise ValueError(f"Unmanaged output path: {relative}")
        file = safe_path(output, relative)
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(data)
        generated.append(relative)

    index = {"schemaVersion": 1, "origin": origin, "products": []}
    products = {}
    sitemap_index = ET.Element(f"{{{NS}}}sitemapindex")
    for product, item in selected:
        version = item["version"]
        pages = []
        sitemap = ET.Element(f"{{{NS}}}urlset")
        for record, markdown_path, markdown in page_records(site, version, policy, write):
            pages.append(record)
            write(markdown_path, markdown)
        pages.sort(key=lambda page: page["url"])
        if not pages or not any(page["path"] == "" for page in pages):
            raise ValueError(f"Public version {version} needs an indexed homepage")
        for page in pages:
            ET.SubElement(ET.SubElement(sitemap, f"{{{NS}}}url"), f"{{{NS}}}loc").text = page["url"]
        # Mike's lastmod normally reflects the build date, not an article change.
        # Omit it rather than advertising every page as changed on each publish.
        sitemap_path = f"sitemaps/{version}.xml"
        write(sitemap_path, xml_bytes(sitemap))
        ET.SubElement(ET.SubElement(sitemap_index, f"{{{NS}}}sitemap"), f"{{{NS}}}loc").text = f"{origin}/{sitemap_path}"
        group = products.setdefault(product, {"name": product, "latest": None, "versions": []})
        if f"{product}-Latest" in item.get("aliases", []) or version in policy["standalone_versions"]:
            if group["latest"]:
                raise ValueError(f"Multiple Latest mappings for {product}")
            group["latest"] = version
        homepage = next(page for page in pages if not page["path"])
        group["versions"].append({"version": version, "url": homepage["url"], "markdownUrl": homepage["markdownUrl"], "pages": pages})
        print(f"{version}: {len(pages)} public pages", flush=True)
    index["products"] = [products[name] for name in sorted(products)]
    write("agents/docs-index.json", json_bytes(index))
    write("robots.txt", robots(policy))
    write("sitemap.xml", xml_bytes(sitemap_index))
    skill = (assets / "beamable-documentation/SKILL.md").read_bytes()
    skill_path = ".well-known/agent-skills/beamable-documentation/SKILL.md"
    write(skill_path, skill)
    write(".well-known/agent-skills/index.json", json_bytes({
        "$schema": "https://schemas.agentskills.io/discovery/0.2.0/schema.json",
        "skills": [{"name": "beamable-documentation", "type": "skill-md",
                    "description": "Find and cite Beamable documentation for the correct SDK and published version",
                    "url": f"{origin}/{skill_path}", "digest": "sha256:" + hashlib.sha256(skill).hexdigest()}]
    }))
    catalog_entries = []
    for name, title, media_type, url, queries in [
        ("documentation", "Beamable public documentation index", "application/json", "/agents/docs-index.json", ["Find Beamable Unity documentation", "Which Beamable CLI versions are published?"]),
        ("documentation-skill", "Read and cite Beamable documentation", "text/markdown", f"/{skill_path}", ["Read Beamable docs for my SDK version", "Cite the Unreal SDK documentation"])
    ]:
        catalog_entries.append({"identifier": f"urn:air:help.beamable.com:docs:{name}", "displayName": title,
                                "type": media_type, "url": origin + url, "representativeQueries": queries})
    write(".well-known/ai-catalog.json", json_bytes({"specVersion": "1.0", "host": {
        "displayName": "Beamable documentation", "identifier": "urn:air:help.beamable.com:host:documentation"}, "entries": catalog_entries}))
    if "Home" in products:
        markdown_url = "/markdown/Home/index.md"
        write("index.html", discovery_html((assets / "index.html").read_text(), markdown_url))
        write("Home/index.html", discovery_html((site / "Home/index.html").read_text(encoding="utf-8-sig"), markdown_url, webmcp=True))
        write("agents/webmcp.js", (assets / "webmcp.js").read_bytes())
    else:
        raise ValueError("Home must be published before generating discovery assets")
    write("agents/generated-files.json", json_bytes(sorted([*generated, "agents/generated-files.json"])))
    return generated


def generate(site, assets=ASSETS, dry_run=False):
    site = Path(site).resolve()
    previous_file = site / "agents/generated-files.json"
    previous = json.loads(previous_file.read_text()) if previous_file.exists() else []
    if not isinstance(previous, list) or any(not isinstance(path, str) or not managed_path(path) for path in previous):
        raise ValueError("Invalid generated-files manifest")
    for path in previous:
        safe_path(site, path)
    with tempfile.TemporaryDirectory(prefix="beamable-discovery-") as directory:
        output = Path(directory)
        files = build_assets(site, output, assets)
        # Canonical repairs are original public HTML, never disposable exports.
        removed = sorted(path for path in set(previous) - set(files) if not public_html(path))
        changed = [path for path in files if not safe_path(site, path).is_file() or safe_path(site, path).read_bytes() != (output / path).read_bytes()]
        if not dry_run:
            for path in changed:
                target = safe_path(site, path)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(output / path, target)
            for path in removed:
                safe_path(site, path).unlink(missing_ok=True)
        print(f"{'Preview' if dry_run else 'Generated'}: {len(changed)} changed, {len(removed)} removed", flush=True)
        return changed, removed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path, help="Checkout of the combined published tree")
    parser.add_argument("--dry-run", action="store_true", help="Validate and report without changing the tree")
    arguments = parser.parse_args()
    generate(arguments.site, dry_run=arguments.dry_run)

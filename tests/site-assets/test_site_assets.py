import contextlib
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.robotparser import RobotFileParser

ROOT = Path(__file__).resolve().parents[2]


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


assets = load("assets", "generate-site-assets.py")
publisher = load("publisher", "publish-site-assets.py")
checker = load("checker", "check-site-discovery.py")
ORIGIN = "https://help.beamable.com"


def put(site, relative, text):
    target = site / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text)


def page(site, version, path="", legacy=False, content=None):
    url = f"{ORIGIN}/{version}/{path}"
    canonical = url.replace(ORIGIN + "/", "https://beamable.github.io/Docs/") if legacy else url
    put(site, f"{version}/{path}index.html", f'''<!DOCTYPE html><html><head>
<title>Example</title><link rel="canonical" href="{canonical}"></head><body>
<nav>Do not export navigation</nav><article class="md-content__inner"><h1>Example</h1>
{content or '<p>Public article</p>'}</article></body></html>''')
    return canonical


def fixture(site):
    put(site, ".nojekyll", "")
    put(site, "CNAME", "help.beamable.com")
    put(site, "unrelated.txt", "keep this")
    registry = []
    for name in ["Home", "Unity-1.0", "Unity-2.0", "CLI-7.0", "Unreal-2.3", "WebSDK-1.0", "Internal", "Toolkit-0.4"]:
        aliases = ["Unity-Latest"] if name == "Unity-2.0" else []
        if name in ["CLI-7.0", "Unreal-2.3", "WebSDK-1.0"]:
            aliases = [name.split("-")[0] + "-Latest"]
        item = {"version": name, "title": name, "aliases": aliases}
        if name == "Internal":
            item["properties"] = {"hidden": True}
        registry.append(item)
        urls = [page(site, name, legacy=name == "CLI-7.0")]
        if name == "Unity-2.0":
            urls.extend([page(site, name, "guide/", content='''<h2>Setup</h2>
<div class="admonition"><p class="admonition-title">Note</p><p>Important text</p></div>
<div class="language-csharp highlight"><pre><code>Console.WriteLine("hello");\n</code></pre></div>
<table><thead><tr><th>Key</th><th>Value</th></tr></thead><tbody><tr><td>SDK</td><td>2.0</td></tr></tbody></table>
<p><a href="../">Home</a><img src="../image.png" alt="Diagram"></p>'''),
                         page(site, name, "SUMMARY/"), page(site, name, "includes/example/"), f"{ORIGIN}/{name}/missing/"])
            redirect = page(site, name, "redirect/")
            put(site, f"{name}/redirect/index.html", '<html><head><meta http-equiv="refresh" content="0;url=../"></head></html>')
            urls.extend([redirect, urls[0]])
        tree = ET.Element(f"{{{assets.NS}}}urlset")
        for url in urls:
            entry = ET.SubElement(tree, f"{{{assets.NS}}}url")
            ET.SubElement(entry, f"{{{assets.NS}}}loc").text = url
            ET.SubElement(entry, f"{{{assets.NS}}}lastmod").text = "2026-10-09"
        put(site, f"{name}/sitemap.xml", ET.tostring(tree, encoding="unicode"))
    put(site, "versions.json", json.dumps(registry))
    put(site, "index.html", '<html><head></head><body>Old redirect</body></html>')


def generate(site, **kwargs):
    with contextlib.redirect_stdout(io.StringIO()):
        return assets.generate(site, **kwargs)


def run(repo, *args):
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True)
    return result.stdout.strip()


class GenerationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.site = Path(self.tmp.name)
        fixture(self.site)

    def test_crawl_groups_and_content_signals(self):
        generate(self.site)
        text = (self.site / "robots.txt").read_text()
        robot = RobotFileParser()
        robot.parse(text.splitlines())
        for agent in ["Googlebot", "OAI-SearchBot", "Claude-SearchBot", "PerplexityBot"]:
            self.assertTrue(robot.can_fetch(agent, ORIGIN + "/Unity-2.0/"))
            for path in ["/Internal/", "/Toolkit-0.4/", "/site/"]:
                self.assertFalse(robot.can_fetch(agent, ORIGIN + path))
        for agent in ["GPTBot", "ClaudeBot", "Google-Extended"]:
            self.assertFalse(robot.can_fetch(agent, ORIGIN + "/Unity-2.0/"))
        self.assertEqual(text.count("Content-Signal: search=yes, ai-input=yes, ai-train=no"), 2)
        self.assertIn(f"Sitemap: {ORIGIN}/sitemap.xml", text)

    def test_exports_filtering_and_discovery(self):
        generate(self.site)
        index = json.loads((self.site / "agents/docs-index.json").read_text())
        self.assertEqual({p["name"] for p in index["products"]}, {"Home", "Unity", "Unreal", "WebSDK", "CLI"})
        unity = next(p for p in index["products"] if p["name"] == "Unity")
        self.assertEqual(unity["latest"], "Unity-2.0")
        latest = next(v for v in unity["versions"] if v["version"] == "Unity-2.0")
        self.assertEqual([p["path"] for p in latest["pages"]], ["", "guide/"])
        markdown = (self.site / "markdown/Unity-2.0/guide/index.md").read_text()
        for expected in ["canonical_url:", "## Setup", "Important text", "```csharp", 'Console.WriteLine("hello");', "| Key | Value |", f"{ORIGIN}/Unity-2.0/image.png"]:
            self.assertIn(expected, markdown)
        self.assertNotIn("Do not export navigation", markdown)
        sitemap = (self.site / "sitemaps/Unity-2.0.xml").read_text()
        for omitted in ["SUMMARY", "includes", "missing", "redirect", "Latest", "lastmod"]:
            self.assertNotIn(omitted, sitemap)
        self.assertNotIn("markdown", (self.site / "sitemap.xml").read_text())
        self.assertFalse((self.site / "markdown/Internal").exists())
        skill_index = json.loads((self.site / ".well-known/agent-skills/index.json").read_text())
        skill = (self.site / ".well-known/agent-skills/beamable-documentation/SKILL.md").read_bytes()
        self.assertEqual(skill_index["skills"][0]["digest"], "sha256:" + hashlib.sha256(skill).hexdigest())
        catalog = json.loads((self.site / ".well-known/ai-catalog.json").read_text())
        for entry in catalog["entries"]:
            self.assertTrue(entry["identifier"].startswith("urn:air:help.beamable.com:"))
            self.assertEqual(sum(key in entry for key in ["url", "data"]), 1)
            self.assertTrue(2 <= len(entry["representativeQueries"]) <= 5)
        self.assertIn("/agents/webmcp.js", (self.site / "Home/index.html").read_text())

    def test_legacy_hostname_repairs_are_idempotent(self):
        source = (self.site / "CLI-7.0/sitemap.xml").read_bytes()
        generate(self.site)
        self.assertIn(f'href="{ORIGIN}/CLI-7.0/"', (self.site / "CLI-7.0/index.html").read_text())
        self.assertEqual(source, (self.site / "CLI-7.0/sitemap.xml").read_bytes())
        self.assertEqual(generate(self.site), ([], []))
        self.assertEqual((self.site / "unrelated.txt").read_text(), "keep this")

    def test_dry_run_and_failed_generation_do_not_change_site(self):
        before = {str(p.relative_to(self.site)): p.read_bytes() for p in self.site.rglob("*") if p.is_file()}
        generate(self.site, dry_run=True)
        after = {str(p.relative_to(self.site)): p.read_bytes() for p in self.site.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        put(self.site, "Unity-2.0/index.html", '<html><head><link rel="canonical" href="https://wrong.example/"></head></html>')
        with self.assertRaisesRegex(ValueError, "Canonical"):
            generate(self.site)
        self.assertFalse((self.site / "robots.txt").exists())

    def test_invalid_registry_and_inputs(self):
        registry = json.loads((self.site / "versions.json").read_text())
        policy = json.loads((assets.ASSETS / "publication-policy.json").read_text())
        with self.assertRaisesRegex(ValueError, "Classify"):
            assets.selected_versions([*registry, {"version": "NewSDK-1.0"}], policy)
        with self.assertRaisesRegex(ValueError, "Duplicate alias"):
            assets.selected_versions([*registry, {"version": "Unity-3.0", "aliases": ["Unity-Latest"]}], policy)
        with self.assertRaisesRegex(ValueError, "Unsafe"):
            assets.safe_path(self.site, "../escape")
        (self.site / "Unreal-2.3/sitemap.xml").unlink()
        with self.assertRaisesRegex(ValueError, "Missing sitemap"):
            generate(self.site)

    def test_stale_exports_removed_but_original_pages_preserved(self):
        generate(self.site)
        registry = json.loads((self.site / "versions.json").read_text())
        registry = [item for item in registry if item["version"] != "CLI-7.0"]
        put(self.site, "versions.json", json.dumps(registry))
        generate(self.site)
        self.assertFalse((self.site / "markdown/CLI-7.0/index.md").exists())
        self.assertTrue((self.site / "CLI-7.0/index.html").exists())

    def test_xml_escaping_and_corrupt_sitemap(self):
        root = ET.Element(f"{{{assets.NS}}}urlset")
        ET.SubElement(ET.SubElement(root, f"{{{assets.NS}}}url"), f"{{{assets.NS}}}loc").text = ORIGIN + "/a&b/"
        self.assertIn(b"a&amp;b", assets.xml_bytes(root))
        put(self.site, "Home/sitemap.xml", "invalid XML")
        with self.assertRaises(ET.ParseError):
            generate(self.site)

    def test_post_publish_checker_checks_head_and_cors(self):
        generate(self.site)
        methods = []

        def request(method, url, **kwargs):
            from urllib.parse import urlsplit
            import requests
            path = urlsplit(url).path.lstrip("/")
            if not path or path.endswith("/"):
                path += "index.html"
            response = requests.Response()
            response.status_code = 200
            response._content = (self.site / path).read_bytes()
            media_type = {".html": "text/html", ".json": "application/json", ".xml": "application/xml"}.get(Path(path).suffix, "text/plain")
            response.headers.update({"Content-Type": media_type, "Access-Control-Allow-Origin": "*"})
            methods.append(method)
            return response

        with patch.object(checker.requests.Session, "request", side_effect=request), contextlib.redirect_stdout(io.StringIO()):
            checker.check()
        self.assertEqual(methods.count("GET"), methods.count("HEAD"))

        def no_cors(method, url, **kwargs):
            response = request(method, url, **kwargs)
            response.headers.pop("Access-Control-Allow-Origin")
            return response

        with patch.object(checker.requests.Session, "request", side_effect=no_cors):
            with self.assertRaisesRegex(ValueError, "CORS"):
                checker.check()


class PublicationTests(unittest.TestCase):
    def test_mike_deploy_alias_and_single_combined_push(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo, remote = root / "repo", root / "remote.git"
            repo.mkdir()
            run(repo, "init", "-b", "gh-pages")
            run(repo, "config", "user.name", "Test")
            run(repo, "config", "user.email", "test@example.com")
            fixture(repo)
            run(repo, "add", ".")
            run(repo, "commit", "-m", "Existing public site")
            subprocess.run(["git", "init", "--bare", str(remote)], capture_output=True, check=True)
            run(repo, "remote", "add", "origin", str(remote))
            run(repo, "push", "origin", "gh-pages")
            hook = remote / "hooks/post-receive"
            hook.write_text('#!/bin/sh\ncat >> "$(dirname "$0")/pushes"\n')
            hook.chmod(0o755)
            initial = run(remote, "rev-parse", "gh-pages")
            with contextlib.redirect_stdout(io.StringIO()):
                publisher.publish(repo)
            self.assertEqual(initial, run(repo, "rev-parse", "gh-pages"))
            self.assertEqual(initial, run(remote, "rev-parse", "gh-pages"))
            self.assertFalse((remote / "hooks/pushes").exists())
            run(repo, "switch", "-c", "content")
            put(repo, "mkdocs.yml", 'site_name: Test\nsite_url: https://help.beamable.com/\ntheme:\n  name: material\nplugins:\n  - mike\n')
            put(repo, "docs/index.md", "# New release\n\nNew public documentation\n")
            run(repo, "add", "mkdocs.yml", "docs")
            run(repo, "commit", "-m", "New content")
            environment = {**os.environ, "PATH": str(Path(sys.executable).parent) + os.pathsep + os.environ["PATH"]}
            result = subprocess.run([str(Path(sys.executable).with_name("mike")), "deploy", "Unity-3.0"], cwd=repo, capture_output=True, text=True, env=environment)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(initial, run(remote, "rev-parse", "gh-pages"))
            with contextlib.redirect_stdout(io.StringIO()):
                publisher.publish(repo, push=True)
            self.assertEqual(len((remote / "hooks/pushes").read_text().splitlines()), 1)
            tree = run(remote, "ls-tree", "-r", "--name-only", "gh-pages")
            for path in ["Unity-3.0/index.html", "markdown/Unity-3.0/index.md", "robots.txt", "unrelated.txt"]:
                self.assertIn(path, tree)
            result = subprocess.run([str(Path(sys.executable).with_name("mike")), "alias", "--update-aliases", "Unity-3.0", "Unity-Latest"], cwd=repo, capture_output=True, text=True, env=environment)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with contextlib.redirect_stdout(io.StringIO()):
                publisher.publish(repo, push=True)
            index = json.loads(run(remote, "show", "gh-pages:agents/docs-index.json"))
            unity = next(p for p in index["products"] if p["name"] == "Unity")
            self.assertEqual(unity["latest"], "Unity-3.0")
            self.assertEqual(len((remote / "hooks/pushes").read_text().splitlines()), 2)
            competitor = root / "competitor"
            subprocess.run(["git", "clone", "--branch", "gh-pages", str(remote), str(competitor)], check=True, capture_output=True)
            run(competitor, "config", "user.name", "Other writer")
            run(competitor, "config", "user.email", "other@example.com")
            put(competitor, "other-writer.txt", "preserve concurrent publication")
            run(competitor, "add", ".")
            run(competitor, "commit", "-m", "Concurrent publication")
            run(competitor, "push", "origin", "gh-pages")
            remote_head = run(remote, "rev-parse", "gh-pages")
            with self.assertRaises(subprocess.CalledProcessError), contextlib.redirect_stdout(io.StringIO()):
                publisher.publish(repo, push=True)
            self.assertEqual(remote_head, run(remote, "rev-parse", "gh-pages"))
            self.assertIn("other-writer.txt", run(remote, "ls-tree", "--name-only", "gh-pages"))


if __name__ == "__main__":
    unittest.main()

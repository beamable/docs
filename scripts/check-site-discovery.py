#!/usr/bin/env python3
"""Verify public discovery endpoints after GitHub Pages finishes deployment."""

import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit

import requests


def check(origin="https://help.beamable.com"):
    session = requests.Session()
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

    def fetch(path, types, cors=False):
        url = path if path.startswith("https://") else origin + path
        if urlsplit(url).netloc != urlsplit(origin).netloc:
            raise ValueError(f"Unexpected discovery host: {url}")
        for method in ["HEAD", "GET"]:
            response = session.request(method, url, timeout=30, allow_redirects=False)
            if response.status_code != 200:
                raise ValueError(f"{method} {url}: expected 200, got {response.status_code}")
            media_type = response.headers.get("Content-Type", "").split(";", 1)[0]
            if media_type not in types:
                raise ValueError(f"{url}: unexpected Content-Type {media_type}")
            if cors and response.headers.get("Access-Control-Allow-Origin") != "*":
                raise ValueError(f"{url}: missing public CORS header")
        return response

    robots = fetch("/robots.txt", {"text/plain"}).text
    if f"Sitemap: {origin}/sitemap.xml" not in robots:
        raise ValueError("robots.txt does not reference the root sitemap")
    sitemaps = ET.fromstring(fetch("/sitemap.xml", {"application/xml", "text/xml"}).content)
    if sitemaps.tag != namespace + "sitemapindex":
        raise ValueError("Expected a sitemap index")
    for entry in sitemaps:
        url = entry.findtext(namespace + "loc")
        tree = ET.fromstring(fetch(url, {"application/xml", "text/xml"}).content)
        if tree.tag != namespace + "urlset":
            raise ValueError(f"Expected a URL sitemap: {url}")
    skills = fetch("/.well-known/agent-skills/index.json", {"application/json"}, cors=True).json()
    for skill in skills["skills"]:
        content = fetch(skill["url"], {"text/plain", "text/markdown"}).content
        if skill["digest"] != "sha256:" + hashlib.sha256(content).hexdigest():
            raise ValueError(f"Skill digest mismatch: {skill['name']}")
    catalog = fetch("/.well-known/ai-catalog.json", {"application/json"}, cors=True).json()
    if not catalog.get("entries"):
        raise ValueError("AI catalog has no entries")
    index = fetch("/agents/docs-index.json", {"application/json"}, cors=True).json()
    versions = 0
    for product in index["products"]:
        for version in product["versions"]:
            versions += 1
            fetch(version["url"], {"text/html"})
            fetch(version["markdownUrl"], {"text/plain", "text/markdown"})
    home = fetch("/Home/", {"text/html"}).text
    if '/agents/webmcp.js' not in home or '/.well-known/ai-catalog.json' not in home:
        raise ValueError("Homepage discovery links or WebMCP script are missing")
    root = fetch("/", {"text/html"}).text
    if 'window.location.replace' not in root or 'Home/' not in root:
        raise ValueError("Root redirect to Home is missing")
    print(json.dumps({"origin": origin, "public_versions": versions, "status": "passed"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--origin", default="https://help.beamable.com")
    check(parser.parse_args().origin.rstrip("/"))

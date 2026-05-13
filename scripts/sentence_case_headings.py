#!/usr/bin/env python3
"""Convert Markdown headings from Title Case to sentence case.

Preserves first-word capitalization, all-caps acronyms (>=2 chars), tokens
with interior capitals (e.g. BeamContext), inline code spans, proper-noun
whitelist (single- and multi-word), and trailing anchor IDs.

Usage from a content-branch worktree:

    python3 scripts/sentence_case_headings.py docs \\
        --exclude docs/cli/commands/cli-command-reference

Add more --exclude flags when running on a branch with auto-synced
core-owned dirs you don't want to touch:

    python3 scripts/sentence_case_headings.py docs \\
        --exclude docs/cli/commands/cli-command-reference \\
        --exclude docs/cli/guides \\
        --exclude docs/includes \\
        --exclude docs/portal

When the proper-noun whitelist needs a new entry, add it to MULTI_WORD
(for phrases) or SINGLE_WORD (for one-word terms) and re-run.
"""
import re
import sys
from pathlib import Path

MULTI_WORD = [
    # Order matters: phrases are stashed sequentially with \b boundaries,
    # so list longer phrases before shorter overlapping ones (e.g.
    # "Global Price War 2" before "Global Price War").
    "Head Adornment Test Scenario", "Turn-based Beamable Fighters",
    "Beamable Boss Battle", "Global Price War 2", "Global Price War",
    "King of the Ring",
    "Cloud Save", "Content Manager", "Admin Console", "Beam Library",
    "Beam CLI", "Beam PIE", "Unreal Engine", "Visual Studio", "Game Maker",
    "Photon Fusion", "Google Play Console", "Google Play Store",
    "Google Play Billing", "Google Play Game Services", "Google Play",
    "Google Cloud Console", "Game Content Designer", "Beam Services",
    "Unity Package Manager", "Unity Editor", "Epic Online Services",
    "Game Center", "Online Subsystem",
]

SINGLE_WORD = {
    "beamable": "Beamable", "unity": "Unity", "unreal": "Unreal",
    "portal": "Portal", "monobehaviour": "MonoBehaviour",
    "blueprint": "Blueprint", "blueprints": "Blueprints",
    "microservice": "Microservice", "microservices": "Microservices",
    "microstorage": "MicroStorage", "microstorages": "MicroStorages",
    "steam": "Steam", "discord": "Discord", "apple": "Apple",
    "google": "Google", "epic": "Epic", "github": "GitHub",
    "gitlab": "GitLab", "docker": "Docker", "dockerfile": "Dockerfile",
    "dockerfiles": "Dockerfiles", "nuget": "NuGet", "mongodb": "MongoDB",
    "linux": "Linux", "windows": "Windows", "macos": "macOS",
    "ios": "iOS", "android": "Android", "mac": "Mac",
    "javascript": "JavaScript", "typescript": "TypeScript",
    "python": "Python", "java": "Java", "scala": "Scala",
    "playfab": "PlayFab", "jetbrains": "JetBrains", "rider": "Rider",
    "beamball": "Beamball", "beamfarm": "BeamFarm",
    "beamcontext": "BeamContext", "pvp": "PvP", "pve": "PvE",
    ".net": ".NET", "c#": "C#", "c++": "C++", "f#": "F#",
    "readme.io": "ReadMe.io", "opentelemetry": "OpenTelemetry",
    "mkdocs": "MkDocs", "markdown": "Markdown", "html": "HTML",
    "css": "CSS", "yaml": "YAML", "json": "JSON",
    "net10": "Net10", "net6.0": "net6.0", "net7.0": "net7.0",
    "net8.0": "net8.0",
    "i": "I",
    "id": "ID", "ids": "IDs",
    "url": "URL", "urls": "URLs", "uri": "URI", "uris": "URIs",
    "facebook": "Facebook", "twitter": "Twitter", "youtube": "YouTube",
    "twitch": "Twitch", "reddit": "Reddit", "instagram": "Instagram",
    "tiktok": "TikTok", "amazon": "Amazon", "microsoft": "Microsoft",
    "stripe": "Stripe", "paypal": "PayPal", "betterstack": "BetterStack",
    "openai": "OpenAI", "photon": "Photon", "epicgames": "EpicGames",
    "playstation": "PlayStation", "xbox": "Xbox", "nintendo": "Nintendo",
    "gradle": "Gradle", "edgegap": "Edgegap",
}

HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)(\s*\{#[^}]+\})?\s*$')
CODE_SPAN_RE = re.compile(r'`[^`]+`')
FENCE_RE = re.compile(r'^(```|~~~)')


def convert_heading(text: str) -> str:
    stashed = []

    def stash(m):
        stashed.append(m.group(0))
        return f"\x00{len(stashed) - 1}\x00"

    protected = CODE_SPAN_RE.sub(stash, text)

    # Replace standalone " & " with " and " in headings. Code spans are
    # already stashed, so this won't touch ampersands inside code.
    protected = re.sub(r' & ', ' and ', protected)

    # Stash multi-word proper nouns as opaque placeholders so per-token
    # casing rules don't touch their interior words.
    for phrase in MULTI_WORD:
        pattern = re.compile(r'\b' + re.escape(phrase) + r'\b', re.IGNORECASE)
        def stash_phrase(m, p=phrase):
            stashed.append(p)
            return f"\x00{len(stashed) - 1}\x00"
        protected = pattern.sub(stash_phrase, protected)

    tokens = re.findall(r'\S+|\s+', protected)
    result = []
    seen_first_word = False
    for tok in tokens:
        if tok.isspace():
            result.append(tok)
            continue
        if '\x00' in tok:
            result.append(tok)
            seen_first_word = True
            continue
        # Skip leading numbering tokens (e.g. "1.", "2.", "a)") — they
        # don't count as "the first word" for capitalization purposes.
        if not seen_first_word and re.fullmatch(r'[\dixvIXV]+[.)\]]', tok):
            result.append(tok)
            continue
        result.append(transform_token(tok, is_first=not seen_first_word))
        seen_first_word = True

    out = ''.join(result)
    for i, span in enumerate(stashed):
        out = out.replace(f'\x00{i}\x00', span)
    return out


def _shrink(s: str) -> str:
    """Return lowercased form; keep multi-word whitelist already done."""
    return s.lower()


def transform_token(tok: str, is_first: bool) -> str:
    if _shrink(tok) in SINGLE_WORD:
        return SINGLE_WORD[_shrink(tok)]

    m = re.match(r'^(\W*)(.*?)(\W*)$', tok)
    if not m:
        return tok
    prefix, core, suffix = m.groups()
    if not core:
        return tok

    # Leading-dot tokens are dotfile/dotdir/extension-like names
    # (.beamable, .dockerignore, .csproj). Preserve verbatim unless the
    # entire token was already matched by the whitelist above (e.g. .NET).
    if prefix.startswith('.'):
        return tok

    if _shrink(core) in SINGLE_WORD:
        return prefix + SINGLE_WORD[_shrink(core)] + suffix

    if core.isupper() and len(core) >= 2:
        return tok

    # Interior-caps preservation (e.g. BeamContext, MongoDb) — but only
    # for words without hyphens. Hyphenated Title Case like "Step-by-Step"
    # should be split and re-cased, not preserved.
    if '-' not in core and any(c.isupper() for c in core[1:]) and core[0].isupper():
        return tok

    if '-' in core:
        parts = core.split('-')
        new_parts = []
        for i, part in enumerate(parts):
            if _shrink(part) in SINGLE_WORD:
                new_parts.append(SINGLE_WORD[_shrink(part)])
            elif part.isupper() and len(part) >= 2:
                new_parts.append(part)
            elif any(c.isupper() for c in part[1:]) and part and part[0].isupper():
                new_parts.append(part)
            else:
                if is_first and i == 0 and part:
                    new_parts.append(part[0].upper() + part[1:].lower())
                else:
                    new_parts.append(part.lower())
        return prefix + '-'.join(new_parts) + suffix

    if is_first and core:
        return prefix + core[0].upper() + core[1:].lower() + suffix
    return prefix + core.lower() + suffix


def process_file(path: Path) -> bool:
    original = path.read_text()
    lines = original.splitlines(keepends=True)
    in_fence = False
    changed = False
    new_lines = []
    for line in lines:
        stripped = line.rstrip('\r\n')
        eol = line[len(stripped):]
        if FENCE_RE.match(stripped.lstrip()):
            in_fence = not in_fence
            new_lines.append(line)
            continue
        if in_fence:
            new_lines.append(line)
            continue
        m = HEADING_RE.match(stripped)
        if m:
            hashes, text, anchor = m.group(1), m.group(2), m.group(3) or ''
            new_text = convert_heading(text)
            new_line = f"{hashes} {new_text}{anchor}{eol}"
            if new_line != line:
                changed = True
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    if changed:
        path.write_text(''.join(new_lines))
    return changed


def main():
    if len(sys.argv) < 2:
        print("usage: sentence_case_headings.py <root> [--exclude path]...")
        sys.exit(1)
    root = Path(sys.argv[1])
    excludes = []
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--exclude":
            excludes.append(Path(sys.argv[i + 1]).resolve())
            i += 2
        else:
            i += 1

    files_changed = 0
    for md in sorted(root.rglob("*.md")):
        md_abs = md.resolve()
        if any(str(md_abs).startswith(str(ex)) for ex in excludes):
            continue
        if process_file(md):
            files_changed += 1
            print(f"changed: {md}")
    print(f"\nTotal files changed: {files_changed}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Finish a local Mike deploy/alias operation, then push gh-pages exactly once."""

import argparse
import importlib.util
import subprocess
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location("site_assets", Path(__file__).with_name("generate-site-assets.py"))
site_assets = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site_assets)


def git(repo, *arguments):
    return subprocess.check_output(["git", "-C", str(repo), *arguments], text=True).strip()


def publish(repo, push=False, branch="gh-pages", remote="origin"):
    repo = Path(repo).resolve()
    previous = git(repo, "rev-parse", f"refs/heads/{branch}")
    # A detached worktree lets generation commit without switching the content
    # checkout or allowing Git to stage authored changes alongside generated files.
    with tempfile.TemporaryDirectory(prefix="beamable-pages-") as directory:
        checkout = Path(directory) / "pages"
        git(repo, "worktree", "add", "--detach", str(checkout), previous)
        try:
            changed, removed = site_assets.generate(checkout)
            if changed or removed:
                # A full publication has thousands of long paths. Feed literal
                # pathspecs on stdin rather than exceeding the OS argument limit.
                pathspecs = b"\0".join((":(literal)" + path).encode() for path in [*changed, *removed]) + b"\0"
                subprocess.run(["git", "-C", str(checkout), "add", "--pathspec-from-file=-", "--pathspec-file-nul"],
                               input=pathspecs, check=True)
            if git(checkout, "diff", "--cached", "--name-only"):
                git(checkout, "commit", "-m", "Generate public crawl and agent discovery assets")
            completed = git(checkout, "rev-parse", "HEAD")
        finally:
            git(repo, "worktree", "remove", "--force", str(checkout))
    if push:
        # Compare-and-swap refuses concurrent local changes; an ordinary push
        # refuses concurrent remote changes. Never force-push a publication.
        git(repo, "update-ref", f"refs/heads/{branch}", completed, previous)
        git(repo, "push", remote, f"refs/heads/{branch}:refs/heads/{branch}")
        print(f"Published {completed}")
    else:
        print(f"Dry run verified {completed}; no refs updated or pushed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--push", action="store_true", help="Push combined Mike output and discovery assets")
    args = parser.parse_args()
    publish(args.repo, push=args.push)

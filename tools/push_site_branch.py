"""Publish the built site through git: replace the `site` branch with build/pages/ and push it.

    python tools/build_pages_bundle.py          # builds and leak-scans build/pages/
    python tools/push_site_branch.py [--no-push]

The `site` branch holds only ``public/`` (the bundle) and ``.github/workflows/deploy-site.yml`` (from
tools/site_branch/). Pushing it runs that workflow, which deploys ``public/`` to the Cloudflare Pages
project cygnus-sky. The branch is rebuilt as one new commit on top of its previous tip each time (a
readable history of deployments), in a temporary git worktree, so the main checkout is never touched.
``public/SITE_BUILD.json`` records the main commit the bundle was built from.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "build" / "pages"
WORKFLOW = ROOT / "tools" / "site_branch" / "deploy-site.yml"
BRANCH = "site"


def git(*args: str, cwd: Path = ROOT, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, check=check, capture_output=True, text=True)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--no-push", action="store_true", help="commit the branch locally only")
    ap.add_argument("--remote", default="origin")
    a = ap.parse_args(argv)
    if not (BUNDLE / "index.html").is_file():
        raise SystemExit("build/pages/index.html missing: run python tools/build_pages_bundle.py first")
    head = git("rev-parse", "HEAD").stdout.strip()
    dirty = bool(git("status", "--porcelain", "--untracked-files=no").stdout.strip())
    git("fetch", a.remote, BRANCH, check=False)
    remote_tip = git("rev-parse", "--verify", "--quiet", f"{a.remote}/{BRANCH}", check=False).stdout.strip()
    tmp = Path(tempfile.mkdtemp(prefix="cygnus-site-"))
    wt = tmp / "site"
    try:
        if remote_tip:
            git("worktree", "add", "--detach", str(wt), remote_tip)
        else:                                     # first publication: an orphan branch with no main history
            git("worktree", "add", "--detach", str(wt), "HEAD")
            git("checkout", "--orphan", f"{BRANCH}-new", cwd=wt)
            git("rm", "-rf", "--quiet", ".", cwd=wt)
        for child in wt.iterdir():
            if child.name != ".git":
                shutil.rmtree(child) if child.is_dir() else child.unlink()
        shutil.copytree(BUNDLE, wt / "public")
        (wt / ".github" / "workflows").mkdir(parents=True)
        shutil.copyfile(WORKFLOW, wt / ".github" / "workflows" / "deploy-site.yml")
        files = sum(1 for p in (wt / "public").rglob("*") if p.is_file())
        build = {"built_from_main_commit": head, "main_worktree_dirty": dirty, "files": files,
                 "built_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
        (wt / "public" / "SITE_BUILD.json").write_text(json.dumps(build, indent=1) + "\n", encoding="utf-8")
        (wt / "README.md").write_text("Deploy branch: `public/` is the built site (tools/build_pages_bundle.py on main); "
                                      "pushing runs .github/workflows/deploy-site.yml. Do not edit by hand.\n",
                                      encoding="utf-8")
        git("add", "-A", cwd=wt)
        if not git("status", "--porcelain", cwd=wt).stdout.strip():
            print("site branch already matches this bundle: nothing to publish")
            return 0
        git("commit", "-q", "-m", f"Site build from main {head[:10]} ({files} files)"
            + (" [main worktree had uncommitted changes]" if dirty else ""), cwd=wt)
        new = git("rev-parse", "HEAD", cwd=wt).stdout.strip()
        print(f"site commit {new[:10]}: {files} files from main {head[:10]}")
        if not a.no_push:
            r = git("push", a.remote, f"{new}:refs/heads/{BRANCH}", check=False)
            print(r.stdout + r.stderr)
            return r.returncode
        return 0
    finally:
        git("worktree", "remove", "--force", str(wt), check=False)
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())

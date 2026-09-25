"""Assemble the Cloudflare Pages deploy bundle and leak-scan it.

    python tools/build_pages_bundle.py        -> build/pages/

Layout: the sky explorer is the home page (``/``, with its ``data/`` and ``img/`` bundle); the public
repository site (``python -m cygnus.publish build`` output) keeps every other path, its own home page
moving to ``/about/``. Old ``/preview/`` links redirect to ``/``. A ``_headers`` file applies the
response headers from docs/PUBLISHING.md. The whole bundle must pass the publication leak scan
(private paths, remote names, credential words, e-mail addresses) or nothing is written.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from cygnus.publish.safety import scan_for_leaks  # noqa: E402

SITE = ROOT / "build" / "site"
MOCK = ROOT / "design-system" / "mockups"
OUT = ROOT / "build" / "pages"

HEADERS = """/*
  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'
  X-Content-Type-Options: nosniff
  Referrer-Policy: no-referrer
  Permissions-Policy: geolocation=(), microphone=(), camera=()

/files/*
  Content-Disposition: attachment

"""

REDIRECTS = """/preview/explorer/ / 301
/preview/explorer/index.html / 301
/preview/* / 301
"""


def main() -> int:
    if not (SITE / "index.html").is_file():
        print("build the site first: python -m cygnus.publish build", file=sys.stderr)
        return 2
    if not (MOCK / "explorer" / "data" / "sky.json").is_file():
        print("build the explorer first: python design-system/mockups/build_explorer.py", file=sys.stderr)
        return 2
    tmp = OUT.with_name("pages.tmp")
    shutil.rmtree(tmp, ignore_errors=True)
    shutil.copytree(SITE, tmp)
    exp = MOCK / "explorer"
    clash = [p.relative_to(exp).as_posix() for p in exp.rglob("*") if p.is_file() and (tmp / p.relative_to(exp)).exists()
             and p.name != "index.html"]
    if clash:
        shutil.rmtree(tmp)
        print("explorer files would overwrite site files: " + ", ".join(clash), file=sys.stderr)
        return 1
    shutil.copytree(exp, tmp, dirs_exist_ok=True)   # explorer index.html replaces the repository home (kept at /about/)
    (tmp / "_headers").write_text(HEADERS, encoding="utf-8")
    (tmp / "_redirects").write_text(REDIRECTS, encoding="utf-8")
    leaks = scan_for_leaks(tmp)
    if leaks:
        shutil.rmtree(tmp)
        print("LEAK SCAN FAILED — nothing written:\n  " + "\n  ".join(leaks), file=sys.stderr)
        return 1
    shutil.rmtree(OUT, ignore_errors=True)
    tmp.rename(OUT)
    n = sum(1 for p in OUT.rglob("*") if p.is_file())
    size = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"bundle ok: {n} files, {size / 1e6:.1f} MB -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

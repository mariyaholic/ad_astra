"""Assemble the Cloudflare Pages deploy bundle and leak-scan it.

    python tools/build_pages_bundle.py        -> build/pages/

Layout: the public repository site (``python -m cygnus.publish build`` output) at the root, and the
sky-explorer prototype with its mockup pages under ``/preview/``. A ``_headers`` file applies the
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

/preview/*
  X-Robots-Tag: noindex
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
    prev = tmp / "preview"
    prev.mkdir()
    for name in ("index.html", "target-wasp-12.html", "log.html", "mockup.css"):
        shutil.copy2(MOCK / name, prev / name)
    shutil.copytree(MOCK / "explorer", prev / "explorer")
    (tmp / "_headers").write_text(HEADERS, encoding="utf-8")
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

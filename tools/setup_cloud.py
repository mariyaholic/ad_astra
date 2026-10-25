"""Prepare a task-local Cygnus environment, or check it without installing.

Run with Python 3.12 in cloud setup; then use .venv/bin/python explicitly.
The readiness receipt is ignored local state, not scientific evidence.
"""
from __future__ import annotations

import argparse
import importlib
import importlib.metadata
import json
import math
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONSTRAINTS = ROOT / "cloud/constraints-linux-py312.txt"
MODULES = ("cygnus", "cygnus.cloud", "cygnus.cloud_diagnostics", "cygnus.cloud_scout", "cygnus.handback",
           "cygnus.tier", "pytest", "yaml", "jinja2", "numpy", "scipy", "astropy",
           "requests", "astroquery", "matplotlib")


def venv_python(root: Path) -> Path:
    return root / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def constraints(root: Path, platform: str = sys.platform, version=sys.version_info) -> list[str]:
    """Pinned resolution for the cloud-agent target (Linux CPython 3.12) only."""
    path = root / CONSTRAINTS.relative_to(ROOT)
    if platform.startswith("linux") and tuple(version[:2]) == (3, 12) and path.is_file():
        return ["-c", str(path)]
    return []


def install(root: Path) -> None:
    """Reuse the local venv and satisfy existing CI extras without upgrading all deps."""
    python = venv_python(root)
    if not python.is_file():
        print("Creating task-local .venv (limit: 300 seconds)", flush=True)
        subprocess.run([sys.executable, "-m", "venv", str(root / ".venv")], cwd=root,
                       check=True, timeout=300)
    print("Installing existing CI extras in .venv (limit: 600 seconds)", flush=True)
    subprocess.run([str(python), "-m", "pip", "install", "--retries", "1", "--timeout", "30",
                    *constraints(root), "-e", ".[test,site,campaign]"], cwd=root, check=True, timeout=600)


def git_receipt(root: Path) -> dict:
    """Do not read remote URLs: only source revision and history completeness."""
    def git(*args):
        return subprocess.run(["git", *args], cwd=root, check=True, capture_output=True,
                              text=True, timeout=30).stdout.strip()

    return {"commit": git("rev-parse", "HEAD"),
            "shallow": git("rev-parse", "--is-shallow-repository") == "true"}


def preflight(root: Path, min_free_gib: float = 1) -> dict:
    """Check this interpreter/checkout offline; do not infer service or science readiness."""
    checks = []

    def record(name, passed, detail):
        checks.append({"name": name, "passed": bool(passed), "detail": detail})

    record("python", sys.version_info >= (3, 10),
           f"{sys.version.split()[0]}; cloud recommendation: 3.12")
    git = {}
    try:
        git = git_receipt(root)
        record("git_history", not git["shallow"],
               "shallow checkout: fetch full history before provenance tests" if git["shallow"]
               else "full history available; offline suite checks individual notebook pins")
    except (OSError, subprocess.SubprocessError):
        record("git_history", False, "cannot read Git revision/history in this checkout")

    for name in MODULES:
        try:
            importlib.import_module(name)
            record(f"import:{name}", True, "imported")
        except Exception as exc:
            record(f"import:{name}", False, f"import failed ({type(exc).__name__}); rerun install")

    try:
        from cygnus.config import WORKTREE, scratch_dir

        record("checkout_import", WORKTREE.resolve() == root.resolve(),
               "cygnus must import from this checkout's editable install")
        scratch = scratch_dir()
        free = shutil.disk_usage(scratch).free / 1024**3
        record("scratch_space", free >= min_free_gib,
               f"{free:.2f} GiB free; require at least {min_free_gib:g} GiB")
    except Exception as exc:
        record("checkout_import", False, f"config/scratch check failed ({type(exc).__name__})")

    try:
        result = subprocess.run([sys.executable, "-m", "pip", "check"], cwd=root,
                                capture_output=True, text=True, timeout=60)
        record("pip_check", result.returncode == 0,
               "dependencies consistent" if result.returncode == 0
               else "dependency conflict or pip unavailable; run python -m pip check in the venv")
    except (OSError, subprocess.SubprocessError):
        record("pip_check", False, "pip check could not complete")

    # Names and versions only. pip freeze / direct_url may contain private URLs.
    packages = sorted([{"name": d.metadata.get("Name", "unknown"), "version": d.version}
                       for d in importlib.metadata.distributions()], key=lambda d: d["name"].lower())
    return {"schema_version": 1, "utc": datetime.now(timezone.utc).isoformat(),
            "scope": "offline environment preflight; no archive or science validation",
            "python": sys.version.split()[0], "platform": sys.platform, "git": git,
            "checks": checks, "packages": packages,
            "ready": all(c["passed"] for c in checks)}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="check this interpreter/checkout offline; never install")
    parser.add_argument("--min-free-gib", type=float, default=1,
                        help="minimum free scratch space for --check (default: 1 GiB)")
    args = parser.parse_args(argv)
    if not math.isfinite(args.min_free_gib) or args.min_free_gib < 0:
        parser.error("--min-free-gib must be finite and nonnegative")
    if not args.check:
        install(ROOT)
        return subprocess.run([str(venv_python(ROOT)), str(Path(__file__).resolve()),
                               "--check", "--min-free-gib", str(args.min_free_gib)], cwd=ROOT).returncode
    print("Checking offline environment; archive access and science are not tested here", flush=True)
    receipt = preflight(ROOT, args.min_free_gib)
    target = ROOT / "state/cloud/environment.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    for check in receipt["checks"]:
        print(f"{'PASS' if check['passed'] else 'FAIL'} {check['name']}: {check['detail']}")
    print("Receipt: state/cloud/environment.json (ignored local state)")
    return 0 if receipt["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

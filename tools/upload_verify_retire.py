"""Upload a staged Tier-1 service pack to Drive, verify, retire local copies.

Per the user's retention instruction (2026-09-24): bulk data lives on
``cygnus:Cygnus`` only; the local staging copy is deleted once the remote
MD5s match the manifest. The manifest (with sha256/md5) stays in the
worktree and on Drive, so every product remains re-retrievable.

Usage:
    python tools/upload_verify_retire.py 01_mast
    python tools/upload_verify_retire.py 02_gaia --transfers 8
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from cygnus.config import ledger_path  # noqa: E402
from cygnus.ingest.pack import retire_local_copies, verify_remote_upload  # noqa: E402
from cygnus.ledger import Ledger  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pack_dir_name", help="staged dir name, e.g. 01_mast")
    ap.add_argument("--remote-root", default="cygnus:Cygnus/data/tier1")
    ap.add_argument("--pack-root", default=r"D:\AO_Artifacts\cygnus_scratch\tier1_pack")
    ap.add_argument("--transfers", type=int, default=4)
    ap.add_argument("--copy-only", action="store_true",
                    help="upload without verifying/retiring")
    args = ap.parse_args(argv)

    pack_root = Path(args.pack_root)
    staged = pack_root / args.pack_dir_name
    if not staged.is_dir():
        raise SystemExit(f"no staged dir: {staged}")
    remote_dir = f"{args.remote_root.rstrip('/')}/{args.pack_dir_name}"

    cmd = ["rclone", "copy", str(staged), remote_dir,
           "--transfers", str(args.transfers), "--drive-chunk-size", "64M", "-q"]
    print("COPY:", " ".join(cmd), flush=True)
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
    if proc.returncode != 0:
        print("COPY FAILED", flush=True)
        print((proc.stdout or "")[-1500:], flush=True)
        print((proc.stderr or "")[-1500:], flush=True)
        return 2
    print("COPY ok", flush=True)
    if args.copy_only:
        return 0

    ledger = Ledger(ledger_path())
    try:
        res = verify_remote_upload(pack_root, args.pack_dir_name, remote_dir, ledger=ledger)
        summary = {k: v for k, v in res.items() if k not in ("details",)}
        print("VERIFY:", json.dumps(summary, indent=1), flush=True)
        if not res["ok"]:
            print("VERIFY FAILED — local copies RETAINED for manual inspection", flush=True)
            return 3
        n = retire_local_copies(pack_root, args.pack_dir_name, ledger=ledger)
        print(f"RETIRE: deleted {n} local files (Drive hosts the data)", flush=True)
    finally:
        ledger.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
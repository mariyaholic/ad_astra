"""Operator CLI for the public repository site.

    python -m cygnus.publish check                 # validate; print what would be public
    python -m cygnus.publish build [--out DIR]     # render build/site (read-only ledger)
    python -m cygnus.publish serve [--port 8765]   # preview on 127.0.0.1 only
    python -m cygnus.publish snapshot --pack-root DIR --name tier1-pack
    python -m cygnus.publish withdraw <collection-id> --reason "..."

There is deliberately no web-facing write path: publishing is an edit to
``publish/collections/*.json`` reviewed like code, then a rebuild.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from ..config import WORKTREE, scratch_dir
from .build import BuildConfig, build_site
from .schema import PublicationError, load_collections


def _publish_root(args: argparse.Namespace) -> Path:
    return Path(args.publish_root) if args.publish_root else WORKTREE / "publish"


def cmd_check(args: argparse.Namespace) -> int:
    root = _publish_root(args)
    colls = load_collections(root)
    report = []
    for c in colls:
        report.append({
            "id": c.id, "status": c.status, "type": c.type,
            "items": [{"id": i.id, "kind": i.kind, "access": i.access, "download": i.download,
                       "origin": i.origin} for i in c.items],
        })
    print(json.dumps(report, indent=1))
    # a dry build into scratch proves sources resolve and the leak scan passes
    out = scratch_dir("site_check")
    res = build_site(BuildConfig(publish_root=root, out_dir=out / "site"))
    print(f"dry build ok: {len(res.pages)} pages, {len(res.files)} public files", file=sys.stderr)
    for w in res.warnings:
        print(f"warning: {w}", file=sys.stderr)
    return 0


def cmd_build(args: argparse.Namespace) -> int:
    cfg = BuildConfig(publish_root=_publish_root(args), out_dir=args.out)
    res = build_site(cfg)
    print(f"built {len(res.pages)} pages, {len(res.files)} public files -> {res.out_dir}")
    for s in res.skipped:
        print(f"skipped: {s}")
    for w in res.warnings:
        print(f"warning: {w}")
    return 0


def cmd_serve(args: argparse.Namespace) -> int:
    from .serve import serve

    out = Path(args.out) if args.out else WORKTREE / "build" / "site"
    if not (out / "index.html").is_file():
        print(f"no built site at {out}; run `python -m cygnus.publish build` first", file=sys.stderr)
        return 1
    serve(out, port=args.port, base_path=args.base_path)
    return 0


def cmd_snapshot(args: argparse.Namespace) -> int:
    from .snapshot import snapshot_pack

    pack = Path(args.pack_root) if args.pack_root else scratch_dir("tier1_pack")
    dest = _publish_root(args) / "data" / args.name
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    written = snapshot_pack(pack, dest, snapshot_utc=ts)
    for p in written:
        print(f"wrote publish/data/{args.name}/{p.name}")
    if not written:
        print("no */MANIFEST.json found under the pack root", file=sys.stderr)
        return 1
    return 0


def cmd_withdraw(args: argparse.Namespace) -> int:
    root = _publish_root(args)
    path = root / "collections" / f"{args.collection}.json"
    if not path.is_file():
        print(f"no collection {args.collection!r}", file=sys.stderr)
        return 1
    raw = json.loads(path.read_text(encoding="utf-8"))
    raw["status"] = "withdrawn"
    raw["withdrawn"] = {"date": datetime.now(timezone.utc).strftime("%Y-%m-%d"), "reason": args.reason}
    path.write_text(json.dumps(raw, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{args.collection}: withdrawn. Rebuild and redeploy to remove its files from the host.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m cygnus.publish", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--publish-root", help="default: <worktree>/publish")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    p = sub.add_parser("build")
    p.add_argument("--out", help="default: <worktree>/build/site")
    p = sub.add_parser("serve")
    p.add_argument("--out")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--base-path", default="/")
    p = sub.add_parser("snapshot")
    p.add_argument("--pack-root")
    p.add_argument("--name", default="tier1-pack")
    p = sub.add_parser("withdraw")
    p.add_argument("collection")
    p.add_argument("--reason", required=True)
    args = ap.parse_args(argv)
    try:
        return {"check": cmd_check, "build": cmd_build, "serve": cmd_serve,
                "snapshot": cmd_snapshot, "withdraw": cmd_withdraw}[args.cmd](args)
    except PublicationError as exc:
        print(f"publication error:\n{exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

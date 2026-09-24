"""``python -m cygnus.campaign {new,run,report,queue,check}``

The repeatable loop for any target, on any machine (docs/AGENT_RUNBOOK.md):

    python -m cygnus.campaign queue                              # what is free
    python -m cygnus.campaign new --next                         # claim the top free queue target
    python -m cygnus.campaign new --planet "WASP-12 b"           # or any known planet
    python -m cygnus.campaign run campaigns/<slug>.yaml
    python -m cygnus.campaign report campaigns/<slug>.yaml
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ..config import WORKTREE, ledger_path
from ..ledger import Ledger
from .runner import SpecError, load_spec, run

DEFAULT_QUEUE = "campaigns/tess-mono-01/target_queue.csv"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="cygnus.campaign")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="execute a campaign spec (steps are ledgered and resumable)")
    r.add_argument("spec")
    r.add_argument("--force", action="store_true", help="recompute steps even if an identical completed run exists")
    r.add_argument("--until", help="stop after this step")
    r.add_argument("--ledger", help="ledger path (default: CYGNUS_LEDGER or state/ledger.sqlite)")
    c = sub.add_parser("check", help="validate a spec without running it")
    c.add_argument("spec")
    n = sub.add_parser("new", help="write campaigns/<slug>.yaml for a known-object test")
    src = n.add_mutually_exclusive_group(required=True)
    src.add_argument("--next", action="store_true", help="the highest-ranked unclaimed target in the queue")
    src.add_argument("--from-queue", metavar="NAME", help="a named target in the queue, e.g. TOI-2666.01")
    src.add_argument("--planet", metavar="PL_NAME", help="a known planet from the NASA Exoplanet Archive, e.g. 'WASP-12 b'")
    src.add_argument("--manual", metavar="NAME", help="give --tic --ra --dec --t0 [--period --depth-ppm --duration-h]")
    n.add_argument("--queue", default=DEFAULT_QUEUE, help=f"queue CSV (default {DEFAULT_QUEUE})")
    n.add_argument("--seed", type=int, default=20260927)
    for flag, typ in (("--tic", int), ("--ra", float), ("--dec", float), ("--t0", float), ("--period", float),
                      ("--depth-ppm", float), ("--duration-h", float)):
        n.add_argument(flag, type=typ)
    n.add_argument("--source", default="given by hand", help="where --manual values came from (recorded in the spec)")
    rp = sub.add_parser("report", help="draft REPORT.md and SEARCH_LOG.md from a finished run")
    rp.add_argument("spec")
    q = sub.add_parser("queue", help="which queued targets are free, claimed, run or reviewed")
    q.add_argument("--queue", default=DEFAULT_QUEUE)
    q.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    from . import scaffold

    root = WORKTREE
    if a.cmd == "new":
        parent = None
        if a.next or a.from_queue:
            qpath = root / a.queue
            row = scaffold.pick_from_queue(root, qpath, a.from_queue)
            t = scaffold.target_from_row(row, "NASA Exoplanet Archive TOI table")
            parent = Path(a.queue).parent.name
            origin = f"{a.queue} (rank {row.get('rank')}), itself from the NASA Exoplanet Archive TOI table"
        elif a.planet:
            t = scaffold.lookup_planet(a.planet)
            origin = f"NASA Exoplanet Archive pscomppars, queried {scaffold.now_utc()[:10]}"
        else:
            missing = [f for f in ("tic", "ra", "dec", "t0") if getattr(a, f) is None]
            if missing:
                ap.error("--manual needs " + ", ".join("--" + m for m in missing))
            t = {"name": a.manual, "tic": a.tic, "ra_deg": a.ra, "dec_deg": a.dec, "t0_bjd": a.t0, "period_days": a.period,
                 "depth_ppm": a.depth_ppm, "duration_h": a.duration_h, "tmag": None, "position_source": a.source,
                 "disposition": ""}
            origin = a.source
        path = scaffold.write_spec(root, t, parent=parent, origin=origin, seed=a.seed)
        load_spec(path)   # generated specs must validate
        print(path.relative_to(root).as_posix())
        return 0
    if a.cmd == "queue":
        rows = scaffold.queue_status(root, root / a.queue)
        if a.json:
            print(json.dumps(rows, indent=1))
        else:
            print(f"{'rank':>4}  {'target':<14} {'state':<10} {'known signal':<13} report")
            for s in rows:
                print(f"{s['rank'] or '':>4}  {s['name']:<14} {s['state'] or '':<10} {s['known_signal'] or '':<13} {s['review'] or ''}")
        return 0
    try:
        spec = load_spec(a.spec)
    except SpecError as exc:
        print(f"spec error: {exc}", file=sys.stderr)
        return 2
    if a.cmd == "check":
        print(json.dumps({"campaign_id": spec["campaign_id"], "steps": [next(iter(s)) for s in spec["steps"]]}, indent=2))
        return 0
    if a.cmd == "report":
        spec["_path"] = Path(a.spec).resolve()
        for p in scaffold.draft_report(spec, root):
            print(p.relative_to(root).as_posix())
        return 0
    ledger = Ledger(a.ledger or ledger_path())
    try:
        out = run(a.spec, ledger=ledger, force=a.force, until=a.until)
    finally:
        ledger.close()
    print(json.dumps({k: out[k] for k in ("campaign_id", "steps_run", "complete", "record")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())

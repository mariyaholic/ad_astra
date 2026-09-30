"""``python -m cygnus.campaign {new,run,report,vet,queue,check}``

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
from .runner import MULTI_RUNNER, SpecError, load_spec, run, spec_runner

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
    v = sub.add_parser("vet", help="vet repeat events of a finished run (writes <outputs>/vetting/)")
    v.add_argument("spec")
    v.add_argument("--no-neighbours", action="store_true", help="skip the same-CCD neighbour light curves")
    v.add_argument("--no-pixels", action="store_true", help="skip the target-pixel-file difference image")
    v.add_argument("--events", help="comma-separated BJD mid-times to vet besides the runner's repeat candidates")
    v.add_argument("--tier-override", metavar="REASON", help="run vet below the T2 gate; the reason is printed and must be recorded in the report")
    v.add_argument("--ledger", help="ledger path (default: CYGNUS_LEDGER or state/ledger.sqlite)")
    q = sub.add_parser("queue", help="which queued targets are free, claimed, run or reviewed")
    q.add_argument("--queue", default=DEFAULT_QUEUE)
    q.add_argument("--json", action="store_true")
    rc = sub.add_parser("reconcile", help="annotate a lead's records as superseded, re-render its dossier, check drift")
    rc.add_argument("campaign_id")
    rc.add_argument("--note", required=True)
    rc.add_argument("--superseded-by")
    rc.add_argument("--candidate-id")
    rc.add_argument("--no-dossier", action="store_true")
    tr = sub.add_parser("tier", help="which analysis tier a target has earned (from its sky record)")
    tr.add_argument("campaign_id", nargs="?")
    tr.add_argument("--all", action="store_true", help="tier counts over every sky record")
    a = ap.parse_args(argv)

    from . import scaffold

    root = WORKTREE
    if a.cmd == "new":
        parent = None
        if a.next or a.from_queue:
            qpath = root / a.queue
            row = scaffold.pick_from_queue(root, qpath, a.from_queue)
            from cygnus.targets import refresh_queue_target
            row = refresh_queue_target(row)
            t = scaffold.target_from_row(row, f"NASA Exoplanet Archive TOI table ({scaffold.TOI_POSITION_NOTE})")
            parent = Path(a.queue).parent.name
            origin = (f"{a.queue} (rank {row.get('rank')}), NASA Exoplanet Archive TOI row refreshed "
                      f"{row['catalogue_retrieved_utc']} (rowupdate {row['toi_rowupdate']})")
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
    if a.cmd == "tier":
        from ..skyrecord import load_records
        from .tiers import decide_campaign, summarize

        if a.all or not a.campaign_id:
            print(json.dumps(summarize([r for r in load_records(root) if r["_path"].startswith("campaigns/")]), indent=2))
            return 0
        print(json.dumps(decide_campaign(root, a.campaign_id).as_dict(), indent=2))
        return 0
    if a.cmd == "reconcile":
        from .reconcile import reconcile

        out = reconcile(root, a.campaign_id, a.note, superseded_by=a.superseded_by,
                        candidate_id=a.candidate_id, render_dossier=not a.no_dossier)
        print(json.dumps(out, indent=2))
        return 1 if out["findings"] else 0
    if a.cmd == "queue":
        rows = scaffold.queue_status(root, root / a.queue)
        if a.json:
            print(json.dumps(rows, indent=1))
        else:
            print(f"{'rank':>4}  {'target':<14} {'state':<10} {'known signal':<13} report")
            for s in rows:
                print(f"{s['rank'] or '':>4}  {s['name']:<14} {s['state'] or '':<10} {s['known_signal'] or '':<13} {s['review'] or ''}")
        return 0
    if a.cmd in ("run", "check", "report", "vet") and spec_runner(a.spec) == MULTI_RUNNER:
        # multi-archive specs (``runner: cygnus.multi``) live in campaigns/ too; hand them over whole
        from ..multi.__main__ import main as multi_main

        return multi_main(argv if argv is not None else sys.argv[1:])
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
    if a.cmd == "vet":
        from .tiers import decide_campaign, rank

        try:
            gate = decide_campaign(root, spec["campaign_id"], spec)
        except FileNotFoundError:
            gate = None
        if gate is not None and (gate.tier == "closed" or rank(gate.tier) < rank("T2")) and not a.tier_override:
            print(f"tier gate: {spec['campaign_id']} is at {gate.tier}, vet needs T2: " + "; ".join(gate.blockers or [gate.reason]) +
                  " (use --tier-override REASON only with a recorded justification)", file=sys.stderr)
            return 3
        if a.tier_override:
            print(f"TIER OVERRIDE: {a.tier_override} (record this in REPORT.md)", file=sys.stderr)
        from .vet import vet

        ledger = Ledger(a.ledger or ledger_path())
        try:
            with ledger.recorded_run(f"cygnus.campaign:{spec['campaign_id']}:lead_vetting", seed=spec.get("random_seed")) as r_:
                rep = vet(spec, root, neighbours=not a.no_neighbours, pixels=not a.no_pixels,
                          extra_events=[float(x) for x in (a.events or '').split(',') if x.strip()])
                r_.summary = f"lead vetting: {len(rep['events'])} event(s)"
        finally:
            ledger.close()
        print((Path(spec.get("outputs", f"campaigns/{spec['campaign_id']}/")) / "vetting" / "VETTING.md").as_posix())
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

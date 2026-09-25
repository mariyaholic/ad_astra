"""``python -m cygnus.multi {run,check,new,report,vet,queue,archives}``

Multi-archive campaign runner. Same ledgered, resumable loop as ``cygnus.campaign``, but
``fetch_products`` can discover from any registered archive adapter (``cygnus.multi.archives``),
single-channel products are screened once with a red-noise model, and archive-specific steps
(``context_products``, ``source_checks``, ``astrometric_vetting``) are available. Specs carry
``runner: cygnus.multi``; ``python -m cygnus.campaign`` hands them over automatically.

    python -m cygnus.multi archives                  # every registered adapter
    python -m cygnus.multi archives --check gaia     # live probe of one adapter
    python -m cygnus.multi new --manual T --tic 1 --ra 10 --dec 20 --t0 2459000.5 --archives mast,gaia
    python -m cygnus.multi run campaigns/<id>.yaml
    python -m cygnus.multi report campaigns/<id>.yaml

Root and ledger: the worktree and the production ledger (``CYGNUS_LEDGER`` or
``state/ledger.sqlite``) by default, with runs under the ``cygnus_multi:`` script namespace so
their provenance stays distinct from ``cygnus.campaign:`` runs. Setting ``CYGNUS_MULTI_ROOT``
runs in a sandbox instead: specs, outputs and ``<root>/state/ledger.sqlite`` all stay under that
root (promote results with ``python -m cygnus.multi.promote``).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from cygnus.config import WORKTREE, ledger_path
from cygnus.ledger import Ledger

from .runner import SpecError, load_spec, run

SANDBOX = os.environ.get("CYGNUS_MULTI_ROOT")
ROOT = Path(SANDBOX or WORKTREE).resolve()
DEFAULT_QUEUE = str(WORKTREE / "campaigns" / "tess-mono-01" / "target_queue.csv")


def _ledger_path(explicit: str | None) -> Path:
    """``--ledger``, else ``CYGNUS_LEDGER``, else the sandbox ledger (sandbox mode) or the production one."""
    if explicit:
        path = Path(explicit)
    else:
        env = os.environ.get("CYGNUS_LEDGER")
        # any root other than the worktree is a sandbox and gets its own ledger, never the production one
        sandbox = Path(ROOT).resolve() != WORKTREE.resolve()
        path = Path(env) if env else (Path(ROOT) / "state" / "ledger.sqlite" if sandbox else ledger_path())
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _cmd_archives(a) -> int:
    from .archives import base

    if a.check:
        from .archives.base import Target

        try:
            adapter = base.get(a.check)
        except KeyError as exc:
            print(json.dumps({"archive": a.check, "state": "unknown", "error": str(exc)}, indent=2))
            return 1
        t = Target(name=a.target, ra_deg=a.ra, dec_deg=a.dec, tic=a.tic)
        try:
            refs = adapter.discover(t, **({"epoch_iso": a.epoch} if a.epoch else {}))
        except base.AdapterUnavailable as exc:
            print(json.dumps({"archive": a.check, "state": "unavailable", "error": str(exc)}, indent=2))
            return 1
        except Exception as exc:  # noqa: BLE001
            print(json.dumps({"archive": a.check, "state": "error", "error": f"{type(exc).__name__}: {exc}"}, indent=2))
            return 1
        print(json.dumps({"archive": a.check, "state": "ok", "n_products": len(refs),
                          "products": [r.as_dict() for r in refs[:5]]}, indent=2, default=str))
        return 0
    print(json.dumps(base.summary(), indent=1))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="cygnus_multi")
    sub = ap.add_subparsers(dest="cmd", required=True)

    ar = sub.add_parser("archives", help="list registered archive adapters")
    ar.add_argument("--check", metavar="NAME", help="live-probe one adapter's discovery path")
    ar.add_argument("--target", default="test", help="target name for --check")
    ar.add_argument("--ra", type=float, default=10.0)
    ar.add_argument("--dec", type=float, default=20.0)
    ar.add_argument("--tic", type=int, default=None)
    ar.add_argument("--epoch", default=None, help="observation epoch for epoch-dependent adapters (e.g. SkyBoT)")

    r = sub.add_parser("run", help="execute a campaign spec (steps are ledgered and resumable)")
    r.add_argument("spec")
    r.add_argument("--force", action="store_true")
    r.add_argument("--until")
    r.add_argument("--ledger")
    c = sub.add_parser("check", help="validate a spec without running it")
    c.add_argument("spec")
    n = sub.add_parser("new", help="write a campaign spec for a known-object test")
    src = n.add_mutually_exclusive_group(required=True)
    src.add_argument("--next", action="store_true")
    src.add_argument("--from-queue", metavar="NAME")
    src.add_argument("--planet", metavar="PL_NAME")
    src.add_argument("--manual", metavar="NAME")
    n.add_argument("--queue", default=DEFAULT_QUEUE)
    n.add_argument("--seed", type=int, default=20260927)
    n.add_argument("--archives", help="comma-separated archive adapters for fetch_products, e.g. mast,gaia,skyview")
    for flag, typ in (("--tic", int), ("--ra", float), ("--dec", float), ("--t0", float), ("--period", float),
                      ("--depth-ppm", float), ("--duration-h", float)):
        n.add_argument(flag, type=typ)
    n.add_argument("--source", default="given by hand")
    rp = sub.add_parser("report", help="draft REPORT.md and SEARCH_LOG.md from a finished run")
    rp.add_argument("spec")
    v = sub.add_parser("vet", help="vet repeat events of a finished run")
    v.add_argument("spec")
    v.add_argument("--no-neighbours", action="store_true")
    v.add_argument("--no-pixels", action="store_true")
    v.add_argument("--events")
    v.add_argument("--ledger")
    q = sub.add_parser("queue", help="queue board")
    q.add_argument("--queue", default=DEFAULT_QUEUE)
    q.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    if a.cmd == "archives":
        return _cmd_archives(a)

    from . import scaffold

    root = ROOT
    if a.cmd == "new":
        try:
            parent = None
            if a.next or a.from_queue:
                qpath = Path(a.queue) if Path(a.queue).is_absolute() else root / a.queue
                row = scaffold.pick_from_queue(root, qpath, a.from_queue)
                t = scaffold.target_from_row(row, f"NASA Exoplanet Archive TOI table ({scaffold.TOI_POSITION_NOTE})")
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
            path = scaffold.write_spec(root, t, parent=parent, origin=origin, seed=a.seed, archives=a.archives)
            load_spec(path)
        except SystemExit:
            raise
        except Exception as exc:  # noqa: BLE001 - a clean CLI error, not a traceback
            print(f"new: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1
        print(path.relative_to(root).as_posix())
        return 0
    if a.cmd == "queue":
        try:
            rows = scaffold.queue_status(root, Path(a.queue) if Path(a.queue).is_absolute() else root / a.queue)
        except Exception as exc:  # noqa: BLE001
            print(f"queue: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1
        if a.json:
            print(json.dumps(rows, indent=1))
        else:
            print(f"{'rank':>4}  {'target':<14} {'state':<10} {'known signal':<13} report")
            for s in rows:
                print(f"{s['rank'] or '':>4}  {s['name']:<14} {s['state'] or '':<10} {s['known_signal'] or '':<13} {s['review'] or ''}")
        return 0
    if not Path(a.spec).is_file():
        print(f"spec not found: {a.spec}", file=sys.stderr)
        return 2
    try:
        spec = load_spec(a.spec)
    except SpecError as exc:
        print(f"spec error: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"spec unreadable: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    if a.cmd == "check":
        print(json.dumps({"campaign_id": spec["campaign_id"], "steps": [next(iter(s)) for s in spec["steps"]]}, indent=2))
        return 0
    if a.cmd == "report":
        spec["_path"] = Path(a.spec).resolve()
        try:
            written = scaffold.draft_report(spec, root)
        except SystemExit:
            raise
        except Exception as exc:  # noqa: BLE001
            print(f"report: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1
        for p in written:
            print(p.relative_to(root).as_posix())
        return 0
    if a.cmd == "vet":
        from ..campaign.vet import vet

        ledger = Ledger(_ledger_path(a.ledger))
        try:
            with ledger.recorded_run(f"cygnus_multi:{spec['campaign_id']}:lead_vetting", seed=spec.get("random_seed")) as r_:
                rep = vet(spec, root, neighbours=not a.no_neighbours, pixels=not a.no_pixels,
                          extra_events=[float(x) for x in (a.events or '').split(',') if x.strip()])
                r_.summary = f"lead vetting: {len(rep['events'])} event(s)"
        except SystemExit:
            raise
        except Exception as exc:  # noqa: BLE001
            print(f"vet: {type(exc).__name__}: {exc}", file=sys.stderr)
            return 1
        finally:
            ledger.close()
        print((Path(spec.get("outputs", f"campaigns/{spec['campaign_id']}/")) / "vetting" / "VETTING.md").as_posix())
        return 0
    ledger = Ledger(_ledger_path(a.ledger))
    try:
        out = run(a.spec, ledger=ledger, root=root, force=a.force, until=a.until)
    except Exception as exc:  # noqa: BLE001 - a failed step is already ledgered; report it cleanly
        print(f"run: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    finally:
        ledger.close()
    print(json.dumps({k: out[k] for k in ("campaign_id", "steps_run", "complete", "record")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
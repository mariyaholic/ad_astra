"""``python -m cygnus.campaign {run,check} <spec.yaml>``"""

from __future__ import annotations

import argparse
import json
import sys

from ..config import ledger_path
from ..ledger import Ledger
from .runner import SpecError, load_spec, run


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
    a = ap.parse_args(argv)
    try:
        spec = load_spec(a.spec)
    except SpecError as exc:
        print(f"spec error: {exc}", file=sys.stderr)
        return 2
    if a.cmd == "check":
        print(json.dumps({"campaign_id": spec["campaign_id"], "steps": [next(iter(s)) for s in spec["steps"]]}, indent=2))
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

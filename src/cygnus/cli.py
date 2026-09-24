"""Minimal operator CLI.

Usage (venv at ``D:/AO_Artifacts/cygnus_scratch/venv``):

    python -m cygnus.cli doctor
    python -m cygnus.cli doctor --full        # include optional-stack flags
    python -m cygnus.cli dossier <candidate_record.json>
    python -m cygnus.cli close-stale-runs --older-than-hours 6 --note "..."

``doctor`` is the standing verification probe: scratch writability, ledger
health, optional dependency availability — stdout JSON, exit code 0/1.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Sequence

_OPTIONAL_STACK = ("astroquery", "astropy", "lightkurve", "photutils", "wotan", "celerite2")


def _probe_scratch() -> dict:
    from .config import scratch_dir

    p = scratch_dir()
    probe = p / ".cygnus_probe"
    try:
        probe.write_text("ok", encoding="ascii")
        ok = probe.read_text(encoding="ascii") == "ok"
        probe.unlink()
        return {"path": str(p), "writable": ok}
    except Exception as exc:  # surface, don't hide
        return {"path": str(p), "writable": False, "error": str(exc)}


def _probe_ledger() -> dict:
    from .config import ledger_path
    from .ledger import Ledger

    path = ledger_path()
    ledger = Ledger(path)
    try:
        count = ledger.count_products()
        return {"path": str(path), "open": True, "products": count}
    finally:
        ledger.close()


def _doctor(full: bool = False) -> int:
    from . import __version__

    checks: dict = {"version": __version__}
    checks["scratch"] = _probe_scratch()
    checks["ledger"] = _probe_ledger()
    if full:
        checks["optional_stack"] = {
            mod: importlib.util.find_spec(mod) is not None for mod in _OPTIONAL_STACK
        }
    print(json.dumps(checks, indent=2))
    healthy = checks["scratch"].get("writable") and checks["ledger"].get("open")
    return 0 if healthy else 1


def _dossier(path: str) -> int:
    from .candidate_record import CandidateRecord
    from .reporting.dossier import emit_dossier_markdown

    record = CandidateRecord.load(Path(path))
    print(emit_dossier_markdown(record))
    return 0


def _close_stale(hours: float, note: str, dry_run: bool) -> int:
    from datetime import datetime, timedelta, timezone

    from .config import ledger_path
    from .ledger import Ledger

    cutoff = (datetime.now(timezone.utc) - timedelta(hours=hours)).strftime("%Y-%m-%dT%H:%M:%SZ")
    ledger = Ledger(ledger_path())
    try:
        stale = [r for r in ledger.runs() if r["status"] == "open" and r["started_utc"] < cutoff]
        if dry_run:
            print(json.dumps({"cutoff_utc": cutoff, "would_close": [r["id"] for r in stale]}, indent=2))
            return 0
        ids = ledger.close_stale_runs(started_before_utc=cutoff, note=note)
        print(json.dumps({"cutoff_utc": cutoff, "closed_as_aborted": ids}, indent=2))
        return 0
    finally:
        ledger.close()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="cygnus", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_doctor = sub.add_parser("doctor", help="verify scratch/ledger/optional stack")
    p_doctor.add_argument("--full", action="store_true", help="include optional-stack flags")
    p_dossier = sub.add_parser("dossier", help="render dossier from a candidate record JSON")
    p_dossier.add_argument("record_json")
    p_stale = sub.add_parser("close-stale-runs", help="mark long-open runs as aborted (process died without closing)")
    p_stale.add_argument("--older-than-hours", type=float, default=6.0)
    p_stale.add_argument("--note", required=True, help="why these runs are being closed (stored in each run's summary)")
    p_stale.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.cmd == "doctor":
        return _doctor(full=args.full)
    if args.cmd == "dossier":
        return _dossier(args.record_json)
    if args.cmd == "close-stale-runs":
        return _close_stale(args.older_than_hours, args.note, args.dry_run)
    parser.error(f"unknown command {args.cmd!r}")
    return 2


if __name__ == "__main__":
    sys.exit(main())

"""Loaders that turn allowlisted worktree sources into public view models.

Every loader returns plain dicts of *already sanitized* values. Missing
metadata stays ``None`` — templates render it as "not recorded" — so the site
never manufactures a size, date, license or uncertainty.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ..candidate_record import AUDIT_STATES, EVIDENCE_LEVELS, CandidateRecord
from ..ledger import Ledger
from ..reporting.dossier import emit_dossier_markdown
from . import markdown
from .safety import redact
from .schema import PublicationError


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def mtime_utc(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ------------------------------------------------------------------ documents
def load_document(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    public_text = redact(raw)
    rendered = markdown.render(public_text, demote_h1=True, unlink_relative=True)
    data = public_text.encode("utf-8")
    maintained = re.search(r"Maintained:\s*(\d{4}-\d{2}-\d{2})", raw)
    return {
        "title": rendered.title or path.stem,
        "html": rendered.html,
        "toc": rendered.toc,
        "text": public_text,
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "redacted": public_text != raw,
        "maintained": maintained.group(1) if maintained else None,
        "source_modified_utc": mtime_utc(path),
        "filename": path.name,
    }


# ----------------------------------------------------------- module register
_STATUS_CLASS = (
    ("live-verified", "verified"),
    ("implemented", "implemented"),
    ("minimal", "planned"),
    ("designed", "planned"),
    ("sprint", "planned"),
)


def classify_module_status(status: str) -> str:
    low = status.lower()
    for needle, cls in _STATUS_CLASS:
        if needle in low:
            return cls
    return "unknown"


def load_module_register(path: Path, heading: str) -> list[dict[str, str]]:
    """Parse the pipe table under ``## <heading>`` (the build-status source of truth)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.lstrip("#").strip().startswith(heading))
    except StopIteration as exc:
        raise PublicationError(f"heading {heading!r} not found in {path.name}") from exc
    rows: list[dict[str, str]] = []
    header: list[str] | None = None
    for line in lines[start + 1:]:
        s = line.strip()
        if s.startswith("#"):
            break
        if not s.startswith("|"):
            if header:
                break
            continue
        cells = markdown._split_row(s)
        if header is None:
            header = [c.lower() for c in cells]
        elif not set(s) <= set("|-: "):
            row = dict(zip(header, cells))
            module = row.get("module", "").strip("`")
            status = re.sub(r"\*\*", "", row.get("status", ""))
            rows.append({
                "module": module,
                "function": row.get("function", ""),
                "status": status,
                "status_class": classify_module_status(status),
                "function_html": markdown.inline(row.get("function", "")),
                "status_html": markdown.inline(status),
            })
    if not rows:
        raise PublicationError(f"no module table under {heading!r} in {path.name}")
    return rows


# Campaign steps implemented by a register row whose module path does not contain the step
# name (e.g. the four screen steps all live in ``campaign/``). Explicit so the campaign pages
# never render an executed step as "status unknown"; a step absent from this map and the
# register resolves to None, which the pages must show honestly.
STEP_MODULE_ALIASES: dict[str, str] = {
    "target_queue": "targets.py",
    "fetch_products": "campaign/",
    "calibrate_screen": "campaign/",
    "residual_screen": "campaign/",
    "bls_recovery": "campaign/",
    "known_signal_recovery": "campaign/",
    "period_aliases": "campaign/",
    "prior_art": "priorart.py",
    "dossier": "reporting/dossier.py",
}


def _module_token_match(module: str, token: str) -> bool:
    if token.endswith("/"):
        return module.endswith(token)
    return module == token or module.endswith("/" + token) or module.rsplit("/", 1)[-1].removesuffix(".py") == token


def module_for_step(step: str, register: list[dict[str, str]]) -> dict[str, str] | None:
    """Match a campaign step (e.g. ``ingest.mast``, ``detrend_lab``) to a register row."""
    token = STEP_MODULE_ALIASES.get(step)
    if token:
        for row in register:
            if _module_token_match(row["module"], token):
                return row
    key = step.replace(".", "/")
    for row in register:
        mod = row["module"]
        stem = mod.rsplit("/", 1)[-1].removesuffix(".py")
        if mod.removesuffix(".py").endswith(key) or stem == step or (
            step == "dossier" and mod.endswith("reporting/dossier.py")
        ):
            return row
    return None


# ------------------------------------------------------------------ campaign
def load_campaign(path: Path, status_override: str | None = None) -> dict[str, Any]:
    import yaml  # site extra; ships with the science stack

    raw = path.read_text(encoding="utf-8")
    spec = yaml.safe_load(raw) or {}
    # YAML drops comments, but the spec documents each step inline; keep them.
    step_notes: dict[str, str] = {}
    field_notes: dict[str, str] = {}
    for line in raw.splitlines():
        m = re.match(r"^\s*-\s*([\w.]+)\s*#\s*(.+)$", line)
        if m:
            step_notes[m.group(1)] = m.group(2).strip()
        m = re.match(r"^\s*(\w+):\s*([^#]*?)\s*#\s*(.+)$", line)
        if m:
            field_notes[m.group(1)] = m.group(3).strip()
    public_text = redact(raw)
    data = public_text.encode("utf-8")
    thresholds = [
        {"name": k, "value": v, "note": field_notes.get(k)}
        for k, v in (spec.get("thresholds") or {}).items()
    ]
    pool = spec.get("target_pool") or {}
    # cygnus.campaign/1 specs: steps are one-key mappings, targets a list of {name, ...}
    steps = [next(iter(x)) if isinstance(x, dict) else str(x) for x in spec.get("steps") or []]
    queue = next((next(iter(x.values())) for x in spec.get("steps") or [] if isinstance(x, dict) and "target_queue" in x), None)
    targets = [t.get("name") if isinstance(t, dict) else t for t in (spec.get("targets") or pool.get("targets") or [])]
    return {
        "id": str(spec.get("campaign") or spec.get("campaign_id") or path.stem),
        "objective": redact(str(spec.get("objective") or "")).strip() or None,
        "domain": spec.get("domain"),
        "status": str(spec.get("status") or status_override or "unknown"),
        "status_note": field_notes.get("status"),
        "target_source": pool.get("source") or ((queue or {}).get("source") if queue else None),
        "target_source_note": field_notes.get("source"),
        "targets": targets,
        "steps": [{"name": s, "note": step_notes.get(s)} for s in steps],
        "thresholds": thresholds,
        "notes": redact(str(spec.get("notes") or "")).strip() or None,
        "text": public_text,
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "filename": path.name,
        "source_modified_utc": mtime_utc(path),
    }


# ---------------------------------------------------------- archive manifests
STATE_LABELS = {
    "local": ("held", "Retrieved; held in private project storage"),
    "drive_only": ("held", "Retrieved and checksum-verified; held in private project storage"),
    "excluded": ("excluded", "Not retrieved (excluded by query result or budget)"),
    "failed": ("failed", "Retrieval attempted and failed"),
}


def load_archive_manifest(path: Path) -> dict[str, Any]:
    snap = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for r in snap.get("rows", []):
        cls, label = STATE_LABELS.get(r.get("state", ""), ("unknown", "State not recorded"))
        url = r.get("url") or ""
        rows.append({**r, "state_class": cls, "state_label": label,
                     "archive_link": url if url.startswith("https://") else None})
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["state_class"]] = counts.get(r["state_class"], 0) + 1
    held_bytes = [r["bytes"] for r in rows if r["state_class"] == "held" and r.get("bytes")]
    return {
        "service": snap.get("service"),
        "pack_dir": snap.get("pack_dir"),
        "snapshot_utc": snap.get("snapshot_utc"),
        "source_manifest": snap.get("source_manifest"),
        "source_sha256": snap.get("source_sha256"),
        "source_modified_utc": snap.get("source_modified_utc"),
        "rows": rows,
        "counts": counts,
        "held_bytes": sum(held_bytes) if held_bytes else None,
        "licenses": sorted({r["license"] for r in rows if r.get("license")}),
    }


# -------------------------------------------------------------- ledger views
def _product_index(ledger: Ledger) -> dict[str, dict[str, Any]]:
    return {p["product_id"]: p for p in ledger.products()}


def public_product(p: dict[str, Any]) -> dict[str, Any]:
    """Allowlisted product fields; ``local_path`` and ``extra_json`` never leave."""
    url = p.get("url") or ""
    return {
        "archive": p["archive"],
        "product_id": p["product_id"],
        "archive_link": url if url.startswith("https://") else None,
        "checksum": p.get("checksum"),
        "license": p.get("license"),
        "retrieved_utc": p.get("retrieved_utc"),
    }


def resolve_product_refs(refs: list[str], index: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """Exact-match product references; report prefix matches as unresolved, never as matches."""
    out = []
    for ref in refs:
        if ref in index:
            out.append({"ref": ref, "resolved": True, "product": public_product(index[ref])})
        else:
            near = sorted(pid for pid in index if pid.startswith(ref))
            out.append({"ref": ref, "resolved": False, "possible": near[:3]})
    return out


def public_run(run: dict[str, Any]) -> dict[str, Any]:
    return {k: run.get(k) for k in (
        "id", "script", "config_hash", "code_version", "seed", "started_utc",
        "finished_utc", "status", "summary")}


def load_ledger_run(ledger: Ledger, run_id: int) -> dict[str, Any]:
    run = public_run(ledger.run(run_id))
    index = _product_index(ledger)
    meas = []
    for m in ledger.measurements_for_run(run_id):
        refs = json.loads(m.get("product_ids_json") or "[]")
        meas.append({
            "id": m["id"], "name": m["name"], "value": m["value"], "unit": m["unit"],
            "uncertainty": m["uncertainty"], "method": m["method"], "notes": m["notes"],
            "candidate_id": m["candidate_id"] or None, "created_utc": m["created_utc"],
            "products": resolve_product_refs(refs, index),
        })
    run["measurements"] = meas
    return run


def load_ledger_runs(ledger: Ledger, script: str) -> dict[str, Any]:
    runs = [public_run(r) for r in ledger.runs(script)]
    counts: dict[str, int] = {}
    for r in runs:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    return {"script": script, "runs": runs, "counts": counts}


def ledger_overview(ledger: Ledger) -> dict[str, Any]:
    """Counts only — the ledger itself is never exported wholesale."""
    q = ledger.db.execute
    by_archive = [
        {"archive": a, "n": n}
        for a, n in q("SELECT archive, COUNT(*) FROM products GROUP BY archive ORDER BY archive")
    ]
    return {
        "products": int(q("SELECT COUNT(*) FROM products").fetchone()[0]),
        "runs": int(q("SELECT COUNT(*) FROM runs").fetchone()[0]),
        "measurements": int(q("SELECT COUNT(*) FROM measurements").fetchone()[0]),
        "candidates": int(q("SELECT COUNT(*) FROM candidates").fetchone()[0]),
        "prior_art": int(q("SELECT COUNT(*) FROM prior_art").fetchone()[0]),
        "products_by_archive": by_archive,
    }


# ---------------------------------------------------------------- candidates
EVIDENCE_LABELS = {
    "unverified_lead": "Unverified lead",
    "vetted_candidate": "Vetted candidate",
    "independently_supported_candidate": "Independently supported candidate",
    "established": "Established object / phenomenon",
}
AUDIT_LABELS = {
    "passed": "Passed", "failed": "Failed", "inconclusive": "Inconclusive", "not_tested": "Not tested",
}


def load_candidate(path: Path, ledger: Ledger | None) -> dict[str, Any]:
    """Load a CandidateRecord and apply the package's own claim rules.

    ``validate_strict`` (evidence pinning, non-empty provenance/audit) runs
    exactly as it does for dossier emission; the ledger row, if any, must
    agree on evidence level. The downloadable dossier is the package's own
    ``emit_dossier_markdown`` output.
    """
    record = CandidateRecord.load(path)
    record.validate_strict()
    if record.evidence_level == "established":
        raise PublicationError(
            f"{record.candidate_id}: 'established' requires external confirmation "
            "handled outside the toolchain; the site will not publish it from a record"
        )
    ledger_row = ledger.get_candidate(record.candidate_id) if ledger else None
    if ledger_row and ledger_row["evidence_level"] != record.evidence_level:
        raise PublicationError(
            f"{record.candidate_id}: record says {record.evidence_level!r} but ledger says "
            f"{ledger_row['evidence_level']!r}; reconcile before publishing"
        )
    prior = ledger.prior_art_for(record.candidate_id) if ledger else []
    measurements = ledger.measurements_for_candidate(record.candidate_id) if ledger else []
    index = _product_index(ledger) if ledger else {}
    dossier_md = redact(emit_dossier_markdown(record, ledger))
    measured = []
    for name in sorted(record.measured):
        spec = record.measured[name]
        if isinstance(spec, dict):
            measured.append({"name": name, **{k: spec.get(k) for k in ("value", "unit", "uncertainty", "method")}})
        else:
            measured.append({"name": name, "value": spec, "unit": None, "uncertainty": None, "method": None})
    return {
        "id": record.candidate_id,
        "evidence_level": record.evidence_level,
        "evidence_label": EVIDENCE_LABELS[record.evidence_level],
        "evidence_rank": EVIDENCE_LEVELS.index(record.evidence_level),
        "bottom_line": record.bottom_line,
        "provenance": {k: redact(str(v)) for k, v in sorted(record.provenance.items())},
        "measured": measured,
        "audit": [{"test": k, "state": v, "label": AUDIT_LABELS[v]} for k, v in sorted(record.audit.items())],
        "audit_counts": {s: sum(1 for v in record.audit.values() if v == s) for s in AUDIT_STATES},
        "catalog_audit": {k: redact(str(v)) for k, v in sorted(record.catalog_audit.items())},
        "competing": list(record.competing),
        "reproduction": {k: redact(str(v)) for k, v in sorted(record.reproduction.items())},
        "next_test": record.next_test,
        "coordinates": ledger_row.get("coordinates") if ledger_row else None,
        "prior_art": [
            {k: row[k] for k in ("gate", "service", "query", "retrieved_utc", "result")} for row in prior
        ],
        "ledger_measurements": [
            {k: m.get(k) for k in ("name", "value", "unit", "uncertainty", "method", "run_id", "script")}
            | {"products": resolve_product_refs(json.loads(m.get("product_ids_json") or "[]"), index)}
            for m in measurements
        ],
        "dossier_md": dossier_md,
    }

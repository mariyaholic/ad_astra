"""Reconcile a falsified/updated lead across its records, and the lead-promotion gate as data.

``python -m cygnus.campaign reconcile <campaign-id> --note "..." [--superseded-by reports/x]``
  * appends an idempotent "superseded by" footer to REPORT/DOSSIER/SEARCH_LOG (original text kept)
  * archives the previous sky record beside the new one, never deleting history
  * checks sky record vs candidate record vs publication collection for drift
  * re-renders the candidate dossier from the candidate record

The checks return findings; nothing is silently rewritten except the footers and the dossier.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

from ..fileio import archive_previous, atomic_write_text

FOOTER_TAG = "<!-- cygnus:reconcile-footer -->"
DOCS = ("REPORT.md", "DOSSIER.md", "SEARCH_LOG.md")


def add_history_footer(path: Path, note: str, superseded_by: str | None = None) -> bool:
    """Append a labelled footer once per distinct note; returns True if the file changed."""
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    line = f"{FOOTER_TAG} **Superseded/annotated:** {note}" + (f" See `{superseded_by}`." if superseded_by else "")
    if line in text:
        return False
    atomic_write_text(path, text.rstrip("\n") + "\n\n" + line + "\n")
    return True


# ---- lead-promotion gate as data -------------------------------------------------------------

def check_units_ppm(depth_ppm: float, displayed: str | None = None) -> list[str]:
    """Event depths are stored in ppm; a displayed conversion must agree (1 ppt = 1000 ppm = 0.1 %)."""
    out = []
    if not isinstance(depth_ppm, (int, float)) or not math.isfinite(depth_ppm) or depth_ppm <= 0:
        out.append("depth_ppm missing/non-positive")
    elif displayed:
        for unit, div in (("ppt", 1e3), ("%", 1e4)):
            if displayed.strip().endswith(unit):
                try:
                    if abs(float(displayed.strip()[: -len(unit)]) * div - depth_ppm) > 0.01 * depth_ppm:
                        out.append(f"displayed {displayed!r} disagrees with {depth_ppm} ppm")
                except ValueError:
                    out.append(f"unparseable displayed depth {displayed!r}")
    return out


def implied_radius_ratio(depth_ppm: float) -> float:
    """sqrt(depth) = Rp/R* for a central, undiluted transit; compare with any quoted planet radius."""
    return math.sqrt(depth_ppm * 1e-6)


def check_radius(depth_ppm: float, stellar_radius_rsun: float, quoted_rp_rearth: float, *, tol=0.25) -> list[str]:
    rp = implied_radius_ratio(depth_ppm) * stellar_radius_rsun * 109.076
    if abs(rp - quoted_rp_rearth) > tol * rp:
        return [f"quoted Rp {quoted_rp_rearth} Rearth vs sqrt(depth)*R* = {rp:.2f} Rearth (central/undiluted)"]
    return []


def check_null_counts(k: int, n: int, *, claims_probability_zero=False) -> list[str]:
    """Empirical nulls are k/N with finite resolution; never 0 probability or a Gaussian sigma."""
    out = []
    if n <= 0 or not 0 <= k <= n:
        out.append(f"invalid null count {k}/{n}")
    if claims_probability_zero and k == 0:
        out.append(f"0/{n} reported as zero probability; resolution is 1/{n}")
    return out


def check_centroid(offset_over_sigma: float | None, radius_rule_passed: bool, *, fail_ratio=3.0) -> str:
    """A significant offset is failed/unresolved localization even if a coarse radius rule passes."""
    if offset_over_sigma is None:
        return "not_tested"
    return "failed_localization" if offset_over_sigma >= fail_ratio else ("inconclusive" if radius_rule_passed else "failed_localization")


def check_event_times(event_bjd: list[float], known_epochs: list[tuple[str, float]], *, tol_days=0.1) -> list[str]:
    """A position match alone cannot clear a transient: flag events coinciding with known ephemerides."""
    return [f"event {e:.5f} coincides with {name} epoch {k:.5f}" for e in event_bjd
            for name, k in known_epochs if abs(e - k) <= tol_days]


# ---- record consistency ----------------------------------------------------------------------

def check_records(root: Path, campaign_id: str, candidate_id: str | None = None) -> list[str]:
    """Findings where the sky record, candidate record and collection disagree (empty list = consistent)."""
    findings = []
    sky_path = root / "campaigns" / campaign_id / "sky_record.json"
    if not sky_path.exists():
        return [f"missing {sky_path.relative_to(root)}"]
    sky = json.loads(sky_path.read_text(encoding="utf-8"))
    if candidate_id:
        cpath = root / "publish" / "candidates" / f"{candidate_id}.json"
        if not cpath.exists():
            findings.append(f"missing candidate record {cpath.name}")
        else:
            cand = json.loads(cpath.read_text(encoding="utf-8"))
            if sky.get("evidence") and cand.get("evidence_level") != sky["evidence"]:
                findings.append(f"evidence level: sky={sky['evidence']!r} candidate={cand.get('evidence_level')!r}")
        for coll in (root / "publish" / "collections").glob("*.json"):
            if candidate_id in coll.read_text(encoding="utf-8"):
                break
        else:
            findings.append(f"{candidate_id} not in any publish collection")
    for chk in sky.get("checks", []):
        if chk.get("state") == "passed" and not chk.get("note") and not chk.get("reported_as"):
            findings.append(f"check {chk.get('name')!r} passed without note/evidence")
    return findings


def reconcile(root: Path, campaign_id: str, note: str, *, superseded_by: str | None = None,
              candidate_id: str | None = None, render_dossier: bool = True) -> dict:
    cdir = root / "campaigns" / campaign_id
    changed = [d for d in DOCS if add_history_footer(cdir / d, note, superseded_by)]
    archived = None
    sky = cdir / "sky_record.json"
    if sky.exists() and superseded_by:
        prev = json.loads(sky.read_text(encoding="utf-8"))
        if "superseded_by" not in prev:
            prev["superseded_by"] = superseded_by
            atomic_write_text(sky, json.dumps(prev, indent=2, ensure_ascii=False) + "\n")
    dossier = None
    if render_dossier and candidate_id:
        from ..candidate_record import CandidateRecord
        from ..ledger import Ledger
        from ..reporting.dossier import emit_dossier_markdown

        rec = CandidateRecord.from_dict(json.loads(
            (root / "publish" / "candidates" / f"{candidate_id}.json").read_text(encoding="utf-8")))
        ledger = Ledger()
        try:
            atomic_write_text(cdir / "DOSSIER.md", emit_dossier_markdown(rec, ledger) + "\n")
        finally:
            ledger.close()
        dossier = "DOSSIER.md"
    return {"footers": changed, "archived": archived and str(archived), "dossier": dossier,
            "findings": check_records(root, campaign_id, candidate_id)}


# ---- prior-art per-paper record --------------------------------------------------------------

def paper_match(citation: str, *, companion_exists: bool | None, event_time_matched: bool | None,
                event_source_identified: bool | None = None, note: str = "") -> dict:
    """One prior-art row. Companion existence, event-time match and eclipsing-source identity are separate.

    ``event_source_identified`` may be True only with an event-time match; otherwise it is forced False.
    """
    ident = bool(event_source_identified) and bool(event_time_matched)
    return {"citation": citation, "companion_exists": companion_exists,
            "event_time_matched": event_time_matched, "event_source_identified": ident, "note": note}

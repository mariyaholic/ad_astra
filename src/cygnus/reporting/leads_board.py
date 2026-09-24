"""Leads board — evidence-level ranked table from the ledger.

Scaffold ranking is by evidence level only; Sprint 1 adds scientific ranking
(completeness-curve weight, next-test discriminative value) as explicitly
configured scoring — never hidden heuristics.
"""

from __future__ import annotations

from ..ledger import Ledger

_ORDER = {
    "unverified_lead": 0,
    "vetted_candidate": 1,
    "independently_supported_candidate": 2,
    "established": 3,
}


def render_leads_table(ledger: Ledger) -> str:
    rows = ledger.candidates()
    if not rows:
        return "No candidates in ledger."
    # Highest evidence first; ties get lexical order.
    rows.sort(key=lambda r: (-_ORDER.get(r["evidence_level"], -1), r["candidate_id"]))
    lines = [
        "### CYGNUS RANKED LEADS",
        "",
        "| candidate | evidence | summary | updated |",
        "| --- | --- | --- | --- |",
    ]
    for row in rows:
        summary = (row["summary"] or "(none recorded)").replace("|", "/")
        lines.append(
            f"| {row['candidate_id']} | {row['evidence_level']} | {summary} "
            f"| {row['updated_utc']} |"
        )
    lines += [
        "",
        "*Scaffold ranking = evidence level only; calibrated scoring lands with "
        "injection-recovery completeness curves (Sprint 1).*",
    ]
    return "\n".join(lines)

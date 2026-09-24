"""Dossier renderer — AGENTS.md 'Required outputs' schema.

Never invents values: any field the evidence does not support renders
'(none recorded)'; strict validation raises rather than silently emitting an
empty dossier. Prior-Art Gate rows come straight from the ledger.
"""

from __future__ import annotations

from ..candidate_record import _UNSET, CandidateRecord
from ..ledger import Ledger


def emit_dossier_markdown(record: CandidateRecord, ledger: Ledger | None = None) -> str:
    """Render the dossier; raises CandidateRecordError on rule violations."""
    record.validate_strict()

    prior_rows = ledger.prior_art_for(record.candidate_id) if ledger is not None else []

    lines: list[str] = [
        "### CYGNUS CANDIDATE DOSSIER",
        "",
        f"**Working identifier:** {record.candidate_id} "
        "(local working ID — not an official designation)",
        f"**Evidence level:** {record.evidence_level}",
        f"**Bottom line:** {record.bottom_line or _UNSET}",
        "",
        "#### 1. Provenance",
        "",
    ]
    if record.provenance:
        for key in sorted(record.provenance):
            lines.append(f"- **{key}:** {record.provenance[key]}")
    else:
        lines.append(_UNSET)
    if prior_rows:
        lines += ["", "Prior-art gate results (ledger-pinned):", ""]
        for row in prior_rows:
            lines.append(
                f"- {row['gate']}/{row['service']}: {row['result']} "
                f"(as of {row['retrieved_utc']})"
            )

    lines += ["", "#### 2. Measured signal", ""]
    if record.measured:
        for name in sorted(record.measured):
            spec = record.measured[name]
            if isinstance(spec, dict):
                parts = [
                    f"{part}={spec[part]}"
                    for part in ("value", "unit", "uncertainty", "method")
                    if part in spec
                ]
                lines.append(f"- **{name}:** " + "; ".join(parts or [str(spec)]))
            else:
                lines.append(f"- **{name}:** {spec}")
    else:
        lines.append(_UNSET)

    lines += ["", "#### 3. Artifact audit", "", "| test | state |", "| --- | --- |"]
    for key in sorted(record.audit):
        lines.append(f"| {key} | {record.audit[key]} |")
    lines += [
        "",
        "(States: passed | failed | inconclusive | not_tested — 'not_tested' "
        "never supports an evidence upgrade.)",
        "",
        "#### 4. Catalog and literature audit",
        "",
    ]
    if record.catalog_audit:
        for key in sorted(record.catalog_audit):
            lines.append(f"- **{key}:** {record.catalog_audit[key]}")
    else:
        lines.append(_UNSET)

    lines += ["", "#### 5. Competing explanations", ""]
    if record.competing:
        lines += [f"- {item}" for item in record.competing]
    else:
        lines.append(_UNSET)

    lines += ["", "#### 6. Reproduction", ""]
    if record.reproduction:
        for key in sorted(record.reproduction):
            lines.append(f"- **{key}:** {record.reproduction[key]}")
    else:
        lines.append(_UNSET)

    lines += ["", "#### 7. Follow-up", "", record.next_test or _UNSET]

    lines += [
        "",
        "---",
        "*Generated from ledger/candidate records only; any field the evidence "
        "does not support renders '(none recorded)' rather than a fabricated "
        "value.*",
    ]
    return "\n".join(lines)

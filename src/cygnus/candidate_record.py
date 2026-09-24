"""CandidateRecord — the standard output object of every Layer-2 detector.

Invariants (AGENTS.md 'Evidence levels' + Prior-Art Gate):

* ``audit`` values are limited to ``passed|failed|inconclusive|not_tested``;
* any audit state other than ``passed`` pins ``evidence_level`` to
  ``unverified_lead`` (a module with unverified artifact tests cannot claim a
  vetted candidate);
* ``established`` is intentionally unreachable inside this package; claiming it
  requires external confirmation handled outside the toolchain;
* a working identifier is required and must look like ``CYG-...`` — it is
  explicitly NOT an official designation;
* rendering never invents values: absent sections render "(none recorded)"
  and strict validation raises rather than silently emitting an empty dossier.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field, fields
from pathlib import Path
from typing import Any

AUDIT_STATES = ("passed", "failed", "inconclusive", "not_tested")

EVIDENCE_LEVELS = (
    "unverified_lead",
    "vetted_candidate",
    "independently_supported_candidate",
    "established",
)

_CAND_ID_RE = re.compile(r"^CYG-[A-Za-z0-9._/-]+$")

_UNSET = "(none recorded)"


class CandidateRecordError(ValueError):
    """Raised when a candidate record would violate the worktree's claim rules."""


@dataclass
class CandidateRecord:
    candidate_id: str
    evidence_level: str = "unverified_lead"
    provenance: dict[str, Any] = field(default_factory=dict)
    measured: dict[str, Any] = field(default_factory=dict)
    audit: dict[str, str] = field(default_factory=dict)
    catalog_audit: dict[str, str] = field(default_factory=dict)
    competing: list[str] = field(default_factory=list)
    reproduction: dict[str, str] = field(default_factory=dict)
    next_test: str | None = None
    bottom_line: str | None = None

    # ------------------------------------------------------------- validation
    def __post_init__(self) -> None:
        self._check_identity()
        if self.evidence_level not in EVIDENCE_LEVELS:
            raise CandidateRecordError(
                f"evidence_level {self.evidence_level!r} not in {EVIDENCE_LEVELS}"
            )
        for key, value in self.audit.items():
            if value not in AUDIT_STATES:
                raise CandidateRecordError(
                    f"audit['{key}'] = {value!r} not in {AUDIT_STATES}"
                )

    def _check_identity(self) -> None:
        if not _CAND_ID_RE.match(self.candidate_id):
            raise CandidateRecordError(
                "candidate_id must be a working 'CYG-*' identifier "
                f"(not an official designation), got {self.candidate_id!r}"
            )
        if any(ch.isspace() for ch in self.candidate_id):
            raise CandidateRecordError("candidate_id must not contain whitespace")

    def enforce_evidence_rule(self) -> None:
        """A non-passed audit item pins the record to 'unverified_lead'."""
        failing = sorted(k for k, v in self.audit.items() if v != "passed")
        if failing and self.evidence_level != "unverified_lead":
            raise CandidateRecordError(
                f"audit items {failing} are not all 'passed'; "
                f"evidence_level must be 'unverified_lead', got {self.evidence_level!r}"
            )

    def demote_if_unvetted(self) -> list[str]:
        """Force evidence level down instead of raising; returns failing keys."""
        failing = sorted(k for k, v in self.audit.items() if v != "passed")
        if failing:
            self.evidence_level = "unverified_lead"
        return failing

    def validate_strict(self) -> None:
        """Full pre-render checks: loud failure over silent fabrication."""
        self.enforce_evidence_rule()
        if not any(str(v).strip() for v in self.provenance.values() if v):
            raise CandidateRecordError(
                "provenance is empty: cite product references or prior-art "
                "sources before rendering a dossier"
            )
        if not self.audit:
            raise CandidateRecordError(
                "audit is empty: run the artifact audit, or record explicit "
                "'not_tested' entries"
            )

    # -------------------------------------------------------------------- I/O
    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "CandidateRecord":
        known = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in known})

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True)

    def save(self, path: str | Path) -> Path:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_json(), encoding="utf-8")
        return path

    @classmethod
    def load(cls, path: str | Path) -> "CandidateRecord":
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))

    # -------------------------------------------------------------- rendering
    def to_markdown(self) -> str:
        """Dossier skeleton in the AGENTS.md schema — never invents values."""
        self.validate_strict()
        lines: list[str] = [
            "### CYGNUS CANDIDATE DOSSIER",
            "",
            f"**Working identifier:** {self.candidate_id} "
            "(local working ID — not an official designation)",
            f"**Evidence level:** {self.evidence_level}",
            f"**Bottom line:** {self.bottom_line or _UNSET}",
            "",
            "#### 1. Provenance",
            "",
        ]
        if self.provenance:
            for key in sorted(self.provenance):
                lines.append(f"- **{key}:** {self.provenance[key]}")
        else:
            lines.append(_UNSET)

        lines += ["", "#### 2. Measured signal", ""]
        if self.measured:
            for name in sorted(self.measured):
                spec = self.measured[name]
                if isinstance(spec, dict):
                    parts = [
                        str(spec.get(part, _UNSET))
                        for part in ("value", "unit", "uncertainty", "method")
                        if part in spec
                    ]
                    lines.append(f"- **{name}:** " + "; ".join(parts))
                else:
                    lines.append(f"- **{name}:** {spec}")
        else:
            lines.append(_UNSET)

        lines += ["", "#### 3. Artifact audit", "", "| test | state |", "| --- | --- |"]
        for key in sorted(self.audit):
            lines.append(f"| {key} | {self.audit[key]} |")
        lines += ["", "(States: passed | failed | inconclusive | not_tested — "
                    "'not_tested' never supports an evidence upgrade.)", ""]

        lines += ["#### 4. Catalog and literature audit", ""]
        if self.catalog_audit:
            for key in sorted(self.catalog_audit):
                lines.append(f"- **{key}:** {self.catalog_audit[key]}")
        else:
            lines.append(_UNSET)

        lines += ["", "#### 5. Competing explanations", ""]
        if self.competing:
            lines += [f"- {item}" for item in self.competing]
        else:
            lines.append(_UNSET)

        lines += ["", "#### 6. Reproduction", ""]
        if self.reproduction:
            for key in sorted(self.reproduction):
                lines.append(f"- **{key}:** {self.reproduction[key]}")
        else:
            lines.append(_UNSET)

        lines += ["", "#### 7. Follow-up", ""]
        lines.append(self.next_test or _UNSET)
        lines += [
            "",
            "---",
            "*Generated from ledger/candidate records only; any field the "
            "evidence does not support renders '(none recorded)' rather than "
            "a fabricated value.*",
        ]
        return "\n".join(lines)

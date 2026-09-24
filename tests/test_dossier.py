import pytest

from cygnus.candidate_record import CandidateRecord, CandidateRecordError
from cygnus.reporting.dossier import emit_dossier_markdown
from cygnus.reporting.leads_board import render_leads_table


def _record():
    return CandidateRecord(
        candidate_id="CYG-CAND-2026-010",
        provenance={"MAST": ["proj-42"], "retrieved_utc": "2026-09-23T00:00:00Z"},
        measured={"modeled_depth": {"value": "420 ppm", "unit": "ppm", "method": "scaffold"}},
        audit={"centroid_stability": "passed", "jitter": "inconclusive"},
        catalog_audit={"VSX": "no match in catalogs searched (retrieved 2026-09-23)"},
        competing=["stellar activity", "BEB"],
        reproduction={"entry": "src/cygnus/ (scaffold)"},
        next_test="obtain second baseline epoch",
    )


def test_dossier_renders_all_sections_and_prior_art(ledger_factory):
    led = ledger_factory()
    led.add_prior_art(
        "ADS_literature",
        "not_tested (offline scaffold)",
        gate="prior_art",
        candidate_id="CYG-CAND-2026-010",
    )
    md = emit_dossier_markdown(_record(), ledger=led)
    for section in (
        "Measured signal",
        "Artifact audit",
        "Catalog and literature audit",
        "Competing explanations",
        "Reproduction",
        "Follow-up",
    ):
        assert section in md
    assert "ADS_literature" in md
    assert "not an official designation" in md


def test_dossier_measured_parts_render():
    md = emit_dossier_markdown(_record())
    assert "modeled_depth" in md and "value=420 ppm" in md


def test_dossier_refuses_empty_provenance():
    rec = CandidateRecord(candidate_id="CYG-CAND-2026-011", audit={"t": "passed"})
    with pytest.raises(CandidateRecordError):
        emit_dossier_markdown(rec)


def test_leads_table_ranks_by_evidence_level(ledger_factory):
    led = ledger_factory()
    led.add_candidate("CYG-CAND-2026-099", evidence_level="vetted_candidate", summary="cleaner")
    led.add_candidate("CYG-CAND-2026-001", evidence_level="unverified_lead", summary="raw")
    table = render_leads_table(led)
    assert table.index("CYG-CAND-2026-001") > table.index("CYG-CAND-2026-099")

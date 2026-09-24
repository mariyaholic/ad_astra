import pytest

from cygnus.candidate_record import AUDIT_STATES, CandidateRecord, CandidateRecordError


def _base(**kw):
    d = {
        "candidate_id": "CYG-CAND-2026-001",
        "provenance": {"MAST": ["proj-1"]},
        "audit": {"centroid_stability": "passed", "jitter_correlation": "not_tested"},
        "catalog_audit": {"VSX": "no match in catalogs searched (retrieved 2026-09-23)"},
    }
    d.update(kw)
    return CandidateRecord(**d)


def test_valid_record_constructs_and_markdown_renders():
    rec = _base()
    md = rec.to_markdown()
    assert "CYGNUS CANDIDATE DOSSIER" in md
    assert "unverified_lead" in md  # not_tested audit pins evidence level
    assert "none recorded" in md  # absent sections are explicit, not invented


def test_invalid_audit_state_rejected():
    with pytest.raises(CandidateRecordError):
        _base(audit={"centtroid": "passd"})


def test_bad_candidate_id_rejected():
    with pytest.raises(CandidateRecordError):
        _base(candidate_id="TOI-1234b sir please")


def test_nonpassed_audit_pins_unverified():
    rec = _base(evidence_level="vetted_candidate")
    with pytest.raises(CandidateRecordError):
        rec.enforce_evidence_rule()
    failing = rec.demote_if_unvetted()
    assert failing == ["jitter_correlation"]
    assert rec.evidence_level == "unverified_lead"


def test_strict_validation_refuses_empty_provenance():
    rec = _base(provenance={})
    with pytest.raises(CandidateRecordError):
        rec.to_markdown()


def test_save_load_roundtrip(tmp_path):
    rec = _base()
    p = rec.save(tmp_path / "rec.json")
    loaded = CandidateRecord.load(p)
    assert loaded == rec

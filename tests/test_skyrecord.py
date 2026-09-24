"""Sky records: every analysis in the worktree must be collectable by the sky explorer.

The first two tests run against the real worktree and are the guard for future work: adding a
campaign spec or a report without a sky_record.json that references it fails the suite.
The rest use synthetic fixtures in ``tmp_path``.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cygnus import skyrecord as sr

ROOT = Path(__file__).resolve().parents[1]


def test_real_worktree_records_are_valid():
    positions = sr.known_positions(ROOT)
    recs = sr.load_records(ROOT)
    assert recs, "expected at least one sky record in the worktree"
    problems = [p for r in recs for p in sr.validate(r, ROOT, positions)]
    assert problems == []


def test_every_campaign_and_report_has_a_sky_record():
    gaps = sr.coverage_gaps(ROOT, sr.load_records(ROOT))
    assert gaps == [], "add a sky_record.json (see docs/SKY_RECORDS.md):\n" + "\n".join(gaps)


def test_real_records_preserve_untested_checks():
    by_id = {r["id"]: r for r in sr.load_records(ROOT)}
    states = {c["state"] for c in by_id["tess-wasp12-residual-01"]["checks"]}
    assert "not_tested" in states
    assert by_id["tess-mono-01"]["status"] == "draft" and by_id["tess-mono-01"]["outcome"] == "not_run"


# ------------------------------------------------------------------ fixtures
def _root(tmp_path: Path) -> Path:
    (tmp_path / "campaigns").mkdir()
    (tmp_path / "reports").mkdir()
    pack = tmp_path / "docs" / "tier1_pack"
    pack.mkdir(parents=True)
    (pack / "NAME_RESOLUTIONS.json").write_text(json.dumps(
        {"Fixture Star": {"ok": True, "ra_deg": 10.0, "dec_deg": -20.0}}), encoding="utf-8")
    return tmp_path


def _series(path: Path, period: float, t0_btjd: float, depth: float) -> None:
    """Synthetic light curve: flat at 1000 with a box dip of the given depth, one bad-quality row."""
    lines = ["TIME,FLUX,QUALITY"]
    t = 0.0
    while t < 10.0:
        ph = ((t - t0_btjd) / period + 0.5) % 1 - 0.5
        f = 1000.0 * (1 - depth) if abs(ph * period * 24) < 1.0 else 1000.0
        lines.append(f"{t:.6f},{f:.6f},0")
        t += 2 / 1440
    lines.append("5.0,1.0,512")  # flagged row with absurd flux must be excluded
    path.write_bytes(("\n".join(lines) + "\n").encode())


def _record(**kw) -> dict:
    rec = {
        "schema": sr.SCHEMA, "id": "fixture-screen", "title": "Fixture screen", "kind": "residual screen",
        "status": "completed", "outcome": "bounded_null", "evidence": None, "date": "2026-01-02",
        "summary": "Synthetic.", "spec": None, "report": "reports/fixture-screen/REPORT.md", "search_log": None,
        "targets": [{"name": "Fixture Star", "position_source": "NAME_RESOLUTIONS"}],
        "products": [{"id": "fixture_lc.fits", "archive": "MAST"}],
        "checks": [{"name": "Injection–recovery", "state": "not_tested"}],
    }
    rec.update(kw)
    return rec


def _write(root: Path, rec: dict, where: str = "reports/fixture-screen") -> None:
    d = root / where
    d.mkdir(parents=True, exist_ok=True)
    (d / "REPORT.md").write_text("# Fixture\n", encoding="utf-8")
    (d / sr.FILENAME).write_text(json.dumps(rec), encoding="utf-8")


def test_new_report_without_record_is_a_gap(tmp_path):
    root = _root(tmp_path)
    (root / "reports" / "new-campaign").mkdir()
    (root / "reports" / "new-campaign" / "REPORT.md").write_text("# New\n", encoding="utf-8")
    (root / "campaigns" / "new-campaign.yaml").write_text("campaign_id: new-campaign\n", encoding="utf-8")
    gaps = sr.coverage_gaps(root, sr.load_records(root))
    assert "report without a sky record: reports/new-campaign/REPORT.md" in gaps
    assert "campaign spec without a sky record: campaigns/new-campaign.yaml" in gaps


def test_record_closes_the_gap_and_is_collected_without_code_changes(tmp_path):
    root = _root(tmp_path)
    (root / "campaigns" / "fixture-screen.yaml").write_text("campaign_id: fixture-screen\n", encoding="utf-8")
    (root / "reports" / "fixture-screen").mkdir()
    _series(root / "reports" / "fixture-screen" / "series.csv", period=2.0, t0_btjd=1.0, depth=0.01)
    rec = _record(spec="campaigns/fixture-screen.yaml", plots=[{
        "type": "fold", "file": "reports/fixture-screen/series.csv", "time_col": "TIME", "flux_col": "FLUX",
        "quality_col": "QUALITY", "time_offset_bjd": 2457000.0, "period_days": 2.0, "t0_bjd": 2457001.0,
        "window_hours": 4, "depth_window_hours": 0.5, "label": "Fixture fold"}])
    _write(root, rec)
    assert sr.coverage_gaps(root, sr.load_records(root)) == []
    got = sr.collect(root)
    [r] = got["by_target"]["Fixture Star"]
    [pd] = r["plot_data"]
    assert pd["depth"]["value"] == pytest.approx(0.01, rel=1e-6)   # derived from the CSV, not typed in
    assert all(abs(h) <= 4 for h, _ in pd["raw"])
    assert max(f for _, f in pd["raw"]) == pytest.approx(1.0)      # flagged row excluded
    assert "not a reported result" in pd["depth"]["method"]


def test_explicit_position_adds_a_new_sky_target(tmp_path):
    root = _root(tmp_path)
    _write(root, _record(targets=[{"name": "New Field", "ra_deg": 150.0, "dec_deg": 2.2, "frame": "ICRS",
                                   "epoch": "J2000.0", "position_source": "fixture"}]))
    got = sr.collect(root)
    assert got["extra_positions"]["New Field"]["ra_deg"] == 150.0


@pytest.mark.parametrize("change, message", [
    ({"checks": [{"name": "Centroid", "state": "partial"}]}, "state must be one of"),
    ({"checks": []}, "must list their checks"),
    ({"status": "draft"}, "draft cannot have an outcome"),
    ({"outcome": "candidate"}, "requires an evidence level"),
    ({"evidence": "Vetted candidate"}, "evidence level set but outcome"),
    ({"targets": [{"name": "Unknown Star"}]}, "not in NAME_RESOLUTIONS"),
    ({"targets": [{"name": "X", "ra_deg": 1.0, "dec_deg": 2.0}]}, "explicit positions need frame"),
    ({"report": "reports/missing/REPORT.md"}, "path does not exist"),
    ({"date": None}, "date YYYY-MM-DD required"),
])
def test_validation_rejects(tmp_path, change, message):
    root = _root(tmp_path)
    _write(root, _record())
    rec = _record(**change)
    problems = sr.validate(rec, root, sr.known_positions(root))
    assert any(message in p for p in problems), problems


def test_collect_refuses_invalid_records(tmp_path):
    root = _root(tmp_path)
    _write(root, _record(checks=[{"name": "c", "state": "probably fine"}]))
    with pytest.raises(ValueError, match="invalid sky records"):
        sr.collect(root)


def test_duplicate_ids_are_reported(tmp_path):
    root = _root(tmp_path)
    _write(root, _record(), "reports/a")
    _write(root, _record(), "reports/b")
    assert "duplicate sky record id: fixture-screen" in sr.coverage_gaps(root, sr.load_records(root))

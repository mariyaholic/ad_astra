"""Promotion path: a completed sandbox campaign copies into campaigns/ with provenance."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cygnus import skyrecord as sr
from cygnus.ledger import Ledger

from cygnus.multi import promote

REPO_ROOT = Path(__file__).resolve().parents[2]

SPEC = """schema: cygnus.campaign/1
campaign_id: exp-01
objective: Promotion fixture
outputs: campaigns/exp-01/
targets:
  - {name: T, ra_deg: 10.0, dec_deg: 20.0, frame: ICRS, epoch: J2000.0, position_source: fixture}
steps:
  - astrometric_vetting: {}
record:
  path: campaigns/exp-01/sky_record.json
  title: Fixture vetting
  kind: known-object test
  outcome: pipeline_check
  date: "2026-01-02"
  report: campaigns/exp-01/REPORT.md
  search_log: campaigns/exp-01/SEARCH_LOG.md
  summary: Fixture summary.
  checks:
    - {name: NSS, state: not_tested}
"""


def _record(status: str = "completed") -> dict:
    return {
        "schema": "cygnus.sky_record/1",
        "id": "exp-01",
        "title": "Fixture vetting",
        "kind": "known-object test",
        "status": status,
        "outcome": "pipeline_check" if status == "completed" else "not_run",
        "evidence": None,
        "date": "2026-01-02" if status == "completed" else None,
        "summary": "Fixture summary.",
        "spec": "campaigns/exp-01.yaml",
        "report": "campaigns/exp-01/REPORT.md",
        "search_log": "campaigns/exp-01/SEARCH_LOG.md",
        "targets": [{"name": "T", "ra_deg": 10.0, "dec_deg": 20.0, "frame": "ICRS",
                     "epoch": "J2000.0", "position_source": "fixture"}],
        "products": [],
        "checks": [{"name": "NSS", "state": "inconclusive"}] if status == "completed" else [],
        "generated_by": "cygnus_multi campaign runner",
        "generated_utc": "2026-01-02T00:00:00Z",
    }


@pytest.fixture
def worlds(tmp_path):
    root = tmp_path / "sandbox"
    worktree = tmp_path / "worktree"
    (root / "campaigns" / "exp-01").mkdir(parents=True)
    (root / "state").mkdir()
    (worktree / "campaigns").mkdir(parents=True)
    (worktree / "publish" / "collections").mkdir(parents=True)
    (root / "campaigns" / "exp-01.yaml").write_text(SPEC, encoding="utf-8")
    (root / "campaigns" / "exp-01" / "REPORT.md").write_text("# Fixture\n", encoding="utf-8")
    (root / "campaigns" / "exp-01" / "SEARCH_LOG.md").write_text("# Fixture log\n", encoding="utf-8")
    (root / "campaigns" / "exp-01" / "nss.json").write_text("{}\n", encoding="utf-8")
    (root / "campaigns" / "exp-01" / "sky_record.json").write_text(
        json.dumps(_record(), indent=1), encoding="utf-8")
    led = Ledger(root / "state" / "ledger.sqlite")
    rid = led.log_run("cygnus_multi:exp-01:astrometric_vetting")
    led.close_run(rid, "completed", "fixture run")
    led.close()
    return root, worktree


def test_promote_copies_rewrites_and_validates(worlds):
    root, worktree = worlds
    out = promote.promote(root, worktree, "exp-01", as_id="prod-01", note="fixture verification")
    assert out["spec"] == "campaigns/prod-01/SPEC.yaml" and out["runs"] == [1]

    spec_text = (worktree / "campaigns" / "prod-01" / "SPEC.yaml").read_text(encoding="utf-8")
    assert "campaign_id: prod-01" in spec_text and "outputs: campaigns/prod-01/" in spec_text
    assert not (worktree / "campaigns" / "prod-01.yaml").exists()

    rec = json.loads((worktree / "campaigns" / "prod-01" / "sky_record.json").read_text(encoding="utf-8"))
    assert rec["id"] == "prod-01"
    assert rec["spec"] == "campaigns/prod-01/SPEC.yaml"
    assert rec["report"] == "campaigns/prod-01/REPORT.md"
    assert rec["search_log"] == "campaigns/prod-01/SEARCH_LOG.md"
    assert rec["generated_by"] == "cygnus_multi campaign runner"
    assert sr.validate(rec, worktree) == []
    assert sr.coverage_gaps(worktree, [rec]) == []

    assert (worktree / "campaigns" / "prod-01" / "PROMOTED.md").is_file()
    assert "run #1" in (worktree / "campaigns" / "prod-01" / "PROMOTED.md").read_text(encoding="utf-8")

    coll = json.loads((worktree / "publish" / "collections" / "prod-01.json").read_text(encoding="utf-8"))
    assert coll["status"] == "draft" and coll["published"] is None
    assert any(i["kind"] == "campaign" and i["source"] == "campaigns/prod-01/SPEC.yaml" for i in coll["items"])
    assert any(i["kind"] == "file" and i["source"] == "campaigns/prod-01/nss.json" for i in coll["items"])


def test_promote_refuses_collision_and_incomplete(worlds):
    root, worktree = worlds
    promote.promote(root, worktree, "exp-01", as_id="prod-01")
    with pytest.raises(SystemExit, match="already exists"):
        promote.promote(root, worktree, "exp-01", as_id="prod-01")

    (root / "campaigns" / "exp-01" / "sky_record.json").write_text(
        json.dumps(_record("draft"), indent=1), encoding="utf-8")
    with pytest.raises(SystemExit, match="not 'completed'"):
        promote.promote(root, worktree, "exp-01", as_id="prod-02")


def test_dry_run_writes_nothing(worlds):
    root, worktree = worlds
    out = promote.promote(root, worktree, "exp-01", as_id="prod-01", dry_run=True)
    assert out["dry_run"] is True
    assert not (worktree / "campaigns" / "prod-01").exists()
    assert not (worktree / "publish" / "collections" / "prod-01.json").exists()

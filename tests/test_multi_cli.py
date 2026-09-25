"""CLI safety: sandbox confinement, ledger namespace, clean errors (offline)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from cygnus.multi import __main__ as cli

REPO_ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture()
def sandbox(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    (tmp_path / "campaigns").mkdir()
    return tmp_path


def test_new_check_and_run_stay_inside_the_sandbox(sandbox):
    assert cli.main(["new", "--manual", "Test Target", "--tic", "1", "--ra", "10", "--dec", "20",
                     "--t0", "2459000.5"]) == 0
    spec = sandbox / "campaigns" / "test-target.yaml"
    assert spec.is_file()
    assert not (REPO_ROOT / "campaigns" / "test-target.yaml").exists()

    assert cli.main(["check", str(spec)]) == 0

    # a zero-step spec still exercises the run path, ledger and record locations
    (sandbox / "campaigns" / "zero").mkdir()
    (sandbox / "campaigns" / "zero" / "REPORT.md").write_text("# zero\n", encoding="utf-8")
    zero = sandbox / "campaigns" / "zero.yaml"
    zero.write_text("""schema: cygnus.campaign/1
campaign_id: zero
objective: smoke
outputs: campaigns/zero/
targets: [{name: Zero, ra_deg: 10.0, dec_deg: 20.0, frame: ICRS, epoch: J2000.0, position_source: test}]
steps: []
record:
  path: campaigns/zero/sky_record.json
  title: Zero
  kind: smoke
  outcome: bounded_null
  date: "2026-01-02"
  report: campaigns/zero/REPORT.md
  summary: Smoke.
  checks: [{name: "Pixel-level audit", state: not_tested}]
""", encoding="utf-8")
    assert cli.main(["run", str(zero)]) == 0
    assert (sandbox / "campaigns" / "zero" / "sky_record.json").is_file()
    ledger = sandbox / "state" / "ledger.sqlite"
    assert ledger.is_file()
    # nothing leaked into the production tree
    assert not (REPO_ROOT / "campaigns" / "zero").exists()


def test_missing_spec_is_a_clean_error(sandbox, capsys):
    rc = cli.main(["check", str(sandbox / "nope.yaml")])
    assert rc == 2
    assert "spec not found" in capsys.readouterr().err


def test_queue_board_is_confined_and_handles_a_missing_queue(sandbox, capsys):
    # a queue CSV inside the sandbox
    q = sandbox / "campaigns" / "q.csv"
    q.write_text("rank,name,tic,ra_deg,dec_deg,t0_bjd\n1,TOI-1.01,1,10,20,2459000.5\n", encoding="utf-8")
    assert cli.main(["queue", "--queue", str(q)]) == 0
    assert "TOI-1.01" in capsys.readouterr().out
    # a missing queue is a clean error, not a traceback
    assert cli.main(["queue", "--queue", str(sandbox / "missing.csv")]) == 1
    assert "queue:" in capsys.readouterr().err


def test_ledger_namespace_is_cygnus_multi(sandbox):
    from cygnus.ledger import Ledger
    (sandbox / "campaigns" / "ns").mkdir()
    (sandbox / "campaigns" / "ns" / "REPORT.md").write_text("# ns\n", encoding="utf-8")
    spec = sandbox / "campaigns" / "ns.yaml"
    spec.write_text("""schema: cygnus.campaign/1
campaign_id: ns
objective: namespace
outputs: campaigns/ns/
targets:
  - {name: T, ra_deg: 10.0, dec_deg: 20.0, frame: ICRS, epoch: J2000.0, position_source: fixture}
steps:
  - fetch_products: {from_targets: {archives: [not-a-real-archive]}}
record:
  path: campaigns/ns/sky_record.json
  title: NS
  kind: smoke
  outcome: bounded_null
  date: "2026-01-02"
  report: campaigns/ns/REPORT.md
  summary: Smoke.
  checks: [{name: "Pixel-level audit", state: not_tested}]
""", encoding="utf-8")
    assert cli.main(["run", str(spec)]) == 1          # no products: clean, offline failure
    led = Ledger(sandbox / "state" / "ledger.sqlite")
    try:
        runs = led.runs()
        assert runs and all(r["script"].startswith("cygnus_multi:") for r in runs)
        assert all(not r["script"].startswith("cygnus.campaign:") for r in runs)
        assert runs[-1]["status"] == "failed" and "no products" in (runs[-1]["summary"] or "")
    finally:
        led.close()
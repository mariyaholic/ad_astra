"""cygnus.batch: lock, orphan-run repair, retries, resume and triage (no network, no real runs)."""

from __future__ import annotations

import json
import os
import socket
import subprocess
import types
from pathlib import Path

import pytest

from cygnus import batch
from cygnus.ledger import Ledger


def _record(root: Path, cid: str, *, outcome="null_result", known="passed", xmatch="passed", xnote="4 answered, 0 errored"):
    d = root / "campaigns" / cid
    d.mkdir(parents=True, exist_ok=True)
    rec = {"status": "completed", "outcome": outcome, "evidence": "Unverified lead" if outcome == "lead" else None,
           "checks": [{"name": batch.CHECK_KNOWN, "state": known},
                      {"name": batch.CHECK_XMATCH, "state": xmatch, "note": f"1 target(s) × 4 services; {xnote}"}]}
    (d / "sky_record.json").write_text(json.dumps(rec), encoding="utf-8")


def _args(**kw):
    base = {"batch": "b1", "spec": None, "jobs": 1, "retries": 2, "timeout": 60, "redo": False, "no_report": True, "ledger": None}
    return types.SimpleNamespace(**{**base, **kw})


def test_lock_refuses_a_live_holder_and_takes_over_a_stale_one(tmp_path):
    led = tmp_path / "ledger.sqlite"
    a = batch.LedgerLock(led)
    assert a.acquire() is None
    with pytest.raises(SystemExit, match="locked by another batch"):
        batch.LedgerLock(led).acquire()
    a.release()
    assert not a.path.exists()
    # a lock left by a process that no longer exists on this host is taken over, with a note
    a.path.write_text(json.dumps({"pid": 999999, "host": socket.gethostname(), "started_utc": "2026-01-01T00:00:00Z"}))
    b = batch.LedgerLock(led)
    note = b.acquire()
    assert note and "stale lock from pid 999999" in note
    assert json.loads(b.path.read_text())["pid"] == os.getpid()
    b.release()


def test_orphan_runs_are_closed_only_for_the_named_campaign(tmp_path):
    led_p = tmp_path / "ledger.sqlite"
    led = Ledger(led_p)
    mine = led.log_run("cygnus_multi:toi-1-01:fetch_products")
    other = led.log_run("cygnus_multi:toi-2-01:fetch_products")
    prefix = led.log_run("cygnus_multi:toi-1-011:fetch_products")   # LIKE 'toi-1-01:%' must not match this
    led.close()
    assert batch.close_orphan_runs(led_p, "toi-1-01", "test") == [mine]
    led = Ledger(led_p)
    assert led.run(mine)["status"] == "aborted" and "test" in led.run(mine)["summary"]
    assert led.run(other)["status"] == "open" and led.run(prefix)["status"] == "open"
    led.close()


def test_triage_flags_leads_failed_controls_and_dead_catalogues(tmp_path):
    _record(tmp_path, "a")
    _record(tmp_path, "b", outcome="lead")
    _record(tmp_path, "c", known="failed")
    _record(tmp_path, "d", xmatch="inconclusive", xnote="0 answered, 4 errored")
    _record(tmp_path, "e", xmatch="inconclusive", xnote="10 answered, 2 errored")
    assert batch.triage(tmp_path, "campaigns/a.yaml")["escalate"] == []
    assert "repeat candidate" in batch.triage(tmp_path, "campaigns/b.yaml")["escalate"][0]
    assert "positive control failed" in batch.triage(tmp_path, "campaigns/c.yaml")["escalate"][0]
    assert "every catalogue service errored" in batch.triage(tmp_path, "campaigns/d.yaml")["escalate"][0]
    assert batch.triage(tmp_path, "campaigns/e.yaml")["escalate"] == []
    assert batch.triage(tmp_path, "campaigns/zz.yaml")["escalate"] == ["no sky record"]


def _fake_runner(tmp_path, script):
    """subprocess.run stand-in: for each `cygnus.multi run <spec>` call pop the next behaviour."""
    calls = []

    def fake(cmd, cwd=None, env=None, stdout=None, stderr=None, timeout=None, **kw):
        spec = cmd[-1]
        cid = Path(spec).stem
        calls.append((cid, env.get("CYGNUS_LEDGER") if env else None))
        what = script[cid].pop(0)
        if what == "hang":
            raise subprocess.TimeoutExpired(cmd, timeout)
        if what == "crash-open":   # a crash that leaves a ledger run open
            led = Ledger(env["CYGNUS_LEDGER"]); led.log_run(f"cygnus_multi:{cid}:fetch_products"); led.close()
            stdout.write("HTTPError: 502 Bad Gateway\n")
            return types.SimpleNamespace(returncode=1)
        if what == "bug":
            stdout.write("KeyError: 'x'\n")
            return types.SimpleNamespace(returncode=1)
        _record(tmp_path, cid)
        return types.SimpleNamespace(returncode=0)

    return fake, calls


def test_run_retries_transient_failures_repairs_orphans_resumes_and_summarises(tmp_path, monkeypatch):
    led_p = tmp_path / "state" / "ledger.sqlite"
    led_p.parent.mkdir(parents=True)
    bdir = batch.batch_dir(tmp_path, "b1")
    bdir.mkdir(parents=True)
    (bdir / "specs.txt").write_text("campaigns/ok-1.yaml\ncampaigns/flaky.yaml\ncampaigns/broken.yaml\n")
    fake, calls = _fake_runner(tmp_path, {"ok-1": ["ok"], "flaky": ["crash-open", "hang", "ok"], "broken": ["bug"]})
    monkeypatch.setattr(batch.subprocess, "run", fake)
    monkeypatch.setattr(batch.time, "sleep", lambda s: None)
    rc = batch.cmd_run(_args(ledger=str(led_p)), tmp_path)
    assert rc == 1                                           # one campaign failed for good
    assert [c for c, _ in calls] == ["ok-1", "flaky", "flaky", "flaky", "broken"]   # a non-transient bug is not retried
    assert all(l == str(led_p) for _, l in calls)
    led = Ledger(led_p)
    assert [r["status"] for r in led.runs()] == ["aborted"]   # the crash's open run was closed before the retry
    led.close()
    summary = (bdir / "SUMMARY.md").read_text(encoding="utf-8")
    assert "finished: 2; failed: 1" in summary and "`campaigns/broken.yaml` | 1 | KeyError" in summary
    assert not batch.LedgerLock(led_p).path.exists()           # lock released
    # resume: finished campaigns are skipped, the failed one is retried
    fake2, calls2 = _fake_runner(tmp_path, {"broken": ["ok"]})
    monkeypatch.setattr(batch.subprocess, "run", fake2)
    assert batch.cmd_run(_args(ledger=str(led_p)), tmp_path) == 0
    assert [c for c, _ in calls2] == ["broken"]
    assert "finished: 3; failed: 0" in (bdir / "SUMMARY.md").read_text(encoding="utf-8")


def test_claim_skips_claimed_rows_and_unrunnable_ones(tmp_path, monkeypatch):
    (tmp_path / "campaigns" / "q").mkdir(parents=True)
    (tmp_path / "campaigns" / "q" / "target_queue.csv").write_text(
        "rank,name,tic\n1,TOI-1.01,1\n2,TOI-2.01,2\n3,TOI-3.01,3\n4,TOI-4.01,4\n", encoding="utf-8")
    (tmp_path / "campaigns" / "toi-1-01.yaml").write_text("claimed", encoding="utf-8")

    def fake(cmd, cwd=None, capture_output=None, text=None, **kw):
        name = cmd[cmd.index("--from-queue") + 1]
        assert cmd[cmd.index("--queue") + 1] == "campaigns/q/target_queue.csv"   # repository-relative
        if name == "TOI-2.01":
            return types.SimpleNamespace(returncode=1, stdout="", stderr="TOI-2.01: no t0_bjd")
        slug = name.lower().replace(".", "-")
        (tmp_path / "campaigns" / f"{slug}.yaml").write_text("spec", encoding="utf-8")
        return types.SimpleNamespace(returncode=0, stdout=f"campaigns/{slug}.yaml\n", stderr="")

    monkeypatch.setattr(batch.subprocess, "run", fake)
    a = types.SimpleNamespace(queue="campaigns/q/target_queue.csv", n=2, batch="b1", archives=None, seed=1)
    assert batch.cmd_claim(a, tmp_path) == 0
    assert batch.batch_specs(batch.batch_dir(tmp_path, "b1")) == ["campaigns/toi-3-01.yaml", "campaigns/toi-4-01.yaml"]
    skipped = [e for e in batch.read_journal(batch.batch_dir(tmp_path, "b1")) if e["event"] == "claim_skipped"]
    assert skipped[0]["target"] == "TOI-2.01" and "no t0_bjd" in skipped[0]["reason"]

"""cygnus.batch beyond tests/test_batch.py (docs/SUITE_EXPANSION.md §4.1 item 7).

queue/status/argparse dispatch, parallel jobs, --redo/--spec, the report step, the TRANSIENT keyword
matrix, lock edge cases, the cygnus.campaign arm of orphan repair, the claim commit hint and the
journal's start/end events. ``subprocess.run`` is always faked; nothing is executed or fetched.
"""

from __future__ import annotations

import json
import os
import socket
import subprocess
import threading
import types
from pathlib import Path

import pytest

from cygnus import batch
from cygnus.ledger import Ledger


def _record(root: Path, cid: str):
    d = root / "campaigns" / cid
    d.mkdir(parents=True, exist_ok=True)
    rec = {"status": "completed", "outcome": "bounded_null", "evidence": None,
           "checks": [{"name": batch.CHECK_KNOWN, "state": "passed"},
                      {"name": batch.CHECK_XMATCH, "state": "passed", "note": "1 target(s) × 4 services; 4 answered, 0 errored"}]}
    (d / "sky_record.json").write_text(json.dumps(rec), encoding="utf-8")


def _args(**kw):
    base = {"batch": "b1", "spec": None, "jobs": 1, "retries": 2, "timeout": 60, "redo": False, "no_report": True, "ledger": None}
    return types.SimpleNamespace(**{**base, **kw})


def _world(tmp_path, specs):
    led = tmp_path / "state" / "ledger.sqlite"
    led.parent.mkdir(parents=True, exist_ok=True)
    bdir = batch.batch_dir(tmp_path, "b1")
    bdir.mkdir(parents=True, exist_ok=True)
    (bdir / "specs.txt").write_text("".join(f"{s}\n" for s in specs), encoding="utf-8")
    return led, bdir


class FakeRun:
    """Thread-safe subprocess.run stand-in. ``script[cid]`` is a list of behaviours for successive
    ``cygnus.multi run`` calls: "ok", or any other string, written to the log as the failure text."""

    def __init__(self, root, script=None, *, barrier=None):
        self.root, self.script, self.barrier = root, script or {}, barrier
        self.calls: list[list[str]] = []
        self.lock = threading.Lock()
        self.threads: set[int] = set()

    def __call__(self, cmd, cwd=None, env=None, stdout=None, stderr=None, timeout=None, **kw):
        with self.lock:
            self.calls.append(list(cmd))
            self.threads.add(threading.get_ident())
        if "report" in cmd:
            return types.SimpleNamespace(returncode=0, stdout="", stderr="")
        cid = Path(cmd[-1]).stem
        if self.barrier is not None:
            self.barrier.wait(timeout=10)                    # both campaigns must be in flight at once
        with self.lock:
            what = self.script.get(cid, ["ok"]).pop(0) if self.script.get(cid) else "ok"
        if what != "ok":
            stdout.write(what + "\n")
            return types.SimpleNamespace(returncode=1)
        _record(self.root, cid)
        return types.SimpleNamespace(returncode=0)

    def runs_of(self, cid):
        return [c for c in self.calls if "run" in c and Path(c[-1]).stem == cid]


@pytest.fixture()
def no_sleep(monkeypatch):
    slept = []
    monkeypatch.setattr(batch.time, "sleep", slept.append)
    return slept


# ------------------------------------------------------------------ queue
def _qargs(**kw):
    base = {"id": "tess-q-09", "where": "pl_orbper IS NULL AND tfopwg_disp IN ('PC','APC')", "top": 25,
            "domain": "worlds.planetary.monotransit", "objective": "rank for the test.", "seed": 7}
    return types.SimpleNamespace(**{**base, **kw})


def test_queue_writes_a_valid_draft_spec_and_runs_it(tmp_path, monkeypatch, capsys):
    import yaml

    from cygnus.campaign.runner import load_spec

    (tmp_path / "campaigns").mkdir()
    calls = []
    monkeypatch.setattr(batch.subprocess, "run", lambda cmd, cwd=None, **kw: calls.append((cmd, cwd))
                        or types.SimpleNamespace(returncode=0))
    a = _qargs(where='disp = "PC" AND pl_orbper IS NULL')
    assert batch.cmd_queue(a, tmp_path) == 0
    spec_p = tmp_path / "campaigns" / "tess-q-09.yaml"
    [(cmd, cwd)] = calls
    assert cmd[-3:] == ["cygnus.campaign", "run", str(spec_p)] and cwd == tmp_path
    assert capsys.readouterr().out.strip() == "campaigns/tess-q-09/target_queue.csv"
    spec = yaml.safe_load(spec_p.read_text(encoding="utf-8"))
    assert spec["status"] == "draft" and spec["random_seed"] == 7 and spec["outputs"] == "campaigns/tess-q-09/"
    [step] = spec["steps"]
    assert step["target_queue"] == {"source": "nasa_exoplanet_archive.toi", "where": 'disp = "PC" AND pl_orbper IS NULL',
                                    "top": 25}                                            # quotes survive escaping
    rec = spec["record"]
    assert rec["status"] == "draft" and rec["kind"] == "target queue" and rec["queue_targets_in_record"] == 10
    assert rec["path"] == "campaigns/tess-q-09/sky_record.json" and "top 25" in rec["summary"]
    assert "outcome" not in rec
    assert load_spec(spec_p)["campaign_id"] == "tess-q-09"                                # the runner accepts it


def test_queue_refuses_an_existing_id_and_reports_a_failed_run(tmp_path, monkeypatch, capsys):
    (tmp_path / "campaigns").mkdir()
    (tmp_path / "campaigns" / "tess-q-09.yaml").write_text("taken", encoding="utf-8")
    monkeypatch.setattr(batch.subprocess, "run", lambda *a, **k: pytest.fail("must not run"))
    with pytest.raises(SystemExit, match="campaigns/tess-q-09.yaml exists; pick a new queue id"):
        batch.cmd_queue(_qargs(), tmp_path)
    assert (tmp_path / "campaigns" / "tess-q-09.yaml").read_text() == "taken"            # untouched
    monkeypatch.setattr(batch.subprocess, "run", lambda *a, **k: types.SimpleNamespace(returncode=3))
    assert batch.cmd_queue(_qargs(id="tess-q-10"), tmp_path) == 3
    assert "queue run failed (3)" in capsys.readouterr().out


# ------------------------------------------------------------------ status and dispatch
def test_status_rewrites_and_prints_the_summary(tmp_path, capsys):
    _, bdir = _world(tmp_path, ["campaigns/a.yaml", "campaigns/b.yaml"])
    _record(tmp_path, "a")
    batch.append_journal(bdir, {"event": "attempt", "spec": "campaigns/a.yaml", "result": "ok", "attempt": 1})
    assert batch.cmd_status(types.SimpleNamespace(batch="b1"), tmp_path) == 0
    out = capsys.readouterr().out
    assert out.startswith("# Batch b1") and "Specs: 2; finished: 1; failed: 0; not yet run: 1" in out
    assert "- `campaigns/b.yaml`" in out and (bdir / "SUMMARY.md").read_text(encoding="utf-8").strip() == out.strip()


def test_main_dispatches_parsed_arguments(tmp_path, monkeypatch):
    seen = {}
    for name in ("cmd_queue", "cmd_claim", "cmd_run", "cmd_status"):
        monkeypatch.setattr(batch, name, lambda a, root, name=name: seen.update({name: (a, root)}) or 5)
    monkeypatch.setattr(batch, "WORKTREE", tmp_path)
    assert batch.main(["run", "--batch", "b9", "--jobs", "2", "--redo", "--no-report", "--spec", "campaigns/x.yaml",
                       "campaigns/y.yaml", "--retries", "0", "--timeout", "30", "--ledger", "l.sqlite"]) == 5
    a, root = seen["cmd_run"]
    assert root == tmp_path
    assert (a.batch, a.jobs, a.redo, a.no_report, a.spec, a.retries, a.timeout, a.ledger) == \
           ("b9", 2, True, True, ["campaigns/x.yaml", "campaigns/y.yaml"], 0, 30, "l.sqlite")
    batch.main(["queue", "q-1", "--where", "x IS NULL"])
    a, _ = seen["cmd_queue"]
    assert (a.id, a.where, a.top, a.seed, a.domain) == ("q-1", "x IS NULL", 200, 20260927, "worlds.planetary.monotransit")
    batch.main(["claim", "--queue", "q.csv", "--batch", "b1", "--n", "3", "--archives", "gaia"])
    a, _ = seen["cmd_claim"]
    assert (a.queue, a.n, a.batch, a.archives) == ("q.csv", 3, "b1", "gaia")
    batch.main(["status", "--batch", "b1"])
    assert seen["cmd_status"][0].batch == "b1"
    batch.main(["run", "--batch", "b2"])
    a, _ = seen["cmd_run"]
    assert (a.jobs, a.retries, a.timeout, a.redo, a.no_report, a.spec, a.ledger) == (1, 2, 1800, False, False, None, None)
    with pytest.raises(SystemExit):
        batch.main([])                                                                # a subcommand is required
    with pytest.raises(SystemExit):
        batch.main(["run"])                                                           # --batch is required


# ------------------------------------------------------------------ run: jobs, redo, spec, report
def test_two_jobs_run_in_parallel_and_the_journal_is_consistent(tmp_path, monkeypatch, capsys):
    led, bdir = _world(tmp_path, ["campaigns/a.yaml", "campaigns/b.yaml"])
    fake = FakeRun(tmp_path, barrier=threading.Barrier(2))
    monkeypatch.setattr(batch.subprocess, "run", fake)
    assert batch.cmd_run(_args(jobs=2, ledger=str(led)), tmp_path) == 0
    assert len(fake.threads) == 2                                                     # two workers, both in flight
    assert sorted(Path(c[-1]).stem for c in fake.calls) == ["a", "b"]
    j = batch.read_journal(bdir)
    assert j[0]["event"] == "start" and j[0]["jobs"] == 2 and j[0]["todo"] == 2 and j[0]["pid"] == os.getpid()
    assert j[0]["lock_note"] is None
    assert j[-1] == {"event": "end", "utc": j[-1]["utc"], "ok": 2, "failed": 0}
    attempts = [e for e in j if e["event"] == "attempt"]
    assert sorted(e["spec"] for e in attempts) == ["campaigns/a.yaml", "campaigns/b.yaml"]
    assert all(e["result"] == "ok" and e["attempt"] == 1 and e["error"] is None and e["triage"]["escalate"] == []
               for e in attempts)
    assert {e["log"] for e in attempts} == {"state/batches/b1/logs/a.attempt1.log", "state/batches/b1/logs/b.attempt1.log"}
    assert "finished: 2; failed: 0" in (bdir / "SUMMARY.md").read_text(encoding="utf-8")
    assert "batch b1: 2 to run, 0 already finished" in capsys.readouterr().out
    assert not batch.LedgerLock(led).path.exists()


def test_finished_campaigns_are_skipped_unless_redo_or_their_record_is_gone(tmp_path, monkeypatch):
    led, bdir = _world(tmp_path, ["campaigns/a.yaml", "campaigns/b.yaml"])
    fake = FakeRun(tmp_path)
    monkeypatch.setattr(batch.subprocess, "run", fake)
    batch.cmd_run(_args(ledger=str(led)), tmp_path)
    fake.calls.clear()
    batch.cmd_run(_args(ledger=str(led)), tmp_path)
    assert fake.calls == []                                                           # nothing left to do
    (tmp_path / "campaigns" / "b" / "sky_record.json").unlink()
    batch.cmd_run(_args(ledger=str(led)), tmp_path)
    assert [Path(c[-1]).stem for c in fake.calls] == ["b"]                            # a lost record is re-run
    fake.calls.clear()
    batch.cmd_run(_args(ledger=str(led), redo=True), tmp_path)
    assert [Path(c[-1]).stem for c in fake.calls] == ["a", "b"]
    starts = [e for e in batch.read_journal(bdir) if e["event"] == "start"]
    assert [s["todo"] for s in starts] == [2, 0, 1, 2]


def test_spec_option_adds_specs_once_and_an_empty_batch_is_refused(tmp_path, monkeypatch):
    led = tmp_path / "ledger.sqlite"
    with pytest.raises(SystemExit, match="batch b1 has no specs"):
        batch.cmd_run(_args(ledger=str(led)), tmp_path)
    fake = FakeRun(tmp_path)
    monkeypatch.setattr(batch.subprocess, "run", fake)
    assert batch.cmd_run(_args(ledger=str(led), spec=["campaigns/x.yaml"]), tmp_path) == 0
    assert batch.cmd_run(_args(ledger=str(led), spec=["campaigns/x.yaml", "campaigns/y.yaml"]), tmp_path) == 0
    assert batch.batch_specs(batch.batch_dir(tmp_path, "b1")) == ["campaigns/x.yaml", "campaigns/y.yaml"]
    assert [Path(c[-1]).stem for c in fake.calls] == ["x", "y"]                       # x ran once, not twice


def test_report_step_runs_after_a_successful_campaign_only(tmp_path, monkeypatch):
    led, _ = _world(tmp_path, ["campaigns/a.yaml", "campaigns/b.yaml"])
    fake = FakeRun(tmp_path, {"b": ["KeyError: 'x'"]})
    monkeypatch.setattr(batch.subprocess, "run", fake)
    assert batch.cmd_run(_args(ledger=str(led), no_report=False), tmp_path) == 1
    reports = [c for c in fake.calls if "report" in c]
    assert [c[-3:] for c in reports] == [["cygnus.multi", "report", "campaigns/a.yaml"]]
    runs = [c for c in fake.calls if "report" not in c]
    assert [c[-3:] for c in runs] == [["cygnus.multi", "run", "campaigns/a.yaml"], ["cygnus.multi", "run", "campaigns/b.yaml"]]


# ------------------------------------------------------------------ TRANSIENT matrix
@pytest.mark.parametrize("keyword", batch.TRANSIENT)
def test_each_transient_keyword_is_retried(tmp_path, monkeypatch, no_sleep, keyword):
    led, bdir = _world(tmp_path, ["campaigns/a.yaml"])
    fake = FakeRun(tmp_path, {"a": [f"urllib.error: {keyword} from the archive", "ok"]})
    monkeypatch.setattr(batch.subprocess, "run", fake)
    assert batch.cmd_run(_args(ledger=str(led)), tmp_path) == 0
    assert len(fake.runs_of("a")) == 2 and no_sleep == [30]
    first = [e for e in batch.read_journal(bdir) if e["event"] == "attempt"][0]
    assert first["result"] == "failed" and keyword in first["error"]


def test_timeouts_are_retried_with_backoff_until_retries_run_out(tmp_path, monkeypatch, no_sleep):
    led, bdir = _world(tmp_path, ["campaigns/a.yaml"])

    def hang(cmd, timeout=None, **kw):
        raise subprocess.TimeoutExpired(cmd, timeout)

    monkeypatch.setattr(batch.subprocess, "run", hang)
    assert batch.cmd_run(_args(ledger=str(led), retries=2, timeout=5), tmp_path) == 1
    attempts = [e for e in batch.read_journal(bdir) if e["event"] == "attempt"]
    assert [e["attempt"] for e in attempts] == [1, 2, 3] and all(e["error"] == "timed out after 5 s" for e in attempts)
    assert no_sleep == [30, 120]                                                      # no sleep after the last attempt


@pytest.mark.parametrize("text", [
    "Traceback (most recent call last):\nKeyError: 'pl_tranmid'",
    "RuntimeError: sky record fails cygnus.skyrecord.validate",
    "ValueError: unknown veto kind 'x'",
])
def test_a_deterministic_traceback_is_not_retried(tmp_path, monkeypatch, no_sleep, text):
    led, bdir = _world(tmp_path, ["campaigns/a.yaml"])
    fake = FakeRun(tmp_path, {"a": [text, "ok"]})
    monkeypatch.setattr(batch.subprocess, "run", fake)
    assert batch.cmd_run(_args(ledger=str(led)), tmp_path) == 1
    assert len(fake.runs_of("a")) == 1 and no_sleep == []
    [e] = [e for e in batch.read_journal(bdir) if e["event"] == "attempt"]
    assert e["error"] == " / ".join(text.splitlines()[-3:])
    summary = (bdir / "SUMMARY.md").read_text(encoding="utf-8")
    assert "## Failed after retries" in summary and "`campaigns/a.yaml` | 1 |" in summary


def test_a_silent_nonzero_exit_reports_the_exit_code(tmp_path, monkeypatch, no_sleep):
    led, bdir = _world(tmp_path, ["campaigns/a.yaml"])
    monkeypatch.setattr(batch.subprocess, "run", lambda cmd, **kw: types.SimpleNamespace(returncode=9))
    assert batch.cmd_run(_args(ledger=str(led)), tmp_path) == 1
    [e] = [e for e in batch.read_journal(bdir) if e["event"] == "attempt"]
    assert e["error"] == "exit 9" and no_sleep == []


# ------------------------------------------------------------------ lock edge cases
def test_a_corrupt_lock_file_is_treated_as_held(tmp_path):
    lock = batch.LedgerLock(tmp_path / "ledger.sqlite")
    lock.path.write_text("{not json", encoding="utf-8")
    with pytest.raises(SystemExit, match="locked by another batch"):
        lock.acquire()
    assert lock.path.read_text(encoding="utf-8") == "{not json" and not lock.held      # never deleted
    lock.release()
    assert lock.path.exists()                                                         # release only removes a held lock


def test_a_lock_from_another_host_is_never_taken_over(tmp_path):
    lock = batch.LedgerLock(tmp_path / "ledger.sqlite")
    lock.path.write_text(json.dumps({"pid": 999999, "host": socket.gethostname() + "-elsewhere",
                                     "started_utc": "2026-01-01T00:00:00Z"}), encoding="utf-8")
    with pytest.raises(SystemExit, match="-elsewhere"):
        lock.acquire()
    assert json.loads(lock.path.read_text())["pid"] == 999999


def test_a_live_holder_on_this_host_blocks_and_a_pidless_lock_is_held(tmp_path, monkeypatch):
    lock = batch.LedgerLock(tmp_path / "ledger.sqlite")
    lock.path.write_text(json.dumps({"pid": os.getpid(), "host": socket.gethostname()}), encoding="utf-8")
    with pytest.raises(SystemExit):
        lock.acquire()
    lock.path.write_text(json.dumps({"host": socket.gethostname()}), encoding="utf-8")
    with pytest.raises(SystemExit):
        lock.acquire()
    # a stale same-host lock is taken over and a new payload written
    monkeypatch.setattr(batch.LedgerLock, "_alive", staticmethod(lambda pid: False))
    lock.path.write_text(json.dumps({"pid": 123, "host": socket.gethostname(), "started_utc": "t0"}), encoding="utf-8")
    assert lock.acquire() == "stale lock from pid 123 (started t0) taken over"
    payload = json.loads(lock.path.read_text())
    assert payload["pid"] == os.getpid() and payload["host"] == socket.gethostname() and payload["started_utc"]
    lock.release()


def test_a_held_lock_blocks_cmd_run_before_any_campaign_starts(tmp_path, monkeypatch):
    led, bdir = _world(tmp_path, ["campaigns/a.yaml"])
    batch.LedgerLock(led).path.write_text(json.dumps({"pid": os.getpid(), "host": socket.gethostname()}))
    monkeypatch.setattr(batch.LedgerLock, "_alive", staticmethod(lambda pid: True))   # (tasklist is a subprocess)
    monkeypatch.setattr(batch.subprocess, "run", lambda *a, **k: pytest.fail("must not run"))
    with pytest.raises(SystemExit, match="locked"):
        batch.cmd_run(_args(ledger=str(led)), tmp_path)
    assert batch.read_journal(bdir) == []


# ------------------------------------------------------------------ orphan repair: the cygnus.campaign arm
def test_orphan_repair_closes_campaign_runner_scripts_too(tmp_path):
    led_p = tmp_path / "ledger.sqlite"
    led = Ledger(led_p)
    multi = led.log_run("cygnus_multi:toi-1-01:fetch_products")
    camp = led.log_run("cygnus.campaign:toi-1-01:residual_screen")
    other = led.log_run("cygnus.campaign:toi-2-01:residual_screen")
    done = led.log_run("cygnus.campaign:toi-1-01:fetch_products")
    led.close_run(done, "completed")
    led.close()
    assert batch.close_orphan_runs(led_p, "toi-1-01", "repair") == [multi, camp]
    led = Ledger(led_p)
    try:
        assert led.run(camp)["status"] == "aborted" and "repair" in led.run(camp)["summary"]
        assert led.run(other)["status"] == "open" and led.run(done)["status"] == "completed"
    finally:
        led.close()


# ------------------------------------------------------------------ claim hint
def test_claim_prints_the_commit_hint_only_when_something_was_claimed(tmp_path, monkeypatch, capsys):
    (tmp_path / "campaigns" / "q").mkdir(parents=True)
    qcsv = tmp_path / "campaigns" / "q" / "target_queue.csv"
    qcsv.write_text("rank,name,tic\n1,TOI-1.01,1\n2,TOI-2.01,2\n", encoding="utf-8")

    def fake(cmd, cwd=None, capture_output=None, text=None, **kw):
        slug = cmd[cmd.index("--from-queue") + 1].lower().replace(".", "-")
        assert cmd[cmd.index("--archives") + 1] == "gaia,simbad" and cmd[cmd.index("--seed") + 1] == "4"
        (tmp_path / "campaigns" / f"{slug}.yaml").write_text("spec", encoding="utf-8")
        return types.SimpleNamespace(returncode=0, stdout=f"campaigns/{slug}.yaml\n", stderr="")

    monkeypatch.setattr(batch.subprocess, "run", fake)
    a = types.SimpleNamespace(queue="campaigns/q/target_queue.csv", n=5, batch="b7", archives="gaia,simbad", seed=4)
    assert batch.cmd_claim(a, tmp_path) == 0
    out = capsys.readouterr().out
    assert ('git add campaigns/toi-1-01.yaml campaigns/toi-2-01.yaml && '
            'git commit -m "Claim 2 targets (batch b7)" && git push') in out
    assert batch.cmd_claim(a, tmp_path) == 0                                          # everything already claimed
    out = capsys.readouterr().out
    assert json.loads(out)["claimed"] == [] and "git commit" not in out
    outside = types.SimpleNamespace(queue=str(tmp_path.parent / "elsewhere.csv"), n=1, batch="b7", archives=None, seed=1)
    with pytest.raises(SystemExit, match="outside the worktree"):
        batch.cmd_claim(outside, tmp_path)


def test_triage_escalates_a_catalogued_eclipsing_binary(tmp_path):
    d = tmp_path / "campaigns" / "eb"
    d.mkdir(parents=True)
    (d / "sky_record.json").write_text(json.dumps({"status": "completed", "outcome": "null_result", "checks": [
        {"name": "Variable-catalogue collision (VSX)", "state": "failed", "note": "TOI-1: V9 EA P=2.5 at 0.4\""},
        {"name": "Object-class guard (SIMBAD)", "state": "passed", "note": "PM*"}]}), encoding="utf-8")
    why = batch.triage(tmp_path, "campaigns/eb.yaml")["escalate"]
    assert len(why) == 1 and why[0].startswith("Variable-catalogue collision (VSX) failed") and "EA" in why[0]

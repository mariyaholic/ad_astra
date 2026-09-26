"""cygnus.multi.runner: spec validation, reuse/force/until, code-fingerprint invalidation, flag_lead,
targets, draft/plots records and product directories (docs/SUITE_EXPANSION.md §4.1 item 6).

Runner mechanics use tiny registered fake steps (monkeypatched into ``STEPS``) so they cost
milliseconds; one test runs real fetch_products + residual_screen on a synthetic SPOC light curve to
assert the integrity check and the ledgered measurements.
"""

from __future__ import annotations

import json
import re
import types
from pathlib import Path

import pytest

pytest.importorskip("yaml")
pytest.importorskip("scipy")
pytest.importorskip("astropy.io.fits")

from cygnus.ledger import Ledger  # noqa: E402

from _multi_fixtures import SPOC_PID, make_ctx, measurements, sha256, write_spoc  # noqa: E402

TARGET = "targets: [{name: X, ra_deg: 1.0, dec_deg: 2.0, frame: ICRS, epoch: J2000.0, position_source: fixture}]\n"


# ------------------------------------------------------------------ load_spec validation matrix
def _load(tmp_path, body):
    from cygnus.multi.runner import load_spec

    p = tmp_path / "s.yaml"
    p.write_text(body, encoding="utf-8")
    return load_spec(p)


HEAD = "schema: cygnus.campaign/1\ncampaign_id: ok-id\noutputs: campaigns/ok-id/\n"


@pytest.mark.parametrize("body, message", [
    ("schema: cygnus.campaign/2\ncampaign_id: ok-id\noutputs: o/\nsteps: []\n", "schema must be 'cygnus.campaign/1'"),
    ("- just\n- a list\n", "schema must be"),
    ("schema: cygnus.campaign/1\ncampaign_id: Bad_Id\noutputs: o/\nsteps: []\n", "campaign_id must be a slug"),
    ("schema: cygnus.campaign/1\ncampaign_id: x\noutputs: o/\nsteps: []\n", "campaign_id must be a slug"),   # too short
    ("schema: cygnus.campaign/1\noutputs: o/\nsteps: []\n", "campaign_id must be a slug"),
    (HEAD + "steps:\n  - {fetch_products: {}, residual_screen: {}}\n", "each step is a one-key mapping"),
    (HEAD + "steps:\n  - fetch_products\n", "each step is a one-key mapping"),
    (HEAD + "steps:\n  - singletransit: {}\n", "step 'singletransit' is not implemented"),
    (HEAD + "runner: cygnus.campaign\nsteps: []\n", "runner is 'cygnus.campaign'; this runner is cygnus.multi"),
    (HEAD + "steps:\n  - residual_screen: {k_mad: 5}\n", "residual_screen needs a fetch_products step before it"),
    (HEAD + "steps:\n  - bls_recovery: {}\n", "bls_recovery needs a fetch_products step before it"),
    (HEAD + "steps:\n  - context_products: {}\n  - fetch_products: {}\n", "context_products must come after fetch_products"),
    (HEAD + "steps:\n  - known_signal_recovery: {}\n  - fetch_products: {}\n  - calibrate_screen: {}\n",
     "known_signal_recovery must come after fetch_products"),
    (HEAD + "steps:\n  - period_aliases: {}\n  - fetch_products: {}\n", "period_aliases must come after fetch_products"),
    (HEAD + "steps:\n  - fetch_products: {}\n  - alias_cross_instrument: {}\n  - fetch_independent: {}\n",
     "alias_cross_instrument must come after fetch_independent"),
    (HEAD + "steps:\n  - fetch_products: {}\n  - residual_screen: {k_mad: calibrated}\n",
     "residual_screen k_mad: calibrated needs a calibrate_screen step"),
    ("schema: cygnus.campaign/1\ncampaign_id: ok-id\nsteps: []\n", "outputs directory required"),
    (HEAD + "veto: {kind: ephemeris, period_days: 1}\nsteps: []\n", "veto.t0_bjd required for an ephemeris veto"),
    (HEAD + "veto: {kind: ephemeris, period_days: 1, t0_bjd: 2, veto_phase: 0.1}\nsteps: []\n",
     "veto.source required for an ephemeris veto"),
])
def test_load_spec_rejects(tmp_path, body, message):
    from cygnus.multi.runner import SpecError

    with pytest.raises(SpecError, match=re.escape(message)):
        _load(tmp_path, body)


def test_load_spec_reports_every_problem_at_once(tmp_path):
    from cygnus.multi.runner import SpecError

    with pytest.raises(SpecError) as e:
        _load(tmp_path, "schema: cygnus.campaign/1\ncampaign_id: B\nveto: {kind: ephemeris}\nsteps:\n  - nope: {}\n")
    msg = str(e.value)
    for part in ("campaign_id must be a slug", "'nope' is not implemented", "outputs directory required",
                 "veto.period_days", "veto.t0_bjd", "veto.veto_phase", "veto.source"):
        assert part in msg


def test_load_spec_accepts_valid_specs(tmp_path):
    spec = _load(tmp_path, HEAD + "runner: cygnus.multi\nveto: {kind: single_epoch, veto_hours: 6}\nsteps:\n"
                 "  - fetch_products: {}\n  - calibrate_screen: {}\n  - residual_screen: {k_mad: calibrated}\n"
                 "  - known_signal_recovery: {k_mad: 5}\n  - period_aliases: {}\n  - prior_art: {}\n")
    assert spec["_path"] == tmp_path / "s.yaml" and spec["campaign_id"] == "ok-id"
    # no steps at all, and a complete ephemeris veto, are also fine
    assert _load(tmp_path, HEAD + "veto: {kind: ephemeris, period_days: 1, t0_bjd: 2, veto_phase: 0.1, source: s}\n")


def test_alias_cross_instrument_may_run_without_fetch_independent(tmp_path):
    """An older spec that fetches other collections through fetch_products stays valid."""
    spec = _load(tmp_path, HEAD + "steps:\n  - fetch_products: {}\n  - period_aliases: {}\n  - alias_cross_instrument: {}\n")
    assert spec["campaign_id"] == "ok-id"


# The campaign twin (cygnus.campaign.runner.load_spec) refuses these at load time; the multi copy
# accepts them and the run then fails mid-way at the step that needs the missing output.
def test_calibrate_screen_after_a_calibrated_screen_is_refused(tmp_path):
    from cygnus.multi.runner import SpecError

    with pytest.raises(SpecError, match="calibrate_screen"):
        _load(tmp_path, HEAD + "steps:\n  - fetch_products: {}\n  - residual_screen: {k_mad: calibrated}\n"
                               "  - calibrate_screen: {}\n")


def test_known_signal_recovery_default_calibrated_k_needs_calibrate_screen(tmp_path):
    from cygnus.multi.runner import SpecError

    with pytest.raises(SpecError, match="calibrate_screen"):
        _load(tmp_path, HEAD + "steps:\n  - fetch_products: {}\n  - known_signal_recovery: {}\n")


def test_target_queue_after_fetch_products_is_refused(tmp_path):
    from cygnus.multi.runner import SpecError

    with pytest.raises(SpecError, match="target_queue must come before fetch_products"):
        _load(tmp_path, HEAD + "steps:\n  - fetch_products: {from_queue: {top: 1}}\n  - target_queue: {}\n")


# ------------------------------------------------------------------ runner mechanics with fake steps
@pytest.fixture()
def fake_steps(monkeypatch, tmp_path):
    from cygnus.multi import steps

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    calls: list[tuple[str, dict]] = []

    def probe(ctx, params):
        calls.append(("probe", params))
        ctx.measure("probe_value", params.get("v", 1), unit="count", method="fake")
        ctx.check("Probe check", "passed", f"probe v={params.get('v', 1)}")
        ctx.note("probe ran.")
        return {"v": params.get("v", 1)}

    def downstream(ctx, params):
        calls.append(("downstream", params))
        return {"seen": ctx.result("probe")["v"]}

    def flagger(ctx, params):
        calls.append(("flagger", params))
        ctx.flag_lead("fake repeat.")
        return {}

    for name, fn in (("probe", probe), ("downstream", downstream), ("flagger", flagger)):
        monkeypatch.setitem(steps.STEPS, name, fn)
    return calls


def _spec(root: Path, steps_yaml: str, *, record_extra: str = "", cid: str = "fake-run", targets: str = TARGET) -> Path:
    p = root / "campaigns" / f"{cid}.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"schema: cygnus.campaign/1\ncampaign_id: {cid}\noutputs: campaigns/{cid}/\nrandom_seed: 1\n"
                 + targets + "steps:\n" + steps_yaml
                 + f"record:\n  path: campaigns/{cid}/sky_record.json\n  title: Fake\n  kind: smoke\n"
                   f"  date: '2026-01-02'\n  report: campaigns/{cid}/REPORT.md\n  summary: Fake.\n"
                   "  checks: [{name: Declared, state: not_tested}]\n" + record_extra, encoding="utf-8")
    return p


def _run(spec, root, led, **kw):
    from cygnus.multi.runner import run

    msgs = []
    out = run(spec, ledger=led, root=root, echo=msgs.append, **kw)
    return out, msgs


def _record(root, cid="fake-run"):
    return json.loads((root / f"campaigns/{cid}/sky_record.json").read_text(encoding="utf-8"))


TWO = "  - probe: {v: 2}\n  - downstream: {}\n"


def test_steps_are_ledgered_reused_and_forced(tmp_path, fake_steps):
    spec = _spec(tmp_path, TWO, record_extra="  outcome: bounded_null\n")
    led = Ledger(":memory:")
    out, msgs = _run(spec, tmp_path, led)
    assert out["complete"] and out["steps_run"] == ["probe", "downstream"]
    assert [r["script"] for r in led.runs()] == ["cygnus_multi:fake-run:probe", "cygnus_multi:fake-run:downstream"]
    assert all(r["status"] == "completed" and r["seed"] == 1 for r in led.runs())
    [m] = measurements(led)
    assert m["name"] == "probe_value" and m["value"] == "2" and m["run_id"] == led.runs()[0]["id"]
    assert led.runs()[0]["summary"] == "probe ran." and led.runs()[1]["summary"] == "downstream completed"
    saved = json.loads((tmp_path / "campaigns/fake-run/runner/probe.json").read_text())
    assert saved["result"] == {"v": 2} and saved["checks"]["Probe check"]["state"] == "passed"
    assert (tmp_path / "campaigns/fake-run/runner/RUN_SUMMARY.json").is_file()
    rec = _record(tmp_path)
    assert rec["status"] == "completed" and rec["outcome"] == "bounded_null"
    checks = {c["name"]: c for c in rec["checks"]}
    assert checks["Declared"]["state"] == "not_tested"                                 # declared, never produced
    assert checks["Probe check"] == {"name": "Probe check", "state": "passed", "note": "probe v=2",
                                     "source": "campaign runner, step probe"}         # produced, not declared
    assert rec["summary"] == "Fake. Runner: probe ran."
    # second run: both steps reused; the saved checks and notes are restored into the record
    n_calls = len(fake_steps)
    out2, msgs2 = _run(spec, tmp_path, led)
    assert len(fake_steps) == n_calls and all("reused completed run" in m for m in msgs2)
    assert len(led.runs()) == 2 and out2["checks"]["Probe check"]["state"] == "passed" and out2["notes"] == ["probe ran."]
    # force: everything recomputed and ledgered again
    _run(spec, tmp_path, led, force=True)
    assert len(fake_steps) == n_calls + 2 and len(led.runs()) == 4


def test_a_changed_parameter_reruns_that_step_and_everything_downstream(tmp_path, fake_steps):
    spec = _spec(tmp_path, TWO, record_extra="  outcome: bounded_null\n")
    led = Ledger(":memory:")
    _run(spec, tmp_path, led)
    spec.write_text(spec.read_text().replace("v: 2", "v: 3"), encoding="utf-8")
    fake_steps.clear()
    out, msgs = _run(spec, tmp_path, led)
    assert [c[0] for c in fake_steps] == ["probe", "downstream"]            # upstream hash propagates
    assert out["checks"]["Probe check"]["note"] == "probe v=3"


def test_code_fingerprint_change_invalidates_reuse(tmp_path, fake_steps, monkeypatch):
    from cygnus.multi import runner

    fp = runner.code_fingerprint()
    assert re.fullmatch(r"[0-9a-f]{12}", fp) and fp == runner.code_fingerprint()        # stable
    spec = _spec(tmp_path, TWO, record_extra="  outcome: bounded_null\n")
    led = Ledger(":memory:")
    _run(spec, tmp_path, led)
    fake_steps.clear()
    monkeypatch.setattr(runner, "code_fingerprint", lambda: "0123456789ab")
    _, msgs = _run(spec, tmp_path, led)
    assert [c[0] for c in fake_steps] == ["probe", "downstream"] and not any("reused" in m for m in msgs)
    assert len(led.runs()) == 4 and len({r["config_hash"] for r in led.runs()}) == 4


def test_until_stops_early_and_writes_a_draft_record(tmp_path, fake_steps):
    spec = _spec(tmp_path, TWO, record_extra="  outcome: bounded_null\n  evidence: null\n")
    led = Ledger(":memory:")
    out, _ = _run(spec, tmp_path, led, until="probe")
    assert out["steps_run"] == ["probe"] and not out["complete"]
    assert [c[0] for c in fake_steps] == ["probe"]
    rec = _record(tmp_path)
    assert rec["status"] == "draft" and rec["outcome"] == "not_run" and rec["evidence"] is None and rec["date"] is None
    assert rec["generated_by"] == "cygnus_multi campaign runner"
    # finishing the run later reuses the first step and completes the record
    fake_steps.clear()
    out, _ = _run(spec, tmp_path, led)
    assert out["complete"] and [c[0] for c in fake_steps] == ["downstream"]
    assert _record(tmp_path)["status"] == "completed"


def test_a_failing_step_is_ledgered_failed_and_writes_no_record(tmp_path, fake_steps, monkeypatch):
    from cygnus.multi import steps

    def broken(ctx, params):
        raise ValueError("synthetic failure")

    monkeypatch.setitem(steps.STEPS, "broken", broken)
    spec = _spec(tmp_path, "  - probe: {}\n  - broken: {}\n", record_extra="  outcome: bounded_null\n")
    led = Ledger(":memory:")
    with pytest.raises(ValueError, match="synthetic failure"):
        _run(spec, tmp_path, led)
    assert [r["status"] for r in led.runs()] == ["completed", "failed"]
    assert "synthetic failure" in led.runs()[1]["summary"]
    assert not (tmp_path / "campaigns/fake-run/sky_record.json").exists()


# ------------------------------------------------------------------ flag_lead
def test_flag_lead_is_never_above_unverified_lead(tmp_path, monkeypatch):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    ctx = make_ctx(tmp_path)
    assert ctx.outcome is None
    ctx.flag_lead("first.")
    ctx.flag_lead("second.")
    assert ctx.outcome == ("lead", "Unverified lead") and ctx.notes == ["first.", "second."]


@pytest.mark.parametrize("record_extra, outcome, evidence", [
    ("  outcome: bounded_null\n", "lead", "Unverified lead"),                          # raised to lead
    ("", "lead", "Unverified lead"),                                                    # no spec outcome
    ("  outcome: candidate\n  evidence: Vetted candidate\n", "candidate", "Vetted candidate"),   # a person's call stands
    ("  outcome: lead\n  evidence: Unverified lead\n", "lead", "Unverified lead"),
])
def test_flag_lead_in_the_record(tmp_path, fake_steps, record_extra, outcome, evidence):
    spec = _spec(tmp_path, "  - flagger: {}\n", record_extra=record_extra)
    led = Ledger(":memory:")
    _run(spec, tmp_path, led)
    rec = _record(tmp_path)
    assert (rec["outcome"], rec["evidence"]) == (outcome, evidence)
    assert "fake repeat." in rec["summary"]
    # a reused flagging step restores its outcome
    _, msgs = _run(spec, tmp_path, led)
    assert all("reused" in m for m in msgs)
    assert (_record(tmp_path)["outcome"], _record(tmp_path)["evidence"]) == (outcome, evidence)


# ------------------------------------------------------------------ targets and records
def test_targets_resolve_names_and_append_queued_targets(tmp_path, monkeypatch):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    pack = tmp_path / "docs" / "tier1_pack"
    pack.mkdir(parents=True)
    (pack / "NAME_RESOLUTIONS.json").write_text(json.dumps({
        "Resolved": {"ok": True, "ra_deg": 10.0, "dec_deg": 20.0},
        "Failed": {"ok": False, "ra_deg": 1.0, "dec_deg": 1.0}}), encoding="utf-8")
    queue = [{"name": f"TOI-{i}.01", "ra_deg": float(i), "dec_deg": -float(i), "tic": i} for i in range(1, 4)]
    ctx = make_ctx(tmp_path, spec={"targets": [{"name": "Resolved"}, {"name": "Explicit", "ra_deg": 5.0, "dec_deg": 6.0}],
                                   "record": {"queue_targets_in_record": 2}},
                   results={"target_queue": {"queue": queue}})
    assert ctx.targets() == [{"name": "Resolved", "ra_deg": 10.0, "dec_deg": 20.0},
                             {"name": "Explicit", "ra_deg": 5.0, "dec_deg": 6.0},
                             {"name": "TOI-1.01", "ra_deg": 1.0, "dec_deg": -1.0},
                             {"name": "TOI-2.01", "ra_deg": 2.0, "dec_deg": -2.0}]
    for bad in ("Failed", "Unknown"):                                   # ok: false is not a resolution
        with pytest.raises(RuntimeError, match=f"target '{bad}' has no position"):
            make_ctx(tmp_path, spec={"targets": [{"name": bad}]}).targets()


def test_record_carries_plots_and_name_resolved_targets(tmp_path, fake_steps):
    pack = tmp_path / "docs" / "tier1_pack"
    pack.mkdir(parents=True)
    (pack / "NAME_RESOLUTIONS.json").write_text(json.dumps({"Resolved": {"ok": True, "ra_deg": 10.0, "dec_deg": 20.0}}))
    (tmp_path / "campaigns/fake-run").mkdir(parents=True)
    (tmp_path / "campaigns/fake-run/series.csv").write_text("t,f\n1,1\n", encoding="utf-8")
    plots = ("  plots:\n    - {type: timeseries, file: campaigns/fake-run/series.csv, time_col: t, flux_col: f, "
             "label: Series}\n")
    spec = _spec(tmp_path, "  - probe: {}\n", record_extra="  outcome: bounded_null\n  append_runner_notes: false\n" + plots,
                 targets="targets: [{name: Resolved}]\n")
    _run(spec, tmp_path, Ledger(":memory:"))
    rec = _record(tmp_path)
    assert rec["plots"] == [{"type": "timeseries", "file": "campaigns/fake-run/series.csv", "time_col": "t",
                             "flux_col": "f", "label": "Series"}]
    assert rec["targets"] == [{"name": "Resolved", "position_source": "NAME_RESOLUTIONS"}]
    assert rec["summary"] == "Fake."                                                   # runner notes suppressed
    assert rec["spec"] == "campaigns/fake-run.yaml"


def test_product_dir_labels_by_tic_sector_and_archive(tmp_path, monkeypatch):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    prods = {"a": {"tic": 42, "target": "T", "sector": 7}, "b": {"tic": 42, "target": None, "sector": 3},
             "c": {"archive": "fake", "sector": None}, "d": {"sector": None}, "e": {"sector": None}}
    ctx = make_ctx(tmp_path, results={"fetch_products": {"products": prods}})
    out = tmp_path / "out"
    assert ctx.product_dir("a") == out / "tic42" / "sector07"
    assert ctx.product_dir("b") == out / "sector03"                    # a TIC without a target: no TIC folder
    assert ctx.product_dir("c") == out / "fake00"
    assert ctx.product_dir("d") == out / "other00"
    assert ctx.product_dir("e", types.SimpleNamespace(primary={"SECTOR": 12})) == out / "sector12"
    assert (out / "tic42" / "sector07").is_dir()


# ------------------------------------------------------------------ a real run: integrity check and measurements
def test_real_run_asserts_integrity_check_and_ledgered_measurements(tmp_path, monkeypatch):
    from cygnus.multi.runner import run

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    lc = write_spoc(tmp_path / "scratch" / "stage" / SPOC_PID, n=2000, dips=(1501.5,))
    spec = _spec(tmp_path, '  - fetch_products: {search_dirs: ["scratch:stage"]}\n'
                           "  - residual_screen: {windows_days: [1.0], k_mad: 5.0, rednoise_trials: 20}\n",
                 record_extra="  outcome: bounded_null\n  checks: [{name: \"Product integrity (SHA-256)\", state: not_tested}]\n",
                 cid="real-run")
    text = spec.read_text().replace("  checks: [{name: Declared, state: not_tested}]\n", "")
    spec.write_text(text.replace("steps:\n", f"input:\n  products: [{{product_id: {SPOC_PID}, sector: 7, "
                                              f"expected_sha256: {sha256(lc)}}}]\nsteps:\n"), encoding="utf-8")
    led = Ledger(tmp_path / "ledger.sqlite")
    try:
        out = run(spec, ledger=led, root=tmp_path, echo=lambda *_: None)
        assert out["complete"]
        rows = measurements(led)
        by = {m["name"]: m for m in rows}
        assert by["screen_entries"]["product_ids_json"] == json.dumps([SPOC_PID])
        assert int(by["screen_entries_outside_veto"]["value"]) >= 1                     # the planted dip, no veto
        screen_run = [r for r in led.runs() if r["script"].endswith(":residual_screen")][0]
        assert by["screen_entries"]["run_id"] == screen_run["id"]
        [prod] = led.products("MAST")
        assert prod["product_id"] == SPOC_PID and prod["checksum"] == sha256(lc)
    finally:
        led.close()
    rec = _record(tmp_path, "real-run")
    [c] = [c for c in rec["checks"] if c["name"] == "Product integrity (SHA-256)"]
    assert c["state"] == "passed" and c["note"] == "1 product(s) from MAST verified; pinned checksums matched"
    assert c["source"] == "campaign runner, step fetch_products"
    assert rec["products"] == [{"id": SPOC_PID, "archive": "MAST", "sha256": sha256(lc), "format": "spoc_lc"}]

"""Campaign runner, ledger run guarantees, catalogue adapters and the target queue.

Everything here is synthetic (tmp_path, in-memory fetchers); no network. The equivalence of the
runner with the original 2026-09-24 scripts was checked on the real WASP-12 light curves
(byte-identical normalized series, identical screen entries and BLS results) and is recorded in
docs/CAMPAIGNS.md.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from cygnus.ledger import Ledger
from cygnus.priorart import catalogue_audit
from cygnus.targets import build_queue


# ------------------------------------------------------------------ ledger runs
def test_recorded_run_closes_completed_failed_and_aborted():
    led = Ledger(":memory:")
    with led.recorded_run("t:ok") as r:
        r.summary = "fine"
    assert led.run(r.id)["status"] == "completed"
    with pytest.raises(ValueError):
        with led.recorded_run("t:boom") as r2:
            raise ValueError("bad input")
    assert led.run(r2.id)["status"] == "failed" and "bad input" in led.run(r2.id)["summary"]
    with pytest.raises(KeyboardInterrupt):
        with led.recorded_run("t:int") as r3:
            raise KeyboardInterrupt
    assert led.run(r3.id)["status"] == "aborted"
    assert not [x for x in led.runs() if x["status"] == "open"]


def test_close_stale_runs_only_touches_old_open_runs():
    led = Ledger(":memory:")
    old = led.log_run("x")
    led.db.execute("UPDATE runs SET started_utc='2020-01-01T00:00:00Z' WHERE id=?", (old,))
    new = led.log_run("y")
    done = led.log_run("z")
    led.db.execute("UPDATE runs SET started_utc='2020-01-01T00:00:00Z' WHERE id=?", (done,))
    led.close_run(done, "completed")
    ids = led.close_stale_runs(started_before_utc="2021-01-01T00:00:00Z", note="process died")
    assert ids == [old]
    assert led.run(old)["status"] == "aborted" and "process died" in led.run(old)["summary"]
    assert led.run(new)["status"] == "open" and led.run(done)["status"] == "completed"


# ------------------------------------------------------------------ catalogue adapters
def test_catalogue_audit_reports_matches_no_match_and_errors():
    def fake(url, adql):
        if "pscomppars" in adql:
            return [{"pl_name": "Fake b", "hostname": "Fake", "ra": "10.0", "dec": "20.0"},
                    {"pl_name": "Far b", "hostname": "Far", "ra": "11.0", "dec": "20.0"}]   # outside radius: dropped
        if "FROM toi" in adql:
            return []
        if "vsx" in adql:
            raise TimeoutError("service down")
        return [{"main_id": "Fake", "otype": "*", "ra": "10.0001", "dec": "20.0"}]

    res = catalogue_audit(10.0, 20.0, radius_arcsec=30, fetch=fake)
    assert res["NASA_Exoplanet_Archive"]["state"] == "done" and res["NASA_Exoplanet_Archive"]["matches"] == ["Fake b (host Fake)"]
    assert res["TESS_TOI"]["result"].startswith("no match in TESS_TOI within 30\"")
    assert res["VSX"]["state"] == "error" and res["VSX"]["result"].startswith("inconclusive")   # never "no match"
    assert "CONTAINS" in res["SIMBAD"]["query"] and "BETWEEN" in res["TESS_TOI"]["query"]


# ------------------------------------------------------------------ target queue
def test_queue_ranks_with_stated_formula_and_keeps_unranked():
    rows = [
        {"toi": "1.01", "tid": "11", "tfopwg_disp": "PC", "ra": "1", "dec": "2", "st_tmag": "10", "pl_trandep": "1000",
         "pl_trandurh": "4", "pl_tranmid": "2459000.5", "pl_orbper": "", "sectors": "", "toi_created": "", "rowupdate": ""},
        {"toi": "2.01", "tid": "22", "tfopwg_disp": "PC", "ra": "3", "dec": "4", "st_tmag": "8", "pl_trandep": "1000",
         "pl_trandurh": "4", "pl_tranmid": "2459001.5", "pl_orbper": "", "sectors": "", "toi_created": "", "rowupdate": ""},
        {"toi": "3.01", "tid": "33", "tfopwg_disp": "PC", "ra": "5", "dec": "6", "st_tmag": "", "pl_trandep": "900",
         "pl_trandurh": "2", "pl_tranmid": "", "pl_orbper": "", "sectors": "", "toi_created": "", "rowupdate": ""},
    ]
    q = build_queue({"top": 5}, fetch=lambda adql: rows)
    assert [t["name"] for t in q["queue"]] == ["TOI-2.01", "TOI-1.01"]            # brighter star first
    assert q["queue"][0]["score"] == pytest.approx(1000 * 2 * 10 ** 0.4)
    assert q["unranked"] and q["unranked"][0][0] == "TOI-3.01"
    assert "pl_orbper IS NULL" in q["query"] and q["pool_size"] == 3


# ------------------------------------------------------------------ runner, end to end on a synthetic light curve
np = pytest.importorskip("numpy")
pytest.importorskip("scipy")
pytest.importorskip("yaml")
fits = pytest.importorskip("astropy.io.fits")


def _fake_spoc(path: Path, *, dip_at: float | None, depth: float = 0.03, seed: int = 1) -> None:
    rng = np.random.default_rng(seed)
    n = 9000
    t = 1500.0 + np.arange(n) * (120 / 86400)
    flux = 1000.0 * (1 + rng.normal(0, 0.001, n))
    if dip_at is not None:
        flux[np.abs(t - dip_at) < 0.06] *= 1 - depth
    q = np.zeros(n, int)
    q[100:110] = 512
    cols = [fits.Column(name=nm, format="D", array=a) for nm, a in
            (("TIME", t), ("SAP_FLUX", flux * 1.01), ("PDCSAP_FLUX", flux), ("MOM_CENTR1", np.full(n, 10.0)),
             ("MOM_CENTR2", np.full(n, 11.0)))] + [fits.Column(name="QUALITY", format="J", array=q)]
    hdu0 = fits.PrimaryHDU()
    hdu0.header.update({"OBJECT": "TIC 1", "TICID": 1, "SECTOR": 7, "TIMEDEL": 120 / 86400, "RA_OBJ": 10.0, "DEC_OBJ": 20.0})
    tab = fits.BinTableHDU.from_columns(cols)
    tab.header.update({"BJDREFI": 2457000, "BJDREFF": 0.0, "TIMESYS": "TDB", "TIMEUNIT": "d"})
    fits.HDUList([hdu0, tab]).writeto(path)


@pytest.fixture()
def world(tmp_path, monkeypatch):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    (tmp_path / "campaigns").mkdir()
    (tmp_path / "reports").mkdir()
    pack = tmp_path / "docs" / "tier1_pack"
    pack.mkdir(parents=True)
    (pack / "NAME_RESOLUTIONS.json").write_text(json.dumps({"Fixture": {"ok": True, "ra_deg": 10.0, "dec_deg": 20.0}}))
    stage = tmp_path / "scratch" / "stage"
    stage.mkdir(parents=True)
    pid = "tess-fixture-s0007-0000000000000001-s_lc.fits"
    _fake_spoc(stage / pid, dip_at=1505.0)
    import hashlib

    sha = hashlib.sha256((stage / pid).read_bytes()).hexdigest()
    (tmp_path / "reports" / "fixture-screen").mkdir()
    (tmp_path / "reports" / "fixture-screen" / "REPORT.md").write_text("# fixture\n")
    spec = f"""schema: cygnus.campaign/1
campaign_id: fixture-screen
objective: synthetic
outputs: reports/fixture-screen/
random_seed: 7
targets: [{{name: Fixture}}]
input:
  products: [{{product_id: {pid}, sector: 7, expected_sha256: {sha}}}]
veto: {{kind: ephemeris, period_days: 3.0, t0_bjd: 2458501.0, veto_phase: 0.02, source: fixture}}
steps:
  - fetch_products: {{search_dirs: ["scratch:stage"]}}
  - residual_screen: {{windows_days: [1.0, 2.0], k_mad: 5.0}}
  - calibrate_screen: {{declared_k: 5.0, k_grid: [3.0, 4.0, 5.0, 6.0], depths_ppm: [2000, 30000], durations_h: [2.0],
                        injections_per_cell: 4, reference_signal: {{depth_ppm: 30000, duration_h: 2.0}}}}
record:
  path: reports/fixture-screen/sky_record.json
  title: Fixture screen
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/fixture-screen/REPORT.md
  summary: Synthetic.
  checks:
    - {{name: "Pixel-level audit", state: not_tested}}
"""
    (tmp_path / "campaigns" / "fixture-screen.yaml").write_text(spec, encoding="utf-8")
    return tmp_path


def test_runner_end_to_end_ledgers_everything_and_reuses(world):
    from cygnus import skyrecord
    from cygnus.campaign.runner import run

    led = Ledger(world / "ledger.sqlite")
    out = run(world / "campaigns" / "fixture-screen.yaml", ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"]
    runs = led.runs()
    assert [r["script"].split(":")[-1] for r in runs] == ["fetch_products", "residual_screen", "calibrate_screen"]
    assert all(r["status"] == "completed" for r in runs)
    names = {m["name"] for r in runs for m in led.measurements_for_run(r["id"])}
    assert {"screen_entries_outside_veto", "calibrated_k_mad", "depth_for_90pct_completeness"} <= names
    screen = json.loads((world / "reports/fixture-screen/sector07/screen.json").read_text())
    outside = [e for e in screen["screened_excursions"] if not e["inside_veto"]]
    assert outside and all(abs(e["mid_time_BJD_like"] - 2458505.0) < 0.1 for e in outside)   # the planted dip, nothing else
    rec = json.loads((world / "reports/fixture-screen/sky_record.json").read_text())
    assert rec["status"] == "completed" and rec["generated_by"] == "cygnus.campaign runner"
    states = {c["name"]: c["state"] for c in rec["checks"]}
    assert states["Pixel-level audit"] == "not_tested" and states["Product integrity (SHA-256)"] == "passed"
    assert states["Synthetic signal injection–recovery"] == "passed"                      # 3 % boxes are easy
    assert skyrecord.validate({**rec, "_path": "reports/fixture-screen/sky_record.json"}, world,
                              skyrecord.known_positions(world)) == []
    # second run reuses every step
    msgs = []
    run(world / "campaigns" / "fixture-screen.yaml", ledger=led, root=world, echo=msgs.append)
    assert all("reused" in m for m in msgs) and len(led.runs()) == 3


def test_runner_refuses_checksum_mismatch_and_records_failure(world):
    from cygnus.campaign.runner import run

    spec = world / "campaigns" / "fixture-screen.yaml"
    spec.write_text(spec.read_text().replace("expected_sha256: ", "expected_sha256: 00"), encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    with pytest.raises(RuntimeError, match="checksum"):
        run(spec, ledger=led, root=world, echo=lambda *_: None)
    [r] = led.runs()
    assert r["status"] == "failed" and "checksum" in r["summary"]


def test_spec_validation_rejects_unknown_steps_and_incomplete_veto(tmp_path):
    from cygnus.campaign.runner import SpecError, load_spec

    p = tmp_path / "x.yaml"
    p.write_text("schema: cygnus.campaign/1\ncampaign_id: x-y\noutputs: out/\nveto: {kind: ephemeris, period_days: 1}\n"
                 "steps:\n  - singletransit: {}\n", encoding="utf-8")
    with pytest.raises(SpecError) as e:
        load_spec(p)
    assert "not implemented" in str(e.value) and "veto.t0_bjd" in str(e.value)


# ------------------------------------------------------------------ known-object loop: new → run → report → queue
def test_known_object_loop_offline(tmp_path, monkeypatch):
    """A generated known-object campaign recovers the planted 'catalogued' transit, finds the planted
    repeat, lists period aliases, flags an unverified lead (never higher) and drafts its report."""
    import hashlib

    from cygnus import priorart, skyrecord
    from cygnus.campaign import scaffold, steps
    from cygnus.campaign.runner import load_spec, run

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    (tmp_path / "campaigns").mkdir()
    t = {"name": "TOI-9.01", "tic": 1, "ra_deg": 10.0, "dec_deg": 20.0, "t0_bjd": 2458505.0, "period_days": None,
         "depth_ppm": 30000.0, "duration_h": 2.88, "tmag": 9.0, "position_source": "fixture", "disposition": "PC"}
    spec_path = scaffold.write_spec(tmp_path, t, parent="fixture-queue", origin="fixture", seed=5)
    assert spec_path.name == "toi-9-01.yaml"
    with pytest.raises(SystemExit, match="claimed"):
        scaffold.write_spec(tmp_path, t, parent=None, origin="fixture", seed=5)
    spec = load_spec(spec_path)
    assert spec["targets"][0]["period_days"] is None and spec["veto"]["kind"] == "single_epoch"

    pid = "tess-fixture-s0007-0000000000000001-s_lc.fits"
    lcdir = tmp_path / "scratch" / "campaign_toi-9-01"
    lcdir.mkdir(parents=True)
    _fake_spoc(lcdir / pid, dip_at=1505.0)
    # plant a repeat 6 days later in the same light curve
    with fits.open(lcdir / pid, mode="update") as h:
        tt = h[1].data["TIME"]
        for col in ("SAP_FLUX", "PDCSAP_FLUX"):
            h[1].data[col][np.abs(tt - 1511.0) < 0.06] *= 0.97
    monkeypatch.setattr(steps, "_discover_spoc_lcs", lambda tic, n, t0=None: [
        {"product_id": pid, "tic": tic, "sector": 7, "covers_known_epoch": True}])
    monkeypatch.setattr(priorart, "catalogue_audit", lambda ra, dec, **kw: {
        "TESS_TOI": {"state": "done", "result": "1 match", "query": "q", "retrieved_utc": "2026-01-01T00:00:00Z", "matches": ["TOI-9.01"]}})

    led = Ledger(tmp_path / "ledger.sqlite")
    out = run(spec_path, ledger=led, root=tmp_path, echo=lambda *_: None)
    assert out["complete"] and all(r["status"] == "completed" for r in led.runs())
    states = {c["name"]: c["state"] for c in json.loads((tmp_path / "campaigns/toi-9-01/sky_record.json").read_text())["checks"]}
    assert states["Known-signal recovery (positive control)"] == "passed"
    assert states["Period aliases (repeat events)"] == "inconclusive"
    assert states["Difference-image centroids / blend audit"] == "not_tested"
    rec = json.loads((tmp_path / "campaigns/toi-9-01/sky_record.json").read_text())
    assert rec["outcome"] == "lead" and rec["evidence"] == "Unverified lead"
    known = json.loads((tmp_path / "campaigns/toi-9-01/runner/known_signal_recovery.json").read_text())["result"]
    ep = known["per_product"][pid]["epochs"][0]
    assert ep["state"] == "recovered" and 20000 < ep["measured_depth_ppm"] < 40000
    al = json.loads((tmp_path / "campaigns/toi-9-01/period_aliases.json").read_text())["candidates"]
    assert len(al) == 1 and abs(al[0]["delta_t_days"] - 6.0) < 0.01
    allowed = {a["n"] for a in al[0]["aliases"] if a["verdict"] == "allowed"}
    assert 1 in allowed and 2 not in allowed          # P = 3 d predicts a transit at 1508 d on usable data: excluded

    # report drafts, then the record validates and the queue board sees it
    spec["_path"] = spec_path
    written = scaffold.draft_report(spec, tmp_path)
    assert [p.name for p in written] == ["REPORT.md", "SEARCH_LOG.md"]
    text = written[0].read_text(encoding="utf-8")
    assert scaffold.DRAFT_MARKER in text and "recovered the catalogued transit" in text and "Repeat candidate" in text
    assert skyrecord.validate({**rec, "_path": "campaigns/toi-9-01/sky_record.json"}, tmp_path, {}) == []
    written[0].write_text(text.replace(scaffold.DRAFT_MARKER + "\n", ""), encoding="utf-8")   # reviewed
    again = scaffold.draft_report(spec, tmp_path)
    assert again[0].name == "REPORT.draft.md"                                                 # reviewed text is never overwritten
    q = tmp_path / "queue.csv"
    q.write_text("name,tic,ra_deg,dec_deg,t0_bjd,rank\nTOI-9.01,1,10,20,2458505.0,1\nTOI-8.01,2,11,21,2458600.0,2\n", encoding="utf-8")
    board = {s["name"]: s for s in scaffold.queue_status(tmp_path, q)}
    assert board["TOI-9.01"]["state"] == "completed" and board["TOI-9.01"]["known_signal"] == "passed"
    assert board["TOI-9.01"]["review"] == "reviewed" and board["TOI-8.01"]["state"] == "unclaimed"
    assert scaffold.pick_from_queue(tmp_path, q, None)["name"] == "TOI-8.01"


def test_threshold_falls_back_to_declared_k_when_calibration_finds_no_k_star():
    from cygnus.campaign.steps import _threshold

    class Ctx:
        def optional_result(self, step, default):
            return {"per_product": {"a": {"k_star": None}, "b": {"k_star": 4.0}}, "declared_k": 5.0}
    k, src = _threshold(Ctx(), "a", "calibrated")
    assert k == 5.0 and src.startswith("UNCALIBRATED")
    assert _threshold(Ctx(), "b", "calibrated") == (4.0, "calibrated (calibrate_screen)")
    assert _threshold(Ctx(), "b", 6) == (6.0, "declared in campaign spec")


def test_group_entries_merges_overlaps_and_marks_persistence():
    from cygnus.campaign.steps import group_entries

    def e(a, b, flux, base, r=-0.01):
        return {"start_time_stored": a, "end_time_stored": b, "flux_type": flux, "detrend_days": base, "n_cadences": 3,
                "median_fractional_residual": r, "mid_time_BJD_like": (a + b) / 2}
    g = group_entries([e(1.0, 1.1, "SAP", 1.0), e(1.05, 1.12, "PDCSAP", 2.0, -0.02), e(1.0, 1.1, "SAP", 2.0), e(5, 5.1, "SAP", 1.0)], 3)
    assert len(g) == 2 and g[0]["persistent"] and not g[1]["persistent"]
    assert g[0]["deepest_median_residual"] == -0.02 and g[0]["n_entries"] == 3


def test_no_products_is_a_documented_exclusion_not_a_red_run(world, monkeypatch):
    """A target with no available products is recorded as a null with not_tested checks."""
    from cygnus.campaign import steps as campaign_steps
    from cygnus.campaign.runner import run

    monkeypatch.setattr(campaign_steps, "_discover_spoc_lcs", lambda *a, **k: [])
    (world / "reports" / "no-data").mkdir()
    (world / "reports" / "no-data" / "REPORT.md").write_text("# no-data fixture\n", encoding="utf-8")
    spec = """schema: cygnus.campaign/1
campaign_id: no-data
objective: synthetic no-data
outputs: reports/no-data/
targets: [{name: Fixture, tic: 1}]
steps:
  - fetch_products: {from_targets: {max_products_per_target: 1}}
  - residual_screen: {k_mad: 5.0}
record:
  path: reports/no-data/sky_record.json
  title: No-data fixture
  kind: known-object test
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/no-data/REPORT.md
  summary: Synthetic no-data.
  checks:
    - {name: "Product integrity (SHA-256)", state: not_tested}
"""
    (world / "campaigns" / "no-data.yaml").write_text(spec, encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    out = run(world / "campaigns" / "no-data.yaml", ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"]
    assert all(r["status"] == "completed" for r in led.runs())
    rec = json.loads((world / "reports/no-data/sky_record.json").read_text(encoding="utf-8"))
    checks = {c["name"]: c for c in rec["checks"]}
    assert checks["Product integrity (SHA-256)"]["state"] == "not_tested"
    assert "no products" in checks["Product integrity (SHA-256)"]["note"]
    assert checks["Calibrated false-alarm threshold (sign-flip null)"]["state"] == "not_tested"
    assert rec["outcome"] == "pipeline_check"   # not a scientific bound: no data was analysed


@pytest.mark.parametrize("steps, message", [
    ("  - known_signal_recovery: {}\n  - fetch_products: {}\n  - calibrate_screen: {}\n",
     "known_signal_recovery must come after fetch_products"),
    ("  - fetch_products: {}\n  - residual_screen: {k_mad: calibrated}\n",
     "k_mad 'calibrated' requires a calibrate_screen step"),
    ("  - fetch_products: {}\n  - known_signal_recovery: {}\n  - calibrate_screen: {}\n",
     "calibrate_screen must come before it"),
])
def test_step_order_is_validated(tmp_path, steps, message):
    from cygnus.campaign.runner import SpecError, load_spec

    spec = tmp_path / "bad.yaml"
    spec.write_text("schema: cygnus.campaign/1\ncampaign_id: bad\noutputs: campaigns/bad/\nsteps:\n" + steps,
                    encoding="utf-8")
    with pytest.raises(SpecError, match=re.escape(message)):
        load_spec(spec)

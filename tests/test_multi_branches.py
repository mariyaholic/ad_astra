"""Branch matrix for cygnus.multi steps (docs/SUITE_EXPANSION.md §4.1 item 2).

Thresholds, veto masks, the calibrated screen, the systematics-model fallback, screen-suitability
gates, SPOC discovery, checksum/size refusal, the from_queue branch and the MAST download seam.
Everything offline: discovery and download are monkeypatched.
"""

from __future__ import annotations

import json
import types
from pathlib import Path

import numpy as np
import pytest

pytest.importorskip("yaml")
pytest.importorskip("scipy")
pytest.importorskip("astropy.io.fits")

from cygnus.ledger import Ledger  # noqa: E402

from _multi_fixtures import SPOC_PID, make_ctx, product_entry, sha256, write_spoc  # noqa: E402


@pytest.fixture()
def scratch(tmp_path, monkeypatch):
    d = tmp_path / "scratch"
    d.mkdir()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(d))
    return d


# ------------------------------------------------------------------ _threshold
class _Cal:
    def __init__(self, cal):
        self.cal = cal

    def optional_result(self, step, default):
        return self.cal if step == "calibrate_screen" and self.cal is not None else default


def test_threshold_declared_calibrated_uncalibrated_and_missing_calibration():
    from cygnus.multi.steps import _threshold

    cal = _Cal({"per_product": {"a": {"k_star": None}, "b": {"k_star": 4.5}}, "declared_k": 6.0})
    assert _threshold(cal, "b", 7) == (7.0, "declared in campaign spec")
    assert _threshold(cal, "b", "calibrated") == (4.5, "calibrated (calibrate_screen)")
    k, src = _threshold(cal, "a", "calibrated")
    assert k == 6.0 and src.startswith("UNCALIBRATED")
    k, src = _threshold(cal, "not-calibrated-product", "calibrated")     # absent from the calibration
    assert k == 6.0 and src.startswith("UNCALIBRATED")
    with pytest.raises(RuntimeError, match="needs a calibrate_screen step"):
        _threshold(_Cal(None), "a", "calibrated")


# ------------------------------------------------------------------ _veto_mask
def _lc(t_bjd):
    t_bjd = np.asarray(t_bjd, float)
    return types.SimpleNamespace(time=t_bjd - 2457000, time_bjd=t_bjd)


def test_veto_mask_none_ephemeris_single_epoch_and_unknown_kind():
    from cygnus.multi.steps import _veto_mask

    t = 2458500.0 + np.arange(0, 6, 0.01)
    m, ph = _veto_mask(_lc(t), None, None)
    assert not m.any() and ph is None and m.size == t.size

    eph = {"kind": "ephemeris", "period_days": 2.0, "t0_bjd": 2458501.0, "veto_phase": 0.02}
    m, ph = _veto_mask(_lc(t), eph, None)
    assert ph is not None and ph.min() >= 0 and ph.max() < 1
    centres = [2458501.0, 2458503.0, 2458505.0]
    expect = np.zeros(t.size, bool)
    for c in centres:
        expect |= np.abs(t - c) < 0.02 * 2.0
    assert np.array_equal(m, expect)

    se = {"kind": "single_epoch", "veto_hours": 12, "t0_bjd": 2458502.0}
    m, ph = _veto_mask(_lc(t), se, {"t0_bjd": 2458504.0})            # the target's own epoch wins
    assert ph is None and np.array_equal(m, np.abs(t - 2458504.0) <= 0.5)
    m, _ = _veto_mask(_lc(t), se, None)                                 # falls back to the veto's epoch
    assert np.array_equal(m, np.abs(t - 2458502.0) <= 0.5)

    with pytest.raises(ValueError, match="unknown veto kind 'periodic'"):
        _veto_mask(_lc(t), {"kind": "periodic"}, None)


# ------------------------------------------------------------------ calibrated residual screen, end to end
def _screen_world(root: Path, scratch: Path, steps_yaml: str, *, cid="cal-fixture", dips=(1501.5,)) -> Path:
    lc = write_spoc(scratch / "stage" / SPOC_PID, n=3000, dips=dips)
    (root / "campaigns").mkdir(exist_ok=True)
    spec = f"""schema: cygnus.campaign/1
campaign_id: {cid}
outputs: campaigns/{cid}/
random_seed: 11
targets: [{{name: Fixture, ra_deg: 10.0, dec_deg: 20.0, frame: ICRS, epoch: J2000.0, position_source: fixture}}]
input:
  products: [{{product_id: {SPOC_PID}, target: Fixture, sector: 7, expected_sha256: {sha256(lc)}}}]
steps:
{steps_yaml}record:
  path: campaigns/{cid}/sky_record.json
  title: Calibration fixture
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: campaigns/{cid}/REPORT.md
  summary: Synthetic.
  checks:
    - {{name: "Pixel-level audit", state: not_tested}}
"""
    p = root / "campaigns" / f"{cid}.yaml"
    p.write_text(spec, encoding="utf-8")
    return p


def _run(spec, root):
    from cygnus.multi.runner import run

    led = Ledger(root / "ledger.sqlite")
    try:
        return run(spec, ledger=led, root=root, echo=lambda *_: None), led.runs()
    finally:
        led.close()


CAL = ("  - calibrate_screen: {{declared_k: 5.0, k_grid: {grid}, depths_ppm: [30000], durations_h: [2.0],\n"
       "                       injections_per_cell: 3, reference_signal: {{depth_ppm: 30000, duration_h: 2.0}}}}\n")


def test_calibrated_k_mad_screens_at_k_star_and_passes_the_checks(tmp_path, scratch):
    steps_yaml = ("  - fetch_products: {search_dirs: [\"scratch:stage\"]}\n" + CAL.format(grid="[4.0, 6.0]")
                  + "  - residual_screen: {windows_days: [1.0, 2.0], k_mad: calibrated, rednoise_trials: 20}\n")
    out, _ = _run(_screen_world(tmp_path, scratch, steps_yaml), tmp_path)
    assert out["complete"]
    screen = json.loads(next((tmp_path / "campaigns/cal-fixture").rglob("screen.json")).read_text())
    assert screen["threshold"] == {"k_mad": 4.0, "source": "calibrated (calibrate_screen)"}
    assert "from the campaign's sign-flip calibration" in screen["interpretation_limit"]
    c = out["checks"]["Calibrated false-alarm threshold (sign-flip null)"]
    assert c["state"] == "passed" and c["step"] == "residual_screen" and "≤4" in c["note"]      # k* at the grid floor
    inj = out["checks"]["Synthetic signal injection–recovery"]
    assert inj["state"] == "passed" and inj["step"] == "residual_screen" and "100%" in inj["note"]
    summ = json.loads((tmp_path / "campaigns/cal-fixture/runner/residual_screen.json").read_text())["result"]
    assert "threshold_note" not in summ["per_product"][SPOC_PID]


def test_uncalibrated_light_curve_uses_the_declared_k_and_says_so(tmp_path, scratch):
    # at k = 0.5 the sign-flip null always fires, so no k* exists on this grid
    steps_yaml = ("  - fetch_products: {search_dirs: [\"scratch:stage\"]}\n" + CAL.format(grid="[0.5]")
                  + "  - residual_screen: {windows_days: [1.0], k_mad: calibrated, rednoise_trials: 20}\n")
    out, _ = _run(_screen_world(tmp_path, scratch, steps_yaml, cid="uncal-fixture"), tmp_path)
    screen = json.loads(next((tmp_path / "campaigns/uncal-fixture").rglob("screen.json")).read_text())
    assert screen["threshold"]["k_mad"] == 5.0 and screen["threshold"]["source"].startswith("UNCALIBRATED")
    assert "is an uncalibrated screen" in screen["interpretation_limit"]
    summ = json.loads((tmp_path / "campaigns/uncal-fixture/runner/residual_screen.json").read_text())["result"]
    assert summ["per_product"][SPOC_PID]["threshold_note"].startswith("UNCALIBRATED")
    c = out["checks"]["Calibrated false-alarm threshold (sign-flip null)"]
    assert c["state"] == "inconclusive" and "used the declared k, uncalibrated" in c["note"]
    assert "none" in c["note"]
    # no calibrated completeness exists, so the residual screen leaves calibrate_screen's own injection check
    assert out["checks"]["Synthetic signal injection–recovery"]["step"] == "calibrate_screen"


def test_systematics_model_failure_does_not_break_the_screen(tmp_path, scratch, monkeypatch):
    from cygnus.multi import systematics

    def boom(*a, **k):
        raise ValueError("synthetic model failure")

    monkeypatch.setattr(systematics, "product_summary", boom)
    steps_yaml = ("  - fetch_products: {search_dirs: [\"scratch:stage\"]}\n"
                  "  - residual_screen: {windows_days: [1.0], k_mad: 5.0}\n")
    out, runs = _run(_screen_world(tmp_path, scratch, steps_yaml, cid="sys-fixture"), tmp_path)
    assert out["complete"] and all(r["status"] == "completed" for r in runs)
    screen = json.loads(next((tmp_path / "campaigns/sys-fixture").rglob("screen.json")).read_text())
    assert screen["systematics_model"] == {"error": "ValueError: synthetic model failure"}
    assert screen["screened_excursions"]                                          # the planted dip is still found


# ------------------------------------------------------------------ screen-suitability gates (fetch_products)
def _pinned(ctx_scratch: Path, pid: str, **kw) -> dict:
    path = write_spoc(ctx_scratch / pid, **kw)
    return {"product_id": pid, "sector": 7, "expected_sha256": sha256(path)}


def test_sparse_and_long_cadence_products_are_excluded_from_the_screen(tmp_path, scratch):
    from cygnus.multi import steps
    from cygnus.config import scratch_dir

    cdir = scratch_dir("campaign_unit-ctx")
    sparse = "tess-sparse-s0007-0000000000000002-s_lc.fits"
    slow = "tess-slow-s0007-0000000000000003-s_lc.fits"
    good = "tess-good-s0007-0000000000000004-s_lc.fits"
    prods = [_pinned(cdir, sparse, n=80), _pinned(cdir, slow, n=300, cadence_s=3600), _pinned(cdir, good, n=400)]
    ctx = make_ctx(tmp_path, spec={"input": {"products": prods}})
    out = steps.step_fetch_products(ctx, {})
    assert out["lightcurve_products"] == [good]
    s = {pid: out["products"][pid]["screen_suitability"] for pid in (sparse, slow, good)}
    assert s[sparse]["screenable"] is False and s[sparse]["reason"] == "80 usable cadence(s) < 100"
    assert s[slow]["screenable"] is False and s[slow]["reason"].startswith("cadence 3600 s > 1800 s")
    assert s[good] == {"usable_cadences": 400, "cadence_s": pytest.approx(120.0), "screenable": True}
    c = ctx.checks["Light-curve suitability for the residual screen"]
    assert c["state"] == "inconclusive" and c["note"].startswith("1 light curve(s) screenable; 2 excluded")
    assert any(n.startswith(f"{sparse}: not screened") for n in ctx.notes)
    assert ctx.checks["Product integrity (SHA-256)"]["state"] == "passed"


def test_all_unsuitable_light_curves_leave_nothing_to_screen(tmp_path, scratch):
    from cygnus.multi import steps
    from cygnus.config import scratch_dir

    ctx = make_ctx(tmp_path, spec={"input": {"products": [_pinned(scratch_dir("campaign_unit-ctx"), SPOC_PID, n=50)]}})
    out = steps.step_fetch_products(ctx, {"min_usable_cadences": 60})
    assert out["lightcurve_products"] == []
    assert out["products"][SPOC_PID]["screen_suitability"]["reason"] == "50 usable cadence(s) < 60"
    assert ctx.checks["Light-curve suitability for the residual screen"]["note"].startswith("0 light curve(s) screenable")
    # the screen then has nothing to read
    ctx._results["fetch_products"] = out
    res = steps.step_residual_screen(ctx, {"k_mad": 5.0})
    assert res["per_product"] == {} and res["entries_outside_veto_total"] == 0


# ------------------------------------------------------------------ discovery branches
def test_empty_spoc_discovery_is_a_documented_exclusion(tmp_path, scratch, monkeypatch):
    """MAST answered and holds no SPOC light curve: a recorded null (as the campaign twin), not a red run."""
    from cygnus.multi import steps

    monkeypatch.setattr(steps, "_discover_spoc_lcs", lambda tic, n, t0=None: [])
    ctx = make_ctx(tmp_path, spec={"targets": [{"name": "Fixture", "tic": 1}]})
    res = steps.step_fetch_products(ctx, {"from_targets": {"max_products_per_target": 1}})
    assert res["excluded"] and res["products"] == {} and res["lightcurve_products"] == []
    assert ctx.notes[0] == "Fixture: no SPOC 120-s light curve found at MAST for TIC 1."
    assert "no SPOC 120-s light curve" in res["exclusion"]
    assert ctx.checks["Product integrity (SHA-256)"]["state"] == "not_tested"
    assert ctx.outcome == ("pipeline_check", None)
    # the steps that need products leave their checks not_tested instead of raising
    ctx._results["fetch_products"] = res
    cal = steps.step_calibrate_screen(ctx, {})
    scr = steps.step_residual_screen(ctx, {})
    assert cal["excluded"] and scr["excluded"]
    assert ctx.checks["Calibrated false-alarm threshold (sign-flip null)"]["state"] == "not_tested"


def test_a_spoc_discovery_error_is_still_a_failure(tmp_path, scratch, monkeypatch):
    from cygnus.multi import steps

    def boom(tic, n, t0=None):
        raise TimeoutError("MAST read timed out")

    monkeypatch.setattr(steps, "_discover_spoc_lcs", boom)
    ctx = make_ctx(tmp_path, spec={"targets": [{"name": "Fixture", "tic": 1}]})
    with pytest.raises(TimeoutError):
        steps.step_fetch_products(ctx, {"from_targets": {"max_products_per_target": 1}})


def test_from_queue_discovers_the_top_queued_targets(tmp_path, scratch, monkeypatch):
    from cygnus.multi import steps
    from cygnus.config import scratch_dir

    write_spoc(scratch_dir("campaign_unit-ctx") / SPOC_PID, n=300)
    calls = []

    def discover(tic, n, t0=None):
        calls.append((tic, n, t0))
        return [{"product_id": SPOC_PID, "tic": tic, "sector": 7, "covers_known_epoch": True}]

    monkeypatch.setattr(steps, "_discover_spoc_lcs", discover)
    queue = [{"name": "TOI-5.01", "tic": 5, "ra_deg": 1.0, "dec_deg": 2.0, "t0_bjd": 2458501.0},
             {"name": "TOI-6.01", "tic": 6, "ra_deg": 3.0, "dec_deg": 4.0, "t0_bjd": 2458502.0}]
    ctx = make_ctx(tmp_path, results={"target_queue": {"queue": queue}})
    out = steps.step_fetch_products(ctx, {"from_queue": {"top": 1, "max_products_per_target": 1}})
    assert calls == [(5, 1, 2458501.0)]                                          # only the top-1 queued target
    p = out["products"][SPOC_PID]
    assert p["target"] == "TOI-5.01" and p["tic"] == 5 and p["archive"] == "MAST" and p["pinned"] is False
    assert p["covers_known_epoch"] is True and p["fetched_now"] is False
    assert "checksummed at first retrieval" in ctx.checks["Product integrity (SHA-256)"]["note"]


def test_from_queue_without_a_target_queue_step_fails_loudly(tmp_path, scratch):
    from cygnus.multi import steps

    ctx = make_ctx(tmp_path)
    with pytest.raises(RuntimeError, match="needs the output of 'target_queue'"):
        steps.step_fetch_products(ctx, {"from_queue": {"top": 1}})


# ------------------------------------------------------------------ integrity refusals
def test_checksum_mismatch_is_refused(tmp_path, scratch):
    from cygnus.multi import steps
    from cygnus.config import scratch_dir

    p = _pinned(scratch_dir("campaign_unit-ctx"), SPOC_PID, n=200)
    p["expected_sha256"] = "0" * 64
    ctx = make_ctx(tmp_path, spec={"input": {"products": [p]}})
    with pytest.raises(RuntimeError, match="checksum/size mismatch.*refusing to analyse"):
        steps.step_fetch_products(ctx, {})
    assert ctx.ledger.count_products() == 0                                        # nothing registered


def test_expected_bytes_mismatch_is_refused_and_a_match_is_accepted(tmp_path, scratch):
    from cygnus.multi import steps
    from cygnus.config import scratch_dir

    p = _pinned(scratch_dir("campaign_unit-ctx"), SPOC_PID, n=200)
    size = (scratch_dir("campaign_unit-ctx") / SPOC_PID).stat().st_size
    ctx = make_ctx(tmp_path, spec={"input": {"products": [{**p, "expected_bytes": size + 1}]}})
    with pytest.raises(RuntimeError, match=f"{size} bytes"):
        steps.step_fetch_products(ctx, {})
    ctx = make_ctx(tmp_path, spec={"input": {"products": [{**p, "expected_bytes": size}]}})
    out = steps.step_fetch_products(ctx, {})
    assert out["products"][SPOC_PID]["bytes"] == size and out["products"][SPOC_PID]["pinned"] is True
    assert "pinned checksums matched" in ctx.checks["Product integrity (SHA-256)"]["note"]


# ------------------------------------------------------------------ the MAST download seam
def test_bare_mast_product_downloads_from_the_mast_url(tmp_path, scratch, monkeypatch):
    from cygnus.ingest import netio
    from cygnus.multi import steps

    staged = write_spoc(tmp_path / "elsewhere" / SPOC_PID, n=200)
    calls = []

    def fetch(url, path, *, timeout_s=None, **kw):
        calls.append((url, Path(path), timeout_s))
        Path(path).write_bytes(staged.read_bytes())

    monkeypatch.setattr(netio, "fetch_to_file", fetch)
    ctx = make_ctx(tmp_path, spec={"input": {"products": [{"product_id": SPOC_PID, "sector": 7,
                                                            "expected_sha256": sha256(staged)}]}})
    out = steps.step_fetch_products(ctx, {})
    url = "https://mast.stsci.edu/api/v0.1/Download/file?uri=mast%3ATESS%2Fproduct%2F" + SPOC_PID
    assert steps.MAST_DOWNLOAD.format(pid=SPOC_PID) == url
    assert calls == [(url, ctx.scratch / SPOC_PID, 120)]
    p = out["products"][SPOC_PID]
    assert p["fetched_now"] is True and p["path"] == f"scratch:campaign_unit-ctx/{SPOC_PID}"
    [row] = ctx.ledger.products("MAST")
    assert row["url"] == url
    # a second fetch finds the file in scratch and does not download again
    ctx2 = make_ctx(tmp_path, spec={"input": {"products": [{"product_id": SPOC_PID, "sector": 7,
                                                             "expected_sha256": sha256(staged)}]}})
    assert steps.step_fetch_products(ctx2, {})["products"][SPOC_PID]["fetched_now"] is False
    assert len(calls) == 1

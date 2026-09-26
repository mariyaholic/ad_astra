"""cygnus.multi steps that previously only had campaign-twin coverage (docs/SUITE_EXPANSION.md §4.1 item 1).

``bls_recovery``, ``period_aliases``, ``prior_art`` and ``target_queue`` on synthetic SPOC-shaped
light curves and monkeypatched catalogue/queue services. Offline and seeded.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
import pytest

pytest.importorskip("yaml")
pytest.importorskip("scipy")
pytest.importorskip("astropy.io.fits")

from cygnus.ledger import Ledger  # noqa: E402

from _multi_fixtures import SPOC_PID, make_ctx, measurements, product_entry, sha256, write_spoc  # noqa: E402


@pytest.fixture()
def scratch(tmp_path, monkeypatch):
    d = tmp_path / "scratch"
    d.mkdir()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(d))
    return d


# ------------------------------------------------------------------ bls_recovery
def test_bls_recovery_finds_the_planted_period_and_writes_results(tmp_path, scratch):
    from cygnus.multi import steps

    lc = write_spoc(scratch / "stage" / SPOC_PID, n=2400, cadence_s=300, periodic=(1.7, 1500.4, 0.01, 0.05))
    ctx = make_ctx(tmp_path, results={"fetch_products": {"products": {SPOC_PID: product_entry(lc)}}})
    out = steps.step_bls_recovery(ctx, {"product": SPOC_PID, "period_grid": [1.0, 3.0, 800],
                                        "duration_arange": [0.06, 0.161, 0.05], "permutation_trials": 5})
    best = out["best_bls"]
    assert best["period_days"] == pytest.approx(1.7, abs=0.01)
    assert best["depth_fraction"] == pytest.approx(0.01, rel=0.25)
    # the planted signal beats every permuted light curve: the smallest FAP 5 trials can give
    assert best["empirical_permutation_fap"] == pytest.approx(1 / 6)
    assert best["power"] > best["null_max_power_95pct"]
    res = json.loads((tmp_path / "out" / "results.json").read_text(encoding="utf-8"))
    assert out["results_json"] == "out/results.json"
    assert res["search"]["permutation_trials"] == 5 and res["search"]["period_grid_count"] == 800
    assert res["sha256"] == sha256(lc) and res["expected_sha256_manifest"] == sha256(lc)   # pinned product
    assert res["product_url"].endswith("mast%3ATESS%2Fproduct%2F" + SPOC_PID)
    # SAP evaluated at the PDCSAP ephemeris carries the same dip (the cross-flux flag)
    assert res["sap_at_pdc_ephemeris"]["depth_fraction"] == pytest.approx(0.01, rel=0.25)
    assert res["n_quality_zero_finite"] == 2400 and res["n_excluded_quality_or_nonfinite"] == 0
    names = {m["name"] for m in measurements(ctx.ledger)}
    assert {"bls_period", "bls_duration", "bls_depth", "bls_power", "permutation_fap_diagnostic"} <= names


def test_bls_recovery_refuses_fewer_than_100_quality_zero_cadences(tmp_path, scratch):
    from cygnus.multi import steps

    bad = np.ones(400, bool)
    bad[:99] = False                                   # 99 quality-zero cadences
    lc = write_spoc(scratch / "stage" / SPOC_PID, n=400, bad_index=bad)
    ctx = make_ctx(tmp_path, results={"fetch_products": {"products": {SPOC_PID: product_entry(lc)}}})
    with pytest.raises(RuntimeError, match="too few quality-zero cadences"):
        steps.step_bls_recovery(ctx, {"product": SPOC_PID, "permutation_trials": 1})
    assert not (tmp_path / "out" / "results.json").exists()


# ------------------------------------------------------------------ period_aliases (through the runner)
def _alias_world(root: Path, scratch: Path, *, outcome="bounded_null", evidence=None, **lc_kw) -> Path:
    """Catalogued transit at BTJD 1501, planted repeat at 1504 (ΔT = 3 d), data to BTJD ~1505.3."""
    cad = lc_kw.pop("cadence_s", 120.0)
    n = int(5.3 * 86400 / cad)
    lc = write_spoc(scratch / "stage" / SPOC_PID, n=n, cadence_s=cad, dips=(1501.0, 1504.0), **lc_kw)
    (root / "campaigns").mkdir(exist_ok=True)
    ev = f"\n  evidence: {evidence}" if evidence else ""
    spec = f"""schema: cygnus.campaign/1
runner: cygnus.multi
campaign_id: alias-fixture
objective: synthetic repeat
outputs: campaigns/alias-fixture/
random_seed: 5
targets:
  - {{name: Fixture, ra_deg: 10.0, dec_deg: 20.0, frame: ICRS, epoch: J2000.0, position_source: fixture,
      t0_bjd: 2458501.0, duration_h: 2.88, depth_ppm: 30000}}
input:
  products: [{{product_id: {SPOC_PID}, target: Fixture, sector: 7, expected_sha256: {sha256(lc)}}}]
veto: {{kind: single_epoch, veto_hours: 6}}
steps:
  - fetch_products: {{search_dirs: ["scratch:stage"]}}
  - residual_screen: {{windows_days: [1.0, 2.0], k_mad: 5.0, rednoise_trials: 20}}
  - known_signal_recovery: {{windows_days: [1.0, 2.0], k_mad: 5.0}}
  - period_aliases: {{min_period_days: 1.0}}
record:
  path: campaigns/alias-fixture/sky_record.json
  title: Alias fixture
  kind: known-object test
  outcome: {outcome}{ev}
  date: "2026-01-02"
  report: campaigns/alias-fixture/REPORT.md
  summary: Synthetic.
  checks:
    - {{name: "Period aliases (repeat events)", state: not_tested}}
"""
    p = root / "campaigns" / "alias-fixture.yaml"
    p.write_text(spec, encoding="utf-8")
    return p


def _run(spec: Path, root: Path):
    from cygnus.multi.runner import run

    led = Ledger(root / "ledger.sqlite")
    try:
        out = run(spec, ledger=led, root=root, echo=lambda *_: None)
    finally:
        led.close()
    rec = json.loads((root / "campaigns/alias-fixture/sky_record.json").read_text(encoding="utf-8"))
    al = json.loads((root / "campaigns/alias-fixture/period_aliases.json").read_text(encoding="utf-8"))
    return out, rec, al


def test_planted_repeat_is_a_candidate_and_flags_only_an_unverified_lead(tmp_path, scratch):
    out, rec, al = _run(_alias_world(tmp_path, scratch), tmp_path)
    assert out["complete"]
    [c] = al["candidates"]
    assert c["delta_t_days"] == pytest.approx(3.0, abs=0.01)
    assert 20000 < c["depth_ppm"] < 40000
    verdict = {a["n"]: a["verdict"] for a in c["aliases"]}
    # P = 3 d predicts transits only outside the data: allowed. P = 1.5 d (BTJD 1502.5) and P = 1 d
    # (1502, 1503, 1505) predict transits on flat usable data: excluded.
    assert verdict == {1: "allowed", 2: "excluded", 3: "excluded"}
    ex = next(a for a in c["aliases"] if a["n"] == 2)["excluded_by"]
    assert ex["predicted_bjd"] == pytest.approx(2458502.5, abs=0.01) and abs(ex["depth_ppm"]) < 0.3 * 30000
    checks = {x["name"]: x for x in rec["checks"]}
    assert checks["Period aliases (repeat events)"]["state"] == "inconclusive"
    assert "1 of 3 aliases" in checks["Period aliases (repeat events)"]["note"]
    assert rec["outcome"] == "lead" and rec["evidence"] == "Unverified lead"      # never higher
    assert any("Repeat candidate" in n for n in out["notes"])


def test_a_predicted_transit_in_a_gap_leaves_the_alias_allowed(tmp_path, scratch):
    # flag the cadences around BTJD 1502.5, the only in-data prediction of P = 1.5 d
    _, _, al = _run(_alias_world(tmp_path, scratch, bad_windows=[(1502.3, 1502.7)]), tmp_path)
    [c] = al["candidates"]
    verdict = {a["n"]: a for a in c["aliases"]}
    assert verdict[2]["verdict"] == "allowed" and verdict[2]["tested_epochs"] == []
    assert verdict[3]["verdict"] == "excluded"                                     # P = 1 d still hits flat data
    assert c["n_allowed"] == 2


def test_alias_exclusion_works_for_a_600s_cadence_product(tmp_path, scratch):
    _, _, al = _run(_alias_world(tmp_path, scratch, cadence_s=600.0), tmp_path)
    [c] = al["candidates"]
    verdict = {a["n"]: a["verdict"] for a in c["aliases"]}
    assert verdict[2] == "excluded"          # BTJD 1502.5 is fully covered by flat 600-s data


def _ref_results(lc_path, state="recovered", screen_events=()):
    return {
        "fetch_products": {"products": {SPOC_PID: product_entry(lc_path, target="Fixture")}},
        "known_signal_recovery": {"per_product": {SPOC_PID: {"epochs": [
            {"epoch_bjd": 2458501.0, "state": state, "measured_depth_ppm": 30000.0, "entry_offset_hours": 0.0}]}}},
        "residual_screen": {"per_product": {SPOC_PID: {"distinct_events_outside_veto": list(screen_events)}}},
    }


def test_unrecovered_reference_leaves_period_aliases_not_tested(tmp_path, scratch):
    from cygnus.multi import steps

    lc = write_spoc(scratch / "stage" / SPOC_PID, n=500)
    ctx = make_ctx(tmp_path, results=_ref_results(lc, state="not_recovered"))
    assert steps.step_period_aliases(ctx, {}) == {"candidates": []}
    assert ctx.checks["Period aliases (repeat events)"]["state"] == "not_tested"
    assert "not recovered" in ctx.checks["Period aliases (repeat events)"]["note"]
    assert ctx.outcome is None


def test_no_matching_repeat_is_not_tested_and_raises_no_lead(tmp_path, scratch):
    from cygnus.multi import steps

    lc = write_spoc(scratch / "stage" / SPOC_PID, n=3000, dips=(1501.0,))
    # a persistent event on flat data (depth ~0) and a non-persistent one: neither matches the reference depth
    evs = [{"mid_time_BJD_like": 2458503.0, "persistent": True}, {"mid_time_BJD_like": 2458501.0, "persistent": False}]
    ctx = make_ctx(tmp_path, spec={"targets": [{"name": "Fixture", "duration_h": 2.88}]},
                   results=_ref_results(lc, screen_events=evs))
    out = steps.step_period_aliases(ctx, {})
    assert out["candidates"] == [] and ctx.outcome is None
    assert ctx.checks["Period aliases (repeat events)"]["state"] == "not_tested"
    assert json.loads((tmp_path / "out" / "period_aliases.json").read_text())["candidates"] == []


# ------------------------------------------------------------------ prior_art
def _audit(states):
    def fake(ra, dec, *, radius_arcsec, services):
        fake.calls.append((ra, dec, radius_arcsec, services))
        out = {}
        for svc, st in states.items():
            res = (f"no match in {svc} within {radius_arcsec:g}\" as of 2026-01-01" if st == "done"
                   else f"inconclusive ({svc} query failed as of 2026-01-01: TimeoutError: down)")
            out[svc] = {"state": st, "result": res, "query": f"q-{svc}", "retrieved_utc": "2026-01-01T00:00:00Z",
                        "matches": []}
        return out
    fake.calls = []
    return fake


def test_prior_art_all_answered_passes_and_is_ledgered(tmp_path, scratch, monkeypatch):
    from cygnus import priorart
    from cygnus.multi import steps

    fake = _audit({"SIMBAD": "done", "VSX": "done"})
    monkeypatch.setattr(priorart, "catalogue_audit", fake)
    ctx = make_ctx(tmp_path, spec={"targets": [{"name": "X", "ra_deg": 1.5, "dec_deg": -2.5}]})
    out = steps.step_prior_art(ctx, {"radius_arcsec": 12, "services": ["SIMBAD", "VSX"]})
    assert fake.calls == [(1.5, -2.5, 12.0, ["SIMBAD", "VSX"])]
    assert set(out["targets"]["X"]) == {"SIMBAD", "VSX"}
    c = ctx.checks["Catalogue cross-match"]
    assert c["state"] == "passed" and "2 answered, 0 errored" in c["note"] and "radius 12″" in c["note"]
    rows = ctx.ledger.prior_art_for("target:X")
    assert sorted(r["service"] for r in rows) == ["SIMBAD", "VSX"]


def test_prior_art_outage_is_inconclusive_in_the_record(tmp_path, scratch, monkeypatch):
    from cygnus import priorart
    from cygnus.multi.runner import run

    monkeypatch.setattr(priorart, "catalogue_audit", _audit({"SIMBAD": "done", "VSX": "error"}))
    (tmp_path / "campaigns").mkdir()
    spec = tmp_path / "campaigns" / "pa.yaml"
    spec.write_text("""schema: cygnus.campaign/1
campaign_id: pa-fixture
outputs: campaigns/pa-fixture/
targets: [{name: X, ra_deg: 1.5, dec_deg: -2.5, frame: ICRS, epoch: J2000.0, position_source: fixture}]
steps:
  - prior_art: {radius_arcsec: 30}
record:
  path: campaigns/pa-fixture/sky_record.json
  title: PA
  kind: smoke
  outcome: bounded_null
  date: "2026-01-02"
  report: campaigns/pa-fixture/REPORT.md
  summary: Smoke.
  checks:
    - {name: "Catalogue cross-match", state: not_tested}
""", encoding="utf-8")
    led = Ledger(tmp_path / "l.sqlite")
    try:
        run(spec, ledger=led, root=tmp_path, echo=lambda *_: None)
        vsx = [r for r in led.prior_art_for("target:X") if r["service"] == "VSX"]
        assert vsx and vsx[0]["result"].startswith("inconclusive")               # never "no match"
    finally:
        led.close()
    rec = json.loads((tmp_path / "campaigns/pa-fixture/sky_record.json").read_text(encoding="utf-8"))
    [c] = [c for c in rec["checks"] if c["name"] == "Catalogue cross-match"]
    assert c["state"] == "inconclusive"
    assert "1 answered, 1 errored" in c["note"] and c["source"] == "campaign runner, step prior_art"


def test_prior_art_with_no_targets_sets_no_check(tmp_path, scratch, monkeypatch):
    from cygnus import priorart
    from cygnus.multi import steps

    monkeypatch.setattr(priorart, "catalogue_audit", _audit({"SIMBAD": "done"}))
    ctx = make_ctx(tmp_path, spec={"targets": []})
    assert steps.step_prior_art(ctx, {}) == {"targets": {}}
    assert "Catalogue cross-match" not in ctx.checks                              # left not_tested by the record


# ------------------------------------------------------------------ target_queue
def _queue(rows):
    def fake(params):
        fake.params = params
        return {"queue": rows, "unranked": [], "pool_size": 7, "query": "SELECT toi FROM toi WHERE x",
                "ranking": {"formula": "depth x duration x flux"}}
    return fake


def test_target_queue_writes_the_ranked_csv_and_measures_the_pool(tmp_path, scratch, monkeypatch):
    from cygnus import targets
    from cygnus.multi import steps

    rows = [{"name": "TOI-2.01", "tic": 22, "ra_deg": 3.0, "dec_deg": 4.0, "score": 2.0},
            {"name": "TOI-1.01", "tic": 11, "ra_deg": 1.0, "dec_deg": 2.0, "score": 1.0}]
    fake = _queue(rows)
    monkeypatch.setattr(targets, "build_queue", fake)
    ctx = make_ctx(tmp_path)
    out = steps.step_target_queue(ctx, {"where": "pl_orbper IS NULL", "top": 2})
    assert fake.params == {"where": "pl_orbper IS NULL", "top": 2}
    assert out["csv"] == "out/target_queue.csv" and out["pool_size"] == 7
    with (tmp_path / "out" / "target_queue.csv").open(encoding="utf-8", newline="") as fh:
        got = list(csv.DictReader(fh))
    assert [r["name"] for r in got] == ["TOI-2.01", "TOI-1.01"] and list(got[0]) == ["name", "tic", "ra_deg", "dec_deg", "score"]
    [m] = [m for m in measurements(ctx.ledger) if m["name"] == "target_pool_size"]
    assert m["value"] == "7" and m["method"] == "SELECT toi FROM toi WHERE x"
    assert ctx.notes == ["Target queue: 2 of 7 pool members ranked by depth x duration x flux."]


def test_empty_target_queue_writes_a_header_only_csv(tmp_path, scratch, monkeypatch):
    from cygnus import targets
    from cygnus.multi import steps

    monkeypatch.setattr(targets, "build_queue", _queue([]))
    ctx = make_ctx(tmp_path)
    out = steps.step_target_queue(ctx, {})
    assert out["queue"] == []
    assert (tmp_path / "out" / "target_queue.csv").read_text(encoding="utf-8").strip() == "name"
    assert ctx.notes[-1].startswith("Target queue: 0 of 7")

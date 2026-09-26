"""Drift guard: ``cygnus.campaign`` and ``cygnus.multi`` must give the same science on the same spec.

The two runners keep separate copies of the known-object steps (``campaign/steps.py`` and
``multi/steps.py``). The multi copy adds archive dispatch and single-channel handling; on a SPOC
light curve both must agree on every number a report quotes. This runs one generated known-object
spec (catalogued transit + a planted repeat) and one no-data spec through both and compares.
Intentional differences are listed in ``docs/SUITE_EXPANSION.md`` (F1).
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

np = pytest.importorskip("numpy")
pytest.importorskip("scipy")
pytest.importorskip("yaml")
fits = pytest.importorskip("astropy.io.fits")

from cygnus.ledger import Ledger

from test_campaign import _fake_spoc

PID = "tess-fixture-s0007-0000000000000001-s_lc.fits"
TARGET = {"name": "TOI-9.01", "tic": 1, "ra_deg": 10.0, "dec_deg": 20.0, "t0_bjd": 2458505.0, "period_days": None,
          "depth_ppm": 30000.0, "duration_h": 2.88, "tmag": 9.0, "position_source": "fixture", "disposition": "PC"}


@pytest.fixture(autouse=True)
def _isolated_registry(monkeypatch):
    """Test-registered adapters never leak (the doc-adapter-count test must pass in any file order)."""
    from cygnus.multi.archives import base

    monkeypatch.setattr(base, "_REGISTRY", dict(base._REGISTRY))
    monkeypatch.setattr(base, "_FACTORIES", dict(base._FACTORIES))


def _both(monkeypatch, found):
    from cygnus import priorart
    from cygnus.campaign import steps as cs
    from cygnus.multi import steps as ms

    for mod in (cs, ms):
        monkeypatch.setattr(mod, "_discover_spoc_lcs", lambda tic, n, t0=None: [dict(d) for d in found])
    monkeypatch.setattr(priorart, "catalogue_audit", lambda ra, dec, **kw: {
        "TESS_TOI": {"state": "done", "result": "1 match", "query": "q", "retrieved_utc": "2026-01-01T00:00:00Z",
                     "matches": ["TOI-9.01"]}})


def _run(root: Path, which: str, spec_path: Path) -> dict:
    if which == "campaign":
        from cygnus.campaign.runner import run
    else:
        from cygnus.multi.runner import run
    led = Ledger(root / f"{which}.sqlite")
    try:
        run(spec_path, ledger=led, root=root, echo=lambda *_: None)
        statuses = [r["status"] for r in led.runs()]
    finally:
        led.close()
    out = root / "campaigns" / "toi-9-01"
    res = {p.stem: json.loads(p.read_text(encoding="utf-8"))["result"] for p in (out / "runner").glob("*.json")
           if p.stem != "RUN_SUMMARY"}
    rec = json.loads((out / "sky_record.json").read_text(encoding="utf-8"))
    return {"results": res, "record": rec, "statuses": statuses, "dir": out}


def _setup(tmp_path, monkeypatch, which, *, with_data=True):
    from cygnus.campaign import scaffold

    root = tmp_path / which
    (root / "campaigns").mkdir(parents=True)
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / f"scratch-{which}"))
    spec = scaffold.write_spec(root, dict(TARGET), parent="fixture-queue", origin="fixture", seed=5)
    if with_data:
        lcdir = tmp_path / f"scratch-{which}" / "campaign_toi-9-01"
        lcdir.mkdir(parents=True)
        master = tmp_path / "master.fits"
        if not master.exists():
            _fake_spoc(master, dip_at=1505.0)
            with fits.open(master, mode="update") as h:          # a repeat 6 d later
                tt = h[1].data["TIME"]
                for col in ("SAP_FLUX", "PDCSAP_FLUX"):
                    h[1].data[col][np.abs(tt - 1511.0) < 0.06] *= 0.97
        shutil.copy(master, lcdir / PID)
    return root, spec


def _science(r: dict) -> dict:
    """The quantities a report quotes, stripped of paths, timestamps and wording."""
    res = r["results"]
    scr = res["residual_screen"]["per_product"]
    cal = res["calibrate_screen"]["per_product"]
    known = res["known_signal_recovery"]["per_product"]
    return {
        "products": {pid: {k: p[k] for k in ("sha256", "bytes", "sector", "covers_known_epoch")}
                     for pid, p in res["fetch_products"]["products"].items()},
        "screen": {pid: {"k": s["k_mad"], "entries": s["entries"], "outside": s["entries_outside_veto"],
                         "events": [{k: e[k] for k in ("mid_time_BJD_like", "deepest_median_residual", "max_cadences",
                                                       "flux_types", "baselines_days", "persistent")}
                                    for e in s["distinct_events_outside_veto"]]} for pid, s in scr.items()},
        "calibration": {pid: {k: c[k] for k in ("null_events_by_k", "k_star", "k_star_at_grid_floor",
                                                 "depth_for_90pct_completeness_ppm", "completeness")}
                        for pid, c in cal.items()},
        "known": {pid: [{k: e.get(k) for k in ("epoch_bjd", "state", "measured_depth_ppm", "depth_err_ppm",
                                               "usable_in_transit_cadences", "flux_types", "entry_offset_hours")}
                        for e in v["epochs"]] for pid, v in known.items()},
        "aliases": res["period_aliases"]["candidates"],
        "checks": {c["name"]: c["state"] for c in r["record"]["checks"]},
        "outcome": (r["record"]["outcome"], r["record"]["evidence"]),
    }


def test_both_runners_give_the_same_science_on_a_spoc_known_object(tmp_path, monkeypatch):
    found = [{"product_id": PID, "tic": 1, "sector": 7, "covers_known_epoch": True}]
    _both(monkeypatch, found)
    got = {}
    for which in ("campaign", "multi"):
        root, spec = _setup(tmp_path, monkeypatch, which)
        got[which] = _run(root, which, spec)
        assert all(s == "completed" for s in got[which]["statuses"]), which
    a, b = _science(got["campaign"]), _science(got["multi"])
    # the multi runner adds record checks of its own (suitability of the light curve for the screen);
    # every check the production runner writes must carry the same state
    extra = set(b["checks"]) - set(a["checks"])
    assert extra <= {"Light-curve suitability for the residual screen"}, extra
    b["checks"] = {k: v for k, v in b["checks"].items() if k in a["checks"]}
    for key in a:
        assert a[key] == b[key], key
    assert a["outcome"] == ("lead", "Unverified lead") and a["aliases"]      # the fixture exercises the lead path
    # the per-product outputs on disk agree too (same seed, same light curve)
    for name in ("screen.json", "calibration.json"):
        ja = json.loads(next(got["campaign"]["dir"].rglob(name)).read_text(encoding="utf-8"))
        jb = json.loads(next(got["multi"]["dir"].rglob(name)).read_text(encoding="utf-8"))
        for k in ("screened_excursions", "rows", "usable", "threshold", "controls", "null_events_by_k", "k_star",
                  "completeness"):
            if k in ja:
                assert ja[k] == jb[k], (name, k)
    pa = (got["campaign"]["dir"] / "period_aliases.json").read_text(encoding="utf-8")
    pb = (got["multi"]["dir"] / "period_aliases.json").read_text(encoding="utf-8")
    assert json.loads(pa) == json.loads(pb)


def test_both_runners_record_a_no_data_target_as_the_same_documented_exclusion(tmp_path, monkeypatch):
    _both(monkeypatch, [])
    got = {}
    for which in ("campaign", "multi"):
        root, spec = _setup(tmp_path, monkeypatch, which, with_data=False)
        got[which] = _run(root, which, spec)
        assert all(s == "completed" for s in got[which]["statuses"]), which
    ca = {c["name"]: c["state"] for c in got["campaign"]["record"]["checks"]}
    cb = {c["name"]: c["state"] for c in got["multi"]["record"]["checks"]}
    assert ca == cb
    assert ca["Product integrity (SHA-256)"] == "not_tested"
    assert ca["Known-signal recovery (positive control)"] == "not_tested"
    assert got["campaign"]["record"]["outcome"] == got["multi"]["record"]["outcome"] == "pipeline_check"


def test_an_archive_outage_is_a_failure_not_a_no_data_exclusion(tmp_path, monkeypatch):
    """Only an archive that answered 'nothing here' is an exclusion; one that could not answer is a failure."""
    from cygnus.multi import runner as mrunner
    from cygnus.multi.archives import base

    class Down(base.ArchiveAdapter):
        name = "down-fixture"
        description = "always unavailable"
        formats = ("csv_lc",)

        def discover(self, target, *, limit=5, **opts):
            raise base.AdapterUnavailable("HTTP 503")

    base.register(Down)
    root = tmp_path / "r"
    (root / "campaigns" / "outage").mkdir(parents=True)
    (root / "campaigns" / "outage" / "REPORT.md").write_text("# o\n", encoding="utf-8")
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    spec = root / "campaigns" / "outage.yaml"
    spec.write_text("""schema: cygnus.campaign/1
campaign_id: outage
objective: outage
outputs: campaigns/outage/
targets: [{name: T, ra_deg: 10.0, dec_deg: 20.0, frame: ICRS, epoch: J2000.0, position_source: fixture}]
steps:
  - fetch_products: {from_targets: {archives: [down-fixture]}}
record:
  path: campaigns/outage/sky_record.json
  title: O
  kind: smoke
  outcome: bounded_null
  date: "2026-01-02"
  report: campaigns/outage/REPORT.md
  summary: Smoke.
  checks: [{name: "Pixel-level audit", state: not_tested}]
""", encoding="utf-8")
    led = Ledger(root / "l.sqlite")
    try:
        with pytest.raises(RuntimeError, match="no products"):
            mrunner.run(spec, ledger=led, root=root, echo=lambda *_: None)
        assert [r["status"] for r in led.runs()] == ["failed"]
    finally:
        led.close()

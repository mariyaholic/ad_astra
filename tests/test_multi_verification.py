"""Regression tests for the defects found in the independent verification of cygnus.multi
(reports/multi-archive-verification-01/). Offline; network seams are faked."""

from __future__ import annotations

import csv
import json
import sys
import types
from pathlib import Path

import numpy as np
import pytest

from cygnus.multi import nss, systematics
from cygnus.multi.archives import base
from cygnus.multi.archives.base import Target
from cygnus.multi.lightcurve import SpocLightCurve, read_campaign_lc
from cygnus.multi.steps import group_entries, significance_state


class _Resp:
    def __init__(self, text="", payload=None, status=200):
        self.text, self._payload, self.status_code = text, payload, status
        self.content = text.encode()

    def json(self):
        return self._payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


# ------------------------------------------------------------------ NSS
NSS_HEAD = ("source_id,nss_solution_type,ra,dec,parallax,period,period_error,eccentricity,eccentricity_error,"
            "semi_amplitude_primary,semi_amplitude_primary_error,mass_ratio,inclination,inclination_error,"
            "significance,goodness_of_fit,flags,astrometric_jitter\n")


def _gaia(source_csv, nss_csv):
    def http(url, data=None, timeout=None, headers=None, params=None):
        q = (data or {}).get("QUERY", "")
        return _Resp(nss_csv if "nss_two_body_orbit" in q else source_csv)
    return base.get("gaia", http=http)


def test_circular_sb1c_solution_is_a_known_companion_not_a_crash():
    """SB1C rows publish no eccentricity; the note must not crash into not_tested (which hid the companion)."""
    row = "111,SB1C,10.0001,20.0,1.5,5.0,0.001,,,30.0,0.5,,,,40.0,1.0,0,\n"
    res = nss.nss_vetting(_gaia("source_id,ra,dec,phot_g_mean_mag,parallax\n111,10.0001,20.0,12.0,1.5\n",
                                NSS_HEAD + row), Target(name="T", ra_deg=10.0, dec_deg=20.0))
    assert res["state"] == "failed"
    sol = res["solutions"][0]
    assert sol["eccentricity"] is None and sol["eccentricity_used"] == 0.0
    # f(M) = P K^3 / (2 pi G) for e = 0, P = 5 d, K = 30 km/s
    expect = 5 * 86400 * 30.0 ** 3 / (2 * np.pi * 1.32712440018e11)
    assert sol["spectroscopic_mass_function_msun"] == pytest.approx(expect, rel=1e-12)
    assert "e 0.00" in res["note"]


def test_several_gaia_sources_in_radius_are_flagged_as_ambiguous():
    src = "source_id,ra,dec,phot_g_mean_mag,parallax\n111,10.0001,20.0,12.0,1.5\n222,10.0005,20.0003,13.0,1.0\n"
    res = nss.nss_vetting(_gaia(src, NSS_HEAD), Target(name="T", ra_deg=10.0, dec_deg=20.0), radius_arcsec=5.0)
    assert res["state"] == "inconclusive"
    assert res["target_match"]["source_id"] == "111" and res["target_match"]["n_sources_in_radius"] == 2
    assert "not unique" in res["note"]


# ------------------------------------------------------------------ channel independence
def _csv(path: Path, cols: dict[str, np.ndarray]) -> Path:
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(list(cols))
        for row in zip(*cols.values()):
            w.writerow(row)
    return path


def test_flux_and_mag_are_not_an_independent_pair(tmp_path):
    t = 2459000.0 + np.arange(300) * 0.01
    f = 1.0 + np.zeros(300)
    lc = read_campaign_lc(_csv(tmp_path / "a.csv", {"time": t, "flux": f, "mag": -2.5 * np.log10(f) + 12}), fmt="csv_lc")
    ch = lc.primary["_channels"]
    assert ch["independent"] is False and ch["sap"] == ch["pdc"]


def test_sap_and_pdcsap_remain_an_independent_pair(tmp_path):
    t = 2459000.0 + np.arange(300) * 0.01
    lc = read_campaign_lc(_csv(tmp_path / "b.csv", {"time": t, "sap_flux": 1 + 0 * t, "pdcsap_flux": 1 + 0 * t}),
                          fmt="csv_lc")
    ch = lc.primary["_channels"]
    assert ch["independent"] is True and (ch["sap"], ch["pdc"]) == ("SAP", "PDCSAP")


# ------------------------------------------------------------------ red-noise model
def _lc(t, flux):
    return SpocLightCurve(path=Path("x.csv"), time=t, sap=flux, pdc=flux, quality=np.zeros(t.size, int), bjdref=0.0,
                          cadence_s=120.0, primary={"_channels": {"independent": False}}, table_header={}, centroids={})


def test_event_duration_comes_from_the_grouped_span_not_one_entry():
    """A 5-h dip whose longest single screen entry is 2 cadences must be tested with a ~5-h box."""
    rng = np.random.default_rng(7)
    t = 1500.0 + np.arange(8000) * (120 / 86400)
    flux = 1.0 + rng.normal(0, 1e-3, t.size)
    flux[np.abs(t - 1505.0) < 5 / 48] -= 0.004                  # 5-h, 4-ppt dip
    entries = [{"start_time_stored": 1505.0 - 5 / 48, "end_time_stored": 1505.0 + 5 / 48, "mid_time_BJD_like": 1505.0,
                "median_fractional_residual": -0.004, "n_cadences": 2, "flux_type": "FLUX", "detrend_days": d}
               for d in (1.0, 2.0)]
    ev = group_entries(entries, 2, single_channel=True)
    assert ev[0]["span_days"] == pytest.approx(10 / 48)
    s = systematics.product_summary(_lc(t, flux), flux, ev, seed=1, n_random=200)["strongest"]
    assert s["duration_days"] == pytest.approx(10 / 48 + 120 / 86400)
    assert s["trial_corrected_fap"] < 1e-3 and s["rednoise_inflation_applied"] is False


def test_parametric_pass_needs_empirical_agreement():
    assert significance_state(1e-4, 1 / 301, 300) == ("passed", True)
    assert significance_state(1e-4, 0.05, 300)[0] == "inconclusive"
    assert significance_state(0.05, 0.05, 300)[0] == "inconclusive"
    assert significance_state(0.5, 0.4, 300)[0] == "failed"


# ------------------------------------------------------------------ adapters
def test_mast_discovery_uses_the_filtered_service_with_column_filters():
    calls = []

    def http(url, data=None, timeout=None, headers=None, params=None):
        req = json.loads(data["request"])
        calls.append(req)
        if req["service"] == "Mast.Caom.Filtered":
            return _Resp(payload={"status": "COMPLETE", "data": [{"obsid": 42}]})
        return _Resp(payload={"status": "COMPLETE", "data": [
            {"productFilename": "tess2020-s0026-0000000000000007-0188-s_lc.fits", "productSubGroupDescription": "LC",
             "dataURI": "mast:TESS/product/x.fits", "obsID": 42}]})

    refs = base.get("mast", http=http).discover(Target(name="T", ra_deg=1.0, dec_deg=2.0, tic=7))
    assert calls[0]["service"] == "Mast.Caom.Filtered"
    filters = {f["paramName"]: f["values"] for f in calls[0]["params"]["filters"]}
    assert filters["target_name"] == ["7"] and filters["provenance_name"] == ["SPOC"]
    assert len(refs) == 1 and refs[0].format == "spoc_lc"


def test_ned_uses_the_live_tap_path_and_columns():
    seen = {}

    def http(url, data=None, timeout=None, headers=None, params=None):
        seen["url"], seen["q"] = url, (data or {}).get("QUERY", "")
        return _Resp("prefname,ra,dec,prefphytype\n\"M 31\",10.68,41.27,G\n")

    base.get("ned", http=http).discover(Target(name="M31", ra_deg=10.68, dec_deg=41.27))
    assert seen["url"].endswith("/tap/sync") and "prefname" in seen["q"]


def test_skybot_empty_field_is_no_match_not_unavailable(monkeypatch):
    class _Skybot:
        @staticmethod
        def cone_search(coo, rad, epoch, **kw):
            raise RuntimeError("No solar system object was found in the requested FOV")

    mod = types.ModuleType("astroquery.imcce")
    mod.Skybot = _Skybot
    monkeypatch.setitem(sys.modules, "astroquery.imcce", mod)
    refs = base.get("skybot").discover(Target(name="F", ra_deg=10.0, dec_deg=5.0), epoch_iso="2024-01-01T00:00:00")
    assert len(refs) == 1 and "(0 rows)" in refs[0].description


# ------------------------------------------------------------------ records and runner dispatch
def _spec(root: Path, record_path="campaigns/xx/sky_record.json", targets=True) -> Path:
    tg = "targets: [{name: X, ra_deg: 1.0, dec_deg: 2.0, frame: ICRS, epoch: J2000.0, position_source: test}]\n"
    p = root / "campaigns" / "x.yaml"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("schema: cygnus.campaign/1\nrunner: cygnus.multi\ncampaign_id: xx\noutputs: campaigns/xx/\n"
                 + (tg if targets else "") + "steps: []\nrecord:\n  path: " + record_path + "\n  title: X\n"
                 "  kind: smoke\n  outcome: bounded_null\n  date: '2026-01-02'\n  report: campaigns/xx/REPORT.md\n"
                 "  summary: Smoke.\n  checks: [{name: A, state: not_tested}]\n", encoding="utf-8")
    return p


def test_invalid_record_is_refused_and_record_path_is_contained(tmp_path, monkeypatch):
    from cygnus.ledger import Ledger
    from cygnus.multi.runner import run

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    led = Ledger(tmp_path / "l.sqlite")
    try:
        with pytest.raises(RuntimeError, match="targets may only be empty"):
            run(_spec(tmp_path, targets=False), ledger=led, root=tmp_path, echo=lambda *_: None)
        with pytest.raises(RuntimeError, match="outside the campaign root"):
            run(_spec(tmp_path, record_path="../escape.json"), ledger=led, root=tmp_path, echo=lambda *_: None)
        assert not (tmp_path.parent / "escape.json").exists()
        run(_spec(tmp_path), ledger=led, root=tmp_path, echo=lambda *_: None)
        assert (tmp_path / "campaigns/xx/sky_record.json").is_file()
    finally:
        led.close()


def test_production_runner_refuses_and_cli_hands_over_multi_specs(tmp_path, capsys):
    from cygnus.campaign import __main__ as campaign_cli
    from cygnus.campaign.runner import SpecError, load_spec

    spec = _spec(tmp_path)
    with pytest.raises(SpecError, match="python -m cygnus.multi"):
        load_spec(spec)
    assert campaign_cli.main(["check", str(spec)]) == 0
    assert json.loads(capsys.readouterr().out)["campaign_id"] == "xx"


def test_an_unfetchable_observing_route_is_a_note_not_a_crash(tmp_path, monkeypatch):
    """Naming an observing route next to a real archive must not abort fetch_products."""
    from cygnus.ledger import Ledger
    from cygnus.multi.runner import run

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    ok = lambda *a, **k: _Resp("reachable")   # noqa: E731
    monkeypatch.setattr(base.get("microobservatory"), "_http", ok)
    src = "source_id,ra,dec,phot_g_mean_mag,parallax\n111,1.0,2.0,12.0,1.5\n"
    monkeypatch.setattr(base.get("gaia"), "_http", lambda url, data=None, **k: _Resp(src))
    spec = _spec(tmp_path)
    spec.write_text(spec.read_text(encoding="utf-8").replace(
        "steps: []", "steps:\n  - fetch_products:\n      from_targets: {archives: [gaia, microobservatory]}"), encoding="utf-8")
    led = Ledger(tmp_path / "l.sqlite")
    try:
        out = run(spec, ledger=led, root=tmp_path, echo=lambda *_: None)
    finally:
        led.close()
    fetched = json.loads((tmp_path / "campaigns/xx/runner/fetch_products.json").read_text(encoding="utf-8"))
    assert list(fetched["result"]["products"]) == ["gaia_cone_X_r30as.csv"]
    assert any("microobservatory: not fetched" in n for n in out["notes"])


def test_magnitudes_are_screened_as_flux_so_a_dimming_is_a_dip(tmp_path):
    t = 2459000.0 + np.arange(400) * (120 / 86400)
    mag = np.full(t.size, 12.0)
    mag[200:210] += 0.02                                   # the star dims by 2%
    lc = read_campaign_lc(_csv(tmp_path / "m.csv", {"time": t, "mag": mag}), fmt="csv_lc")
    assert lc.primary["_channels"]["converted"].startswith("MAG")
    assert lc.pdc[205] < lc.pdc[0]                          # dimmer = lower flux = a dip
    assert lc.pdc[205] == pytest.approx(10 ** (-0.4 * 0.02))
    assert lc.cadence_s == pytest.approx(120.0) and "median time step" in lc.primary["_channels"]["cadence_source"]


def _votable(path: Path, cols: dict[str, np.ndarray]) -> Path:
    from astropy.table import Table

    Table(cols).write(path, format="votable", overwrite=True)
    return path


def test_ztf_votable_prefers_hjd_and_offsets_mjd(tmp_path):
    from cygnus.multi.readers import read_lightcurve

    mjd = 59000.0 + np.arange(5.0)
    both = read_lightcurve(_votable(tmp_path / "a.vot", {"mjd": mjd, "hjd": mjd + 2400000.5 + 0.003,
                                                          "mag": np.full(5, 12.0)}), fmt="ztf_lc")
    assert both.bjdref == 0.0 and both.time_bjd[0] == pytest.approx(2459000.503) and "HJD" in both.time_scale
    only = read_lightcurve(_votable(tmp_path / "b.vot", {"mjd": mjd, "mag": np.full(5, 12.0)}), fmt="ztf_lc")
    assert only.time_bjd[0] == pytest.approx(2459000.5) and "not barycentric" in only.time_scale


def test_a_much_fainter_neighbour_does_not_make_the_identification_ambiguous():
    src = "source_id,ra,dec,phot_g_mean_mag,parallax\n111,10.0001,20.0,7.5,31.0\n222,10.0002,20.0004,13.7,\n"
    res = nss.nss_vetting(_gaia(src, NSS_HEAD), Target(name="T", ra_deg=10.0, dec_deg=20.0), radius_arcsec=5.0)
    m = res["target_match"]
    assert m["identification"] == "unique" and m["n_sources_in_radius"] == 2
    assert m["min_delta_g_to_others"] == pytest.approx(6.2) and "not unique" not in res["note"]


def test_catalogue_cones_are_not_capped_by_the_product_count_and_caps_are_flagged(tmp_path, monkeypatch):
    """max_products_per_target (3) used to become Gaia's TOP 3, dropping the target from its own cone."""
    from cygnus.ledger import Ledger
    from cygnus.multi.runner import run

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    seen = []

    def http(url, data=None, **k):
        seen.append(data["QUERY"])
        top = int(data["QUERY"].split("TOP ")[1].split()[0])
        rows = "".join(f"{i},1.0,2.0,0.5,0,0,{12 + i},1,1,,0\n" for i in range(min(top, 250)))
        return _Resp("source_id,ra,dec,parallax,pmra,pmdec,phot_g_mean_mag,bp_rp,ruwe,radial_velocity,non_single_star\n"
                     + rows)

    monkeypatch.setattr(base.get("gaia"), "_http", http)
    spec = _spec(tmp_path)
    spec.write_text(spec.read_text(encoding="utf-8").replace("steps: []", "steps:\n  - fetch_products:\n"
                    "      from_targets: {archives: [gaia], max_products_per_target: 3}\n  - source_checks: {}"),
                    encoding="utf-8")
    led = Ledger(tmp_path / "l.sqlite")
    try:
        out = run(spec, ledger=led, root=tmp_path, echo=lambda *_: None)
    finally:
        led.close()
    assert "TOP 200" in seen[0]                           # the adapter's own row default, not 3
    assert any("hit the TOP 200 row cap" in n for n in out["notes"])
    checks = json.loads((tmp_path / "campaigns/xx/source_checks.json").read_text(encoding="utf-8"))
    assert any(c["name"] == "gaia row cap" and c["state"] == "inconclusive" for c in checks["gaia_cone_X_r30as.csv"])


def test_inline_query_results_are_rewritten_not_reused_from_scratch(tmp_path, monkeypatch):
    from cygnus.ledger import Ledger
    from cygnus.multi.runner import run

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    stale = tmp_path / "scratch" / "campaign_xx" / "gaia__gaia_cone_X_r30as.csv"
    stale.parent.mkdir(parents=True)
    stale.write_text("source_id,ra,dec\n999,5.0,5.0\n", encoding="utf-8")
    fresh = "source_id,ra,dec,phot_g_mean_mag,parallax\n111,1.0,2.0,8.0,7.0\n"
    monkeypatch.setattr(base.get("gaia"), "_http", lambda url, data=None, **k: _Resp(fresh))
    spec = _spec(tmp_path)
    spec.write_text(spec.read_text(encoding="utf-8").replace(
        "steps: []", "steps:\n  - fetch_products:\n      from_targets: {archives: [gaia]}"), encoding="utf-8")
    led = Ledger(tmp_path / "l.sqlite")
    try:
        run(spec, ledger=led, root=tmp_path, echo=lambda *_: None)
    finally:
        led.close()
    assert "111" in stale.read_text(encoding="utf-8") and "999" not in stale.read_text(encoding="utf-8")

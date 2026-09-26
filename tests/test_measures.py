"""New measures from already-fetched data (docs/SUITE_EXPANSION.md §4.2): units and the campaign steps.

Offline: catalogue services are replaced by fakes behind ``archives.base.get``; light curves are
synthetic and seeded.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

np = pytest.importorskip("numpy")
pytest.importorskip("scipy")
pytest.importorskip("yaml")
fits = pytest.importorskip("astropy.io.fits")

from cygnus.ledger import Ledger
from cygnus.multi import measures as M

from _multi_fixtures import make_ctx, product_entry, write_spoc


# ============================================================================ stellar priors
def _gaia_row(**kw):
    row = {"source_id": "1", "ra": 10.0, "dec": 20.0, "pmra": 0.0, "pmdec": 0.0, "phot_g_mean_mag": 9.67, "bp_rp": 0.82,
           "parallax": 10.0, "parallax_error": 0.02, "ruwe": 1.0}
    row.update(kw)
    return row


def test_a_sun_like_dwarf_gets_solar_priors_from_the_tabulated_sequence():
    p = M.stellar_priors(_gaia_row())
    assert p["usable"]
    assert 5600 < p["teff_k"] < 5950                      # the table's G2V is 5770 K at Bp-Rp 0.823
    assert p["radius_rsun"] == pytest.approx(1.0, abs=0.08) and p["mass_msun"] == pytest.approx(1.0, abs=0.08)
    assert p["density_rho_sun"] == pytest.approx(1.0, abs=0.2)
    assert p["radius_err_rsun"] >= 0.08 * p["radius_rsun"] - 1e-9          # the declared floor is applied
    assert "no extinction" in p["assumptions"]


@pytest.mark.parametrize("row, why", [
    (_gaia_row(phot_g_mean_mag=2.0), "above"),                        # far too luminous for a dwarf of its colour
    (_gaia_row(phot_g_mean_mag=14.0), "below"),
    (_gaia_row(parallax_error=5.0), "parallax/error"),
    (_gaia_row(ruwe=2.1), "RUWE"),
    (_gaia_row(bp_rp=None), "no Bp-Rp"),
    (_gaia_row(bp_rp=9.0), "outside the tabulated dwarf range"),
    (_gaia_row(parallax=-1.0), "no positive parallax"),
])
def test_dwarf_priors_are_withheld_with_a_reason(row, why):
    p = M.stellar_priors(row)
    assert not p["usable"] and why in p["reason"]


def test_colour_interpolation_stops_where_the_table_turns_over():
    b, stop = M._colour_range()
    assert np.all(np.diff(b) > 0) and stop < M.dwarf_table()["bp_rp"].size
    assert M.teff_from_bprp(float(b[-1]) + 0.01)[0] is None


def test_dwarf_table_is_the_cited_version():
    head = M.DWARF_TABLE.read_text(encoding="utf-8").splitlines()[:5]
    assert any("2022.04.16" in h for h in head) and any("Pecaut & Mamajek 2013" in h for h in head)


# ============================================================================ identification and dilution
def test_identification_propagates_proper_motion_to_the_position_epoch():
    # a star moving 1 arcsec/yr north: at 2016.0 it is 0.5" north of where it was at 2015.5
    row = _gaia_row(dec=20.0 + 0.5 / 3600, pmdec=1000.0)
    other = _gaia_row(source_id="2", ra=10.0 + 3 / 3600, phot_g_mean_mag=12.0)
    m = M.identify([row, other], 10.0, 20.0, position_epoch=2015.5)
    assert m["source_id"] == "1" and m["sep_arcsec"] < 0.01 and m["sep_unpropagated_arcsec"] == pytest.approx(0.5, abs=0.01)
    assert m["pm_shift_arcsec"] == pytest.approx(0.5) and not m["high_proper_motion"]
    assert m["next"]["source_id"] == "2" and m["next"]["delta_g"] == pytest.approx(12.0 - 9.67)
    fast = M.identify([_gaia_row(pmdec=5000.0)], 10.0, 20.0, position_epoch=2000.0)
    assert fast["high_proper_motion"]
    assert M.identify([_gaia_row()], 10.0, 20.0, position_epoch=None)["propagated_to"] is None
    assert M.julian_year("J2015.5") == 2015.5 and M.julian_year("unverified") is None


def test_dilution_census_names_neighbours_able_to_produce_the_depth():
    target = _gaia_row()
    bright = _gaia_row(source_id="b", ra=10.0 + 20 / 3600, phot_g_mean_mag=9.67 + 2.0)   # 16% of the target's flux
    faint = _gaia_row(source_id="f", ra=10.0 - 30 / 3600, phot_g_mean_mag=9.67 + 8.0)
    outside = _gaia_row(source_id="o", ra=10.0 + 90 / 3600, phot_g_mean_mag=5.0)
    no_g = _gaia_row(source_id="n", dec=20.0 + 10 / 3600, phot_g_mean_mag="")
    c = M.dilution_census([target, bright, faint, outside, no_g], "1", 9.67, ra=10.0, dec=20.0, aperture_arcsec=52.5,
                          depth_ppm=10000)
    assert c["n_neighbours"] == 2 and [n["source_id"] for n in c["neighbours"]] == ["b", "f"]
    b, f = c["neighbours"]
    assert b["could_mimic_depth"] and not f["could_mimic_depth"]
    assert b["max_depth_ppm_if_fully_eclipsed"] == pytest.approx(10 ** -0.8 / c["depth_dilution_factor"] * 1e6)
    assert c["neighbours_without_g"][0]["source_id"] == "n"
    assert M.dilution_census([], "1", None, ra=0, dec=0, aperture_arcsec=1, depth_ppm=1)["computed"] is False


# ============================================================================ durations and aliases
def test_transit_duration_matches_the_earth_sun_case():
    T = M.transit_duration_days(np.array([365.25]), np.array([M.RHO_SUN]), np.array([0.0]), 0.00917)[0] * 24
    assert T == pytest.approx(13.0, abs=0.3)            # Earth's central transit of the Sun lasts about 13 h


def test_duration_likelihood_favours_the_alias_that_matches_the_stellar_density():
    true_p = 10.0
    dur_h = float(M.transit_duration_days(np.array([true_p]), np.array([M.RHO_SUN]), np.array([0.3]), 0.1)[0] * 24)
    rows = M.alias_duration_likelihood([40.0, 20.0, true_p, 5.0, 2.5], dur_h, 0.1 * dur_h, 1.0, 0.1, seed=1)
    w = {r["period_days"]: r["weight_likelihood_only"] for r in rows}
    assert max(w, key=w.get) in (true_p, 20.0) and w[2.5] < 0.05 and w[40.0] < w[true_p]
    assert sum(w.values()) == pytest.approx(1.0)
    assert sum(r["weight_with_transit_probability"] for r in rows) == pytest.approx(1.0)
    assert rows[0]["predicted_duration_h_16_84"][0] < rows[0]["predicted_duration_h_median"]


def test_alias_depths_in_an_independent_sparse_series():
    rng = np.random.default_rng(4)
    t0, p_true, dur = 2459000.0, 7.0, 0.12
    t = np.sort(rng.uniform(t0 - 400, t0 + 400, 6000))            # a ZTF-like irregular series
    y = 1 + rng.normal(0, 0.003, t.size)
    ph = ((t - t0 + p_true / 2) % p_true) - p_true / 2
    y[np.abs(ph) < dur / 2] *= 1 - 0.01
    rows = {r["period_days"]: r for r in M.alias_depths_in_series(t, y, t0=t0, periods=[p_true, 3.5, 14.0 / 3], dur_d=dur,
                                                                 ref_depth_ppm=10000)}
    assert rows[p_true]["verdict"] == "supported" and rows[p_true]["depth_ppm"] == pytest.approx(10000, rel=0.3)
    assert rows[14.0 / 3]["verdict"] == "excluded"
    sparse = M.alias_depths_in_series(t[:3], y[:3], t0=t0, periods=[p_true], dur_d=dur, ref_depth_ppm=10000)
    assert sparse == [] or sparse[0]["verdict"] == "untested"


# ============================================================================ per-event census
def _series(n=2000, cad=120 / 86400):
    t = 2459000.0 + np.arange(n) * cad
    return t, np.zeros(n, int), {k: np.random.default_rng(i).normal(0, 0.01, n) + 100
                                 for i, k in enumerate(("MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2", "SAP_BKG"))}


def test_event_census_is_clean_on_flat_engineering_data():
    t, q, s = _series()
    r = M.event_census(t, q, s, t_mid=float(t[1000]), dur_d=0.1)
    assert r["clean"] and r["tested_series"] == sorted(s) and r["quality_bits_near"] == {}


def test_event_census_flags_a_centroid_shift_and_a_momentum_dump():
    t, q, s = _series()
    mid = float(t[1000])
    s["MOM_CENTR1"][np.abs(t - mid) < 0.05] += 0.05
    r = M.event_census(t, q, s, t_mid=mid, dur_d=0.1)
    assert r["flagged_series"] == ["MOM_CENTR1"] and not r["clean"] and r["series"]["MOM_CENTR1"]["z"] > 5
    q[1010] = 32 | 1024
    r = M.event_census(t, q, _series()[2], t_mid=mid, dur_d=0.1)
    assert r["artifact_bits_near"] == ["momentum dump"] and r["quality_bits_near"]["collateral cosmic"] == 1
    assert r["suspect"] and r["artifact_bits_in_event"] == ["momentum dump"]
    q2 = np.zeros_like(q)
    q2[1000 + 144] = 16                                   # argabrightening 0.2 d away: inside the pad, not the event
    near = M.event_census(t, q2, _series()[2], t_mid=mid, dur_d=0.1)
    assert near["artifact_bits_near"] == ["argabrightening"] and near["artifact_bits_in_event"] == []
    assert not near["clean"] and not near["suspect"]      # a caution (inconclusive), not a failure
    few = M.event_census(t[:5], q[:5], {"SAP_BKG": s["SAP_BKG"][:5]}, t_mid=float(t[2]), dur_d=0.01)
    assert few["series"]["SAP_BKG"]["tested"] is False


# ============================================================================ moving objects and time
def test_bjd_to_utc_removes_light_time_and_the_tdb_offset():
    from astropy.time import Time

    iso = M.bjd_tdb_to_utc_iso(2459000.5, 10.0, 20.0)
    dt_s = (Time(2459000.5, format="jd", scale="tdb").utc - Time(iso, scale="utc")).sec   # both as UTC instants
    assert abs(dt_s) < 510                          # |light time to the barycentre| ≤ 8.3 min


def test_moving_object_brightness_cut():
    rows = [{"Name": "Bright", "V": "12.0", "centerdist": "40"}, {"Name": "Faint", "V": "22.0", "centerdist": "5"},
            {"Name": "NoMag", "V": "", "centerdist": "9"}]
    h = M.moving_object_hits(rows, target_mag=10.0, depth_ppm=2000)
    assert [x["name"] for x in h["bright_enough"]] == ["Bright"] and h["too_faint"] == 1
    assert h["unknown_brightness"][0]["name"] == "NoMag"


# ============================================================================ catalogue guards
@pytest.mark.parametrize("vtype, cls", [("EA", "eclipsing"), ("EW|BY", "eclipsing"), ("EP", "transit"), ("ELL", "ellipsoidal"),
                                        ("BY", "other_variable"), ("", "unclassified"), ("EA:", "eclipsing")])
def test_vsx_types(vtype, cls):
    assert M.vsx_classify(vtype) == cls


def test_vsx_guard_states():
    at = {"Name": "V1", "RAJ2000": 10.0, "DEJ2000": 20.0}
    assert M.vsx_guard([{**at, "Type": "EA", "Period": "2.5"}], 10.0, 20.0, match_arcsec=10)["state"] == "failed"
    assert M.vsx_guard([{**at, "Type": "EP", "Period": "2.5"}], 10.0, 20.0, match_arcsec=10)["state"] == "passed"
    rot = M.vsx_guard([{**at, "Type": "ROT", "Period": "5.0"}], 10.0, 20.0, match_arcsec=10, periods=[10.02])
    assert rot["state"] == "inconclusive" and rot["entries"][0]["period_collisions"][0]["ratio"] == 2.0
    far = {"Name": "V2", "RAJ2000": 10.01, "DEJ2000": 20.0, "Type": "EA"}
    assert M.vsx_guard([far], 10.0, 20.0, match_arcsec=10)["state"] == "passed"


@pytest.mark.parametrize("otype, state", [("EB*", "failed"), ("G", "failed"), ("RG*", "inconclusive"), ("**", "inconclusive"),
                                          ("PM*", "passed"), ("*", "passed")])
def test_simbad_guard_states(otype, state):
    rows = [{"main_id": "X", "otype": otype, "ra": 10.0, "dec": 20.0}]
    assert M.simbad_guard(rows, 10.0, 20.0, match_arcsec=5)["state"] == state
    assert M.simbad_guard([], 10.0, 20.0, match_arcsec=5)["state"] == "inconclusive"


# ============================================================================ RVs
def test_mass_function_inversion_recovers_jupiter():
    f = M.mass_function_msun(4332.6, 12.47)                     # Jupiter's reflex on the Sun
    assert M.companion_min_mass_msun(f, 1.0) / M.MJUP_MSUN == pytest.approx(1.0, abs=0.02)
    m = M.companion_min_mass_msun(0.028, 1.0)
    assert m ** 3 / (1 + m) ** 2 == pytest.approx(0.028, rel=1e-6)
    assert M.companion_min_mass_msun(0.0, 1.0) == 0.0


def test_rv_bounds_exclude_a_stellar_companion_only_when_the_data_allow():
    rng = np.random.default_rng(2)
    t = np.sort(rng.uniform(0, 60, 25))
    quiet = rng.normal(0, 3.0, t.size)
    b = M.rv_companion_bounds(t, quiet, np.full(t.size, 3.0), [3.0, 10.0], m1_msun=1.0)
    assert all(x["m2_upper_msun"] < 0.08 for x in b)
    binary = 20000 * np.sin(2 * np.pi * t / 10.0) + quiet
    b2 = M.rv_companion_bounds(t, binary, np.full(t.size, 3.0), [10.0], m1_msun=1.0)[0]
    assert b2["K"] == pytest.approx(20000, rel=0.01) and b2["m2_upper_msun"] > 0.08


def test_read_rv_reads_stated_units_and_refuses_guesses(tmp_path):
    from cygnus.multi.readers import ReaderError, read_rv

    p = tmp_path / "rv.csv"
    p.write_text("bjd,rv_kms,err_kms\n2459000.1,1.5,0.002\n2459001.1,1.6,0.002\n", encoding="utf-8")
    rv = read_rv(p, fmt="rv_table")
    assert rv["rv_ms"] == [1500.0, 1600.0] and rv["err_ms"] == [2.0, 2.0]
    bad = tmp_path / "bad.csv"
    bad.write_text("time,rv\n1,2\n", encoding="utf-8")
    with pytest.raises(ReaderError, match="stated units"):
        read_rv(bad, fmt="rv_table")
    h = fits.PrimaryHDU()
    h.header["HIERARCH ESO QC CCF RV"] = 12.5
    h.header["HIERARCH ESO QC CCF RV ERROR"] = 0.001
    h.header["HIERARCH ESO QC BJD"] = 2459100.5
    h.writeto(tmp_path / "esp.fits")
    rv = read_rv(tmp_path / "esp.fits", fmt="eso_spectrum")
    assert rv["rv_ms"] == [12500.0] and rv["bjd"] == [2459100.5]
    fits.PrimaryHDU().writeto(tmp_path / "none.fits")
    with pytest.raises(ReaderError, match="no ESO pipeline RV keywords"):
        read_rv(tmp_path / "none.fits", fmt="eso_spectrum")


# ============================================================================ images
def test_read_image_carries_its_wcs_and_calibrated_photometry(tmp_path):
    from astropy.wcs import WCS

    from cygnus.multi.readers import read_image

    w = WCS(naxis=2)
    w.wcs.crpix, w.wcs.cdelt, w.wcs.crval, w.wcs.ctype = [25, 25], [-1 / 3600, 1 / 3600], [10.0, 20.0], ["RA---TAN", "DEC--TAN"]
    yy, xx = np.indices((50, 50))
    img = 1.0 + 100.0 * np.exp(-((xx - 24) ** 2 + (yy - 24) ** 2) / 4.0)
    hdr = w.to_header()
    hdr["BUNIT"] = "nanomaggy"
    fits.PrimaryHDU(img, header=hdr).writeto(tmp_path / "ls.fits")
    im = read_image(tmp_path / "ls.fits")
    x, y = im["wcs"].world_to_pixel_values(10.0, 20.0)
    assert (float(x), float(y)) == pytest.approx((24.0, 24.0), abs=1e-6)
    zp, note = M.image_zeropoint(im["header"])
    assert zp == 22.5 and "nanomaggies" in note
    ph = M.aperture_photometry(im["data"], float(x), float(y), 6, 10, 15)
    assert ph["measured"] and ph["flux"] == pytest.approx(100 * math.pi * 4.0, rel=0.02)
    fits.PrimaryHDU(img).writeto(tmp_path / "plain.fits")
    assert read_image(tmp_path / "plain.fits")["wcs"] is None
    assert M.image_zeropoint(fits.Header())[0] is None


# ============================================================================ the steps, end to end
class _FakeAdapter:
    def __init__(self, rows=None, error=None):
        self.rows, self.error, self.calls = rows or [], error, []

    def discover(self, target, **opts):
        from cygnus.multi.archives.base import AdapterUnavailable, ProductRef

        self.calls.append(opts)
        if self.error:
            raise AdapterUnavailable(self.error)
        return [ProductRef(archive="fake", product_id="x.csv", format="csv", kind="table",
                           extra={"rows": self.rows, "inline": True})]


@pytest.fixture()
def fakes(monkeypatch):
    from cygnus.multi.archives import base

    table: dict[str, _FakeAdapter] = {}
    real = base.get
    monkeypatch.setattr(base, "get", lambda name, **kw: table[name] if name in table else real(name, **kw))
    return table


PID = "tess-fixture-s0007-0000000000000001-s_lc.fits"
TARGET = {"name": "TOI-9.01", "tic": 1, "ra_deg": 10.0, "dec_deg": 20.0, "t0_bjd": 2458505.0, "period_days": None,
          "depth_ppm": 30000.0, "duration_h": 2.88, "tmag": 9.0, "position_source": "fixture", "disposition": "PC"}


def _lc_with_engineering(path: Path, *, shift_at: float | None = None):
    rng = np.random.default_rng(1)
    n = 9000
    t = 1500.0 + np.arange(n) * (120 / 86400)
    flux = 1000.0 * (1 + rng.normal(0, 0.001, n))
    for c in (1505.0, 1511.0):                          # the catalogued transit and a repeat 6 d later
        flux[np.abs(t - c) < 0.06] *= 0.97
    cols = {"TIME": t, "SAP_FLUX": flux * 1.01, "PDCSAP_FLUX": flux}
    for i, k in enumerate(("MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2", "SAP_BKG")):
        cols[k] = 100 + np.random.default_rng(10 + i).normal(0, 0.01, n)
    if shift_at is not None:
        cols["MOM_CENTR1"][np.abs(t - shift_at) < 0.06] += 0.05
    hdu0 = fits.PrimaryHDU()
    hdu0.header.update({"OBJECT": "TIC 1", "TICID": 1, "SECTOR": 7, "TIMEDEL": 120 / 86400, "RA_OBJ": 10.0, "DEC_OBJ": 20.0})
    tab = fits.BinTableHDU.from_columns([fits.Column(name=k, format="D", array=v) for k, v in cols.items()]
                                        + [fits.Column(name="QUALITY", format="J", array=np.zeros(n, int))])
    tab.header.update({"BJDREFI": 2457000, "BJDREFF": 0.0, "TIMESYS": "TDB", "TIMEUNIT": "d"})
    path.parent.mkdir(parents=True, exist_ok=True)
    fits.HDUList([hdu0, tab]).writeto(path, overwrite=True)


def _run_known_object(tmp_path, monkeypatch, *, shift_at=None):
    from cygnus import priorart
    from cygnus.multi import scaffold, steps
    from cygnus.multi.runner import run

    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    (tmp_path / "campaigns").mkdir(exist_ok=True)
    spec = scaffold.write_spec(tmp_path, dict(TARGET, epoch="J2015.5"), parent="q", origin="fixture", seed=5)
    _lc_with_engineering(tmp_path / "scratch" / "campaign_toi-9-01" / PID, shift_at=shift_at)
    monkeypatch.setattr(steps, "_discover_spoc_lcs", lambda tic, n, t0=None: [
        {"product_id": PID, "tic": tic, "sector": 7, "covers_known_epoch": True}])
    monkeypatch.setattr(priorart, "catalogue_audit", lambda ra, dec, **kw: {
        "TESS_TOI": {"state": "done", "result": "1 match", "query": "q", "retrieved_utc": "2026-01-01T00:00:00Z", "matches": []}})
    led = Ledger(tmp_path / "l.sqlite")
    try:
        run(spec, ledger=led, root=tmp_path, echo=lambda *_: None)
        assert all(r["status"] == "completed" for r in led.runs())
    finally:
        led.close()
    out = tmp_path / "campaigns" / "toi-9-01"
    rec = json.loads((out / "sky_record.json").read_text(encoding="utf-8"))
    return out, {c["name"]: c for c in rec["checks"]}, rec


def _gaia_field(g_neighbour=11.0):
    # the TOI position is J2015.5; the Gaia star (2016.0) has moved 0.3" north since then
    return [_gaia_row(dec=20.0 + 0.3 / 3600, pmdec=600.0, phot_g_mean_mag=9.67),
            _gaia_row(source_id="2", ra=10.0 + 25 / 3600, phot_g_mean_mag=g_neighbour, bp_rp=1.5, parallax=1.0)]


def test_measure_steps_on_a_known_object_with_a_repeat(tmp_path, monkeypatch, fakes):
    fakes["gaia"] = _FakeAdapter(_gaia_field())
    fakes["vizier"] = _FakeAdapter([{"Name": "V9", "Type": "ROT", "Period": "3.0", "RAJ2000": 10.0, "DEJ2000": 20.0}])
    fakes["simbad"] = _FakeAdapter([{"main_id": "TYC 1", "otype": "PM*", "ra": 10.0, "dec": 20.0}])
    fakes["skybot"] = _FakeAdapter([{"Name": "(9) Metis", "V": "11.5", "centerdist": "300"}])
    out, checks, rec = _run_known_object(tmp_path, monkeypatch)
    assert rec["outcome"] == "lead" and rec["evidence"] == "Unverified lead"       # nothing raises it further
    assert checks["Target-to-Gaia identification (proper motion propagated)"]["state"] == "passed"
    assert "propagated 2016.0 → J2015.5" in checks["Target-to-Gaia identification (proper motion propagated)"]["note"]
    assert checks["Stellar priors (Gaia colour and parallax)"]["state"] == "passed"
    # the 11th-mag neighbour holds ~25% of the target's flux: it could produce a 3% dip alone
    assert checks["Blend and dilution census (Gaia DR3 cone)"]["state"] == "inconclusive"
    sc = json.loads((out / "stellar_context.json").read_text(encoding="utf-8"))["TOI-9.01"]
    assert sc["match"]["sep_arcsec"] < 0.05 and sc["dilution"]["n_could_mimic"] == 1
    # the duration likelihood rides on the period aliases
    pa = json.loads((out / "period_aliases.json").read_text(encoding="utf-8"))["candidates"][0]
    dl = pa["duration_likelihood"]
    assert [a["period_days"] for a in dl["aliases"]] == pytest.approx([a["period_days"] for a in pa["aliases"]
                                                                        if a["verdict"] == "allowed"])
    assert "circular orbit" in dl["assumptions"] and "duration likelihood" in checks["Period aliases (repeat events)"]["note"]
    # the repeat event at 1511 is persistent: census clean, a bright asteroid at its epoch fails the moving-object check
    assert checks["Pointing and quality census per event"]["state"] == "passed"
    assert checks["Moving objects at screen-event epochs"]["state"] == "failed"
    mo = json.loads((out / "moving_objects.json").read_text(encoding="utf-8"))
    assert mo[0]["bright_enough"][0]["name"] == "(9) Metis" and mo[0]["utc"].startswith("2019-01-")
    assert fakes["skybot"].calls[0]["radius_arcsec"] == 600.0
    # a rotational variable whose 3-d period is half the 6-d alias: inconclusive, not failed
    assert checks["Variable-catalogue collision (VSX)"]["state"] == "inconclusive"
    assert checks["Object-class guard (SIMBAD)"]["state"] == "passed"
    assert checks["Independent repetition (other MAST collections)"]["state"] == "not_tested"
    assert checks["Independent-epoch confirmation (ZTF)"]["state"] == "not_tested"


def test_measure_steps_report_outages_as_not_tested_and_flag_a_centroid_shift(tmp_path, monkeypatch, fakes):
    for name in ("gaia", "vizier", "simbad", "skybot"):
        fakes[name] = _FakeAdapter(error="HTTP 503")
    out, checks, _ = _run_known_object(tmp_path, monkeypatch, shift_at=1511.0)
    for c in ("Target-to-Gaia identification (proper motion propagated)", "Stellar priors (Gaia colour and parallax)",
              "Blend and dilution census (Gaia DR3 cone)", "Variable-catalogue collision (VSX)", "Object-class guard (SIMBAD)",
              "Moving objects at screen-event epochs"):
        assert checks[c]["state"] == "not_tested", c
        assert "503" in checks[c]["note"] or "not answered" in checks[c]["note"], c
    assert "duration_likelihood" not in json.loads((out / "period_aliases.json").read_text(encoding="utf-8"))["candidates"][0]
    assert checks["Pointing and quality census per event"]["state"] == "failed"
    assert "MOM_CENTR1" in checks["Pointing and quality census per event"]["note"]


def test_alias_cross_instrument_uses_a_ztf_series(tmp_path, scratch_env, fakes):
    from cygnus.multi.measure_steps import step_alias_cross_instrument

    rng = np.random.default_rng(6)
    t0, dur = 2458505.0, 0.12
    t = np.sort(rng.uniform(t0 - 500, t0 + 500, 8000))
    mag = 12 + rng.normal(0, 0.003, t.size)
    ph = ((t - t0 + 3.0) % 6.0) - 3.0
    mag[np.abs(ph) < dur / 2] += 0.033                           # a 3% dimming every 6 d
    vot = scratch_env / "ztf.csv"
    with vot.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["TIME", "MAG", "QUALITY"])
        w.writerows([[f"{a - 2457000:.6f}", f"{b:.5f}", 0] for a, b in zip(t, mag)])
    ctx = make_ctx(tmp_path, spec={"targets": [dict(TARGET)]}, results={
        "fetch_products": {"products": {"ztf.csv": {**product_entry(vot, archive="IRSA", fmt="csv_lc", sector=None),
                                                    "product_id": "ztf.csv"}}},
        "period_aliases": {"candidates": [{"product": PID, "event_bjd": t0 + 6.0, "reference_depth_ppm": 30000,
                                           "allowed_periods_days": [6.0, 3.0, 2.0]}]}})
    (ctx.outdir / "period_aliases.json").write_text(json.dumps({"reference_epoch_bjd": t0}), encoding="utf-8")
    res = step_alias_cross_instrument(ctx, {})
    [r] = res["results"]
    v = {a["period_days"]: a["verdict"] for a in r["aliases"]}
    assert r["instrument"] == "IRSA:csv_lc" or r["instrument"] == "ZTF"
    assert v[6.0] == "supported" and v[2.0] == "excluded"


@pytest.fixture()
def scratch_env(tmp_path, monkeypatch):
    d = tmp_path / "scratch"
    d.mkdir()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(d))
    return d


def test_rv_bounds_step(tmp_path, scratch_env, fakes):
    from cygnus.multi.measure_steps import step_rv_bounds

    rng = np.random.default_rng(3)
    t = np.sort(rng.uniform(2459000, 2459100, 20))
    p = scratch_env / "rv.csv"
    p.write_text("bjd,rv_ms,err_ms\n" + "".join(f"{a},{b},3.0\n" for a, b in zip(t, rng.normal(0, 3, t.size))),
                 encoding="utf-8")
    base = {"fetch_products": {"products": {"rv.csv": {**product_entry(p, archive="eso", fmt="rv_table", kind="table",
                                                                       sector=None)}}},
            "period_aliases": {"candidates": [{"allowed_periods_days": [6.0, 3.0]}]}}
    ctx = make_ctx(tmp_path, spec={"targets": [dict(TARGET)]}, results=base)
    assert step_rv_bounds(ctx, {})["n_rv"] == 20
    assert ctx.checks["Stellar-companion exclusion (archival RVs)"]["state"] == "not_tested"   # no primary mass
    ctx2 = make_ctx(tmp_path, spec={"targets": [dict(TARGET)]}, results=base)
    res = step_rv_bounds(ctx2, {"primary_mass_msun": 1.0})
    assert ctx2.checks["Stellar-companion exclusion (archival RVs)"]["state"] == "passed"
    assert all(b["m2_upper_msun"] < 0.08 for b in res["bounds"])


def test_spec_order_rules_for_the_measure_steps(tmp_path):
    from cygnus.multi.runner import SpecError, load_spec

    p = tmp_path / "x.yaml"
    p.write_text("schema: cygnus.campaign/1\ncampaign_id: x-y\noutputs: out/\nsteps:\n  - fetch_products: {}\n"
                 "  - calibrate_screen: {}\n  - known_signal_recovery: {}\n  - period_aliases: {}\n  - stellar_context: {}\n"
                 "  - event_census: {}\n  - residual_screen: {k_mad: calibrated}\n", encoding="utf-8")
    with pytest.raises(SpecError) as e:
        load_spec(p)
    assert "stellar_context must come before period_aliases" in str(e.value)
    assert "event_census must come after residual_screen" in str(e.value)


def test_generated_specs_carry_the_measure_steps(tmp_path):
    from cygnus.multi import scaffold
    from cygnus.multi.runner import load_spec

    (tmp_path / "campaigns").mkdir()
    spec = load_spec(scaffold.write_spec(tmp_path, dict(TARGET, epoch="J2015.5"), parent=None, origin="fixture", seed=1))
    order = [next(iter(s)) for s in spec["steps"]]
    for step in ("stellar_context", "event_census", "moving_objects", "alias_cross_instrument", "variability_guard"):
        assert step in order
    assert "rv_bounds" not in order
    spec2 = scaffold.spec_for(dict(TARGET, name="TOI-8.01"), parent=None, origin="f", seed=1, archives="mast,eso")
    assert "  - rv_bounds: {}" in spec2


def test_context_products_measures_calibrated_colours_on_a_band_cube(tmp_path, scratch_env):
    from astropy.wcs import WCS

    from cygnus.multi.steps import step_context_products

    w = WCS(naxis=2)
    w.wcs.crpix, w.wcs.cdelt, w.wcs.crval, w.wcs.ctype = [30, 30], [-0.262 / 3600, 0.262 / 3600], [10.0, 20.0], ["RA---TAN", "DEC--TAN"]
    yy, xx = np.indices((60, 60))
    psf = np.exp(-((xx - 29) ** 2 + (yy - 29) ** 2) / 8.0)
    cube = np.stack([0.01 + 100.0 * psf, 0.01 + 250.0 * psf])     # r is 2.5x brighter: g - r = +0.995
    hdr = w.to_header()
    hdr.update({"BUNIT": "nanomaggy", "BAND0": "g", "BAND1": "r"})
    p = scratch_env / "ls.fits"
    fits.PrimaryHDU(cube, header=hdr).writeto(p)
    ctx = make_ctx(tmp_path, spec={"targets": [dict(TARGET)]}, results={
        "fetch_products": {"products": {"ls.fits": product_entry(p, archive="legacysurvey", fmt="fits_image", kind="image",
                                                                 sector=None)}}})
    out = step_context_products(ctx, {"aperture_arcsec": 3.0})["products"]["ls.fits"]["photometry"]
    assert [b["band"] for b in out["bands"]] == ["g", "r"] and all(b["mag"] is not None for b in out["bands"])
    assert out["colours"]["g-r"] == pytest.approx(2.5 * math.log10(2.5), abs=0.01)
    assert out["pixel_scale_arcsec"] == pytest.approx(0.262, rel=1e-3)


def test_oversized_products_are_skipped_before_download(tmp_path, scratch_env, monkeypatch):
    from cygnus.multi import steps

    called = []
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", lambda *a, **k: called.append(a))
    ctx = make_ctx(tmp_path, spec={"input": {"products": [{"product_id": "big.fits", "size_bytes": 5_000_000_000,
                                                           "url": "https://example.invalid/big.fits"}]}})
    with pytest.raises(RuntimeError, match="no products"):
        steps.step_fetch_products(ctx, {"max_product_bytes": 100_000_000})
    assert not called and "skipped before download" in ctx.notes[0]


def test_generic_fits_reader_keeps_engineering_columns(tmp_path):
    from cygnus.multi.lightcurve import read_campaign_lc

    p = tmp_path / "k.fits"
    _lc_with_engineering(p)
    lc = read_campaign_lc(p, fmt="fits_table")
    assert set(lc.centroids) == {"MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2"}


def test_moving_objects_with_some_epochs_unanswered_is_inconclusive(tmp_path, fakes):
    from cygnus.multi.measure_steps import step_moving_objects

    answers = iter([[], None])

    class Flaky(_FakeAdapter):
        def discover(self, target, **opts):
            from cygnus.multi.archives.base import AdapterUnavailable

            a = next(answers)
            if a is None:
                raise AdapterUnavailable("SkyBoT failed: ValueError: No table found")
            return super().discover(target, **opts)

    fakes["skybot"] = Flaky([])
    ev = [{"mid_time_BJD_like": 2459000.5 + i, "persistent": True, "deepest_median_residual": -0.01} for i in range(2)]
    ctx = make_ctx(tmp_path, spec={"targets": [dict(TARGET)]}, results={"residual_screen": {"per_product": {"p": {
        "distinct_events_outside_veto": ev}}}})
    step_moving_objects(ctx, {})
    c = ctx.checks["Moving objects at screen-event epochs"]
    assert c["state"] == "inconclusive" and "1 epoch(s) not answered" in c["note"]

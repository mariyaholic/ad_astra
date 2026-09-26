"""Offline suite for ``cygnus.campaign.vet`` (docs/SUITE_EXPANSION.md §4.1 item 8).

Unit tests for the helpers not covered by tests/test_vet.py, then the ``vet()`` orchestrator on a
synthetic campaign: a *clean null* (on-target planted dip, flat engineering columns, flat
neighbours, on-target difference image) and one *planted contamination* per artifact check.

Every fixture is synthetic and seeded (numpy ``default_rng``); FITS files are written into
``tmp_path`` only. There is no network: socket connects raise, and every archive seam
(``requests``, ``astroquery.mast``, ``vet._mast_file``, ``vet.siblings``) is an in-memory fake.
"""

from __future__ import annotations

import csv
import json
import math
import shutil
import socket
import sys
import types
from pathlib import Path

import numpy as np
import pytest
from astropy.io import fits

from cygnus.campaign import vet

# ------------------------------------------------------------------ synthetic geometry
BJDREFI = 2457000
T_OFF = 1500.0                     # TIME column = BJD - BJDREFI (TESS BTJD-like)
CAD = 120 / 86400
SPAN = 13.0                        # days of data, with one gap
GAP = (9.4, 11.2)
REL_REF, REL_EV, REL_SEC, REL_FLAT, REL_GAP = 2.0, 8.0, 5.0, 12.2, 10.3
DUR = 3 / 24
DEPTH = 3000e-6
RA, DEC = 150.0, -30.0
TIC = 123456789
CID = "vetsynth"
SECTOR, CAMERA, CCD = 10, 1, 2
LC_NAME = f"tess2019000000000-s{SECTOR:04d}-{TIC:016d}-0000-s_lc.fits"
TP_NAME = LC_NAME.replace("_lc.fits", "_tp.fits")
STAMP = 11                         # TPF stamp is STAMP x STAMP, target at pixel (5, 5)
NB_XY = (9, 5)                     # contaminating neighbour star in the TPF (x, y)

EVENT_CHECKS = {                   # checks a significant dip with a reference, star and aliases reaches
    "Shape matches reference transit", "Sibling TOI ephemerides", "Detrending alternatives",
    "Red-noise significance", "Background / centroid / pointing", "Quality flags and coverage",
    "Gaia neighbours able to mimic the depth", "Difference-image centroid", "Common mode (same camera/CCD)",
    "Stellar-density duration limit", "Secondary eclipse (circular aliases)", "Error-weighted box fit",
}
ALL_CHECKS = EVENT_CHECKS | {"Box fit finds a dip", "Shape fit"}


def bjd(rel):
    return BJDREFI + T_OFF + rel


def rel_grid():
    rel = np.arange(0.0, SPAN, CAD)
    return rel[(rel < GAP[0]) | (rel > GAP[1])]


def inbox(rel, mid, dur=DUR):
    return np.abs(rel - mid) <= dur / 2


# ------------------------------------------------------------------ network guard and fakes
def _guard(mp):
    def refuse(*a, **k):
        raise RuntimeError("network access attempted in an offline test")

    mp.setattr(socket.socket, "connect", refuse)
    mp.setattr(socket, "create_connection", refuse)
    mp.setitem(sys.modules, "requests", _fake_requests(get=refuse, post=refuse))


@pytest.fixture(autouse=True)
def _no_network(monkeypatch):
    _guard(monkeypatch)


def _fake_requests(get=None, post=None):
    mod = types.ModuleType("requests")
    mod.get, mod.post = get, post
    return mod


class FakeResp:
    def __init__(self, content=b"", text="", status=200):
        self.content, self.text, self.status = content, text, status

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def raise_for_status(self):
        if self.status >= 400:
            raise RuntimeError(f"HTTP {self.status}")

    def iter_content(self, n):
        yield self.content[:5]
        yield self.content[5:]


# ------------------------------------------------------------------ synthetic products
def write_lc(path: Path, *, seed, tic=TIC, ra=RA, dec=DEC, tmag=10.0, camera=CAMERA, ccd=CCD,
             dips=((REL_REF, DEPTH), (REL_EV, DEPTH)), centroid_shift=0.0, quality=()):
    """A SPOC-like 120-s light curve (HDU1 table + primary header keys vet.LC reads)."""
    rng = np.random.default_rng(seed)
    rel = rel_grid()
    n = rel.size
    model = np.ones(n)
    for mid, d in dips:
        model -= d * inbox(rel, mid)
    pdc = 1e4 * (model + rng.normal(0, 3e-4, n))
    sap = 1.2e4 * (model + rng.normal(0, 3e-4, n)) * (1 + 5e-4 * np.sin(2 * np.pi * rel / 9.0))
    q = np.zeros(n, np.int32)
    for rel_t, bit in quality:
        q[np.argmin(np.abs(rel - rel_t))] |= bit
    cols = {"TIME": ("D", rel + T_OFF), "SAP_FLUX": ("E", sap), "PDCSAP_FLUX": ("E", pdc),
            "PDCSAP_FLUX_ERR": ("E", np.full(n, 3.0)), "SAP_BKG": ("E", 80 + rng.normal(0, 0.5, n)),
            "MOM_CENTR1": ("D", 512.3 + rng.normal(0, 1e-3, n) + centroid_shift * inbox(rel, REL_EV)),
            "MOM_CENTR2": ("D", 256.7 + rng.normal(0, 1e-3, n)),
            "POS_CORR1": ("E", rng.normal(0, 1e-3, n)), "POS_CORR2": ("E", rng.normal(0, 1e-3, n)),
            "QUALITY": ("J", q)}
    h1 = fits.BinTableHDU.from_columns([fits.Column(name=k, format=f, array=a) for k, (f, a) in cols.items()])
    h1.header["BJDREFI"], h1.header["BJDREFF"] = BJDREFI, 0.0
    h0 = fits.PrimaryHDU()
    for k, v in dict(SECTOR=SECTOR, CAMERA=camera, CCD=ccd, RA_OBJ=ra, DEC_OBJ=dec, TESSMAG=tmag, TICID=tic).items():
        h0.header[k] = v
    fits.HDUList([h0, h1]).writeto(path, overwrite=True)
    return path


def write_tpf(path: Path, *, seed, dip_on="target"):
    """A SPOC-like target pixel file: target PSF at (5, 5), a fainter star at NB_XY; the planted
    dips (reference and event epochs) are on the target or on the neighbour. HDU2 carries the
    aperture (bit 2 = optimal, 3x3 around the target) and a TAN WCS centred on the target."""
    rng = np.random.default_rng(seed)
    rel = rel_grid()
    n = rel.size
    yy, xx = np.mgrid[0:STAMP, 0:STAMP]

    def psf(x0, y0):
        return np.exp(-((xx - x0) ** 2 + (yy - y0) ** 2) / (2 * 0.9 ** 2))

    ft, fn = np.ones(n), np.ones(n)
    for mid in (REL_REF, REL_EV):
        if dip_on == "target":
            ft -= DEPTH * inbox(rel, mid)
        else:
            fn -= 0.03 * inbox(rel, mid)
    flux = (ft[:, None, None] * 5000 * psf(5, 5) + fn[:, None, None] * 2000 * psf(*NB_XY)
            + 50 + rng.normal(0, 2.0, (n, STAMP, STAMP)))
    h1 = fits.BinTableHDU.from_columns([
        fits.Column(name="TIME", format="D", array=rel + T_OFF),
        fits.Column(name="FLUX", format=f"{STAMP * STAMP}E", dim=f"({STAMP},{STAMP})", array=flux.astype(np.float32)),
        fits.Column(name="QUALITY", format="J", array=np.zeros(n, np.int32))])
    h1.header["BJDREFI"], h1.header["BJDREFF"] = BJDREFI, 0.0
    ap = np.ones((STAMP, STAMP), np.int32)
    ap[4:7, 4:7] |= 2
    h2 = fits.ImageHDU(ap)
    for k, v in dict(CTYPE1="RA---TAN", CTYPE2="DEC--TAN", CRPIX1=6.0, CRPIX2=6.0, CRVAL1=RA, CRVAL2=DEC,
                     CDELT1=-21 / 3600, CDELT2=21 / 3600, CUNIT1="deg", CUNIT2="deg").items():
        h2.header[k] = v
    fits.HDUList([fits.PrimaryHDU(), h1, h2]).writeto(path, overwrite=True)
    return path


def write_gaia(root: Path, rows):
    f = root / "design-system" / "mockups" / "data" / f"field_{CID}.csv"
    f.parent.mkdir(parents=True, exist_ok=True)
    with f.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["source_id", "ra", "dec", "g"])
        w.writeheader()
        w.writerows(rows)
    return f


def gaia_row(sid, dra_arcsec, ddec_arcsec, g):
    return {"source_id": sid, "ra": RA + dra_arcsec / 3600 / math.cos(math.radians(DEC)),
            "dec": DEC + ddec_arcsec / 3600, "g": g}


GAIA_CLEAN = [gaia_row("1", 0.2, 0.1, 10.0),      # the target
              gaia_row("2", 30.0, 0.0, 17.0),     # inside 52.5", too faint for 3000 ppm (dG 7 > 6.31)
              gaia_row("3", 0.0, 80.0, 11.0),     # bright but outside 2.5 TESS pixels
              {"source_id": "4", "ra": RA, "dec": DEC, "g": ""}]   # no G: ignored


class SimpleLC:
    """Duck-typed vet.LC (t in days, normalised fluxes, all cadences good unless flagged)."""

    def __init__(self, rel, cols, q=None):
        self.t = np.asarray(rel, float)
        self.q = np.zeros(self.t.size, int) if q is None else np.asarray(q, int)
        self.col = cols
        self.ok = np.isfinite(self.t) & (self.q == 0)


def simple_lc(seed=0, dips=((REL_EV, DEPTH),), rel=None):
    rng = np.random.default_rng(seed)
    rel = rel_grid() if rel is None else rel
    model = np.ones(rel.size)
    for mid, d in dips:
        model -= d * inbox(rel, mid)
    return SimpleLC(rel, {"PDCSAP_FLUX": model + rng.normal(0, 3e-4, rel.size),
                          "SAP_FLUX": model * (1 + 5e-4 * np.sin(rel / 2)) + rng.normal(0, 3e-4, rel.size)})


# ------------------------------------------------------------------ unit: small helpers
def test_f_parses_finite_numbers_only():
    assert vet._f("1.5") == 1.5 and vet._f(3) == 3.0 and vet._f(" -2e3 ") == -2000.0
    for bad in (None, "", "abc", "nan", "inf", float("nan"), [1]):
        assert vet._f(bad) is None


def test_shift_measures_in_box_offset_and_refuses_thin_data():
    rel = np.arange(0, 3, CAD)
    y = 5.0 + 0.01 * (rel - 1.5) ** 2 - 0.2 * inbox(rel, 1.5)
    ok = np.ones(rel.size, bool)
    assert vet._shift(rel, y, ok, 1.5, DUR, 0.7) == pytest.approx(-0.2, abs=1e-6)
    assert vet._shift(rel, y, ok, 1.5, 0.002, 0.7) is None            # < 3 cadences in the box
    thin = ok & (inbox(rel, 1.5) | (np.abs(rel - 1.5) > 0.69))          # < 20 baseline cadences
    assert vet._shift(rel, y, thin, 1.5, DUR, 0.7) is None
    y2 = y.copy()
    y2[100] = np.nan                                                    # non-finite values are skipped
    assert vet._shift(rel, y2, ok, 1.5, DUR, 0.7) == pytest.approx(-0.2, abs=1e-6)


def test_alt_depths_all_twelve_detrendings_bracket_the_planted_depth():
    lc = simple_lc(seed=3)
    alts, rng_ = vet.alt_depths(lc, REL_EV, DUR, 0.6625)
    expected = {f"{f} {m}" for f in ("PDCSAP", "SAP") for m in ("poly1", "poly2", "poly3", "median 0.5 d", "median 1 d", "median 2 d")}
    assert set(alts) == expected
    for k, v in alts.items():
        assert v == pytest.approx(3000, abs=200), k
    lo, hi = rng_
    assert lo == min(v for k, v in alts.items() if k.startswith("PDCSAP"))
    assert hi == max(v for k, v in alts.items() if k.startswith("PDCSAP"))


def test_alt_depths_event_in_a_gap_gives_no_range():
    alts, rng_ = vet.alt_depths(simple_lc(seed=3), REL_GAP, DUR, 0.6625)
    assert alts == {} and rng_ is None


def test_empirical_scores_a_planted_dip_against_random_epochs():
    lc = simple_lc(seed=5)
    rng = np.random.default_rng(9)
    flat = 1.0 + rng.normal(0, 3e-4, lc.t.size)
    bump = flat + 5e-3 * inbox(lc.t, REL_EV)
    series = {"PDCSAP": lc.col["PDCSAP_FLUX"], "flat": flat, "bump": bump}
    out = vet.empirical(lc, series, REL_EV, DUR, 0.6625, [REL_EV], n=200, seed=1)
    assert out["PDCSAP"]["n_random"] == 200
    assert out["PDCSAP"]["event"] == pytest.approx(-DEPTH, abs=2e-4)
    assert out["PDCSAP"]["z"] < -30 and out["PDCSAP"]["fraction_random_as_extreme"] == 0.0
    assert abs(out["flat"]["z"]) < 3 and out["flat"]["fraction_random_as_extreme"] > 0.01
    assert out["bump"]["z"] > 30                                        # sign preserved (a rise is +z)
    again = vet.empirical(lc, series, REL_EV, DUR, 0.6625, [REL_EV], n=200, seed=1)
    assert again == out                                                 # seeded: reproducible


def test_empirical_too_short_for_random_epochs_reports_no_z():
    rel = np.arange(7.0, 9.0, CAD)
    lc = simple_lc(seed=1, rel=rel)
    out = vet.empirical(lc, {"PDCSAP": lc.col["PDCSAP_FLUX"]}, REL_EV, DUR, 0.6625, [REL_EV], n=50)
    assert out["PDCSAP"]["z"] is None and out["PDCSAP"]["n_random"] == 0
    assert out["PDCSAP"]["event"] == pytest.approx(-DEPTH, abs=3e-4)


def test_quality_near_counts_flags_in_the_pad_and_the_nearest_momentum_dump():
    rel = rel_grid()
    q = np.zeros(rel.size, int)
    idx = lambda x: int(np.argmin(np.abs(rel - x)))
    q[idx(REL_EV + 0.01)] |= 32                  # momentum dump in the box
    q[idx(REL_EV + 0.30)] |= 2048 | 1024         # scattered light + collateral cosmic in the pad
    q[idx(REL_EV + 2.00)] |= 128                 # outside the pad: not counted
    q[idx(REL_EV - 1.00)] |= 32                  # a second, farther dump
    lc = SimpleLC(rel, {}, q)
    r = vet.quality_near(lc, REL_EV, DUR)
    assert r["flags_within_pad"] == {"momentum dump": 1, "scattered light": 1, "collateral cosmic": 1}
    assert r["nearest_momentum_dump_h"] == pytest.approx(0.24, abs=0.04)
    assert r["expected_in_box"] == 90 and r["usable_in_box"] == int(inbox(rel, REL_EV).sum()) - 1
    assert vet.quality_near(SimpleLC(rel, {}), REL_EV, DUR)["nearest_momentum_dump_h"] is None


# ------------------------------------------------------------------ unit: catalogue seams
def test_tap_and_siblings_post_adql_and_parse_csv(monkeypatch):
    seen = {}

    def post(url, data, timeout):
        seen.update(url=url, data=data, timeout=timeout)
        return FakeResp(text="toi,tid,pl_orbper\n1234.01,99,3.5\n1234.02,99,\n")

    monkeypatch.setitem(sys.modules, "requests", _fake_requests(post=post))
    rows, q = vet.siblings(99)
    assert rows == [{"toi": "1234.01", "tid": "99", "pl_orbper": "3.5"}, {"toi": "1234.02", "tid": "99", "pl_orbper": ""}]
    assert seen["url"] == vet.EXO_TAP and seen["data"]["QUERY"] == q
    assert seen["data"]["LANG"] == "ADQL" and seen["data"]["FORMAT"] == "csv" and seen["data"]["REQUEST"] == "doQuery"
    assert "FROM toi WHERE tid = 99" in q and "st_logg" in q
    monkeypatch.setitem(sys.modules, "requests", _fake_requests(post=lambda url, data, timeout: FakeResp(status=503)))
    with pytest.raises(RuntimeError, match="503"):
        vet.tap("SELECT 1")


def test_gaia_neighbours_missing_field_and_unidentified_target(tmp_path):
    r = vet.gaia_neighbours(tmp_path, CID, RA, DEC, 3000)
    assert r["state"] == "not_tested" and f"field_{CID}.csv" in r["note"]
    write_gaia(tmp_path, [gaia_row("9", 10.0, 0.0, 10.0)])            # nearest source 10" away
    assert vet.gaia_neighbours(tmp_path, CID, RA, DEC, 3000)["state"] == "inconclusive"


def test_gaia_neighbours_depth_cap_and_radius(tmp_path):
    write_gaia(tmp_path, GAIA_CLEAN + [gaia_row("5", 0.0, 20.0, 12.0)])
    r = vet.gaia_neighbours(tmp_path, CID, RA, DEC, 3000)
    assert r["state"] == "done" and r["target_gaia"] == "1" and r["target_g"] == 10.0
    assert r["radius_arcsec"] == pytest.approx(52.5)
    assert r["max_delta_g_for_depth"] == pytest.approx(-2.5 * math.log10(3000e-6), abs=0.01)
    assert [n["source_id"] for n in r["neighbours"]] == ["5", "2"]    # sorted by separation; "3" outside
    assert r["neighbours"][0]["sep_arcsec"] == pytest.approx(20.0, abs=0.1) and r["neighbours"][0]["delta_g"] == 2.0
    assert [c["source_id"] for c in r["capable"]] == ["5"]
    shallow = vet.gaia_neighbours(tmp_path, CID, RA, DEC, 1e6)       # 100% depth: nothing fainter can do it
    assert shallow["max_delta_g_for_depth"] == 0.0 and shallow["capable"] == []


# ------------------------------------------------------------------ unit: pixels
def test_mast_file_and_tpf_for_stream_to_scratch_and_cache(monkeypatch, tmp_path):
    got = []

    def get(url, stream, timeout):
        got.append(url)
        return FakeResp(content=b"SIMPLE-synthetic-bytes")

    monkeypatch.setitem(sys.modules, "requests", _fake_requests(get=get))
    p = vet.tpf_for(LC_NAME, tmp_path)
    assert p == tmp_path / "tpf" / TP_NAME and p.read_bytes() == b"SIMPLE-synthetic-bytes"
    assert got == ["https://mast.stsci.edu/api/v0.1/Download/file?uri=mast:TESS/product/" + TP_NAME]
    assert not list((tmp_path / "tpf").glob("*.part"))
    assert vet.tpf_for(LC_NAME, tmp_path) == p and len(got) == 1     # cached: no second request
    monkeypatch.setitem(sys.modules, "requests", _fake_requests(get=lambda url, stream, timeout: FakeResp(status=404)))
    with pytest.raises(RuntimeError, match="404"):
        vet._mast_file("mast:TESS/product/x_tp.fits", tmp_path / "tpf" / "x_tp.fits")
    assert not (tmp_path / "tpf" / "x_tp.fits").exists()


@pytest.fixture(scope="module")
def tpfs(tmp_path_factory):
    d = tmp_path_factory.mktemp("tpf")
    return {"target": write_tpf(d / "target_tp.fits", seed=11), "neighbour": write_tpf(d / "nb_tp.fits", seed=11, dip_on="neighbour")}


def test_difference_image_on_target_signal(tpfs):
    evs = [("E", bjd(REL_EV), DUR), ("GAP", bjd(REL_GAP), DUR)]
    r = vet.difference_image(tpfs["target"], RA, DEC, evs, n_boot=60)
    assert r["target_pixel_xy"] == pytest.approx([5.0, 5.0], abs=1e-6)
    assert r["stamp_shape"] == [STAMP, STAMP] and r["optimal_aperture_pixels"] == 9
    assert np.array(r["aperture"]).sum() == 9
    assert r["events"]["GAP"]["state"] == "not_tested" and "0 in-transit" in r["events"]["GAP"]["note"]
    e = r["events"]["E"]
    assert e["state"] == "done" and e["peak_pixel"] == [5, 5]
    assert e["diff_centroid_xy"] == pytest.approx([5.0, 5.0], abs=0.15)
    assert e["offset_from_oot_centroid_arcsec"] < 0.25 * vet.TESS_PIX_ARCSEC
    assert e["fraction_of_positive_difference_in_optimal_aperture"] > 0.6
    assert all(s is not None and s > 0 for s in e["bootstrap_sigma_pix"])
    assert np.array(e["image"]).shape == (STAMP, STAMP)


def test_difference_image_centroid_moves_to_the_neighbour_carrying_the_dip(tpfs):
    r = vet.difference_image(tpfs["neighbour"], RA, DEC, [("E", bjd(REL_EV), DUR)], n_boot=60)
    e = r["events"]["E"]
    assert e["peak_pixel"] == list(NB_XY)
    assert e["diff_centroid_xy"] == pytest.approx(list(NB_XY), abs=0.15)
    assert e["oot_centroid_xy"] == pytest.approx([5.0, 5.0], abs=0.1)     # the bright target out of transit
    assert e["offset_from_target_arcsec"] == pytest.approx(4 * vet.TESS_PIX_ARCSEC, abs=4)
    assert e["oot_offset_over_sigma"] >= 3 and e["offset_over_sigma"] >= 3
    assert e["fraction_of_positive_difference_in_optimal_aperture"] < 0.2


# ------------------------------------------------------------------ neighbour light curves
NB_TICS = {444: (0.30, 0.0, CCD), 555: (0.0, 0.50, CCD), 666: (-0.6, 0.2, CCD), 222: (0.1, 0.1, 3), 333: (0.2, 0.0, CCD)}


def nb_name(tic, fast=False):
    return f"tess2019000000000-s{SECTOR:04d}-{tic:016d}-0000-{'a_fast' if fast else 's'}_lc.fits"


def build_neighbours(d: Path, dipping=()):
    """Neighbour LC products and the (fake) MAST observation rows pointing at them."""
    registry, rows = {}, []
    for tic, (dra, ddec, ccd) in NB_TICS.items():
        fn = nb_name(tic)
        if tic != 333:   # 333: listed but its download fails
            registry[fn] = write_lc(d / fn, seed=tic, tic=tic, ra=RA + dra, dec=DEC + ddec, tmag=11.0, ccd=ccd,
                                    dips=((REL_EV, DEPTH),) if tic in dipping else ())
        rows.append({"target_name": str(tic), "s_ra": RA + dra, "s_dec": DEC + ddec, "dataURL": f"mast:TESS/product/{fn}"})
    rows += [{"target_name": str(TIC), "s_ra": RA, "s_dec": DEC, "dataURL": f"mast:TESS/product/{LC_NAME}"},   # the target
             {"target_name": "GAIA-EXT-1", "s_ra": RA, "s_dec": DEC, "dataURL": "mast:x/y_lc.fits"},        # not a TIC
             {"target_name": "777", "s_ra": RA + 0.05, "s_dec": DEC, "dataURL": f"mast:TESS/product/{nb_name(777, fast=True)}"},
             {"target_name": "888", "s_ra": RA + 0.06, "s_dec": DEC, "dataURL": ""}]                        # no product
    return registry, rows


def install_fakes(mp, registry, obs_rows, sibling_rows, *, outage=False):
    calls = {"mast": [], "obs": [], "siblings": []}

    def fake_mast_file(uri, dest):
        calls["mast"].append(uri)
        assert uri.startswith("mast:TESS/product/")
        name = uri.rsplit("/", 1)[-1]
        if name not in registry:
            raise OSError(f"synthetic download failure: {name}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(registry[name], dest)
        return dest

    class Observations:
        @staticmethod
        def query_criteria(**kw):
            calls["obs"].append(kw)
            if outage:
                raise ConnectionError("synthetic MAST outage")
            return [dict(r) for r in obs_rows]

    def fake_siblings(tic):
        calls["siblings"].append(tic)
        if outage:
            raise ConnectionError("synthetic TAP outage")
        return [dict(r) for r in sibling_rows], f"SELECT ... FROM toi WHERE tid = {int(tic)} ORDER BY toi"

    mod = types.ModuleType("astroquery.mast")
    mod.Observations = Observations
    mp.setitem(sys.modules, "astroquery.mast", mod)
    mp.setattr(vet, "_mast_file", fake_mast_file)
    mp.setattr(vet, "siblings", fake_siblings)
    return calls


def test_neighbour_lcs_filters_and_orders_same_ccd_products(monkeypatch, tmp_path):
    registry, rows = build_neighbours(tmp_path)
    calls = install_fakes(monkeypatch, registry, rows, [])
    out = vet.neighbour_lcs(RA, DEC, SECTOR, CAMERA, CCD, TIC, tmp_path / "scratch")
    kw = calls["obs"][0]
    assert kw == {"coordinates": f"{RA} {DEC}", "radius": "1.5 deg", "obs_collection": "TESS", "provenance_name": "SPOC",
                  "dataproduct_type": "timeseries", "sequence_number": SECTOR}
    # nearest first: 333 (download error, recorded), 444, 555, 666; 222 is on another CCD; the target,
    # the non-TIC name, the fast-cadence product and the row without a product are never downloaded
    assert [r.get("tic") or r["product"] for r in out] == [nb_name(333), "444", "555", "666"]
    assert "error" in out[0] and "synthetic download failure" in out[0]["error"]
    assert all(isinstance(r["lc"], vet.LC) and r["lc"].ccd == CCD for r in out[1:])
    assert out[1]["sep_deg"] == pytest.approx(0.26, abs=0.01) and out[1]["tmag"] == 11.0
    assert not any(str(TIC) in u or "777" in u or "fast" in u for u in calls["mast"])
    assert (tmp_path / "scratch" / "neighbours" / nb_name(444)).is_file()
    assert len(vet.neighbour_lcs(RA, DEC, SECTOR, CAMERA, CCD, TIC, tmp_path / "scratch", n_max=2)) == 2


def test_lc_reader_normalises_and_masks(tmp_path):
    p = write_lc(tmp_path / LC_NAME, seed=2, quality=((REL_EV, 32),))
    lc = vet.LC(p)
    assert lc.t[0] == pytest.approx(bjd(0.0)) and (lc.sector, lc.camera, lc.ccd) == (SECTOR, CAMERA, CCD)
    assert (lc.ra, lc.dec, lc.tmag) == (RA, DEC, 10.0)
    assert set(lc.col) == {"SAP_FLUX", "PDCSAP_FLUX", "PDCSAP_FLUX_ERR", "SAP_BKG", "MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2"}
    assert (~lc.ok).sum() == 1
    assert np.median(lc.col["PDCSAP_FLUX"][lc.ok]) == pytest.approx(1.0) and np.median(lc.col["SAP_FLUX"][lc.ok]) == pytest.approx(1.0)


# ------------------------------------------------------------------ orchestrator
SIB_TARGET = {"toi": "9999.01", "tid": str(TIC), "tfopwg_disp": "PC", "pl_orbper": "", "pl_orbpererr1": "",
              "pl_tranmid": str(bjd(REL_REF)), "pl_tranmiderr1": "0.001", "pl_trandurh": "3.0", "pl_trandep": "3000",
              "st_rad": "1.0", "st_logg": "4.44", "rowupdate": "2026-01-01"}
SIB_OTHER = {"toi": "9999.02", "tid": str(TIC), "tfopwg_disp": "PC", "pl_orbper": "4.1", "pl_orbpererr1": "0.0001",
             "pl_tranmid": str(bjd(0.5)), "pl_tranmiderr1": "0.001", "pl_trandurh": "3.0", "pl_trandep": "150",
             "st_rad": "1.0", "st_logg": "4.44", "rowupdate": "2026-01-01"}

# scenario -> (check that must flag, its expected state). Quality and Gaia checks never "fail" by design:
# the strongest state they give is "inconclusive".
CONTAMINATIONS = {
    "centroid": ("Background / centroid / pointing", "failed"),        # MOM_CENTR1 moves 0.02 px in transit
    "quality": ("Quality flags and coverage", "inconclusive"),         # momentum dump + scattered light at the event
    "common_mode": ("Common mode (same camera/CCD)", "failed"),        # two neighbours carry the same dip
    "diffimg": ("Difference-image centroid", "failed"),                # the pixel-level dip is on a star 4 px away
    "gaia": ("Gaia neighbours able to mimic the depth", "inconclusive"),  # a G=12 source 20" away
    "secondary": ("Secondary eclipse (circular aliases)", "failed"),   # 600-ppm dip at phase 0.5 of the P=6 d alias
    "sibling": ("Sibling TOI ephemerides", "failed"),                  # a periodic sibling predicted on the event
    "density": ("Stellar-density duration limit", "failed"),           # 0.1 Rsun star: 3-h transit too long at 6 d
    "shape": ("Shape matches reference transit", "failed"),            # event 2.3x deeper than the reference
}


def build_campaign(root: Path, scenario: str = "clean"):
    s = scenario
    data = root / "inputs"
    data.mkdir(parents=True, exist_ok=True)
    dips = [(REL_REF, DEPTH), (REL_EV, 7000e-6 if s == "shape" else DEPTH)]
    if s == "secondary":
        dips.append((REL_SEC, 600e-6))
    quality = ((REL_EV + 0.01, 32), (REL_EV + 0.30, 2048), (REL_EV + 0.31, 2048)) if s == "quality" else ()
    lc = write_lc(data / LC_NAME, seed=1, dips=dips, centroid_shift=0.02 if s == "centroid" else 0.0, quality=quality)
    registry, obs_rows = build_neighbours(data, dipping=(444, 555) if s == "common_mode" else ())
    if s != "outage":
        registry[TP_NAME] = write_tpf(data / TP_NAME, seed=11, dip_on="neighbour" if s == "diffimg" else "target")
    sibs = [dict(SIB_TARGET), dict(SIB_OTHER)]
    if s == "sibling":
        sibs[1].update(pl_tranmid=str(bjd(REL_EV) + 0.01))
    if s == "density":
        sibs[0].update(st_rad="0.1", st_logg="5.5")
    write_gaia(root, GAIA_CLEAN + ([gaia_row("5", 0.0, 20.0, 12.0)] if s == "gaia" else []))

    out = root / "campaigns" / CID
    (out / "runner").mkdir(parents=True, exist_ok=True)
    wj = lambda p, obj: p.write_text(json.dumps(obj), encoding="utf-8")
    wj(out / "runner" / "fetch_products.json",
       {"result": {"products": {LC_NAME: {"path": str(lc), "archive": "MAST", "format": "spoc_lc"}}}})
    wj(out / "runner" / "known_signal_recovery.json",
       {"result": {"per_product": {LC_NAME: {"epochs": [{"state": "recovered", "epoch_bjd": bjd(REL_REF) - 0.5 / 24,
                                                           "entry_offset_hours": 0.5}]}}}})
    wj(out / "period_aliases.json",
       {"candidates": [{"product": LC_NAME, "event_bjd": bjd(REL_EV) + dt, "depth_ppm": d, "n_allowed": n,
                        "allowed_periods_days": [6.0]} for dt, d, n in ((-0.02, 2600.0, 1), (0.01, 2900.0, 1))]})
    spec = {"campaign_id": CID, "outputs": f"campaigns/{CID}/", "random_seed": 7,
            "targets": [{"name": "TOI-9999.01", "tic": TIC, "ra_deg": RA, "dec_deg": DEC, "duration_h": 3.0}]}
    return spec, registry, obs_rows, sibs


def run_scenario(root: Path, mp, scenario="clean", fast=False, **kw):
    """Build the synthetic campaign for ``scenario`` and run vet() on it with every seam faked.

    ``fast`` (contamination runs only) caps the random-epoch trials at 60 and the difference-image
    bootstrap at 30 and skips the figures; the check logic and thresholds are unchanged. The clean
    null runs with vet()'s own defaults (300 trials, 200 bootstraps, figures)."""
    if fast:
        emp, dimg = vet.empirical, vet.difference_image
        mp.setattr(vet, "empirical", lambda *a, n=300, **k: emp(*a, n=min(n, 60), **k))
        mp.setattr(vet, "difference_image", lambda *a, n_boot=200, **k: dimg(*a, n_boot=min(n_boot, 30), **k))
        mp.setattr(vet, "plot", lambda *a, **k: None)
    scratch = root / "scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    mp.setenv("CYGNUS_SCRATCH", str(scratch))
    spec, registry, obs_rows, sibs = build_campaign(root, scenario)
    calls = install_fakes(mp, registry, obs_rows, sibs, outage=scenario == "outage")
    msgs = []
    kw.setdefault("extra_events", (bjd(40.0),))   # outside every light curve: skipped with a message
    rep = vet.vet(spec, root, echo=msgs.append, **kw)
    return {"report": rep, "root": root, "calls": calls, "msgs": msgs, "vdir": root / "campaigns" / CID / "vetting"}


def states(ev):
    return {k: v[0] for k, v in ev["checks"].items()}


@pytest.fixture(scope="module")
def clean(tmp_path_factory):
    root = tmp_path_factory.mktemp("clean")
    with pytest.MonkeyPatch.context() as mp:
        _guard(mp)
        return run_scenario(root, mp)


def test_vet_clean_null_reaches_every_check_and_passes_every_artifact_test(clean):
    rep = clean["report"]
    (e1,) = rep["events"]
    # the planted dip reaches all eleven event checks (the other two: the hand-given-epoch test)
    assert set(e1["checks"]) == EVENT_CHECKS
    bad = {k: v for k, v in e1["checks"].items() if v[0] != "passed"}
    assert not bad, bad
    assert e1["significant_dip"] and e1["fit"]["depth_ppm"] == pytest.approx(3000, abs=250)
    assert e1["fit"]["mid_bjd"] == pytest.approx(bjd(REL_EV), abs=10 / 1440)
    assert e1["screen_candidates"] == 2 and not e1["given_by_hand"]
    assert e1["aliases_from_reference"]["allowed_periods_days"] == [pytest.approx(6.0, abs=0.01)]      # P = 3, 2, 1.5, 1.2, 1 land on flat data
    assert [r["period_days"] for r in e1["secondary_eclipse"]] == [pytest.approx(6.0, abs=0.01)] and e1["secondary_eclipse"][0]["n_epochs"] == 1
    assert e1["aliases_density"][0]["disfavoured_circular"] is False
    assert any("not inside any retrieved light curve" in m for m in clean["msgs"])
    # reference transit, star, neighbours, pixels
    ref = rep["reference"]
    assert ref["product"] == LC_NAME and ref["fit"]["mid_bjd"] == pytest.approx(bjd(REL_REF), abs=10 / 1440)
    assert ref["difference_image"]["state"] == "done"
    assert ref["difference_image"]["offset_from_oot_centroid_arcsec"] < 0.25 * vet.TESS_PIX_ARCSEC
    assert rep["star"]["mass_msun_from_logg"] == pytest.approx(1.0, rel=0.05)
    assert [n.get("tic") for n in e1["neighbours"]] == [None, "444", "555", "666"]
    assert all(abs(n["pdcsap_z"]) < 4 for n in e1["neighbours"][1:])
    tp_calls = [u for u in clean["calls"]["mast"] if u.endswith("_tp.fits")]
    assert tp_calls == ["mast:TESS/product/" + TP_NAME]                        # one TPF serves E1 and REF
    assert e1["difference_image"]["diff_centroid_xy"] == pytest.approx([5.0, 5.0], abs=0.15)
    assert clean["calls"]["siblings"] == [TIC]


def test_vet_clean_null_writes_json_markdown_and_figures(clean):
    rep, vdir = clean["report"], clean["vdir"]
    assert "plot_error" not in rep
    on_disk = json.loads((vdir / "vetting.json").read_text(encoding="utf-8"))
    assert on_disk["campaign_id"] == CID and len(on_disk["events"]) == 1
    assert on_disk["events"][0]["checks"]["Red-noise significance"][0] == "passed"
    assert sorted(p.name for p in vdir.glob("*.png")) == [f"E1_S{SECTOR}.png"]
    md = (vdir / "VETTING.md").read_text(encoding="utf-8")
    assert md == vet.summary_md(rep)
    assert md.startswith(f"# Lead vetting: TOI-9999.01 (TIC {TIC})")
    for name in EVENT_CHECKS:
        assert f"| {name} | " in md, name
    assert "**Reference transit** (S10)" in md and "Reference difference-image centroid" in md
    assert "**Periodic TOIs on this TIC:** TOI-9999.02 P 4.1000 d" in md
    assert "## E1: S10, BJD 2458508.0" in md and "2 screen candidate(s) merged;" in md
    # plot() ran inside vet() (it swallows exceptions into plot_error, asserted absent above)
    assert all(p.stat().st_size > 10_000 for p in vdir.glob("*.png"))


@pytest.mark.parametrize("scenario", sorted(CONTAMINATIONS))
def test_vet_planted_contamination_flags_the_specific_check(scenario, tmp_path, monkeypatch):
    name, want = CONTAMINATIONS[scenario]
    # neighbours / pixels only where the contamination lives (the other scenarios never touch them)
    nb, px = scenario == "common_mode", scenario == "diffimg"
    rep = run_scenario(tmp_path, monkeypatch, scenario, fast=True, extra_events=(), neighbours=nb, pixels=px)["report"]
    e1 = rep["events"][0]
    got = states(e1)
    assert got[name] == want, e1["checks"][name]
    # specificity: every other event check keeps its clean-null state
    expect = EVENT_CHECKS - {name}
    expect -= set() if nb else {"Common mode (same camera/CCD)"}
    expect -= set() if px else {"Difference-image centroid"}
    others = {k: v for k, v in got.items() if k != name}
    assert others == {k: "passed" for k in expect}, {k: e1["checks"].get(k) for k in expect | set(others) if others.get(k) != "passed"}


def test_vet_outages_are_inconclusive_never_passed(tmp_path, monkeypatch):
    rep = run_scenario(tmp_path, monkeypatch, "outage", fast=True, extra_events=())["report"]
    assert "synthetic TAP outage" in rep["siblings"]["error"]
    assert rep["star"]["radius_rsun"] is None and rep["star"]["mass_msun_from_logg"] is None
    got = states(rep["events"][0])
    assert got["Sibling TOI ephemerides"] == "inconclusive"
    assert got["Difference-image centroid"] == "inconclusive"
    assert "unavailable" in rep["events"][0]["checks"]["Difference-image centroid"][1]
    assert got["Common mode (same camera/CCD)"] == "inconclusive"
    assert "neighbour query failed" in rep["events"][0]["checks"]["Common mode (same camera/CCD)"][1]
    assert "Stellar-density duration limit" not in got                        # no star without the TOI table
    assert rep["reference"]["difference_image"]["state"] == "inconclusive"
    for k in ("Shape matches reference transit", "Red-noise significance", "Background / centroid / pointing",
              "Quality flags and coverage", "Secondary eclipse (circular aliases)"):
        assert got[k] == "passed", k


def test_vet_hand_given_epochs_reach_the_remaining_checks_and_seams_can_be_disabled(clean, tmp_path, monkeypatch):
    res = run_scenario(tmp_path, monkeypatch, "clean", fast=True, pixels=False, neighbours=False,
                       extra_events=(bjd(REL_FLAT), bjd(REL_GAP)))
    rep = res["report"]
    e1, e2, e3 = rep["events"]
    # every check is reachable: with the clean null's E1, the flat hand-given epoch fails the box fit
    # and the epoch inside the data gap cannot be fitted
    assert set().union(clean["report"]["events"][0]["checks"], *(ev["checks"] for ev in rep["events"])) == ALL_CHECKS
    assert set(states(e1)) == EVENT_CHECKS - {"Difference-image centroid", "Common mode (same camera/CCD)"}
    assert set(states(e1).values()) == {"passed"}
    assert res["calls"]["mast"] == [] and res["calls"]["obs"] == []      # pixels / neighbours disabled
    assert "difference_image" not in rep["reference"]
    assert e2["given_by_hand"] and states(e2)["Box fit finds a dip"] == "failed" and not e2["significant_dip"]
    assert not {"Shape matches reference transit", "Detrending alternatives", "Red-noise significance",
                "Gaia neighbours able to mimic the depth", "Stellar-density duration limit",
                "Secondary eclipse (circular aliases)"} & set(e2["checks"])      # dip-only checks are not made
    assert e3["checks"] == {"Shape fit": ("not_tested", "fewer than 20 usable cadences around the event")} and e3["fit"] is None
    md = vet.summary_md(rep)
    assert "## E3: S10" in md and "(given by hand)" in md
    for name in ("Box fit finds a dip", "Shape fit"):
        assert f"| {name} | " in md, name


def test_vet_refuses_non_spoc_products(tmp_path, monkeypatch):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    rdir = tmp_path / "campaigns" / CID / "runner"
    rdir.mkdir(parents=True)
    (rdir / "fetch_products.json").write_text(json.dumps({"result": {"products": {
        "z1": {"path": "x", "archive": "IRSA", "format": "ztf_lc"}, LC_NAME: {"path": "y", "archive": "MAST"}}}}), encoding="utf-8")
    spec = {"campaign_id": CID, "targets": [{"name": "X", "tic": 1, "ra_deg": RA, "dec_deg": DEC}]}
    with pytest.raises(SystemExit, match=r"1 product\(s\).*z1 \(IRSA/ztf_lc\)"):
        vet.vet(spec, tmp_path)

"""Branch matrix for ``cygnus.multi.source_checks`` (offline, synthetic products)."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from cygnus.multi import source_checks as sc
from cygnus.multi.archives.base import Target

T = Target(name="T", ra_deg=10.0, dec_deg=20.0)


def _st(checks):
    return [(c.name, c.state) for c in checks]


def _csv(path: Path, text: str) -> Path:
    path.write_text(text, encoding="utf-8")
    return path


# ---------------------------------------------------------------------------- text
def test_text_checks_branches(tmp_path):
    empty = _csv(tmp_path / "e.txt", "")
    assert _st(sc.text_checks(empty, source="S")) == [("S payload", "failed")]
    assert "0 character(s)" in sc.text_checks(empty)[0].note

    short = _csv(tmp_path / "s.txt", "abc")
    assert _st(sc.text_checks(short, source="S", min_bytes=10)) == [("S payload", "failed")]

    ok = _csv(tmp_path / "o.txt", "  API VERSION 1.2  \n" + "x" * 200)
    c = sc.text_checks(ok, source="S")
    assert _st(c) == [("S payload", "passed")] and c[0].note.startswith("220 character(s); head 'API VERSION 1.2")

    assert _st(sc.text_checks(tmp_path / "missing.txt", source="S")) == [("S readable", "failed")]


# ---------------------------------------------------------------------------- tables
def test_table_checks_unreadable_votable_fails(tmp_path):
    p = _csv(tmp_path / "t.vot", "this is not xml")
    checks = sc.table_checks(p, T, kind="K")
    assert _st(checks) == [("K table readable", "failed")]


def test_table_checks_missing_file_fails(tmp_path):
    assert _st(sc.table_checks(tmp_path / "nope.csv", T)) == [("catalog table readable", "failed")]


def test_table_checks_empty_table_is_inconclusive(tmp_path):
    p = _csv(tmp_path / "t.csv", "ra,dec\n")
    checks = sc.table_checks(p, T, kind="K")
    assert _st(checks) == [("K rows", "inconclusive")] and checks[0].note == "0 row(s); columns ra, dec"


def test_table_checks_without_target_or_coordinates_stop_at_rows(tmp_path):
    p = _csv(tmp_path / "t.csv", "ra,dec\n10.0,20.0\n")
    assert _st(sc.table_checks(p, None, kind="K")) == [("K rows", "passed")]
    nocoord = _csv(tmp_path / "n.csv", "name,type\nA,EA\n")
    assert _st(sc.table_checks(nocoord, T, kind="K")) == [("K rows", "passed")]
    # coordinate columns present but no parsable values: no nearest-match check is invented
    blank = _csv(tmp_path / "b.csv", "ra,dec\n,\nnan,inf\n")
    assert _st(sc.table_checks(blank, T, kind="K")) == [("K rows", "passed")]


def test_table_checks_row_note_lists_at_most_ten_columns(tmp_path):
    cols = [f"c{i}" for i in range(12)]
    p = _csv(tmp_path / "t.csv", ",".join(cols) + "\n" + ",".join("1" for _ in cols) + "\n")
    note = sc.table_checks(p, T)[0].note
    assert "c9" in note and "c10" not in note


@pytest.mark.parametrize("header,dra_arcsec,state", [
    ("ra,dec", 4.9, "passed"),
    ("ra,dec", 4.99, "passed"),
    ("RAJ2000,DEJ2000", 5.5, "inconclusive"),
    ("ra_deg,dec_deg", 60.0, "inconclusive"),
])
def test_table_checks_nearest_match_threshold(tmp_path, header, dra_arcsec, state):
    # offsets along declination so the separation is exactly the offset
    near = T.dec_deg + dra_arcsec / 3600
    far = T.dec_deg + 0.1
    p = _csv(tmp_path / "t.csv", f"{header}\n{T.ra_deg},{far}\n{T.ra_deg},{near}\n")
    checks = sc.table_checks(p, T, kind="K")
    assert _st(checks) == [("K rows", "passed"), ("K nearest match", state)]
    assert f"nearest row {dra_arcsec:.2f}" in checks[1].note and "(n=2)" in checks[1].note


def test_table_checks_reads_json_and_votable(tmp_path):
    from astropy.io.votable import from_table, writeto
    from astropy.table import Table

    j = _csv(tmp_path / "t.json", json.dumps({"data": [{"ra": 10.0, "dec": 20.0}]}))
    assert _st(sc.table_checks(j, T, kind="K")) == [("K rows", "passed"), ("K nearest match", "passed")]
    v = tmp_path / "t.vot"
    writeto(from_table(Table({"ra": [10.0], "dec": [20.01]})), str(v))
    assert _st(sc.table_checks(v, T, kind="K")) == [("K rows", "passed"), ("K nearest match", "inconclusive")]


# ---------------------------------------------------------------------------- Gaia
_GAIA_HDR = "source_id,ra,dec,parallax,ruwe,non_single_star\n"


def test_gaia_checks_clean_cone_passes_with_parallax_range(tmp_path):
    p = _csv(tmp_path / "g.csv", _GAIA_HDR + "1,10.0,20.0,1.234,1.0,0\n2,10.01,20.0,-0.5,1.39,0\n")
    checks = {c.name: c for c in sc.gaia_checks(p, T)}
    assert checks["Gaia rows"].state == "passed" and checks["Gaia nearest match"].state == "passed"
    assert checks["Gaia RUWE"].state == "passed" and checks["Gaia RUWE"].note.startswith("0 of 2")
    assert checks["Gaia non-single-star flag"].state == "passed"
    px = checks["Gaia parallax"]
    assert px.state == "passed" and px.note == "2 parallax value(s), range -0.500..1.234 mas"


def test_gaia_checks_flags_and_missing_values(tmp_path):
    p = _csv(tmp_path / "g.csv", _GAIA_HDR + "1,10.0,20.0,,1.5,2\n2,10.0,20.001,,,\n")
    checks = {c.name: c for c in sc.gaia_checks(p, T)}
    assert checks["Gaia RUWE"].state == "inconclusive" and checks["Gaia RUWE"].note.startswith("1 of 1")
    assert checks["Gaia non-single-star flag"].state == "inconclusive"
    assert checks["Gaia non-single-star flag"].note.startswith("1 of 1")
    assert "Gaia parallax" not in checks                  # no parallax values: no check invented


def test_gaia_checks_without_astrometric_columns(tmp_path):
    p = _csv(tmp_path / "g.csv", "source_id,ra,dec\n1,10.0,20.0\n")
    assert [c.name for c in sc.gaia_checks(p, T)] == ["Gaia rows", "Gaia nearest match"]


def test_gaia_checks_unreadable_returns_the_table_failure(tmp_path):
    assert _st(sc.gaia_checks(tmp_path / "missing.csv", T)) == [("Gaia table readable", "failed")]


# ---------------------------------------------------------------------------- images
def _fits(path: Path, data) -> Path:
    from astropy.io import fits

    fits.PrimaryHDU(data).writeto(path)
    return path


def test_image_checks_constant_image_background_inconclusive(tmp_path):
    p = _fits(tmp_path / "c.fits", np.full((8, 8), 5.0))
    checks = sc.image_checks(p, source="S")
    assert _st(checks) == [("S image shape", "passed"), ("S finite pixels", "passed"), ("S background", "inconclusive")]
    assert checks[0].note == "(8, 8)" and "robust sigma 0" in checks[2].note


def test_image_checks_all_nan_image_fails_without_background(tmp_path):
    p = _fits(tmp_path / "n.fits", np.full((8, 8), np.nan))
    assert _st(sc.image_checks(p, source="S")) == [("S image shape", "passed"), ("S finite pixels", "failed")]


def test_image_checks_half_finite_threshold(tmp_path):
    rng = np.random.default_rng(3)
    data = rng.normal(0, 1, (10, 10))
    data[:5] = np.nan                                   # exactly 50 % finite: still passes
    assert dict(_st(sc.image_checks(_fits(tmp_path / "h.fits", data), source="S")))["S finite pixels"] == "passed"
    data[5, 0] = np.nan                                 # 49 %: fails
    st = dict(_st(sc.image_checks(_fits(tmp_path / "h2.fits", data), source="S")))
    assert st["S finite pixels"] == "failed" and st["S background"] == "passed"


def test_image_checks_unreadable_and_no_2d_hdu(tmp_path):
    bad = _csv(tmp_path / "b.fits", "not fits")
    assert _st(sc.image_checks(bad, source="S")) == [("S image readable", "failed")]
    one_d = _fits(tmp_path / "1d.fits", np.arange(5.0))
    c = sc.image_checks(one_d, source="S")
    assert _st(c) == [("S image readable", "failed")] and "no 2-D image HDU" in c[0].note


# ---------------------------------------------------------------------------- light curves
def _fits_lc(path: Path, *, n=50, timesys="TDB", bjdrefi=2457000, n_bad=0) -> Path:
    from astropy.io import fits

    t = 1500.0 + np.arange(n) * (120 / 86400)
    f = np.ones(n)
    f[:n_bad] = np.nan
    tab = fits.BinTableHDU.from_columns([fits.Column(name="TIME", format="D", array=t),
                                         fits.Column(name="SAP_FLUX", format="D", array=f)])
    if timesys is not None:
        tab.header["TIMESYS"] = timesys
    if bjdrefi:
        tab.header["BJDREFI"] = bjdrefi
    fits.HDUList([fits.PrimaryHDU(), tab]).writeto(path)
    return path


def test_lightcurve_checks_tdb_with_bjdref(tmp_path):
    c = sc.lightcurve_checks(_fits_lc(tmp_path / "a.fits"), fmt="spoc_lc", source="S")
    assert _st(c) == [("S usable cadences", "passed"), ("S baseline", "passed"), ("S time standard", "passed"),
                      ("S time reference", "passed")]
    assert c[0].note == "50 of 50 cadence(s) usable in channel SAP"
    assert c[2].note == "TIMESYS=TDB as supplied" and c[3].note == "BJDREF 2457000.0"


def test_lightcurve_checks_no_timesys_no_bjdref(tmp_path):
    c = sc.lightcurve_checks(_fits_lc(tmp_path / "a.fits", timesys=None, bjdrefi=0), fmt="fits_table", source="S")
    assert _st(c) == [("S usable cadences", "passed"), ("S baseline", "passed"), ("S time standard", "not_tested")]
    assert c[2].note == "no TIMESYS in the product header"


def test_lightcurve_checks_few_usable_cadences(tmp_path):
    c = sc.lightcurve_checks(_fits_lc(tmp_path / "a.fits", n=12, n_bad=3), fmt="spoc_lc", source="S")
    assert c[0].state == "inconclusive" and c[0].note.startswith("9 of 12")
    one = sc.lightcurve_checks(_fits_lc(tmp_path / "b.fits", n=5, n_bad=4), fmt="spoc_lc", source="S")
    assert [n for n, _ in _st(one)] == ["S usable cadences", "S time standard", "S time reference"]   # no baseline


def _vot_lc(path: Path, timecol: str) -> Path:
    from astropy.io.votable import from_table, writeto
    from astropy.table import Table

    n = 15
    writeto(from_table(Table({timecol: 58000.0 + np.arange(n), "mag": np.full(n, 18.0)})), str(path))
    return path


@pytest.mark.parametrize("timecol,state,has_ref", [
    ("mjd", "inconclusive", True),         # "MJD (UTC) exposure start; not barycentric"
    ("jd", "inconclusive", False),         # "JD as supplied (not barycentric)"
    ("time", "not_tested", False),         # "time column as supplied; standard not established"
    ("bjd", "passed", False),              # "BJD as supplied"
    ("hjd", "passed", False),
])
def test_lightcurve_checks_time_standard_branches(tmp_path, timecol, state, has_ref):
    c = dict(_st(sc.lightcurve_checks(_vot_lc(tmp_path / "z.vot", timecol), fmt="ztf_lc", source="S")))
    assert c["S time standard"] == state
    assert ("S time reference" in c) is has_ref


def test_lightcurve_checks_unreadable(tmp_path):
    p = _csv(tmp_path / "x.csv", "a,b\n1,2\n")
    c = sc.lightcurve_checks(p, fmt="csv_lc", source="S")
    assert _st(c) == [("S readable", "failed")] and "no time column" in c[0].note


# ---------------------------------------------------------------------------- json
def test_json_checks_branches(tmp_path):
    bad = _csv(tmp_path / "b.json", "{not json")
    assert _st(sc.json_checks(bad, source="S")) == [("S parse", "failed")]

    obj = _csv(tmp_path / "o.json", json.dumps({"object": {}, "orbit": {}}))
    assert _st(sc.json_checks(obj, source="S")) == [("S parse", "passed")]
    c = sc.json_checks(obj, source="S", required_keys=("object", "orbit"))
    assert _st(c) == [("S parse", "passed"), ("S required keys", "passed")] and c[1].note == "all present"
    c = sc.json_checks(obj, source="S", required_keys=("object", "signature", "phys_par"))
    assert c[1].state == "failed" and c[1].note == "missing signature, phys_par"

    lst = _csv(tmp_path / "l.json", json.dumps([{"object": 1}]))
    c = sc.json_checks(lst, source="S", required_keys=("object",))
    assert c[0].note == "list payload" and c[1].state == "failed" and c[1].note == "missing object"

"""Adapter framework, registry coverage and readers (offline, no network)."""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import pytest

from cygnus.multi.archives import base
from cygnus.multi.archives.base import AdapterUnavailable, ProductRef, Target
from cygnus.multi.readers import read_lightcurve, read_table


# ------------------------------------------------------------------ registry
def test_every_datasource_archive_has_an_adapter():
    """Every archive the project lists in DATA_SOURCES.md is registered."""
    expected = {
        # section 1
        "mast", "gaia", "skyview", "vizier", "simbad", "ned", "eso", "irsa", "legacysurvey",
        # section 5
        "horizons", "sbdb", "mpc", "astdys", "skybot",
        # section 2
        "earthdata", "copernicus", "asf", "usgs", "firms", "worldview",
        # section 3
        "microobservatory", "skynet",
        # supporting catalogue
        "exoarchive",
    }
    got = set(base.available())
    assert expected <= got, f"missing adapters: {sorted(expected - got)}"


def test_summary_has_description_and_formats():
    for row in base.summary():
        assert row["name"] and row["description"] and row["formats"]
        assert row["verified"].startswith("[V") or row["verified"].startswith("[K"), row
        assert row["capabilities"], row


def test_get_unknown_adapter_raises():
    with pytest.raises(KeyError, match="no archive adapter"):
        base.get("not-a-real-archive")


def test_adapter_unavailable_is_never_no_match():
    """A non-retrievable archive must raise AdapterUnavailable, not return []."""
    for name in ("asf", "usgs", "firms", "worldview"):
        with pytest.raises(AdapterUnavailable):
            base.get(name).discover(Target(name="X", ra_deg=1.0, dec_deg=2.0))


# ------------------------------------------------------------------ injectable discovery (offline)
class _Resp:
    def __init__(self, text="", content=b"", status=200):
        self.text, self.content, self.status_code = text, content, status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        import json

        return json.loads(self.text)


def test_gaia_adapter_builds_an_inline_csv_product():
    rows = [{"source_id": "1", "ra": "10.0", "dec": "20.0", "phot_g_mean_mag": "12.3"}]
    body = "source_id,ra,dec,phot_g_mean_mag\n" + "\n".join(
        ",".join(str(r[k]) for k in ("source_id", "ra", "dec", "phot_g_mean_mag")) for r in rows)

    def http(url, **kw):
        return _Resp(text=body)

    adapter = base.get("gaia", http=http)
    refs = adapter.discover(Target(name="Fake", ra_deg=10.0, dec_deg=20.0), radius_arcsec=30)
    assert len(refs) == 1 and refs[0].format == "csv" and refs[0].archive == "gaia"
    assert refs[0].extra["rows"][0]["source_id"] == "1"


def test_adapter_fetch_writes_inline_rows(tmp_path):
    adapter = base.get("vizier")
    ref = ProductRef(archive="vizier", product_id="v.csv", format="csv",
                     extra={"inline": True, "rows": [{"Name": "A", "Type": "Ecl"}]})
    out = adapter.fetch(ref, tmp_path / "v.csv")
    assert out.read_text(encoding="utf-8").splitlines() == ["Name,Type", "A,Ecl"]


def test_solar_system_context_adapters_inline(tmp_path):
    class _H:
        text = "API VERSION: 1.2"

        def raise_for_status(self):
            pass

    adapter = base.get("horizons", http=lambda *a, **k: _H())
    ref = refs = adapter.discover(Target(name="Ceres", ra_deg=0, dec_deg=0))
    assert refs and refs[0].format == "text"
    out = adapter.fetch(refs[0], tmp_path / "h.txt")
    assert "API VERSION" in out.read_text(encoding="utf-8")


# ------------------------------------------------------------------ readers
def test_read_lightcurve_detects_channels(tmp_path):
    p = tmp_path / "lc.csv"
    with p.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["TIME", "FLUX", "FLUX_CORR", "QUALITY"])
        for i in range(10):
            w.writerow([1500 + i * 120 / 86400, 1.0, 1.02, 0])
    lc = read_lightcurve(p, fmt="csv_lc")
    assert set(lc.channels) == {"FLUX", "FLUX_CORR"}
    assert lc.usable("FLUX").all()


def test_read_table_json_and_csv(tmp_path):
    j = tmp_path / "t.json"
    j.write_text('[{"a": 1, "b": "x"}]', encoding="utf-8")
    assert read_table(j)["rows"][0]["a"] == 1
    c = tmp_path / "t.csv"
    c.write_text("a,b\n1,x\n", encoding="utf-8")
    assert read_table(c)["columns"] == ["a", "b"]


# ------------------------------------------------------------------ target/ref round-trips
def test_target_from_mapping_and_productref_round_trip():
    t = Target.from_mapping({"name": "T", "ra_deg": 1, "dec_deg": 2, "tic": "123", "tmag": 9.1})
    assert t.tic == 123 and t.mag == 9.1
    ref = base.as_products([{"product_id": "p", "url": "http://x", "format": "csv", "sector": 7}], "mast", "csv")[0]
    assert ref.as_dict()["extra"]["sector"] == 7
    assert ref.kind == "table"          # kind derived from the format


# ------------------------------------------------------------------ source checks
def test_gaia_source_checks_flag_astrometric_problems(tmp_path):
    p = tmp_path / "gaia.csv"
    p.write_text("source_id,ra,dec,phot_g_mean_mag,ruwe,non_single_star,parallax\n"
                 "1,10.0,20.0,12.3,1.0,0,1.2\n"
                 "2,10.001,20.0,13.0,1.8,1,0.4\n", encoding="utf-8")
    checks = base.get("gaia").source_checks(Target(name="T", ra_deg=10.0, dec_deg=20.0),
                                            base.ProductRef(archive="gaia", product_id="gaia.csv", format="csv"),
                                            p)
    names = {c.name: c for c in checks}
    assert names["Gaia RUWE"].state == "inconclusive" and "RUWE > 1.4" in names["Gaia RUWE"].note
    assert names["Gaia non-single-star flag"].state == "inconclusive"
    assert names["Gaia nearest match"].state == "passed"


def test_image_source_checks_detect_nan_image(tmp_path):
    from astropy.io import fits
    rng = np.random.default_rng(0)
    good = tmp_path / "good.fits"
    fits.PrimaryHDU(100.0 + rng.normal(0, 1.0, (10, 10))).writeto(good)
    bad = tmp_path / "bad.fits"
    fits.PrimaryHDU(np.full((10, 10), np.nan)).writeto(bad)
    ok = base.get("skyview").source_checks(None, base.ProductRef(archive="skyview", product_id="g", format="fits_image"), good)
    assert all(c.state == "passed" for c in ok)
    states = {c.name: c.state for c in base.get("skyview").source_checks(
        None, base.ProductRef(archive="skyview", product_id="b", format="fits_image"), bad)}
    assert states["skyview finite pixels"] == "failed"


def test_mpc_adapter_queries_the_data_api(tmp_path):
    payload = '[{"OBS80": ["one"], "XML": ""}, {"OBS80": [], "XML": ""}]'

    class _R:
        text = payload

        def raise_for_status(self):
            pass

    captured = {}

    def http(url, **kw):
        captured["url"] = url
        captured["kw"] = kw
        return _R()

    adapter = base.get("mpc", http=http)
    refs = adapter.discover(Target(name="Ceres", ra_deg=0, dec_deg=0))
    assert refs and refs[0].format == "json" and "get-obs" in captured["url"]
    assert captured["kw"]["data"] == '{"desigs": ["Ceres"]}'          # GET with a JSON body
    out = adapter.fetch(refs[0], tmp_path / "mpc.json")
    checks = {c.name: c for c in adapter.source_checks(None, refs[0], out)}
    assert checks["MPC observation records"].state == "passed"
    assert "1 observation" in checks["MPC observation records"].note


def test_ztf_votable_lightcurve_reads_magnitudes(tmp_path):
    from astropy.io.votable import from_table, writeto
    from astropy.table import Table

    from cygnus.multi.readers import read_lightcurve

    tab = Table({"mjd": [1.0, 2.0, 3.0], "mag": [20.0, 19.9, 20.1], "magerr": [0.1, 0.1, 0.1],
                 "catflags": [0, 0, 0]})
    p = tmp_path / "ztf.vot"
    writeto(from_table(tab), str(p))
    lc = read_lightcurve(p, fmt="ztf_lc")
    assert lc.channels == ("MAG",) and lc.usable("MAG").all()
"""Discover + fetch contracts for every archive adapter no other test probes (offline).

Each adapter is driven through its injectable ``http`` seam (or a faked astroquery /
``netio.fetch_to_file``) and the tests assert: the query it sends, the ProductRef(s) it
builds (archive, format, kind), that ``fetch`` writes the expected file, that an empty
result is distinguished from an unavailable service (``AdapterUnavailable`` is never
"no match"), and the adapter's ``source_checks`` on the fetched product.

A real network call anywhere in this module fails the test (autouse guard).
"""

from __future__ import annotations

import io
import json
import sys
import types
from pathlib import Path

import numpy as np
import pytest

from cygnus.multi.archives import astronomy, base, solar_system
from cygnus.multi.archives.base import AdapterError, AdapterUnavailable, ProductRef, Target

T = Target(name="Test Star", ra_deg=139.4808650, dec_deg=-3.3875250, tic=52368076)


# ---------------------------------------------------------------------------- fakes
@pytest.fixture(autouse=True)
def _no_network(monkeypatch):
    import urllib.request

    import requests

    def boom(*a, **k):
        raise AssertionError(f"real network call attempted: {a[:2]!r}")

    monkeypatch.setattr(requests.sessions.Session, "request", boom)
    monkeypatch.setattr(urllib.request, "urlopen", boom)


class _Resp:
    def __init__(self, text: str = "", *, content: bytes | None = None, status: int = 200, payload=None):
        self.text = text
        self.content = content if content is not None else text.encode("utf-8")
        self.status_code = status
        self._payload = payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._payload if self._payload is not None else json.loads(self.text)


class Http:
    """Recording fake for the adapter ``http`` seam: returns queued responses (or raises)."""

    def __init__(self, *responses):
        self.responses = list(responses)
        self.calls: list[dict] = []

    def __call__(self, url, data=None, params=None, timeout=None, headers=None):
        self.calls.append({"url": url, "data": data, "params": params, "timeout": timeout, "headers": headers})
        r = self.responses.pop(0) if len(self.responses) > 1 else self.responses[0]
        if isinstance(r, BaseException):
            raise r
        if callable(r):
            return r(url, data=data, params=params)
        return r

    @property
    def adql(self) -> str:
        return self.calls[-1]["data"]["QUERY"]


def _fits_bytes(data=None) -> bytes:
    from astropy.io import fits

    rng = np.random.default_rng(0)
    arr = data if data is not None else 100.0 + rng.normal(0, 1.0, (12, 12))
    buf = io.BytesIO()
    fits.PrimaryHDU(arr).writeto(buf)
    return buf.getvalue()


def _states(checks) -> dict[str, str]:
    return {c.name: c.state for c in checks}


def _assert_tap_post(call, url):
    assert call["url"] == url
    d = call["data"]
    assert d["REQUEST"] == "doQuery" and d["LANG"] == "ADQL" and d["FORMAT"] == "csv"


def _write_spoc(path: Path, *, n: int = 200, n_flagged: int = 0, timesys: str | None = "TDB",
                bjdrefi: int = 2457000) -> Path:
    from astropy.io import fits

    t = 1500.0 + np.arange(n) * (120 / 86400)
    rng = np.random.default_rng(1)
    flux = 1000.0 + rng.normal(0, 1.0, n)
    q = np.zeros(n, dtype=np.int32)
    q[:n_flagged] = 128
    cols = [fits.Column(name="TIME", format="D", array=t),
            fits.Column(name="SAP_FLUX", format="E", array=flux),
            fits.Column(name="PDCSAP_FLUX", format="E", array=flux),
            fits.Column(name="QUALITY", format="J", array=q)]
    tab = fits.BinTableHDU.from_columns(cols)
    if timesys:
        tab.header["TIMESYS"] = timesys
    if bjdrefi:
        tab.header["BJDREFI"] = bjdrefi
        tab.header["BJDREFF"] = 0.0
    prim = fits.PrimaryHDU()
    prim.header["TIMEDEL"] = 120 / 86400
    fits.HDUList([prim, tab]).writeto(path)
    return path


# ============================================================================ SkyView
def test_skyview_discover_builds_cutout_refs_without_a_network_call():
    http = Http(AssertionError("discover must not call out"))
    a = base.get("skyview", http=http)
    refs = a.discover(T)
    assert http.calls == []
    assert len(refs) == 1
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.url) == ("skyview", "fits_image", "image", None)
    assert r.product_id == "skyview_Test_Star_DSS2Blue_0.fits"
    assert r.extra["survey"] == "DSS2 Blue" and r.extra["size_deg"] == 0.5 and r.extra["pixels"] == 500
    # the survey list is capped by ``limit``
    refs = a.discover(T, surveys=["DSS2 Red", "2MASS-J", "SDSS g"], limit=2, size_deg=0.1, pixels=100)
    assert [x.extra["survey"] for x in refs] == ["DSS2 Red", "2MASS-J"]
    assert refs[1].product_id.endswith("_2MASS-J_0.fits") and refs[1].extra["pixels"] == 100


def test_skyview_fetch_writes_fits_and_image_checks_pass(tmp_path):
    body = _fits_bytes()
    http = Http(_Resp(content=body))
    a = base.get("skyview", http=http)
    ref = a.discover(T)[0]
    out = a.fetch(ref, tmp_path / "sub" / "sv.fits")
    assert out.read_bytes() == body
    call = http.calls[0]
    assert call["url"] == astronomy.SKYVIEW_CGI
    p = call["params"]
    assert p["Survey"] == "DSS2 Blue" and p["Return"] == "FITS" and p["coordinates"] == "J2000"
    assert p["Size"] == 0.5 and p["Pixels"] == 500 and p["projection"] == "Tan"
    st = _states(a.source_checks(T, ref, out, {"kind": "image"}))
    assert st == {"skyview image shape": "passed", "skyview finite pixels": "passed", "skyview background": "passed"}


def test_skyview_fetch_sends_the_target_position(tmp_path):
    http = Http(_Resp(content=_fits_bytes()))
    a = base.get("skyview", http=http)
    ref = a.discover(T)[0]
    a.fetch(ref, tmp_path / "sv.fits")
    pos = http.calls[0]["params"]["Position"]
    assert pos is not None, "requests drops a None param, so SkyView receives no position at all"
    ra, dec = (float(x) for x in str(pos).split(","))
    assert abs(ra - T.ra_deg) < 1e-5 and abs(dec - T.dec_deg) < 1e-5


def test_skyview_refuses_non_fits_content(tmp_path):
    a = base.get("skyview", http=Http(_Resp("<html>500 Internal error</html>")))
    ref = a.discover(T)[0]
    with pytest.raises(AdapterError, match="non-FITS"):
        a.fetch(ref, tmp_path / "sv.fits")
    assert not (tmp_path / "sv.fits").exists()


def test_skyview_refuses_a_four_null_byte_body(tmp_path):
    a = base.get("skyview", http=Http(_Resp(content=b"\x00\x00\x00\x00")))
    ref = a.discover(T)[0]
    with pytest.raises(AdapterError):
        a.fetch(ref, tmp_path / "sv.fits")


def test_skyview_http_error_propagates_and_writes_nothing(tmp_path):
    a = base.get("skyview", http=Http(_Resp("x", status=500)))
    with pytest.raises(RuntimeError, match="HTTP 500"):
        a.fetch(a.discover(T)[0], tmp_path / "sv.fits")
    assert not (tmp_path / "sv.fits").exists()


# ============================================================================ TAP catalogue adapters
def _csv(*lines: str) -> _Resp:
    return _Resp("\n".join(lines) + "\n")


def test_simbad_discover_query_ref_fetch_and_checks(tmp_path):
    http = Http(_csv("main_id,otype,ra,dec,pmra,pmdec,sep_deg",
                     f"\"* alf Hya\",*,{T.ra_deg + 0.0002},{T.dec_deg},1.0,2.0,0.0002",
                     f"\"Far\",G,{T.ra_deg + 0.005},{T.dec_deg},,,0.005"))
    a = base.get("simbad", http=http)
    refs = a.discover(T, limit=50, radius_arcsec=20)
    _assert_tap_post(http.calls[0], astronomy.SIMBAD_TAP)
    q = http.adql
    assert q.startswith("SELECT TOP 50 main_id, otype, ra, dec, pmra, pmdec,") and "FROM basic" in q
    assert f"CIRCLE('ICRS', {T.ra_deg:.7f}, {T.dec_deg:.7f}, {20 / 3600:.7f})" in q
    assert len(refs) == 1
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.url) == ("simbad", "csv", "table", None)
    assert r.product_id == "simbad_Test_Star.csv" and "(2 rows)" in r.description and r.extra["inline"] is True
    out = a.fetch(r, tmp_path / "s.csv")
    lines = out.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "main_id,otype,ra,dec,pmra,pmdec,sep_deg" and len(lines) == 3
    st = _states(a.source_checks(T, r, out, {"kind": "table"}))
    assert st == {"simbad catalogue rows": "passed", "simbad catalogue nearest match": "passed"}


def test_simbad_empty_cone_is_a_zero_row_product_not_unavailable(tmp_path):
    a = base.get("simbad", http=Http(_csv("main_id,otype,ra,dec,pmra,pmdec,sep_deg")))
    refs = a.discover(T)
    assert len(refs) == 1 and refs[0].extra["rows"] == [] and "(0 rows)" in refs[0].description
    out = a.fetch(refs[0], tmp_path / "s.csv")
    assert out.exists()
    checks = a.source_checks(T, refs[0], out, {"kind": "table"})
    assert [(c.name, c.state) for c in checks] == [("simbad catalogue rows", "inconclusive")]


@pytest.mark.parametrize("name", ["simbad", "eso", "irsa", "exoarchive"])
@pytest.mark.parametrize("failure", [ConnectionError("down"),
                                     _Resp("<VOTABLE><INFO name=\"QUERY_STATUS\" value=\"ERROR\"/></VOTABLE>"),
                                     _Resp("bad gateway", status=502)])
def test_tap_adapters_report_outages_as_unavailable(name, failure):
    a = base.get(name, http=Http(failure))
    with pytest.raises(AdapterUnavailable):
        a.discover(T)


# ---------------------------------------------------------------------------- ESO
def test_eso_discover_query_and_refs():
    http = Http(_csv("dp_id,obs_collection,instrument_name,access_url,access_format,dataproduct_type,s_ra,s_dec",
                     "ADP.1,HARPS,HARPS,https://dataportal.eso.org/datalink/links?ID=ivo://eso.org/ID?ADP.1,"
                     "application/x-votable+xml;content=datalink,spectrum,139.48,-3.38",
                     "ADP.2,VVV,VIRCAM,https://dataportal.eso.org/datalink/links?ID=ivo://eso.org/ID?ADP.2,"
                     "application/x-votable+xml;content=datalink,image,139.48,-3.38",
                     ",X,Y,,,cube,139.48,-3.38"))
    refs = base.get("eso", http=http).discover(T, limit=7, radius_arcsec=5)
    _assert_tap_post(http.calls[0], astronomy.ESO_OBS_TAP)
    q = http.adql
    assert q.startswith("SELECT TOP 7 dp_id,") and "FROM ivoa.ObsCore" in q and "POINT('ICRS', s_ra, s_dec)" in q
    assert [r.product_id for r in refs] == ["ADP.1", "ADP.2", "eso_2"]
    assert all(r.archive == "eso" for r in refs)
    # ObsCore dataproduct_type picks the reader: a spectrum is never read as a light curve
    assert [(r.format, r.kind) for r in refs] == [("eso_spectrum", "spectrum"), ("fits_image", "image"),
                                                   ("fits_cube", "image")]
    assert refs[0].url.startswith("https://dataportal.eso.org/datalink/") and refs[0].extra["instrument"] == "HARPS"
    assert refs[2].url == ""          # an empty access_url survives as "", and base.fetch refuses it


def test_eso_empty_result_is_no_products():
    assert base.get("eso", http=Http(_csv("dp_id,obs_collection,instrument_name,access_url"))).discover(T) == []


def test_eso_fetch_goes_through_the_shared_downloader(tmp_path, monkeypatch):
    import cygnus.ingest.netio as netio

    seen = {}
    body = _fits_bytes()

    def fake_fetch(url, dest, *, timeout_s):
        seen.update(url=url, timeout_s=timeout_s)
        Path(dest).write_bytes(body)
        return {"url": url, "bytes": len(body)}

    monkeypatch.setattr(netio, "fetch_to_file", fake_fetch)
    a = base.get("eso", http=Http(_csv("dp_id,obs_collection,instrument_name,access_url,access_format,"
                                       "dataproduct_type,s_ra,s_dec",
                                       "ADP.2,VVV,VIRCAM,https://example.invalid/ADP.2.fits,image/fits,image,1,2",
                                       "ADP.3,VVV,VIRCAM,,image/fits,image,1,2")))
    refs = a.discover(T)
    out = a.fetch(refs[0], tmp_path / "e.fits", timeout_s=33)
    assert seen == {"url": "https://example.invalid/ADP.2.fits", "timeout_s": 33}
    assert out.read_bytes() == body
    assert all(s == "passed" for s in _states(a.source_checks(T, refs[0], out, {"kind": "image"})).values())
    with pytest.raises(AdapterError, match="no URL"):
        a.fetch(refs[1], tmp_path / "e3.fits")


# ---------------------------------------------------------------------------- IRSA
def test_irsa_allwise_query_ref_fetch_and_checks(tmp_path):
    http = Http(_csv("designation,ra,dec,w1mpro,w2mpro,w3mpro,w4mpro,sep_arcsec",
                     f"J091755.40-032315.1,{T.ra_deg + 0.01},{T.dec_deg},5.1,5.0,4.9,4.8,36.0"))
    a = base.get("irsa", http=http)
    refs = a.discover(T, limit=3)
    _assert_tap_post(http.calls[0], astronomy.IRSA_TAP)
    q = http.adql
    assert q.startswith("SELECT TOP 3 designation, ra, dec, w1mpro,") and "FROM allwise_p3as_psd" in q
    assert f"CIRCLE('J2000', {T.ra_deg:.7f}, {T.dec_deg:.7f}, {10 / 3600:.7f})" in q
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.product_id) == ("irsa", "csv", "table", "irsa_allwise_Test_Star.csv")
    out = a.fetch(r, tmp_path / "w.csv")
    assert "J091755.40-032315.1" in out.read_text(encoding="utf-8")
    st = _states(a.source_checks(T, r, out, {"kind": "table"}))
    # the only row is ~36" away: rows present, nearest match not within 5"
    assert st == {"irsa catalogue rows": "passed", "irsa catalogue nearest match": "inconclusive"}


def _ztf_votable_bytes(tmp_path) -> bytes:
    from astropy.io.votable import from_table, writeto
    from astropy.table import Table

    n = 20
    tab = Table({"oid": np.full(n, 7), "mjd": 58300.0 + np.arange(n), "mag": 18.0 + 0.01 * np.arange(n),
                 "magerr": np.full(n, 0.02), "catflags": np.zeros(n, int)})
    p = tmp_path / "src.vot"
    writeto(from_table(tab), str(p))
    return p.read_bytes()


def test_irsa_ztf_mode_builds_a_lazy_ref_and_fetches_through_the_cgi(tmp_path):
    body = _ztf_votable_bytes(tmp_path)
    http = Http(_Resp(content=body))
    a = base.get("irsa", http=http)
    refs = a.discover(T, mode="ztf", radius_arcsec=3.6)
    assert http.calls == []                       # ztf discovery is lazy
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.url) == ("irsa", "ztf_lc", "lightcurve", None)
    assert r.product_id == "ztf_Test_Star.vot" and r.extra["radius"] == 3.6
    out = a.fetch(r, tmp_path / "z" / "ztf.vot")
    assert out.read_bytes() == body
    call = http.calls[0]
    assert call["url"] == astronomy.IRSA_ZTF
    assert call["params"] == {"POS": f"CIRCLE {T.ra_deg} {T.dec_deg} {3.6 / 3600}"}   # CGI takes POS (+FORMAT) only
    st = _states(a.source_checks(T, r, out, {"kind": "lightcurve"}))
    assert st["irsa usable cadences"] == "passed" and st["irsa baseline"] == "passed"
    assert st["irsa time standard"] == "inconclusive"          # ZTF MJD is UTC exposure start, not barycentric
    assert st["irsa time reference"] == "passed"                # MJD offset 2400000.5 recorded as BJDREF


# ---------------------------------------------------------------------------- Legacy Survey
def test_legacysurvey_discover_is_lazy_and_fetch_hits_the_cutout_service(tmp_path):
    body = _fits_bytes()
    http = Http(_Resp(content=body))
    a = base.get("legacysurvey", http=http)
    refs = a.discover(T, size_arcsec=30.0, layer="ls-dr9")
    assert http.calls == []
    r = refs[0]
    assert (r.archive, r.format, r.kind) == ("legacysurvey", "fits_image", "image")
    assert r.product_id == "legacysurvey_ls-dr9_Test_Star.fits"
    out = a.fetch(r, tmp_path / "ls.fits")
    call = http.calls[0]
    assert call["url"] == f"{astronomy.LS_VIEWER}/cutout.fits"
    # the viewer takes an integer pixel count: 30" at 0.262"/px is 115 px (a float size is an HTTP 500 live)
    assert call["params"] == {"ra": T.ra_deg, "dec": T.dec_deg, "size": 115, "pixscale": 0.262, "layer": "ls-dr9",
                              "fits": "1"}
    assert out.read_bytes() == body
    assert all(s == "passed" for s in _states(a.source_checks(T, r, out, {"kind": "image"})).values())


def test_legacysurvey_refuses_non_fits_content(tmp_path):
    a = base.get("legacysurvey", http=Http(_Resp("no coverage")))
    with pytest.raises(AdapterError, match="non-FITS"):
        a.fetch(a.discover(T)[0], tmp_path / "ls.fits")
    assert not (tmp_path / "ls.fits").exists()


# ---------------------------------------------------------------------------- Exoplanet Archive
_TOI_CSV = ("toi,tid,tfopwg_disp,ra,dec,st_tmag,pl_trandep,pl_trandurh,pl_tranmid,pl_orbper",
            f"1234.01,52368076,PC,{T.ra_deg},{T.dec_deg},9.1,500,2.1,2459000.5,3.3")


def test_exoarchive_toi_mode_queries_by_tic(tmp_path):
    http = Http(_csv(*_TOI_CSV))
    a = base.get("exoarchive", http=http)
    refs = a.discover(T)
    _assert_tap_post(http.calls[0], astronomy.EXO_TAP)
    assert http.adql.endswith("FROM toi WHERE tid = 52368076") and "pl_trandep" in http.adql
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.product_id) == ("exoarchive", "csv", "table", "exoarchive_toi_Test_Star.csv")
    assert r.extra["rows"][0]["toi"] == "1234.01"
    out = a.fetch(r, tmp_path / "toi.csv")
    st = _states(a.source_checks(T, r, out, {"kind": "table"}))
    assert st == {"exoarchive catalogue rows": "passed", "exoarchive catalogue nearest match": "passed"}


def test_exoarchive_planet_mode_lowercases_and_strips_quotes():
    http = Http(_csv("pl_name,hostname,tic_id,ra,dec"))
    refs = base.get("exoarchive", http=http).discover(Target(name="O'Brien-1 B", ra_deg=1.0, dec_deg=2.0), mode="planet")
    assert http.adql.endswith("FROM pscomppars WHERE lower(pl_name) = 'obrien-1 b'")
    assert refs[0].product_id == "exoarchive_planet_O'Brien-1_B.csv" and refs[0].extra["rows"] == []


@pytest.mark.parametrize("mode,tic", [("cone", 52368076), ("toi", None)])
def test_exoarchive_box_search_mode(mode, tic):
    """Any mode other than toi-with-TIC / planet runs the positional box (a TOI query without a TIC too)."""
    http = Http(_csv(*_TOI_CSV))
    tgt = Target(name="Box", ra_deg=T.ra_deg, dec_deg=T.dec_deg, tic=tic)
    refs = base.get("exoarchive", http=http).discover(tgt, mode=mode, limit=4)
    q = http.adql
    assert q.startswith("SELECT top 4 toi, tid, tfopwg_disp, ra, dec FROM toi WHERE ra BETWEEN")
    r = 30.0 / 3600
    assert f"dec BETWEEN {T.dec_deg - r:.7f} AND {T.dec_deg + r:.7f}" in q
    assert refs[0].product_id == f"exoarchive_{mode}_Box.csv"


# ============================================================================ solar-system context adapters
def test_horizons_query_ref_fetch_and_checks(tmp_path):
    http = Http(_Resp("API VERSION: 1.2\nTarget body name: 1 Ceres"))
    a = base.get("horizons", http=http)
    refs = a.discover(Target(name="Ceres", ra_deg=0, dec_deg=0))
    call = http.calls[0]
    assert call["url"] == solar_system.HORIZONS_API
    assert call["params"] == {"format": "text", "COMMAND": "'Ceres'", "OBJ_DATA": "'YES'", "MAKE_EPHEM": "'NO'"}
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.product_id) == ("horizons", "text", "text", "horizons_Ceres.txt")
    out = a.fetch(r, tmp_path / "h.txt")
    assert out.read_text(encoding="utf-8").startswith("API VERSION")
    assert _states(a.source_checks(None, r, out)) == {"horizons payload": "passed"}
    a.discover(Target(name="Ceres", ra_deg=0, dec_deg=0), command="'1;'")
    assert http.calls[-1]["params"]["COMMAND"] == "'1;'"


def test_sbdb_query_ref_fetch_and_checks(tmp_path):
    payload = '{"object": {"fullname": "1 Ceres"}, "orbit": {"elements": []}}'
    http = Http(_Resp(payload))
    a = base.get("sbdb", http=http)
    refs = a.discover(Target(name="1 Ceres", ra_deg=0, dec_deg=0))
    assert http.calls[0]["url"] == solar_system.SBDB_API and http.calls[0]["params"] == {"sstr": "1 Ceres"}
    r = refs[0]
    # the SBDB product is a JSON body stored as a *text* product
    assert (r.archive, r.format, r.kind, r.product_id) == ("sbdb", "text", "text", "sbdb_1_Ceres.json")
    out = a.fetch(r, tmp_path / "sbdb.json")
    assert json.loads(out.read_text(encoding="utf-8"))["object"]["fullname"] == "1 Ceres"
    assert _states(a.source_checks(None, r, out)) == {"sbdb payload": "passed"}


def test_astdys_reachability_marker(tmp_path):
    http = Http(_Resp("<html>AstDyS</html>"))
    a = base.get("astdys", http=http)
    refs = a.discover(Target(name="Vesta", ra_deg=0, dec_deg=0))
    assert http.calls[0]["url"] == solar_system.ASTDYS + "/" and http.calls[0]["params"] is None
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.product_id) == ("astdys", "text", "text", "astdys_Vesta.txt")
    out = a.fetch(r, tmp_path / "a.txt")
    assert "AstDyS reachable" in out.read_text(encoding="utf-8")
    assert _states(a.source_checks(None, r, out)) == {"astdys payload": "passed"}


@pytest.mark.parametrize("name", ["horizons", "sbdb", "astdys", "mpc"])
@pytest.mark.parametrize("failure", [ConnectionError("down"), _Resp("nope", status=503)])
def test_solar_system_outages_are_unavailable(name, failure):
    with pytest.raises(AdapterUnavailable):
        base.get(name, http=Http(failure)).discover(Target(name="Ceres", ra_deg=0, dec_deg=0))


# ---------------------------------------------------------------------------- SkyBoT
def _fake_skybot(monkeypatch, behaviour):
    seen = {}

    class _Skybot:
        @staticmethod
        def cone_search(coo, rad, epoch, **kw):
            seen.update(coo=coo, rad=rad, epoch=epoch)
            return behaviour()

    mod = types.ModuleType("astroquery.imcce")
    mod.Skybot = _Skybot
    monkeypatch.setitem(sys.modules, "astroquery.imcce", mod)
    return seen


def _skybot_table():
    from astropy.table import Table

    return Table({"Number": [1, 4], "Name": ["Ceres", "Vesta"], "RA": [10.001, 10.002], "DEC": [5.0, 5.001],
                  "V": [8.5, 7.9]})


def test_skybot_filled_rows_are_carried_in_the_ref(monkeypatch):
    seen = _fake_skybot(monkeypatch, _skybot_table)
    refs = base.get("skybot").discover(Target(name="F", ra_deg=10.0, dec_deg=5.0),
                                       epoch_iso="2024-01-01T00:00:00", radius_arcsec=30)
    assert seen["coo"].ra.deg == pytest.approx(10.0) and seen["coo"].dec.deg == pytest.approx(5.0)
    assert seen["rad"].to_value("arcsec") == pytest.approx(30.0)
    assert seen["epoch"].scale == "utc" and seen["epoch"].isot.startswith("2024-01-01T00:00:00")
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.product_id) == ("skybot", "csv", "table", "skybot_F.csv")
    assert "(2 rows)" in r.description
    assert r.extra["rows"] == [{"Number": "1", "Name": "Ceres", "RA": "10.001", "DEC": "5.0", "V": "8.5"},
                               {"Number": "4", "Name": "Vesta", "RA": "10.002", "DEC": "5.001", "V": "7.9"}]


def test_skybot_fetch_writes_the_rows(monkeypatch, tmp_path):
    _fake_skybot(monkeypatch, _skybot_table)
    a = base.get("skybot")
    ref = a.discover(Target(name="F", ra_deg=10.0, dec_deg=5.0), epoch_iso="2024-01-01T00:00:00")[0]
    out = a.fetch(ref, tmp_path / "skybot.csv")
    assert "Ceres" in out.read_text(encoding="utf-8")
    st = _states(a.source_checks(Target(name="F", ra_deg=10.0, dec_deg=5.0), ref, out, {"kind": "table"}))
    assert st["skybot catalogue rows"] == "passed"


def test_skybot_without_epoch_is_unavailable_not_no_match(monkeypatch):
    seen = _fake_skybot(monkeypatch, _skybot_table)
    with pytest.raises(AdapterUnavailable, match="epoch_iso"):
        base.get("skybot").discover(Target(name="F", ra_deg=10.0, dec_deg=5.0))
    assert seen == {}                              # no query was even attempted


def test_skybot_missing_astroquery_is_unavailable(monkeypatch):
    monkeypatch.setitem(sys.modules, "astroquery.imcce", None)     # import raises ImportError
    with pytest.raises(AdapterUnavailable, match="not installed"):
        base.get("skybot").discover(Target(name="F", ra_deg=10.0, dec_deg=5.0), epoch_iso="2024-01-01T00:00:00")


def test_skybot_service_error_is_unavailable(monkeypatch):
    def fail():
        raise RuntimeError("IMCCE service returned HTTP 503")

    _fake_skybot(monkeypatch, fail)
    with pytest.raises(AdapterUnavailable, match="SkyBoT failed"):
        base.get("skybot").discover(Target(name="F", ra_deg=10.0, dec_deg=5.0), epoch_iso="2024-01-01T00:00:00")


# ---------------------------------------------------------------------------- MPC
def test_mpc_obs_df_payload_counts_observations(tmp_path):
    payload = json.dumps([{"designation": "Ceres", "OBS_DF": [{"obstime": "2020-01-01"}, {"obstime": "2020-01-02"},
                                                               {"obstime": "2020-01-03"}]}])
    http = Http(_Resp(payload))
    a = base.get("mpc", http=http)
    refs = a.discover(Target(name="X", ra_deg=0, dec_deg=0), desig="1 Ceres")
    call = http.calls[0]
    assert call["url"] == f"{solar_system.MPC_DATA}/api/get-obs"
    assert json.loads(call["data"]) == {"desigs": ["1 Ceres"]} and call["headers"]["Content-Type"] == "application/json"
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.product_id) == ("mpc", "json", "table", "mpc_obs_1_Ceres.json")
    out = a.fetch(r, tmp_path / "mpc.json")
    checks = {c.name: c for c in a.source_checks(None, r, out)}
    assert checks["mpc catalogue rows"].state == "passed"
    assert checks["MPC observation records"].state == "passed"
    assert "1 object record(s), 3 observation" in checks["MPC observation records"].note


def test_mpc_xml_payload_counts_observations_not_characters(tmp_path):
    xml = "<ades version=\"2022\"><obsBlock><obsData><optical/><optical/></obsData></obsBlock></ades>"
    a = base.get("mpc", http=Http(_Resp(json.dumps([{"designation": "Ceres", "XML": xml}]))))
    ref = a.discover(Target(name="Ceres", ra_deg=0, dec_deg=0))[0]
    out = a.fetch(ref, tmp_path / "mpc.json")
    note = {c.name: c for c in a.source_checks(None, ref, out)}["MPC observation records"].note
    assert f"{len(xml)} observation" not in note
    assert "2 observation" in note


def test_mpc_empty_list_is_inconclusive_and_garbage_fails(tmp_path):
    a = base.get("mpc", http=Http(_Resp("[]")))
    ref = a.discover(Target(name="Nobody", ra_deg=0, dec_deg=0))[0]
    out = a.fetch(ref, tmp_path / "e.json")
    st = _states(a.source_checks(None, ref, out))
    assert st["MPC observation records"] == "inconclusive" and st["mpc catalogue rows"] == "inconclusive"

    g = base.get("mpc", http=Http(_Resp("<html>gateway timeout</html>")))
    ref = g.discover(Target(name="Ceres", ra_deg=0, dec_deg=0))[0]
    out = g.fetch(ref, tmp_path / "g.json")
    st = _states(g.source_checks(None, ref, out))
    assert st["MPC observation records"] == "failed" and st["mpc catalogue table readable"] == "failed"


# ============================================================================ Earth observation / observing
@pytest.mark.parametrize("name,url,pid", [("earthdata", "https://www.earthdata.nasa.gov/", "earthdata_status.txt"),
                                          ("copernicus", "https://dataspace.copernicus.eu/", "cdse_status.txt")])
def test_earth_observation_status_products(tmp_path, name, url, pid):
    http = Http(_Resp("<html/>"))
    a = base.get(name, http=http)
    refs = a.discover(T)
    assert http.calls[0]["url"] == url
    r = refs[0]
    assert (r.archive, r.format, r.kind, r.product_id) == (name, "text", "text", pid)
    out = a.fetch(r, tmp_path / pid)
    assert "reachable" in out.read_text(encoding="utf-8")
    assert _states(a.source_checks(T, r, out)) == {f"{name} payload": "passed"}
    assert a.capabilities_list() == ["earth_observation", "context"]
    with pytest.raises(AdapterUnavailable, match="unreachable"):
        base.get(name, http=Http(ConnectionError("dns"))).discover(T)


@pytest.mark.parametrize("name,url", [("skynet", "https://skynet.unc.edu/"),
                                      ("microobservatory", "https://mo-www.cfa.harvard.edu/cgi-bin/OWN/Own.pl")])
def test_observing_routes_discover_status_but_never_fetch(tmp_path, name, url):
    http = Http(_Resp("ok"))
    a = base.get(name, http=http)
    refs = a.discover(T)
    assert http.calls[0]["url"] == url
    assert (refs[0].archive, refs[0].format, refs[0].kind) == (name, "text", "text")
    assert a.capabilities_list() == ["observing"]
    with pytest.raises(AdapterUnavailable):
        a.fetch(refs[0], tmp_path / "x.txt")
    assert not (tmp_path / "x.txt").exists()
    with pytest.raises(AdapterUnavailable):
        base.get(name, http=Http(_Resp("x", status=404))).discover(T)


# ============================================================================ MAST
@pytest.mark.parametrize("fn,coll,fmt", [
    ("tess2020-s0026-0000000000000007-0188-s_lc.fits", "TESS", "spoc_lc"),
    ("hlsp_qlp_tess_ffi_s0001-0000000000000007_tess_v01_llc-lc.fits", "TESS", "spoc_lc"),
    ("tess2020-s0026-0000000000000007-0188-s_tp.fits", "TESS", "fits_table"),
    ("kplr000757076-2009166043257_llc.fits", "Kepler", "kepler_lc"),
    ("kplr000757076-2009166043257_lpd-targ.fits.gz", "Kepler", "kepler_lc"),
    ("ktwo201367065-c01_llc.fits", "K2", "kepler_lc"),
    ("hlsp_x_hst_wfc3_f555w_drz.fits", "HST", "fits_table"),
    ("PS1_x_stack.fits.gz", "PS1", "fits_table"),
    ("GI1_x-nd-int.jpg", "GALEX", "fits_image"),
])
def test_mast_fmt_for_branches(fn, coll, fmt):
    assert astronomy.MastAdapter._fmt_for(fn, coll) == fmt


def _mast_http(products, *, obs=({"obsid": 11}, {"obsid": 12}), status="COMPLETE"):
    calls = []

    def respond(url, data=None, params=None):
        req = json.loads(data["request"])
        calls.append(req)
        if req["service"] == "Mast.Caom.Filtered":
            return _Resp(payload={"status": status, "data": list(obs)})
        return _Resp(payload={"status": "COMPLETE", "data": products})

    return Http(respond), calls


def test_mast_product_list_filtering_and_refs():
    good = "tess2018206045859-s0001-0000000052368076-0120-s_lc.fits"
    prods = [
        {"productFilename": good, "productSubGroupDescription": "LC", "dataURI": f"mast:TESS/product/{good}", "obsID": 11},
        {"productFilename": good, "productSubGroupDescription": "LC", "obsID": 12},                   # duplicate
        {"productFilename": "", "productSubGroupDescription": "LC"},                                  # no filename
        {"productFilename": "tess2018206045859-s0001-0000000052368076-0120-s_tp.fits",
         "productSubGroupDescription": "TP"},                                                          # wrong subgroup
        {"productFilename": "tess-s0028-x-a_fast", "productSubGroupDescription": "LC"},               # ends with fast
        {"productFilename": "tess-s0028-x-fast-lc.fits", "productSubGroupDescription": "LC"},         # "-fast"
        {"productFilename": "tess2020212050318-s0028-0000000052368076-0190-s_lc.fits",
         "productSubGroupDescription": "LC", "obsID": 12},                                             # no dataURI
        {"productFilename": "tess2021-s0041-0000000052368076-0200-s_lc.fits", "productSubGroupDescription": "LC"},
    ]
    http, calls = _mast_http(prods)
    refs = base.get("mast", http=http).discover(T, limit=2)
    assert [c["service"] for c in calls] == ["Mast.Caom.Filtered", "Mast.Caom.Products"]
    assert calls[1]["params"] == {"obsid": "11,12"} and calls[1]["pagesize"] == 1000
    assert [r.product_id for r in refs] == [good, "tess2020212050318-s0028-0000000052368076-0190-s_lc.fits"]
    r0, r1 = refs
    assert (r0.archive, r0.format, r0.kind) == ("mast", "spoc_lc", "lightcurve")
    assert r0.url == f"{astronomy.MAST_DL}?uri=mast:TESS/product/{good}"
    assert r1.url == f"{astronomy.MAST_DL}?uri=mast:TESS/product/{r1.product_id}"     # default URI from filename
    assert r0.extra["sector"] == 1 and r1.extra["sector"] == 28 and r0.extra["tic"] == 52368076
    assert r0.extra["obsid"] == 11


def test_mast_non_tess_collection_uses_the_target_name_and_no_subgroup():
    prods = [{"productFilename": "kplr000757076-2009166043257_llc.fits", "productSubGroupDescription": "LLC"},
             {"productFilename": "kplr000757076-2009166043257_lpd-targ.fits.gz", "productSubGroupDescription": "TPF"}]
    http, calls = _mast_http(prods, obs=({"obsid": 5},))
    refs = base.get("mast", http=http).discover(T, collection="Kepler", provenance="", subgroup="")
    filters = {f["paramName"]: f["values"] for f in calls[0]["params"]["filters"]}
    assert filters == {"target_name": ["Test Star"], "obs_collection": ["Kepler"], "dataproduct_type": ["timeseries"]}
    assert [r.format for r in refs] == ["kepler_lc", "kepler_lc"] and all(r.extra["sector"] is None for r in refs)


def test_mast_drops_real_fast_cadence_filenames():
    fast = "tess2020212050318-s0028-0000000052368076-0190-a_fast-lc.fits"
    http, _ = _mast_http([{"productFilename": fast, "productSubGroupDescription": "FAST-LC"}])
    refs = base.get("mast", http=http).discover(T, subgroup="")
    assert refs == []


def test_mast_empty_observations_is_no_products_and_outages_are_unavailable():
    http, calls = _mast_http([], obs=())
    assert base.get("mast", http=http).discover(T) == []
    assert len(calls) == 1                           # no product-list call when nothing was observed

    http, _ = _mast_http([], status="EXECUTING")
    with pytest.raises(AdapterUnavailable, match="status EXECUTING"):
        base.get("mast", http=http).discover(T)

    with pytest.raises(AdapterUnavailable, match="MAST query failed"):
        base.get("mast", http=Http(ConnectionError("reset"))).discover(T)

    def second_fails(url, data=None, params=None):
        if json.loads(data["request"])["service"] == "Mast.Caom.Products":
            raise TimeoutError("product list hung")
        return _Resp(payload={"status": "COMPLETE", "data": [{"obsid": 1}]})

    with pytest.raises(AdapterUnavailable, match="product list failed"):
        base.get("mast", http=Http(second_fails)).discover(T)


def test_mast_fetch_uses_the_download_url(tmp_path, monkeypatch):
    import cygnus.ingest.netio as netio

    seen = {}

    def fake_fetch(url, dest, *, timeout_s):
        seen["url"] = url
        _write_spoc(Path(dest))
        return {}

    monkeypatch.setattr(netio, "fetch_to_file", fake_fetch)
    fn = "tess2018206045859-s0001-0000000052368076-0120-s_lc.fits"
    http, _ = _mast_http([{"productFilename": fn, "productSubGroupDescription": "LC", "dataURI": f"mast:TESS/product/{fn}"}])
    a = base.get("mast", http=http)
    ref = a.discover(T)[0]
    out = a.fetch(ref, tmp_path / fn)
    assert seen["url"] == ref.url and out.exists()


@pytest.mark.parametrize("n_flagged,state", [(20, "passed"), (160, "inconclusive")])
def test_mast_quality_flag_check_on_a_synthetic_spoc_product(tmp_path, n_flagged, state):
    p = _write_spoc(tmp_path / "tess-s0001-0000000052368076-s_lc.fits", n=200, n_flagged=n_flagged)
    ref = ProductRef(archive="mast", product_id=p.name, format="spoc_lc")
    checks = {c.name: c for c in base.get("mast").source_checks(T, ref, p, {"kind": "lightcurve"})}
    q = checks["MAST quality flags"]
    assert q.state == state and q.note.startswith(f"{n_flagged} of 200 cadence(s)")
    assert checks["mast usable cadences"].state == "passed"
    assert checks["mast time standard"].state == "passed" and "TDB" in checks["mast time standard"].note
    assert checks["mast time reference"].note == "BJDREF 2457000.0"


def test_mast_quality_check_needs_a_lightcurve_kind_and_reports_unreadable(tmp_path):
    p = _write_spoc(tmp_path / "x_lc.fits")
    ref = ProductRef(archive="mast", product_id=p.name, format="spoc_lc")
    names = [c.name for c in base.get("mast").source_checks(T, ref, p)]      # no product mapping
    assert "MAST quality flags" not in names
    bad = tmp_path / "bad_lc.fits"
    bad.write_bytes(b"not a fits file")
    checks = {c.name: c for c in base.get("mast").source_checks(T, ref, bad, {"kind": "lightcurve"})}
    assert checks["MAST quality flags"].state == "failed" and checks["mast readable"].state == "failed"

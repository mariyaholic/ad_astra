"""Seams of ``cygnus.multi.archives.base`` (offline; the registry is restored after each test)."""

from __future__ import annotations

import io
import json
from pathlib import Path

import numpy as np
import pytest

from cygnus.multi.archives import base
from cygnus.multi.archives.base import (AdapterError, AdapterUnavailable, ArchiveAdapter, ProductRef, SourceCheck,
                                        Target)


@pytest.fixture(autouse=True)
def _isolated(monkeypatch):
    """No real network, and a private copy of the registry so test adapters never leak."""
    import urllib.request

    import requests

    def boom(*a, **k):
        raise AssertionError("real network call attempted")

    monkeypatch.setattr(requests.sessions.Session, "request", boom)
    monkeypatch.setattr(urllib.request, "urlopen", boom)
    monkeypatch.setattr(base, "_REGISTRY", dict(base._REGISTRY))
    monkeypatch.setattr(base, "_FACTORIES", dict(base._FACTORIES))


class _Dummy(ArchiveAdapter):
    name = "dummy_test"
    description = "test adapter"
    formats = ("csv", "fits_image", "text", "mystery")

    def discover(self, target, *, limit=5, **opts):
        return []


class _Resp:
    def __init__(self, text="", status=200):
        self.text, self.status_code = text, status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


# ---------------------------------------------------------------------------- fetch
def test_fetch_uses_the_injected_fetch_fn(tmp_path):
    seen = []

    def fetch_fn(ref, dest):
        seen.append((ref.product_id, dest))
        return str(dest)

    ref = ProductRef(archive="dummy_test", product_id="p", url="https://example.invalid/p")
    out = _Dummy(fetch_fn=fetch_fn).fetch(ref, tmp_path / "p")
    assert isinstance(out, Path) and out == tmp_path / "p" and seen == [("p", tmp_path / "p")]


def test_fetch_without_url_is_an_adapter_error(tmp_path):
    with pytest.raises(AdapterError, match="dummy_test:p: no URL"):
        _Dummy().fetch(ProductRef(archive="dummy_test", product_id="p", url=None), tmp_path / "p")


def test_default_fetch_delegates_to_the_shared_downloader(tmp_path, monkeypatch):
    import cygnus.ingest.netio as netio

    seen = {}

    def fake(url, dest, *, timeout_s):
        seen.update(url=url, dest=dest, timeout_s=timeout_s)
        Path(dest).write_bytes(b"x")
        return {}

    monkeypatch.setattr(netio, "fetch_to_file", fake)
    ref = ProductRef(archive="dummy_test", product_id="p", url="https://example.invalid/p")
    out = _Dummy().fetch(ref, tmp_path / "p.bin", timeout_s=7.0)
    assert out == tmp_path / "p.bin" and out.read_bytes() == b"x"
    assert seen == {"url": "https://example.invalid/p", "dest": tmp_path / "p.bin", "timeout_s": 7.0}


def test_default_fetch_streams_through_netio_to_disk(tmp_path, monkeypatch):
    """The real ``fetch_to_file`` path with a faked session: streamed, .part renamed into place."""
    import cygnus.ingest.netio as netio

    calls = []

    class _Stream:
        status_code = 200

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def raise_for_status(self):
            pass

        def iter_content(self, chunk_size):
            yield b"SIMPLE"
            yield b""
            yield b"  = T"

    class _Sess:
        def request(self, method, url, **kw):
            calls.append((method, url, kw["stream"], kw["timeout"]))
            return _Stream()

    monkeypatch.setattr(netio, "session", lambda: _Sess())
    ref = ProductRef(archive="dummy_test", product_id="p", url="https://example.invalid/p.fits")
    out = _Dummy().fetch(ref, tmp_path / "d" / "p.fits", timeout_s=5.0)
    assert out.read_bytes() == b"SIMPLE  = T"
    assert calls == [("GET", "https://example.invalid/p.fits", True, 5.0)]
    assert not (tmp_path / "d" / "p.fits.part").exists()


# ---------------------------------------------------------------------------- read
def test_read_dispatches_through_the_readers(tmp_path):
    from astropy.io import fits

    c = tmp_path / "t.csv"
    c.write_text("a,b\n1,2\n", encoding="utf-8")
    tab = _Dummy().read(c, ProductRef(archive="dummy_test", product_id="t", format="csv"))
    assert tab["columns"] == ["a", "b"] and tab["rows"] == [{"a": "1", "b": "2"}]

    t = tmp_path / "t.txt"
    t.write_text("hello", encoding="utf-8")
    assert _Dummy().read(t, ProductRef(archive="dummy_test", product_id="t", format="text")) == {"text": "hello"}

    f = tmp_path / "i.fits"
    fits.PrimaryHDU(np.ones((3, 4))).writeto(f)
    img = _Dummy().read(f, ProductRef(archive="dummy_test", product_id="i", format="fits_image"))
    assert img["shape"] == (3, 4)

    from cygnus.multi.readers import ReaderError

    with pytest.raises(ReaderError, match="unknown product format"):
        _Dummy().read(t, ProductRef(archive="dummy_test", product_id="t", format="mystery"))


# ---------------------------------------------------------------------------- source-check dispatch
def test_default_source_checks_dispatch_by_kind(tmp_path, monkeypatch):
    from cygnus.multi import source_checks as sc

    seen = []
    for fn in ("table_checks", "image_checks", "lightcurve_checks", "json_checks", "text_checks"):
        monkeypatch.setattr(sc, fn, lambda *a, _fn=fn, **k: seen.append((_fn, k)) or [SourceCheck(_fn, "passed")])
    d = _Dummy()
    p = tmp_path / "x"

    def run(fmt, product=None):
        seen.clear()
        d.source_checks(None, ProductRef(archive="dummy_test", product_id="x", format=fmt), p, product)
        return seen[0]

    assert run("csv") == ("table_checks", {"kind": "dummy_test catalogue"})
    assert run("fits_image") == ("image_checks", {"source": "dummy_test"})
    assert run("spoc_lc") == ("lightcurve_checks", {"fmt": "spoc_lc", "source": "dummy_test"})
    assert run("text") == ("text_checks", {"source": "dummy_test"})
    # the product record's kind overrides the format's kind; json of kind text goes to json_checks
    assert run("json", {"kind": "text"}) == ("json_checks", {"source": "dummy_test"})
    assert run("csv", {"kind": "image"})[0] == "image_checks"
    # unknown formats fall back to the light-curve kind
    assert run("mystery")[0] == "lightcurve_checks"


def test_text_check_dispatch_on_a_real_file(tmp_path):
    p = tmp_path / "t.txt"
    p.write_text("reachable", encoding="utf-8")
    checks = _Dummy().source_checks(None, ProductRef(archive="dummy_test", product_id="t", format="text"), p)
    assert [(c.name, c.state) for c in checks] == [("dummy_test payload", "passed")]
    assert "'reachable'" in checks[0].note


def test_capabilities_list_is_derived_from_formats():
    assert _Dummy().capabilities_list() == ["catalog", "image", "context", "lightcurve"]

    class _Declared(_Dummy):
        capabilities = ("observing",)

    assert _Declared().capabilities_list() == ["observing"]


# ---------------------------------------------------------------------------- http helpers
def test_http_helpers_use_the_injected_seam():
    calls = []

    def http(url, **kw):
        calls.append((url, kw))
        return "R"

    d = _Dummy(http=http)
    assert d.http_get("u", params={"a": 1}, timeout=3) == "R"
    assert d.http_post("u", {"b": 2}, timeout=4, headers={"h": "v"}) == "R"
    assert d.http_get_body("u", {"desigs": ["x"]}, timeout=5) == "R"
    assert calls[0] == ("u", {"params": {"a": 1}, "timeout": 3, "headers": None})
    assert calls[1] == ("u", {"data": {"b": 2}, "timeout": 4, "headers": {"h": "v"}})
    assert calls[2] == ("u", {"data": '{"desigs": ["x"]}', "headers": {"Content-Type": "application/json"},
                              "timeout": 5})


def test_http_helpers_fall_back_to_a_session():
    class _S:
        def __init__(self):
            self.calls = []

        def get(self, url, **kw):
            self.calls.append(("get", url, kw))
            return "G"

        def post(self, url, **kw):
            self.calls.append(("post", url, kw))
            return "P"

    s = _S()
    d = _Dummy(session=s)
    assert d.http_get("u", params={"q": 1}) == "G" and d.http_post("u", {"d": 1}) == "P"
    assert d.http_get_body("u", {"k": 1}) == "G"
    assert [c[0] for c in s.calls] == ["get", "post", "get"]
    assert s.calls[2][2]["data"] == '{"k": 1}'


def test_session_or_new_builds_a_requests_session_with_a_user_agent():
    import requests

    d = _Dummy()
    s = d._session_or_new()
    assert isinstance(s, requests.Session) and s.headers["User-Agent"].startswith("cygnus-multi/")
    assert d._session_or_new() is s


# ---------------------------------------------------------------------------- tap_csv
def test_tap_csv_posts_the_query_and_returns_rows():
    seen = {}

    def http(url, data=None, timeout=None, headers=None, params=None):
        seen.update(url=url, data=data, timeout=timeout)
        return _Resp("a,b\n1,x\n2,y\n")

    rows = _Dummy(http=http).tap_csv("https://tap.invalid/sync", "SELECT 1", timeout=9)
    assert rows == [{"a": "1", "b": "x"}, {"a": "2", "b": "y"}]
    assert seen == {"url": "https://tap.invalid/sync", "timeout": 9,
                    "data": {"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": "SELECT 1"}}


def test_tap_csv_header_only_is_zero_rows():
    assert _Dummy(http=lambda *a, **k: _Resp("a,b\n")).tap_csv("u", "q") == []


@pytest.mark.parametrize("body", [
    '<?xml version="1.0"?><VOTABLE><RESOURCE type="results"><INFO name="QUERY_STATUS" value="ERROR">'
    "table not found</INFO></RESOURCE></VOTABLE>",
    "\n  <VOTABLE><INFO name=\"QUERY_STATUS\" value=\"ERROR\"/></VOTABLE>",
    "<html><body>Service temporarily unavailable</body></html>",
])
def test_tap_csv_refuses_a_200_xml_error_body(body):
    with pytest.raises(AdapterError, match="TAP error from u"):
        _Dummy(http=lambda *a, **k: _Resp(body)).tap_csv("u", "q")


@pytest.mark.parametrize("body", ["ERROR: Query failed: table \"foo\" does not exist\n", ""])
def test_tap_csv_refuses_a_200_text_error_body(body):
    with pytest.raises(AdapterError):
        _Dummy(http=lambda *a, **k: _Resp(body)).tap_csv("u", "q")


def test_tap_csv_http_error_propagates():
    with pytest.raises(RuntimeError, match="HTTP 500"):
        _Dummy(http=lambda *a, **k: _Resp("oops", status=500)).tap_csv("u", "q")


def test_a_tap_error_body_makes_a_catalogue_adapter_unavailable_not_empty():
    body = '<VOTABLE><INFO name="QUERY_STATUS" value="ERROR"/></VOTABLE>'
    with pytest.raises(AdapterUnavailable):
        base.get("vizier", http=lambda *a, **k: _Resp(body)).discover(Target(name="x", ra_deg=1, dec_deg=2))


# ---------------------------------------------------------------------------- registry
def test_register_class_and_instance():
    assert base.register(_Dummy) is _Dummy
    assert "dummy_test" in base.available()
    a = base.get("dummy_test")
    assert isinstance(a, _Dummy) and base.get("dummy_test") is a          # cached on first use

    class _Inst(_Dummy):
        name = "dummy_inst"

    inst = _Inst(http=lambda *a, **k: None)
    assert base.register(inst) is _Inst
    assert base.get("dummy_inst") is inst
    fresh = base.get("dummy_inst", session="S")                          # kwargs build a new instance of the type
    assert type(fresh) is _Inst and fresh is not inst and fresh._session == "S"
    assert base.get("dummy_inst") is inst


def test_register_refuses_nameless_adapters():
    class _NoName(_Dummy):
        name = ""

    with pytest.raises(ValueError, match="has no name"):
        base.register(_NoName)
    with pytest.raises(ValueError, match="instance has no name"):
        base.register(_NoName())


def test_get_with_kwargs_on_a_factory_does_not_cache():
    base.register(_Dummy)
    base._REGISTRY.pop("dummy_test", None)
    a = base.get("dummy_test", http=lambda *x, **k: None)
    assert "dummy_test" not in base._REGISTRY and a._http is not None
    assert base.get("dummy_test") is not a


def test_all_adapters_available_and_summary_agree():
    base.register(_Dummy)
    names = base.available()
    assert names == sorted(names) and "dummy_test" in names and "mast" in names
    allad = base.all_adapters()
    assert list(allad) == names and all(isinstance(v, ArchiveAdapter) for v in allad.values())
    rows = {r["name"]: r for r in base.summary()}
    assert list(rows) == names
    assert rows["dummy_test"] == {"name": "dummy_test", "description": "test adapter",
                                  "formats": ["csv", "fits_image", "text", "mystery"],
                                  "capabilities": ["catalog", "image", "context", "lightcurve"], "verified": "[K]"}


# ---------------------------------------------------------------------------- products and targets
def test_as_products_does_not_invent_fields():
    refs = base.as_products([
        {"product_id": 12, "sector": 3},
        {"product_id": "b", "url": "u", "format": "fits_image", "description": 5, "expected_sha256": "ab",
         "size_bytes": 10, "survey": "DSS"},
        {"product_id": "c", "format": "csv", "kind": "text"},
    ], "arch", "spoc_lc")
    a, b, c = refs
    assert (a.product_id, a.url, a.format, a.kind, a.description, a.expected_sha256, a.size_bytes) == \
        ("12", None, "spoc_lc", "lightcurve", "", None, None)
    assert dict(a.extra) == {"sector": 3}
    assert (b.format, b.kind, b.description, b.expected_sha256, b.size_bytes) == ("fits_image", "image", "5", "ab", 10)
    assert dict(b.extra) == {"survey": "DSS"}
    assert c.kind == "text"                                              # explicit kind wins over the format's
    assert all(r.archive == "arch" for r in refs)
    assert base.as_products([], "arch", "csv") == []
    d = b.as_dict()
    assert d["extra"] == {"survey": "DSS"} and d["kind"] == "image" and json.dumps(d)


@pytest.mark.parametrize("fmt,kind", [("spoc_lc", "lightcurve"), ("ztf_lc", "lightcurve"), ("fits_cube", "image"),
                                      ("votable", "table"), ("json", "table"), ("text", "text"),
                                      ("fits_table", "lightcurve"), ("never-heard-of-it", "lightcurve"), ("", "lightcurve")])
def test_kind_for_format(fmt, kind):
    assert base.kind_for_format(fmt) == kind


def test_target_from_mapping_edge_cases():
    t = Target.from_mapping({"name": 42, "ra_deg": "10.5", "dec_deg": -3, "tic": "", "t0_bjd": "abc",
                             "period_days": None, "depth_ppm": "150", "duration_h": 2, "mag": 11.0,
                             "frame": "ICRS", "epoch": "J2000.0"})
    assert t.name == "42" and t.ra_deg == 10.5 and t.dec_deg == -3.0
    assert t.tic is None and t.t0_bjd is None and t.period_days is None
    assert t.depth_ppm == 150.0 and t.duration_h == 2.0 and t.mag == 11.0
    assert dict(t.extra) == {"frame": "ICRS", "epoch": "J2000.0"}
    # tmag takes precedence over mag; tic None is None; an int-like tic is converted
    t2 = Target.from_mapping({"name": "x", "ra_deg": 0, "dec_deg": 0, "tic": None, "tmag": "9.5", "mag": 11})
    assert t2.tic is None and t2.mag == 9.5 and dict(t2.extra) == {}
    assert Target.from_mapping({"name": "x", "ra_deg": 0, "dec_deg": 0, "tic": 7.0}).tic == 7
    # tmag explicitly None falls back to mag
    assert Target.from_mapping({"name": "x", "ra_deg": 0, "dec_deg": 0, "tmag": None, "mag": "12"}).mag == 12.0
    with pytest.raises(KeyError):
        Target.from_mapping({"ra_deg": 0, "dec_deg": 0})
    with pytest.raises(ValueError):
        Target.from_mapping({"name": "x", "ra_deg": "north", "dec_deg": 0})


def test_source_check_and_productref_serialise():
    assert SourceCheck("n", "not_tested").as_dict() == {"name": "n", "state": "not_tested", "note": ""}
    r = ProductRef(archive="a", product_id="p")
    assert (r.format, r.kind, r.url) == ("fits_table", "lightcurve", None) and r.as_dict()["extra"] == {}

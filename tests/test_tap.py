"""Byte-safe TAP client: VOTable normalization, retry and sync->async fallback (no network).

A fake ``requests.Session`` supplies byte-exact responses; ``time.sleep`` is frozen so the
retry/backoff paths are exercised without delay.
"""

from __future__ import annotations

import pytest

requests = pytest.importorskip("requests")
pytest.importorskip("astropy")

from cygnus.ingest import tap  # noqa: E402


class FakeResponse:
    def __init__(self, status_code: int = 200, content: bytes = b"", text: str = "", headers=None):
        self.status_code = status_code
        self.content = content
        self.text = text
        self.headers = headers or {}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")


class FakeSession:
    def __init__(self, *, gets=(), posts=()):
        self._gets = list(gets)
        self._posts = list(posts)
        self.calls = {"get": 0, "post": 0, "delete": 0}

    def get(self, url, **kw):
        self.calls["get"] += 1
        return self._gets.pop(0) if self._gets else FakeResponse(200, b"a,b\n1,2\n")

    def post(self, url, **kw):
        self.calls["post"] += 1
        return self._posts.pop(0)

    def delete(self, url, **kw):
        self.calls["delete"] += 1
        return FakeResponse(204)


VOT = (b'<?xml version="1.0" encoding="UTF-8"?>'
       b'<VOTABLE version="1.3" xmlns="http://www.ivoa.net/xml/VOTable/v1.3">'
       b'<RESOURCE type="results"><TABLE><FIELD name="a" datatype="int"/>'
       b'<DATA><TABLEDATA><TR><TD>1</TD></TR></TABLEDATA></DATA></TABLE></RESOURCE></VOTABLE>')


def test_normalize_adds_encoding_and_repairs_lone_bytes():
    assert tap.normalize_votable_bytes(b"<VOTABLE/>").startswith(b'<?xml version="1.0" encoding="UTF-8"?>')
    declared = tap.normalize_votable_bytes(b'<?xml version="1.0"?><VOTABLE/>')
    assert b'encoding="UTF-8"' in declared
    repaired = tap.normalize_votable_bytes(b'<?xml version="1.0" encoding="UTF-8"?><VOTABLE>\xa0</VOTABLE>')
    repaired.decode("utf-8")                      # must be valid UTF-8 now
    assert b"\xef\xbf\xbd" in repaired            # U+FFFD placeholder for the lone byte


def test_sync_retries_transient_http_and_parses_csv(monkeypatch):
    monkeypatch.setattr(tap.time, "sleep", lambda *_: None)
    sess = FakeSession(gets=[FakeResponse(503), FakeResponse(200, b"a,b\n1,2\n")])
    tab, status = tap.TapDirect("https://tap.example", sess=sess).sync_table("SELECT 1")
    assert list(tab["a"]) == [1] and "200" in status and sess.calls["get"] == 2


def test_sync_gives_up_after_retries(monkeypatch):
    monkeypatch.setattr(tap.time, "sleep", lambda *_: None)
    sess = FakeSession(gets=[FakeResponse(500), FakeResponse(500)])
    with pytest.raises(tap.TapDirectError, match="sync failed after 2 attempts"):
        tap.TapDirect("https://tap.example", sess=sess).sync_table("SELECT 1", max_retries=2)


def test_sync_parse_error_is_explicit(monkeypatch):
    monkeypatch.setattr(tap.time, "sleep", lambda *_: None)
    sess = FakeSession(gets=[FakeResponse(200, b"not a votable document")])
    with pytest.raises(tap.TapDirectError, match="sync parse failed"):
        tap.TapDirect("https://tap.example", sess=sess).sync_table("SELECT 1", fmt="votable")


def test_async_follows_redirect_polls_and_deletes():
    sess = FakeSession(
        posts=[FakeResponse(303, headers={"Location": "https://tap.example/async/123"})],
        gets=[FakeResponse(200, text="EXECUTING"), FakeResponse(200, text="COMPLETED"), FakeResponse(200, content=VOT)],
    )
    tab, status = tap.TapDirect("https://tap.example", sess=sess).async_table("SELECT 1", poll_s=0)
    assert list(tab["a"]) == [1] and "COMPLETED" in status and sess.calls["delete"] == 1


def test_async_error_phase_raises():
    sess = FakeSession(
        posts=[FakeResponse(303, headers={"Location": "https://tap.example/async/9"})],
        gets=[FakeResponse(200, text="ERROR")],
    )
    with pytest.raises(tap.TapDirectError, match="phase='ERROR'"):
        tap.TapDirect("https://tap.example", sess=sess).async_table("SELECT 1", poll_s=0)


def test_run_falls_back_to_async(monkeypatch):
    monkeypatch.setattr(tap.time, "sleep", lambda *_: None)
    sess = FakeSession(
        posts=[FakeResponse(303, headers={"Location": "https://tap.example/async/7"})],
        gets=[FakeResponse(500), FakeResponse(500), FakeResponse(500),
              FakeResponse(200, text="COMPLETED"), FakeResponse(200, content=VOT)],
    )
    tab, status, mode = tap.TapDirect("https://tap.example", sess=sess).run("SELECT 1", max_retries=3)
    assert mode == "async" and list(tab["a"]) == [1] and "COMPLETED" in status

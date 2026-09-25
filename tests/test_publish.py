"""Publication boundary, metadata mapping, access control and built-site UI checks.

All scientific content here is synthetic test fixture data inside ``tmp_path``;
nothing from these tests reaches the real ``publish/`` tree or the real site.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import threading
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

import pytest

try:
    import jinja2  # noqa: F401  (imported for its absence check)
    import yaml  # noqa: F401
except ImportError as exc:  # pragma: no cover
    if os.environ.get("CYGNUS_REQUIRE_SITE"):
        raise
    pytest.skip(f"site extra not installed ({exc}); set CYGNUS_REQUIRE_SITE=1 to fail instead",
                allow_module_level=True)

from cygnus.candidate_record import CandidateRecord  # noqa: E402
from cygnus.ledger import Ledger  # noqa: E402
from cygnus.publish import markdown  # noqa: E402
from cygnus.publish.build import BuildConfig, build_site  # noqa: E402
from cygnus.publish.safety import redact, resolve_source, scan_for_leaks, scan_text  # noqa: E402
from cygnus.publish.schema import PublicationError, parse_collection  # noqa: E402
from cygnus.publish.serve import make_server, safe_resolve  # noqa: E402
from cygnus.publish.snapshot import sanitize_row  # noqa: E402

PRIVATE_DOC = """# Fixture spec

Maintained: 2026-01-02 (UTC).

Bulk data goes to D:\\AO_Artifacts\\cygnus_scratch\\ and reports to cygnus:Cygnus/reports.
Contact someone@example.com. Archive: https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html

## Layer-2 module register

| Module | Function | Status |
| --- | --- | --- |
| `ingest/mast.py` | archive client | **implemented; live-verified 2026-01-01** |
| `domains/timeseries/detrend_lab.py` | detrending | designed — Sprint 1 |
"""

CAMPAIGN = """campaign: fx-01
domain: worlds.planetary.monotransit
status: draft          # queued; not yet executed
target_pool:
  source: manual
  targets: []
steps:
  - ingest.mast        # fetch
  - detrend_lab        # robustness
thresholds:
  fa_alpha: null       # calibrated later
storage:
  persistent: cygnus:Cygnus/
"""


def coll(cid: str, **kw) -> dict:
    base = {"id": cid, "title": f"Title {cid}", "type": "documents", "status": "published",
            "published": "2026-01-02", "summary": f"Summary {cid}", "items": []}
    base.update(kw)
    return base


# ------------------------------------------------------------------ fixtures
@pytest.fixture
def worktree(tmp_path: Path) -> Path:
    wt = tmp_path / "wt"
    (wt / "campaigns").mkdir(parents=True)
    (wt / "state").mkdir()
    (wt / "publish" / "collections").mkdir(parents=True)
    (wt / "publish" / "pages").mkdir()
    (wt / "publish" / "files").mkdir()
    (wt / "publish" / "candidates").mkdir()
    (wt / "SPEC.md").write_text(PRIVATE_DOC, encoding="utf-8")
    (wt / "campaigns" / "fx-01.yaml").write_text(CAMPAIGN, encoding="utf-8")
    (wt / "publish" / "pages" / "methods.md").write_text(
        "# Methods\n\n## Publication boundary\n\nSee [catalog](/data/catalog.json).\n", encoding="utf-8")
    (wt / "publish" / "files" / "table.csv").write_bytes(b"a,b\n1,2\n")
    (wt / "publish" / "files" / "secret.csv").write_text("x\n", encoding="utf-8")
    (wt / "publish" / "data" / "tier1-pack").mkdir(parents=True)
    (wt / "publish" / "data" / "tier1-pack" / "early.json").write_text(json.dumps({
        "service": "MAST", "pack_dir": "early", "source_manifest": "early/MANIFEST.json",
        "source_sha256": "0" * 64, "source_modified_utc": "2026-01-01T00:00:00Z",
        "snapshot_utc": "2026-01-02T00:00:00Z", "rows": [], "counts": {}, "held_bytes": 0,
    }), encoding="utf-8")
    (wt / "publish" / "site.json").write_text(json.dumps({
        "title": "Fixture Site", "short_title": "Fx", "subtitle": "test", "headline": "Fixture",
        "tagline": "Fixture tagline", "footer_note": "Fixture footer", "base_path": "/"}), encoding="utf-8")

    led = Ledger(wt / "state" / "ledger.sqlite")
    led.add_product("MAST", "prod-A", url="https://mast.stsci.edu/x", local_path=str(tmp_path / "private.fits"),
                    checksum="ab" * 32, license_="public MAST")
    run = led.log_run("fixture.run")
    led.add_measurement(run, "depth", "1200", unit="ppm", uncertainty="±150", method="box fit",
                        candidate_id="CYG-FX-0001", product_ids=["prod-A"])
    led.add_measurement(run, "rows", "10", unit="cadences", product_ids=["prod-A-missing"])
    led.close_run(run, "completed", summary="fixture")
    led.add_candidate("CYG-FX-0001", evidence_level="unverified_lead", summary="fixture dip")
    led.add_prior_art("VSX", "no match within 10\" as of 2026-01-01", gate="catalog",
                      query="cone 10as", candidate_id="CYG-FX-0001")
    led.close()

    CandidateRecord(
        candidate_id="CYG-FX-0001",
        provenance={"product": "MAST prod-A"},
        measured={"depth": {"value": 1200, "unit": "ppm", "uncertainty": "±150", "method": "box fit"}},
        audit={"centroid_shift": "passed", "scattered_light": "not_tested", "detrend_robustness": "inconclusive"},
        competing=["background eclipsing binary", "systematic"],
        reproduction={"code": "tests/fixture"},
        next_test="difference-image centroid",
        bottom_line="Synthetic fixture signal.",
    ).save(wt / "publish" / "candidates" / "CYG-FX-0001.json")

    colls = [
        coll("docs", items=[{"id": "spec", "kind": "document", "source": "SPEC.md", "download": True}],
             related=["campaign:fx-01", "collection:ghost"]),
        coll("camp", type="campaign", items=[{"id": "fx", "kind": "campaign", "source": "campaigns/fx-01.yaml", "download": True}]),
        coll("soft", type="software", items=[
            {"id": "reg", "kind": "module_register", "source": "SPEC.md"},
            {"id": "tbl", "kind": "file", "source": "publish/files/table.csv", "download": True},
            {"id": "sec", "kind": "file", "source": "publish/files/secret.csv", "access": "restricted",
             "access_note": "license pending"},
            {"id": "early", "kind": "archive_manifest", "source": "publish/data/tier1-pack/early.json",
             "access": "restricted", "access_note": "superseded by the later run"},
        ]),
        coll("runs", type="measurements", items=[{"id": "r1", "kind": "ledger_run", "params": {"run_id": 1}, "download": True}]),
        coll("cands", type="candidates", items=[{"id": "c1", "kind": "candidate",
                                                 "source": "publish/candidates/CYG-FX-0001.json", "download": True}]),
        coll("hidden-draft", status="draft", items=[{"id": "dd", "kind": "file", "source": "publish/files/secret.csv", "download": True}]),
        coll("gone", status="withdrawn", withdrawn={"date": "2026-01-03", "reason": "superseded"},
             items=[{"id": "gg", "kind": "file", "source": "publish/files/secret.csv", "download": True}]),
    ]
    for c in colls:
        (wt / "publish" / "collections" / f"{c['id']}.json").write_text(json.dumps(c), encoding="utf-8")
    return wt


def do_build(wt: Path) -> tuple[Path, object]:
    out = wt.parent / "site"
    res = build_site(BuildConfig(worktree=wt, out_dir=out, ledger=wt / "state" / "ledger.sqlite",
                                 build_utc="2026-01-04T00:00:00Z"))
    return out, res


@pytest.fixture
def built(worktree: Path):
    return (worktree, *do_build(worktree))


# ---------------------------------------------------------------- schema
@pytest.mark.parametrize("bad, needle", [
    (coll("Bad_ID"), "lowercase slug"),
    (coll("x1", status="live"), "status"),
    (coll("x1", published=None), "published"),
    (coll("x1", status="withdrawn"), "withdrawn.date"),
    (coll("x1", extra=1), "unknown keys"),
    (coll("x1", items=[{"id": "ff", "kind": "file", "source": "publish/files/a.exe"}]), "extension"),
    (coll("x1", items=[{"id": "ff", "kind": "file", "source": "publish/files/a.csv", "access": "restricted"}]), "access_note"),
    (coll("x1", items=[{"id": "ff", "kind": "file", "source": "publish/files/a.csv", "origin": "third_party", "download": True}]),
     "redistribution_ok"),
    (coll("x1", items=[{"id": "ff", "kind": "file", "source": "publish/files/a.csv"},
                       {"id": "ff", "kind": "file", "source": "publish/files/b.csv"}]), "duplicate"),
])
def test_schema_rejects(bad, needle):
    with pytest.raises(PublicationError, match=needle):
        parse_collection(bad)


def test_schema_accepts_third_party_with_recorded_redistribution():
    c = parse_collection(coll("x1", items=[{"id": "ff", "kind": "file", "source": "publish/files/a.csv",
                                            "origin": "third_party", "download": True, "redistribution_ok": True}]))
    assert c.items[0].redistribution_ok


# ---------------------------------------------------------------- path confinement
@pytest.mark.parametrize("kind, src", [
    ("document", "../outside.md"),
    ("document", "C:/Windows/win.md"),
    ("document", "/etc/passwd.md"),
    ("file", "state/ledger.sqlite"),
    ("file", "publish/files/../../SPEC.md"),
    ("document", "campaigns/nested.md"),          # documents: top level only
    ("file", "SPEC.md"),                           # files: publish/files only
    ("file", "publish/files/.env"),
    ("file", "publish/files/missing.csv"),
])
def test_resolve_source_rejects(worktree, kind, src):
    with pytest.raises(PublicationError):
        resolve_source(worktree, kind, src)


def test_resolve_source_allows_confined(worktree):
    assert resolve_source(worktree, "document", "SPEC.md").name == "SPEC.md"
    assert resolve_source(worktree, "file", "publish/files/table.csv").name == "table.csv"


# ---------------------------------------------------------------- redaction and leak scan
def test_redact_private_locations_but_not_urls():
    text = redact(PRIVATE_DOC + "\nworktree D:\\Ad Astra\\src and D:/AO_Artifacts/cygnus_scratch/venv\n")
    assert "AO_Artifacts" not in text and "cygnus:Cygnus" not in text and "Ad Astra" not in text
    assert "example.com" not in text
    assert "https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html" in text
    assert scan_text(text) == []


@pytest.mark.parametrize("leak", [
    r"C:\Users\x", "D:/AO_Artifacts/x", "cygnus:Cygnus/data", "client_secret = 'x'",
    "refresh_token: abc", "a@b.com",
])
def test_scan_text_flags(leak):
    assert scan_text(f"prefix {leak} suffix")


def test_scan_text_ignores_urls():
    assert scan_text("see https://gea.esac.esa.int/archive/ and mast:TESS/product/x") == []


# ---------------------------------------------------------------- markdown safety
def test_markdown_escapes_html_and_unsafe_links():
    r = markdown.render("# T\n\n<script>alert(1)</script> [x](javascript:alert(1)) **b** `<i>`")
    assert "<script>" not in r.html and "&lt;script&gt;" in r.html
    assert "javascript:" not in r.html
    assert "<strong>b</strong>" in r.html and "<code>&lt;i&gt;</code>" in r.html


def test_markdown_tables_lists_and_toc():
    r = markdown.render("# Title\n\n## A\n\n- one\n  - nested\n- two\n\n| h | k |\n| --- | --- |\n| `a|b` | 2 |\n",
                        demote_h1=True)
    assert r.title == "Title" and "<h1" not in r.html
    assert r.toc == [(2, "a", "A")]
    assert r.html.count("<ul>") == 2 and "<td><code>a|b</code></td>" in r.html


# ---------------------------------------------------------------- snapshot mapping
def test_snapshot_row_sanitized():
    row = {"service": "gaia", "pack_dir": "gaia", "product_id": "p1", "dest_rel": "x\\y.csv", "state": "drive_only",
           "bytes": "123", "sha256": "", "url": "https://gea.esac.esa.int/", "extra_json": json.dumps({"dest_rel": "a", "nrows": 5}),
           "note": "verified_md5@cygnus:Cygnus/data/tier1/02_gaia; local_deleted@2026-09-23T22:32:45Z"}
    out = sanitize_row(row)
    assert "dest_rel" not in out and "dest_rel" not in out["extra"]
    assert out["bytes"] == 123 and out["sha256"] is None           # missing stays missing
    assert out["extra"] == {"nrows": 5}
    assert out["note"].startswith("Upload verified") and "cygnus:" not in out["note"]


# ---------------------------------------------------------------- build: boundary
def test_build_publication_boundary(built):
    wt, out, res = built
    catalog = json.loads((out / "data" / "catalog.json").read_text(encoding="utf-8"))
    ids = {c["id"] for c in catalog["collections"]}
    assert ids == {"docs", "camp", "soft", "runs", "cands"}
    assert [w["id"] for w in catalog["withdrawn"]] == ["gone"]
    # draft: no page, no files, not in catalog
    assert not (out / "collections" / "hidden-draft").exists()
    assert not (out / "files" / "hidden-draft").exists()
    # withdrawn: tombstone page only
    tomb = (out / "collections" / "gone" / "index.html").read_text(encoding="utf-8")
    assert "withdrawn on" in tomb and "superseded" in tomb
    assert not (out / "files" / "gone").exists()
    # restricted file listed but never copied
    assert (out / "files" / "soft" / "tbl" / "table.csv").is_file()
    assert not list(out.rglob("secret.csv"))
    soft = (out / "collections" / "soft" / "index.html").read_text(encoding="utf-8")
    assert "license pending" in soft
    # unresolved related ref is dropped with a warning, not rendered
    assert any("collection:ghost" in w for w in res.warnings)


def test_build_never_leaks_private_values(built):
    wt, out, _ = built
    assert scan_for_leaks(out) == []
    everything = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in out.rglob("*") if p.is_file())
    assert "private.fits" not in everything          # ledger local_path never exported
    assert "local_path" not in everything
    doc = (out / "files" / "docs" / "spec" / "SPEC.md").read_text(encoding="utf-8")
    assert "[private path]" in doc and "[private Drive store]" in doc


def test_download_checksums_match_catalog(built):
    _, out, _ = built
    catalog = json.loads((out / "data" / "catalog.json").read_text(encoding="utf-8"))
    files = [f for c in catalog["collections"] for i in c["items"] for f in i["files"]]
    assert files
    for f in files:
        data = (out / f["url"].lstrip("/")).read_bytes()
        assert hashlib.sha256(data).hexdigest() == f["sha256"] and len(data) == f["bytes"]


def test_leak_in_unredacted_config_aborts_build(worktree):
    site = json.loads((worktree / "publish" / "site.json").read_text(encoding="utf-8"))
    site["footer_note"] = "mirror at D:\\AO_Artifacts\\x"
    (worktree / "publish" / "site.json").write_text(json.dumps(site), encoding="utf-8")
    with pytest.raises(PublicationError, match="leak scan failed"):
        do_build(worktree)
    assert not (worktree.parent / "site").exists()


def test_build_opens_ledger_read_only(worktree):
    path = worktree / "state" / "ledger.sqlite"
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    do_build(worktree)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == before
    led = Ledger.open_readonly(path)
    try:
        with pytest.raises(Exception):
            led.add_product("X", "y")
    finally:
        led.close()


def test_duplicate_page_ids_rejected(worktree):
    extra = coll("docs2", items=[{"id": "spec", "kind": "document", "source": "SPEC.md"}])
    (worktree / "publish" / "collections" / "docs2.json").write_text(json.dumps(extra), encoding="utf-8")
    with pytest.raises(PublicationError, match="claimed by both"):
        do_build(worktree)


# ---------------------------------------------------------------- build: candidate rules
def test_candidate_page_preserves_claim_rules(built):
    _, out, _ = built
    html = (out / "candidates" / "CYG-FX-0001" / "index.html").read_text(encoding="utf-8")
    assert "not an official" in html
    assert 'aria-current="step">Unverified lead' in html
    for state in ("state--passed", "state--not_tested", "state--inconclusive"):
        assert state in html
    assert "Not tested" in html and "Inconclusive" in html
    assert "±150" in html and "ppm" in html
    assert "VSX" in html and "as of" in html.lower()
    dossier = (out / "files" / "cands" / "c1" / "CYG-FX-0001-dossier.md").read_text(encoding="utf-8")
    assert "CYGNUS CANDIDATE DOSSIER" in dossier and "not an official designation" in dossier


def test_candidate_promotion_with_untested_audit_is_refused(worktree):
    path = worktree / "publish" / "candidates" / "CYG-FX-0001.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    raw["evidence_level"] = "vetted_candidate"
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(Exception, match="unverified_lead"):
        do_build(worktree)


def test_candidate_ledger_disagreement_is_refused(worktree):
    path = worktree / "publish" / "candidates" / "CYG-FX-0001.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    raw["evidence_level"] = "vetted_candidate"
    raw["audit"] = {k: "passed" for k in raw["audit"]}
    path.write_text(json.dumps(raw), encoding="utf-8")
    with pytest.raises(PublicationError, match="ledger says"):
        do_build(worktree)


def test_empty_candidates_state(worktree):
    (worktree / "publish" / "collections" / "cands.json").unlink()
    out, _ = do_build(worktree)
    html = (out / "candidates" / "index.html").read_text(encoding="utf-8")
    assert "No candidate dossiers have been published" in html
    assert "<strong>1</strong> candidate record" in html   # ledger count, reported not invented


# ---------------------------------------------------------------- build: metadata mapping
def test_campaign_draft_and_step_status(built):
    _, out, _ = built
    html = (out / "campaigns" / "fx-01" / "index.html").read_text(encoding="utf-8")
    assert "Draft campaign — no results" in html
    assert "queued; not yet executed" in html            # comment preserved from YAML
    assert "state--verified" in html and "state--planned" in html   # from module register
    assert "not set" in html                             # null threshold not invented


def test_restricted_archive_manifest_builds_without_a_manifest_bar(built):
    """A restricted manifest is listed with its note but must not crash or render as retrieved."""
    _, out, _ = built
    home = (out / "index.html").read_text(encoding="utf-8")
    assert ">early</a>" not in home
    soft = (out / "collections" / "soft" / "index.html").read_text(encoding="utf-8")
    assert "superseded by the later run" in soft


def test_every_published_campaign_step_resolves_to_a_register_row():
    """Executed steps must not render as "status unknown" on the public campaign pages."""
    from cygnus.publish import safety, sources

    wt = Path(__file__).resolve().parents[1]
    register = sources.load_module_register(wt / "ANALYSIS_STACK.md", "Layer-2 module register")
    unresolved = []
    checked = 0
    for coll in sorted((wt / "publish" / "collections").glob("*.json")):
        manifest = json.loads(coll.read_text(encoding="utf-8"))
        if manifest.get("status") != "published":
            continue                                     # drafts are not built into pages
        for item in manifest.get("items", []):
            if item.get("kind") != "campaign":
                continue
            path = safety.resolve_source(wt, "campaign", item["source"])
            camp = sources.load_campaign(path)
            for step in camp["steps"]:
                checked += 1
                if sources.module_for_step(step["name"], register) is None:
                    unresolved.append(f"{coll.name}: {item['id']}: {step['name']}")
    assert checked > 0
    assert unresolved == [], "campaign steps with no register row:\n" + "\n".join(unresolved)


def test_run_measurements_and_unresolved_products(built):
    _, out, _ = built
    html = (out / "collections" / "runs" / "index.html").read_text(encoding="utf-8")
    assert "prod-A-missing" in html and "unresolved" in html
    assert "https://mast.stsci.edu/x" in html


# ---------------------------------------------------------------- built UI: structure
class _PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.lang = None
        self.main = False
        self.skip = False
        self.imgs_without_alt = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if tag == "h1":
            self.h1 += 1
        if tag == "main":
            self.main = True
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
            if a.get("class") == "skip" and a["href"] == "#main":
                self.skip = True
        if tag == "img" and "alt" not in a:
            self.imgs_without_alt += 1


def test_every_page_is_structurally_sound_and_links_resolve(built):
    _, out, _ = built
    pages = sorted(out.rglob("*.html"))
    assert len(pages) >= 10
    for page in pages:
        audit = _PageAudit()
        audit.feed(page.read_text(encoding="utf-8"))
        rel = page.relative_to(out).as_posix()
        assert audit.lang == "en", rel
        assert audit.h1 == 1, rel
        assert audit.main and audit.skip, rel
        assert audit.imgs_without_alt == 0, rel
        for href in audit.links:
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, frag = href.partition("#")
            if not path:
                assert frag in audit.ids, f"{rel}: dangling #{frag}"
                continue
            target = out / path.lstrip("/")
            if path.endswith("/"):
                target = target / "index.html"
            assert target.is_file(), f"{rel}: broken link {href}"


def test_pages_use_only_self_hosted_assets(built):
    _, out, _ = built
    for page in out.rglob("*.html"):
        html = page.read_text(encoding="utf-8")
        for src in re.findall(r'(?:src|href)="([^"]+\.(?:css|js|svg))"', html):
            assert src.startswith("/static/"), f"{page.name}: external asset {src}"
        assert "style=" not in html, f"{page.name}: inline style breaks CSP"
        assert "<script>" not in html, f"{page.name}: inline script breaks CSP"


# ---------------------------------------------------------------- local server
@pytest.mark.parametrize("url", ["/../secret", "/%2e%2e/secret", "/files/..%2f..%2fx", "/.hidden",
                                 "/static/..\\x", "/C:/x", "/nope/"])
def test_safe_resolve_rejects(tmp_path, url):
    (tmp_path / "index.html").write_text("x")
    assert safe_resolve(tmp_path, url) is None


def test_server_serves_only_built_files(built):
    _, out, _ = built
    httpd = make_server(out, port=0)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/files/soft/tbl/table.csv") as r:
            assert r.status == 200 and r.read() == b"a,b\n1,2\n"
            assert "attachment" in r.headers["Content-Disposition"]
            assert "default-src 'self'" in r.headers["Content-Security-Policy"]
            assert r.headers["X-Content-Type-Options"] == "nosniff"
        for bad in ("/../wt/SPEC.md", "/files/soft/sec/secret.csv", "/collections/hidden-draft/"):
            with pytest.raises(urllib.error.HTTPError) as exc:
                urllib.request.urlopen(f"http://127.0.0.1:{port}{bad}")
            assert exc.value.code == 404
        req = urllib.request.Request(f"http://127.0.0.1:{port}/", data=b"x", method="POST")
        with pytest.raises(urllib.error.HTTPError) as exc:
            urllib.request.urlopen(req)
        assert exc.value.code == 405
    finally:
        httpd.shutdown()
        httpd.server_close()

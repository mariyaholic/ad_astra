"""Acquisition evidence is not a discovery or scientific tier promotion."""
from __future__ import annotations

import importlib.util
import json

import pytest


def scout():
    assert importlib.util.find_spec("cygnus.cloud_scout"), "cloud scouting/acquisition is missing"
    from cygnus import cloud_scout
    return cloud_scout


def config(**changes):
    return {"schema": "cygnus.scout/1", "bootstrap_top": 5, "field_limit": 1,
            "target_limit": 2, "rows_per_catalogue": 3, "products_per_source": 2,
            "sources": ["exoarchive", "gaia", "mast", "skyview", "koa"], **changes}


def toi(number=2, **changes):
    return {"toi": f"{number}.01", "tid": str(number), "tfopwg_disp": "PC", "ra": "10", "dec": "20",
            "pl_tranmid": "2459002", "pl_orbper": "20", "pl_trandep": "1000", "pl_trandurh": "2",
            "st_tmag": "11", "rowupdate": "2026-10-01", **changes}


def adapters(monkeypatch, calls, *, outage=False):
    from cygnus.multi.archives import base
    from cygnus.multi.archives.base import ArchiveAdapter, ProductRef

    class Adapter(ArchiveAdapter):
        def discover(self, target, *, limit=5, **kwargs):
            calls.append((self.name, target.name, kwargs))
            if self.name == "gaia":
                if outage:
                    raise RuntimeError("synthetic unavailable service")
                rows = self.tap_csv("https://example.invalid/tap", "SELECT synthetic_fixture")
                return [ProductRef("gaia", "cone.csv", format="csv", kind="table",
                                   extra={"inline": True, "rows": rows})]
            if self.name == "mast":
                return [ProductRef("mast", "synthetic-spoc.fits", "https://example.invalid/lc.fits",
                                   format="spoc_lc", kind="lightcurve")]
            if self.name == "koa":
                return [ProductRef("koa", "metadata.csv", format="table", kind="table",
                                   extra={"inline": True, "rows": [{"koaid": "synthetic"}]})]
            return []

        def tap_csv(self, endpoint, adql, **kwargs):
            return [{"source_id": "1234567890123456789", "ra": "10", "dec": "20", "ref_epoch": "2016.0"}]

    def get(name):
        obj = Adapter()
        obj.name = name
        return obj
    monkeypatch.setattr(base, "get", get)


def test_inventory_accounts_for_every_registered_source_without_fake_download_support():
    from cygnus.multi.archives.base import available
    module = scout()
    inventory = module.inventory()
    assert set(available()) <= set(inventory)
    assert inventory["mast"]["mode"] == "products"
    assert inventory["koa"]["mode"] == "metadata"
    assert inventory["earthdata"]["mode"] == "outside_scope"
    assert inventory["microobservatory"]["mode"] == "manual"
    assert inventory["esasky"]["mode"] == "manual"
    assert all(row["reason"] for row in inventory.values())


@pytest.mark.parametrize("change", [{"sources": ["typo"]}, {"field_limit": 0},
                                   {"bootstrap_top": 10001}, {"cone_arcsec": float("nan")},
                                   {"budget": {"product_mb": float("inf")}}])
def test_unbounded_or_unknown_scout_requests_are_rejected(change):
    with pytest.raises(ValueError):
        scout().normalize_config(config(**change))


def test_bootstrap_uses_fresh_bounded_catalogue_not_a_saved_queue(tmp_path):
    module = scout()
    seen = []
    result = module.bootstrap(module.normalize_config(config()), fetch=lambda query: (
        seen.append(query) or [toi(), toi(224), toi(3, ra="nan"), toi(5, pl_trandurh="-2")]))
    assert "TOP 5" in seen[0] and "FROM toi" in seen[0] and "ORDER BY" in seen[0]
    assert [t["name"] for t in result["targets"]] == ["TOI-2.01"]
    assert len(result["excluded"]) == 3
    assert result["queries"][0]["query"] == seen[0]
    assert result["targets"][0]["position_epoch"] == "J2015.5"


def test_catalogue_candidates_keep_source_ids_and_do_not_merge_by_position():
    module = scout()
    a = module.catalogue_targets("gaia", [{"source_id": "1234567890123456789", "ra": "10", "dec": "20"}], "field")
    b = module.catalogue_targets("simbad", [{"main_id": "different", "ra": "10", "dec": "20"}], "field")
    merged = module.merge_targets(a + a + b)
    assert len(merged) == 2
    assert merged[0]["source_id"] == "1234567890123456789"
    assert all(t["route"] != "transit" for t in merged)
    assert module.catalogue_targets("gaia", [{"source_id": "x", "ra": "nan", "dec": "20"}], "f") == []


def test_native_discovery_records_query_rows_and_outage_separately(tmp_path, monkeypatch):
    module = scout()
    calls = []
    adapters(monkeypatch, calls)
    target = module.bootstrap(module.normalize_config(config()), fetch=lambda q: [toi()])["targets"][0]
    result = module.discover({"source": "gaia", "target": target, "options": {"radius_arcsec": 30}, "limit": 3})
    assert result["state"] == "answered"
    assert result["queries"][0]["query"] == "SELECT synthetic_fixture"
    assert result["targets"][0]["source_id"] == "1234567890123456789"
    assert result["products"][0]["ref"]["extra"]["rows"]
    adapters(monkeypatch, calls, outage=True)
    failed = module.discover({"source": "gaia", "target": target, "options": {}, "limit": 3})
    assert failed["state"] == "unavailable" and not failed["products"]


def test_scout_reports_all_sources_and_preserves_products_and_routed_targets(tmp_path, monkeypatch):
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    calls = []
    adapters(monkeypatch, calls)
    monkeypatch.setattr(module, "bootstrap", lambda c: module._bootstrap(c, lambda q: [toi()]))
    receipt = module.scout(tmp_path, config(), executor=module.direct_executor)
    assert receipt["schema"] == "cygnus.scout_result/1"
    assert {t["source"] for t in receipt["targets"]} >= {"exoarchive", "gaia"}
    assert "earthdata" in receipt["sources"]
    assert receipt["sources"]["earthdata"]["state"] == "not_requested"
    assert any(p["ref"]["archive"] == "mast" for p in receipt["products"])
    assert any(name == "mast" for name, _, _ in calls)
    from cygnus.skyrecord import validate
    capsule = module.capsule(tmp_path, receipt)
    assert not validate(json.loads((capsule / "sky_record.json").read_text()), tmp_path)
    original = len(calls)
    again = module.scout(tmp_path, module.state_path(tmp_path, receipt) / "PLAN.json", executor=module.direct_executor)
    assert again == receipt and len(calls) == original
    path = next((capsule / "jobs").glob("*.json"))
    path.write_text("{}")
    with pytest.raises(ValueError, match="checkpoint|changed|hash"):
        module.scout(tmp_path, module.state_path(tmp_path, receipt) / "PLAN.json", executor=module.direct_executor)


def test_mast_image_discovery_uses_image_filter_and_image_reader():
    from cygnus.multi.archives.astronomy import MastAdapter
    from cygnus.multi.archives.base import Target
    calls = []
    adapter = MastAdapter()
    def mashup(service, params, **kwargs):
        calls.append(params)
        return {"data": [{"obsid": 1}]} if len(calls) == 1 else {"data": [
            {"productFilename": "jwst_synthetic_i2d.fits", "productSubGroupDescription": "I2D", "obs_collection": "JWST"}]}
    adapter._mashup = mashup
    refs = adapter.discover(Target("field", 10., 20.), collection="JWST", provenance="", subgroup="I2D",
                            radius_arcsec=30, dataproduct_type="image")
    assert next(f["values"] for f in calls[0]["filters"] if f["paramName"] == "dataproduct_type") == ["image"]
    assert refs[0].format == "fits_image" and refs[0].kind == "image"


def test_download_cap_does_not_accept_a_truncated_product(tmp_path, monkeypatch):
    from cygnus.fileio import atomic_write_text
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    def fetch(url, dest, **kwargs):
        assert kwargs["max_bytes"] == 1024
        atomic_write_text(dest, "truncated fixture")
        return {"truncated": True, "bytes": 1024}
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", fetch)
    product = {"target": {"name": "field", "ra_deg": 10., "dec_deg": 20.},
               "ref": {"archive": "mast", "product_id": "x.fits", "url": "https://example.invalid/x.fits",
                       "format": "fits_image", "kind": "image", "extra": {}}}
    result = module.fetch_product(product, tmp_path / "scratch/x.fits", 1024)
    assert result["state"] == "budget_stopped" and not result["eligible"]


def test_acquired_spoc_is_tic_bound_and_reused_by_cloud_plan(tmp_path, monkeypatch):
    from _multi_fixtures import write_spoc
    from astropy.io import fits
    from cygnus.fileio import sha256_file
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    target = module.bootstrap(module.normalize_config(config()), fetch=lambda q: [toi()])["targets"][0]
    product = {"target": target, "ref": {"archive": "mast", "product_id": "synthetic.fits",
        "url": "https://example.invalid/synthetic.fits", "format": "spoc_lc", "kind": "lightcurve", "extra": {}}}
    path = tmp_path / "scratch/data/synthetic.fits"
    def fetch(url, dest, **kwargs):
        write_spoc(dest, n=1728, cadence_s=600, bjdrefi=2459000, t_start=0, dips=[2.], sector=1)
        with fits.open(dest, mode="update") as hdus:
            hdus[0].header["TICID"] = 2
        return {"truncated": False, "bytes": dest.stat().st_size}
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", fetch)
    result = module.fetch_product(product, path, 1024**2)
    assert result["state"] == "downloaded" and result["eligible"]
    assert result["sha256"] == sha256_file(path)
    assert result["route"] == "transit"
    with fits.open(path, mode="update") as hdus:
        hdus[0].header["TICID"] = 3
    # A valid file is still not the requested target when its native identity differs.
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", lambda *a, **k: {"truncated": False})
    mismatch = module.fetch_product(product, path, 1024**2)
    assert not mismatch["eligible"] and mismatch["state"] == "identity_failed"


def test_acquisition_resume_and_transit_bridge_are_bound_to_downloaded_bytes(tmp_path, monkeypatch):
    from _multi_fixtures import write_spoc
    from astropy.io import fits
    from cygnus import cloud
    from cygnus.fileio import sha256_file
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    calls, downloads = [], []
    adapters(monkeypatch, calls)
    monkeypatch.setattr(module, "bootstrap", lambda c: module._bootstrap(c, lambda q: [toi()]))
    def fetch(url, dest, **kwargs):
        downloads.append(url)
        write_spoc(dest, n=1728, cadence_s=600, bjdrefi=2459000, t_start=0, dips=[2.], sector=1)
        with fits.open(dest, mode="update") as hdus:
            hdus[0].header["TICID"] = 2
        return {"truncated": False, "bytes": dest.stat().st_size}
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", fetch)
    found = module.scout(tmp_path, config(sources=["exoarchive", "mast"], mast_collections=["TESS"]),
                         executor=module.direct_executor)
    out = module.capsule(tmp_path, found)
    acquired = module.acquire(tmp_path, (out / "SCOUT.json").relative_to(tmp_path).as_posix(), executor=module.direct_executor)
    assert len(downloads) == 1 and acquired["products"][0]["eligible"]
    assert module.acquire(tmp_path, out / "SCOUT.json", executor=module.direct_executor) == acquired
    assert len(downloads) == 1
    cfg = module.bridge_config(tmp_path, {"schema": "cygnus.cloud/1", "queue": "unused.csv", "limit": 1,
                                         "max_tier": "T2"}, out / "ACQUISITION.json")
    plan = cloud.make_plan(tmp_path, cfg, refresh=lambda row: {**row,
        "catalogue_query": "synthetic exact-source recheck", "catalogue_retrieved_utc": found["targets"][0]["catalogue_retrieved_utc"]})
    worker_scratch = tmp_path / "scratch/worker"
    pins = module.seed_products(tmp_path, plan, "toi-2-01", worker_scratch)
    path = worker_scratch / "campaign_toi-2-01/synthetic-spoc.fits"
    assert len(pins) == 1 and pins[0]["expected_sha256"] == sha256_file(path)
    from cygnus.multi import runner, scaffold, steps
    from cygnus.fileio import atomic_write_json
    def native_run(spec_path, *, ledger, root):
        spec = runner.load_spec(spec_path)
        params = next(s["fetch_products"] for s in spec["steps"] if "fetch_products" in s)
        assert "from_targets" not in params and spec["input"]["products"] == pins
        ctx = runner.Context(spec, ledger, root)
        ctx.step = "fetch_products"
        got = steps.step_fetch_products(ctx, params)
        assert got["products"]["synthetic-spoc.fits"]["pinned"]
        assert not got["products"]["synthetic-spoc.fits"]["fetched_now"]
        runner.write_record(ctx, True)
        (ctx.outdir / "runner").mkdir()
        atomic_write_json(ctx.outdir / "runner/RUN_SUMMARY.json", {"complete": True})
    monkeypatch.setattr(runner, "run", native_run)
    monkeypatch.setattr(scaffold, "draft_report", lambda *a, **k: [])
    monkeypatch.setenv("CYGNUS_SCRATCH", str(worker_scratch))
    assert cloud.run_stage(tmp_path, plan, "toi-2-01", "screen")["status"] == "completed"
    assert len(downloads) == 1
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    source = module._verify_file(acquired["products"][0])
    source.write_bytes(b"corrupt")
    with pytest.raises(ValueError, match="changed|checksum|hash"):
        module.bridge_config(tmp_path, cfg, out / "ACQUISITION.json")


def test_modified_scout_summary_cannot_inject_unqueried_products(tmp_path, monkeypatch):
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    adapters(monkeypatch, [])
    monkeypatch.setattr(module, "bootstrap", lambda c: module._bootstrap(c, lambda q: [toi()]))
    found = module.scout(tmp_path, config(), executor=module.direct_executor)
    path = module.capsule(tmp_path, found) / "SCOUT.json"
    changed = json.loads(path.read_text())
    changed["products"] = []
    path.write_text(json.dumps(changed))
    with pytest.raises(ValueError, match="lineage|receipt|changed"):
        module.acquire(tmp_path, path, executor=module.direct_executor)


def test_named_solar_context_does_not_fabricate_a_sky_position(tmp_path, monkeypatch):
    from cygnus.multi.archives import base
    from cygnus.multi.archives.base import ArchiveAdapter
    module = scout()
    seen = []
    class Adapter(ArchiveAdapter):
        def discover(self, target, **kwargs):
            seen.append(target)
            return []
    monkeypatch.setattr(base, "get", lambda name: Adapter())
    result = module.discover({"source": "mpc", "target": {"name": "1 Ceres"}, "limit": 1, "options": {}})
    assert result["state"] == "answered_empty"
    assert seen[0].ra_deg is None and seen[0].dec_deg is None


def test_generated_cutout_is_a_plan_until_an_archive_request_answers():
    module = scout()
    result = module.discover({"source": "skyview", "target": {"name": "field", "ra_deg": 10., "dec_deg": 20.},
                              "limit": 1, "options": {"size_deg": .01, "pixels": 32}})
    assert result["state"] == "planned" and result["products"] and not result["queries"]


def test_skyview_resolves_a_download_url_instead_of_using_legacy_get(tmp_path, monkeypatch):
    from astroquery.skyview import SkyView
    from astropy.io import fits
    import numpy as np
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    queries, urls = [], []
    def resolve(position, survey, **kwargs):
        queries.append((position, survey, kwargs))
        return ["https://example.invalid/skyview-result.fits"]
    monkeypatch.setattr(SkyView, "get_image_list", resolve)
    def fetch(url, dest, **kwargs):
        urls.append(url)
        dest.parent.mkdir(parents=True, exist_ok=True)
        fits.PrimaryHDU(np.ones((32, 32))).writeto(dest)
        return {"truncated": False}
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", fetch)
    found = module.discover({"source": "skyview", "target": {"name": "field", "ra_deg": 10., "dec_deg": 20.},
                            "limit": 1, "options": {"size_deg": .01, "pixels": 32}})
    result = module.fetch_product(found["products"][0], tmp_path / "scratch/image.fits", 1024**2)
    assert result["state"] == "downloaded" and result["route"] == "image_review"
    assert urls == ["https://example.invalid/skyview-result.fits"]
    assert queries and any(r["operation"] == "skyview_image_list" for r in result["queries"])


def test_eso_download_selects_science_link_and_preserves_access_failure(tmp_path, monkeypatch):
    from astropy.table import Table
    from astropy.io import fits
    import numpy as np
    from cygnus.multi.archives import base
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    adapter = base.get("eso")
    class Response:
        content = b"synthetic VOTable seam"
        def raise_for_status(self):
            pass
    monkeypatch.setattr(adapter, "http_get", lambda *a, **k: Response())
    monkeypatch.setattr("cygnus.ingest.tap.parse_votable_bytes", lambda content: Table(
        rows=[("#auxiliary", "https://example.invalid/aux.fits"), ("#this", "https://example.invalid/science.fits")],
        names=["semantics", "access_url"]))
    selected = []
    def fetch(url, dest, **kwargs):
        selected.append(url)
        dest.parent.mkdir(parents=True, exist_ok=True)
        fits.PrimaryHDU(np.ones((10, 10))).writeto(dest)
        return {"truncated": False}
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", fetch)
    product = {"target": {"name": "field", "ra_deg": 10., "dec_deg": 20.}, "ref": {
        "archive": "eso", "product_id": "synthetic", "format": "fits_image", "kind": "image",
        "url": "https://example.invalid/datalink", "extra": {}}}
    result = module.fetch_product(product, tmp_path / "scratch/eso.fits", 1024**2)
    assert selected == ["https://example.invalid/science.fits"]
    assert result["state"] == "downloaded" and not result["eligible"]
    def forbidden(*a, **k):
        raise PermissionError("synthetic HTTP 401")
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", forbidden)
    assert module.fetch_product(product, tmp_path / "scratch/forbidden.fits", 1024**2)["state"] == "unavailable"


def test_real_supervised_worker_records_unavailable_without_a_completion_checkpoint(tmp_path, monkeypatch):
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    plan = module._plan(tmp_path, config())
    jobs = module.Jobs(tmp_path, plan)
    result = jobs.run({"kind": "discover", "source": "worldview", "target": {
        "name": "field", "ra_deg": 10., "dec_deg": 20.}, "limit": 1, "options": {}})
    assert result["state"] == "unavailable" and result["resource"]["state"] == "ok"
    assert not list((module.state_path(tmp_path, plan) / "checkpoints").glob("*.json"))


def test_download_size_mismatch_is_not_an_eligible_file(tmp_path, monkeypatch):
    from cygnus.fileio import atomic_write_text
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    def fetch(url, dest, **kwargs):
        atomic_write_text(dest, "short")
        return {"truncated": False}
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", fetch)
    product = {"target": {"name": "field", "ra_deg": 10., "dec_deg": 20.}, "ref": {
        "archive": "mast", "product_id": "x.fits", "url": "https://example.invalid/x.fits",
        "format": "fits_image", "kind": "image", "size_bytes": 100, "extra": {}}}
    result = module.fetch_product(product, tmp_path / "scratch/x.fits", 1024)
    assert result["state"] == "integrity_failed" and not result["eligible"]


def test_scout_summary_change_is_rejected_on_resume(tmp_path, monkeypatch):
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    adapters(monkeypatch, [])
    monkeypatch.setattr(module, "bootstrap", lambda c: module._bootstrap(c, lambda q: [toi()]))
    found = module.scout(tmp_path, config(), executor=module.direct_executor)
    (module.capsule(tmp_path, found) / "SCOUT.json").write_text("{}")
    with pytest.raises(ValueError, match="receipt|changed|hash"):
        module.scout(tmp_path, module.state_path(tmp_path, found) / "PLAN.json", executor=module.direct_executor)


def test_inline_koa_metadata_is_retained_as_a_table_without_raw_spectrum_claim(tmp_path, monkeypatch):
    module = scout()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    product = {"target": {"name": "field", "ra_deg": 10., "dec_deg": 20.}, "ref": {
        "archive": "koa", "product_id": "metadata.csv", "format": "table", "kind": "table", "url": None,
        "extra": {"inline": True, "rows": [{"koaid": "synthetic", "ra": 10., "dec": 20.}]}}}
    result = module.fetch_product(product, tmp_path / "scratch/metadata.csv", 1024**2)
    assert result["state"] == "downloaded" and result["route"] == "catalogue_review"
    assert not result["eligible"] and "synthetic" in (tmp_path / "scratch/metadata.csv").read_text()


def test_request_trace_restores_class_method_lookup_after_use(monkeypatch):
    from cygnus.multi.archives.spectroscopy import KoaAdapter
    from cygnus.multi.archives.base import ArchiveAdapter, Target
    module = scout()
    adapter = KoaAdapter()
    with module.trace(adapter, []):
        pass
    assert "tap_csv" not in adapter.__dict__
    seen = []
    def changed(self, endpoint, query, **kwargs):
        seen.append(query)
        return []
    monkeypatch.setattr(ArchiveAdapter, "tap_csv", changed)
    adapter.discover(Target("field", 10., 20.))
    assert seen and "koa_hires" in seen[0]

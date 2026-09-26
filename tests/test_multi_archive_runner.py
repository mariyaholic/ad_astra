"""End-to-end multi-archive runner test on a synthetic non-MAST light curve (offline).

This proves the copied pipeline can fetch and screen a generic archive product,
not only a MAST SPOC FITS light curve.
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np
import pytest

from cygnus.ledger import Ledger

pytest.importorskip("yaml")
pytest.importorskip("scipy")
fits = pytest.importorskip("astropy.io.fits")


@pytest.fixture(autouse=True)
def _isolated_registry(monkeypatch):
    """Test-registered adapters never leak: the doc-adapter-count test must pass in any file order."""
    from cygnus.multi.archives import base

    monkeypatch.setattr(base, "_REGISTRY", dict(base._REGISTRY))
    monkeypatch.setattr(base, "_FACTORIES", dict(base._FACTORIES))


def _csv_lc(path: Path, *, dip_at: float, depth: float = 0.03, seed: int = 1) -> None:
    rng = np.random.default_rng(seed)
    n = 6000
    t = 1500.0 + np.arange(n) * (120 / 86400)
    flux = 1000.0 * (1 + rng.normal(0, 0.001, n))
    flux[np.abs(t - dip_at) < 0.06] *= 1 - depth
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["TIME", "FLUX", "FLUX_CORR", "QUALITY"])
        for a, b, c in zip(t, flux, flux * 1.005):
            w.writerow([f"{a:.6f}", f"{b:.6f}", f"{c:.6f}", 0])


@pytest.fixture()
def world(tmp_path, monkeypatch):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    (tmp_path / "campaigns").mkdir()
    (tmp_path / "reports").mkdir()
    (tmp_path / "reports" / "multi").mkdir()
    (tmp_path / "reports" / "multi" / "REPORT.md").write_text("# multi\n", encoding="utf-8")
    return tmp_path


def test_multi_archive_fetch_and_screen(world, monkeypatch):
    from cygnus.multi import runner, steps
    from cygnus.multi.archives import base

    stage = world / "scratch" / "campaign_multi-archive"
    pid = "fake__synthetic-lc.csv"
    _csv_lc(stage / pid, dip_at=1505.0)
    sha = hashlib.sha256((stage / pid).read_bytes()).hexdigest()

    # a fake registered archive discovers exactly this staged product
    class FakeAdapter(base.ArchiveAdapter):
        name = "fake"
        description = "synthetic test archive"
        formats = ("csv_lc",)

        def discover(self, target, *, limit=5, **opts):
            return [base.ProductRef(archive="fake", product_id="synthetic-lc.csv", url="http://invalid",
                                    format="csv_lc", expected_sha256=sha, description="synthetic")]

    base.register(FakeAdapter)

    spec = f"""schema: cygnus.campaign/1
campaign_id: multi-archive
objective: synthetic multi-archive
outputs: reports/multi/
random_seed: 3
targets:
  - name: FakeTarget
    ra_deg: 10.0
    dec_deg: 20.0
    frame: ICRS
    epoch: J2000.0
    position_source: fixture
    t0_bjd: 1505.0
    duration_h: 2.0
    depth_ppm: 30000
veto: {{kind: single_epoch, veto_hours: 12}}
steps:
  - fetch_products: {{from_targets: {{archives: [fake], max_products_per_target: 1}}}}
  - residual_screen: {{windows_days: [1.0, 2.0], k_mad: 5.0}}
  - known_signal_recovery: {{k_mad: 5.0, epoch_tolerance_hours: 2.0}}
record:
  path: reports/multi/sky_record.json
  title: Multi-archive fixture
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/multi/REPORT.md
  summary: Synthetic multi-archive screen.
  checks:
    - {{name: "Pixel-level audit", state: not_tested}}
"""
    spec_path = world / "campaigns" / "multi-archive.yaml"
    spec_path.write_text(spec, encoding="utf-8")

    led = Ledger(world / "ledger.sqlite")
    out = runner.run(spec_path, ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"], out
    prods = json.loads((world / "reports/multi/runner/fetch_products.json").read_text())["result"]["products"]
    [entry] = prods.values()
    assert entry["archive"] == "fake" and entry["format"] == "csv_lc"
    # the product was ledgered under its own archive, not MAST
    assert led.count_products("fake") == 1 and led.count_products("MAST") == 0
    # the screen ran on the generic product and found the planted dip (inside the known-signal veto)
    screen_path = next((world / "reports/multi").rglob("screen.json"))
    screen = json.loads(screen_path.read_text())
    entries = screen.get("screened_excursions", [])
    assert entries and all(abs(e["mid_time_BJD_like"] - 1505.0) < 0.1 for e in entries)
    assert screen["input"]["file"].endswith(".csv")
    # the generic reader records which columns became SAP and PDCSAP
    known = json.loads((world / "reports/multi/runner/known_signal_recovery.json").read_text())["result"]
    ep = next(iter(known["per_product"].values()))["epochs"][0]
    assert ep["state"] == "recovered" and 20000 < ep["measured_depth_ppm"] < 40000
    # the record names the archive it used
    rec = json.loads((world / "reports/multi/sky_record.json").read_text())
    assert rec["products"][0]["archive"] == "fake"
    assert rec["status"] == "completed"


def test_mast_pinned_path_unchanged(world):
    """A pinned MAST product still uses the exact old SPOC reader and MAST archive."""
    from cygnus.multi import runner

    stage = world / "scratch" / "stage"
    pid = "tess-fixture-s0007-0000000000000001-s_lc.fits"

    rng = np.random.default_rng(1)
    n = 4000
    t = 1500.0 + np.arange(n) * (120 / 86400)
    flux = 1000.0 * (1 + rng.normal(0, 0.001, n))
    cols = [fits.Column(name=nm, format="D", array=a) for nm, a in
            (("TIME", t), ("SAP_FLUX", flux * 1.01), ("PDCSAP_FLUX", flux))] + \
           [fits.Column(name="QUALITY", format="J", array=np.zeros(n, int))]
    hdu0 = fits.PrimaryHDU()
    hdu0.header.update({"OBJECT": "TIC 1", "TICID": 1, "SECTOR": 7, "TIMEDEL": 120 / 86400, "RA_OBJ": 10.0, "DEC_OBJ": 20.0})
    tab = fits.BinTableHDU.from_columns(cols)
    tab.header.update({"BJDREFI": 2457000, "BJDREFF": 0.0, "TIMESYS": "TDB", "TIMEUNIT": "d"})
    stage.mkdir(parents=True, exist_ok=True)
    fits.HDUList([hdu0, tab]).writeto(stage / pid)
    sha = hashlib.sha256((stage / pid).read_bytes()).hexdigest()

    spec = f"""schema: cygnus.campaign/1
campaign_id: mast-pinned
objective: pinned MAST
outputs: reports/mast-pinned/
random_seed: 3
targets:
  - name: Fixture
    ra_deg: 10.0
    dec_deg: 20.0
    frame: ICRS
    epoch: J2000.0
    position_source: fixture
    t0_bjd: 1505.0
input:
  products: [{{product_id: {pid}, target: Fixture, sector: 7, expected_sha256: {sha}}}]
veto: {{kind: single_epoch, veto_hours: 12}}
steps:
  - fetch_products: {{search_dirs: ["scratch:stage"]}}
  - residual_screen: {{windows_days: [1.0], k_mad: 5.0}}
record:
  path: reports/mast-pinned/sky_record.json
  title: Pinned MAST
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/mast-pinned/REPORT.md
  summary: Synthetic pinned MAST.
  checks:
    - {{name: "Pixel-level audit", state: not_tested}}
"""
    (world / "reports" / "mast-pinned").mkdir()
    (world / "reports" / "mast-pinned" / "REPORT.md").write_text("# m\n", encoding="utf-8")
    spec_path = world / "campaigns" / "mast-pinned.yaml"
    spec_path.write_text(spec, encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    out = runner.run(spec_path, ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"]
    prods = json.loads((world / "reports/mast-pinned/runner/fetch_products.json").read_text())["result"]["products"]
    assert prods[pid]["archive"] == "MAST" and prods[pid]["format"] == "spoc_lc"
    assert led.count_products("MAST") == 1


def test_mixed_products_screen_only_the_lightcurve(world):
    """A campaign fetching a light curve plus a Gaia-style table screens the curve and records the table."""
    from cygnus.multi import runner
    from cygnus.multi.archives import base

    stage = world / "scratch" / "campaign_mixed-products"
    lc_pid = "mixed__lc.csv"
    table_pid = "mixed__gaia.csv"
    _csv_lc(stage / lc_pid, dip_at=1505.0)
    (stage / table_pid).write_text("source_id,ra,dec\n1,10.0,20.0\n", encoding="utf-8")

    class MixedAdapter(base.ArchiveAdapter):
        name = "mixed"
        description = "synthetic mixed archive"
        formats = ("csv_lc", "csv")

        def discover(self, target, *, limit=5, **opts):
            return [
                base.ProductRef(archive="mixed", product_id="lc.csv", url=None, format="csv_lc",
                                kind="lightcurve", description="synthetic light curve"),
                base.ProductRef(archive="mixed", product_id="gaia.csv", url=None, format="csv",
                                kind="table", description="synthetic neighbour table"),
            ]

    base.register(MixedAdapter)

    spec = """schema: cygnus.campaign/1
campaign_id: mixed-products
objective: mixed product kinds
outputs: reports/mixed/
random_seed: 3
targets:
  - name: MixedTarget
    ra_deg: 10.0
    dec_deg: 20.0
    frame: ICRS
    epoch: J2000.0
    position_source: fixture
    t0_bjd: 1505.0
    duration_h: 2.0
veto: {kind: single_epoch, veto_hours: 12}
steps:
  - fetch_products: {from_targets: {archives: [mixed], max_products_per_target: 2}}
  - context_products: {}
  - source_checks: {}
  - residual_screen: {windows_days: [1.0], k_mad: 5.0}
record:
  path: reports/mixed/sky_record.json
  title: Mixed fixture
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/mixed/REPORT.md
  summary: Synthetic mixed-product screen.
  checks:
    - {name: "Pixel-level audit", state: not_tested}
"""
    (world / "reports" / "mixed").mkdir()
    (world / "reports" / "mixed" / "REPORT.md").write_text("# m\n", encoding="utf-8")
    p = world / "campaigns" / "mixed-products.yaml"
    p.write_text(spec, encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    out = runner.run(p, ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"]
    fetch = json.loads((world / "reports/mixed/runner/fetch_products.json").read_text())["result"]
    assert fetch["lightcurve_products"] == ["lc.csv"]
    # both products are ledgered, under their own archive
    assert led.count_products("mixed") == 2
    # the screen only saw the light curve
    screen = json.loads(next((world / "reports/mixed").rglob("screen.json")).read_text())
    assert screen["input"]["file"].endswith("lc.csv")
    # the table was read as context, not screened
    ctx = json.loads((world / "reports/mixed/context.json").read_text())
    assert list(ctx) == ["gaia.csv"] and ctx["gaia.csv"]["n_rows"] == 1
    checks = {c["name"]: c["state"] for c in
              json.loads((world / "reports/mixed/sky_record.json").read_text())["checks"]}
    assert checks["Context products read"] == "passed"
    # per-source checks ran for each product and are recorded
    src = json.loads((world / "reports/mixed/source_checks.json").read_text())
    assert set(src) == {"lc.csv", "gaia.csv"} and all(v for v in src.values())
    lc_checks = {c["name"]: c["state"] for c in src["lc.csv"]}
    assert lc_checks["mixed usable cadences"] == "passed"
    assert lc_checks["mixed time standard"] == "not_tested"      # a CSV carries no TIMESYS
    # the archive-level state is not_tested because the time standard is genuinely unestablished
    assert checks["Source checks (mixed)"] == "not_tested"


def _csv_lc_single(path: Path, *, dip_at: float, second_at: float | None = None,
                   depth: float = 0.02, seed: int = 2) -> None:
    rng = np.random.default_rng(seed)
    n = 6000
    t = 1500.0 + np.arange(n) * (120 / 86400)
    flux = 1000.0 * (1 + rng.normal(0, 0.001, n))
    flux[np.abs(t - dip_at) < 0.06] *= 1 - depth
    if second_at is not None:
        flux[np.abs(t - second_at) < 0.06] *= 1 - depth
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["TIME", "FLUX", "QUALITY"])
        for a, b in zip(t, flux):
            w.writerow([f"{a:.6f}", f"{b:.6f}", 0])


def test_single_channel_product_screened_without_independence_claim(world):
    """A one-channel archive product is screened once, and the record says independence was lost."""
    from cygnus.multi import runner
    from cygnus.multi.archives import base

    stage = world / "scratch" / "campaign_single-channel"
    pid = "single__lc.csv"
    _csv_lc_single(stage / pid, dip_at=1505.0, second_at=1506.5)   # second dip outside the veto and inside the span

    class SingleAdapter(base.ArchiveAdapter):
        name = "single"
        description = "synthetic single-channel archive"
        formats = ("csv_lc",)

        def discover(self, target, *, limit=5, **opts):
            return [base.ProductRef(archive="single", product_id="lc.csv", url=None, format="csv_lc",
                                    kind="lightcurve", description="single-channel light curve")]

    base.register(SingleAdapter)

    spec = """schema: cygnus.campaign/1
campaign_id: single-channel
objective: single-channel screening
outputs: reports/single/
random_seed: 5
targets:
  - name: SingleTarget
    ra_deg: 10.0
    dec_deg: 20.0
    frame: ICRS
    epoch: J2000.0
    position_source: fixture
    t0_bjd: 1505.0
    duration_h: 2.0
    depth_ppm: 20000
veto: {kind: single_epoch, veto_hours: 12}
steps:
  - fetch_products: {from_targets: {archives: [single], max_products_per_target: 1}}
  - calibrate_screen: {declared_k: 5.0, k_grid: [3.0, 4.0, 5.0], depths_ppm: [2000, 20000],
                        durations_h: [2.0], injections_per_cell: 4, reference_signal: {depth_ppm: 20000, duration_h: 2.0}}
  - residual_screen: {windows_days: [1.0, 2.0, 3.0], k_mad: 5.0}
  - known_signal_recovery: {k_mad: 5.0, epoch_tolerance_hours: 2.0}
record:
  path: reports/single/sky_record.json
  title: Single-channel fixture
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/single/REPORT.md
  summary: Synthetic single-channel screen.
  checks:
    - {name: "Pixel-level audit", state: not_tested}
"""
    (world / "reports" / "single").mkdir()
    (world / "reports" / "single" / "REPORT.md").write_text("# s\n", encoding="utf-8")
    p = world / "campaigns" / "single-channel.yaml"
    p.write_text(spec, encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    out = runner.run(p, ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"]
    screen = json.loads(next((world / "reports/single").rglob("screen.json")).read_text())
    assert screen["channel_mode"].startswith("single channel")
    assert screen["channels"]["independent"] is False and screen["channels"]["all"] == ["FLUX"]
    entries = screen.get("screened_excursions", [])
    assert entries and all(e["flux_type"] == "FLUX" for e in entries)   # screened once, not twice
    summary = json.loads((world / "reports/single/runner/residual_screen.json").read_text())["result"]
    [per] = summary["per_product"].values()
    assert per["channel_mode"] == "single"
    events = per["distinct_events_outside_veto"]
    if events:   # the planted dip is the catalogued epoch and is vetoed, so this may be empty
        assert all("single channel" in e["persistence_basis"] for e in events)
    cal = json.loads((world / "reports/single/runner/calibrate_screen.json").read_text())["result"]
    assert next(iter(cal["per_product"].values()))["channel_mode"] == "single"
    known = json.loads((world / "reports/single/runner/known_signal_recovery.json").read_text())["result"]
    ep = next(iter(known["per_product"].values()))["epochs"][0]
    assert ep["state"] == "recovered" and ep["flux_types"] == ["FLUX"]
    # the red-noise model assessed the non-vetoed event instead of a false channel comparison
    checks = {c["name"]: c["state"] for c in
              json.loads((world / "reports/single/sky_record.json").read_text())["checks"]}
    assert checks["Single-channel event significance (red noise)"] == "passed"
    model = screen["systematics_model"]
    assert model["strongest"] is not None and model["strongest"]["tau_days"] is not None


def test_source_checks_fail_visibly_on_an_unreadable_product(world):
    """A fetched product that cannot be read yields a failed source check, never 'passed'."""
    from cygnus.multi import runner
    from cygnus.multi.archives import base

    stage = world / "scratch" / "campaign_source-checks"
    pid = "bad__lc.csv"
    stage.mkdir(parents=True, exist_ok=True)
    (stage / pid).write_text("not,a,lightcurve\n", encoding="utf-8")

    class BadAdapter(base.ArchiveAdapter):
        name = "bad"
        description = "synthetic malformed archive"
        formats = ("csv_lc",)

        def discover(self, target, *, limit=5, **opts):
            return [base.ProductRef(archive="bad", product_id="lc.csv", url=None, format="csv_lc",
                                    kind="lightcurve", description="malformed")]

    base.register(BadAdapter)
    spec = """schema: cygnus.campaign/1
campaign_id: source-checks
objective: source check failure
outputs: reports/source-checks/
random_seed: 1
targets:
  - name: BadTarget
    ra_deg: 10.0
    dec_deg: 20.0
    frame: ICRS
    epoch: J2000.0
    position_source: fixture
steps:
  - fetch_products: {from_targets: {archives: [bad], max_products_per_target: 1}}
  - source_checks: {}
record:
  path: reports/source-checks/sky_record.json
  title: Source-check fixture
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/source-checks/REPORT.md
  summary: Synthetic.
  checks:
    - {name: "Pixel-level audit", state: not_tested}
"""
    (world / "reports" / "source-checks").mkdir()
    (world / "reports" / "source-checks" / "REPORT.md").write_text("# c\n", encoding="utf-8")
    p = world / "campaigns" / "source-checks.yaml"
    p.write_text(spec, encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    out = runner.run(p, ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"]
    checks = {c["name"]: c["state"] for c in
              json.loads((world / "reports/source-checks/sky_record.json").read_text())["checks"]}
    assert checks["Source checks (bad)"] == "failed"


def test_astrometric_vetting_step_flags_a_known_companion(world, monkeypatch):
    """The NSS step marks a target with a significant Gaia solution as already explained."""
    from cygnus.multi import runner
    from cygnus.multi.archives import base

    class _R:
        def __init__(self, text):
            self.text = text

        def raise_for_status(self):
            pass

    source = "source_id,ra,dec,phot_g_mean_mag,parallax\n111,10.0001,20.0,12.0,1.5\n"
    head = ("source_id,nss_solution_type,ra,dec,parallax,period,period_error,eccentricity,eccentricity_error,"
            "semi_amplitude_primary,semi_amplitude_primary_error,mass_ratio,inclination,inclination_error,"
            "significance,goodness_of_fit,flags,astrometric_jitter\n")
    row = "111,SB1,10.0001,20.0,1.5,100.0,0.1,0.2,0.01,10.0,0.1,0.3,80.0,2.0,20.0,1.1,0,0.2\n"

    def http(url, data=None, timeout=None, headers=None):
        is_nss = "nss_two_body_orbit" in (data or {}).get("QUERY", "")
        return _R(head + row if is_nss else source)

    fake_gaia = base.get("gaia", http=http)
    real_get = base.get
    monkeypatch.setattr(base, "get", lambda name, **kw: fake_gaia if name == "gaia" else real_get(name, **kw))

    spec = """schema: cygnus.campaign/1
campaign_id: nss-vetting
objective: astrometric vetting
outputs: reports/nss/
random_seed: 1
targets:
  - name: NssTarget
    ra_deg: 10.0
    dec_deg: 20.0
    frame: ICRS
    epoch: J2000.0
    position_source: fixture
steps:
  - astrometric_vetting: {radius_arcsec: 5, significance_min: 5}
record:
  path: reports/nss/sky_record.json
  title: NSS fixture
  kind: astrometric vetting
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/nss/REPORT.md
  summary: Synthetic NSS vetting.
  checks:
    - {name: "Pixel-level audit", state: not_tested}
"""
    (world / "reports" / "nss").mkdir()
    (world / "reports" / "nss" / "REPORT.md").write_text("# n\n", encoding="utf-8")
    p = world / "campaigns" / "nss-vetting.yaml"
    p.write_text(spec, encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    out = runner.run(p, ledger=led, root=world, echo=lambda *_: None)
    assert out["complete"]
    checks = {c["name"]: c["state"] for c in
              json.loads((world / "reports/nss/sky_record.json").read_text())["checks"]}
    assert checks["Gaia NSS astrometric vetting"] == "failed"
    nss_out = json.loads((world / "reports/nss/nss.json").read_text())
    assert nss_out["NssTarget"]["nss_solutions"] == 1
    assert nss_out["NssTarget"]["top_mass_function_msun"] > 0


def test_archive_unavailable_is_recorded_not_empty(world):
    """When an adapter is unavailable, fetch_products notes it rather than silently producing nothing."""
    from cygnus.multi import runner

    spec = """schema: cygnus.campaign/1
campaign_id: unavailable
objective: unavailable archive
outputs: reports/unavailable/
random_seed: 1
targets:
  - name: X
    ra_deg: 1.0
    dec_deg: 2.0
    frame: ICRS
    epoch: J2000.0
    position_source: fixture
steps:
  - fetch_products: {from_targets: {archives: [asf], max_products_per_target: 1}}
record:
  path: reports/unavailable/sky_record.json
  title: Unavailable
  kind: residual screen
  outcome: bounded_null
  date: "2026-01-02"
  report: reports/unavailable/REPORT.md
  summary: Synthetic.
  checks:
    - {name: "Pixel-level audit", state: not_tested}
"""
    (world / "reports" / "unavailable").mkdir()
    (world / "reports" / "unavailable" / "REPORT.md").write_text("# u\n", encoding="utf-8")
    p = world / "campaigns" / "unavailable.yaml"
    p.write_text(spec, encoding="utf-8")
    led = Ledger(world / "ledger.sqlite")
    with pytest.raises(RuntimeError, match="no products") as ei:
        runner.run(p, ledger=led, root=world, echo=lambda *_: None)
    assert "asf" in str(ei.value) and "unavailable" in str(ei.value)
    [run] = led.runs()
    assert run["status"] == "failed" and "asf" in run["summary"]
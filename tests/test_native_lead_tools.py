"""Native versions of the 2026-09-30 lead-resolution tools: synthetic controls and failure-mode rules."""

import gzip
import json

import numpy as np
import pytest

from cygnus.analysis import events, localize, prf, rv, spectra
from cygnus.campaign import reconcile as rc
from cygnus.fileio import archive_previous, atomic_write_json, sha256_file
from cygnus.ingest import access


def lc(dip=0.0, n=3000, cad=0.002, seed=1):
    r = np.random.default_rng(seed)
    t = np.arange(n) * cad
    y = 1.0 + 1e-4 * r.standard_normal(n) + 2e-3 * (t - t.mean())
    return t, y * np.where(np.abs(t - 3.0) < 0.05, 1 - dip, 1.0)


def test_box_measure_recovers_depth_and_flags_gap_as_uncovered():
    t, y = lc(dip=0.01)
    m = events.box_measure(t, y, 3.0, 0.1, 2)
    assert m["state"] == "measured" and abs(m["depth_ppm"] - 1e4) < 800
    keep = np.abs(t - 3.0) > 0.06
    assert events.box_measure(t[keep], y[keep], 3.0, 0.1, 2)["state"] == "uncovered"


def test_null_counts_have_finite_resolution_and_injection_excludes_uncovered():
    t, y = lc()
    nul = events.null_exceedance(t, y, 0.1, 2, 5000, centres=[1.5, 2.0, 4.0, 9999.0])
    assert nul["n_covered"] == 3 and nul["n_exceed"] == 0 and nul["resolution"] == pytest.approx(1 / 3)
    inj = events.injection_recovery(t, y, 0.1, 2, 1e4, epochs=[1.5, 2.5, 9999.0])
    assert inj["n_covered"] == 2 and inj["n_recovered"] == 2


def test_alias_with_no_covered_window_stays_untested_not_excluded():
    t, y = lc(dip=0.01)
    out = events.classify_aliases([3.0, 1.0], [(0.0, 6.0)], t, y, 0.1, 2, 1e4, epoch0=3.0)
    by = {o["period_days"]: o for o in out}
    assert by[3.0]["status"] == "present" or by[3.0]["status"] == "excluded"
    far = events.classify_aliases([100.0], [(50.0, 60.0)], t, y, 0.1, 2, 1e4, epoch0=0.0)
    assert far[0]["status"] == "untested"


def test_prf_preference_flip_is_inconclusive():
    g = np.exp(-0.5 * ((np.arange(117) - 58) / 9.0) ** 2)
    image = np.outer(g, g)
    a = prf.source_model(image, (11, 11), 5.0, 5.0)
    b = prf.source_model(image, (11, 11), 5.15, 5.0)
    res = prf.profile_source_preference(a + b * 0.98, np.full(a.shape, 0.02), image,
                                        {"A": (5.0, 5.0), "B": (5.15, 5.0)}, shifts=[(0, 0)])
    assert res["state"] in ("inconclusive", "single_preference") and set(res["per_floor"]) == {"0.01", "0.03", "0.05"}
    sole = prf.profile_source_preference(a, np.full(a.shape, 0.01), image,
                                         {"A": (5.0, 5.0), "far": (8.0, 8.0)}, shifts=[(0, 0)])
    assert sole["state"] == "single_preference" and sole["per_floor"]["0.03"]["best"] == "A"


def test_rv_transit_tied_units_and_amplitude():
    t = np.linspace(0, 100, 30)
    tmpl = rv.rv_template(t, 50.0, 10.0)
    assert abs(rv.rv_template(np.array([10.0]), 50.0, 10.0)[0]) < 1e-9
    r = rv.rv_linear_fit(35.0 * tmpl + 5.0, np.full(30, 0.01), tmpl, np.ones((30, 1)))
    assert r["semiamplitude_kms"] == pytest.approx(35.0, abs=1e-6)
    out = rv.fit_transit_tied_orbit(t, 35 * tmpl, np.full(30, 0.1), 10.0, [50.0, 40.0], fwhm=np.sin(t))
    assert out["rv_fwhm_correlation"] is not None and all(f["dof"] >= 1 for f in out["fits"])
    assert min(out["fits"], key=lambda f: f["chi2"])["period_days"] == 50.0


def test_precision_gate_blocks_promotion():
    ok = spectra.precision_gate([0, 1.0, 2.0], [0, 1.001, 2.002])
    assert ok["state"] == "passed"
    bad = spectra.precision_gate([0, 1.0, 2.0], [0, 1.2, 2.3])
    assert bad["state"] == "failed"
    with pytest.raises(PermissionError):
        spectra.require_gate(bad)
    assert spectra.precision_gate([0, 1], [0, 1])["state"] == "not_tested"


def test_spectral_shift_and_mask_ccf_roundtrip():
    v = np.arange(-400, 400, 0.5)
    tmpl = 1 - 0.3 * np.exp(-0.5 * ((v - 0) / 8) ** 2)
    obs = np.interp(v - 3.4, v, tmpl)
    assert spectra.spectral_shift(v, tmpl, obs) == pytest.approx(3.4, abs=0.02)
    w = np.arange(4800.0, 4806.0, 0.002)
    c = 4803.0 * np.sqrt((1 + 20 / spectra.C_KMS) / (1 - 20 / spectra.C_KMS))
    flux = 1 - 0.4 * np.exp(-0.5 * ((w - c) / 0.055) ** 2)
    vel = np.arange(-80, 80.01, 0.2)
    fit = spectra.fit_mask_ccf(vel, spectra.integrated_mask_ccf(w, flux, np.array([[4802.98, 4803.02]]), vel))
    assert fit["center_kms"] == pytest.approx(20.0, abs=0.02)


def test_block_bootstrap_never_passes():
    r = np.random.default_rng(0)
    cube = 100 + r.standard_normal((80, 7, 7))
    ev = np.zeros(80, bool); ev[30:50] = True
    cube[ev, 3, 3] -= 30
    ap = np.zeros((7, 7), bool); ap[2:5, 2:5] = True
    bg = np.zeros((7, 7), bool); bg[0, :] = True
    res = localize.block_bootstrap_offset(cube, ev, ~ev, ap, bg, flux_unit="e-/s", draws=40, block=5)
    assert res["state"] in ("inconclusive", "failed_localization")


def test_gate_helpers():
    assert rc.check_units_ppm(7000, "7 ppt") == [] and rc.check_units_ppm(7000, "7%")
    assert rc.check_null_counts(0, 400, claims_probability_zero=True)
    assert rc.check_centroid(4.7, True) == "failed_localization"
    assert rc.check_centroid(None, True) == "not_tested"
    assert rc.check_event_times([2459092.18], [("planet b", 2459092.2)])
    assert rc.check_radius(7000, 0.5, 20.0)


def test_atomic_write_history_and_hash_link(tmp_path):
    src = tmp_path / "in.txt"; src.write_text("x")
    out = tmp_path / "o.json"
    atomic_write_json(out, {"a": 1}, inputs={"in": src})
    assert json.loads(out.read_text())["_provenance"]["input_sha256"]["in"] == sha256_file(src)
    with pytest.raises(ValueError):
        atomic_write_json(out, {"a": float("nan")})
    assert json.loads(out.read_text())["a"] == 1 and not list(tmp_path.glob(".*tmp"))
    h1 = archive_previous(out, "pre rerun", today="2026-09-30")
    out.write_text("{}"); h2 = archive_previous(out, "pre rerun", today="2026-09-30")
    assert h1.exists() and h2.exists() and h1 != h2


def test_access_states_and_sniffing():
    assert access.classify_error(status=401) == "http_401"
    assert access.classify_error(TimeoutError()) == "timeout"
    with pytest.raises(ValueError):
        access.ProductAccess("p", state="gone")
    assert access.sniff_container(gzip.compress(b"abc" * 100)) == "gzip"
    assert access.sniff_container(b"SIMPLE  =") == "fits"

    class R:
        closed = False
        def iter_content(self, chunk_size): yield from (b"a" * 10 for _ in range(100))
        def close(self): self.closed = True
    r = R(); data, digest = access.capped_stream(r, 25)
    assert len(data) == 25 and r.closed and len(digest) == 64


def test_reconcile_footer_idempotent_and_drift(tmp_path):
    c = tmp_path / "campaigns" / "x"; c.mkdir(parents=True)
    (c / "REPORT.md").write_text("# r\n")
    assert rc.add_history_footer(c / "REPORT.md", "note", "reports/y") is True
    assert rc.add_history_footer(c / "REPORT.md", "note", "reports/y") is False
    (c / "sky_record.json").write_text(json.dumps({"evidence": "Vetted candidate",
        "checks": [{"name": "k", "state": "passed"}]}))
    (tmp_path / "publish" / "candidates").mkdir(parents=True); (tmp_path / "publish" / "collections").mkdir()
    (tmp_path / "publish" / "candidates" / "CID.json").write_text(json.dumps({"evidence_level": "Unverified lead"}))
    f = rc.check_records(tmp_path, "x", "CID")
    assert any("evidence level" in s for s in f) and any("passed without" in s for s in f)


def test_paper_match_cannot_identify_source_without_time_match():
    r = rc.paper_match("Zhang 2024", companion_exists=True, event_time_matched=False, event_source_identified=True)
    assert r["companion_exists"] and not r["event_source_identified"]


def test_eso_exact_name_and_koa_queries_offline():
    from cygnus.multi.archives import base
    seen = []

    def fake(self, url, adql, **k):
        seen.append(adql)
        return []
    base.ArchiveAdapter.tap_csv, orig = fake, base.ArchiveAdapter.tap_csv
    try:
        t = base.Target.from_mapping({"name": "T", "ra_deg": 10.0, "dec_deg": -3.0})
        base.get("eso").discover(t, names=["HD 80133", "O'x"])
        base.get("koa").discover(t)
    finally:
        base.ArchiveAdapter.tap_csv = orig
    assert "target_name IN ('HD 80133', 'O''x')" in seen[0] and "koa_hires" in seen[1]


def _chk(**kw):
    return [{"name": n.replace("_", " "), "state": st} for n, st in kw.items()]


T1_OK = [("Period aliases (repeat events)", "passed"), ("Catalogue cross-match", "passed"),
         ("Event-time comparison vs published ephemerides", "inconclusive"),
         ("Calibrated false-alarm threshold (sign-flip null)", "passed"),
         ("Moving objects at screen-event epochs", "passed")]


def _rec(extra=(), outcome="lead", evidence="Unverified lead", base=T1_OK, **top):
    return {"status": "completed", "outcome": outcome, "evidence": evidence, **top,
            "checks": [{"name": n, "state": st} for n, st in [*base, *extra]]}


NULLS = [("Event-epoch null exceedance (k/N)", "passed")]
LOC_OK = [("Vetting difference-image localization (E1)", "passed"), ("Blend and dilution census (Gaia DR3 cone)", "passed"),
          *NULLS]


def test_tiers_gate_by_record_state():
    from cygnus.campaign import tiers as T
    assert T.decide(_rec(base=(), outcome="pipeline_check", evidence=None)).tier == "T0"
    d = T.decide(_rec(base=[]))
    assert d.tier == "T1" and len(d.blockers) >= 4
    assert T.decide(_rec()).tier == "T2"                                   # T1 gates met, no localization yet
    assert T.decide(_rec(LOC_OK)).tier == "T3"
    # the event-epoch null (k/N) gates T3; the event-depth injection-recovery gates T4
    assert T.decide(_rec([b for b in LOC_OK if b not in NULLS])).tier == "T2"
    assert T.decide(_rec([*LOC_OK[:-1], ("Event-epoch null exceedance (k/N)", "inconclusive")])).tier == "T2"
    # position-only match never clears: drop the event-time comparison and it falls back to T1
    no_time = [b for b in T1_OK if not b[0].startswith("Event-time")]
    assert T.decide(_rec(LOC_OK, base=no_time)).tier == "T1"
    # spec must state a budget and a discriminating question for T3
    assert T.decide(_rec(LOC_OK), spec={}).tier == "T2"
    assert T.decide(_rec(LOC_OK), spec={"budget": {"mb": 500}, "discriminating_question": "which star?"}).tier == "T3"
    # same-pixel 'independent' reduction must not lift T3 -> T4; a real independent-sky check does
    same = LOC_OK + [("Independent cached TPF localization (2026-09-27)", "passed")]
    assert T.decide(_rec(same, evidence="Vetted candidate")).tier == "T3"
    sky = same + [("Independent-epoch confirmation (ZTF)", "passed")]
    assert T.decide(_rec(sky, evidence="Vetted candidate")).tier == "T3"          # no injection-recovery yet
    d4 = T.decide(_rec(sky + [("Event-depth injection-recovery", "passed")], evidence="Vetted candidate"))
    assert d4.tier == "T4" and d4.needs_approval == "user go-ahead"
    with pytest.raises(PermissionError):
        T.require_tier(_rec(base=(), outcome="pipeline_check", evidence=None), "T3")


def test_localization_is_per_event_and_rejected_events_do_not_block():
    from cygnus.campaign import tiers as T
    e = [("Vetting difference-image localization (E1)", "passed"), ("Vetting difference-image localization (E2)", "failed"),
         ("Blend and dilution census (Gaia DR3 cone)", "passed")]
    assert T.decide(_rec(e)).tier == "T2"                                   # failed defining event blocks T3
    assert T.decide(_rec([*e, *NULLS], rejected_events=["E2"])).tier == "T3"           # artifact-rejected event is set aside
    # a failed same-pixel localization check still blocks even when the events pass
    assert T.decide(_rec(LOC_OK + [("Independent cached TPF localization (2026-09-27)", "failed")])).tier == "T2"
    # untouched template placeholder does not block once real localization exists
    assert T.decide(_rec(LOC_OK + [("Difference-image centroids / blend audit", "not_tested")])).tier == "T3"


def test_closing_rules_are_polarity_aware():
    from cygnus.campaign import tiers as T
    assert T.decide(_rec([("Published event-time identity (S34/S61)", "passed")])).tier == "closed"
    assert T.decide(_rec([("Variable-catalogue collision (VSX)", "failed")])).tier == "closed"
    assert T.decide(_rec([("Variable-catalogue collision (VSX)", "passed")])).tier != "closed"
    assert T.decide(_rec(), rejection_note=True).tier == "closed"
    # a failed pointing census demotes events; it does not close the target
    assert T.decide(_rec([("Pointing and quality census per event", "failed")])).tier == "T2"
    only = [("Vetting difference-image localization (E1)", "failed")]
    assert T.decide(_rec(only, rejected_events=["E1"])).tier == "closed"


def test_every_check_name_in_campaign_records_is_mapped():
    from pathlib import Path
    from cygnus.campaign import tiers as T
    from cygnus.skyrecord import load_records
    root = Path(__file__).resolve().parents[1]
    recs = [r for r in load_records(root) if r["_path"].startswith("campaigns/")]
    assert T.unmapped_checks(recs) == set()


def test_current_leads_match_reviewed_tiers():
    from pathlib import Path
    from cygnus.campaign import tiers as T
    root = Path(__file__).resolve().parents[1]
    got = {c: T.decide_campaign(root, c).tier for c in
           ("toi-224-01", "toi-2666-01", "toi-3500-02", "toi-6695-01", "toi-7610-01")}
    assert got == {"toi-224-01": "T2", "toi-2666-01": "T2", "toi-3500-02": "T2",
                   "toi-6695-01": "closed", "toi-7610-01": "closed"}


def test_step_gate_skips_and_override_is_recorded():
    from cygnus.campaign import tiers as T
    low = _rec()
    ok, msg = T.gate_step("spectra_download", low)
    assert not ok and "needs T3" in msg
    ok, msg = T.gate_step("spectra_download", low, {"tier": "T3", "reason": "user asked", "approved_by": "user"})
    assert ok and "override" in msg
    assert not T.gate_step("event_null", _rec(base=(), outcome="pipeline_check", evidence=None))[0]
    assert not T.gate_step("spectra_extract", _rec(LOC_OK), {"tier": "T4", "reason": "x"})[0]   # T4 needs approved_by
    assert T.gate_step("residual_screen", low) == (True, "")


def test_runner_tier_gate_reads_parent_record(tmp_path):
    import json
    from types import SimpleNamespace
    from cygnus.campaign import runner
    parent = tmp_path / "parent.json"
    parent.write_text(json.dumps(_rec()))
    ctx = SimpleNamespace(spec={"parent_record": "parent.json"}, root=tmp_path, outdir=tmp_path, checks={},
                          outcome=None, notes=[], note=lambda t: None)
    assert "needs T3" in runner._tier_gate(ctx, "rv_fit")
    assert runner._tier_gate(ctx, "residual_screen") is None
    ctx.spec["tier_override"] = {"tier": "T3", "reason": "approved", "approved_by": "user"}
    assert runner._tier_gate(ctx, "rv_fit") is None


def test_null_verdict_finite_resolution():
    v = events.null_verdict
    assert v(0, 300)["state"] == "passed" and v(0, 300)["resolution"] == pytest.approx(1 / 300)
    assert v(0, 40)["state"] == "inconclusive"            # 0/40 is not a strong null: resolution too coarse
    assert v(30, 300)["state"] == "failed"                # 10% of event-free windows as deep as the event
    assert v(0, 0)["state"] == "not_tested"


def test_event_null_step_runs_and_records_checks(tmp_path, monkeypatch):
    import json
    from types import SimpleNamespace
    from cygnus.campaign import steps
    r = np.random.default_rng(3)
    t = np.arange(0, 27, 0.002)
    flux = 1 + 2e-4 * r.standard_normal(t.size)
    flux[np.abs(t - 10.0) < 0.05] *= 1 - 0.01
    lc = SimpleNamespace(usable=np.ones(t.size, bool), time_bjd=t + 2457000.0, pdc=flux)
    monkeypatch.setattr(steps, "read_spoc", lambda path: lc)
    monkeypatch.setattr(steps, "resolve", lambda stored: stored)
    checks = {}
    ctx = SimpleNamespace(
        seed=1, outdir=tmp_path, spec={"veto": None}, checks=checks,
        rel=lambda p: str(p), check=lambda n, s, note: checks.__setitem__(n, (s, note)),
        optional_result=lambda name, default=None: {"candidates": [{"product": "p", "event_bjd": 2457010.0}]},
        result=lambda name: {"products": {"p": {"path": "x"}}})
    monkeypatch.setattr(steps, "_target_for", lambda c, pid: {"duration_h": 2.4})
    out = steps.step_event_null(ctx, {"n_null": 200, "n_inject": 100})
    e = out["events"][0]
    assert e["observed"]["depth_ppm"] > 7000 and e["null"]["n_exceed"] == 0
    assert checks["Event-epoch null exceedance (k/N)"][0] == "passed"
    assert checks["Event-depth injection-recovery"][0] in ("passed", "inconclusive")
    assert json.loads((tmp_path / "event_null.json").read_text())["events"]
    # a candidate whose event window is uncovered is not_tested, never passed
    lc2 = SimpleNamespace(usable=np.ones(t.size, bool), time_bjd=t + 2457000.0, pdc=flux)
    monkeypatch.setattr(steps, "read_spoc", lambda path: lc2)
    ctx.optional_result = lambda n, d=None: {"candidates": [{"product": "p", "event_bjd": 2457500.0}]}
    steps.step_event_null(ctx, {})
    assert checks["Event-epoch null exceedance (k/N)"][0] == "not_tested"

"""Cloud orchestration contracts; synthetic fixtures are not astronomical evidence."""
from __future__ import annotations

import csv
import importlib.util
import json
import sys

import pytest


def cloud():
    assert importlib.util.find_spec("cygnus.cloud") is not None, "gated cloud controller is missing"
    from cygnus import cloud
    return cloud


def pool(root):
    path = root / "queue.csv"
    rows = [{"name": name, "tic": tic, "rank": i, "ra_deg": 10., "dec_deg": 20.,
             "t0_bjd": 2459000., "period_days": 4., "duration_h": 2., "depth_ppm": 1000.,
             "tmag": 10., "rationale": "synthetic ordering"}
            for i, (name, tic) in enumerate([("TOI-224.01", 224), ("TOI-2.01", 2),
                                            ("TOI-3.01", 3), ("TOI-4.01", 4)], 1)]
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    return path


def config(**changes):
    return {"schema": "cygnus.cloud/1", "queue": "queue.csv", "limit": 2, "max_tier": "T3",
            "budget": {"scratch_mb": 128, "stage_seconds": 60, "run_seconds": 300, "min_free_mb": 1},
            "discriminating_question": "Which source and conditional orbit can explain the synthetic event?",
            **changes}


def refreshed(row):
    from cygnus.ledger import now_utc
    return {**row, "catalogue_query": "synthetic exact-identity query", "catalogue_retrieved_utc": now_utc(),
            "toi_rowupdate": "2026-10-01", "position_source": "synthetic fixture"}


def plan_fixture(tmp_path, refresh=refreshed, **changes):
    module = cloud()
    pool(tmp_path)
    plan = module.make_plan(tmp_path, config(**changes), refresh=refresh)
    return module, plan


def record(cid="toi-2-01", tier="T2"):
    from cygnus.ledger import now_utc
    checks = [{"name": name, "state": "passed", "note": "synthetic fixture", "source": "fixture"}
              for name in ("Period aliases (repeat events)", "Catalogue cross-match",
                           "Event-time comparison vs published ephemerides",
                           "Calibrated false-alarm threshold (sign-flip null)",
                           "Moving objects at screen-event epochs", "Known-signal recovery (positive control)")]
    if tier == "T3":
        checks += [{"name": name, "state": "passed", "note": "synthetic fixture", "source": "fixture"}
                   for name in ("Vetting difference-image localization (E1)", "Blend and dilution census",
                                "Event-epoch null exceedance (k/N)")]
    return {"schema": "cygnus.sky_record/1", "id": cid, "title": "Synthetic cloud fixture",
            "kind": "test", "status": "completed", "outcome": "lead", "evidence": "Unverified lead",
            "date": now_utc()[:10], "summary": "Synthetic software test, not sky evidence",
            "targets": [{"name": "TOI-2.01", "ra_deg": 10., "dec_deg": 20., "frame": "ICRS",
                         "epoch": "J2015.5", "position_source": "synthetic fixture"}],
            "products": [], "checks": checks}


def seed_stage(module, root, plan, cid="toi-2-01", stage="screen", tier="T2"):
    from cygnus.fileio import atomic_write_json, atomic_write_text
    out = module.stage_dir(root, plan, cid, stage)
    out.mkdir(parents=True)
    rec = record(cid, tier)
    rec.update(report=(out / "REPORT.md").relative_to(root).as_posix(),
               search_log=(out / "SEARCH_LOG.md").relative_to(root).as_posix(),
               spec=(out / "SPEC.yaml").relative_to(root).as_posix())
    atomic_write_text(out / "REPORT.md", "Synthetic fixture\n")
    atomic_write_text(out / "SEARCH_LOG.md", "Synthetic fixture\n")
    import yaml
    from cygnus.multi.scaffold import target_from_row
    target = target_from_row(plan["targets"][cid], "synthetic fixture")
    target.update(frame="ICRS", epoch="J2015.5")
    atomic_write_text(out / "SPEC.yaml", yaml.safe_dump({"schema": "cygnus.campaign/1", "campaign_id": cid,
        "random_seed": 1, "targets": [target], "steps": [], "record": {}}))
    atomic_write_json(out / "sky_record.json", rec)
    atomic_write_json(out / "STAGE.json", {"stage": stage, "complete": True,
                                          "executed": ["native_screen"], "synthetic": True})
    (out / "runner").mkdir()
    atomic_write_json(out / "runner/RUN_SUMMARY.json", {"complete": True})
    module.save_stage(root, plan, cid, stage)
    return out


def test_plan_refreshes_exact_rows_and_accounts_for_every_exclusion(tmp_path):
    module = cloud()
    pool(tmp_path)
    (tmp_path / "campaigns").mkdir()
    (tmp_path / "campaigns/toi-3-01.yaml").touch()
    calls = []

    def refresh(row):
        calls.append(row["name"])
        return refreshed(row)

    plan = module.make_plan(tmp_path, config(), refresh=refresh)
    assert calls == ["TOI-2.01", "TOI-4.01"]
    assert list(plan["targets"]) == ["toi-2-01", "toi-4-01"]
    assert len(plan["selection"]) == 4
    assert "frozen" in plan["selection"][0]["reason"]
    assert plan["targets"]["toi-2-01"]["catalogue_query"] == "synthetic exact-identity query"
    assert module.load_plan(tmp_path, module.plan_path(tmp_path, plan)) == plan


def test_source_lookup_failure_is_recorded_without_stale_fallback(tmp_path):
    module = cloud()
    pool(tmp_path)

    def refresh(row):
        raise RuntimeError("archive unavailable")

    plan = module.make_plan(tmp_path, config(), refresh=refresh)
    assert not plan["targets"]
    assert any(row["state"] == "lookup_failed" for row in plan["selection"])


def test_plan_rejects_changed_queue_and_lineage(tmp_path):
    module, plan = plan_fixture(tmp_path)
    (tmp_path / "queue.csv").write_text("changed\n")
    with pytest.raises(ValueError, match="queue|source"):
        module.load_plan(tmp_path, module.plan_path(tmp_path, plan))


@pytest.mark.parametrize("mutation", ["record", "extra", "decision"])
def test_completed_stage_is_verified_and_never_trusts_mutable_tier_labels(tmp_path, mutation):
    module, plan = plan_fixture(tmp_path)
    out = seed_stage(module, tmp_path, plan)
    assert module.verify_stage(tmp_path, plan, "toi-2-01", "screen")["earned"] == "T2"
    if mutation == "record":
        (out / "sky_record.json").write_text("{}")
    elif mutation == "extra":
        (out / "unlisted.json").write_text("{}")
    else:
        path = module.checkpoint_path(tmp_path, plan, "toi-2-01", "screen")
        data = json.loads(path.read_text())
        data["decision"]["earned"] = "T4"
        path.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="checkpoint|artifact|decision"):
        module.verify_stage(tmp_path, plan, "toi-2-01", "screen")


def test_gate_blocks_t3_for_failed_localization_and_for_failed_positive_control(tmp_path):
    module, plan = plan_fixture(tmp_path)
    rec = record(tier="T3")
    assert module.gate(rec, plan["config"])["tier"] == "T3"
    rec["checks"].append({"name": "Difference-image centroids / blend audit", "state": "failed"})
    assert module.gate(rec, plan["config"])["tier"] == "T2"
    rec = record()
    next(c for c in rec["checks"] if c["name"].startswith("Known-signal"))["state"] = "failed"
    assert module.gate(rec, plan["config"])["escalation"]


def test_t2_without_a_measured_defining_event_cannot_checkpoint(tmp_path):
    module, plan = plan_fixture(tmp_path)
    out = seed_stage(module, tmp_path, plan)
    target = module.stage_dir(tmp_path, plan, "toi-2-01", "T2")
    import shutil
    shutil.copytree(out, target)
    (target / "STAGE.json").write_text(json.dumps({"stage": "T2", "complete": True, "executed": ["vet"]}))
    with pytest.raises(ValueError, match="T2|defining|vet"):
        module.save_stage(tmp_path, plan, "toi-2-01", "T2")


def test_missing_t3_inputs_are_not_passes_or_a_completed_stage(tmp_path):
    module, plan = plan_fixture(tmp_path)
    result = module.run_diagnostics(tmp_path, record(tier="T3"), {}, ["rv_fit", "prf_source_fit"])
    assert not result["complete"]
    assert all(row["state"] == "not_tested" and not row["ran"] for row in result["tests"].values())


def test_resource_guard_stops_owned_child_and_reports_incomplete(tmp_path):
    module = cloud()
    scratch = tmp_path / "scratch"
    scratch.mkdir()
    (scratch / "bulk").write_bytes(b"x" * 20)
    result = module.supervise([sys.executable, "-c", "import time; time.sleep(20)"], tmp_path,
                              tmp_path / "child.log", scratch, timeout_s=5, max_bytes=10, min_free_bytes=0)
    assert result["returncode"] != 0 and result["state"] == "budget_stopped"
    assert "scratch" in result["reason"]


def test_config_rejects_t4_and_nonfinite_budgets():
    module = cloud()
    with pytest.raises(ValueError, match="T3|tier"):
        module.normalize_config(config(max_tier="T4"))
    data = config()
    data["budget"]["stage_seconds"] = float("nan")
    with pytest.raises(ValueError, match="budget"):
        module.normalize_config(data)


def input_packet(root, path, **fields):
    from cygnus.fileio import atomic_write_json, sha256_file
    quality = root / (path.stem + "-quality.json")
    atomic_write_json(quality, {"target": "TOI-2.01", "input_sha256": sha256_file(path), "state": "passed",
                                "checks": [{"name": "Synthetic known-answer validation", "state": "passed",
                                            "source": "explicit synthetic test fixture"}]})
    return {"path": path.relative_to(root).as_posix(), "sha256": sha256_file(path),
            "target": "TOI-2.01", "tic": 2,
            "validation": {"path": quality.name, "sha256": sha256_file(quality)},
            "provenance": {"archive": "synthetic", "product_id": path.name,
                           "url": "https://example.invalid/synthetic", "retrieved_utc": "2026-10-17T00:00:00Z",
                           "method": "explicitly synthetic software validation"}, **fields}


def test_t3_rv_uses_the_defining_event_epoch_and_preserves_conditional_claim(tmp_path):
    import numpy as np
    from cygnus.analysis.rv import rv_template
    module = cloud()
    time = np.linspace(2459000., 2459015., 30)
    velocity = 12. + 1.5 * rv_template(time, 4., 2459001.)
    path = tmp_path / "rv.csv"
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["time_bjd_tdb", "rv_kms", "sigma_kms"])
        writer.writerows(zip(time, velocity, np.full(len(time), .01)))
    entry = input_packet(tmp_path, path, time_standard="BJD_TDB", velocity_unit="km/s", rv_frame="barycentric",
                         periods_days=[4.], event_label="E1", event_bjd=2459001.)
    target = {"name": "TOI-2.01", "tic": 2, "t0_bjd": 2459000., "defining_events": {"E1": 2459001.}}
    result = module.run_diagnostics(tmp_path, record(tier="T3"), {"rv_fit": entry}, ["rv_fit"], target=target)
    assert result["complete"]
    test = result["tests"]["rv_fit"]
    assert test["state"] == "inconclusive" and test["ran"]
    assert test["result"]["fits"][0]["semiamplitude_kms"] == pytest.approx(1.5, abs=.001)
    entry["event_bjd"] = 2459000.
    with pytest.raises(ValueError, match="event"):
        module.run_diagnostics(tmp_path, record(), {"rv_fit": entry}, ["rv_fit"], target=target)


def test_t3_prf_runs_native_model_and_refuses_changed_input(tmp_path):
    import numpy as np
    from cygnus.analysis.prf import source_model
    module = cloud()
    axis = np.exp(-.5 * ((np.arange(117) - 58) / 9.) ** 2)
    prf = np.outer(axis, axis)
    path = tmp_path / "pixels.npz"
    np.savez(path, difference=source_model(prf, (11, 11), 5., 5.), sigma=np.full((11, 11), .01), prf=prf)
    entry = input_packet(tmp_path, path, instrument="TESS", pixel_unit="cutout_pixel", flux_unit="electron/s",
                         positions={"TOI-2.01": [5., 5.], "neighbour": [8., 8.]},
                         shifts=[[0., 0.]], floors=[.01, .03], event_label="E1", event_bjd=2459001.)
    target = {"name": "TOI-2.01", "tic": 2, "defining_events": {"E1": 2459001.}}
    result = module.run_diagnostics(tmp_path, record(), {"prf_source_fit": entry}, ["prf_source_fit"], target=target)
    assert result["complete"] and result["tests"]["prf_source_fit"]["state"] == "inconclusive"
    path.write_bytes(b"changed")
    with pytest.raises(ValueError, match="checksum"):
        module.run_diagnostics(tmp_path, record(), {"prf_source_fit": entry}, ["prf_source_fit"], target=target)


def test_budget_detects_a_fast_childs_final_write(tmp_path):
    module = cloud()
    scratch = tmp_path / "scratch"
    scratch.mkdir()
    result = module.supervise([sys.executable, "-c", "from pathlib import Path; Path('scratch/bulk').write_bytes(b'x'*100)"],
                              tmp_path, tmp_path / "child.log", scratch, timeout_s=10,
                              max_bytes=10, min_free_bytes=0)
    assert result["state"] == "budget_stopped"


def test_native_t2_reuses_pinned_light_curve_and_keeps_missing_pixels_inconclusive(tmp_path, monkeypatch):
    import yaml
    from _multi_fixtures import write_spoc, product_entry
    from cygnus.fileio import atomic_write_json, atomic_write_text, sha256_file
    from cygnus.campaign import vet as vet_module
    module, plan = plan_fixture(tmp_path, limit=1, refresh=lambda r: {
        **refreshed(r), "t0_bjd": 2459002., "period_days": 20.})
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    out = seed_stage(module, tmp_path, plan)
    module.checkpoint_path(tmp_path, plan, "toi-2-01", "screen").unlink()
    product = "tess-fixture-s0001-s_lc.fits"
    path = tmp_path / "scratch/campaign_toi-2-01" / product
    write_spoc(path, n=1728, cadence_s=600, t_start=0., bjdrefi=2459000,
               dips=[2., 6.], depth=.01, half_width_d=1/24, noise=.0002, sector=1)
    # The test fixture's source metadata uses TIC 2; write that exact identity in the FITS header.
    from astropy.io import fits
    with fits.open(path, mode="update") as hdus:
        hdus[0].header["TICID"] = 2
    target = {"name": "TOI-2.01", "tic": 2, "ra_deg": 10., "dec_deg": 20.,
              "frame": "ICRS", "epoch": "J2015.5", "position_source": "synthetic fixture",
              "duration_h": 2., "t0_bjd": 2459002., "period_days": 20.}
    spec = {"schema": "cygnus.campaign/1", "runner": "cygnus.multi", "campaign_id": "toi-2-01",
            "outputs": out.relative_to(tmp_path).as_posix(), "random_seed": 1, "targets": [target],
            "veto": {"kind": "ephemeris", "period_days": 20., "t0_bjd": 2459002.,
                     "veto_phase": .02, "source": "synthetic fixture"}, "steps": [], "record": {}}
    atomic_write_text(out / "SPEC.yaml", yaml.safe_dump(spec))
    rec = json.loads((out / "sky_record.json").read_text())
    rec["targets"] = [target]
    rec["products"] = [{"id": product, "archive": "MAST", "sha256": sha256_file(path)}]
    atomic_write_json(out / "sky_record.json", rec)
    entry = product_entry(path, target="TOI-2.01", tic=2, sector=1)
    atomic_write_json(out / "runner/fetch_products.json", {"result": {"products": {product: entry}}})
    atomic_write_json(out / "runner/known_signal_recovery.json", {"result": {"per_product": {product: {
        "epochs": [{"epoch_bjd": 2459002., "state": "recovered"}]}}}})
    atomic_write_json(out / "period_aliases.json", {"candidates": [{"product": product, "event_bjd": 2459006.,
                       "depth_ppm": 10000., "n_allowed": 1, "allowed_periods_days": [4.]}]})
    module.save_stage(tmp_path, plan, "toi-2-01", "screen")
    source_hash = sha256_file(out / "sky_record.json")
    monkeypatch.setattr(vet_module, "siblings", lambda tic: ([], "synthetic archive boundary"))
    monkeypatch.setattr(vet_module, "neighbour_lcs", lambda *args: [])
    monkeypatch.setattr(vet_module, "tpf_for", lambda *args: (_ for _ in ()).throw(FileNotFoundError("no synthetic pixels")))
    result = module.run_stage(tmp_path, plan, "toi-2-01", "T2")
    assert result["status"] == "completed" and result["run_at"] == "T2"
    # Only the supervisor commits checkpoints after enforcing the final resource postcondition.
    assert module.verify_stage(tmp_path, plan, "toi-2-01", "T2") is None
    module.save_stage(tmp_path, plan, "toi-2-01", "T2")
    assert sha256_file(out / "sky_record.json") == source_hash
    final = module.stage_dir(tmp_path, plan, "toi-2-01", "T2")
    derived = json.loads((final / "sky_record.json").read_text())
    states = {c["name"]: c["state"] for c in derived["checks"]}
    assert states["Vetting difference-image localization (E1)"] == "inconclusive"
    assert states["Event-epoch null exceedance (k/N)"] != "not_tested"
    assert derived["evidence"] == "Unverified lead"
    assert module.board(tmp_path, plan)["toi-2-01"]["next_stage"] is None
    assert module.verify_stage(tmp_path, plan, "toi-2-01", "T2")["run_at"] == "T2"


def test_t3_metadata_retains_exact_query_and_does_not_clear_identity(tmp_path, monkeypatch):
    from cygnus.multi.archives import base
    module = cloud()

    class Adapter:
        def tap_csv(self, endpoint, query):
            return []

        def discover(self, target, **kwargs):
            self.tap_csv("https://example.invalid/tap", "SELECT synthetic_fixture")
            return []

    adapter = Adapter()
    original_tap = adapter.tap_csv
    monkeypatch.setattr(base, "get", lambda name: adapter)
    target = {"name": "TOI-2.01", "tic": 2, "ra_deg": 10., "dec_deg": 20.}
    result = module.run_diagnostics(tmp_path, record(), {}, ["archive_metadata"], target=target)
    assert result["complete"] and result["tests"]["archive_metadata"]["state"] == "inconclusive"
    assert result["tests"]["archive_metadata"]["queries"][0]["query"] == "SELECT synthetic_fixture"
    assert adapter.tap_csv == original_tap
    assert "tap_csv" not in adapter.__dict__
    again = module.run_diagnostics(tmp_path, record(), {}, ["archive_metadata"], target=target)
    assert len(again["tests"]["archive_metadata"]["queries"]) == 1


def test_finished_targets_resume_without_invoking_a_worker(tmp_path, monkeypatch):
    module, plan = plan_fixture(tmp_path, limit=1, max_tier="T0")
    seed_stage(module, tmp_path, plan)
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    monkeypatch.setattr(module, "supervise", lambda *a, **kw: pytest.fail("verified target was recomputed"))
    assert module.run_plan(tmp_path, plan) == 0
    from cygnus.skyrecord import validate
    rec = json.loads((module.report_dir(tmp_path, plan) / "sky_record.json").read_text())
    assert not validate(rec, tmp_path)


def seed_t2(module, root, plan):
    from cygnus.fileio import atomic_write_json
    import shutil
    out = seed_stage(module, root, plan)
    target = module.stage_dir(root, plan, "toi-2-01", "T2")
    shutil.copytree(out, target)
    source = json.loads((out / "sky_record.json").read_text())
    derived = record(tier="T3")
    derived.update({k: source[k] for k in ("spec", "report", "search_log")})
    atomic_write_json(target / "sky_record.json", derived)
    atomic_write_json(target / "SOURCE_RECORD.json", source)
    atomic_write_json(target / "STAGE.json", {"stage": "T2", "complete": True, "executed": ["vet", "event_null"]})
    atomic_write_json(target / "period_aliases.json", {"candidates": [{"product": "synthetic_lc.fits", "event_bjd": 2459001.}]})
    (target / "vetting").mkdir()
    atomic_write_json(target / "vetting/vetting.json", {"events": [{"label": "E1", "product": "synthetic_lc.fits",
        "fit": {"mid_bjd": 2459001., "duration_h": 2., "depth_ppm": 1000., "depth_err_ppm": 100., "n_in": 12}}]})
    atomic_write_json(target / "event_null.json", {"events": [{"product": "synthetic_lc.fits", "event_bjd": 2459001.,
        "observed": {"state": "measured", "depth_ppm": 1000., "n_event": 12, "coverage": 1.},
        "null": {"n_exceed": 0, "n_covered": 300}}]})
    module.save_stage(root, plan, "toi-2-01", "T2")
    return target


def test_t3_missing_inputs_retains_t2_checkpoint_and_cannot_be_marked_done(tmp_path):
    module, plan = plan_fixture(tmp_path, limit=1, t3={"tests": ["rv_fit"]})
    seed_t2(module, tmp_path, plan)
    result = module.run_stage(tmp_path, plan, "toi-2-01", "T3")
    assert result["status"] == "blocked"
    assert module.verify_stage(tmp_path, plan, "toi-2-01", "T2")
    assert module.verify_stage(tmp_path, plan, "toi-2-01", "T3") is None
    with pytest.raises(ValueError, match="completed|execution proof"):
        module.save_stage(tmp_path, plan, "toi-2-01", "T3")
    assert module.board(tmp_path, plan)["toi-2-01"]["run_at"] == "T2"


def test_failed_native_artifact_check_blocks_t3_without_rewriting_earned_tier(tmp_path):
    from cygnus.fileio import atomic_write_json
    module, plan = plan_fixture(tmp_path, limit=1)
    target = seed_t2(module, tmp_path, plan)
    rec = json.loads((target / "sky_record.json").read_text())
    report = {"events": [{"label": "E1", "checks": {
        "Background / centroid / pointing": ["failed", "synthetic pointing excursion"],
        "Quality flags and coverage": ["not_tested", "unavailable"],
        "Shape matches reference transit": ["failed", "different shape is not an artifact verdict"]}}]}
    rec = module.retain_vetting_checks(rec, report)
    atomic_write_json(target / "sky_record.json", rec)
    module.save_stage(tmp_path, plan, "toi-2-01", "T2")
    row = module.board(tmp_path, plan)["toi-2-01"]
    assert row["earned"] == "T3" and row["next_stage"] is None
    assert "artifact" in row["reason"]
    assert any(c["state"] == "not_tested" for c in rec["checks"])
    with pytest.raises(ValueError, match="gate|artifact"):
        module.run_stage(tmp_path, plan, "toi-2-01", "T3")
    only_shape = module.retain_vetting_checks(record(tier="T3"), {"events": [{"label": "E1", "checks": {
        "Shape matches reference transit": ["failed", "conditional model mismatch"]}}]})
    assert not module.gate(only_shape, plan["config"])["escalation"]


def test_report_ships_lineage_and_a_complete_verifiable_manifest(tmp_path):
    from cygnus.colab import verify_manifest
    module, plan = plan_fixture(tmp_path, limit=1)
    seed_stage(module, tmp_path, plan)
    module.write_report(tmp_path, plan)
    out = module.report_dir(tmp_path, plan)
    assert json.loads((out / "LINEAGE.json").read_text()) == plan
    assert not verify_manifest(out / "MANIFEST.sha256", out)
    assert (out / "CHECKPOINTS.json").is_file()


def test_checkpoint_rejects_wrong_target_even_when_record_id_is_unchanged(tmp_path):
    module, plan = plan_fixture(tmp_path, limit=1)
    out = seed_stage(module, tmp_path, plan)
    value = json.loads((out / "sky_record.json").read_text())
    value["targets"][0]["name"] = "AnotherSource"
    (out / "sky_record.json").write_text(json.dumps(value))
    with pytest.raises(ValueError, match="identity|source"):
        module.save_stage(tmp_path, plan, "toi-2-01", "screen")


def test_truncated_attempt_log_does_not_hide_verified_checkpoints(tmp_path, monkeypatch):
    module, plan = plan_fixture(tmp_path, limit=1, max_tier="T0")
    seed_stage(module, tmp_path, plan)
    journal = module.plan_path(tmp_path, plan).parent / "ATTEMPTS.jsonl"
    journal.write_text('{"interrupted":')
    assert module.board(tmp_path, plan)["toi-2-01"]["earned"] == "T2"
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    assert module.run_plan(tmp_path, plan) == 0
    assert all(json.loads(line) for line in journal.read_text().splitlines())


def test_t3_worker_completes_a_supported_validated_diagnostic_without_promotion(tmp_path):
    import numpy as np
    from cygnus.analysis.rv import rv_template
    module = cloud()
    path = tmp_path / "rv.csv"
    time = np.linspace(2459000., 2459015., 30)
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["time_bjd_tdb", "rv_kms", "sigma_kms"])
        writer.writerows(zip(time, 12. + 1.5 * rv_template(time, 4., 2459001.), np.full(len(time), .01)))
    entry = input_packet(tmp_path, path, time_standard="BJD_TDB", velocity_unit="km/s", rv_frame="barycentric",
                         periods_days=[4.], event_label="E1", event_bjd=2459001.)
    _, plan = plan_fixture(tmp_path, limit=1, t3={"tests": ["rv_fit"], "inputs": {"toi-2-01": {"rv_fit": entry}}})
    seed_t2(module, tmp_path, plan)
    result = module.run_stage(tmp_path, plan, "toi-2-01", "T3")
    assert result["status"] == "completed" and result["evidence"] == "Unverified lead"
    assert module.verify_stage(tmp_path, plan, "toi-2-01", "T3") is None
    module.save_stage(tmp_path, plan, "toi-2-01", "T3")
    assert module.board(tmp_path, plan)["toi-2-01"]["next_stage"] is None
    module.write_report(tmp_path, plan)
    out = module.stage_dir(tmp_path, plan, "toi-2-01", "T3")
    data = json.loads((out / "diagnostics.json").read_text())
    assert data["tests"]["rv_fit"]["result"]["fits"][0]["semiamplitude_kms"] == pytest.approx(1.5, abs=.001)
    assert json.loads((out / "sky_record.json").read_text())["evidence"] == "Unverified lead"


def test_screen_uses_fresh_source_period_and_native_runner_interface(tmp_path, monkeypatch):
    from cygnus.multi import runner, scaffold
    from cygnus.fileio import atomic_write_json
    module, plan = plan_fixture(tmp_path, limit=1, max_tier="T0", refresh=lambda row: {
        **refreshed(row), "period_days": 7.5})
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    calls = []

    def native_run(path, *, ledger, root):
        spec = runner.load_spec(path)
        calls.append(spec)
        assert spec["veto"]["kind"] == "ephemeris" and spec["veto"]["period_days"] == 7.5
        ctx = runner.Context(spec, ledger, root)
        ctx.check("Known-signal recovery (positive control)", "passed", "synthetic interface fixture")
        runner.write_record(ctx, True)
        (ctx.outdir / "runner").mkdir()
        atomic_write_json(ctx.outdir / "runner/RUN_SUMMARY.json", {"complete": True})
        return {"complete": True}

    def report(spec, root):
        # Scientific runner behaviour is covered by native tests; this checks the cloud boundary.
        return []

    monkeypatch.setattr(runner, "run", native_run)
    monkeypatch.setattr(scaffold, "draft_report", report)
    result = module.run_stage(tmp_path, plan, "toi-2-01", "screen")
    assert result["status"] == "completed" and len(calls) == 1
    module.save_stage(tmp_path, plan, "toi-2-01", "screen")
    assert module.board(tmp_path, plan)["toi-2-01"]["next_stage"] is None

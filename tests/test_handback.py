"""Tier contracts and handback verification; synthetic fixtures are not astronomical evidence.

Several cases replay failures seen in real runs (2026-10-02 to 2026-10-17); each says which.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from test_cloud_workflow import plan_fixture, record, seed_stage

ROOT = Path(__file__).resolve().parents[1]
REAL_COLAB = ROOT / "docs/colab_runs/t2-p02-b02-2026-10-02-10deebcecc06/cloud"


def no_git(commit, files=None):
    return []


def hb():
    from cygnus import handback
    return handback


def seed_capsule(tmp_path, *, t2=True):
    """A plan with a verified screen (and T2) stage carrying every contract output, packed."""
    from cygnus.fileio import atomic_write_json, atomic_write_text
    module, plan = plan_fixture(tmp_path, limit=1)
    out = seed_stage(module, tmp_path, plan)
    atomic_write_json(out / "SOURCE_ROW.json", plan["targets"]["toi-2-01"])
    module.save_stage(tmp_path, plan, "toi-2-01", "screen")
    if t2:
        target = module.stage_dir(tmp_path, plan, "toi-2-01", "T2")
        shutil.copytree(out, target)
        source = json.loads((out / "sky_record.json").read_text())
        derived = record(tier="T2")
        derived.update({k: source[k] for k in ("spec", "report", "search_log")})
        atomic_write_json(target / "sky_record.json", derived)
        atomic_write_json(target / "SOURCE_RECORD.json", source)
        atomic_write_text(target / "SOURCE_SPEC.yaml", (out / "SPEC.yaml").read_text())
        atomic_write_json(target / "STAGE.json", {"stage": "T2", "complete": True, "executed": ["vet", "event_null"]})
        atomic_write_json(target / "period_aliases.json",
                          {"candidates": [{"product": "synthetic_lc.fits", "event_bjd": 2459001.}]})
        (target / "vetting").mkdir()
        atomic_write_json(target / "vetting/vetting.json", {"events": [{"label": "E1", "product": "synthetic_lc.fits",
            "fit": {"mid_bjd": 2459001., "duration_h": 2., "depth_ppm": 1000., "depth_err_ppm": 100., "n_in": 12}}]})
        atomic_write_json(target / "event_null.json", {"events": [{"product": "synthetic_lc.fits", "event_bjd": 2459001.,
            "observed": {"state": "measured", "depth_ppm": 1000., "n_event": 12, "coverage": 1.},
            "null": {"n_exceed": 0, "n_covered": 300}}]})
        atomic_write_json(target / "runner/fetch_products.json", {"result": {"products": []}})
        atomic_write_json(target / "FOLLOWUP_PRODUCTS.json", {"ancillary": []})
        module.save_stage(tmp_path, plan, "toi-2-01", "T2")
    module.write_report(tmp_path, plan)
    capsule = module.report_dir(tmp_path, plan)
    hb().pack(capsule, environment="cloud-agent", harness="synthetic", code_check=no_git)
    return module, plan, capsule


def remanifest(module, plan, tmp_path):
    """Rebuild the capsule manifest the way a careless producer would, so only deeper checks can catch it."""
    from cygnus.colab import build_manifest
    out = module.report_dir(tmp_path, plan)
    entries = build_manifest(out, [p.name for p in out.iterdir()
                                   if p.name not in ("MANIFEST.sha256", "HANDBACK.json", "IMPORTED.sha256")])
    (out / "MANIFEST.sha256").write_text("".join(f"{v}  {k}\n" for k, v in entries.items()))


def test_contracts_cover_every_stage_and_never_allow_t4_or_promotion():
    from cygnus import cloud
    handback = hb()
    assert set(cloud.STAGES) <= set(handback.CONTRACTS)
    for name, contract in handback.CONTRACTS.items():
        assert {"inputs", "outputs", "gate_in", "gate_out", "may_earn", "evidence"} <= set(contract), name
        assert "T4" not in contract["may_earn"] and "sky_record.json" in contract["outputs"]
    assert handback.AUTOMATED_EVIDENCE == (None, "Unverified lead")


def test_capsule_packs_verifies_ingests_in_place_and_passes_repo_checks(tmp_path):
    from cygnus import skyrecord as sr
    handback = hb()
    module, plan, capsule = seed_capsule(tmp_path)
    found = handback.verify(capsule, code_check=no_git)
    assert found["ok"], found["problems"]
    assert found["handback"]["targets"]["toi-2-01"]["stages"] == ["screen", "T2"]
    (tmp_path / "docs/STATUS.md").write_text("# Status\n\nmanual decisions stay\n")
    receipt = handback.ingest(capsule, tmp_path, code_check=no_git)
    assert receipt["retained_elsewhere"] == {}
    assert handback.check_imported(tmp_path) == []
    report = tmp_path / "reports" / handback.report_slug(plan["id"])
    rec = json.loads((report / "sky_record.json").read_text())
    assert sr.validate(rec, tmp_path) == [] and rec["evidence"] is None
    # Stage records keep the target id; outside reports/ they cannot become duplicate published ids.
    ids = [r["id"] for r in sr.load_records(tmp_path)]
    assert ids == [rec["id"]] and not sr.coverage_gaps(tmp_path, sr.load_records(tmp_path))
    status = (tmp_path / "docs/STATUS.md").read_text()
    assert "manual decisions stay" in status and f"cygnus:handback:{plan['id']}:start" in status
    again = handback.ingest(capsule, tmp_path, code_check=no_git)
    assert again["imported"] == receipt["imported"]


def test_capsule_location_keeps_stage_records_out_of_published_record_search(tmp_path):
    # Lesson: capsules under reports/cloud/<id>/ nested one same-id sky record per stage.
    module, plan = plan_fixture(tmp_path, limit=1)
    rel = module.report_dir(tmp_path, plan).relative_to(tmp_path).parts[0]
    from cygnus.skyrecord import SEARCH_DIRS
    assert rel not in SEARCH_DIRS


def _mutate(capsule, module, plan, tmp_path, how):
    from cygnus.fileio import atomic_write_json
    t2 = capsule / "targets/toi-2-01/T2"
    if how == "checksum":
        (t2 / "REPORT.md").write_text("edited after the manifest\n")
    elif how == "unlisted":
        (capsule / "notes.txt").write_text("extra\n")
    elif how == "fits":
        (capsule / "cutout.fits").write_bytes(b"SIMPLE")
        remanifest(module, plan, tmp_path)
    elif how == "private_path":
        (capsule / "REPORT.md").write_text("cache at C:\\Users\\someone\\scratch\n")
        remanifest(module, plan, tmp_path)
    elif how == "token":
        (capsule / "REPORT.md").write_text('{"access_token": "x"}\n')
        remanifest(module, plan, tmp_path)
    elif how == "board":
        board = json.loads((capsule / "tier_board.json").read_text())
        board["targets"]["toi-2-01"]["earned"] = "T3"
        atomic_write_json(capsule / "tier_board.json", board)
        remanifest(module, plan, tmp_path)
    elif how == "claims":
        claims = json.loads((capsule / "HANDBACK.json").read_text())
        claims["counts"] = {"T3": 1}
        atomic_write_json(capsule / "HANDBACK.json", claims)
    elif how == "missing_output":
        (t2 / "event_null.json").unlink()
    elif how == "decision":
        receipts = json.loads((capsule / "CHECKPOINTS.json").read_text())
        receipts["toi-2-01.T2"]["decision"]["earned"] = "T3"
        atomic_write_json(capsule / "CHECKPOINTS.json", receipts)
        remanifest(module, plan, tmp_path)


@pytest.mark.parametrize("how, message", [
    ("checksum", "checksum mismatch"), ("unlisted", "not covered by the manifest"),
    ("fits", "bulk product"), ("private_path", "private machine path"), ("token", "credential"),
    ("board", "tier_board.json claims"), ("claims", "HANDBACK.json counts"),
    ("missing_output", "contract outputs missing"), ("decision", "decision differs")])
def test_malformed_or_unverifiable_capsules_are_rejected(tmp_path, how, message):
    handback = hb()
    module, plan, capsule = seed_capsule(tmp_path)
    _mutate(capsule, module, plan, tmp_path, how)
    found = handback.verify(capsule, code_check=no_git)
    assert not found["ok"] and any(message in p for p in found["problems"]), found["problems"]
    with pytest.raises(handback.HandbackError, match="rejected"):
        handback.ingest(capsule, tmp_path, code_check=no_git)
    assert not (tmp_path / "reports").exists()


def test_self_consistent_capsule_that_promotes_evidence_is_rejected(tmp_path):
    from cygnus.fileio import atomic_write_json
    handback = hb()
    module, plan, capsule = seed_capsule(tmp_path)
    t2 = capsule / "targets/toi-2-01/T2"
    rec = json.loads((t2 / "sky_record.json").read_text())
    rec["evidence"] = "Vetted candidate"
    atomic_write_json(t2 / "sky_record.json", rec)
    module.save_stage(tmp_path, plan, "toi-2-01", "T2")    # a producer re-checkpointing its own promotion
    module.write_report(tmp_path, plan)
    with pytest.raises(handback.HandbackError, match="evidence"):
        handback.pack(capsule, environment="cloud-agent", code_check=no_git)


def test_unknown_or_dirty_code_commit_is_unverifiable(tmp_path):
    handback = hb()
    module, plan, capsule = seed_capsule(tmp_path)
    found = handback.verify(capsule, code_check=lambda c, f=None: ["code commit abc is not in local history"])
    assert not found["ok"] and "local history" in found["problems"][0]
    check = handback.git_code_check(ROOT)
    assert check("0" * 40) and "not a full SHA" in check("HEAD")[0]


def test_resumed_run_supersedes_but_a_shrunk_handback_does_not(tmp_path):
    handback = hb()
    _, _, capsule = seed_capsule(tmp_path, t2=False)
    inbox = tmp_path / "inbox" / "docs/handbacks" / capsule.name
    shutil.copytree(capsule, inbox)
    assert handback.ingest(inbox, tmp_path, code_check=no_git)["id"] == capsule.name
    claims = json.loads((capsule / "HANDBACK.json").read_text())
    claims["targets"]["toi-2-01"]["stages"] = ["screen", "T2"]     # the earlier import had more work
    (capsule / "HANDBACK.json").write_text(json.dumps(claims))
    with pytest.raises(handback.HandbackError, match="does not supersede"):
        handback.ingest(inbox, tmp_path, code_check=no_git)


def test_check_imported_detects_an_edited_import(tmp_path):
    handback = hb()
    _, _, capsule = seed_capsule(tmp_path)
    handback.ingest(capsule, tmp_path, code_check=no_git)
    (capsule / "targets/toi-2-01/T2/REPORT.md").write_text("rewritten by hand\n")
    assert any("changed" in p for p in handback.check_imported(tmp_path))


@pytest.mark.parametrize("message, kind, retry", [
    # 2026-10-08/10: shared rclone client quota while staging and reading Drive.
    ("rclone: HTTP 403 RATE_LIMIT_EXCEEDED (userRateLimitExceeded)", "storage_quota", True),
    # 2026-10-10 Colab T2: 11 targets stopped by the event-null coverage guard.
    ("event null emitted no measured/covered defining event: not a completed T2 target", "coverage_guard", False),
    ("ValueError: T2 native null has no covered/measured defining event", "coverage_guard", False),
    # 2026-09-26: drive.file token cannot see folders the Colab mount created.
    ("rclone lsf exit status 3: directory not found", "not_visible", False),
    # 2026-10-17: shared workstation interpreter; gradio 5.29.1 requires pillow<12.
    ("pip check: gradio 5.29.1 has requirement pillow<12", "environment", False),
    ("checkpoint artifact set or hash changed", "integrity", False),
    ("ReadTimeout: HTTPSConnectionPool timed out", "transient", True),
    ("managed scratch byte budget exceeded", "budget", False),
])
def test_past_failures_are_classified_for_retry(message, kind, retry):
    found = hb().classify_failure(message)
    assert (found["class"], found["retryable"]) == (kind, retry)


def test_with_retries_backs_off_only_for_retryable_failures():
    handback = hb()
    calls, sleeps, log = [], [], []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise RuntimeError("HTTP 403 RATE_LIMIT_EXCEEDED")
        return "ok"

    assert handback.with_retries(flaky, sleep=sleeps.append, log=log) == "ok"
    assert sleeps == [30.0, 120.0] and [row["class"] for row in log] == ["storage_quota"] * 2

    def guard():
        raise ValueError("no measured/covered defining event")
    with pytest.raises(ValueError):
        handback.with_retries(guard, sleep=sleeps.append)
    assert sleeps == [30.0, 120.0]


def _real_packet(tmp_path):
    from cygnus.colab import read_manifest
    if not (REAL_COLAB / "MANIFEST.sha256").is_file():
        pytest.skip("the 2026-10-10 Colab export copy is not present in this checkout")
    dest = tmp_path / "inbox" / "t2-p02-b02-2026-10-02-10deebcecc06"
    for rel in [*read_manifest(REAL_COLAB / "MANIFEST.sha256"), "MANIFEST.sha256", "LOCATION.json"]:
        if (REAL_COLAB / rel).is_file() and rel != "ledger.sqlite":
            (dest / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REAL_COLAB / rel, dest / rel)
    return dest


def test_real_colab_t2_export_verifies_with_its_reported_counts(tmp_path):
    # The 2026-10-10 browser-driven Colab batch: report says 17 T2, 2 closed, 11 incomplete.
    found = hb().verify(_real_packet(tmp_path), code_check=no_git)
    assert found["ok"], found["problems"][:5]
    assert found["handback"]["counts"] == {"T2": 17, "closed": 2, "incomplete": 11}
    assert all(row["evidence"] in (None, "Unverified lead") for row in found["handback"]["targets"].values())


def test_real_colab_export_with_an_edited_tier_label_is_rejected(tmp_path):
    from cygnus.colab import build_manifest, write_manifest
    from cygnus.fileio import sha256_file
    packet = _real_packet(tmp_path)
    done = json.loads((packet / "done.json").read_text())
    done["toi-1938-01"]["earned"] = "T3"
    (packet / "done.json").write_text(json.dumps(done))
    names = [p.relative_to(packet).as_posix() for p in packet.rglob("*") if p.is_file()
             and p.name not in ("MANIFEST.sha256", "LOCATION.json")]
    write_manifest(packet / "MANIFEST.sha256", build_manifest(packet, names))
    location = json.loads((packet / "LOCATION.json").read_text())
    location["manifest_sha256"] = sha256_file(packet / "MANIFEST.sha256")
    (packet / "LOCATION.json").write_text(json.dumps(location))
    found = hb().verify(packet, code_check=no_git)
    assert not found["ok"] and any("toi-1938-01" in p for p in found["problems"])


def test_handbacks_committed_to_this_repository_match_their_receipts():
    assert hb().check_imported(ROOT) == []

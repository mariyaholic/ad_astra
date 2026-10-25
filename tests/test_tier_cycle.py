"""One-command tier cycles: ledgered, resumable, retried only when a failure is transient.

Synthetic stages stand in for native science; the archive and git boundaries are replaced.
"""
from __future__ import annotations

import json

import pytest
import yaml

from test_cloud_workflow import config, pool, refreshed, seed_stage


@pytest.fixture
def env(tmp_path, monkeypatch):
    from cygnus import cloud, handback, storage, targets, tier
    pool(tmp_path)
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs/STATUS.md").write_text("# Status\n")
    (tmp_path / "recipe.yaml").write_text(yaml.safe_dump(config(limit=1, max_tier="T0")))
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    monkeypatch.setattr(targets, "refresh_queue_target", refreshed)
    monkeypatch.setattr(handback, "git_code_check", lambda repo: lambda commit, files=None: [])
    monkeypatch.setattr(storage, "resolve_route", lambda *a, **k: None)
    monkeypatch.setattr(tier, "preflight", lambda root, env: ([], [], {"checks": []}))
    calls = {"run": 0}

    def run_plan(root, plan):
        calls["run"] += 1
        out = seed_stage(cloud, root, plan, plan_cid(plan))
        from cygnus.fileio import atomic_write_json
        atomic_write_json(out / "SOURCE_ROW.json", plan["targets"][plan_cid(plan)])
        cloud.save_stage(root, plan, plan_cid(plan), "screen")
        return 0
    monkeypatch.setattr(cloud, "run_plan", run_plan)
    return tmp_path, tier, cloud, handback, calls


def plan_cid(plan):
    return next(iter(plan["targets"]))


def test_local_cycle_goes_from_recipe_to_verified_ingest_and_resumes(env, monkeypatch):
    root, tier, cloud, handback, calls = env
    assert tier.cycle(root, "recipe.yaml", env="local", name="pilot") == 0
    state = json.loads((root / "state/tier_cycles/pilot/CYCLE.json").read_text())
    assert all(state["steps"][s]["state"] in ("done", "skipped") for s in tier.STEPS)
    plan = state["steps"]["plan"]["plan"]
    hid = plan.split("/")[2]
    assert (root / "reports" / handback.report_slug(hid) / "sky_record.json").is_file()
    assert handback.check_imported(root) == []
    assert state["steps"]["cleanup"]["state"] == "skipped"       # local default keeps scratch
    monkeypatch.setattr(cloud, "make_plan", lambda *a, **k: pytest.fail("resume must reuse PLAN.json"))
    assert tier.cycle(root, "recipe.yaml", env="local", name="pilot") == 0
    assert calls["run"] == 1
    journal = (root / "state/tier_cycles/pilot/JOURNAL.jsonl").read_text().splitlines()
    assert [json.loads(row)["step"] for row in journal].count("plan") == 1


def test_cloud_agent_without_a_drive_route_delivers_through_the_checkout_and_cleans_scratch(env):
    root, tier, cloud, handback, calls = env
    assert tier.cycle(root, "recipe.yaml", env="cloud-agent", name="agent") == 0
    state = json.loads((root / "state/tier_cycles/agent/CYCLE.json").read_text())
    assert state["steps"]["deliver"]["mode"] == "git"
    assert state["steps"]["cleanup"]["state"] == "done"
    claims = json.loads((root / state["steps"]["report"]["capsule"] / "HANDBACK.json").read_text())
    assert claims["environment"] == "cloud-agent"
    assert not (root / "scratch/cloud" / claims["id"]).exists()


def test_transient_run_failure_is_retried_then_left_for_a_rerun(env, monkeypatch):
    root, tier, cloud, handback, calls = env
    sleeps = []

    def failing(root_, plan):
        calls["run"] += 1
        journal = cloud.plan_path(root_, plan).parent / "ATTEMPTS.jsonl"
        journal.parent.mkdir(parents=True, exist_ok=True)
        with journal.open("a") as stream:
            stream.write(json.dumps({"state": "failed", "error": "ReadTimeout: MAST timed out"}) + "\n")
        return 1
    good = cloud.run_plan
    monkeypatch.setattr(cloud, "run_plan", failing)
    assert tier.cycle(root, "recipe.yaml", env="local", name="flaky", sleep=sleeps.append) == tier.EXIT_RETRY
    assert calls["run"] == 2 and sleeps == [30]
    monkeypatch.setattr(cloud, "run_plan", good)
    assert tier.cycle(root, "recipe.yaml", env="local", name="flaky") == 0


def test_coverage_guard_is_not_retried_and_still_hands_back_an_honest_incomplete(env, monkeypatch):
    root, tier, cloud, handback, calls = env

    def guarded(root_, plan):
        calls["run"] += 1
        journal = cloud.plan_path(root_, plan).parent / "ATTEMPTS.jsonl"
        journal.parent.mkdir(parents=True, exist_ok=True)
        journal.write_text(json.dumps({"state": "failed", "error":
                                       "ValueError: T2 native null has no covered/measured defining event"}) + "\n")
        return 1
    monkeypatch.setattr(cloud, "run_plan", guarded)
    assert tier.cycle(root, "recipe.yaml", env="local", name="guard", sleep=lambda s: pytest.fail("retried")) == 0
    state = json.loads((root / "state/tier_cycles/guard/CYCLE.json").read_text())
    assert state["steps"]["run"]["state"] == "partial"
    assert state["steps"]["run"]["failure"]["class"] == "coverage_guard"
    capsule = root / state["steps"]["report"]["capsule"]
    claims = json.loads((capsule / "HANDBACK.json").read_text())
    assert {row["status"] for row in claims["targets"].values()} == {"incomplete"}


def test_cloud_agents_require_a_clean_preflight_but_local_tolerates_pip_check(tmp_path, monkeypatch):
    from cygnus import tier
    receipt = {"checks": [{"name": "pip_check", "passed": False, "detail": "gradio pin"},
                          {"name": "import:numpy", "passed": True, "detail": "imported"}]}
    monkeypatch.setattr(tier.runpy, "run_path", lambda path: {"preflight": lambda root: receipt})
    assert tier.preflight(tmp_path, "local")[:2] == ([], ["pip_check"])
    assert tier.preflight(tmp_path, "cloud-agent")[:2] == (["pip_check"], [])


def test_changed_recipe_under_the_same_cycle_name_is_refused(env):
    root, tier, cloud, handback, calls = env
    assert tier.cycle(root, "recipe.yaml", env="local", name="fixed") == 0
    (root / "recipe.yaml").write_text(yaml.safe_dump(config(limit=2, max_tier="T0")))
    with pytest.raises(SystemExit, match="different recipe"):
        tier.cycle(root, "recipe.yaml", env="local", name="fixed")


def test_cli_lists_contracts(capsys):
    from cygnus import tier
    assert tier.main(["contracts"]) == 0
    assert "colab_T2" in json.loads(capsys.readouterr().out)

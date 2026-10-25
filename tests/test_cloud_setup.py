"""Cloud preparation must preserve isolation and fail visibly on incomplete setup."""
from __future__ import annotations

import importlib.util
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def tool():
    path = ROOT / "tools/setup_cloud.py"
    assert path.is_file(), "the reusable cloud setup command is missing"
    spec = importlib.util.spec_from_file_location("setup_cloud", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(*args):
    return subprocess.run(["git", *map(str, args)], check=True, capture_output=True, text=True)


def repository(path):
    git("init", "-q", path)
    (path / "README.md").write_text("fixture\n")
    git("-C", path, "add", "README.md")
    git("-C", path, "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
        "commit", "-qm", "fixture")
    return path


def test_history_check_handles_spaces_and_detects_shallow_checkout(tmp_path):
    module = tool()
    origin = repository(tmp_path / "source with spaces")
    assert module.git_receipt(origin)["shallow"] is False
    clone = tmp_path / "shallow checkout"
    git("clone", "-q", "--depth", "1", origin.as_uri(), clone)
    assert module.git_receipt(clone)["shallow"] is True


def test_install_reuses_environment_and_does_not_upgrade_on_resume(tmp_path, monkeypatch):
    module = tool()
    python = module.venv_python(tmp_path)
    python.parent.mkdir(parents=True)
    python.touch()
    calls = []
    monkeypatch.setattr(module.subprocess, "run", lambda argv, **kwargs: calls.append((argv, kwargs)))
    module.install(tmp_path)
    assert len(calls) == 1
    argv, kwargs = calls[0]
    assert argv[0] == str(python)
    assert "--upgrade" not in argv
    assert argv[-1] == ".[test,site,campaign]"
    assert kwargs["cwd"] == tmp_path
    assert kwargs["check"] is True


def test_install_failure_propagates(tmp_path, monkeypatch):
    module = tool()
    python = module.venv_python(tmp_path)
    python.parent.mkdir(parents=True)
    python.touch()

    def fail(argv, **kwargs):
        raise subprocess.CalledProcessError(23, argv)

    monkeypatch.setattr(module.subprocess, "run", fail)
    with pytest.raises(subprocess.CalledProcessError) as error:
        module.install(tmp_path)
    assert error.value.returncode == 23


def test_preflight_rejects_package_imported_from_another_checkout(tmp_path, monkeypatch):
    module = tool()
    repository(tmp_path)
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    receipt = module.preflight(tmp_path, min_free_gib=0)
    assert receipt["ready"] is False
    assert any(c["name"] == "checkout_import" and not c["passed"] for c in receipt["checks"])


def test_preflight_rejects_insufficient_disk_space(tmp_path, monkeypatch):
    module = tool()
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path))
    receipt = module.preflight(ROOT, min_free_gib=10**12)
    assert receipt["ready"] is False
    assert any(c["name"] == "scratch_space" and not c["passed"] for c in receipt["checks"])


def test_cloud_agent_install_applies_the_pinned_linux_resolution_only_there(tmp_path):
    module = tool()
    lock = tmp_path / "cloud/constraints-linux-py312.txt"
    lock.parent.mkdir()
    lock.write_text("numpy==2.5.4\n")
    assert module.constraints(tmp_path, "linux", (3, 12)) == ["-c", str(lock)]
    assert module.constraints(tmp_path, "win32", (3, 12)) == []
    assert module.constraints(tmp_path, "linux", (3, 11)) == []
    shipped = module.ROOT / "cloud/constraints-linux-py312.txt"
    pins = [line for line in shipped.read_text().splitlines() if line.strip() and not line.lstrip().startswith("#")]
    assert pins and all("==" in line for line in pins)
    assert {"numpy", "astropy", "scipy", "pytest"} <= {line.split("==")[0] for line in pins}

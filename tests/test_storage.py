"""cygnus.storage: harness-neutral Drive locations, the committed index and verified uploads (offline)."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

import pytest

from cygnus import storage as S
from cygnus.config import WORKTREE


def _cp(rc=0, out="", err=""):
    return subprocess.CompletedProcess([], rc, out, err)


def _tree(root: Path) -> Path:
    (root / "batch" / "logs").mkdir(parents=True)
    (root / "batch" / "journal.jsonl").write_text('{"event": "end"}\n', encoding="utf-8")
    (root / "batch" / "logs" / "a.log").write_text("ok\n", encoding="utf-8")
    (root / "ledger.sqlite").write_bytes(b"SQLite format 3\x00" + bytes(64))
    return root


@pytest.mark.parametrize("raw,want", [("colab_runs/b1", "colab_runs/b1"), ("Cygnus/colab_runs/b1/", "colab_runs/b1"),
                                      ("batches\\x", "batches/x")])
def test_logical_paths_are_relative_to_the_cygnus_folder(raw, want):
    assert S.logical(raw) == want


@pytest.mark.parametrize("bad", ["", "Cygnus", "../x", "a/../../b", "gdrive:Cygnus/x"])
def test_logical_paths_cannot_leave_cygnus(bad):
    with pytest.raises(S.StorageError):
        S.logical(bad)


def test_rclone_specs_are_told_apart_from_windows_and_posix_paths():
    assert S._is_rclone_spec("gdrive:Cygnus") and S._is_rclone_spec("cygnus:Cygnus")
    assert not S._is_rclone_spec("G:/My Drive/Cygnus") and not S._is_rclone_spec("C:\\Drive\\Cygnus")
    assert not S._is_rclone_spec("/content/drive/MyDrive/Cygnus")


def test_route_prefers_the_environment_then_the_colab_mount_then_rclone(tmp_path):
    no_rclone = lambda *a, **k: pytest.fail("rclone must not be consulted")  # noqa: E731
    r = S.resolve_route(env={"CYGNUS_DRIVE": "gdrive:Cygnus/"}, run=no_rclone, colab_mydrive=tmp_path)
    assert (r.kind, r.base, r.how, r.label) == ("rclone", "gdrive:Cygnus", "CYGNUS_DRIVE", "rclone remote gdrive:")
    r = S.resolve_route(env={"CYGNUS_DRIVE": str(tmp_path)}, run=no_rclone, colab_mydrive=tmp_path)
    assert r.kind == "path" and r.how == "CYGNUS_DRIVE"
    (tmp_path / "Cygnus").mkdir()
    r = S.resolve_route(env={}, run=no_rclone, colab_mydrive=tmp_path)
    assert r.kind == "path" and r.how == "Colab mount"


def test_rclone_auto_detect_takes_the_first_drive_remote_that_has_cygnus(tmp_path):
    calls = []

    def run(cmd, **kw):
        calls.append(cmd[1:])
        if cmd[1] == "listremotes":
            return _cp(out="s3box: s3\nother: drive\nmine: drive\n")
        return _cp(rc=0 if cmd[2] == "mine:Cygnus" else 3)

    r = S.resolve_route(env={}, run=run, colab_mydrive=tmp_path)
    assert r.base == "mine:Cygnus" and r.how == "rclone auto-detect"
    assert ["lsf", "s3box:Cygnus", "--max-depth", "1"] not in calls       # non-drive remotes never probed
    assert S.resolve_route(env={}, run=lambda c, **k: _cp(out="x: drive\n") if c[1] == "listremotes" else _cp(rc=3),
                           colab_mydrive=tmp_path) is None


def test_upload_through_a_mounted_folder_verifies_writes_location_and_indexes(tmp_path, monkeypatch):
    monkeypatch.setenv("CYGNUS_SCRATCH", str(tmp_path / "scratch"))
    local = _tree(tmp_path / "scratch" / "colab_runs" / "b1")
    drive = tmp_path / "drive" / "Cygnus"
    drive.mkdir(parents=True)
    index = tmp_path / "locations.jsonl"
    route = S.Route("path", str(drive), "CYGNUS_DRIVE")
    e = S.upload(local, "colab_runs/b1", kind="colab_run", producer="test", route=route, index=index, commit="a" * 40)
    assert e["id"] == "colab_runs/b1" and e["drive_path"] == "Cygnus/colab_runs/b1" and e["files"] == 3
    assert e["local_copy"] == "scratch:colab_runs/b1"
    assert e["links"]["search"].endswith("q=b1") and e["links"]["folder"] is None     # no xattr off Colab
    assert e["visible_via"]["mounted folder"]["state"] == "visible"
    assert (drive / "colab_runs" / "b1" / "LOCATION.json").is_file() and (local / "LOCATION.json").is_file()
    assert (drive / "colab_runs" / "b1" / "MANIFEST.sha256").is_file()
    assert S.read_index(index) == [e]


def test_upload_refuses_when_drive_reads_back_different_bytes(tmp_path, monkeypatch):
    local = _tree(tmp_path / "l")
    drive = tmp_path / "Cygnus"
    drive.mkdir()
    monkeypatch.setattr(S, "remote_hashes", lambda route, path, run=None: {"ledger.sqlite": "0" * 64})
    with pytest.raises(S.StorageError, match="not read back identically"):
        S.upload(local, "colab_runs/x", kind="colab_run", producer="t", route=S.Route("path", str(drive), "t"),
                 index=tmp_path / "i.jsonl")
    assert not (tmp_path / "i.jsonl").exists()


def test_upload_through_rclone_uses_immutable_copy_hashsum_and_the_parent_listing_for_the_id(tmp_path):
    local = _tree(tmp_path / "l")
    remote: dict[str, bytes] = {}
    calls = []

    def run(cmd, **kw):
        calls.append(cmd[1])
        if cmd[1] == "copy":
            assert "--immutable" in cmd and cmd[3] == "gd:Cygnus/batches/x"
            for f in Path(cmd[2]).rglob("*"):
                if f.is_file():
                    remote[f.relative_to(cmd[2]).as_posix()] = f.read_bytes()
            return _cp()
        if cmd[1] == "hashsum":
            return _cp(out="".join(f"{hashlib.sha256(b).hexdigest()}  {n}\n" for n, b in remote.items()))
        if cmd[1] == "lsjson":
            assert cmd[2] == "gd:Cygnus/batches"
            return _cp(out=json.dumps([{"Name": "x", "ID": "FOLDER123", "IsDir": True}]))
        if cmd[1] == "copyto":
            return _cp()
        pytest.fail(f"unexpected rclone call {cmd}")

    e = S.upload(local, "batches/x", kind="batch", producer="t", route=S.Route("rclone", "gd:Cygnus", "t"),
                 run=run, index=tmp_path / "i.jsonl")
    assert e["drive_folder_id"] == "FOLDER123"
    assert e["links"]["folder"] == "https://drive.google.com/drive/folders/FOLDER123"
    assert calls == ["copy", "hashsum", "lsjson", "copyto"]


def test_each_area_has_one_writer_kind_so_no_duplicate_folders_appear(tmp_path):
    local = _tree(tmp_path / "l")
    with pytest.raises(S.StorageError, match="only through a path route"):
        S.upload(local, "colab_runs/x", kind="colab_run", producer="t", route=S.Route("rclone", "gd:Cygnus", "t"),
                 run=lambda *a, **k: pytest.fail("nothing may be copied"), index=tmp_path / "i.jsonl")
    with pytest.raises(S.StorageError, match="only through a rclone route"):
        S.upload(local, "batches/x", kind="batch", producer="t", route=S.Route("path", str(tmp_path), "t"),
                 index=tmp_path / "i.jsonl")
    with pytest.raises(S.StorageError, match="unknown area"):
        S.upload(local, "misc/x", kind="other", producer="t", route=S.Route("path", str(tmp_path), "t"),
                 index=tmp_path / "i.jsonl")


def test_upsert_merges_visibility_from_different_harnesses(tmp_path):
    index = tmp_path / "i.jsonl"
    e = S.make_entry("colab_runs/b", kind="colab_run", writer="Colab drive.mount", producer="nb")
    e["visible_via"] = {"Colab drive.mount": {"state": "visible", "utc": "t0"}}
    S.upsert(e, index)
    S.record_visibility("colab_runs/b", "rclone remote gdrive:", False, index)
    again = S.make_entry("colab_runs/b", kind="colab_run", writer="Colab drive.mount", producer="nb", files=11)
    got = S.upsert(again, index)
    assert got["files"] == 11
    assert set(got["visible_via"]) == {"Colab drive.mount", "rclone remote gdrive:"}
    assert got["visible_via"]["rclone remote gdrive:"]["state"] == "not_visible"


def test_entries_refuse_machine_paths_and_foreign_links():
    with pytest.raises(S.StorageError, match="scratch-relative"):
        S.make_entry("batches/x", kind="batch", writer="w", producer="p", local_copy="D:/somewhere/x")
    e = S.make_entry("batches/x", kind="batch", writer="w", producer="p")
    e["links"]["folder"] = "https://example.com/x"
    with pytest.raises(S.StorageError, match="unexpected link"):
        S.validate(e)
    with pytest.raises(S.StorageError, match="kind"):
        S.make_entry("batches/x", kind="nope", writer="w", producer="p")


def test_the_committed_index_is_valid_and_carries_no_machine_paths():
    entries = S.read_index(S.INDEX)
    assert entries, "storage/locations.jsonl should list at least the known locations"
    for e in entries:
        S.validate(e)
        blob = json.dumps(e)
        assert ":\\\\" not in blob and "/Users/" not in blob and "AO_Artifacts" not in blob, e["id"]
        assert e["links"]["search"].startswith("https://drive.google.com/drive/search?q=")

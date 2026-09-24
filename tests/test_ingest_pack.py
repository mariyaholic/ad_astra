"""Unit tests for the PackBuilder manifest/budget machinery (no network).

The failed-fetch path uses a closed local port, so no external traffic occurs.
The verify/retire cycle uses rclone against a *local mirror* directory
(skipped if rclone is absent), exercising the exact upload-verification flow
offline. Staged files always live inside the service pack dir; manifest
``dest_rel`` paths are POSIX-style so Drive listings match across OSes.
"""

from __future__ import annotations

import json
import shutil
import socket
from pathlib import Path

import pytest

from cygnus.ingest.netio import md5_file
from cygnus.ingest.pack import (MANIFEST_FIELDS, PackBuilder,
                                _write_manifest_files, ledger_products_csv,
                                retire_local_copies, verify_remote_upload)


@pytest.fixture
def builder(ledger_factory, tmp_scratch):
    led = ledger_factory()
    b = PackBuilder(led, budgets={"mast": 1.0})
    b.quiet = True
    return b


def test_register_and_ledger_row(builder):
    f = builder.pack_dir("mast") / "t" / "alpha.fits"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_bytes(b"0123456789abcdef")
    row = builder.register("mast", "alpha", path=f, url="https://example/alpha.fits",
                           endpoint="test://endpoint", query="q=1", license_="public")
    assert row["state"] == "local"
    assert row["sha256"] and row["md5"]
    assert row["dest_rel"] == "t/alpha.fits"  # POSIX separators in manifests
    prods = builder.ledger.products("mast")
    assert len(prods) == 1
    assert prods[0]["product_id"] == "alpha"
    assert prods[0]["checksum"] == row["sha256"]
    assert builder.bytes_used("mast") == 16


def test_manifest_roundtrip_files(builder):
    rows = [{"service": "mast", "pack_dir": "01_mast", "product_id": "a",
             "dest_rel": "a.fits", "state": "local", "bytes": 3, "sha256": "h",
             "md5": "m", "retrieved_utc": "t", "url": "u", "endpoint": "e",
             "query": "q", "license": "L", "truncated": "", "extra_json": "{}",
             "note": ""}]
    _write_manifest_files(rows, builder.root, "01_mast")
    reread = json.loads((builder.root / "01_mast" / "MANIFEST.json").read_text(encoding="utf-8"))
    assert reread[0]["product_id"] == "a"
    fields_ok = all(k in reread[0] for k in ("service", "dest_rel", "md5", "state"))
    assert fields_ok
    csv_head = (builder.root / "01_mast" / "MANIFEST.csv").read_text(encoding="utf-8")
    assert csv_head.splitlines()[0].split(",")[0] == "service"


def test_failed_fetch_is_recorded_not_silent(builder):
    # bind a port then close it so connections are refused immediately
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    url = f"http://127.0.0.1:{port}/nope.fits"
    row = builder.try_fetch("mast", "ghost", url=url, dest_rel="t/ghost.fits",
                            endpoint="test", query="q", license_="L",
                            max_retries=1, timeout_s=2.0)
    assert row["state"] == "failed"
    assert "fetch error" in row["note"]
    assert not (builder.pack_dir("mast") / "t" / "ghost.fits").exists()


def test_budget_exclusion(builder):
    row = builder.try_fetch("mast", "bigone", url="https://example.invalid/x",
                            dest_rel="big/x.fits", endpoint="e", query="q",
                            license_="L", size_hint=2 * (1 << 30))
    assert row is not None
    assert row["state"] == "excluded"
    assert "budget" in row["note"]


def test_master_and_search_log(tmp_scratch, ledger_factory):
    led = ledger_factory()
    b = PackBuilder(led, pack_root=tmp_scratch / "tier1_pack")
    b.quiet = True
    f = b.pack_dir("mast") / "f.bin"
    f.write_bytes(b"data")
    b.register("mast", "g1", path=f, url="u", endpoint="e")
    m = b.write_master()
    assert b"mast," in m.read_bytes()
    s = b.write_search_log()
    assert s.exists() and "mast" in s.read_text(encoding="utf-8")
    assert b.run_config_sha({"a": 1}) == b.run_config_sha({"a": 1})
    assert b.run_config_sha({"a": 1}) != b.run_config_sha({"a": 2})


def test_ledger_products_csv_export(tmp_scratch, ledger_factory):
    led = ledger_factory()
    b = PackBuilder(led, pack_root=tmp_scratch / "tier1_pack")
    b.quiet = True
    f = b.pack_dir("ned") / "x.bin"
    f.write_bytes(b"zz")
    b.register("NED", "n1", path=f, url="u", endpoint="e", license_="public")
    out = ledger_products_csv(led, tmp_scratch / "export" / "products.csv")
    txt = out.read_text(encoding="utf-8")
    assert "n1" in txt and "NED" in txt


def _has_rclone() -> bool:
    return shutil.which("rclone") is not None


@pytest.mark.skipif(not _has_rclone(), reason="rclone not on PATH")
def test_verify_and_retire_cycle_with_local_rclone(tmp_scratch, ledger_factory):
    """Full register-verify-retire logic driven by rclone against a mirror."""
    led = ledger_factory()
    b = PackBuilder(led, pack_root=tmp_scratch / "tier1_pack")
    b.quiet = True
    a = b.pack_dir("mast") / "a.bin"
    a.write_bytes(b"alpha-bytes")
    c = b.pack_dir("mast") / "sub" / "c.bin"
    c.parent.mkdir(parents=True, exist_ok=True)
    c.write_bytes(b"gamma-bytes")
    b.register("mast", "prod_a", path=a, url="u", endpoint="e")
    b.register("mast", "prod_c", path=c, url="u", endpoint="e")
    b.write_manifest("mast")
    assert md5_file(a) == next(r["md5"] for r in b.rows("mast") if r["product_id"] == "prod_a")

    # In production the mirror is cygnus:Cygnus/data/tier1/<pack_dir>; here it is a
    # local directory rclone reads with the same md5sum interface.
    svc_root = b.pack_dir("mast")
    mirror = tmp_scratch / "mirror_mast"
    shutil.copytree(svc_root, mirror)
    res = verify_remote_upload(b.root, "mast", str(mirror))
    assert res["ok"] is True, res
    assert res["verified"] == 2

    n = retire_local_copies(b.root, "mast", ledger=led)
    assert n == 2
    assert not a.exists() and not c.exists()
    rows = json.loads((svc_root / "MANIFEST.json").read_text(encoding="utf-8"))
    assert all(r["state"] == "drive_only" for r in rows)

    # Re-verification passes against the mirror even though staging is empty —
    # this is exactly the 'host on Drive only' retention state.
    res2 = verify_remote_upload(b.root, "mast", str(mirror))
    assert res2["ok"] is True

    prods = led.products("mast")
    assert all(not p["local_path"] for p in prods)


@pytest.mark.skipif(not _has_rclone(), reason="rclone not on PATH")
def test_retire_refuses_unverified(tmp_scratch, ledger_factory):
    led = ledger_factory()
    b = PackBuilder(led, pack_root=tmp_scratch / "tier1_pack")
    b.quiet = True
    f = b.pack_dir("gaia") / "f.bin"
    f.write_bytes(b"payload")
    b.register("gaia", "g", path=f, url="u", endpoint="e")
    b.write_manifest("gaia")
    with pytest.raises(RuntimeError):
        retire_local_copies(b.root, "gaia", ledger=led)
    assert f.exists()

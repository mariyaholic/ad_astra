"""Unit tests for cygnus.ingest.netio (cybernetic paths only; no network)."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from cygnus.ingest.netio import md5_file, sha256_file, session


def test_sha256_and_md5_of_known_bytes(tmp_path: Path):
    blob = b"cygnus test payload" + b"x" * (1024 * 512 + 7)  # cross several read chunk sizes
    p = tmp_path / "blob.bin"
    p.write_bytes(blob)
    assert sha256_file(p) == hashlib.sha256(blob).hexdigest()
    assert md5_file(p) == hashlib.md5(blob).hexdigest()


def test_session_carries_user_agent():
    s = session()
    assert s.headers.get("User-Agent", "").startswith("cygnus/")

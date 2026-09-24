import os
import time

import pytest

from cygnus.ingest import cleanup_scratch, resolve_scratch


def test_resolve_creates_under_scratch_root(tmp_scratch):
    p = resolve_scratch("mast")
    assert p.is_dir()
    assert p.parent == tmp_scratch


def test_cleanup_refuses_outside_scratch_root(tmp_scratch):
    outside = tmp_scratch.parent
    with pytest.raises(ValueError):
        cleanup_scratch(outside)


def test_cleanup_removes_contents_with_age_filter(tmp_scratch):
    keep = tmp_scratch / "keep.bin"
    keep.write_text("keep-me")
    gone = tmp_scratch / "gone.bin"
    gone.write_text("delete-me")
    old = time.time() - 365 * 24 * 3600
    os.utime(gone, (old, old))

    n = cleanup_scratch(older_than_days=180)
    assert n == 1
    assert gone.exists() is False
    assert keep.exists() is True

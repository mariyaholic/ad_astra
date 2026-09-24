"""Tier-1 collector configuration integrity (offline checks)."""

from __future__ import annotations

import json

from cygnus.ingest.tier1 import (COLLECTORS, DEFAULT_BUDGETS_GB, PACK_DIRS,
                                 SERVICE_ORDER, slug)


def test_service_registry_is_complete_and_disjoint():
    assert sorted(COLLECTORS) == sorted(SERVICE_ORDER)
    assert set(PACK_DIRS) == set(SERVICE_ORDER)
    assert len(set(PACK_DIRS.values())) == len(PACK_DIRS)


def test_budgets_cover_every_service():
    assert set(DEFAULT_BUDGETS_GB) == set(SERVICE_ORDER)
    total = sum(DEFAULT_BUDGETS_GB.values())
    assert 5.0 <= total <= 10.5  # per user instruction: 5–10 GB pack target


def test_slug_sanitizes_names():
    assert slug("KIC 8462852 s0003/SPOC") == "KIC_8462852_s0003_SPOC"
    assert slug("   ") == ""


def test_name_cache_dump_roundtrip(tmp_path):
    from cygnus.ingest.tier1 import _name_cache, write_name_cache

    _name_cache.clear()
    _name_cache["Unit Test Object"] = {
        "ok": True, "ra_deg": 10.0, "dec_deg": -20.0,
        "resolver": "CDS Sesame via astropy SkyCoord.from_name",
        "resolved_utc": "2026-09-24T00:00:00Z",
    }
    p = write_name_cache(tmp_path / "tier1_pack")
    data = json.loads(p.read_text(encoding="utf-8"))
    assert data["Unit Test Object"]["ra_deg"] == 10.0

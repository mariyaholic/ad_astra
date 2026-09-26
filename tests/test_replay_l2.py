"""L2: checksum-pinned replay of committed campaigns (``pytest -m replay``; not in the offline gate).

For a fixed sample of committed known-object campaigns, re-run the science steps through the
multi runner on the archive products already in scratch — never downloading: discovery is replaced
by the committed ``fetch_products`` list, and every product must match its committed SHA-256 — and
compare the science outputs with the committed runner outputs value by value. A reader, screen or
calibration change that moves any number a report quotes fails here. Campaigns whose products are
not in this machine's scratch are skipped (with the reason), never downloaded.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import pytest

pytest.importorskip("yaml")
pytest.importorskip("scipy")
pytest.importorskip("astropy")

from cygnus.config import WORKTREE, scratch_dir
from cygnus.ledger import Ledger

pytestmark = pytest.mark.replay

# a lead with three sectors, a failed positive control, an inconclusive one and a periodic target
SAMPLE = ("toi-2666-01", "toi-1301-02", "toi-125-04", "toi-2003-01")
SCIENCE_STEPS = ("fetch_products", "calibrate_screen", "known_signal_recovery", "residual_screen", "period_aliases")


def _sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _science(res: dict) -> dict:
    scr = res["residual_screen"]["per_product"]
    cal = res["calibrate_screen"]["per_product"]
    known = res["known_signal_recovery"]["per_product"]
    return {
        "screen": {pid: {"k": s["k_mad"], "entries": s["entries"], "outside": s["entries_outside_veto"],
                         "events": s["distinct_events_outside_veto"]} for pid, s in scr.items()},
        "calibration": {pid: {k: c[k] for k in ("null_events_by_k", "k_star", "k_star_at_grid_floor",
                                                 "depth_for_90pct_completeness_ppm", "completeness")} for pid, c in cal.items()},
        "known": {pid: v["epochs"] for pid, v in known.items()},
        "aliases": res["period_aliases"]["candidates"],
    }


@pytest.mark.parametrize("cid", SAMPLE)
def test_committed_campaign_replays_to_the_same_numbers(cid, tmp_path, monkeypatch):
    import yaml

    from cygnus.multi import steps
    from cygnus.multi.runner import run

    src = WORKTREE / "campaigns" / f"{cid}.yaml"
    committed = WORKTREE / "campaigns" / cid / "runner"
    if not src.is_file() or not (committed / "fetch_products.json").is_file():
        pytest.skip(f"{cid}: no committed spec/runner outputs")
    prods = json.loads((committed / "fetch_products.json").read_text(encoding="utf-8"))["result"]["products"]
    stage = scratch_dir(f"campaign_{cid}")
    missing = [pid for pid in prods if not (stage / pid).is_file()]
    if missing:
        pytest.skip(f"{cid}: {len(missing)} product(s) not in scratch ({stage}); L2 never downloads")
    for pid, p in prods.items():
        assert _sha(stage / pid) == p["sha256"], f"{pid}: scratch copy differs from the committed checksum"

    spec = yaml.safe_load(src.read_text(encoding="utf-8"))
    spec["steps"] = [s for s in spec["steps"] if next(iter(s)) in SCIENCE_STEPS]
    spec.pop("record", None)
    (tmp_path / "campaigns").mkdir()
    (tmp_path / "campaigns" / f"{cid}.yaml").write_text(yaml.safe_dump(spec, sort_keys=False), encoding="utf-8")
    listed = [{"product_id": pid, "tic": p.get("tic"), "sector": p.get("sector"),
               "covers_known_epoch": p.get("covers_known_epoch")} for pid, p in prods.items()]

    def no_download(tic, n, t0=None):
        return [dict(d) for d in listed if d["tic"] == tic][:n]

    monkeypatch.setattr(steps, "_discover_spoc_lcs", no_download)
    monkeypatch.setattr("cygnus.ingest.netio.fetch_to_file", lambda *a, **k: pytest.fail("L2 replay tried to download"))
    led = Ledger(tmp_path / "replay.sqlite")
    try:
        run(tmp_path / "campaigns" / f"{cid}.yaml", ledger=led, root=tmp_path, echo=lambda *_: None)
    finally:
        led.close()
    got = {p.stem: json.loads(p.read_text(encoding="utf-8"))["result"] for p in (tmp_path / "campaigns" / cid / "runner").glob("*.json")
           if p.stem in SCIENCE_STEPS}
    want = {s: json.loads((committed / f"{s}.json").read_text(encoding="utf-8"))["result"] for s in SCIENCE_STEPS}
    assert {pid: p["sha256"] for pid, p in got["fetch_products"]["products"].items()} == \
           {pid: p["sha256"] for pid, p in want["fetch_products"]["products"].items()}
    a, b = _science(got), _science(want)
    for key in a:
        assert a[key] == b[key], f"{cid}: {key} drifted from the committed outputs"
    shutil.rmtree(tmp_path / "campaigns", ignore_errors=True)

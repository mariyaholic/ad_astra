"""Budgeted T3 adapters over native tools; no evidence promotion or spectral extraction."""
from __future__ import annotations

import csv
import json
import math
import re
import zipfile
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

from .fileio import sha256_file
from .ledger import now_utc


def _file(root, entry, suffixes):
    from .cloud import inside
    from .config import scratch_dir

    rel = entry.get("path", "")
    path = inside(scratch_dir(), rel[8:]) if rel.startswith("scratch:") else inside(root, rel)
    cap = {".json": 1, ".csv": 8, ".npz": 64}.get(path.suffix, 0) * 1024**2
    if path.suffix not in suffixes or not path.is_file() or path.stat().st_size > cap:
        raise ValueError("T3 input is missing, oversized or has an unsupported file type")
    expected = entry.get("sha256", "")
    if not re.fullmatch(r"[0-9a-f]{64}", expected) or sha256_file(path) != expected:
        raise ValueError("T3 input checksum mismatch")
    return path


def _packet(root, entry, target, suffixes):
    if entry.get("target") != target.get("name") or entry.get("tic") != target.get("tic"):
        raise ValueError("T3 packet target identity differs from the refreshed source")
    event = target.get("defining_events", {}).get(entry.get("event_label"))
    if (event is None or type(entry.get("event_bjd")) not in (int, float) or
            not math.isclose(event, entry["event_bjd"], rel_tol=0, abs_tol=1e-8)):
        raise ValueError("T3 packet event differs from the measured defining event")
    source = entry.get("provenance", {})
    if any(not source.get(k) for k in ("archive", "product_id", "url", "retrieved_utc", "method")):
        raise ValueError("T3 packet lacks exact source provenance")
    url = urlsplit(source["url"])
    stamp = datetime.fromisoformat(source["retrieved_utc"].replace("Z", "+00:00"))
    if url.scheme != "https" or not url.hostname or url.username or url.password or stamp.tzinfo is None:
        raise ValueError("T3 source URL/time provenance is invalid")
    data = _file(root, entry, suffixes)
    if not entry.get("validation"):
        return None, "no checksum-bound input-quality validation receipt"
    validation_path = _file(root, entry["validation"], (".json",))
    validation = json.loads(validation_path.read_text())
    if (validation.get("target") != target.get("name") or validation.get("input_sha256") != entry["sha256"] or
            validation.get("state") != "passed" or not validation.get("checks") or
            not all(c.get("state") == "passed" and c.get("source") for c in validation["checks"])):
        return None, "input-quality receipt is absent/inconclusive/failed or bound to another input"
    return data, None


def _rv(root, entry, target):
    import numpy as np
    from .analysis.rv import fit_transit_tied_orbit

    path, reason = _packet(root, entry, target, (".csv",))
    if path is None:
        return {"ran": False, "state": "not_tested", "note": reason}
    if entry.get("time_standard") != "BJD_TDB" or entry.get("velocity_unit") != "km/s" or entry.get("rv_frame") != "barycentric":
        raise ValueError("RV packet needs BJD_TDB, barycentric velocities and km/s; no implicit conversion")
    from itertools import islice
    with path.open(encoding="utf-8", newline="") as stream:
        rows = list(islice(csv.DictReader(stream), 10001))
    if len(rows) > 10000:
        raise ValueError("RV table exceeds the bounded 10000-row input contract")
    arrays = [np.array([float(r[k]) for r in rows]) for k in ("time_bjd_tdb", "rv_kms", "sigma_kms")]
    if len(rows) < 6 or not all(np.isfinite(a).all() for a in arrays) or np.any(arrays[2] <= 0) or len(np.unique(arrays[0])) < 6:
        raise ValueError("RV fit needs at least six finite distinct epochs with positive uncertainties")
    periods = entry.get("periods_days", [])
    jitters = entry.get("jitters_kms", [0.])
    if not 1 <= len(periods) <= 32 or not 1 <= len(jitters) <= 10 or any(
            type(p) not in (int, float) or not math.isfinite(p) or p <= 0 for p in periods):
        raise ValueError("RV trial-period grid must be finite, positive and bounded")
    if any(type(j) not in (int, float) or not math.isfinite(j) or j < 0 for j in jitters):
        raise ValueError("RV jitter grid must be finite and nonnegative")
    transit = entry.get("event_bjd")
    if transit is None or not math.isfinite(float(transit)):
        raise ValueError("RV fit needs a verified transit epoch")
    result = fit_transit_tied_orbit(*arrays, float(transit), periods, jitters_kms=jitters)
    if not result["fits"]:
        raise ValueError("RV fit emitted no usable conditional fits")
    return {"ran": True, "state": "inconclusive", "result": result, "input_sha256": entry["sha256"],
            "provenance": entry["provenance"], "validation": entry["validation"],
            "note": "Conditional orbit fits only; no period selection, companion mass or independent validation."}


def _prf(root, entry, target):
    import numpy as np
    from .analysis.prf import profile_source_preference

    path, reason = _packet(root, entry, target, (".npz",))
    if path is None:
        return {"ran": False, "state": "not_tested", "note": reason}
    if entry.get("instrument") != "TESS" or entry.get("pixel_unit") != "cutout_pixel" or entry.get("flux_unit") != "electron/s":
        raise ValueError("PRF packet needs TESS, cutout_pixel positions and electron/s image/error units")
    with zipfile.ZipFile(path) as archive:
        if len(archive.infolist()) > 8 or sum(i.file_size for i in archive.infolist()) > 64 * 1024**2:
            raise ValueError("PRF packet exceeds its decompressed memory budget")
    with np.load(path, allow_pickle=False) as data:
        diff, sigma, prf = (np.asarray(data[k], float) for k in ("difference", "sigma", "prf"))
    if (diff.ndim != 2 or sigma.shape != diff.shape or prf.ndim != 2 or max(diff.shape) > 101 or
            prf.shape != (117, 117) or not all(np.isfinite(a).all() for a in (diff, sigma, prf)) or
            np.any(sigma <= 0) or np.any(prf < 0) or prf.sum() <= 0):
        raise ValueError("invalid PRF/difference image/error arrays")
    positions, shifts, floors = entry.get("positions", {}), entry.get("shifts", []), entry.get("floors", [.01, .03, .05])
    if not 2 <= len(positions) <= 20 or target["name"] not in positions or not 1 <= len(shifts) <= 100 or not 2 <= len(floors) <= 10:
        raise ValueError("PRF test needs target/competitor positions and bounded registration/model-floor sensitivity grids")
    for x, y in [*positions.values(), *shifts]:
        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError("PRF position/registration is nonfinite")
    if any(not math.isfinite(f) or f <= 0 for f in floors):
        raise ValueError("PRF model floors must be finite and positive")
    result = profile_source_preference(diff, sigma, prf, positions, shifts=shifts, floors=floors)
    return {"ran": True, "state": "inconclusive", "result": result, "input_sha256": entry["sha256"],
            "provenance": entry["provenance"], "validation": entry["validation"],
            "note": "Source preference under supplied models; no automatic on-target pass or independent-sky claim."}


def _metadata(target, archives):
    from .multi.archives.base import get
    from .multi.archives.base import Target

    queries, results = [], {}
    for name in archives:
        adapter = get(name)
        tap = adapter.tap_csv
        owned_tap = "tap_csv" in vars(adapter)

        def capture(endpoint, query, **kwargs):
            queries.append({"archive": name, "endpoint": endpoint, "query": query, "retrieved_utc": now_utc()})
            return tap(endpoint, query, **kwargs)

        adapter.tap_csv = capture
        try:
            refs = adapter.discover(Target(name=target["name"], ra_deg=float(target["ra_deg"]),
                                           dec_deg=float(target["dec_deg"]), tic=target.get("tic")), limit=20)
            results[name] = {"state": "answered", "products": [r.as_dict() for r in refs]}
        except Exception as exc:
            results[name] = {"state": "unavailable", "error": f"{type(exc).__name__}: {exc}"}
        finally:
            if owned_tap:
                adapter.tap_csv = tap
            else:
                delattr(adapter, "tap_csv")
    return {"ran": all(r["state"] == "answered" for r in results.values()), "state": "inconclusive",
            "archives": results, "queries": queries,
            "note": "Metadata only. A cone/box match does not establish source identity, public bytes or RV precision."}


def run_diagnostics(root, record, inputs, requested, *, target=None, archives=("koa",)):
    """Report each requested test. Missing inputs never count as executed/passed."""
    target = target or next(iter(record.get("targets", [])), {})
    tests = {}
    for name in requested:
        if name not in ("archive_metadata", "rv_fit", "prf_source_fit"):
            raise ValueError("unsupported T3 diagnostic")
        if name != "archive_metadata" and not inputs.get(name):
            tests[name] = {"ran": False, "state": "not_tested", "note": "no provenance-bound validated input packet"}
        elif not target.get("name"):
            tests[name] = {"ran": False, "state": "not_tested", "note": "no exact target identity"}
        elif name == "archive_metadata":
            tests[name] = _metadata(target, archives)
        else:
            tests[name] = (_rv if name == "rv_fit" else _prf)(Path(root), inputs[name], target)
    return {"schema": "cygnus.cloud_diagnostics/1", "tests": tests,
            "complete": bool(tests) and all(row["ran"] for row in tests.values()),
            "note": "Execution completeness only; input-quality receipts are declarations whose sources require scientific review."}

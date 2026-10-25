"""Finite public-archive scouting and bounded acquisition before scientific T0.

Use ``python -m cygnus.cloud sources/scout/acquire``. Discovery, access, file
integrity, source identity and scientific eligibility are separate evidence.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import math
import os
import re
import shutil
import sys
import time
from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path
from urllib.parse import urlsplit

from .cloud import FROZEN, code_identity, digest, inside, supervise
from .config import scratch_dir
from .fileio import atomic_write_json, atomic_write_text, sha256_file
from .ledger import now_utc

CATALOGUES = {"gaia", "vizier", "simbad", "ned", "irsa", "exoarchive"}
PRODUCT_SOURCES = {"mast", "skyview", "legacysurvey", "eso"}
DEFAULT_SOURCES = sorted(CATALOGUES | PRODUCT_SOURCES | {"koa", "skybot", "horizons", "sbdb", "mpc"})


def inventory():
    """Explicit implementation coverage; historical verification tags are not health probes."""
    from .multi.archives.base import all_adapters
    result = {}
    for name, adapter in all_adapters().items():
        if name in CATALOGUES:
            mode, reason = "catalogue", "bounded catalogue rows; source IDs remain distinct across catalogues"
        elif name in PRODUCT_SOURCES:
            mode, reason = "products", "public product discovery/download; availability and integrity checked per product"
        elif name == "koa":
            mode, reason = "metadata", "HIRES metadata table; raw/calibration retrieval is a separate specialist route"
        elif name in {"horizons", "sbdb", "mpc", "skybot"}:
            mode, reason = "context", "requires a named solar-system object or an explicit UTC observation epoch"
        elif "earth_observation" in adapter.capabilities_list():
            mode, reason = "outside_scope", "Earth-observation/AOI service; not a sky-target archive; account routes are not wired here"
        else:
            mode, reason = "manual", "reachability/viewer/observing route, not automatic archived sky-product retrieval"
        result[name] = {"mode": mode, "reason": reason, "description": adapter.description}
    for name, reason in {
        "esasky": "browser/multi-mission viewer; use archive-backed downloads, never disable TLS",
        "esa_jwst": "separate mirror adapter absent; public JWST products use the canonical MAST route",
        "aladin": "viewer; catalogue data use VizieR/SIMBAD, images use their source archives",
        "aws_open_eo": "Earth-observation bucket/AOI route, outside astronomical sky-target scope",
        "space_track": "account-based satellite element service; no anonymous download adapter",
        "proposal_time": "new observing proposals/requests require specific user authorization",
    }.items():
        result[name] = {"mode": "manual", "reason": reason, "description": reason}
    return result


def normalize_config(value):
    c = deepcopy(value)
    allowed = {"schema", "sources", "bootstrap_top", "field_limit", "target_limit", "rows_per_catalogue",
               "products_per_source", "cone_arcsec", "max_jobs", "budget", "fields", "solar_objects",
               "epoch_utc", "observer", "mast_collections"}
    if c.get("schema") != "cygnus.scout/1" or set(c) - allowed:
        raise ValueError("invalid scouting configuration schema/keys")
    defaults = {"sources": DEFAULT_SOURCES, "bootstrap_top": 100, "field_limit": 1, "target_limit": 3,
                "rows_per_catalogue": 10, "products_per_source": 2, "cone_arcsec": 60., "max_jobs": 100,
                "fields": [], "solar_objects": [], "mast_collections": ["TESS", "Kepler", "K2", "HST", "JWST"]}
    for k, v in defaults.items():
        c.setdefault(k, v)
    for k, maximum in {"bootstrap_top": 1000, "field_limit": 10, "target_limit": 20,
                       "rows_per_catalogue": 100, "products_per_source": 10, "max_jobs": 500}.items():
        if type(c[k]) is not int or not 1 <= c[k] <= maximum:
            raise ValueError(f"{k} must be a positive bounded integer (maximum {maximum})")
    if type(c["cone_arcsec"]) not in (int, float) or not math.isfinite(c["cone_arcsec"]) or not 0 < c["cone_arcsec"] <= 3600:
        raise ValueError("cone_arcsec must be finite and within (0,3600]")
    if (not isinstance(c["sources"], list) or not c["sources"] or len(set(c["sources"])) != len(c["sources"]) or
            set(c["sources"]) - set(inventory())):
        raise ValueError("unknown/duplicate source selection")
    if not set(c["mast_collections"]) <= {"TESS", "Kepler", "K2", "HST", "JWST"}:
        raise ValueError("unsupported MAST collection")
    budget = {"scratch_mb": 512, "product_mb": 32, "job_seconds": 180, "run_seconds": 1800, "min_free_mb": 1024,
              **c.get("budget", {})}
    if set(budget) != {"scratch_mb", "product_mb", "job_seconds", "run_seconds", "min_free_mb"} or any(
            type(v) not in (int, float) or not math.isfinite(v) or v <= 0 for v in budget.values()):
        raise ValueError("scout budget must have finite positive fields")
    if budget["product_mb"] > budget["scratch_mb"]:
        raise ValueError("per-product budget exceeds total scratch budget")
    c["budget"] = budget
    if not isinstance(c["fields"], list) or len(c["fields"]) > c["field_limit"]:
        raise ValueError("too many explicit sky fields")
    for f in c["fields"]:
        if not f.get("name") or not f.get("position_source") or not coordinates(f.get("ra_deg"), f.get("dec_deg")):
            raise ValueError("fields need valid degrees and declared source provenance")
    if not c["fields"] and "exoarchive" not in c["sources"]:
        raise ValueError("without explicit fields the fresh TOI bootstrap source must be enabled")
    if not isinstance(c["solar_objects"], list) or len(c["solar_objects"]) > 10 or any(
            not isinstance(s, str) or not s.strip() or len(s) > 80 for s in c["solar_objects"]):
        raise ValueError("solar_objects must be a bounded list of exact designations")
    if c.get("epoch_utc"):
        from datetime import datetime
        stamp = datetime.fromisoformat(c["epoch_utc"].replace("Z", "+00:00"))
        if stamp.utcoffset() is None or stamp.utcoffset().total_seconds() != 0:
            raise ValueError("SkyBoT epoch must explicitly be UTC")
        if not re.fullmatch(r"[A-Za-z0-9]{3}", c.get("observer", "500")):
            raise ValueError("observer must be an explicit IAU/MPC code")
    return c


def coordinates(ra, dec):
    try:
        return math.isfinite(float(ra)) and math.isfinite(float(dec)) and 0 <= float(ra) < 360 and -90 <= float(dec) <= 90
    except (ValueError, TypeError):
        return False


def _bootstrap(config, fetch):
    from .targets import EXO_TAP, TOI_COLUMNS, build_queue
    query = (f"SELECT TOP {config['bootstrap_top']} {', '.join(TOI_COLUMNS)} FROM toi "
             "WHERE tfopwg_disp IN ('PC','APC') AND pl_tranmid IS NOT NULL AND st_tmag IS NOT NULL "
             "ORDER BY st_tmag ASC, toi ASC")
    stamp = now_utc()
    queries = [{"endpoint": EXO_TAP, "query": query, "retrieved_utc": stamp}]
    try:
        rows = fetch(query)
    except Exception as exc:
        return {"state": "unavailable", "targets": [], "products": [], "excluded": [], "queries": queries,
                "error": f"{type(exc).__name__}: {exc}"}
    valid, excluded = [], []
    for row in rows:
        try:
            if (not re.fullmatch(r"\d+\.\d+", str(row.get("toi", ""))) or int(float(row["tid"])) <= 0 or
                    float(row.get("pl_trandurh") or 0) < 0 or float(row.get("pl_trandep") or 0) < 0):
                raise ValueError("invalid identity, duration or depth")
            valid.append(row)
        except (ValueError, TypeError, KeyError, OverflowError):
            excluded.append({"name": f"TOI-{row.get('toi', 'unusable row')}", "reason": "invalid catalogue identity/duration/depth"})
    # The native ranking is applied only within this declared brightness-limited sample.
    result = build_queue({"top": config["bootstrap_top"]}, fetch=lambda q: valid)
    targets = []
    from .multi.scaffold import slug_for
    for row in result["queue"]:
        if slug_for(row["name"]) in FROZEN or not coordinates(row["ra_deg"], row["dec_deg"]):
            excluded.append({"name": row["name"], "reason": "frozen/retracted target or unusable coordinates"})
            continue
        targets.append({**row, "source": "exoarchive", "source_id": row["name"], "route": "transit",
                        "frame": "ICRS", "position_epoch": "J2015.5", "position_source": "NASA Exoplanet Archive TOI table",
                        "catalogue_query": query, "catalogue_retrieved_utc": stamp})
    excluded += [{"name": n, "reason": why} for n, why in result["unranked"]]
    return {"state": "answered" if rows else "answered_empty", "targets": targets, "products": [],
            "excluded": excluded, "queries": queries, "raw_rows": rows,
            "selection": "top brightness-limited TOI sample, then native heuristic rank; not a complete sky census"}


def bootstrap(config, fetch=None):
    from .targets import _fetch
    return _bootstrap(config, fetch or _fetch)


def catalogue_targets(source, rows, field):
    columns = {"gaia": ("source_id", "ra", "dec"), "simbad": ("main_id", "ra", "dec"),
               "vizier": ("Name", "RAJ2000", "DEJ2000"), "ned": ("prefname", "ra", "dec"),
               "irsa": ("designation", "ra", "dec")}
    if source not in columns:
        return []
    key, racol, deccol = columns[source]
    result = []
    for row in rows:
        if not row.get(key) or not coordinates(row.get(racol), row.get(deccol)):
            continue
        result.append({"name": f"{source}:{row[key]}", "source": source, "source_id": str(row[key]),
                       "ra_deg": float(row[racol]), "dec_deg": float(row[deccol]), "frame": "ICRS",
                       "position_epoch": f"J{row['ref_epoch']}" if row.get("ref_epoch") else "unverified",
                       "position_source": f"{source} returned row; no proper-motion identity merge",
                       "field": field, "route": "catalogue_review", "source_row": row,
                       "rationale": "bounded field catalogue sample; selection is not anomaly significance"})
    return result


def merge_targets(targets):
    merged = {}
    for target in targets:
        key = (target["source"], target["source_id"])
        if key not in merged:
            merged[key] = deepcopy(target)
        elif (merged[key]["ra_deg"], merged[key]["dec_deg"]) != (target["ra_deg"], target["dec_deg"]):
            merged[key]["route"] = "identity_review"
            merged[key]["identity_conflict"] = True
    return list(merged.values())


@contextmanager
def trace(adapter, records):
    """Capture public request selections without headers, session state or credentials."""
    originals = {}
    for name in ("tap_csv", "http_get", "http_post", "http_get_body"):
        if not hasattr(adapter, name):
            continue
        original = getattr(adapter, name)
        originals[name] = (original, name in vars(adapter))
        def traced(*args, _call=original, _name=name, **kwargs):
            records.append({"operation": _name, "endpoint": args[0] if args else None,
                            "query": args[1] if len(args) > 1 else kwargs.get("data") or kwargs.get("params"),
                            "retrieved_utc": now_utc()})
            return _call(*args, **kwargs)
        setattr(adapter, name, traced)
    try:
        yield
    finally:
        for name, (method, owned) in originals.items():
            if owned:
                setattr(adapter, name, method)
            else:
                delattr(adapter, name)


def discover(job):
    from .multi.archives.base import Target, get
    source, target = job["source"], job["target"]
    records, products, targets = [], [], []
    adapter = get(source)
    try:
        with trace(adapter, records):
            position = (Target(target["name"], None, None) if source in {"horizons", "sbdb", "mpc"}
                        else Target.from_mapping(target))
            refs = adapter.discover(position, limit=job["limit"], **job["options"])
        for ref in refs:
            products.append({"target": target, "ref": ref.as_dict(), "selection": job["options"], "queries": records})
            targets += catalogue_targets(source, ref.extra.get("rows", []), target["name"])
        has_rows = any(r.extra.get("rows") for r in refs)
        empty_inline = bool(refs) and all(r.extra.get("inline") and "rows" in r.extra for r in refs) and not has_rows
        return {"state": "answered_empty" if not refs or empty_inline else "planned" if not records else "answered", "products": products,
                "targets": targets, "queries": records,
                "note": "selection-specific response; empty is not archive-wide absence; spatial association is not identity"}
    except Exception as exc:
        return {"state": "unavailable", "products": [], "targets": [], "queries": records,
                "error": f"{type(exc).__name__}: {exc}"}


def capsule(root, plan):
    return inside(root, f"reports/cloud-scout/{plan['id']}")


def state_path(root, plan):
    return inside(root, f"state/cloud_scout/{plan['id']}")


def managed_scratch(plan):
    return scratch_dir(f"cloud_scout/{plan['id']}")


def _plan(root, value):
    if isinstance(value, (str, Path)):
        path = Path(value)
        if not path.is_absolute():
            path = inside(root, path.as_posix())
        plan = json.loads(path.read_text())
        body = {k: v for k, v in plan.items() if k != "id"}
        if (plan.get("schema") != "cygnus.scout_plan/1" or plan.get("id") != "scout-" + digest(body)[:16] or
                path.resolve() != (state_path(root, plan) / "PLAN.json").resolve() or plan["code"] != code_identity()):
            raise ValueError("scout source/runtime lineage changed")
        return plan
    body = {"schema": "cygnus.scout_plan/1", "created_utc": now_utc(), "config": normalize_config(value),
            "code": code_identity()}
    plan = {"id": "scout-" + digest(body)[:16], **body}
    atomic_write_json(state_path(root, plan) / "PLAN.json", plan)
    return plan


class Jobs:
    """One writer; parent alone certifies jobs after supervised resource checks."""
    def __init__(self, root, plan, executor=None):
        self.root, self.plan, self.executor = Path(root), plan, executor or supervised_executor
        self.started, self.count = time.monotonic(), 0
        self.receipts = {}

    def run(self, descriptor):
        key = digest(descriptor)[:24]
        desc = deepcopy({"key": key, "plan_sha256": digest(self.plan), **descriptor})
        output = capsule(self.root, self.plan) / "jobs" / f"{key}.json"
        cp = state_path(self.root, self.plan) / "checkpoints" / f"{key}.json"
        if cp.exists():
            saved = json.loads(cp.read_text())
            if saved["job"] != desc or not output.exists() or saved["sha256"] != sha256_file(output):
                raise ValueError("scout checkpoint changed or hash mismatch")
            result = json.loads(output.read_text())
            if result.get("sha256"):
                _verify_file(result)
            self.receipts[key] = deepcopy(saved)
            return result
        self.count += 1
        remaining = self.plan["config"]["budget"]["run_seconds"] - (time.monotonic() - self.started)
        if self.count > self.plan["config"]["max_jobs"] or remaining <= 0:
            return {"state": "budget_stopped", "products": [], "targets": [], "note": "job/run budget exhausted"}
        job_path = state_path(self.root, self.plan) / "jobs" / f"{key}.json"
        atomic_write_json(job_path, desc)
        result = self.executor(self.root, self.plan, desc, job_path, output, remaining)
        if not isinstance(result, dict) or "state" not in result:
            raise ValueError("invalid scout job result")
        if result["state"] not in ("budget_stopped", "failed", "unavailable"):
            atomic_write_json(output, result)
            saved = {"job": desc, "sha256": sha256_file(output), "verified_utc": now_utc()}
            atomic_write_json(cp, saved)
            self.receipts[key] = deepcopy(saved)
        else:
            atomic_write_json(output, result)
        return result


def direct_executor(root, plan, job, job_path, output, remaining):
    """In-process seam for offline tests only; CLI always supervises a child."""
    result = execute_job(root, plan, job)
    atomic_write_json(output, result)
    return result


def supervised_executor(root, plan, job, job_path, output, remaining):
    budget = plan["config"]["budget"]
    log = state_path(root, plan) / "logs" / f"{job['key']}.{time.time_ns()}.log"
    argv = [sys.executable, "-m", "cygnus.cloud_scout", "worker", str(root),
            str(state_path(root, plan) / "PLAN.json"), str(job_path), str(output)]
    result = supervise(argv, root, log, managed_scratch(plan), env={**os.environ, "MPLBACKEND": "Agg",
                       "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1"},
                       timeout_s=min(remaining, budget["job_seconds"]),
                       max_bytes=int(budget["scratch_mb"] * 1024**2), min_free_bytes=int(budget["min_free_mb"] * 1024**2))
    with (state_path(root, plan) / "ATTEMPTS.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps({"job": job["key"], "utc": now_utc(), **result}) + "\n")
    if result["state"] != "ok" or not output.exists():
        return {"state": result["state"] if result["state"] != "ok" else "failed", "products": [], "targets": [],
                "note": result.get("reason") or "worker failed; inspect ignored attempt log", "resource": result}
    return {**json.loads(output.read_text()), "resource": result}


def _claimable(root, target):
    from .multi.scaffold import slug_for
    cid = slug_for(target["name"])
    if cid in FROZEN or (Path(root) / "campaigns" / f"{cid}.yaml").exists() or (Path(root) / "campaigns" / cid / "REJECTION.md").exists():
        return False
    for path in (Path(root) / "state/cloud_runs").glob("*/PLAN.json"):
        if cid in json.loads(path.read_text())["targets"]:
            return False
    return True


def scout(root, value, *, executor=None):
    from .batch import LedgerLock
    root = Path(root).resolve()
    plan = _plan(root, value)
    lock = LedgerLock(state_path(root, plan) / "writer")
    lock.acquire()
    try:
        previous = capsule(root, plan) / "SCOUT.json"
        if previous.exists():
            saved = json.loads((state_path(root, plan) / "SCOUT_RECEIPT.json").read_text())
            if saved != {"sha256": sha256_file(previous), "plan_sha256": digest(plan)}:
                raise ValueError("scout receipt changed; refusing to overwrite")
        jobs = Jobs(root, plan, executor)
        c = plan["config"]
        sources = {name: {**row, "state": "not_requested" if name not in c["sources"] else "not_tested"}
                   for name, row in inventory().items()}
        first = jobs.run({"kind": "bootstrap"}) if "exoarchive" in c["sources"] or not c["fields"] else {"targets": [], "products": [], "state": "not_requested"}
        targets = deepcopy(first.get("targets", []))
        excluded = first.get("excluded", [])
        seeds = [t for t in targets if _claimable(root, t)]
        excluded += [{"name": t["name"], "reason": "already claimed/analysed"} for t in targets if t not in seeds]
        targets = seeds
        fields = c["fields"] or seeds[:c["field_limit"]]
        results = [{"source": "exoarchive", "result": first}]
        products = []
        for source in c["sources"]:
            if source not in CATALOGUES - {"exoarchive"}:
                continue
            for field in fields:
                job = {"kind": "discover", "source": source, "target": field, "limit": c["rows_per_catalogue"],
                       "options": {"radius_arcsec": c["cone_arcsec"]}}
                found = jobs.run(job)
                results.append({"source": source, "result": found})
                targets += deepcopy(found.get("targets", []))
                products += found.get("products", [])
        targets = merge_targets(targets)
        # Round-robin source diversity is explicit ordering, not a discovery score.
        pools = {s: [t for t in targets if t["source"] == s] for s in ["exoarchive", *sorted(CATALOGUES - {"exoarchive"})]}
        selected = []
        while len(selected) < c["target_limit"] and any(pools.values()):
            for pool in pools.values():
                if pool and len(selected) < c["target_limit"]:
                    selected.append(pool.pop(0))
        if not selected:
            selected = fields[:c["target_limit"]]
        for target in selected:
            for source in c["sources"]:
                if source not in PRODUCT_SOURCES | {"koa"}:
                    continue
                options = [{"radius_arcsec": c["cone_arcsec"]}]
                if source == "mast":
                    options = [{"collection": name, "provenance": "SPOC" if name == "TESS" else "",
                                "subgroup": "LC" if name == "TESS" else "LLC" if name in ("Kepler", "K2") else "I2D" if name == "JWST" else "DRZ,DRC",
                                "dataproduct_type": "image" if name in ("HST", "JWST") else "timeseries",
                                **({} if name == "TESS" and target.get("tic") else {"radius_arcsec": c["cone_arcsec"]})}
                               for name in c["mast_collections"]]
                elif source == "skyview":
                    options = [{"size_deg": c["cone_arcsec"] / 1800, "pixels": 128, "surveys": ["DSS2 Blue"]}]
                elif source == "legacysurvey":
                    options = [{"size_arcsec": min(120, c["cone_arcsec"] * 2)}]
                elif source == "koa":
                    options = [{"box_arcsec": c["cone_arcsec"]}]
                for option in options:
                    found = jobs.run({"kind": "discover", "source": source, "target": target,
                                      "limit": c["products_per_source"], "options": option})
                    results.append({"source": source, "result": found})
                    products += found.get("products", [])
            if "irsa" in c["sources"]:
                found = jobs.run({"kind": "discover", "source": "irsa", "target": target, "limit": 1,
                                  "options": {"mode": "ztf", "radius_arcsec": min(5, c["cone_arcsec"])}})
                results.append({"source": "irsa", "result": found})
                products += found.get("products", [])
        for source in c["sources"]:
            if source in {"horizons", "sbdb", "mpc"}:
                for name in c["solar_objects"]:
                    found = jobs.run({"kind": "discover", "source": source,
                                      "target": {"name": name, "source": "solar_designation",
                                                 "position_source": "name-only context; no sky position supplied"},
                                      "limit": 1, "options": {}})
                    results.append({"source": source, "result": found})
                    products += found.get("products", [])
            elif source == "skybot" and c.get("epoch_utc"):
                for field in fields:
                    found = jobs.run({"kind": "discover", "source": source, "target": field,
                                      "limit": c["rows_per_catalogue"], "options": {"epoch_iso": c["epoch_utc"],
                                      "location": c.get("observer", "500"), "radius_arcsec": c["cone_arcsec"]}})
                    results.append({"source": source, "result": found})
                    products += found.get("products", [])
        for name, row in sources.items():
            matching = [r["result"]["state"] for r in results if r["source"] == name]
            if matching:
                row["state"] = matching[0] if len(set(matching)) == 1 else "partial" if any(
                    s in ("unavailable", "failed", "budget_stopped") for s in matching) else "answered"
                row["attempt_states"] = matching
            elif row["state"] == "not_tested":
                row["reason"] += "; no suitable field, designation/epoch, or automatic adapter for this request"
        for index, target in enumerate(targets, 1):
            target["scout_rank"] = index
        receipt = {"schema": "cygnus.scout_result/1", "id": plan["id"], "plan_sha256": digest(plan),
                   "targets": targets, "retrieval_targets": selected, "products": products, "sources": sources,
                   "attempts": results, "excluded": excluded, "fields": fields, "checkpoints": jobs.receipts}
        output = capsule(root, plan) / "SCOUT.json"
        if output.exists() and json.loads(output.read_text()) != receipt:
            # Failed jobs may gain actual results on an explicit resume; preserve history.
            from .fileio import archive_previous
            archive_previous(output, "previous_attempt")
        atomic_write_json(output, receipt)
        atomic_write_json(state_path(root, plan) / "SCOUT_RECEIPT.json",
                          {"sha256": sha256_file(output), "plan_sha256": digest(plan)})
        write_report(root, plan, receipt)
        return receipt
    finally:
        lock.release()


def _public_url(url):
    p = urlsplit(url)
    if p.scheme != "https" or not p.hostname or p.username or p.password:
        raise ValueError("expected a credential-free public HTTPS archive URL")
    return url


def _ref(value):
    from .multi.archives.base import ProductRef
    return ProductRef(**value)


def _data_path(plan, product):
    ref = product["ref"]
    suffix = ".fits" if "fits" in ref["format"] or ref["format"] in ("spoc_lc", "kepler_lc", "tess_lc", "eso_spectrum") else ".vot" if ref["format"] == "ztf_lc" else ".csv" if ref["format"] in ("csv", "table") else ".json" if ref["format"] == "json" else ".txt"
    return managed_scratch(plan) / "products" / (_product_key(ref) + suffix)


def _product_key(ref):
    if ref.get("url") and not ref.get("extra", {}).get("inline"):
        return digest({k: ref.get(k) for k in ("archive", "product_id", "url", "format", "expected_sha256")})
    return digest(ref)


def _verify_file(result):
    if not str(result.get("path", "")).startswith("scratch:"):
        raise ValueError("acquired product lacks a portable scratch path")
    path = inside(scratch_dir(), result["path"][8:])
    if not path.is_file() or path.stat().st_size != result["bytes"] or sha256_file(path) != result["sha256"]:
        raise ValueError("acquired product missing or changed; checksum verification failed")
    return path


def verified_acquisition(root, path):
    path = Path(path)
    if not path.is_absolute():
        path = inside(root, path.as_posix())
    result = json.loads(path.read_text())
    plan = _plan(root, state_path(root, result) / "PLAN.json")
    out = capsule(root, plan)
    saved = json.loads((state_path(root, plan) / "ACQUISITION_RECEIPT.json").read_text())
    if (path.resolve() != (out / "ACQUISITION.json").resolve() or result.get("schema") != "cygnus.acquisition/1" or
            saved != {"sha256": sha256_file(path), "plan_sha256": digest(plan),
                      "queue_sha256": sha256_file(out / "TRANSIT_QUEUE.csv")} or
            result["scout_sha256"] != sha256_file(out / "SCOUT.json")):
        raise ValueError("acquisition receipt/queue lineage changed")
    for key, cp in result["checkpoints"].items():
        if cp != json.loads((state_path(root, plan) / "checkpoints" / f"{key}.json").read_text()) or cp["sha256"] != sha256_file(out / "jobs" / f"{key}.json"):
            raise ValueError("acquisition checkpoint changed")
    for row in result["products"]:
        if row.get("sha256"):
            _verify_file(row)
    return result


def bridge_config(root, config, path):
    """Only verified acquired SPOC inputs can feed the existing transit controller."""
    result = verified_acquisition(root, path)
    out = capsule(root, result)
    if not any(r.get("eligible") and r.get("route") == "transit" for r in result["products"]):
        raise ValueError("no acquired target passed transit input eligibility; review other queues")
    return {**config, "queue": (out / "TRANSIT_QUEUE.csv").relative_to(root).as_posix(),
            "acquisition": {"path": (out / "ACQUISITION.json").relative_to(root).as_posix(),
                            "sha256": sha256_file(out / "ACQUISITION.json")}}


def acquisition_pins(root, plan, cid):
    entry = plan["config"].get("acquisition")
    if not entry:
        return []
    path = inside(root, entry["path"])
    if sha256_file(path) != entry["sha256"]:
        raise ValueError("acquisition manifest hash changed")
    result = verified_acquisition(root, path)
    target = plan["targets"][cid]
    return [row for row in result["products"] if row.get("eligible") and row.get("route") == "transit" and
            row["product"]["target"]["name"] == target["name"] and
            int(row["product"]["target"]["tic"]) == int(target["tic"])]


def pinned_inputs(root, plan, cid):
    # Reading the manifest does not resolve source scratch in a worker, whose
    # scratch root is deliberately different. The parent already verifies bytes.
    entry = plan["config"].get("acquisition")
    if not entry:
        return []
    path = inside(root, entry["path"])
    if sha256_file(path) != entry["sha256"]:
        raise ValueError("acquisition manifest hash changed")
    target = plan["targets"][cid]
    result = json.loads(path.read_text())
    rows = [r for r in result["products"] if r.get("eligible") and r.get("route") == "transit" and
            r["product"]["target"]["name"] == target["name"] and
            int(r["product"]["target"]["tic"]) == int(target["tic"])]
    if not rows:
        raise ValueError("selected target has no acquired pinned SPOC input")
    return [{"archive": "MAST", "product_id": r["product"]["ref"]["product_id"],
             "url": r["product"]["ref"]["url"], "format": "spoc_lc", "kind": "lightcurve",
             "target": target["name"], "tic": int(target["tic"]), "expected_sha256": r["sha256"],
             "expected_bytes": r["bytes"]} for r in rows]


def seed_products(root, plan, cid, destination):
    rows = acquisition_pins(root, plan, cid)
    Path(destination).mkdir(parents=True, exist_ok=True)
    budget = plan["config"]["budget"]
    occupied = sum(p.stat().st_size for p in Path(destination).rglob("*") if p.is_file())
    missing = sum(r["bytes"] for r in rows if not (Path(destination) / f"campaign_{cid}" / r["product"]["ref"]["product_id"]).exists())
    if occupied + missing > budget["scratch_mb"] * 1024**2 or shutil.disk_usage(destination).free - missing < budget["min_free_mb"] * 1024**2:
        raise ValueError("acquired cache copy would breach worker scratch/free-space budget")
    for row in rows:
        source = _verify_file(row)
        name = row["product"]["ref"]["product_id"]
        if Path(name).name != name or ":" in name or "\\" in name:
            raise ValueError("unsafe archive product filename")
        path = inside(destination, f"campaign_{cid}/{name}")
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            if sha256_file(path) != row["sha256"]:
                raise ValueError("worker cached acquired product changed")
        else:
            # Keep the acquired immutable source and worker cache independent.
            # A later scientific tool writing in-place must not alter acquisition.
            shutil.copyfile(source, path)
        if sha256_file(path) != row["sha256"]:
            raise ValueError("worker cache copy failed checksum verification")
    return pinned_inputs(root, plan, cid)


def fetch_product(product, path, cap):
    from .multi.archives.base import Target, get
    from .ingest.netio import fetch_to_file
    target, ref = product["target"], _ref(product["ref"])
    adapter = get(ref.archive)
    records = []
    base = {"product": product, "eligible": False, "route": "input_review", "queries": records}
    if ref.size_bytes and ref.size_bytes > cap:
        return {**base, "state": "excluded_size", "note": "metadata size exceeds remaining/per-product budget"}
    try:
        with trace(adapter, records):
            if ref.archive == "skyview":
                from astroquery.skyview import SkyView
                import astropy.units as u
                parameters = {"position": ref.extra["position"], "survey": [ref.extra["survey"]],
                              "coordinates": "J2000", "projection": "Tan", "pixels": str(ref.extra["pixels"]),
                              "width": ref.extra["size_deg"] * u.deg, "height": ref.extra["size_deg"] * u.deg,
                              "cache": False}
                records.append({"operation": "skyview_image_list", "endpoint": SkyView.URL,
                                "query": {k: str(v) for k, v in parameters.items()}, "retrieved_utc": now_utc()})
                urls = SkyView.get_image_list(**parameters)
                if not urls:
                    return {**base, "state": "not_tested", "note": "SkyView returned no cutout for this selection"}
                url = sorted(urls)[0]
                records.append({"operation": "download", "endpoint": url, "retrieved_utc": now_utc()})
                download = fetch_to_file(_public_url(url), path, max_bytes=cap, max_retries=1, timeout_s=60)
                if download.get("truncated"):
                    return {**base, "state": "budget_stopped", "note": "truncated SkyView cutout; never eligible"}
            elif ref.url and ref.archive != "eso":
                records.append({"operation": "download", "endpoint": ref.url, "retrieved_utc": now_utc()})
                download = fetch_to_file(_public_url(ref.url), path, max_bytes=cap, max_retries=1, timeout_s=60)
                if download.get("truncated"):
                    return {**base, "state": "budget_stopped", "note": "truncated download retained in scratch; never eligible"}
            elif ref.archive == "eso" and ref.url:
                from .ingest.tap import parse_votable_bytes
                answer = adapter.http_get(_public_url(ref.url), timeout=60)
                answer.raise_for_status()
                table = parse_votable_bytes(answer.content)
                choices = []
                if table is not None:
                    for row in table:
                        semantics = str(row["semantics"]) if "semantics" in table.colnames else ""
                        if semantics not in ("#this", "http://www.ivoa.net/rdf/datalink/core#this"):
                            continue
                        url = str(row["access_url"])
                        if url and url != "--":
                            choices.append(url)
                if not choices:
                    return {**base, "state": "not_tested", "note": "no science #this Datalink URL; metadata is not public bytes"}
                url = sorted(choices)[0]
                download = fetch_to_file(_public_url(url), path, max_bytes=cap, max_retries=1, timeout_s=60)
                records.append({"operation": "download", "endpoint": url, "retrieved_utc": now_utc()})
                if download.get("truncated"):
                    return {**base, "state": "budget_stopped", "note": "truncated ESO science product; never eligible"}
            elif ref.extra.get("inline"):
                from .multi.archives.solar_system import _ContextAdapter
                _ContextAdapter.fetch(adapter, ref, path, timeout_s=60)
            else:
                adapter.fetch(ref, path, timeout_s=60)
        if not path.is_file() or not 0 < path.stat().st_size <= cap:
            return {**base, "state": "budget_stopped", "note": "empty/oversized product; never eligible"}
        checksum = sha256_file(path)
        if ref.size_bytes and path.stat().st_size != ref.size_bytes:
            return {**base, "state": "integrity_failed", "note": "downloaded bytes differ from archive metadata size"}
        if ref.expected_sha256 and checksum != ref.expected_sha256:
            raise ValueError("archive expected checksum mismatch")
        position = Target(target["name"], None, None) if target.get("source") == "solar_designation" else Target.from_mapping(target)
        checks = [c.as_dict() for c in adapter.source_checks(position, ref, path,
                                                           {"kind": ref.kind, "format": ref.format})]
        good = bool(checks) and all(c["state"] == "passed" for c in checks)
        route = {"image": "image_review", "spectrum": "spectral_review", "lightcurve": "time_series_review",
                 "table": "catalogue_review"}.get(ref.kind, "context_review")
        eligible, state = False, "downloaded"
        if ref.archive == "mast" and ref.format == "spoc_lc" and target.get("source") == "exoarchive" and target.get("tic"):
            from astropy.io import fits
            with fits.open(path, memmap=True) as hdus:
                same = hdus[0].header.get("TICID") == int(target["tic"])
                timesys = str(hdus[1].header.get("TIMESYS", hdus[0].header.get("TIMESYS", ""))).upper()
                timed = timesys == "TDB"
            eligible = same and timed and good
            state = "downloaded" if same else "identity_failed"
            checks += [{"name": "Exact TIC header", "state": "passed" if same else "failed", "note": "TICID vs exact TOI row"},
                       {"name": "Declared TDB time system", "state": "passed" if timed else "inconclusive", "note": "FITS TIMESYS"}]
            route = "transit" if eligible else "time_series_review"
        return {**base, "state": state, "route": route, "eligible": eligible, "checks": checks,
                "path": "scratch:" + path.resolve().relative_to(scratch_dir().resolve()).as_posix(),
                "sha256": checksum, "bytes": path.stat().st_size, "retrieved_utc": now_utc(),
                "note": "integrity/access only; no scientific tier, source-assignment or discovery claim"}
    except Exception as exc:
        return {**base, "state": "unavailable", "error": f"{type(exc).__name__}: {exc}"}


def execute_job(root, plan, job):
    if job["kind"] == "bootstrap":
        return bootstrap(plan["config"])
    if job["kind"] == "discover":
        return discover(job)
    if job["kind"] == "acquire":
        occupied = sum(p.stat().st_size for p in managed_scratch(plan).rglob("*") if p.is_file())
        path = _data_path(plan, job["product"])
        existing = path.stat().st_size if path.exists() else 0
        cap = int(min(job["cap"], plan["config"]["budget"]["scratch_mb"] * 1024**2 - occupied + existing))
        if cap <= 0:
            return {"state": "budget_stopped", "product": job["product"], "eligible": False,
                    "note": "retained scratch quota exhausted"}
        return fetch_product(job["product"], path, cap)
    raise ValueError("unknown scout job")


def acquire(root, scout_path, *, executor=None):
    from .batch import LedgerLock
    root = Path(root).resolve()
    path = Path(scout_path)
    if not path.is_absolute():
        path = inside(root, path.as_posix())
    scout_result = json.loads(path.read_text())
    plan = _plan(root, state_path(root, scout_result) / "PLAN.json")
    saved_scout = json.loads((state_path(root, plan) / "SCOUT_RECEIPT.json").read_text())
    if (path.resolve() != (capsule(root, plan) / "SCOUT.json").resolve() or scout_result["plan_sha256"] != digest(plan) or
            saved_scout != {"sha256": sha256_file(path), "plan_sha256": digest(plan)}):
        raise ValueError("scouting receipt lineage changed")
    # Every source receipt is independently bound to a completed supervised job.
    lock = LedgerLock(state_path(root, plan) / "writer")
    lock.acquire()
    try:
        jobs = Jobs(root, plan, executor)
        for key, saved in scout_result["checkpoints"].items():
            output = capsule(root, plan) / "jobs" / f"{key}.json"
            if (saved != json.loads((state_path(root, plan) / "checkpoints" / f"{key}.json").read_text()) or
                    saved["sha256"] != sha256_file(output)):
                raise ValueError("scouting checkpoint changed")
        results, seen = [], set()
        associations = {}
        for product in scout_result["products"]:
            associations.setdefault(_product_key(product["ref"]), []).append(product["target"])
        for product in scout_result["products"]:
            key = _product_key(product["ref"])
            if key in seen:
                continue
            seen.add(key)
            budget = plan["config"]["budget"]
            result = jobs.run({"kind": "acquire", "product": product, "cap": int(budget["product_mb"] * 1024**2)})
            result.setdefault("product", product)
            result.setdefault("eligible", False)
            results.append({**result, "associations": associations[key]})
        receipt = {"schema": "cygnus.acquisition/1", "id": plan["id"], "plan_sha256": digest(plan),
                   "scout_sha256": sha256_file(path), "products": results, "checkpoints": jobs.receipts}
        atomic_write_json(capsule(root, plan) / "ACQUISITION.json", receipt)
        write_report(root, plan, scout_result, receipt)
        atomic_write_json(state_path(root, plan) / "ACQUISITION_RECEIPT.json", {
            "sha256": sha256_file(capsule(root, plan) / "ACQUISITION.json"), "plan_sha256": digest(plan),
            "queue_sha256": sha256_file(capsule(root, plan) / "TRANSIT_QUEUE.csv")})
        return receipt
    finally:
        lock.release()


def _csv(path, rows):
    stream = io.StringIO(newline="")
    keys = list(dict.fromkeys(k for row in rows for k in row)) or ["name", "rank", "tic"]
    writer = csv.DictWriter(stream, fieldnames=keys)
    writer.writeheader()
    writer.writerows([{k: json.dumps(v, sort_keys=True) if isinstance(v, (dict, list)) else v for k, v in r.items()} for r in rows])
    atomic_write_text(path, stream.getvalue())


def write_report(root, plan, result, acquisition=None):
    from .colab import build_manifest
    out = capsule(root, plan)
    rel = out.relative_to(root).as_posix()
    lines = ["# Public archive scout and acquisition", "", "<!-- cygnus:generated-draft -->", "",
             "Finite metadata selections and input integrity only; no astronomical signal or earned tier is claimed.", "",
             "| Source | Mode | Execution state | Limitation |", "| --- | --- | --- | --- |"]
    for name, row in result["sources"].items():
        lines.append(f"| {name} | {row['mode']} | {row['state']} | {row['reason']} |")
    lines += ["", f"Catalogued targets: {len(result['targets'])}; product references: {len(result['products'])}.",
              "Rank is a sample/order heuristic. Targets with equal positions are not merged across catalogues.",
              "Frames/epochs and source rows remain explicit; unverified epochs require proper-motion review.",
              "Requests, footprints, exclusions and rows are in SCOUT.json and per-job receipts."]
    eligible = []
    if acquisition:
        lines += ["", "## Acquisition", "", "| Product | State | Route | Bytes |", "| --- | --- | --- | --- |"]
        for row in acquisition["products"]:
            product = row.get("product", {}).get("ref", {})
            lines.append(f"| {product.get('product_id', 'uncompleted job')} | {row['state']} | {row.get('route', 'unavailable')} | {row.get('bytes', '')} |")
            if row.get("eligible"):
                target = row["product"]["target"]
                if target["name"] not in {t["name"] for t in eligible}:
                    eligible.append({k: v for k, v in target.items() if k not in ("source_row", "field", "scout_rank")})
        for rank, target in enumerate(eligible, 1):
            target["rank"] = rank
    _csv(out / "TARGET_QUEUE.csv", result["targets"])
    _csv(out / "TRANSIT_QUEUE.csv", eligible)
    _csv(out / "REVIEW_QUEUE.csv", [t for t in result["targets"] if t["route"] != "transit"])
    atomic_write_json(out / "LINEAGE.json", plan)
    atomic_write_text(out / "REPORT.md", "\n".join(lines) + "\n")
    atomic_write_text(out / "SEARCH_LOG.md", "# Scout search log\n\n" +
                      "SCOUT.json retains exact attempts, queries, field footprints, row caps, source IDs and exclusions.\n" +
                      "Bootstrap is a brightness-limited TOI sample, not an all-sky completeness claim. No signals tested.\n")
    targets = result["retrieval_targets"]
    atomic_write_json(out / "sky_record.json", {"schema": "cygnus.sky_record/1", "id": plan["id"],
        "title": "Public archive acquisition audit", "kind": "workflow audit", "status": "completed",
        "outcome": "pipeline_check", "evidence": None, "date": now_utc()[:10],
        "summary": "Scouting/acquisition audit only; read source attempts and integrity states; no scientific tier earned.",
        "report": rel + "/REPORT.md", "search_log": rel + "/SEARCH_LOG.md",
        "targets": [{"name": t["name"], "ra_deg": t["ra_deg"], "dec_deg": t["dec_deg"],
                     "frame": t.get("frame", "ICRS"), "epoch": t.get("position_epoch", "unverified"),
                     "position_source": t.get("position_source", "explicit field")} for t in targets],
        "products": [{"id": r["product"]["ref"]["product_id"], "archive": r["product"]["ref"]["archive"],
                      "sha256": r["sha256"]} for r in (acquisition or {}).get("products", []) if r.get("sha256")],
        "checks": [{"name": "Dated follow-up public archive acquisition", "state": "inconclusive",
                    "note": "operational inventory only; unavailable/manual sources and scientific review remain explicit"}]})
    entries = build_manifest(out, [p.name for p in out.iterdir() if p.name != "MANIFEST.sha256"])
    atomic_write_text(out / "MANIFEST.sha256", "".join(f"{v}  {k}\n" for k, v in entries.items()))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["worker"])
    parser.add_argument("root")
    parser.add_argument("plan")
    parser.add_argument("job")
    parser.add_argument("output")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    plan = _plan(root, args.plan)
    job = json.loads(Path(args.job).read_text())
    if job["plan_sha256"] != digest(plan):
        raise ValueError("worker job lineage changed")
    atomic_write_json(Path(args.output), execute_job(root, plan, job))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

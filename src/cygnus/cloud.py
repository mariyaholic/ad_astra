"""Evidence-gated, resumable CPU campaigns for a repository checkout.

python -m cygnus.cloud plan cloud/workflow.yaml
python -m cygnus.cloud run state/cloud_runs/<id>/PLAN.json
python -m cygnus.cloud status state/cloud_runs/<id>/PLAN.json

Science remains in cygnus.multi, campaign.vet and the native analysis tools.
Earned tiers never stand in for executed stages or astrophysical confirmation.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import os
import runpy
import shutil
import signal
import subprocess
import sys
import time
from copy import deepcopy
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path, PurePosixPath

from .campaign.tiers import decide, rank
from .config import WORKTREE, scratch_dir
from .fileio import archive_previous, atomic_write_json, atomic_write_text, sha256_file
from .ledger import now_utc
from .skyrecord import SCHEMA, validate

STAGES = ("screen", "T2", "T3")
CODE_ROOT = Path(__file__).resolve().parents[2]
FROZEN = {"toi-224-01", "toi-2666-01", "toi-3500-02", "toi-7610-01", "toi-6695-01"}
DEFAULT_NULL = {"n_null": 300, "n_inject": 100, "min_n": 100}
# Capsules live outside campaigns/ and reports/: each stage keeps its own sky record with the target id,
# and nesting them under reports/ would publish duplicate ids. reports/handback-<id>/ is generated on ingest.
HANDBACK_BASE = "docs/handbacks"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    allow_nan=False).encode()).hexdigest()


def digest_receipt(receipt):
    """SHA-256 of a checkpoint file as atomic_write_json writes it, so a shipped copy can be rechecked."""
    return hashlib.sha256((json.dumps(receipt, indent=2, allow_nan=False, ensure_ascii=False) + "\n")
                          .encode("utf-8")).hexdigest()


def inside(root, rel):
    """Repository-relative paths only; reject traversal and symlink escapes."""
    rel = str(rel)
    parts = PurePosixPath(rel)
    if not rel or parts.is_absolute() or ".." in parts.parts or "\\" in rel or ":" in rel:
        raise ValueError("unsafe relative cloud path")
    path = Path(root) / rel
    if not path.resolve().is_relative_to(Path(root).resolve()) or any(
            p.is_symlink() for p in (path, *path.parents) if p != Path(root).parent):
        raise ValueError("cloud path escapes its root or uses a symlink")
    return path


def normalize_config(config):
    config = deepcopy(config)
    allowed = {"schema", "queue", "limit", "max_tier", "budget", "discriminating_question", "seed",
               "null_params", "t3", "source_max_age_hours", "max_source_queries", "retries", "acquisition"}
    if set(config) - allowed or config.get("schema") != "cygnus.cloud/1":
        raise ValueError("cloud config schema/keys are invalid")
    if config.get("max_tier", "T3") not in ("T0", "T1", "T2", "T3"):
        raise ValueError("cloud max_tier must be T0 through T3; T4 is not enabled")
    config.setdefault("max_tier", "T3")
    config.setdefault("limit", 5)
    if type(config["limit"]) is not int or not 1 <= config["limit"] <= 100:
        raise ValueError("limit must be an integer from 1 to 100")
    config.setdefault("seed", 20261017)
    if type(config["seed"]) is not int:
        raise ValueError("seed must be an integer")
    config.setdefault("source_max_age_hours", 24)
    config.setdefault("max_source_queries", config["limit"] * 2)
    config.setdefault("retries", 1)
    if type(config["retries"]) is not int or config["retries"] not in (0, 1):
        raise ValueError("retries must be 0 or 1")
    if type(config["max_source_queries"]) is not int or config["max_source_queries"] < 1:
        raise ValueError("max_source_queries must be a positive integer")
    if not math.isfinite(config["source_max_age_hours"]) or config["source_max_age_hours"] <= 0:
        raise ValueError("source_max_age_hours must be finite and positive")
    budget = {"scratch_mb": 1024, "stage_seconds": 1800, "run_seconds": 3600, "min_free_mb": 1024,
              **config.get("budget", {})}
    if set(budget) != {"scratch_mb", "stage_seconds", "run_seconds", "min_free_mb"} or any(
            type(v) not in (int, float) or not math.isfinite(v) or v <= 0 for v in budget.values()):
        raise ValueError("budget fields must be finite positive numbers")
    config["budget"] = budget
    if config["max_tier"] == "T3" and not str(config.get("discriminating_question", "")).strip():
        raise ValueError("T3 needs a discriminating_question and budget")
    config["null_params"] = {**DEFAULT_NULL, **config.get("null_params", {})}
    if set(config["null_params"]) != set(DEFAULT_NULL) or any(
            type(v) is not int or v <= 0 for v in config["null_params"].values()):
        raise ValueError("null_params must contain positive integer trial counts")
    if config["null_params"]["min_n"] < 100:
        raise ValueError("cloud null gate requires min_n >= 100")
    t3 = {"tests": ["archive_metadata", "rv_fit", "prf_source_fit"], "archives": ["koa"],
          "inputs": {}, **config.get("t3", {})}
    if set(t3) != {"tests", "archives", "inputs"} or not isinstance(t3["inputs"], dict):
        raise ValueError("invalid T3 configuration")
    if not t3["tests"] or len(set(t3["tests"])) != len(t3["tests"]) or any(
            t not in ("archive_metadata", "rv_fit", "prf_source_fit") for t in t3["tests"]):
        raise ValueError("unsupported or duplicate T3 test")
    if not t3["archives"] or any(a not in ("koa", "eso") for a in t3["archives"]):
        raise ValueError("T3 metadata archives must be koa/eso")
    config["t3"] = t3
    inside(Path.cwd(), config["queue"])
    return config


def code_identity():
    """Bind source bytes and relevant runtime versions, including notebook helpers."""
    files = sorted((CODE_ROOT / "src/cygnus").rglob("*.py"))
    files += [CODE_ROOT / "notebooks/higher_tiers/workflow.py", CODE_ROOT / "pyproject.toml"]
    source = {p.relative_to(CODE_ROOT).as_posix(): hashlib.sha256(
        p.read_bytes().replace(b"\r\n", b"\n")).hexdigest() for p in files}
    versions = {}
    for name in ("numpy", "scipy", "astropy", "astroquery", "matplotlib", "requests", "PyYAML", "pyvo"):
        try:
            versions[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            versions[name] = None
    git = subprocess.run(["git", "rev-parse", "HEAD"], cwd=CODE_ROOT, capture_output=True, text=True)
    return {"source_sha256": digest(source), "files": source, "git_commit": git.stdout.strip() or None,
            "python": sys.version.split()[0], "platform": sys.platform, "packages": versions}


@lru_cache(maxsize=1)
def notebook_helpers():
    # Use the reviewed pure follow-up helpers without editing/rebuilding frozen notebook artifacts.
    # The trusted checkout file is included in code_identity, never supplied by remote content.
    return runpy.run_path(str(CODE_ROOT / "notebooks/higher_tiers/workflow.py"))


def plan_path(root, plan):
    return inside(root, f"state/cloud_runs/{plan['id']}/PLAN.json")


def report_dir(root, plan):
    return inside(root, f"{HANDBACK_BASE}/{plan['id']}")


def stage_dir(root, plan, cid, stage):
    if cid not in plan["targets"] or stage not in STAGES:
        raise ValueError("target/stage is outside the cloud plan")
    return inside(root, f"{HANDBACK_BASE}/{plan['id']}/targets/{cid}/{stage}")


def checkpoint_path(root, plan, cid, stage):
    stage_dir(root, plan, cid, stage)
    return inside(root, f"state/cloud_runs/{plan['id']}/checkpoints/{cid}.{stage}.json")


def make_plan(root, config, *, refresh=None):
    """Select a finite queue batch and refresh exact identities. No FITS or science run."""
    from .multi.scaffold import read_queue, slug_for, target_from_row
    from .targets import refresh_queue_target, EXO_TAP, TOI_COLUMNS
    from .batch import LedgerLock

    root = Path(root).resolve()
    config = normalize_config(config)
    if config.get("acquisition"):
        from .cloud_scout import verified_acquisition
        receipt = inside(root, config["acquisition"]["path"])
        if sha256_file(receipt) != config["acquisition"]["sha256"]:
            raise ValueError("acquisition manifest changed")
        verified_acquisition(root, receipt)
    queue = inside(root, config["queue"])
    rows = read_queue(queue)
    taken = {p.stem for p in (root / "campaigns").glob("*.yaml")}
    taken |= {p.parent.name for p in (root / "campaigns").glob("*/REJECTION.md")}
    rows.sort(key=lambda r: (float(r.get("rank") or math.inf), r.get("name", "")))
    selection, selected, seen = [], {}, set()
    queries = 0
    lock_path = root / "state/cloud_selection"
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock = LedgerLock(lock_path)
    lock.acquire()
    try:
        for prior in (root / "state/cloud_runs").glob("*/PLAN.json"):
            taken.update(json.loads(prior.read_text())["targets"])
        for row in rows:
            cid = slug_for(row.get("name", ""))
            item = {"id": cid, "name": row.get("name"), "rank": row.get("rank"),
                    "rationale": row.get("rationale", "queue ordering; not a measurement")}
            if cid in FROZEN:
                state, reason = "excluded", "frozen/retracted specialist target"
            elif cid in taken or cid in seen:
                state, reason = "excluded", "already claimed, analysed or duplicated"
            elif len(selected) >= config["limit"]:
                state, reason = "excluded", "outside this finite batch limit"
            elif queries >= config["max_source_queries"]:
                state, reason = "excluded", "source-query budget exhausted"
            else:
                queries += 1
                try:
                    item.update(endpoint=EXO_TAP, query=f"SELECT {', '.join(TOI_COLUMNS)} FROM toi WHERE tid = {int(row['tic'])}",
                                request_utc=now_utc())
                    current = (refresh or refresh_queue_target)(deepcopy(row))
                    if current["name"] != row["name"] or int(current["tic"]) != int(row["tic"]):
                        raise ValueError("exact source identity changed")
                    if not current.get("catalogue_query") or not current.get("catalogue_retrieved_utc"):
                        raise ValueError("exact source provenance is missing")
                    stamp = datetime.fromisoformat(current["catalogue_retrieved_utc"].replace("Z", "+00:00"))
                    if stamp.tzinfo is None:
                        raise ValueError("source retrieval time has no time zone")
                    target = target_from_row(current, "NASA Exoplanet Archive TOI table")
                    if any(target.get(k) is None or not math.isfinite(target[k]) for k in ("ra_deg", "dec_deg", "t0_bjd")):
                        raise ValueError("source coordinates/epoch are unusable")
                    selected[cid] = current
                    state, reason = "selected", "exact TOI/TIC row refreshed; queue rank is a dated heuristic"
                except (Exception, SystemExit) as exc:
                    state, reason = "lookup_failed", f"{type(exc).__name__}: {exc}"
            seen.add(cid)
            selection.append({**item, "state": state, "reason": reason})
        body = {"schema": "cygnus.cloud_plan/1", "created_utc": now_utc(), "config": config,
                "queue_sha256": sha256_file(queue), "code": code_identity(),
                "targets": selected, "selection": selection}
        plan = {"id": "cloud-" + digest(body)[:16], **body}
        path = plan_path(root, plan)
        if path.exists():
            raise ValueError("plan already exists; resume its exact PLAN.json")
        atomic_write_json(path, plan)
        write_report(root, plan)
        return plan
    finally:
        lock.release()


def load_plan(root, path):
    plan = json.loads(Path(path).read_text(encoding="utf-8"))
    body = {k: v for k, v in plan.items() if k != "id"}
    if plan.get("id") != "cloud-" + digest(body)[:16] or plan.get("schema") != "cygnus.cloud_plan/1":
        raise ValueError("plan lineage changed")
    if Path(path).resolve() != plan_path(root, plan).resolve():
        raise ValueError("plan path differs from its lineage")
    if sha256_file(inside(root, plan["config"]["queue"])) != plan["queue_sha256"]:
        raise ValueError("source queue changed; create a new plan")
    if code_identity() != plan["code"]:
        raise ValueError("source/runtime version changed; create a new plan")
    return plan


ARTIFACT_CHECKS = {"Box fit finds a dip", "Detrending alternatives", "Red-noise significance",
                   "Background / centroid / pointing", "Common mode (same camera/CCD)"}


def retain_vetting_checks(record, report):
    """Retain every native event check without inventing canonical tier passes."""
    checks = {c["name"]: c for c in record["checks"]}
    for event in report.get("events", []):
        for name, (state, note) in event.get("checks", {}).items():
            key = f"Dated follow-up T2 {event['label']}: {name}"
            checks[key] = {"name": key, "state": state, "note": note,
                           "source": "native campaign vet; vetting/vetting.json"}
    return {**record, "checks": list(checks.values())}


def gate(record, config):
    decision = decide(record, spec={"budget": config["budget"],
                                   "discriminating_question": config.get("discriminating_question")})
    escalation = any(c["name"].startswith("Known-signal recovery") and c["state"] == "failed"
                     for c in record.get("checks", []))
    artifacts = [c["name"] for c in record.get("checks", [])
                 if c["state"] == "failed" and c["name"].startswith("Dated follow-up T2 ") and
                 c["name"].partition(": ")[2] in ARTIFACT_CHECKS]
    return {**decision.as_dict(), "escalation": escalation or bool(artifacts), "artifact_blockers": artifacts}


def _stage_files(out):
    files = {}
    for p in sorted(out.rglob("*")):
        if p.is_symlink():
            raise ValueError("checkpoint artifact symlink is forbidden")
        if p.is_file():
            if p.name.lower().endswith((".fits", ".fits.gz", ".sqlite", ".sqlite-wal", ".sqlite-shm")):
                raise ValueError("bulk/ledger file in scientific artifact directory")
            files[p.relative_to(out).as_posix()] = sha256_file(p)
    return files


def _stage_decision(root, plan, cid, stage):
    import yaml
    from .multi.scaffold import target_from_row
    out = stage_dir(root, plan, cid, stage)
    record = json.loads((out / "sky_record.json").read_text())
    problems = validate(record, Path(root))
    proof = json.loads((out / "STAGE.json").read_text())
    if problems or record.get("id") != cid or record.get("status") != "completed":
        raise ValueError("checkpoint needs a valid, matching completed sky record: " + "; ".join(problems))
    expected = target_from_row(plan["targets"][cid], "exact source")
    spec = yaml.safe_load((out / "SPEC.yaml").read_text())
    targets, positions = spec.get("targets", []), record.get("targets", [])
    if (len(targets) != 1 or len(positions) != 1 or positions[0].get("name") != expected["name"] or
            any(targets[0].get(k) != expected[k] for k in ("name", "tic", "t0_bjd", "period_days", "ra_deg", "dec_deg"))):
        raise ValueError("checkpoint target/source identity or ephemeris differs from the exact row")
    if proof.get("stage") != stage or not proof.get("complete"):
        raise ValueError("checkpoint has no completed stage execution proof")
    decision = gate(record, plan["config"])
    if stage == "screen":
        summary = json.loads((out / "runner/RUN_SUMMARY.json").read_text())
        if summary.get("complete") is not True or "native_screen" not in proof.get("executed", []):
            raise ValueError("screen checkpoint is incomplete")
    elif stage == "T2":
        if not all((out / rel).is_file() for rel in ("SOURCE_RECORD.json", "period_aliases.json", "vetting/vetting.json")):
            raise ValueError("T2 checkpoint lacks defining-event source/vet artifacts")
        helpers = notebook_helpers()
        source = json.loads((out / "SOURCE_RECORD.json").read_text())
        aliases = json.loads((out / "period_aliases.json").read_text())
        vet = json.loads((out / "vetting/vetting.json").read_text())
        if not helpers["fitted_defining_events"](source, vet, aliases):
            raise ValueError("T2 checkpoint lacks a measurable defining vet event")
        if decision["tier"] != "closed":
            products = {c["product"] for c in aliases["candidates"]}
            rows = json.loads((out / "event_null.json").read_text())["events"]
            if not any(r.get("product") in products and r.get("observed", {}).get("state") == "measured" and
                       type(r.get("observed", {}).get("depth_ppm")) in (int, float) and
                       math.isfinite(r["observed"]["depth_ppm"]) for r in rows):
                raise ValueError("T2 checkpoint lacks a measured/covered defining event null")
    else:
        tests = json.loads((out / "diagnostics.json").read_text())["tests"]
        if set(tests) != set(plan["config"]["t3"]["tests"]) or not all(r.get("ran") for r in tests.values()):
            raise ValueError("T3 checkpoint has missing/unexecuted diagnostics")
    return {"earned": decision["tier"], "run_at": stage, "decision": decision,
            "evidence": record.get("evidence"), "status": "completed"}


def save_stage(root, plan, cid, stage):
    out = stage_dir(root, plan, cid, stage)
    decision = _stage_decision(root, plan, cid, stage)
    upstream = None if stage == "screen" else STAGES[STAGES.index(stage) - 1]
    previous = verify_stage(root, plan, cid, upstream) if upstream else None
    if upstream and previous is None:
        raise ValueError("checkpoint lacks verified upstream stage")
    if previous and (previous["decision"]["escalation"] or previous["earned"] == "closed" or
                     rank(previous["earned"]) < rank(stage)):
        raise ValueError("checkpoint upstream tier gate is not satisfied")
    payload = {"lineage_sha256": digest(plan), "artifacts": _stage_files(out), "decision": decision,
               "decision_sha256": digest(decision),
               "upstream_sha256": sha256_file(checkpoint_path(root, plan, cid, upstream)) if upstream else None}
    atomic_write_json(checkpoint_path(root, plan, cid, stage), payload)
    return decision


def verify_stage(root, plan, cid, stage):
    path = checkpoint_path(root, plan, cid, stage)
    if not path.exists():
        return None
    try:
        receipt = json.loads(path.read_text())
        if receipt["lineage_sha256"] != digest(plan) or receipt["artifacts"] != _stage_files(stage_dir(root, plan, cid, stage)):
            raise ValueError("checkpoint artifact set or hash changed")
        decision = _stage_decision(root, plan, cid, stage)
        if receipt["decision"] != decision or receipt["decision_sha256"] != digest(decision):
            raise ValueError("checkpoint decision changed")
        if stage != "screen":
            previous = STAGES[STAGES.index(stage) - 1]
            prior = verify_stage(root, plan, cid, previous)
            if prior is None or receipt["upstream_sha256"] != sha256_file(
                    checkpoint_path(root, plan, cid, previous)):
                raise ValueError("checkpoint upstream changed")
            if prior["decision"]["escalation"] or prior["earned"] == "closed" or rank(prior["earned"]) < rank(stage):
                raise ValueError("checkpoint upstream tier gate is not satisfied")
        return decision
    except (OSError, KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid {cid}/{stage} checkpoint: {exc}") from exc


def read_attempts(path):
    """Only an incomplete final append is recoverable; corrupt complete/interior rows fail closed."""
    if not path.exists():
        return [], False
    raw = path.read_text(encoding="utf-8")
    lines, entries = raw.splitlines(), []
    for index, line in enumerate(lines):
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            if index == len(lines) - 1 and not raw.endswith("\n"):
                return entries, True
            raise ValueError("cloud attempt journal has a corrupt complete/interior row")
    return entries, False


def board(root, plan):
    rows = {}
    for cid in plan["targets"]:
        completed = {}
        for stage in STAGES:
            found = verify_stage(root, plan, cid, stage)
            if found:
                completed[stage] = found
        latest = next(reversed(completed.values()), None)
        nxt, reason = "screen", "not screened"
        if latest:
            earned, current = latest["earned"], latest["run_at"]
            if earned == "closed":
                nxt, reason = None, "closed by recorded evidence"
            elif latest["decision"]["escalation"]:
                nxt = None
                reason = ("failed native artifact checks; review required: " +
                          "; ".join(latest["decision"]["artifact_blockers"]) if
                          latest["decision"]["artifact_blockers"] else "covered positive control failed; review required")
            elif current == "T3":
                nxt, reason = None, "requested T3 diagnostics executed; evidence unchanged"
            elif current == "T2":
                nxt = "T3" if rank(earned) >= 3 and rank(plan["config"]["max_tier"]) >= 3 else None
                reason = ("T2 gates passed; T3 budget/question supplied" if nxt else
                          "; ".join(latest["decision"]["blockers"]) or "configured tier ceiling")
            else:
                nxt = "T2" if rank(earned) >= 2 and rank(plan["config"]["max_tier"]) >= 2 else None
                reason = "; ".join(latest["decision"]["blockers"]) or "configured tier ceiling"
        rows[cid] = {"earned": latest["earned"] if latest else None,
                     "run_at": latest["run_at"] if latest else None,
                     "evidence": latest["evidence"] if latest else None,
                     "completed_stages": list(completed), "next_stage": nxt, "reason": reason}
    journal = plan_path(root, plan).parent / "ATTEMPTS.jsonl"
    attempts, interrupted = read_attempts(journal)
    for attempt in attempts:
        if attempt.get("target") in rows:
            rows[attempt["target"]]["last_attempt"] = attempt
    if interrupted:
        for row in rows.values():
            row["journal_warning"] = "interrupted final attempt-log append; verified checkpoints retained"
    return rows


def write_report(root, plan):
    from .colab import build_manifest
    out = report_dir(root, plan)
    out.mkdir(parents=True, exist_ok=True)
    rows = board(root, plan)
    atomic_write_json(out / "tier_board.json", {"schema": "cygnus.cloud_board/1", "run": plan["id"], "targets": rows})
    lines = ["# Cloud campaign readout", "", "<!-- cygnus:generated-draft -->", "",
             "Earned tiers are derived from verified sky records; run_at records executed stages.",
             "No automatic scientific evidence promotion. Missing tests are not passes.", "",
             "| Target | Queue rank | Earned | Executed | Next | Reason |",
             "| --- | --- | --- | --- | --- | --- |"]
    for cid, row in rows.items():
        last = row.get("last_attempt", {})
        if last.get("state") not in (None, "ok"):
            lines.append(f"<!-- Last attempt for {cid}: {last['state']}; {last.get('reason') or 'see attempt log'} -->")
        lines.append(f"| {plan['targets'][cid]['name']} | {plan['targets'][cid].get('rank', '')} | {row['earned']} | "
                     f"{row['run_at']} | {row['next_stage']} | "
                     f"{(last.get('reason') or row['reason']).replace('|', '/')} |")
    for cid, row in rows.items():
        source = plan["targets"][cid]
        lines += ["", f"## {source['name']}", "",
                  f"Catalogue position: {float(source['ra_deg']):.8f}, {float(source['dec_deg']):.8f} deg; ICRS, epoch J2015.5.",
                  f"Ranking rationale: {str(source.get('rationale') or 'dated queue heuristic').replace(chr(10), ' ')}."]
        if row["run_at"]:
            leaf = stage_dir(root, plan, cid, row["run_at"])
            rec = json.loads((leaf / "sky_record.json").read_text())
            lines += [f"Evidence: {rec.get('evidence') or 'no candidate evidence level'}. "
                      f"[Stage report](targets/{cid}/{row['run_at']}/REPORT.md).",
                      "Product IDs: " + ", ".join(p["id"] for p in rec.get("products", [])) + "."]
            null_path = leaf / "event_null.json"
            if null_path.exists():
                for item in json.loads(null_path.read_text()).get("events", []):
                    observed, null = item.get("observed", {}), item.get("null", {})
                    if observed.get("state") == "measured":
                        lines.append(f"Measured event BJD: {item['event_bjd']}; depth {observed['depth_ppm']:.3f} ppm. "
                                     f"Empirical null exceedances: {null.get('n_exceed', 'unavailable')}/"
                                     f"{null.get('n_covered', 'unavailable')} covered trials; finite resolution, not Gaussian significance.")
            severity = {"failed": 3, "inconclusive": 2, "not_tested": 1, "passed": 0}
            concern = max(rec.get("checks", []), key=lambda c: severity[c["state"]], default=None)
            if concern:
                lines.append(f"Strongest recorded concern: {concern['name']} — {concern['state']}; {concern.get('note', '')}.")
        lines.append("Next test/action: " + (row.get("last_attempt", {}).get("reason") or row["reason"]) + ".")
    lines += ["", "Read each target's stage REPORT.md, sky_record.json, source receipts and diagnostics.",
              "Queue order is a dated heuristic. Empirical k/N nulls are selection-touched, not search-wide FAP.",
              "A same-pixel reduction is not independent sky support. T4 and publication are not executed."]
    atomic_write_text(out / "REPORT.md", "\n".join(lines) + "\n")
    atomic_write_json(out / "SELECTION.json", {"queue_sha256": plan["queue_sha256"], "rows": plan["selection"]})
    atomic_write_json(out / "ENVIRONMENT.json", plan["code"])
    atomic_write_json(out / "LINEAGE.json", plan)
    receipts = {}
    for cid in plan["targets"]:
        for stage in STAGES:
            path = checkpoint_path(root, plan, cid, stage)
            if path.exists():
                receipts[f"{cid}.{stage}"] = json.loads(path.read_text())
    atomic_write_json(out / "CHECKPOINTS.json", receipts)
    atomic_write_text(out / "SEARCH_LOG.md", "# Cloud search log\n\n" +
                      f"Plan: {plan['id']}; queue: {plan['config']['queue']}; SHA-256: {plan['queue_sha256']}.\n" +
                      f"Rows accounted: {len(plan['selection'])}; selected: {len(rows)}; " +
                      f"excluded/lookup failed: {len(plan['selection']) - len(rows)}.\n" +
                      "SELECTION.json retains every exclusion and ranking rationale. Exact refreshed rows/config are in LINEAGE.json.\n" +
                      "Per-stage logs and records identify actual products, queries, epochs, thresholds and failures.\n")
    rel = out.relative_to(Path(root)).as_posix()
    active = bool(rows) and any(r["next_stage"] for r in rows.values())
    source_errors = any(r["state"] == "lookup_failed" for r in plan["selection"])
    targets = [{"name": row["name"], "ra_deg": float(row["ra_deg"]), "dec_deg": float(row["dec_deg"]),
                "frame": "ICRS", "epoch": "J2015.5", "position_source": "NASA Exoplanet Archive exact TOI row"}
               for row in plan["targets"].values()]
    atomic_write_json(out / "sky_record.json", {"schema": SCHEMA, "id": plan["id"],
        "title": "Cloud campaign execution audit", "kind": "workflow audit",
        "status": "draft" if not targets else "running" if active else "completed",
        "outcome": "pipeline_check" if targets else "not_run", "evidence": None, "date": now_utc()[:10],
        "summary": "Operational audit only. Read per-target scientific records; no discovery or evidence promotion is claimed.",
        "report": rel + "/REPORT.md", "search_log": rel + "/SEARCH_LOG.md", "targets": targets, "products": [],
        "checks": [{"name": "Dated follow-up cloud execution", "state": "inconclusive" if active or source_errors else "passed",
                    "note": "Execution state only; scientific checks are in per-target records.", "source": "verified stage checkpoints"}]})
    entries = build_manifest(out, [p.name for p in out.iterdir()
                                   if p.name not in ("MANIFEST.sha256", "HANDBACK.json", "IMPORTED.sha256")])
    atomic_write_text(out / "MANIFEST.sha256", "# Cloud capsule: every retained file except this manifest\n" +
                      "".join(f"{value}  {name}\n" for name, value in entries.items()))
    return out / "REPORT.md"


def _stop_child(process):
    if process.poll() is not None:
        return
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"], capture_output=True,
                       creationflags=subprocess.CREATE_NO_WINDOW, timeout=30)
    else:
        os.killpg(process.pid, signal.SIGTERM)
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        if os.name != "nt":
            os.killpg(process.pid, signal.SIGKILL)
        else:
            process.kill()
        process.wait(timeout=5)


def supervise(argv, cwd, log, scratch, *, timeout_s, max_bytes, min_free_bytes, env=None):
    """Bound an owned worker. Scratch is sampled, so a single response can overshoot the cap."""
    scratch = Path(scratch)
    scratch.mkdir(parents=True, exist_ok=True)
    Path(log).parent.mkdir(parents=True, exist_ok=True)
    started, peak, reason = time.monotonic(), 0, None
    def scratch_size():
        total = 0
        for path in scratch.rglob("*"):
            try:
                if path.is_file() and not path.is_symlink():
                    total += path.stat().st_size
            except FileNotFoundError:  # a downloader atomically renamed a partial file
                continue
        return total
    options = ({"creationflags": subprocess.CREATE_NO_WINDOW | subprocess.CREATE_NEW_PROCESS_GROUP}
               if os.name == "nt" else {"start_new_session": True})
    with Path(log).open("w", encoding="utf-8") as stream:
        process = subprocess.Popen(argv, cwd=cwd, env=env, stdout=stream, stderr=subprocess.STDOUT, **options)
        try:
            while process.poll() is None:
                size = scratch_size()
                peak = max(peak, size)
                if size > max_bytes:
                    reason = "managed scratch byte budget exceeded"
                elif shutil.disk_usage(scratch).free < min_free_bytes:
                    reason = "minimum free scratch space breached"
                elif time.monotonic() - started >= timeout_s:
                    reason = "stage/run wall-clock budget exceeded"
                if reason:
                    _stop_child(process)
                    break
                time.sleep(0.25)
        finally:
            _stop_child(process)
    final_size = scratch_size()
    peak = max(peak, final_size)
    if reason is None and final_size > max_bytes:
        reason = "managed scratch byte budget exceeded at worker completion"
    if reason is None and shutil.disk_usage(scratch).free < min_free_bytes:
        reason = "minimum free scratch space breached at worker completion"
    return {"state": "budget_stopped" if reason else "ok" if process.returncode == 0 else "failed",
            "returncode": process.returncode, "seconds": round(time.monotonic() - started, 3),
            "scratch_bytes_peak": peak, "reason": reason}


def run_diagnostics(root, record, inputs, requested, **kwargs):
    from .cloud_diagnostics import run_diagnostics as run
    return run(root, record, inputs, requested, **kwargs)


def _paths(spec, out, root):
    """Only change execution/output paths, retaining exact measured/source parameters."""
    spec = deepcopy(spec)
    rel = out.relative_to(root).as_posix()
    spec["outputs"] = rel
    spec.setdefault("record", {}).update(path=rel + "/sky_record.json", report=rel + "/REPORT.md",
                                         search_log=rel + "/SEARCH_LOG.md")
    spec["_path"] = out / "SPEC.yaml"
    return spec


def _write_spec(spec):
    import yaml
    atomic_write_text(spec["_path"], yaml.safe_dump({k: v for k, v in spec.items() if k != "_path"}, sort_keys=False))


def _record_paths(record, spec):
    record = deepcopy(record)
    record.update(spec=spec["outputs"] + "/SPEC.yaml", report=spec["record"]["report"],
                  search_log=spec["record"]["search_log"], generated_by="cygnus.cloud", generated_utc=now_utc())
    return record


def _draft_files(out, spec, root, source=None):
    from .multi.runner import Context, write_record
    from .ledger import Ledger

    for name in ("REPORT.md", "SEARCH_LOG.md"):
        atomic_write_text(out / name, "<!-- cygnus:generated-draft -->\n\n# Incomplete cloud attempt\n\nNo completed stage is claimed.\n")
    if source:
        rec = _record_paths(source, spec)
        rec.update(status="draft", outcome="not_run", evidence=None,
                   summary="This stage is incomplete. The completed upstream evidence is retained in SOURCE_RECORD.json.")
        atomic_write_json(out / "sky_record.json", rec)
    else:
        # A valid draft remains even if a native call raises before its final record write.
        led = Ledger(":memory:")
        try:
            write_record(Context(spec, led, root), False)
        finally:
            led.close()


def _followup_report(out, record, stage, notes):
    lines = ["<!-- cygnus:generated-draft -->", "", f"# {stage} follow-up: {record['id']}", "",
             f"Evidence remains **{record.get('evidence')}**. No automatic promotion.", "", *notes, "",
             "| Check | State | Note |", "| --- | --- | --- |"]
    lines += [f"| {c['name']} | {c['state']} | {c.get('note', '').replace('|', '/')} |" for c in record["checks"]]
    atomic_write_text(out / "REPORT.md", "\n".join(lines) + "\n")
    atomic_write_text(out / "SEARCH_LOG.md", "# Follow-up search log\n\n" + "\n".join(notes) +
                      "\nSource inputs and exact methods are retained in SOURCE_RECORD.json, SOURCE_SPEC.yaml and runner receipts.\n")


def run_stage(root, plan, cid, stage):
    """One in-process worker body. CLI run supervises it in a bounded child process."""
    import yaml
    from .ledger import Ledger
    from .multi import scaffold as multi_scaffold
    from .multi import runner as multi_runner
    from .campaign.runner import Context
    from .campaign import steps, vet as vet_module
    from .campaign.tiers import require_tier, unmapped_checks

    root = Path(root).resolve()
    if cid in FROZEN:
        raise PermissionError("routine cloud execution cannot reopen a frozen/retracted specialist target")
    state = board(root, plan)[cid]
    if state["next_stage"] != stage:
        raise ValueError(f"stage gate: {cid} next stage is {state['next_stage']}, not {stage}")
    row = plan["targets"][cid]
    stamp = datetime.fromisoformat(row["catalogue_retrieved_utc"].replace("Z", "+00:00"))
    if stage == "screen" and (datetime.now(timezone.utc) - stamp).total_seconds() > plan["config"]["source_max_age_hours"] * 3600:
        raise ValueError("exact source row is too old; generate a fresh plan")
    out = stage_dir(root, plan, cid, stage)
    if out.exists():
        # Preserve failed attempts in ignored state; never delete authoritative source/checkpoints.
        history = inside(root, f"state/cloud_runs/{plan['id']}/history/{cid}")
        history.mkdir(parents=True, exist_ok=True)
        dest = history / stage
        archive_previous(dest, "previous_attempt")
        os.replace(out, dest)
    out.mkdir(parents=True, exist_ok=True)
    ledger_path = plan_path(root, plan).parent / "ledger.sqlite"
    led = Ledger(ledger_path)
    try:
        if stage == "screen":
            target = multi_scaffold.target_from_row(row, "NASA Exoplanet Archive TOI table")
            source = f"exact TOI/TIC refresh {row['catalogue_retrieved_utc']}; {row['catalogue_query']}"
            spec = _paths(yaml.safe_load(multi_scaffold.spec_for(target, parent=None, origin=source,
                                                               seed=plan["config"]["seed"])), out, root)
            if plan["config"].get("acquisition"):
                from .cloud_scout import pinned_inputs
                spec["input"] = {"products": pinned_inputs(root, plan, cid)}
                for item in spec["steps"]:
                    if "fetch_products" in item:
                        item["fetch_products"].pop("from_targets", None)
            for item in spec["steps"]:
                if "fetch_products" in item:
                    item["fetch_products"]["max_product_bytes"] = int(plan["config"]["budget"]["scratch_mb"] * 1024**2)
            _write_spec(spec)
            atomic_write_json(out / "SOURCE_ROW.json", row)
            _draft_files(out, spec, root)
            multi_runner.run(spec["_path"], ledger=led, root=root)
            multi_scaffold.draft_report(spec, root)
            executed, complete = ["native_screen"], True
        else:
            previous = STAGES[STAGES.index(stage) - 1]
            src = stage_dir(root, plan, cid, previous)
            base = json.loads((src / "sky_record.json").read_text())
            spec = _paths(yaml.safe_load((src / "SPEC.yaml").read_text()), out, root)
            require_tier(base, stage, spec={"budget": plan["config"]["budget"],
                                          "discriminating_question": plan["config"].get("discriminating_question")})
            # Keep receipts/context available for native vet. Original stage stays byte-identical.
            shutil.copytree(src, out, dirs_exist_ok=True)
            atomic_write_text(out / "SOURCE_SPEC.yaml", (src / "SPEC.yaml").read_text())
            atomic_write_json(out / "SOURCE_RECORD.json", base)
            _write_spec(spec)
            _draft_files(out, spec, root, base)
            if stage == "T2":
                products = json.loads((src / "runner/fetch_products.json").read_text())["result"]["products"]
                aliases = json.loads((src / "period_aliases.json").read_text())
                helpers = notebook_helpers()
                spec.update(runner="cygnus.campaign", input={"products": helpers["pinned_source_products"](
                    base, products, spec["targets"][0])}, steps=[{"fetch_products": {}}, {"event_null": plan["config"]["null_params"]}])
                _write_spec(spec)
                ctx = Context(spec, led, root)
                ctx.step = "fetch_products"
                with led.recorded_run(f"cygnus.campaign:{cid}:cloud-T2:fetch_products", seed=ctx.seed) as receipt:
                    ctx.run_id = receipt.id
                    got = steps.step_fetch_products(ctx, {})
                    ctx._results["fetch_products"] = got
                    atomic_write_json(out / "runner/fetch_products.json", {"result": got, "run_id": receipt.id})
                with led.recorded_run(f"cygnus.campaign:{cid}:cloud-T2:vet", seed=ctx.seed):
                    report = vet_module.vet(spec, root)
                    if not helpers["fitted_defining_events"](base, report, aliases):
                        raise ValueError("T2 native vet has no measurable defining event")
                base = helpers["merge_vetting"](base, report)
                base = retain_vetting_checks(base, report)
                executed = ["fetch_products", "vet"]
                if decide(base, spec={}).tier == "closed":
                    null = {"events": [], "skipped_closed": True}
                    for name in ("Event-epoch null exceedance (k/N)", "Event-depth injection-recovery"):
                        ctx.check(name, "not_tested", "fresh vet closed the route; event-identity review required")
                    atomic_write_json(out / "event_null.json", null)
                else:
                    ctx.step = "event_null"
                    ctx._results["period_aliases"] = aliases
                    with led.recorded_run(f"cygnus.campaign:{cid}:cloud-T2:event_null", seed=ctx.seed) as receipt:
                        ctx.run_id = receipt.id
                        null = steps.step_event_null(ctx, plan["config"]["null_params"])
                        if not any(e.get("product") in products and e.get("observed", {}).get("state") == "measured"
                                   for e in null.get("events", [])):
                            raise ValueError("T2 native null has no covered/measured defining event")
                        executed.append("event_null")
                atomic_write_json(out / "runner/event_null.json", {"result": null, "checks": ctx.checks})
                checks = {c["name"]: c for c in base["checks"]}
                for name, check in ctx.checks.items():
                    checks[name] = {"name": name, "state": check["state"], "note": check["note"], "source": "native T2 tool"}
                base["checks"] = list(checks.values())
                # Native vet can retrieve target pixels and neighbour light curves outside the
                # initial fetch step. Preserve their actual hashes without exporting FITS.
                known = {p["id"] for p in base.get("products", [])}
                ancillary = []
                for path in sorted(scratch_dir(f"campaign_{cid}").rglob("*.fits")):
                    if path.name not in known:
                        ancillary.append({"id": path.name, "archive": "MAST", "sha256": sha256_file(path),
                                          "bytes": path.stat().st_size,
                                          "format": "tess_tpf" if path.name.endswith("_tp.fits") else
                                                    "spoc_lc" if path.name.endswith("_lc.fits") else "fits"})
                base["products"] = base.get("products", []) + ancillary
                atomic_write_json(out / "FOLLOWUP_PRODUCTS.json", {"ancillary": ancillary})
                complete = True
                notes = ["Exact source products/events reused without rescreening.",
                         f"Native vet groups: {len(report['events'])}; null rows: {len(null['events'])}.",
                         f"Random seed: {ctx.seed}; null parameters: {json.dumps(plan['config']['null_params'])}.",
                         "Local empirical nulls are selection-touched diagnostics, not original-search FAP."]
            else:
                target = dict(spec["targets"][0])
                aliases = json.loads((src / "period_aliases.json").read_text())
                report = json.loads((src / "vetting/vetting.json").read_text())
                target["defining_events"] = {e["label"]: e["fit"]["mid_bjd"] for e in notebook_helpers()[
                    "fitted_defining_events"](base, report, aliases)}
                t3 = plan["config"]["t3"]
                spec.update(schema="cygnus.cloud_stage/1", runner="cygnus.cloud", stage="T3", steps=[],
                            budget=plan["config"]["budget"],
                            discriminating_question=plan["config"]["discriminating_question"],
                            t3=t3, targets=[target])
                _write_spec(spec)
                with led.recorded_run(f"cygnus.campaign:{cid}:cloud-T3:diagnostics", seed=spec["random_seed"]):
                    result = run_diagnostics(root, base, t3["inputs"].get(cid, {}), t3["tests"],
                                             target=target, archives=t3["archives"])
                atomic_write_json(out / "diagnostics.json", result)
                complete = result["complete"]
                executed = [name for name, row in result["tests"].items() if row["ran"]]
                base["checks"] += [{"name": f"Dated follow-up T3 {name}", "state": row["state"],
                                    "note": row["note"], "source": "diagnostics.json"} for name, row in result["tests"].items()]
                atomic_write_json(out / "INPUTS.json", t3["inputs"].get(cid, {}))
                notes = ["T3 eligible does not mean T3 completed.",
                         "Each requested diagnostic records ran and state separately; missing inputs remain not_tested.",
                         "No spectral extraction, source assignment, orbit confirmation or evidence promotion."]
            rec = _record_paths(base, spec)
            if unmapped_checks([rec]):
                raise ValueError("follow-up emitted an unmapped scientific check")
            rec["status"] = "completed" if complete else "running"
            atomic_write_json(out / "sky_record.json", rec)
            _followup_report(out, rec, stage, notes)
        atomic_write_json(out / "STAGE.json", {"stage": stage, "complete": complete, "executed": executed,
                                                "finished_utc": now_utc()})
        if complete:
            # The supervisor alone commits a checkpoint after final resource checks. A worker
            # that exits between samples cannot certify its own over-budget completion.
            return _stage_decision(root, plan, cid, stage)
        return {"status": "blocked", "reason": "requested diagnostics lack usable inputs or archive access"}
    finally:
        led.close()


def run_plan(root, plan):
    from .batch import LedgerLock, close_orphan_runs, TRANSIENT

    root = Path(root).resolve()
    state = plan_path(root, plan).parent
    managed = scratch_dir(f"cloud/{plan['id']}")
    budget = plan["config"]["budget"]
    lock = LedgerLock(state / "ledger.sqlite")
    lock.acquire()
    started, failed = time.monotonic(), False
    journal = state / "ATTEMPTS.jsonl"
    try:
        attempts, interrupted = read_attempts(journal)
        if interrupted:
            archive_previous(journal, "interrupted_append")
            atomic_write_text(journal, "".join(json.dumps(row) + "\n" for row in attempts))
        for cid in plan["targets"]:
            for stage in STAGES:
                current = board(root, plan)[cid]
                if current["next_stage"] != stage:
                    continue
                remaining = budget["run_seconds"] - (time.monotonic() - started)
                if remaining <= 0:
                    failed = True
                    break
                print(f"{cid}: {stage}; earned={current['earned']}", flush=True)
                if stage == "screen" and plan["config"].get("acquisition"):
                    from .cloud_scout import seed_products
                    seed_products(root, plan, cid, managed)
                success = False
                for attempt in range(plan["config"]["retries"] + 1):
                    close_orphan_runs(state / "ledger.sqlite", cid, "exclusive cloud worker resume")
                    log = state / "logs" / f"{cid}.{stage}.{time.time_ns()}.log"
                    env = {**os.environ, "CYGNUS_SCRATCH": str(managed), "MPLBACKEND": "Agg",
                           "PYTHONUNBUFFERED": "1", "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
                           "MKL_NUM_THREADS": "1"}
                    remaining = budget["run_seconds"] - (time.monotonic() - started)
                    if remaining <= 0:
                        break
                    result = supervise([sys.executable, "-m", "cygnus.cloud", "--root", str(root), "_worker",
                                        str(plan_path(root, plan)), cid, stage], root, log, managed,
                                       timeout_s=min(budget["stage_seconds"], remaining),
                                       max_bytes=int(budget["scratch_mb"] * 1024**2),
                                       min_free_bytes=int(budget["min_free_mb"] * 1024**2), env=env)
                    if result["returncode"] == 2 and result["state"] == "failed":
                        result.update(state="blocked", reason="requested diagnostics lack usable inputs or archive access")
                    tail = " / ".join(log.read_text(encoding="utf-8", errors="replace").splitlines()[-4:])
                    result.update(target=cid, stage=stage, attempt=attempt + 1, utc=now_utc(),
                                  log=log.relative_to(root).as_posix(), error=tail if result["returncode"] else None)
                    with journal.open("a", encoding="utf-8") as stream:
                        stream.write(json.dumps(result, allow_nan=False) + "\n")
                    write_report(root, plan)
                    if result["state"] == "ok":
                        save_stage(root, plan, cid, stage)
                        success = True
                        break
                    if result["state"] in ("budget_stopped", "blocked") or not any(s.lower() in tail.lower() for s in TRANSIENT):
                        break
                if not success:
                    close_orphan_runs(state / "ledger.sqlite", cid, "cloud attempt incomplete/failed")
                    failed = True
                    break
        write_report(root, plan)
    finally:
        lock.release()
    if not plan["targets"] and any(r["state"] == "lookup_failed" for r in plan["selection"]):
        failed = True
    return 1 if failed else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(WORKTREE), help="repository root (default: current Cygnus checkout)")
    sub = parser.add_subparsers(dest="command", required=True)
    plan_parser = sub.add_parser("plan", help="refresh exact rows and freeze a bounded target plan")
    plan_parser.add_argument("config")
    plan_parser.add_argument("--acquisition", help="use a verified scout ACQUISITION.json and acquired transit queue")
    sub.add_parser("sources", help="show actual archive scouting/download capabilities")
    sub.add_parser("scout", help="discover a finite target/product sample or resume its PLAN.json").add_argument("config")
    sub.add_parser("acquire", help="download a verified SCOUT.json within its budget").add_argument("scout")
    for name in ("run", "status", "report"):
        sub.add_parser(name).add_argument("plan")
    worker = sub.add_parser("_worker", help="internal supervised stage; use run")
    worker.add_argument("plan")
    worker.add_argument("target")
    worker.add_argument("stage", choices=STAGES)
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    if args.command in ("sources", "scout", "acquire"):
        from . import cloud_scout
        if args.command == "sources":
            print(json.dumps(cloud_scout.inventory(), indent=2))
            return 0
        if args.command == "scout":
            import yaml
            path = inside(root, args.config)
            value = path if path.suffix == ".json" else yaml.safe_load(path.read_text())
            result = cloud_scout.scout(root, value)
            print((cloud_scout.capsule(root, result) / "SCOUT.json").relative_to(root).as_posix())
        else:
            result = cloud_scout.acquire(root, args.scout)
            print((cloud_scout.capsule(root, result) / "ACQUISITION.json").relative_to(root).as_posix())
        if args.command == "acquire":
            return 0 if any(r.get("state") == "downloaded" for r in result["products"]) else 1
        return 0 if result.get("targets") else 1
    if args.command == "plan":
        import yaml
        config = yaml.safe_load(inside(root, args.config).read_text(encoding="utf-8"))
        if args.acquisition:
            from .cloud_scout import bridge_config
            config = bridge_config(root, config, args.acquisition)
        plan = make_plan(root, config)
        print(plan_path(root, plan).relative_to(root).as_posix())
        print(f"Selected {len(plan['targets'])}; accounted {len(plan['selection'])} queue rows; no science run.")
        return 0
    plan = load_plan(root, Path(args.plan) if Path(args.plan).is_absolute() else inside(root, args.plan))
    if args.command == "run":
        return run_plan(root, plan)
    if args.command == "_worker":
        result = run_stage(root, plan, args.target, args.stage)
        print(json.dumps(result, indent=2), flush=True)
        return 0 if result.get("status") == "completed" else 2
    if args.command == "report":
        from .batch import LedgerLock
        lock = LedgerLock(plan_path(root, plan).parent / "ledger.sqlite")
        lock.acquire()
        try:
            path = write_report(root, plan)
        finally:
            lock.release()
    else:  # status is read-only and can inspect completed checkpoints while a worker runs
        path = report_dir(root, plan) / "REPORT.md"
    print(json.dumps(board(root, plan), indent=2))
    print(path.relative_to(root).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

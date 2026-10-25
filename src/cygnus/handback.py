"""Tier contracts and verified handbacks between local, Colab and cloud-agent executions.

A *handback* is the small, reviewable result of running a tier somewhere else: either a cloud
capsule written by ``cygnus.cloud`` (``docs/handbacks/<plan-id>/``) or a Colab higher-tier export
(``Cygnus/colab_runs/<run>/``). Whatever produced it, the local repository accepts it only after
:func:`verify` re-derives every claim from the shipped bytes:

* every file is listed in the manifest with the right SHA-256; no unsafe path, symlink, bulk FITS,
  credential or private machine path;
* checkpoints match their artifacts, lineage and upstream receipts; decisions and earned tiers are
  re-derived from the sky records with ``campaign.tiers``, never read from labels;
* each stage carries the outputs its contract requires, and no automated stage assigns evidence
  above an Unverified lead or changes the evidence of the record it started from;
* the code commit exists in local history and (for cloud capsules) its source bytes match it.

:func:`ingest` then imports the review set into ``docs/handbacks/<id>/`` (files over
``IMPORT_MAX_BYTES`` stay in Drive/scratch and are listed with their hashes), regenerates
``reports/handback-<id>/`` (report, search log, sky record, INGEST.json) and a managed STATUS block.
Nothing is promoted into ``campaigns/`` or ``publish/``: that remains scientific review.

CLI: ``python -m cygnus.tier`` (contracts, verify, ingest, cycle).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import time
from collections import Counter
from copy import deepcopy
from pathlib import Path, PurePosixPath

from .campaign.tiers import decide, rank, unmapped_checks
from .colab import read_manifest, write_manifest
from .fileio import atomic_write_json, atomic_write_text, sha256_file
from .ledger import now_utc
from .skyrecord import SCHEMA as SKY_SCHEMA, validate as validate_record

SCHEMA = "cygnus.handback/1"
CAPSULE = "cygnus.cloud_capsule/1"
COLAB_T2 = "cygnus.higher_tier_export/1"
ENVIRONMENTS = ("local", "colab", "cloud-agent")
HANDBACK_FILE = "HANDBACK.json"
INGEST_FILE = "INGEST.json"
IMPORTED_MANIFEST = "IMPORTED.sha256"
# Automated tiers never promote evidence; promotion is scientific review (AGENTS.md evidence levels).
AUTOMATED_EVIDENCE = (None, "Unverified lead")
MAX_FILE_BYTES = 64 * 1024**2          # anything larger is not a review artifact
MAX_TOTAL_BYTES = 512 * 1024**2
IMPORT_MAX_BYTES = 1024**2            # larger verified files stay in Drive/scratch, listed by hash
FORBIDDEN = re.compile(r"(\.fits(\.gz|\.fz)?|\.fz|\.sqlite(-wal|-shm|-journal)?|\.db|rclone\.conf|\.env|"
                       r"\.pem|\.key|credentials\.json|token\.json)$", re.I)
COMPANION = {"ledger.sqlite"}          # Colab exports list their companion ledger; it is never imported
TEXT = (".json", ".md", ".yaml", ".yml", ".txt", ".csv", ".sha256", ".log", ".jsonl")
PRIVATE = re.compile(
    r"(?:[A-Za-z]:(?:\\\\|\\|/)(?:Users|AO_Artifacts|Documents and Settings)\b|/home/[a-z_][\w.-]*/|"
    r"/Users/[A-Za-z][\w.-]*/|/root/|\bya29\.[\w-]{10,}|\bgh[pousr]_[A-Za-z0-9]{20,}|\bsk-[A-Za-z0-9_-]{20,}|"
    r"\bAKIA[0-9A-Z]{16}\b|-----BEGIN [A-Z ]*PRIVATE KEY-----|\"(?:access|refresh)_token\"\s*:)")
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,120}$")

# --------------------------------------------------------------------------- tier contracts
# One entry per executable stage. ``outputs`` are required files relative to the stage directory;
# a handback lacking any of them is rejected. Gates restate campaign.tiers, which enforces them.
_COMMON = ["sky_record.json", "REPORT.md", "SEARCH_LOG.md"]
CONTRACTS = {
    "screen": {
        "tiers": "T0/T1",
        "runs": "native T0/T1 campaign screen: calibrated SPOC light curves, known-signal control, "
                "residual screen, aliases, context and event-time prior art",
        "inputs": ["exact refreshed TOI/TIC row with its query and timezone-aware retrieval time",
                   "SPOC products by product ID, or acquisition-verified pinned inputs"],
        "outputs": _COMMON + ["SPEC.yaml", "STAGE.json", "SOURCE_ROW.json", "runner/RUN_SUMMARY.json"],
        "gate_in": "selected in a verified plan; exact source row younger than source_max_age_hours",
        "gate_out": "completed record that re-derives to T2; covered positive control not failed",
        "may_earn": ["T0", "T1", "T2", "T3", "closed"],
        "evidence": "null or Unverified lead",
    },
    "T2": {
        "tiers": "T2",
        "runs": "native pixel/neighbour/sibling vetting on the pinned source products and saved event "
                "selection, then event-epoch empirical nulls and event-depth injection recovery",
        "inputs": ["verified upstream screen checkpoint that earned T2, not escalated or closed",
                   "exact source products pinned by ID, size and SHA-256; saved period aliases"],
        "outputs": _COMMON + ["SPEC.yaml", "STAGE.json", "SOURCE_SPEC.yaml", "SOURCE_RECORD.json",
                              "period_aliases.json", "vetting/vetting.json", "event_null.json",
                              "runner/fetch_products.json", "FOLLOWUP_PRODUCTS.json"],
        "gate_in": "upstream earned >= T2; no failed artifact interlock or positive control",
        "gate_out": "T3 needs passed localization on every defining event, passed blend census, calibrated "
                    "and event-epoch nulls, plus a recipe budget and discriminating question",
        "may_earn": ["T2", "T3", "closed"],
        "evidence": "unchanged from SOURCE_RECORD.json",
    },
    "T3": {
        "tiers": "T3",
        "runs": "requested supported diagnostics: archive metadata, transit-tied RV fit and TESS PRF source "
                "preference on validated input packets",
        "inputs": ["verified upstream T2 checkpoint that earned T3",
                   "checksummed input packets with provenance and a matching quality receipt"],
        "outputs": _COMMON + ["SPEC.yaml", "STAGE.json", "SOURCE_RECORD.json", "diagnostics.json", "INPUTS.json"],
        "gate_in": "upstream earned T3, budget and discriminating question in the recipe",
        "gate_out": "none automated: T4, independent-sky confirmation and evidence promotion need review",
        "may_earn": ["T2", "T3", "closed"],
        "evidence": "unchanged from SOURCE_RECORD.json",
    },
    "colab_T2": {
        "tiers": "T2",
        "runs": "notebooks/cygnus_higher_tiers_colab.ipynb on a finalized first-stage export",
        "inputs": ["manifest-verified first-stage export; targets re-derived as T2-eligible"],
        "outputs": _COMMON + ["SOURCE_SPEC.yaml", "FOLLOWUP_SPEC.yaml", "SOURCE_RECORD.json", "SOURCE_LINK.json",
                              "period_aliases.json", "vetting/vetting.json", "event_null.json",
                              "runner/fetch_products.json"],
        "gate_in": "first-stage audit re-derives T2; frozen specialist targets excluded",
        "gate_out": "same T2->T3 gates as the cloud T2 stage; T3 is not run in Colab",
        "may_earn": ["T2", "T3", "closed"],
        "evidence": "unchanged from SOURCE_RECORD.json",
    },
}


class HandbackError(ValueError):
    """The handback cannot be read at all (as opposed to a list of verification problems)."""


# --------------------------------------------------------------------------- failure classes
# Lessons from past runs, matched on the recorded message. Tests pin each one.
FAILURES = [
    ("storage_quota", re.compile(r"RATE_LIMIT_EXCEEDED|rateLimitExceeded|userRateLimitExceeded|HTTP 429|quota", re.I),
     "retry later with backoff; a quota error is not a verification result"),
    ("storage_auth", re.compile(r"invalid_grant|unauthorized_client|token (?:has been )?expired|oauth", re.I),
     "re-run the rclone OAuth flow and tell the user; never hide the failure"),
    ("not_visible", re.compile(r"directory not found|object not found|exit (?:status )?3\b", re.I),
     "this route cannot see the folder (drive.file scope); use another route or --local"),
    ("transient", re.compile(r"\b50[234]\b|timed out|Timeout|Connection (?:reset|aborted)|RemoteDisconnected|"
                             r"Temporary failure|Max retries exceeded|IncompleteRead|ProxyError", re.I),
     "bounded retry"),
    ("coverage_guard", re.compile(r"no (?:measured/covered|covered/measured) defining event|"
                                  r"lacks a measur\w+ (?:defining|/covered)", re.I),
     "scientific incompleteness; inspect coverage/extraction, never relax the guard or auto-retry"),
    ("integrity", re.compile(r"checksum|hash|lineage|manifest|artifact set|changed", re.I),
     "stop: a person must inspect the altered or corrupt packet"),
    ("budget", re.compile(r"budget|free scratch space", re.I),
     "stopped by a resource budget; not a scientific null result"),
    ("environment", re.compile(r"ModuleNotFoundError|ImportError|pip check|dependency conflict|requires .*<", re.I),
     "fix the isolated environment (tools/setup_cloud.py); do not weaken tests"),
]
RETRYABLE = {"storage_quota", "transient"}


def classify_failure(text: str | None) -> dict:
    for name, pattern, action in FAILURES:
        if text and pattern.search(text):
            return {"class": name, "retryable": name in RETRYABLE, "action": action}
    return {"class": "unknown", "retryable": False, "action": "stop and inspect the attempt log"}


def with_retries(fn, *, attempts=3, base_s=30.0, sleep=time.sleep, log=None):
    """Call ``fn`` and retry only retryable failures, backing off 30 s, 120 s, ... Re-raises the last."""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception as exc:
            kind = classify_failure(f"{type(exc).__name__}: {exc}")
            if log is not None:
                log.append({"attempt": attempt, "utc": now_utc(), "error": str(exc)[-500:], **kind})
            if not kind["retryable"] or attempt == attempts:
                raise
            sleep(min(600.0, base_s * 4 ** (attempt - 1)))


# --------------------------------------------------------------------------- helpers
def safe_id(value):
    value = str(value)
    if not SAFE_ID.match(value) or value in (".", ".."):
        raise HandbackError(f"unsafe handback/target id: {value!r}")
    return value


def report_slug(hid):
    slug = re.sub(r"[^a-z0-9-]+", "-", str(hid).lower()).strip("-")
    return ("handback-" + slug)[:63].rstrip("-")


def _json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _unsafe(rel):
    parts = PurePosixPath(rel)
    return (not rel or parts.is_absolute() or ".." in parts.parts or "\\" in rel or ":" in rel or
            rel.startswith("/"))


def _files(base):
    out = {}
    for path in sorted(Path(base).rglob("*")):
        rel = path.relative_to(base).as_posix()
        if path.is_symlink():
            out[rel] = None
        elif path.is_file():
            out[rel] = path
    return out


def detect(directory):
    """Which handback format a directory holds."""
    directory = Path(directory)
    if (directory / HANDBACK_FILE).is_file():
        fmt = _json(directory / HANDBACK_FILE).get("format")
        if fmt in (CAPSULE, COLAB_T2):
            return fmt
    if (directory / "LINEAGE.json").is_file():
        schema = _json(directory / "LINEAGE.json").get("schema")
        if schema == "cygnus.cloud_plan/1":
            return CAPSULE
        if schema == "cygnus.higher_tier_lineage/1":
            return COLAB_T2
    raise HandbackError("not a recognized handback: no HANDBACK.json or known LINEAGE.json schema")


def git_code_check(repo):
    """Default code verifier: the commit must exist locally, and capsule source bytes must match it."""
    repo = Path(repo)

    def check(commit, files=None):
        if not commit or not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
            return [f"code commit is not a full SHA: {commit!r}"]
        probe = subprocess.run(["git", "cat-file", "-e", f"{commit}^{{commit}}"], cwd=repo,
                               capture_output=True, text=True)
        if probe.returncode:
            return [f"code commit {commit[:12]} is not in local history: fetch the branch that produced it"]
        problems = []
        for rel, digest in sorted((files or {}).items()):
            blob = subprocess.run(["git", "show", f"{commit}:{rel}"], cwd=repo, capture_output=True)
            if blob.returncode or hashlib.sha256(blob.stdout.replace(b"\r\n", b"\n")).hexdigest() != digest:
                problems.append(f"code {rel} differs from commit {commit[:12]}: run from a clean, committed checkout")
                if len(problems) >= 5:
                    break
        return problems
    return check


# --------------------------------------------------------------------------- shared payload checks
def _payload_problems(directory, manifest, allowed_unlisted, *, allow_absent=()):
    problems, sizes = [], {}
    present = _files(directory)
    for rel, path in present.items():
        if path is None:
            problems.append(f"symlink in handback: {rel}")
            continue
        if rel not in manifest and rel not in allowed_unlisted:
            problems.append(f"file not covered by the manifest: {rel}")
        if FORBIDDEN.search(rel) and PurePosixPath(rel).name not in COMPANION:
            problems.append(f"bulk product, ledger or credential file in handback: {rel}")
        sizes[rel] = path.stat().st_size
        if sizes[rel] > MAX_FILE_BYTES:
            problems.append(f"file exceeds {MAX_FILE_BYTES // 1024**2} MiB review limit: {rel}")
        elif rel.lower().endswith(TEXT) and sizes[rel] <= IMPORT_MAX_BYTES:
            # Only files that can enter git are scanned; larger ones stay in Drive/scratch.
            text = path.read_text(encoding="utf-8", errors="replace")
            hit = PRIVATE.search(text)
            if hit:
                problems.append(f"private machine path or credential pattern in {rel}: {hit.group(0)[:24]!r}")
    if sum(sizes.values()) > MAX_TOTAL_BYTES:
        problems.append(f"handback exceeds {MAX_TOTAL_BYTES // 1024**2} MiB in total")
    for rel, digest in manifest.items():
        if _unsafe(rel):
            problems.append(f"unsafe manifest path: {rel}")
        elif rel not in present:
            if rel not in allow_absent:
                problems.append(f"manifest-listed file missing: {rel}")
        elif present[rel] is not None and sha256_file(present[rel]) != digest:
            problems.append(f"checksum mismatch: {rel}")
    return problems, sizes


def _record_problems(record, root, cid, stage, contract, source_record=None):
    problems = [f"{cid}/{stage}: {p}" for p in validate_record(record, Path(root))]
    if record.get("id") != cid:
        problems.append(f"{cid}/{stage}: sky record id is {record.get('id')!r}")
    unknown = unmapped_checks([record])
    if unknown:
        problems.append(f"{cid}/{stage}: unmapped gate checks {sorted(unknown)}")
    if record.get("evidence") not in AUTOMATED_EVIDENCE:
        problems.append(f"{cid}/{stage}: automated stage assigned evidence {record.get('evidence')!r}; "
                        "promotion requires scientific review")
    if source_record is not None and record.get("evidence") != source_record.get("evidence"):
        problems.append(f"{cid}/{stage}: evidence changed from {source_record.get('evidence')!r} to "
                        f"{record.get('evidence')!r}")
    tier = decide(record, spec={}).tier
    if tier not in contract["may_earn"]:
        problems.append(f"{cid}/{stage}: earned tier {tier} is outside the {stage} contract")
    if tier == "T4":
        problems.append(f"{cid}/{stage}: T4 is not automated")
    return problems


def _target_row(record, cid, earned, run_at, stages, status="completed"):
    position = next(iter(record.get("targets") or []), {})
    return {"earned": earned, "run_at": run_at, "status": status, "stages": stages,
            "evidence": record.get("evidence"), "outcome": record.get("outcome"),
            "name": position.get("name", cid),
            "position": {k: position[k] for k in ("ra_deg", "dec_deg", "frame", "epoch", "position_source")
                         if k in position},
            "blockers": decide(record, spec={}).blockers,
            "concern": _concern(record)}


def _concern(record):
    severity = {"failed": 3, "inconclusive": 2, "not_tested": 1, "passed": 0}
    worst = max(record.get("checks", []), key=lambda c: severity.get(c.get("state"), 0), default=None)
    if not worst or worst.get("state") == "passed":
        return None
    return f"{worst['name']}: {worst['state']}"


# --------------------------------------------------------------------------- cloud capsules
def _verify_capsule(directory, code_check):
    from . import cloud
    directory = Path(directory)
    problems, warnings = [], []
    try:
        plan = _json(directory / "LINEAGE.json")
        manifest = read_manifest(directory / "MANIFEST.sha256")
        receipts = _json(directory / "CHECKPOINTS.json")
    except (OSError, ValueError) as exc:
        return {"problems": [f"capsule metadata unreadable: {exc}"], "warnings": [], "targets": {}}
    body = {k: v for k, v in plan.items() if k != "id"}
    if plan.get("schema") != "cygnus.cloud_plan/1" or plan.get("id") != "cloud-" + cloud.digest(body)[:16]:
        problems.append("plan lineage digest does not match its id")
    if directory.name != plan.get("id"):
        problems.append(f"capsule folder {directory.name!r} differs from plan id {plan.get('id')!r}")
    payload, sizes = _payload_problems(directory, manifest, {"MANIFEST.sha256", HANDBACK_FILE, IMPORTED_MANIFEST,
                                                                  "LOCATION.json"})
    problems += payload
    # Records point at docs/handbacks/<id>/...; verify them against a root where that path holds.
    rel = Path(cloud.HANDBACK_BASE) / directory.name
    root = directory.parents[len(rel.parts) - 1] if directory.as_posix().endswith(rel.as_posix()) else None
    if root is None:
        problems.append(f"capsule must sit at <root>/{rel.as_posix()} to verify its record paths")
        return {"problems": problems, "warnings": warnings, "targets": {}, "plan": plan, "sizes": sizes}
    code = plan.get("code", {})
    problems += code_check(code.get("git_commit"), code.get("files"))
    targets = {}
    for cid in sorted(plan.get("targets", {})):
        completed, previous_receipt, previous = [], None, None
        for stage in cloud.STAGES:
            key = f"{cid}.{stage}"
            if key not in receipts:
                break
            receipt = receipts[key]
            where = f"{cid}/{stage}"
            out = directory / "targets" / cid / stage
            missing = [name for name in CONTRACTS[stage]["outputs"] if not (out / name).is_file()]
            if missing:
                problems.append(f"{where}: contract outputs missing: {missing}")
                break
            artifacts = {p.relative_to(out).as_posix(): sha256_file(p) for p in sorted(out.rglob("*")) if p.is_file()}
            if receipt.get("artifacts") != artifacts:
                problems.append(f"{where}: checkpoint artifact set or hash changed")
                break
            if receipt.get("lineage_sha256") != cloud.digest(plan):
                problems.append(f"{where}: checkpoint lineage differs from the plan")
                break
            try:
                decision = cloud._stage_decision(root, plan, cid, stage)
            except (OSError, KeyError, TypeError, ValueError) as exc:
                problems.append(f"{where}: {exc}")
                break
            if receipt.get("decision") != decision or receipt.get("decision_sha256") != cloud.digest(decision):
                problems.append(f"{where}: shipped decision differs from the re-derived decision")
                break
            if stage != "screen":
                expected = cloud.digest_receipt(previous_receipt)
                if receipt.get("upstream_sha256") != expected:
                    problems.append(f"{where}: upstream checkpoint receipt changed")
                    break
                if previous["decision"]["escalation"] or previous["earned"] == "closed" or \
                        rank(previous["earned"]) < rank(stage):
                    problems.append(f"{where}: ran without satisfying the upstream tier gate")
                    break
            record = _json(out / "sky_record.json")
            source = _json(out / "SOURCE_RECORD.json") if stage != "screen" else None
            problems += _record_problems(record, root, cid, stage, CONTRACTS[stage], source)
            completed.append(stage)
            previous_receipt, previous = receipt, decision
        if previous:
            targets[cid] = _target_row(_json(directory / "targets" / cid / previous["run_at"] / "sky_record.json"),
                                       cid, previous["earned"], previous["run_at"], completed)
            targets[cid]["escalation"] = previous["decision"]["escalation"]
        else:
            targets[cid] = {"earned": None, "run_at": None, "status": "incomplete", "stages": [],
                            "name": plan["targets"][cid].get("name", cid), "evidence": None}
    extra = set(receipts) - {f"{c}.{s}" for c in plan.get("targets", {}) for s in cloud.STAGES}
    if extra:
        problems.append(f"checkpoints for targets/stages outside the plan: {sorted(extra)}")
    board = directory / "tier_board.json"
    if board.is_file():
        shipped = _json(board).get("targets", {})
        for cid, row in targets.items():
            if shipped.get(cid, {}).get("earned") != row["earned"] or shipped.get(cid, {}).get("run_at") != row["run_at"]:
                problems.append(f"{cid}: tier_board.json claims differ from re-derived checkpoints")
    return {"problems": problems, "warnings": warnings, "targets": targets, "plan": plan, "sizes": sizes,
            "manifest": manifest, "code": {"git_commit": code.get("git_commit"),
                                           "source_sha256": code.get("source_sha256")}}


# --------------------------------------------------------------------------- Colab exports
def _verify_colab(directory, code_check):
    from . import cloud, colab_sync
    directory = Path(directory)
    problems, warnings = [], []
    try:
        lineage = _json(directory / "LINEAGE.json")
        manifest, location = colab_sync._manifest(directory)
    except (OSError, ValueError, KeyError) as exc:
        return {"problems": [f"Colab export metadata unreadable: {exc}"], "warnings": [], "targets": {}}
    absent = {rel for rel in manifest if PurePosixPath(rel).name in COMPANION}
    payload, sizes = _payload_problems(directory, manifest, {"MANIFEST.sha256", "LOCATION.json", HANDBACK_FILE, IMPORTED_MANIFEST},
                                       allow_absent=absent)
    problems += payload
    if any(not (directory / rel).is_file() for rel in absent):
        warnings.append("companion ledger not present; it is never imported or merged")
    if lineage.get("schema") != "cygnus.higher_tier_lineage/1" or lineage.get("max_tier") != "T2":
        problems.append("Colab lineage is not a T2 higher-tier contract")
    if location.get("id") != f"colab_runs/{directory.name}":
        problems.append(f"LOCATION id {location.get('id')!r} differs from folder {directory.name!r}")
    problems += code_check(lineage.get("code_commit"))
    try:
        audit = colab_sync.audit(directory)
    except (OSError, ValueError, KeyError) as exc:
        problems.append(f"tier audit failed: {exc}")
        audit = {"targets": {}}
    helpers = cloud.notebook_helpers()
    done = _json(directory / "done.json") if (directory / "done.json").is_file() else {}
    contract = CONTRACTS["colab_T2"]
    targets = {}
    for cid in sorted(lineage.get("targets", [])):
        out = directory / "campaigns" / cid
        if cid not in done:
            targets[cid] = {"earned": None, "run_at": None, "status": "incomplete", "stages": [], "name": cid,
                            "evidence": None,
                            "attempt": (directory / "errors" / f"{cid}.json").is_file() or
                                       (directory / "ATTEMPTS" / cid).is_dir()}
            continue
        missing = [name for name in contract["outputs"] if not (out / name).is_file()]
        if missing:
            problems.append(f"{cid}/T2: contract outputs missing: {missing}")
            continue
        if not helpers["completed_target"](directory, cid):
            problems.append(f"{cid}/T2: checkpoint artifacts, lineage or decision do not verify")
            continue
        record = _json(out / "sky_record.json")
        problems += _record_problems(record, directory, cid, "T2", contract, _json(out / "SOURCE_RECORD.json"))
        earned = audit["targets"].get(cid, {}).get("tier")
        if earned != done[cid].get("earned"):
            problems.append(f"{cid}/T2: done.json tier {done[cid].get('earned')!r} differs from audit {earned!r}")
        targets[cid] = _target_row(record, cid, done[cid].get("earned"), "T2", ["T2"])
    extra = set(done) - set(lineage.get("targets", []))
    if extra:
        problems.append(f"done.json lists targets outside the lineage: {sorted(extra)}")
    return {"problems": problems, "warnings": warnings, "targets": targets, "lineage": lineage,
            "location": location, "sizes": sizes, "manifest": manifest,
            "code": {"git_commit": lineage.get("code_commit"), "notebook_revision": lineage.get("revision")}}


# --------------------------------------------------------------------------- public API
def summary(directory, fmt, found, environment, harness=None):
    """The HANDBACK.json claims for a verified payload (computed, never copied from the producer)."""
    directory = Path(directory)
    targets = found["targets"]
    source = ({"plan": found["plan"]["id"], "queue": found["plan"]["config"]["queue"],
               "queue_sha256": found["plan"]["queue_sha256"], "max_tier": found["plan"]["config"]["max_tier"],
               "selected": len(found["plan"]["targets"]), "accounted_rows": len(found["plan"]["selection"])}
              if fmt == CAPSULE else
              {"source_run": found["lineage"]["source_run"], "source_commit": found["lineage"]["source_commit"],
               "source_manifest_sha256": found["lineage"]["source_manifest_sha256"],
               "max_tier": found["lineage"]["max_tier"], "null_params": found["lineage"].get("null_params")})
    return {"schema": SCHEMA, "id": directory.name, "format": fmt, "environment": environment,
            "harness": harness, "code": found["code"], "source": source,
            "manifest_sha256": sha256_file(directory / "MANIFEST.sha256"),
            "counts": dict(sorted(Counter(str(r["earned"] or r["status"]) for r in targets.values()).items())),
            "targets": {cid: {k: row.get(k) for k in ("earned", "run_at", "status", "stages", "evidence")}
                        for cid, row in targets.items()}}


def verify(directory, *, code_check=None, repo=None):
    """Every problem that stops this handback being accepted. ``ok`` is True only with none."""
    directory = Path(directory)
    if not directory.is_dir():
        raise HandbackError(f"{directory} is not a directory")
    safe_id(directory.name)
    fmt = detect(directory)
    code_check = code_check or git_code_check(repo or Path(__file__).resolve().parents[2])
    found = (_verify_capsule if fmt == CAPSULE else _verify_colab)(directory, code_check)
    claims = None
    if (directory / HANDBACK_FILE).is_file():
        claims = _json(directory / HANDBACK_FILE)
        if claims.get("schema") != SCHEMA or claims.get("environment") not in ENVIRONMENTS:
            found["problems"].append("HANDBACK.json schema/environment is invalid")
    elif fmt == CAPSULE:
        found["problems"].append("cloud capsule has no HANDBACK.json: run `python -m cygnus.tier pack`")
    if not found["problems"]:
        recomputed = summary(directory, fmt, found, (claims or {}).get("environment", "colab"),
                             (claims or {}).get("harness"))
        if claims is not None:
            for key in ("id", "format", "code", "source", "manifest_sha256", "counts", "targets"):
                if claims.get(key) != recomputed[key]:
                    found["problems"].append(f"HANDBACK.json {key} differs from the re-derived value")
        found["handback"] = recomputed
    found.update(ok=not found["problems"], format=fmt, id=directory.name)
    return found


def pack(capsule, *, environment, harness=None, code_check=None, repo=None):
    """Write HANDBACK.json into a cloud capsule after verifying it. Raises with the problem list."""
    capsule = Path(capsule)
    if environment not in ENVIRONMENTS:
        raise HandbackError(f"environment must be one of {ENVIRONMENTS}")
    (capsule / HANDBACK_FILE).unlink(missing_ok=True)
    found = verify(capsule, code_check=code_check, repo=repo)
    problems = [p for p in found["problems"] if "no HANDBACK.json" not in p]
    if problems:
        raise HandbackError("capsule failed verification: " + "; ".join(problems[:12]))
    claims = summary(capsule, CAPSULE, found, environment, harness)
    claims["packed_utc"] = now_utc()
    atomic_write_json(capsule / HANDBACK_FILE, claims)
    return claims


# --------------------------------------------------------------------------- ingest
def _write_status_block(root, hid, text):
    status = Path(root) / "docs/STATUS.md"
    old = status.read_text(encoding="utf-8") if status.exists() else "# Project status\n"
    start, end = f"<!-- cygnus:handback:{hid}:start -->", f"<!-- cygnus:handback:{hid}:end -->"
    block = f"{start}\n\n{text}\n\n{end}"
    if start in old:
        if end not in old:
            raise HandbackError("unterminated managed STATUS block")
        new = old[:old.index(start)] + block + old[old.index(end) + len(end):]
    else:
        first, sep, rest = old.partition("\n")
        new = first + "\n\n" + block + "\n" + sep + rest
    if new != old:
        atomic_write_text(status, new)


def _reports(root, hid, found, receipt):
    """Regenerate reports/handback-<id>/ from verified claims. Deterministic for the same receipt."""
    slug = report_slug(hid)
    out = Path(root) / "reports" / slug
    rel = f"reports/{slug}"
    claims = found["handback"]
    rows = found["targets"]
    counts = ", ".join(f"{k}: {v}" for k, v in claims["counts"].items()) or "no targets"
    lines = [f"# Handback {hid}", "", "<!-- cygnus:generated-draft -->", "",
             f"Format `{claims['format']}` from **{claims['environment']}**"
             f"{' (' + claims['harness'] + ')' if claims.get('harness') else ''}; code "
             f"`{claims['code'].get('git_commit')}`. Verified {receipt['verified_utc']}: "
             f"{len(found['manifest'])} manifest files, {len(receipt['imported'])} imported, "
             f"{len(receipt['retained_elsewhere'])} kept outside git by size.", "",
             f"**{counts}.** Earned tiers are re-derived from the shipped sky records; `run_at` is the "
             "highest executed stage. No evidence was promoted and no canonical campaign record changed.", "",
             "| Target | Earned | Executed | Evidence | Strongest concern | Next-tier blockers |",
             "| --- | --- | --- | --- | --- | --- |"]
    for cid, row in rows.items():
        blockers = "; ".join(row.get("blockers") or []) or ("not completed; see attempt diagnostics"
                                                              if row["status"] == "incomplete" else "")
        lines.append(f"| {row.get('name', cid)} | {row['earned'] or 'incomplete'} | {row['run_at'] or '—'} | "
                     f"{row.get('evidence') or '—'} | {(row.get('concern') or '—').replace('|', '/')} | "
                     f"{blockers.replace('|', '/')} |")
    lines += ["", "## What this does not establish", "",
              "A verified handback certifies saved-file integrity, lineage and re-derived tiers. It is not a",
              "scientific review: localization, blends, nulls and event-time prior art must be read in the",
              "per-target records. Empirical k/N nulls are selection-touched with finite resolution; zero",
              "exceedances are not zero probability. Closed routes need event-by-event review before any",
              "canonical record is reconciled. T4, independent-sky confirmation and publication are not run.", "",
              f"Payload: [`docs/handbacks/{hid}/`](../../docs/handbacks/{hid}/). Verification receipt: "
              f"[INGEST.json]({INGEST_FILE})."]
    if found.get("warnings"):
        lines += ["", "Warnings: " + "; ".join(found["warnings"]) + "."]
    atomic_write_text(out / "REPORT.md", "\n".join(lines) + "\n")
    source = claims["source"]
    atomic_write_text(out / "SEARCH_LOG.md", "\n".join([
        f"# Handback search log: {hid}", "",
        "Source: " + ", ".join(f"{k}={v}" for k, v in source.items() if not isinstance(v, dict)) + ".",
        f"Targets accounted: {len(rows)}; completed: {sum(r['status'] == 'completed' for r in rows.values())}; "
        f"incomplete: {sum(r['status'] == 'incomplete' for r in rows.values())}.",
        "Selection, exclusions, exact queries, products, epochs, thresholds and seeds are in the payload "
        "(LINEAGE.json, SELECTION.json or SOURCE_AUDIT.json, and each stage's SEARCH_LOG.md).",
        f"Handback manifest SHA-256: {claims['manifest_sha256']}.", ""]))
    targets = [{"name": r["name"], **r["position"]} for r in rows.values()
               if {"ra_deg", "dec_deg", "frame", "epoch", "position_source"} <= set(r.get("position") or {})]
    partial = bool(receipt["retained_elsewhere"])
    atomic_write_json(out / INGEST_FILE, receipt)
    atomic_write_json(out / "sky_record.json", {
        "schema": SKY_SCHEMA, "id": slug, "title": f"Verified tier handback {hid}", "kind": "workflow audit",
        "status": "completed" if targets else "draft", "outcome": "pipeline_check" if targets else "not_run",
        "evidence": None, "date": receipt["verified_utc"][:10] if targets else None,
        "summary": "Operational verification of an external tier run. Per-target scientific records are in "
                   "the payload; nothing was promoted.",
        "spec": None, "report": rel + "/REPORT.md", "search_log": rel + "/SEARCH_LOG.md",
        "targets": targets, "products": [],
        "checks": [{"name": "Dated follow-up handback verification", "state": "passed",
                    "note": "manifest, lineage, checkpoints, contracts and re-derived tiers verified",
                    "source": INGEST_FILE},
                   {"name": "Dated follow-up handback import completeness",
                    "state": "inconclusive" if partial else "passed",
                    "note": (f"{len(receipt['retained_elsewhere'])} large file(s) verified but kept outside git"
                             if partial else "full payload imported"), "source": INGEST_FILE}]})
    _write_status_block(root, hid, f"**Handback {hid}** ({claims['environment']}, {claims['format']}): {counts}. "
                        "Verified and imported; scientific review pending, no evidence promoted. "
                        f"[Report](../{rel}/REPORT.md).")
    return out


def ingest(source, root, *, origin=None, code_check=None, journal=None, route_label=None):
    """Verify a handback directory and import it. Returns the INGEST receipt; raises on rejection.

    ``source`` is a local directory (already fetched, or the in-repo capsule itself). Rejection writes
    only to the ignored journal: the repository is unchanged.
    """
    root, source = Path(root).resolve(), Path(source).resolve()
    hid = safe_id(source.name)
    journal = Path(journal or root / "state/handbacks/JOURNAL.jsonl")
    found = verify(source, code_check=code_check, repo=root)
    entry = {"utc": now_utc(), "id": hid, "origin": origin or "local directory", "ok": found["ok"],
             "problems": found["problems"][:50]}
    journal.parent.mkdir(parents=True, exist_ok=True)
    with journal.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(entry) + "\n")
    if not found["ok"]:
        raise HandbackError(f"handback {hid} rejected ({len(found['problems'])} problem(s)): " +
                            "; ".join(found["problems"][:8]))
    dest = root / "docs/handbacks" / hid
    imported, elsewhere = {}, {}
    in_place = dest.resolve() == source
    for rel, digest in sorted(found["manifest"].items()):
        size = found["sizes"].get(rel)
        if size is None or PurePosixPath(rel).name in COMPANION:   # companion ledger is never imported
            continue
        if size > IMPORT_MAX_BYTES and not in_place:
            elsewhere[rel] = {"sha256": digest, "bytes": size}
        else:
            imported[rel] = digest
    if dest.exists() and not in_place:
        old = dest / HANDBACK_FILE
        before = _json(old) if old.is_file() else {}
        done_before = {c for c, r in before.get("targets", {}).items() if r.get("status") == "completed"}
        done_now = {c for c, r in found["handback"]["targets"].items() if r.get("status") == "completed"}
        # A resumed run of the same lineage may supersede its earlier handback; nothing may be lost.
        if before.get("format") != found["format"] or not done_before <= done_now or any(
                before["targets"][c].get("stages", []) != found["handback"]["targets"][c]["stages"][
                    :len(before["targets"][c].get("stages", []))] for c in done_before):
            raise HandbackError(f"docs/handbacks/{hid} already holds a handback this one does not supersede; "
                                "never overwritten")
    if not in_place:
        tmp = dest.with_name(dest.name + ".importing")
        shutil.rmtree(tmp, ignore_errors=True)
        for rel in list(imported) + ["MANIFEST.sha256"] + (["LOCATION.json"] if (source / "LOCATION.json").is_file() else []):
            target = tmp / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source / rel, target)
        atomic_write_json(tmp / HANDBACK_FILE, found["handback"])
        write_manifest(tmp / IMPORTED_MANIFEST, imported, comment=f"{hid}: files imported into git; "
                       "MANIFEST.sha256 is the full verified payload")
        if dest.exists():
            shutil.rmtree(dest)
        os.replace(tmp, dest)
    else:
        if not (dest / HANDBACK_FILE).is_file():
            atomic_write_json(dest / HANDBACK_FILE, found["handback"])
        write_manifest(dest / IMPORTED_MANIFEST, imported, comment=f"{hid}: in-place handback; full payload")
    receipt = {"schema": "cygnus.handback_ingest/1", "id": hid, "verified_utc": entry["utc"],
               "origin": origin or "local directory", "format": found["format"],
               "handback_sha256": sha256_file(dest / HANDBACK_FILE),
               "manifest_sha256": found["handback"]["manifest_sha256"],
               "imported_sha256": sha256_file(dest / IMPORTED_MANIFEST),
               "imported": imported, "retained_elsewhere": elsewhere, "warnings": found["warnings"],
               "scope": "integrity, lineage, contracts and re-derived tiers; not scientific review"}
    _reports(root, hid, {**found, "manifest": found["manifest"]}, receipt)
    location = source / "LOCATION.json"
    if route_label and location.is_file():
        from . import storage
        storage.upsert(storage.validate(_json(location)), root / "storage/locations.jsonl")
        storage.record_visibility(_json(location)["id"], route_label, True, root / "storage/locations.jsonl",
                                  note="full handback payload verified by cygnus.handback")
    return receipt


def check_imported(root):
    """Problems with handbacks already in the repository (used by the test suite)."""
    root = Path(root)
    problems = []
    for dest in sorted((root / "docs/handbacks").glob("*/")):
        hid = dest.name
        receipt_path = root / "reports" / report_slug(hid) / INGEST_FILE
        if not receipt_path.is_file():
            problems.append(f"{hid}: no {receipt_path.relative_to(root).as_posix()}; run `python -m cygnus.tier ingest`")
            continue
        receipt = _json(receipt_path)
        if not (dest / IMPORTED_MANIFEST).is_file() or sha256_file(dest / IMPORTED_MANIFEST) != receipt["imported_sha256"]:
            problems.append(f"{hid}: imported manifest differs from its ingest receipt")
            continue
        if sha256_file(dest / HANDBACK_FILE) != receipt["handback_sha256"]:
            problems.append(f"{hid}: HANDBACK.json changed after ingest")
        imported = read_manifest(dest / IMPORTED_MANIFEST)
        full = read_manifest(dest / "MANIFEST.sha256")
        if imported != receipt["imported"] or any(full.get(k) != v for k, v in imported.items()):
            problems.append(f"{hid}: imported files are not the verified payload")
        for rel, digest in imported.items():
            if not (dest / rel).is_file() or sha256_file(dest / rel) != digest:
                problems.append(f"{hid}: imported file changed or missing: {rel}")
                break
        claims = _json(dest / HANDBACK_FILE)
        for cid, row in claims.get("targets", {}).items():
            if row.get("evidence") not in AUTOMATED_EVIDENCE:
                problems.append(f"{hid}/{cid}: handback carries promoted evidence {row.get('evidence')!r}")
            if row.get("earned") == "T4":
                problems.append(f"{hid}/{cid}: handback claims T4")
    return problems


def contracts():
    return deepcopy(CONTRACTS)

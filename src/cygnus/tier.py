"""One command per environment: run a tier batch to a verified, ingested handback.

  local        python -m cygnus.tier cycle cloud/workflow.yaml --env local
  cloud agent  python3.12 tools/setup_cloud.py && .venv/bin/python -m cygnus.tier cycle cloud/workflow.yaml --env cloud-agent
  Colab        open notebooks/cygnus_higher_tiers_colab.ipynb, Run all; then locally
               python -m cygnus.tier colab ingest --latest

Each cycle step (preflight, plan, run, report, pack, deliver, ingest, cleanup) is journaled in
ignored ``state/tier_cycles/<name>/``; rerunning the same command resumes at the first unfinished
step and reuses the same PLAN.json, whose stages skip when their checkpoints verify. Science stays
in ``cygnus.cloud`` and the native tools; tier contracts and handback checks are in
``cygnus.handback``. No step promotes evidence, publishes, commits or pushes.

Other commands: ``contracts``, ``verify DIR``, ``ingest DIR``, ``check``, ``status NAME``,
``colab stage``.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import runpy
import shutil
import sys
import time
from pathlib import Path

from . import handback
from .config import WORKTREE, scratch_dir
from .fileio import atomic_write_json, sha256_file
from .ledger import now_utc

STEPS = ("preflight", "plan", "run", "report", "pack", "deliver", "cleanup")
EXIT_RETRY = 75   # EX_TEMPFAIL: rerun the same command later
# Checks that may fail on a shared workstation interpreter without making the run unverifiable:
# the 2026-10-17 preflight failed only `pip check` (an unrelated Gradio pin). Cloud agents get none.
LOCAL_TOLERATED = {"pip_check"}


def _digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class Cycle:
    """Ledgered step state for one named cycle; one writer at a time."""

    def __init__(self, root, name):
        self.root = Path(root)
        self.name = handback.safe_id(name)
        self.dir = self.root / "state/tier_cycles" / self.name
        self.path = self.dir / "CYCLE.json"
        self.journal = self.dir / "JOURNAL.jsonl"
        self.state = json.loads(self.path.read_text(encoding="utf-8")) if self.path.is_file() else None

    def open(self, recipe, env, recipe_sha256):
        fresh = {"schema": "cygnus.tier_cycle/1", "name": self.name, "env": env, "recipe": recipe,
                 "recipe_sha256": recipe_sha256, "created_utc": now_utc(), "steps": {}}
        if self.state is None:
            self.state = fresh
            self.save()
        elif (self.state["recipe"], self.state["recipe_sha256"], self.state["env"]) != (recipe, recipe_sha256, env):
            raise SystemExit(f"cycle {self.name} was started with a different recipe or environment; "
                             "use --name for a new cycle (recipes are never edited under a running cycle)")
        return self

    def save(self):
        atomic_write_json(self.path, self.state)

    def step(self, name):
        return self.state["steps"].setdefault(name, {"state": "pending", "attempts": 0})

    def log(self, step, state, **detail):
        row = self.step(step)
        row.update(state=state, utc=now_utc(), **detail)
        self.save()
        self.journal.parent.mkdir(parents=True, exist_ok=True)
        with self.journal.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps({"step": step, "state": state, "utc": row["utc"], **detail}) + "\n")

    def done(self, step):
        return self.step(step)["state"] in ("done", "skipped")


def preflight(root, env):
    tool = runpy.run_path(str(Path(root) / "tools/setup_cloud.py"))
    receipt = tool["preflight"](Path(root))
    tolerated = LOCAL_TOLERATED if env == "local" else set()
    failed = [c["name"] for c in receipt["checks"] if not c["passed"] and c["name"] not in tolerated]
    warned = [c["name"] for c in receipt["checks"] if not c["passed"] and c["name"] in tolerated]
    return failed, warned, receipt


def _last_failure(state_dir):
    from .cloud import read_attempts
    rows, _ = read_attempts(Path(state_dir) / "ATTEMPTS.jsonl")
    bad = [r for r in rows if r.get("state") != "ok"]
    return bad[-1] if bad else None


def cycle(root, recipe, *, env, name=None, deliver="auto", run_attempts=2, cleanup=None, acquisition=None,
          sleep=time.sleep, harness=None):
    """Run every unfinished step. Returns 0 when the handback was verified and delivered."""
    import yaml
    from . import cloud
    from .batch import LedgerLock

    root = Path(root).resolve()
    recipe_path = cloud.inside(root, recipe)
    raw = recipe_path.read_bytes()
    name = name or f"{recipe_path.stem}-{_digest(raw)[:10]}"
    state = Cycle(root, name).open(recipe_path.relative_to(root).as_posix(), env, _digest(raw))
    lock = LedgerLock(state.dir / "cycle")
    lock.acquire()
    try:
        if not state.done("preflight"):
            failed, warned, receipt = preflight(root, env)
            atomic_write_json(state.dir / "PREFLIGHT.json", receipt)
            if failed:
                state.log("preflight", "blocked", failed=failed,
                          action="fix the isolated environment: python3.12 tools/setup_cloud.py")
                print(f"preflight failed: {failed}; see {state.dir.relative_to(root).as_posix()}/PREFLIGHT.json")
                return 1
            state.log("preflight", "done", warnings=warned)
        plan_row = state.step("plan")
        if plan_row.get("plan"):
            plan = cloud.load_plan(root, cloud.inside(root, plan_row["plan"]))
        else:
            config = yaml.safe_load(raw.decode("utf-8"))
            if acquisition:
                from .cloud_scout import bridge_config
                config = bridge_config(root, config, acquisition)
            plan = cloud.make_plan(root, config)
            state.log("plan", "done", plan=cloud.plan_path(root, plan).relative_to(root).as_posix(),
                      selected=len(plan["targets"]), accounted=len(plan["selection"]))
        if not plan["targets"]:
            state.log("run", "blocked", action="no target selected; read SELECTION.json")
            return 1
        capsule = cloud.report_dir(root, plan)
        run = state.step("run")
        if run["state"] != "done":
            code = 1
            for attempt in range(run_attempts):
                code = cloud.run_plan(root, plan)
                failure = _last_failure(cloud.plan_path(root, plan).parent) if code else None
                kind = handback.classify_failure(" ".join(str(failure.get(k) or "") for k in ("reason", "error"))
                                                 if failure else None)
                state.log("run", "running" if code else "done", attempts=run["attempts"] + 1, exit=code,
                          failure=kind if code else None)
                if not code or not kind["retryable"] or attempt + 1 == run_attempts:
                    break
                sleep(min(600, 30 * 4 ** attempt))
            if code:
                # A blocked or failed target is still an honest result: pack what verifies, mark the step.
                state.log("run", "partial", exit=code,
                          action="incomplete targets are reported; rerun this command to resume them")
        lock_plan = LedgerLock(cloud.plan_path(root, plan).parent / "ledger.sqlite")
        lock_plan.acquire()
        try:
            cloud.write_report(root, plan)
        finally:
            lock_plan.release()
        state.log("report", "done", capsule=capsule.relative_to(root).as_posix())
        try:
            claims = handback.pack(capsule, environment=env, harness=harness, repo=root)
        except handback.HandbackError as exc:
            state.log("pack", "blocked", error=str(exc)[-2000:], failure=handback.classify_failure(str(exc)))
            print(exc)
            return 1
        state.log("pack", "done", manifest_sha256=claims["manifest_sha256"], counts=claims["counts"])
        result = deliver_handback(root, capsule, env=env, mode=deliver)
        state.log("deliver", "done" if result["ok"] else "blocked", **result)
        if not result["ok"]:
            print(json.dumps(result, indent=2))
            return 1
        cleanup = (env == "cloud-agent") if cleanup is None else cleanup
        if cleanup:
            managed = scratch_dir(f"cloud/{plan['id']}")
            freed = sum(p.stat().st_size for p in managed.rglob("*") if p.is_file())
            shutil.rmtree(managed, ignore_errors=True)
            state.log("cleanup", "done", freed_bytes=freed, path=f"scratch:cloud/{plan['id']}")
        else:
            state.log("cleanup", "skipped", note="scratch kept (local default); public inputs are re-fetchable by product ID")
        incomplete = [cid for cid, row in claims["targets"].items() if row["status"] != "completed"]
        print(json.dumps({"cycle": name, "handback": capsule.relative_to(root).as_posix(),
                          "counts": claims["counts"], "delivery": result, "incomplete": incomplete}, indent=2))
        retry = state.step("run").get("failure") or {}
        return EXIT_RETRY if state.step("run")["state"] == "partial" and retry.get("retryable") else 0
    finally:
        lock.release()


def deliver_handback(root, capsule, *, env, mode="auto"):
    """local: ingest in place. cloud-agent: Drive under Cygnus/handbacks/ when a route exists, else the
    checkout itself (the task diff) after an in-place ingest so the agent's own test suite passes."""
    from . import storage
    root, capsule = Path(root), Path(capsule)
    large = sorted(rel for rel, p in handback._files(capsule).items()
                   if p is not None and p.stat().st_size > handback.IMPORT_MAX_BYTES)
    out = {"ok": True, "mode": mode, "large_files": large}
    if env == "cloud-agent" and mode in ("auto", "drive"):
        route = storage.resolve_route()
        if mode == "drive" and (route is None or route.kind != storage.AREA_WRITER["handbacks"]):
            return {**out, "ok": False, "error": "no rclone route to Cygnus/handbacks/: set CYGNUS_DRIVE to an "
                                                 "rclone spec (docs/STORAGE.md) or deliver by git"}
        if route is not None and route.kind == storage.AREA_WRITER["handbacks"]:
            log = []
            try:
                entry = handback.with_retries(lambda: storage.upload(
                    capsule, f"handbacks/{capsule.name}", kind="handback", producer="cygnus.tier cycle",
                    route=route, notes="cloud-agent handback; verify locally with python -m cygnus.tier"), log=log)
                out.update(mode="drive", location=entry["id"], route=route.label)
            except Exception as exc:
                return {**out, "ok": False, "mode": "drive", "error": str(exc)[-500:], "attempts": log,
                        **handback.classify_failure(str(exc))}
        else:
            out["mode"] = "git"
            if large:
                out["warning"] = ("files over the git import limit; a person must transfer them or configure a "
                                  "Drive route (CYGNUS_DRIVE)")
    receipt = handback.ingest(capsule, root, origin=f"{env} cycle ({out['mode']})")
    out["ingest"] = {"id": receipt["id"], "imported": len(receipt["imported"]),
                     "report": f"reports/{handback.report_slug(receipt['id'])}/REPORT.md"}
    return out


# --------------------------------------------------------------------------- Colab
def _fetch(route, rel, dest, names):
    """Copy named files of Cygnus/<rel> into dest through this harness's route."""
    from . import colab_sync, storage
    dest.mkdir(parents=True, exist_ok=True)
    if route.kind == "path":
        base = Path(route.join(rel))
        for name in names:
            target = dest / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(base / name, target)
        return
    listing = dest.parent / f"{dest.name}.files.txt"
    listing.write_text("\n".join(names) + "\n", encoding="utf-8")
    # --no-traverse is one Drive lookup per file: fast for a few names, very slow for a whole export
    # (observed 2026-10-25: 515 files). Larger lists let rclone list the folder once instead.
    traverse = ["--no-traverse"] if len(names) <= 50 else []
    p = colab_sync._background_run(["rclone", "copy", route.join(rel), str(dest), "--files-from-raw", str(listing),
                                    *traverse, "--ignore-times", "--transfers", "8", "--checkers", "8",
                                    "--timeout", "60s", "--retries", "1"], capture_output=True, text=True, timeout=1800)
    if p.returncode:
        raise storage.StorageError(f"rclone retrieval of Cygnus/{rel} failed: {p.stderr[-800:]}")


def colab_exports(route):
    """T2 export folders under Cygnus/colab_runs/ that this route can see, oldest export first.

    Order comes from each LOCATION.json's created_utc, not folder names; a folder without a readable
    LOCATION.json is still an unfinished export and sorts first (it will be rejected, not skipped)."""
    from . import colab_sync
    found = []
    for row in colab_sync._children(route, "colab_runs"):
        if not (row["IsDir"] and row["Name"].startswith("t2-")):
            continue
        try:
            created = colab_sync._location(route, f"colab_runs/{row['Name']}/LOCATION.json").get("created_utc") or ""
        except Exception:
            created = ""
        found.append((created, row["Name"]))
    return [name for _, name in sorted(found)]


def colab_ingest(root, run, *, route=None, local=None, sleep=time.sleep):
    """Fetch a whole Colab T2 export (except its companion ledger), verify and ingest it."""
    from . import colab_sync, storage
    from .colab import read_manifest
    root = Path(root).resolve()
    run = handback.safe_id(run)
    if local:
        source, label, origin = Path(local), None, f"local copy {Path(local).name}"
        if source.name != run:
            inbox = scratch_dir(f"handback_inbox/{run}") / run
            shutil.rmtree(inbox, ignore_errors=True)
            shutil.copytree(source, inbox)
            source = inbox
    else:
        route = route or storage.require_route(run=colab_sync._background_run)
        label, origin = route.label, f"Drive Cygnus/colab_runs/{run} via {route.label}"
        source = scratch_dir(f"handback_inbox/{run}") / run
        rel = f"colab_runs/{run}"
        log = []
        handback.with_retries(lambda: _fetch(route, rel, source, ["LOCATION.json", "MANIFEST.sha256"]),
                              sleep=sleep, log=log)
        names = [n for n in read_manifest(source / "MANIFEST.sha256") if Path(n).name not in handback.COMPANION]
        needed = [n for n in names if not (source / n).is_file()
                  or sha256_file(source / n) != read_manifest(source / "MANIFEST.sha256")[n]]
        if needed:
            handback.with_retries(lambda: _fetch(route, rel, source, needed), sleep=sleep, log=log)
    marks = root / "docs/handbacks" / run / handback.HANDBACK_FILE
    if marks.is_file() and json.loads(marks.read_text(encoding="utf-8")).get("manifest_sha256") == \
            sha256_file(source / "MANIFEST.sha256"):
        return {"id": run, "state": "unchanged"}
    receipt = handback.ingest(source, root, origin=origin, route_label=label)
    return {"id": run, "state": "ingested", "imported": len(receipt["imported"]),
            "retained_elsewhere": len(receipt["retained_elsewhere"])}


def colab_stage(root, *, route=None):
    """Put the reviewed notebook kit under Cygnus/batches/ with a read-back-verified manifest."""
    from . import storage
    root = Path(root)
    notebook = root / "notebooks/cygnus_higher_tiers_colab.ipynb"
    revision = json.loads(notebook.read_text(encoding="utf-8")).get("metadata", {}).get("cygnus", {}).get("revision")
    digest = sha256_file(notebook)
    kit_id = f"higher-tiers-{revision or digest[:12]}"
    existing = {e["id"]: e for e in storage.read_index(root / "storage/locations.jsonl")}
    if existing.get(f"batches/{kit_id}", {}).get("visible_via"):
        return {"id": kit_id, "state": "already staged", "entry": existing[f"batches/{kit_id}"]}
    kit = scratch_dir(f"colab_kits/{kit_id}")
    for src in (notebook, root / "docs/HIGHER_TIERS_COLAB.md"):
        shutil.copyfile(src, kit / src.name)
    atomic_write_json(kit / "KIT.json", {"notebook_sha256": digest, "revision": revision,
                                         "instructions": "Open in Colab (CPU), Run all; locally run "
                                                         "python -m cygnus.tier colab ingest --latest"})
    log = []
    entry = handback.with_retries(lambda: storage.upload(kit, f"batches/{kit_id}", kind="batch",
                                                         producer="cygnus.tier colab stage", route=route,
                                                         index=root / "storage/locations.jsonl"), log=log)
    return {"id": kit_id, "state": "staged", "entry": entry, "attempts": log}


# --------------------------------------------------------------------------- CLI
def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m cygnus.tier", description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=str(WORKTREE))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("contracts", help="print the tier contracts (inputs, outputs, gates, evidence)")
    c = sub.add_parser("cycle", help="preflight, plan, run, report, pack, deliver, ingest; resumable")
    c.add_argument("recipe")
    c.add_argument("--env", required=True, choices=("local", "cloud-agent"))
    c.add_argument("--name", help="cycle name (default: recipe name + digest)")
    c.add_argument("--deliver", default="auto", choices=("auto", "drive", "git"))
    c.add_argument("--acquisition", help="verified scout ACQUISITION.json for plan --acquisition")
    c.add_argument("--run-attempts", type=int, default=2)
    c.add_argument("--harness", help="free-text harness label for the handback (no host names)")
    c.add_argument("--cleanup", action=argparse.BooleanOptionalAction, default=None)
    for name in ("verify", "ingest"):
        p = sub.add_parser(name, help=f"{name} a handback directory")
        p.add_argument("directory")
    sub.add_parser("check", help="check handbacks already imported into the repository")
    s = sub.add_parser("status", help="show a cycle's step journal")
    s.add_argument("name")
    colab = sub.add_parser("colab", help="stage the notebook kit or ingest Colab T2 exports")
    csub = colab.add_subparsers(dest="colab_command", required=True)
    csub.add_parser("stage")
    ci = csub.add_parser("ingest")
    which = ci.add_mutually_exclusive_group(required=True)
    which.add_argument("--run")
    which.add_argument("--latest", action="store_true")
    which.add_argument("--all", action="store_true")
    ci.add_argument("--local", help="an already downloaded export folder (for routes that cannot see it)")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()

    if args.command == "contracts":
        print(json.dumps(handback.contracts(), indent=2))
        return 0
    if args.command == "cycle":
        return cycle(root, args.recipe, env=args.env, name=args.name, deliver=args.deliver,
                     run_attempts=max(1, args.run_attempts), cleanup=args.cleanup,
                     acquisition=args.acquisition, harness=args.harness)
    if args.command == "verify":
        found = handback.verify(Path(args.directory), repo=root)
        print(json.dumps({k: found.get(k) for k in ("id", "format", "ok", "problems", "warnings")}, indent=2))
        return 0 if found["ok"] else 1
    if args.command == "ingest":
        try:
            receipt = handback.ingest(Path(args.directory), root)
        except handback.HandbackError as exc:
            print(exc)
            return 1
        print(json.dumps({k: receipt[k] for k in ("id", "format", "manifest_sha256")} |
                         {"imported": len(receipt["imported"]), "retained_elsewhere": len(receipt["retained_elsewhere"])},
                         indent=2))
        return 0
    if args.command == "check":
        problems = handback.check_imported(root)
        print("\n".join(problems) or "all imported handbacks match their ingest receipts")
        return 1 if problems else 0
    if args.command == "status":
        state = Cycle(root, args.name)
        print(json.dumps(state.state, indent=2) if state.state else f"no cycle named {args.name}")
        return 0 if state.state else 1
    if args.colab_command == "stage":
        print(json.dumps(colab_stage(root), indent=2, default=str))
        return 0
    from . import colab_sync, storage
    route = None if args.local else storage.require_route(run=colab_sync._background_run)
    if args.local:
        runs = [args.run or Path(args.local).name]
    else:
        found = colab_exports(route)
        runs = found if args.all else [args.run] if args.run else found[-1:]
    results, failed = [], False
    for run in runs:
        try:
            results.append(colab_ingest(root, run, route=route, local=args.local))
        except Exception as exc:
            failed = True
            results.append({"id": run, "state": "rejected" if isinstance(exc, handback.HandbackError) else "error",
                            "error": str(exc)[-800:], **handback.classify_failure(str(exc))})
    print(json.dumps(results, indent=2))
    if failed and all(r.get("retryable") for r in results if r.get("state") == "error"):
        return EXIT_RETRY if any(r.get("state") == "error" for r in results) else 1
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

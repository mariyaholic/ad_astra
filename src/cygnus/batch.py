"""Batch driver: queue, claim, run and triage many known-object campaigns unattended.

One agent (or a cron job) can work a whole queue with four commands::

    python -m cygnus.batch queue tess-mono-02 --where "pl_orbper IS NULL AND tfopwg_disp IN ('PC','APC')" --top 500
    python -m cygnus.batch claim --queue campaigns/tess-mono-02/target_queue.csv --n 100 --batch b01
    python -m cygnus.batch run --batch b01 [--jobs 3]
    python -m cygnus.batch status --batch b01          # also rewritten after every campaign

It only drives the existing CLIs (``cygnus.multi new/run/report``, ``cygnus.campaign run``), so a batch
produces exactly what the one-target loop in ``docs/AGENT_RUNBOOK.md`` would. What it adds:

* **one writer per ledger**: a lock file beside the ledger. A second batch on the same ledger refuses to
  start, and a lock left by a dead process is taken over.
* **crash safety**: each campaign runs in its own process with a wall-clock timeout. Runs left ``open``
  by a killed or crashed attempt are closed as ``aborted`` (with a note) before that campaign is
  retried. Only that campaign's own scripts are touched, and only while the lock is held.
* **retries** with backoff for transient archive failures (MAST 5xx, timeouts, proxy errors).
* **resume**: the journal (``state/batches/<id>/journal.jsonl``) records every attempt. A re-run
  skips campaigns that already finished with a valid record, and the runner itself reuses completed steps.
* **triage**: ``SUMMARY.md`` separates the campaigns a reviewer must read (escalations, as defined in
  the runbook) from routine ones. Nothing is reviewed, published or committed automatically.

Batch state lives under ``state/`` (never committed). The campaign specs and ``campaigns/<id>/``
outputs are the committed record, as for single campaigns.
"""

from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from .config import WORKTREE, ledger_path

CHECK_KNOWN = "Known-signal recovery (positive control)"
CHECK_XMATCH = "Catalogue cross-match"
TRANSIENT = ("502", "503", "504", "Bad Gateway", "Service Unavailable", "timed out", "Timeout", "ReadTimeout",
             "ConnectTimeout", "ConnectionError", "Connection reset", "RemoteDisconnected", "ProxyError",
             "Temporary failure", "Max retries exceeded", "IncompleteRead", "database is locked")
_IO = threading.Lock()   # journal and summary writes from parallel workers


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _py() -> list[str]:
    return [sys.executable, "-u", "-m"]


def batch_dir(root: Path, batch: str) -> Path:
    return root / "state" / "batches" / batch


# ------------------------------------------------------------------ lock
class LedgerLock:
    """Exclusive lock for one ledger, held for the whole batch. The file records pid, host and start
    time; a lock whose pid is gone (same host) is stale and is taken over."""

    def __init__(self, ledger: Path):
        self.path = Path(str(ledger) + ".batch.lock")
        self.held = False

    @staticmethod
    def _alive(pid: int) -> bool:
        if os.name == "nt":
            out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True).stdout
            return str(pid) in out
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        return True

    def acquire(self) -> str | None:
        """Take the lock. Returns a note if a stale lock was taken over; raises SystemExit if it is held."""
        note = None
        if self.path.exists():
            try:
                info = json.loads(self.path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                info = {}
            same_host = info.get("host") == socket.gethostname()
            if same_host and info.get("pid") and not self._alive(int(info["pid"])):
                note = f"stale lock from pid {info['pid']} (started {info.get('started_utc')}) taken over"
                self.path.unlink()
            else:
                raise SystemExit(f"ledger is locked by another batch: {info or self.path} "
                                 f"(delete {self.path} only if that process is gone)")
        payload = {"pid": os.getpid(), "host": socket.gethostname(), "started_utc": now_utc()}
        fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)   # atomic: loses cleanly to a racing batch
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(payload, fh)
        self.held = True
        return note

    def release(self) -> None:
        if self.held:
            self.path.unlink(missing_ok=True)
            self.held = False


def close_orphan_runs(ledger: Path, campaign_id: str, note: str) -> list[int]:
    """Close runs still ``open`` for one campaign's steps as ``aborted``. Only call while holding the lock
    and before that campaign is (re)started: then no live process can own them."""
    from .ledger import Ledger

    led = Ledger(ledger)
    try:
        ids = [int(r["id"]) for r in led.db.execute(
            "SELECT id FROM runs WHERE status='open' AND (script LIKE ? OR script LIKE ?) ORDER BY id",
            (f"cygnus_multi:{campaign_id}:%", f"cygnus.campaign:{campaign_id}:%"))]
        for i in ids:
            led.close_run(i, "aborted", f"closed retrospectively {now_utc()}: {note}")
        return ids
    finally:
        led.close()


# ------------------------------------------------------------------ journal
def read_journal(bdir: Path) -> list[dict]:
    p = bdir / "journal.jsonl"
    if not p.is_file():
        return []
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def append_journal(bdir: Path, entry: dict) -> None:
    bdir.mkdir(parents=True, exist_ok=True)
    with _IO, (bdir / "journal.jsonl").open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(entry, sort_keys=True) + "\n")


def batch_specs(bdir: Path) -> list[str]:
    p = bdir / "specs.txt"
    return [s for s in p.read_text(encoding="utf-8").splitlines() if s.strip()] if p.is_file() else []


# ------------------------------------------------------------------ triage
def triage(root: Path, spec: str) -> dict:
    """What a reviewer needs to know about one finished campaign, read from its sky record."""
    cid = Path(spec).stem
    rec_p = root / "campaigns" / cid / "sky_record.json"
    if not rec_p.is_file():
        return {"campaign": cid, "record": False, "escalate": ["no sky record"]}
    rec = json.loads(rec_p.read_text(encoding="utf-8"))
    checks = {c["name"]: c for c in rec.get("checks", [])}
    known = (checks.get(CHECK_KNOWN) or {}).get("state")
    xm = checks.get(CHECK_XMATCH) or {}
    why = []
    if rec.get("outcome") == "lead":
        why.append("repeat candidate: outcome lead (Unverified lead); run `vet` and log it in the lead vetting log")
    if known == "failed":
        why.append("positive control failed on data covering the epoch")
    if xm.get("state") == "inconclusive" and "; 0 answered" in (xm.get("note") or ""):
        why.append("every catalogue service errored")
    if rec.get("status") != "completed":
        why.append(f"record status {rec.get('status')}")
    return {"campaign": cid, "record": True, "status": rec.get("status"), "outcome": rec.get("outcome"),
            "evidence": rec.get("evidence"), "known_signal": known, "cross_match": xm.get("state"),
            "escalate": why}


def write_summary(root: Path, batch: str) -> Path:
    bdir = batch_dir(root, batch)
    specs = batch_specs(bdir)
    last: dict[str, dict] = {}
    attempts: dict[str, int] = {}
    for e in read_journal(bdir):
        if e.get("event") == "attempt":
            last[e["spec"]] = e
            attempts[e["spec"]] = attempts.get(e["spec"], 0) + 1
    rows, esc, failed, pending = [], [], [], []
    for s in specs:
        e = last.get(s)
        if e is None:
            pending.append(s)
            continue
        if e["result"] != "ok":
            failed.append((s, e))
            continue
        t = e.get("triage") or triage(root, s)
        rows.append((s, t))
        if t["escalate"]:
            esc.append((s, t))
    lines = [f"# Batch {batch}", "", f"Updated {now_utc()}. Specs: {len(specs)}; finished: {len(rows)}; "
             f"failed: {len(failed)}; not yet run: {len(pending)}; to review first: {len(esc)}.", "",
             "Nothing here is reviewed. Every finished campaign still needs the review in "
             "`docs/AGENT_RUNBOOK.md` before its draft marker is removed; start with the escalations.", ""]
    if esc:
        lines += ["## Escalations (review these first)", "", "| Campaign | Why |", "|---|---|"]
        lines += [f"| `{s}` | {'; '.join(t['escalate'])} |" for s, t in esc] + [""]
    if failed:
        lines += ["## Failed after retries (do not patch code; report the error)", "",
                  "| Campaign | Attempts | Last error |", "|---|---|---|"]
        lines += [f"| `{s}` | {attempts.get(s, 0)} | {(e.get('error') or '').replace('|', '/')[:200]} |" for s, e in failed] + [""]
    if rows:
        lines += ["## Finished", "", "| Campaign | Status | Outcome | Positive control | Cross-match |", "|---|---|---|---|---|"]
        lines += [f"| `{s}` | {t.get('status')} | {t.get('outcome')} | {t.get('known_signal')} | {t.get('cross_match')} |"
                  for s, t in rows] + [""]
    if pending:
        lines += ["## Not yet run", ""] + [f"- `{s}`" for s in pending] + [""]
    p = bdir / "SUMMARY.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    with _IO:
        p.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return p


# ------------------------------------------------------------------ commands
def cmd_queue(a, root: Path) -> int:
    """Write campaigns/<id>.yaml holding only a target_queue step, and run it."""
    spec = root / "campaigns" / f"{a.id}.yaml"
    if spec.exists():
        raise SystemExit(f"{spec.relative_to(root).as_posix()} exists; pick a new queue id")
    where = a.where.replace('"', '\\"')
    spec.write_text(
        f"# CYGNUS target queue {a.id}: built by `python -m cygnus.batch queue` on {now_utc()[:10]}.\n"
        f"# Work it with `python -m cygnus.batch claim --queue campaigns/{a.id}/target_queue.csv`.\n"
        f"schema: cygnus.campaign/1\ncampaign_id: {a.id}\ndomain: {a.domain}\nstatus: draft\n"
        f"objective: >\n  Target queue only: {a.objective}\noutputs: campaigns/{a.id}/\nrandom_seed: {a.seed}\n\n"
        f"veto:\n  kind: single_epoch\n  veto_hours: 12\n\nsteps:\n  - target_queue:\n"
        f"      source: nasa_exoplanet_archive.toi\n      where: \"{where}\"\n      top: {a.top}\n\n"
        f"# A queue is a draft record: it ranks targets and analyses nothing. Its targets are run as\n"
        f"# their own known-object campaigns (python -m cygnus.batch claim / run).\n"
        f"record:\n  path: campaigns/{a.id}/sky_record.json\n  title: Target queue {a.id}\n  kind: target queue\n"
        f"  status: draft\n  queue_targets_in_record: 10\n  summary: >\n"
        f"    Ranked target queue from the NASA Exoplanet Archive TOI table ({a.where.replace(chr(10), ' ')}; top {a.top}).\n"
        f"    No light curve is analysed here; each target becomes its own known-object campaign.\n",
        encoding="utf-8", newline="\n")
    r = subprocess.run(_py() + ["cygnus.campaign", "run", str(spec)], cwd=root)
    print(f"campaigns/{a.id}/target_queue.csv" if r.returncode == 0 else f"queue run failed ({r.returncode})")
    return r.returncode


def cmd_claim(a, root: Path) -> int:
    """Claim the next N unclaimed queue rows (write their specs) and add them to the batch."""
    from .multi import scaffold

    qpath = Path(a.queue) if Path(a.queue).is_absolute() else root / a.queue
    try:   # specs record the queue path; keep it repository-relative (no private paths in committed files)
        qarg = qpath.resolve().relative_to(Path(root).resolve()).as_posix()
    except ValueError:
        raise SystemExit(f"queue {a.queue} is outside the worktree; copy it into campaigns/ first")
    rows = scaffold.read_queue(qpath)
    taken = {p.stem for p in (root / "campaigns").glob("*.yaml")}
    bdir = batch_dir(root, a.batch)
    specs = batch_specs(bdir)
    made, skipped = [], []
    for row in rows:
        if len(made) >= a.n:
            break
        slug = scaffold.slug_for(row["name"])
        if slug in taken:
            continue
        cmd = _py() + ["cygnus.multi", "new", "--from-queue", row["name"], "--queue", qarg, "--seed", str(a.seed)]
        if a.archives:
            cmd += ["--archives", a.archives]
        r = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
        if r.returncode == 0:
            made.append(r.stdout.strip().splitlines()[-1])
            taken.add(slug)
        else:   # e.g. no catalogued epoch: record it and move on, never stall the queue on one row
            skipped.append((row["name"], (r.stderr or r.stdout).strip().splitlines()[-1:] or ["?"]))
    bdir.mkdir(parents=True, exist_ok=True)
    (bdir / "specs.txt").write_text("\n".join(specs + [m for m in made if m not in specs]) + "\n",
                                    encoding="utf-8", newline="\n")
    for name, why in skipped:
        append_journal(bdir, {"event": "claim_skipped", "target": name, "reason": why[0], "utc": now_utc()})
    print(json.dumps({"batch": a.batch, "claimed": made, "skipped": skipped}, indent=1))
    if made:
        print("\nCommit the claims before running (other agents see them on pull):\n"
              f"  git add {' '.join(made)} && git commit -m \"Claim {len(made)} targets (batch {a.batch})\" && git push")
    return 0


def run_one(root: Path, ledger: Path, bdir: Path, spec: str, *, retries: int, timeout_s: int, report: bool) -> dict:
    cid = Path(spec).stem
    logs = bdir / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "CYGNUS_LEDGER": str(ledger)}
    entry: dict = {}
    for attempt in range(1, retries + 2):
        closed = close_orphan_runs(ledger, cid, f"left open by an interrupted attempt; batch {bdir.name} retries {cid}")
        t0 = time.time()
        log = logs / f"{cid}.attempt{attempt}.log"
        try:
            with log.open("w", encoding="utf-8") as fh:
                r = subprocess.run(_py() + ["cygnus.multi", "run", spec], cwd=root, env=env, stdout=fh,
                                   stderr=subprocess.STDOUT, timeout=timeout_s)
            code, err = r.returncode, None
        except subprocess.TimeoutExpired:
            code, err = -1, f"timed out after {timeout_s} s"
        tail = log.read_text(encoding="utf-8", errors="replace").strip().splitlines()[-3:]
        if code != 0 and err is None:
            err = " / ".join(tail) or f"exit {code}"
        entry = {"event": "attempt", "spec": spec, "attempt": attempt, "utc": now_utc(),
                 "seconds": round(time.time() - t0, 1), "result": "ok" if code == 0 else "failed",
                 "error": err, "closed_orphans": closed, "log": log.relative_to(root).as_posix()}
        if code == 0:
            if report:
                subprocess.run(_py() + ["cygnus.multi", "report", spec], cwd=root, env=env, capture_output=True)
            entry["triage"] = triage(root, spec)
            append_journal(bdir, entry)
            return entry
        append_journal(bdir, entry)
        transient = err is not None and (err.startswith("timed out") or any(k in err for k in TRANSIENT))
        if attempt > retries or not transient:
            break
        time.sleep(min(600, 30 * 4 ** (attempt - 1)))   # 30 s, 120 s, 480 s …
    close_orphan_runs(ledger, cid, f"left open by a failed attempt; batch {bdir.name} gave up on {cid}")
    return entry


def cmd_run(a, root: Path) -> int:
    bdir = batch_dir(root, a.batch)
    if a.spec:
        specs = batch_specs(bdir)
        (bdir).mkdir(parents=True, exist_ok=True)
        (bdir / "specs.txt").write_text("\n".join(specs + [s for s in a.spec if s not in specs]) + "\n",
                                        encoding="utf-8", newline="\n")
    specs = batch_specs(bdir)
    if not specs:
        raise SystemExit(f"batch {a.batch} has no specs; claim targets or pass --spec")
    done = {e["spec"] for e in read_journal(bdir) if e.get("event") == "attempt" and e["result"] == "ok"}
    todo = [s for s in specs if a.redo or s not in done
            or not (root / "campaigns" / Path(s).stem / "sky_record.json").is_file()]
    ledger = Path(a.ledger or os.environ.get("CYGNUS_LEDGER") or ledger_path())
    lock = LedgerLock(ledger)
    note = lock.acquire()
    try:
        append_journal(bdir, {"event": "start", "utc": now_utc(), "pid": os.getpid(), "todo": len(todo),
                              "jobs": a.jobs, "lock_note": note})
        print(f"batch {a.batch}: {len(todo)} to run, {len(specs) - len(todo)} already finished"
              + (f"; {note}" if note else ""), flush=True)

        def work(s: str) -> dict:
            e = run_one(root, ledger, bdir, s, retries=a.retries, timeout_s=a.timeout, report=not a.no_report)
            print(f"[{e['result']}] {s} ({e['seconds']} s, attempt {e['attempt']})"
                  + (f": {e['error']}" if e.get("error") else ""), flush=True)
            write_summary(root, a.batch)
            return e

        with ThreadPoolExecutor(max_workers=max(1, a.jobs)) as pool:
            results = list(pool.map(work, todo))
        append_journal(bdir, {"event": "end", "utc": now_utc(), "ok": sum(r["result"] == "ok" for r in results),
                              "failed": sum(r["result"] != "ok" for r in results)})
    finally:
        lock.release()
    print(write_summary(root, a.batch).relative_to(root).as_posix())
    return 0 if all(r["result"] == "ok" for r in results) else 1


def cmd_status(a, root: Path) -> int:
    p = write_summary(root, a.batch)
    print(p.read_text(encoding="utf-8"))
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m cygnus.batch", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("queue", help="build a new ranked target queue (campaigns/<id>/target_queue.csv)")
    q.add_argument("id", help="queue campaign id, e.g. tess-mono-02")
    q.add_argument("--where", required=True, help="ADQL condition on the NASA Exoplanet Archive TOI table")
    q.add_argument("--top", type=int, default=200)
    q.add_argument("--domain", default="worlds.planetary.monotransit")
    q.add_argument("--objective", default="rank TOI-table targets for the known-object loop (docs/AGENT_RUNBOOK.md).")
    q.add_argument("--seed", type=int, default=20260927)
    c = sub.add_parser("claim", help="claim the next N unclaimed queue targets into a batch")
    c.add_argument("--queue", required=True, help="queue CSV, e.g. campaigns/tess-mono-01/target_queue.csv")
    c.add_argument("--n", type=int, default=20)
    c.add_argument("--batch", required=True)
    c.add_argument("--archives", help="extra archive adapters for fetch_products (cygnus.multi new --archives)")
    c.add_argument("--seed", type=int, default=20260927)
    r = sub.add_parser("run", help="run every unfinished campaign of a batch (resumable)")
    r.add_argument("--batch", required=True)
    r.add_argument("--spec", nargs="*", help="add these specs to the batch before running")
    r.add_argument("--jobs", type=int, default=1, help="campaigns in parallel (default 1; 2-3 is safe on one ledger)")
    r.add_argument("--retries", type=int, default=2, help="retries per campaign for transient failures")
    r.add_argument("--timeout", type=int, default=1800, help="wall-clock seconds per attempt")
    r.add_argument("--redo", action="store_true", help="re-run campaigns that already finished")
    r.add_argument("--no-report", action="store_true", help="skip drafting REPORT.md / SEARCH_LOG.md")
    r.add_argument("--ledger", help="ledger path (default: CYGNUS_LEDGER or state/ledger.sqlite)")
    s = sub.add_parser("status", help="rewrite and print the batch SUMMARY.md")
    s.add_argument("--batch", required=True)
    a = ap.parse_args(argv)
    root = WORKTREE
    return {"queue": cmd_queue, "claim": cmd_claim, "run": cmd_run, "status": cmd_status}[a.cmd](a, root)


if __name__ == "__main__":
    sys.exit(main())

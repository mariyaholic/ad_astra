"""Execute a campaign spec as ledgered, resumable steps and emit its sky record.

Contract (docs/CAMPAIGNS.md):

* the spec (``schema: cygnus.campaign/1``) is the single source of the run's parameters; steps read
  nothing that is hard-coded per campaign;
* every step runs inside ``Ledger.recorded_run`` (script ``cygnus.campaign:<id>:<step>``) and so is
  always closed completed / failed / aborted; measurements go to the ledger;
* a step whose config hash (its params, the spec's shared blocks, upstream outputs, code version)
  matches a completed run with a saved output is reused, not recomputed (``--force`` overrides);
* the sky record is regenerated from the spec's ``record`` block plus the checks and notes the
  steps produced, so it cannot drift from what ran.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from ..config import WORKTREE, scratch_dir
from ..ledger import Ledger, now_utc
from ..skyrecord import SCHEMA as RECORD_SCHEMA
from .scaffold import TOI_POSITION_EPOCH, TOI_POSITION_NOTE
from .steps import STEPS

SPEC_SCHEMA = "cygnus.campaign/1"
SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{1,62}$")


class SpecError(ValueError):
    pass


MULTI_RUNNER = "cygnus.multi"


def spec_runner(path: str | Path) -> str | None:
    """The spec's declared ``runner`` (``cygnus.multi`` for multi-archive specs), or None."""
    import yaml

    try:
        spec = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None
    return spec.get("runner") if isinstance(spec, dict) else None


def load_spec(path: str | Path) -> dict:
    import yaml

    path = Path(path)
    spec = yaml.safe_load(path.read_text(encoding="utf-8"))
    problems = []
    if not isinstance(spec, dict) or spec.get("schema") != SPEC_SCHEMA:
        raise SpecError(f"{path}: schema must be {SPEC_SCHEMA!r}")
    if spec.get("runner") not in (None, "cygnus.campaign"):
        raise SpecError(f"{path}: runner is {spec['runner']!r}; run it with `python -m {spec['runner']}` "
                        "(`python -m cygnus.campaign` hands such specs over automatically)")
    if not SLUG.match(str(spec.get("campaign_id", ""))):
        problems.append("campaign_id must be a slug")
    steps = spec.get("steps") or []
    for s in steps:
        if not (isinstance(s, dict) and len(s) == 1):
            problems.append(f"each step is a one-key mapping, got {s!r}")
            continue
        name = next(iter(s))
        if name not in STEPS:
            problems.append(f"step {name!r} is not implemented (known: {', '.join(STEPS)})")
    order = [next(iter(s)) for s in steps if isinstance(s, dict) and len(s) == 1]
    for dep in ("calibrate_screen", "residual_screen", "known_signal_recovery", "bls_recovery", "period_aliases"):
        if dep in order and "fetch_products" not in order:
            problems.append(f"{dep} needs a fetch_products step before it")
        elif dep in order and "fetch_products" in order and order.index(dep) < order.index("fetch_products"):
            problems.append(f"{dep} must come after fetch_products")
    for s in steps:
        if not (isinstance(s, dict) and len(s) == 1):
            continue
        name = next(iter(s))
        params = next(iter(s.values())) or {}
        if not isinstance(params, dict):
            continue
        if name in ("residual_screen", "known_signal_recovery"):
            k = params.get("k_mad", "calibrated" if name == "known_signal_recovery" else None)
            if str(k).lower() == "calibrated":
                if "calibrate_screen" not in order:
                    problems.append(f"{name}: k_mad 'calibrated' requires a calibrate_screen step")
                elif order.index("calibrate_screen") > order.index(name):
                    problems.append(f"{name}: calibrate_screen must come before it to provide k*")
    if "fetch_products" in order and "target_queue" in order and order.index("target_queue") > order.index("fetch_products"):
        problems.append("target_queue must come before fetch_products")
    if "outputs" not in spec:
        problems.append("outputs directory required")
    veto = spec.get("veto")
    if veto and veto.get("kind") == "ephemeris":
        for k in ("period_days", "t0_bjd", "veto_phase", "source"):
            if k not in veto:
                problems.append(f"veto.{k} required for an ephemeris veto")
    if problems:
        raise SpecError(f"{path}:\n  " + "\n  ".join(problems))
    spec["_path"] = path
    return spec


def code_fingerprint() -> str:
    """Hash of the source files that define campaign behaviour, so a code change invalidates reuse."""
    pkg = Path(__file__).resolve().parents[1]
    files = sorted((pkg / "campaign").glob("*.py")) + [pkg / "targets.py", pkg / "priorart.py"]
    h = hashlib.sha256()
    for f in files:
        h.update(f.name.encode())
        h.update(f.read_bytes().replace(b"\r\n", b"\n"))
    return h.hexdigest()[:12]


def _hash(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()[:16]


class Context:
    def __init__(self, spec: dict, ledger: Ledger, root: Path):
        self.spec, self.ledger, self.root = spec, ledger, root
        self.campaign_id = spec["campaign_id"]
        self.seed = spec.get("random_seed")
        self.outdir = (root / spec["outputs"]).resolve()
        self.outdir.mkdir(parents=True, exist_ok=True)
        self.scratch = scratch_dir(f"campaign_{self.campaign_id}")
        self._results: dict[str, dict] = {}
        self.checks: dict[str, dict] = {}
        self.notes: list[str] = []
        self.run_id: int | None = None
        self.step: str | None = None
        self.outcome: tuple[str, str] | None = None   # (outcome, evidence) raised by a step

    # results
    def result(self, step: str) -> dict:
        if step not in self._results:
            raise RuntimeError(f"step {self.step!r} needs the output of {step!r}, which has not run")
        return self._results[step]

    def optional_result(self, step: str, default):
        return self._results.get(step, default)

    # provenance
    def measure(self, name, value, *, unit=None, method=None, products=(), notes=None):
        self.ledger.add_measurement(self.run_id, name, value, unit=unit, method=method, notes=notes, product_ids=list(products))

    def ledger_has_product(self, archive: str, pid: str) -> bool:
        return self.ledger.db.execute("SELECT 1 FROM products WHERE archive=? AND product_id=?", (archive, pid)).fetchone() is not None

    def spec_step_param(self, step: str, key: str, default=None):
        for s in self.spec.get("steps", []):
            if step in s:
                return (s[step] or {}).get(key, default)
        return default

    def check(self, name: str, state: str, note: str):
        self.checks[name] = {"state": state, "note": note, "step": self.step}

    def flag_lead(self, why: str):
        """Steps may raise a record to ``lead`` but never above *Unverified lead*: vetting beyond
        the automated checks is a person's (or reviewing agent's) decision."""
        self.outcome = ("lead", "Unverified lead")
        self.note(why)

    def note(self, text: str):
        self.notes.append(text)

    # paths
    def rel(self, p: Path) -> str:
        return Path(p).resolve().relative_to(self.root.resolve()).as_posix()

    def product_dir(self, pid: str, lc=None) -> Path:
        prod = self._results["fetch_products"]["products"][pid]
        sector = prod.get("sector") or (lc.primary.get("SECTOR") if lc is not None else None)
        sub = self.outdir / (f"tic{prod['tic']}" if prod.get("tic") and prod.get("target") else "") / f"sector{int(sector):02d}"
        sub.mkdir(parents=True, exist_ok=True)
        return sub

    def targets(self) -> list[dict]:
        """Campaign targets with positions: the spec's ``targets`` (resolved via NAME_RESOLUTIONS when
        no position is given) plus the queued targets if a target_queue step ran."""
        from ..skyrecord import known_positions

        pos = known_positions(self.root)
        out = []
        for t in self.spec.get("targets", []):
            ra, dec = (t["ra_deg"], t["dec_deg"]) if "ra_deg" in t else pos.get(t["name"], (None, None))
            if ra is None:
                raise RuntimeError(f"target {t['name']!r} has no position (add ra_deg/dec_deg or a name resolution)")
            out.append({"name": t["name"], "ra_deg": ra, "dec_deg": dec})
        q = self.optional_result("target_queue", {}).get("queue", [])
        n = int(self.spec.get("record", {}).get("queue_targets_in_record", 10))
        out += [{"name": t["name"], "ra_deg": t["ra_deg"], "dec_deg": t["dec_deg"]} for t in q[:n]]
        return out


def run(spec_path: str | Path, *, ledger: Ledger, root: Path = WORKTREE, force: bool = False,
        until: str | None = None, echo=print) -> dict:
    spec = load_spec(spec_path)
    ctx = Context(spec, ledger, root)
    shared = {k: spec.get(k) for k in ("input", "veto", "targets", "random_seed")}
    upstream = ""
    source = code_fingerprint()
    state_dir = ctx.outdir / "runner"
    state_dir.mkdir(exist_ok=True)
    done = []
    for entry in spec["steps"]:
        name, params = next(iter(entry.items()))
        params = params or {}
        ctx.step = name
        cfg = _hash({"step": name, "params": params, "shared": shared, "upstream": upstream,
                     "code": ledger.code_version, "source": source})
        script = f"cygnus.campaign:{ctx.campaign_id}:{name}"
        saved = state_dir / f"{name}.json"
        prior = None if force else ledger.completed_run(script, cfg)
        if prior and saved.is_file():
            blob = json.loads(saved.read_text(encoding="utf-8"))
            ctx._results[name] = blob["result"]
            ctx.checks.update(blob.get("checks", {}))
            ctx.notes += blob.get("notes", [])
            if blob.get("outcome"):
                ctx.outcome = tuple(blob["outcome"])
            echo(f"[{name}] reused completed run #{prior['id']} (config {cfg})")
        else:
            n_checks, n_notes, n_out = dict(ctx.checks), len(ctx.notes), ctx.outcome
            with ledger.recorded_run(script, config_hash=cfg, seed=ctx.seed) as run_:
                ctx.run_id = run_.id
                echo(f"[{name}] run #{run_.id} (config {cfg}) ...")
                result = STEPS[name](ctx, params)
                ctx._results[name] = result
                new_checks = {k: v for k, v in ctx.checks.items() if n_checks.get(k) != v}
                saved.write_text(json.dumps({"step": name, "run_id": run_.id, "config_hash": cfg, "finished_utc": now_utc(),
                                             "result": result, "checks": new_checks, "notes": ctx.notes[n_notes:],
                                             "outcome": ctx.outcome if ctx.outcome != n_out else None},
                                            indent=2, default=str), encoding="utf-8")
                run_.summary = "; ".join(ctx.notes[n_notes:]) or f"{name} completed"
            echo(f"[{name}] completed")
        upstream = _hash([upstream, cfg, saved.read_bytes().hex()[:64] if saved.is_file() else ""])
        done.append(name)
        if until and name == until:
            break
    complete = len(done) == len(spec["steps"])
    record = write_record(ctx, complete)
    summary = {"campaign_id": ctx.campaign_id, "steps_run": done, "complete": complete, "checks": ctx.checks,
               "notes": ctx.notes, "record": record, "finished_utc": now_utc()}
    (state_dir / "RUN_SUMMARY.json").write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
    return summary


def write_record(ctx: Context, complete: bool) -> str | None:
    """Regenerate the campaign's sky_record.json from the spec's record block and the steps' checks."""
    rec_spec = ctx.spec.get("record")
    if not rec_spec:
        return None
    checks = []
    for c in rec_spec.get("checks", []):
        c = dict(c)
        got = ctx.checks.get(c["name"])
        if got:
            c["state"], c["note"] = got["state"], got["note"]
            c["source"] = f"campaign runner, step {got['step']}"
        c.setdefault("state", "not_tested")
        checks.append(c)
    for name, got in ctx.checks.items():   # checks produced by steps but not pre-declared
        if not any(c["name"] == name for c in checks):
            checks.append({"name": name, "state": got["state"], "note": got["note"], "source": f"campaign runner, step {got['step']}"})
    status = rec_spec.get("status") or ("completed" if complete else "draft")
    targets = []
    for t in ctx.spec.get("targets", []):
        targets.append({"name": t["name"], "position_source": "NAME_RESOLUTIONS"} if "ra_deg" not in t else
                       {k: t[k] for k in ("name", "ra_deg", "dec_deg", "frame", "epoch", "position_source")})
    n = int(rec_spec.get("queue_targets_in_record", 10))
    for t in ctx.optional_result("target_queue", {}).get("queue", [])[:n]:
        targets.append({"name": t["name"], "ra_deg": t["ra_deg"], "dec_deg": t["dec_deg"], "frame": "ICRS",
                        "epoch": TOI_POSITION_EPOCH,
                        "position_source": f"NASA Exoplanet Archive TOI table ({TOI_POSITION_NOTE})"})
    products = [{"id": pid, "archive": "MAST", "sha256": p["sha256"]}
                for pid, p in ctx.optional_result("fetch_products", {}).get("products", {}).items()]
    summary = rec_spec["summary"].strip()
    if ctx.notes and rec_spec.get("append_runner_notes", True):
        summary += " Runner: " + " ".join(ctx.notes)
    outcome, evidence = rec_spec.get("outcome", "not_run"), rec_spec.get("evidence")
    if ctx.outcome and outcome not in ("lead", "candidate"):
        outcome, evidence = ctx.outcome
    rec = {"schema": RECORD_SCHEMA, "id": ctx.campaign_id, "title": rec_spec["title"], "kind": rec_spec["kind"],
           "status": status, "outcome": outcome if status != "draft" else "not_run",
           "evidence": evidence if status != "draft" else None,
           "date": (rec_spec.get("date") or now_utc()[:10]) if status != "draft" else None,
           "summary": summary, "spec": ctx.rel(ctx.spec["_path"]), "report": rec_spec.get("report"),
           "search_log": rec_spec.get("search_log"), "targets": targets, "products": products, "checks": checks,
           "generated_by": "cygnus.campaign runner", "generated_utc": now_utc()}
    if rec_spec.get("plots"):
        rec["plots"] = rec_spec["plots"]
    path = ctx.root / rec_spec.get("path", ctx.rel(ctx.outdir / "sky_record.json"))
    path.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    return ctx.rel(path)

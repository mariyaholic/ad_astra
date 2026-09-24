"""Sky records: the machine-readable summary every analysis leaves for the sky explorer and the site.

A sky record is a small JSON file named ``sky_record.json`` placed in an analysis output directory
(``campaigns/<id>/`` or ``reports/<id>/``). It says *what was looked at, where, with which products,
what came out, and which checks were run* — nothing that is not already in the report it points to.

The explorer build (``design-system/mockups/build_explorer.py``) and, later, the public site collect
every record found by :func:`find_records`; no code change is needed to show a new analysis.
:func:`coverage_gaps` is what keeps this true: the test suite fails when a campaign spec or report
exists without a record that references it.

Schema ``cygnus.sky_record/1`` (see docs/SKY_RECORDS.md for the prose version)::

    id            slug, unique across records
    title         short human title
    kind          free text, e.g. "known-planet recovery", "residual screen", "monotransit search"
    status        draft | running | completed | abandoned
    outcome       not_run | pipeline_check | bounded_null | lead | candidate
    evidence      null or one AGENTS.md evidence level (only with outcome lead/candidate)
    date          YYYY-MM-DD of the run (null for drafts)
    summary       one or two sentences, copied or condensed from the report's bottom line
    spec, report, search_log     repository-relative paths (null where not applicable)
    targets       [{name, ra_deg?, dec_deg?, frame?, epoch?, position_source}]
    products      [{id, archive, sha256?}]
    footprints    optional [{shape: circle|box, ra, dec, r | w,h (deg), what}]
    checks        [{name, state: passed|failed|inconclusive|not_tested, reported_as?, note?}]
    plots         optional [{type: timeseries|fold, file, time_col, flux_col, quality_col?,
                             time_offset_bjd?, period_days?, t0_bjd?, window_hours?, veto_phase?,
                             depth_window_hours?, label}]
"""

from __future__ import annotations

import json
import re
from pathlib import Path

SCHEMA = "cygnus.sky_record/1"
FILENAME = "sky_record.json"
STATUSES = ("draft", "running", "completed", "abandoned")
OUTCOMES = ("not_run", "pipeline_check", "bounded_null", "lead", "candidate")
EVIDENCE = ("Unverified lead", "Vetted candidate", "Independently supported candidate", "Established object/phenomenon")
CHECK_STATES = ("passed", "failed", "inconclusive", "not_tested")
PLOT_TYPES = ("timeseries", "fold")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,62}$")
SEARCH_DIRS = ("campaigns", "reports")


def find_records(root: Path) -> list[Path]:
    """Every sky_record.json under campaigns/ and reports/, sorted for stable output."""
    out: list[Path] = []
    for d in SEARCH_DIRS:
        base = root / d
        if base.is_dir():
            out.extend(p for p in base.rglob(FILENAME) if "__pycache__" not in p.parts)
    return sorted(out)


def load_records(root: Path) -> list[dict]:
    recs = []
    for p in find_records(root):
        rec = json.loads(p.read_text(encoding="utf-8"))
        rec["_path"] = p.relative_to(root).as_posix()
        recs.append(rec)
    return recs


def _is_num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def validate(rec: dict, root: Path, known_positions: dict[str, tuple[float, float]] | None = None) -> list[str]:
    """Return a list of problems; an empty list means the record is usable."""
    e: list[str] = []
    where = rec.get("_path", rec.get("id", "?"))
    known_positions = known_positions or {}
    if rec.get("schema") != SCHEMA:
        e.append(f"{where}: schema must be {SCHEMA!r}")
    if not isinstance(rec.get("id"), str) or not SLUG_RE.match(rec["id"]):
        e.append(f"{where}: id must match {SLUG_RE.pattern}")
    for k in ("title", "kind", "summary"):
        if not isinstance(rec.get(k), str) or not rec[k].strip():
            e.append(f"{where}: {k} is required")
    status, outcome = rec.get("status"), rec.get("outcome")
    if status not in STATUSES:
        e.append(f"{where}: status must be one of {STATUSES}")
    if outcome not in OUTCOMES:
        e.append(f"{where}: outcome must be one of {OUTCOMES}")
    if status == "draft" and outcome != "not_run":
        e.append(f"{where}: a draft cannot have an outcome other than not_run")
    if status == "completed" and outcome == "not_run":
        e.append(f"{where}: a completed record needs an outcome")
    ev = rec.get("evidence")
    if ev is not None and ev not in EVIDENCE:
        e.append(f"{where}: evidence must be null or one of {EVIDENCE}")
    if outcome in ("lead", "candidate") and ev is None:
        e.append(f"{where}: outcome {outcome} requires an evidence level")
    if outcome not in ("lead", "candidate") and ev is not None:
        e.append(f"{where}: evidence level set but outcome is {outcome}")
    if status != "draft" and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(rec.get("date"))):
        e.append(f"{where}: date YYYY-MM-DD required once a run has started")
    for k in ("spec", "report", "search_log"):
        v = rec.get(k)
        if v is not None and not (root / v).is_file():
            e.append(f"{where}: {k} path does not exist: {v}")
    if status == "completed" and not rec.get("report"):
        e.append(f"{where}: completed records must point to a report")

    targets = rec.get("targets")
    if not isinstance(targets, list):
        e.append(f"{where}: targets must be a list")
        targets = []
    if status != "draft" and not targets:
        e.append(f"{where}: targets may only be empty for drafts")
    for t in targets:
        name = t.get("name")
        if not name:
            e.append(f"{where}: every target needs a name")
            continue
        has_pos = _is_num(t.get("ra_deg")) and _is_num(t.get("dec_deg"))
        if has_pos:
            if not (0 <= t["ra_deg"] < 360 and -90 <= t["dec_deg"] <= 90):
                e.append(f"{where}: {name}: position out of range")
            for k in ("frame", "epoch", "position_source"):
                if not t.get(k):
                    e.append(f"{where}: {name}: explicit positions need {k}")
        elif name not in known_positions:
            e.append(f"{where}: {name}: no position given and not in NAME_RESOLUTIONS.json")

    for p in rec.get("products", []):
        if not p.get("id") or not p.get("archive"):
            e.append(f"{where}: products need id and archive")
    for f in rec.get("footprints", []) or []:
        if f.get("shape") == "circle":
            ok = all(_is_num(f.get(k)) for k in ("ra", "dec", "r"))
        elif f.get("shape") == "box":
            ok = all(_is_num(f.get(k)) for k in ("ra", "dec", "w", "h"))
        else:
            ok = False
        if not ok:
            e.append(f"{where}: footprint needs shape circle(ra,dec,r) or box(ra,dec,w,h)")
    checks = rec.get("checks", [])
    if status == "completed" and not checks:
        e.append(f"{where}: completed records must list their checks, including those not tested")
    for c in checks:
        if not c.get("name"):
            e.append(f"{where}: every check needs a name")
        if c.get("state") not in CHECK_STATES:
            e.append(f"{where}: check {c.get('name')!r}: state must be one of {CHECK_STATES}")
    for pl in rec.get("plots", []) or []:
        if pl.get("type") not in PLOT_TYPES:
            e.append(f"{where}: plot type must be one of {PLOT_TYPES}")
        if not pl.get("file") or not (root / pl["file"]).is_file():
            e.append(f"{where}: plot file missing: {pl.get('file')}")
        for k in ("time_col", "flux_col", "label"):
            if not pl.get(k):
                e.append(f"{where}: plot needs {k}")
        if pl.get("type") == "fold" and not (_is_num(pl.get("period_days")) and _is_num(pl.get("t0_bjd"))):
            e.append(f"{where}: fold plots need period_days and t0_bjd")
    return e


def referenced_paths(rec: dict) -> set[str]:
    """Repository paths a record accounts for: its spec, report, search log, plot files and its own directory."""
    out = {rec[k] for k in ("spec", "report", "search_log") if rec.get(k)}
    out |= {p["file"] for p in rec.get("plots", []) or [] if p.get("file")}
    if rec.get("_path"):
        out.add(str(Path(rec["_path"]).parent.as_posix()))
    return out


def coverage_gaps(root: Path, recs: list[dict]) -> list[str]:
    """Campaign specs and report directories that no sky record accounts for."""
    refs: set[str] = set()
    for r in recs:
        refs |= referenced_paths(r)
    ref_dirs = {str(Path(p).parent.as_posix()) for p in refs} | refs
    gaps = []
    for spec in sorted((root / "campaigns").glob("*.yaml")):
        rel = spec.relative_to(root).as_posix()
        if rel not in refs:
            gaps.append(f"campaign spec without a sky record: {rel}")
    for base in SEARCH_DIRS:
        for rep in sorted((root / base).glob("*/REPORT.md")):
            d = rep.parent.relative_to(root).as_posix()
            if d not in ref_dirs:
                gaps.append(f"report without a sky record: {d}/REPORT.md")
    ids = [r.get("id") for r in recs]
    gaps += [f"duplicate sky record id: {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    return gaps


def known_positions(root: Path) -> dict[str, tuple[float, float]]:
    f = root / "docs" / "tier1_pack" / "NAME_RESOLUTIONS.json"
    if not f.is_file():
        return {}
    res = json.loads(f.read_text(encoding="utf-8"))
    return {k: (v["ra_deg"], v["dec_deg"]) for k, v in res.items() if v.get("ok")}


# ------------------------------------------------------------------ plot data (stdlib only)
def _median(v: list[float]) -> float:
    s = sorted(v)
    n = len(s)
    if not n:
        raise ValueError("median of empty sequence")
    return s[n // 2] if n % 2 else 0.5 * (s[n // 2 - 1] + s[n // 2])


def _bins(x: list[float], y: list[float], width: float, min_n: int = 3) -> list[tuple[float, float]]:
    groups: dict[int, tuple[list[float], list[float]]] = {}
    for a, b in zip(x, y):
        k = int((a - x[0]) // width) if x else 0
        gx, gy = groups.setdefault(k, ([], []))
        gx.append(a)
        gy.append(b)
    return [(_median(gx), _median(gy)) for _, (gx, gy) in sorted(groups.items()) if len(gx) >= min_n]


def read_series(root: Path, plot: dict) -> tuple[list[float], list[float]]:
    """Time (as stored) and median-normalised flux of good cadences, exactly as the record declares them."""
    import csv
    import math

    t, f = [], []
    with (root / plot["file"]).open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            try:
                tv, fv = float(row[plot["time_col"]]), float(row[plot["flux_col"]])
                q = float(row[plot["quality_col"]]) if plot.get("quality_col") else 0.0
            except (KeyError, ValueError):
                continue
            if q == 0 and math.isfinite(tv) and math.isfinite(fv) and fv > 0:
                t.append(tv)
                f.append(fv)
    if not f:
        raise ValueError(f"no usable rows in {plot['file']}")
    m = _median(f)
    order = sorted(range(len(t)), key=t.__getitem__)
    return [t[i] for i in order], [f[i] / m for i in order]


def plot_data(root: Path, plot: dict) -> dict:
    """Numbers for one declared plot. Depth, when requested, is computed here and labelled as such."""
    t, f = read_series(root, plot)
    out: dict = {"type": plot["type"], "label": plot["label"], "file": plot["file"], "n": len(t),
                 "time_col": plot["time_col"], "flux_col": plot["flux_col"]}
    if plot["type"] == "timeseries":
        out["bins"] = _bins(t, f, 30 / 1440)
        out["t_range"] = (t[0], t[-1])
        out["time_offset_bjd"] = plot.get("time_offset_bjd")
        return out
    P, t0, off = plot["period_days"], plot["t0_bjd"], plot.get("time_offset_bjd", 0.0)
    win = plot.get("window_hours", 4.0)
    phase = [((ti + off - t0) / P + 0.5) % 1.0 - 0.5 for ti in t]
    hours = [p * P * 24 for p in phase]
    sel = [(h, fi) for h, fi in zip(hours, f) if abs(h) <= win]
    sel.sort()
    out.update(period_days=P, t0_bjd=t0, window_hours=win, veto_phase=plot.get("veto_phase"),
               raw=sel, bins=_bins([a for a, _ in sel], [b for _, b in sel], 0.1))
    dw = plot.get("depth_window_hours")
    if dw:
        inside = [fi for h, fi in zip(hours, f) if abs(h) < dw]
        outside = [fi for p, fi in zip(phase, f) if abs(p) > 0.15]
        if inside and outside:
            out["depth"] = {"value": 1 - _median(inside) / _median(outside), "n_in": len(inside),
                            "method": f"1 − median(flux within ±{dw} h of mid-transit) / median(flux beyond ±0.15 phase); "
                                      "computed when the explorer is built, not a reported result"}
    return out


def collect(root: Path) -> dict:
    """Everything the explorer needs from sky records: records with plot data, grouped by target name."""
    positions = known_positions(root)
    recs = load_records(root)
    problems = [p for r in recs for p in validate(r, root, positions)]
    if problems:
        raise ValueError("invalid sky records:\n" + "\n".join(problems))
    by_target: dict[str, list[dict]] = {}
    extra_positions: dict[str, dict] = {}
    unplaced: list[dict] = []
    for r in recs:
        r = dict(r)
        r["plot_data"] = [plot_data(root, p) for p in r.get("plots", []) or []]
        if not r["targets"]:
            unplaced.append(r)
        for t in r["targets"]:
            by_target.setdefault(t["name"], []).append(r)
            if t["name"] not in positions and "ra_deg" in t:
                extra_positions[t["name"]] = {k: t[k] for k in ("ra_deg", "dec_deg", "frame", "epoch", "position_source")}
    return {"by_target": by_target, "extra_positions": extra_positions, "unplaced": unplaced, "records": recs}

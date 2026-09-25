"""Per-target campaigns for known objects in a target queue, and drafts of their reports.

``new``    writes ``campaigns/<slug>.yaml`` for one queued target (a known-object test: fetch its
           SPOC light curves, calibrate the screen, check the catalogued transit is recovered,
           screen for further dips, cross-match catalogues).
``report`` drafts ``REPORT.md`` and ``SEARCH_LOG.md`` from the runner's saved outputs. Every number
           in them is copied from those outputs; nothing is inferred. The drafts say they are
           drafts until an agent or person reviews them and removes the marker.
``queue``  shows which queued targets have a campaign and how far each got, so several agents
           can split a queue without colliding.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from cygnus.ledger import now_utc

DRAFT_MARKER = "<!-- cygnus:generated-draft -->"
CHECK_KNOWN = "Known-signal recovery (positive control)"


def slug_for(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def read_queue(path: Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _f(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


EXO_TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"


def target_from_row(row: dict, source: str) -> dict:
    """Normalise a target-queue row (``targets.build_queue`` columns)."""
    t0 = _f(row.get("t0_bjd"))
    if t0 is None:
        raise SystemExit(f"{row['name']}: no t0_bjd; a known-object test needs the catalogued epoch")
    return {"name": row["name"], "tic": int(float(row["tic"])), "ra_deg": _f(row["ra_deg"]), "dec_deg": _f(row["dec_deg"]),
            "t0_bjd": t0, "depth_ppm": _f(row.get("depth_ppm")), "duration_h": _f(row.get("duration_h")),
            "period_days": _f(row.get("period_days")), "tmag": _f(row.get("tmag")), "position_source": source,
            "catalogue_row_updated": row.get("toi_rowupdate") or row.get("rowupdate") or "",
            "disposition": row.get("disposition") or ""}


TOI_POSITION_EPOCH = "J2015.5"
TOI_POSITION_NOTE = "Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01"


def position_epoch(t: dict) -> str:
    """Epoch label for a target position. TOI-table positions are at the Gaia DR2 epoch J2015.5
    (reports/position-epoch-audit-01: TOI minus Gaia DR3 equals -0.5 yr x proper motion). Other
    sources have not been audited, so an explicit ``epoch`` is used if given, else "unverified"."""
    if t.get("epoch"):
        return str(t["epoch"])
    if "TOI table" in str(t.get("position_source", "")):
        return TOI_POSITION_EPOCH
    return "unverified"


def lookup_planet(name: str, fetch=None) -> dict:
    """A known planet from the NASA Exoplanet Archive composite table (``pscomppars``)."""
    import io

    safe = name.lower().replace("'", "")
    adql = ("SELECT pl_name, hostname, tic_id, ra, dec, pl_orbper, pl_tranmid, pl_trandep, pl_trandur, sy_tmag, rowupdate "
            f"FROM pscomppars WHERE lower(pl_name) = '{safe}'")
    if fetch is None:
        import requests

        r = requests.post(EXO_TAP, data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": adql},
                          headers={"User-Agent": "cygnus-campaign/0.1"}, timeout=120)
        r.raise_for_status()
        rows = list(csv.DictReader(io.StringIO(r.text)))
    else:
        rows = fetch(adql)
    if not rows:
        raise SystemExit(f"{name!r} not found in pscomppars (use the archive's pl_name, e.g. 'WASP-12 b')")
    r = rows[0]
    tic = re.sub(r"\D", "", r.get("tic_id") or "")
    if not tic or _f(r.get("pl_tranmid")) is None:
        raise SystemExit(f"{name}: archive row lacks a TIC id or transit midtime; use --tic/--t0 by hand")
    dep = _f(r.get("pl_trandep"))
    return {"name": r["pl_name"], "tic": int(tic), "ra_deg": _f(r["ra"]), "dec_deg": _f(r["dec"]),
            "t0_bjd": _f(r["pl_tranmid"]), "period_days": _f(r.get("pl_orbper")),
            "depth_ppm": dep * 1e4 if dep is not None else None,          # pscomppars pl_trandep is in per cent
            "duration_h": _f(r.get("pl_trandur")), "tmag": _f(r.get("sy_tmag")),
            "position_source": "NASA Exoplanet Archive pscomppars", "catalogue_row_updated": r.get("rowupdate") or "",
            "disposition": "confirmed planet", "query": adql}


def spec_for(t: dict, *, parent: str | None, origin: str, seed: int, archives: str | None = None) -> str:
    """YAML text of a known-object campaign for one normalised target. Periodic targets get an
    ephemeris veto (every predicted transit in the data is a positive control); single transits a
    ±12 h veto about the catalogued epoch.

    ``archives`` is an optional comma-separated adapter list. When given, the
    generated ``fetch_products`` step discovers from those archives; when absent
    it keeps the original MAST SPOC path so existing specs are unchanged.
    """
    slug = slug_for(t["name"])
    out = f"campaigns/{slug}/"
    periodic = bool(t.get("period_days"))
    dur = t.get("duration_h") or 2.0
    if periodic:
        vp = max(0.02, round(1.5 * dur / 24 / t["period_days"], 4))
        veto = "\n".join(["veto:", "  kind: ephemeris", f"  period_days: {t['period_days']}", f"  t0_bjd: {t['t0_bjd']}",
                          f"  veto_phase: {vp}", f"  depth_ppm: {t.get('depth_ppm')}", f"  duration_h: {t.get('duration_h')}",
                          f"  source: {origin}"])
        what = "every catalogued transit in its retrieved light curves"
    else:
        veto = "veto:\n  kind: single_epoch\n  veto_hours: 12"
        what = "the catalogued single transit in its retrieved light curve"
    disp = f", {t['disposition']}" if t.get("disposition") else ""
    domain = "transit" if periodic else "monotransit"
    if archives:
        arch_list = [x.strip() for x in archives.split(",") if x.strip()]
        fetch = ("  - fetch_products:\n"
                 f"      from_targets:\n        archives: [{', '.join(arch_list)}]\n"
                 "        max_products_per_target: 6")
        arch_comment = f"# Archives: {', '.join(arch_list)} (via cygnus.multi.archives).\n"
        fetch += "\n  - context_products: {}\n  - source_checks: {}"
        if "gaia" in arch_list:
            fetch += "\n  - astrometric_vetting: {}"
    else:
        fetch = "  - fetch_products:\n      from_targets: {max_products_per_target: 6}"
        arch_comment = ""
    return _yaml_nulls(f"""# CYGNUS known-object test for {t['name']}, generated {now_utc()[:10]} by `python -m cygnus.multi new`.
{arch_comment}# Target values are copied from: {origin}. Run with
#   python -m cygnus.multi run {out.rstrip('/')}.yaml
#   python -m cygnus.multi report {out.rstrip('/')}.yaml
schema: cygnus.campaign/1
runner: cygnus.multi
campaign_id: {slug}
parent: {parent or 'none'}
domain: worlds.planetary.{domain}
objective: >
  Known-object test on {t['name']} (TIC {t['tic']}{disp}): check that the calibrated residual screen
  recovers {what}, measure the depth, then screen the same light curves for further transit-like
  dips outside the catalogued transits. A further dip is an unverified lead until vetted; it does
  not imply a period.
outputs: {out}
random_seed: {seed}

targets:
  - name: {t['name']}
    tic: {t['tic']}
    ra_deg: {t['ra_deg']}
    dec_deg: {t['dec_deg']}
    frame: ICRS
    epoch: {position_epoch(t)}
    position_source: {t['position_source']}
    t0_bjd: {t['t0_bjd']}
    period_days: {t.get('period_days')}
    depth_ppm: {t.get('depth_ppm')}
    duration_h: {t.get('duration_h')}
    tmag: {t.get('tmag')}
    catalogue_row_updated: "{t.get('catalogue_row_updated', '')}"

# Catalogued transits are excluded from the search for further dips and are the positive control.
{veto}

steps:
{fetch}
  - calibrate_screen:
      declared_k: 5.0
      window_days: 2.0
      k_grid: [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0, 10.0, 12.0]
      max_null_events: 0
      depths_ppm: [500, 1000, 2000, 5000, 10000, 20000]
      durations_h: [1.0, 2.0, 4.0, 8.0]
      injections_per_cell: 10
      reference_signal: {{depth_ppm: 2000, duration_h: 4.0}}
  - known_signal_recovery:
      k_mad: calibrated
      epoch_tolerance_hours: 2.0
  - residual_screen:
      windows_days: [1.0, 2.0, 3.0]
      k_mad: calibrated
      min_cadences: 2
      series_window_days: 2.0
  - period_aliases:
      depth_ratio: [0.5, 2.0]
      min_period_days: 1.0
      min_coverage: 0.5
      excluded_below: 0.3
  - prior_art:
      radius_arcsec: 30

record:
  path: {out}sky_record.json
  title: Known-object test, {t['name']}
  kind: known-object test
  outcome: pipeline_check
  report: {out}REPORT.md
  search_log: {out}SEARCH_LOG.md
  summary: >
    Known-object test on {t['name']}: positive control on the catalogued transit(s), calibrated
    screen for further dips, catalogue cross-match.
  checks:
    - {{name: "Product integrity (SHA-256)", state: not_tested}}
    - {{name: "{CHECK_KNOWN}", state: not_tested}}
    - {{name: "Calibrated false-alarm threshold (sign-flip null)", state: not_tested}}
    - {{name: "Synthetic signal injection–recovery", state: not_tested}}
    - {{name: "Catalogue cross-match", state: not_tested}}
    - {{name: "Period aliases (repeat events)", state: not_tested}}
    - {{name: "Alternative detrending", state: not_tested}}
    - {{name: "Difference-image centroids / blend audit", state: not_tested}}
    - {{name: "Pointing / jitter correlation", state: not_tested}}
    - {{name: "Literature (ADS) audit", state: not_tested}}
""")


def _yaml_nulls(text: str) -> str:
    """Python ``None`` interpolated into YAML would read back as the string 'None'."""
    return re.sub(r": None$", ": null", text, flags=re.M)


def write_spec(root: Path, t: dict, *, parent: str | None, origin: str, seed: int,
               archives: str | None = None) -> Path:
    path = root / "campaigns" / f"{slug_for(t['name'])}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"campaigns/{path.name} already exists (claimed); pick another target")
    path.write_text(spec_for(t, parent=parent, origin=origin, seed=seed, archives=archives),
                    encoding="utf-8", newline="\n")
    return path


def pick_from_queue(root: Path, queue_csv: Path, target: str | None) -> dict:
    """The named queue row, or the highest-ranked one nobody has claimed (no campaigns/<slug>.yaml)."""
    rows = read_queue(queue_csv)
    if target is None:
        taken = {p.stem for p in (root / "campaigns").glob("*.yaml")}
        row = next((r for r in rows if slug_for(r["name"]) not in taken), None)
        if row is None:
            raise SystemExit("every queued target already has a campaign")
        return row
    row = next((r for r in rows if slug_for(r["name"]) == slug_for(target)), None)
    if row is None:
        raise SystemExit(f"{target!r} is not in {queue_csv}")
    return row


# ------------------------------------------------------------------ report drafts
def _load_outputs(outdir: Path) -> dict:
    out = {}
    for f in sorted((outdir / "runner").glob("*.json")):
        out[f.stem] = json.loads(f.read_text(encoding="utf-8"))
    return out


def _fmt(v, nd=0):
    if v is None:
        return "—"
    if isinstance(v, float):
        return f"{v:.{nd}f}"
    return str(v)


def _transit_sections(known, cal, evs, repeats) -> list[str]:
    """Report sections that only apply when light curves were screened."""
    L: list[str] = []
    L += ["", "## Positive control (catalogued transit)", "",
          "| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |",
          "|---|---|---|---|---|---|---|"]
    for pid, v in known.items():
        if not v["epochs"]:
            L.append(f"| `{pid}` | — | epoch not in this light curve | — | — | {_fmt(v['catalogue']['depth_ppm'])} | — |")
        for ep in v["epochs"]:
            dep = _fmt(ep.get("measured_depth_ppm")) + (f" ± {ep['depth_err_ppm']:.0f}" if ep.get("depth_err_ppm") else "")
            L.append(f"| `{pid}` | {ep['epoch_bjd']:.5f} | {ep['state']} | {ep['usable_in_transit_cadences']} | {dep} | "
                     f"{_fmt(v['catalogue']['depth_ppm'])} | {_fmt(ep.get('entry_offset_hours'), 2)} |")
    L += ["", "Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median;"
          " the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or"
          " an epoch/duration error; it is reported, not used as a pass mark.", ""]

    L += ["## Calibration and sensitivity", "",
          "| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |", "|---|---|---|---|---|"]
    for pid, c in cal.items():
        d90 = c.get("depth_for_90pct_completeness_ppm", {})
        dec = ", ".join(f"{d}: {_fmt(v.get('declared'))}" for d, v in d90.items())
        kst = ", ".join(f"{d}: {_fmt(v.get('calibrated'))}" for d, v in d90.items())
        L.append(f"| `{pid}` | {_fmt(c.get('k_star'))} | {c.get('k_star_at_grid_floor')} | {dec} | {kst} |")
    L += ["", "The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.", ""]

    L += ["## Screen events outside the catalogued epoch", ""]
    if evs:
        L += ["Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.", "",
              "| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |",
              "|---|---|---|---|---|---|---|"]
        for pid, e in sorted(evs, key=lambda x: (not x[1]["persistent"], x[1]["deepest_median_residual"])):
            L.append(f"| `{pid}` | {e['mid_time_BJD_like']:.5f} | {e['deepest_median_residual']:.5f} | {e['max_cadences']} | "
                     f"{'+'.join(e['flux_types'])} | {', '.join(f'{b:g}' for b in e['baselines_days'])} | {'yes' if e['persistent'] else 'no'} |")
        L += ["", "None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**."
              " Most screen events in TESS light curves are systematics; each is at most an unverified lead.", ""]
    else:
        L += ["None at the threshold used.", ""]

    if repeats:
        L += ["## Repeat candidates", "",
              "Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded"
              " only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed."
              " Full per-alias evidence: `period_aliases.json`.", "",
              "| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |",
              "|---|---|---|---|---|---|"]
        for c in repeats:
            L.append(f"| {c['event_bjd']:.5f} | {c['depth_ppm']:.0f} | {c['reference_depth_ppm']:.0f} | {c['delta_t_days']:.4f} | "
                     f"{c['n_allowed']} / {c['n_aliases']} | {', '.join(f'{p:g}' for p in c['allowed_periods_days'][:20])} |")
        L += ["", "To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a"
              " period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.", ""]

    return L


def draft_report(spec: dict, root: Path) -> list[Path]:
    """Write REPORT.md / SEARCH_LOG.md drafts from runner outputs. A file without the draft marker
    (i.e. already reviewed or hand-written) is never overwritten; the draft goes beside it."""
    outdir = (root / spec["outputs"]).resolve()
    o = _load_outputs(outdir)
    summ = o.get("RUN_SUMMARY")
    if not summ:
        raise SystemExit(f"no runner outputs in {outdir}; run the campaign first")
    rec_path = root / spec["record"]["path"]
    rec = json.loads(rec_path.read_text(encoding="utf-8")) if rec_path.is_file() else {}
    checks = rec.get("checks", [])
    prods = (o.get("fetch_products") or {}).get("result", {}).get("products", {})
    cal = (o.get("calibrate_screen") or {}).get("result", {}).get("per_product", {})
    known = (o.get("known_signal_recovery") or {}).get("result", {}).get("per_product", {})
    screen = (o.get("residual_screen") or {}).get("result", {}).get("per_product", {})
    prior = (o.get("prior_art") or {}).get("result", {}).get("targets", {})
    repeats = (o.get("period_aliases") or {}).get("result", {}).get("candidates", [])
    runs = {k: v.get("run_id") for k, v in o.items() if k != "RUN_SUMMARY"}
    tgt = (spec.get("targets") or [{}])[0]
    kstate = next((c for c in checks if c["name"] == CHECK_KNOWN), {})
    n_out = sum(v.get("entries_outside_veto", 0) for v in screen.values())
    evs = [(pid, e) for pid, v in screen.items() for e in v.get("distinct_events_outside_veto", [])]
    n_pers = sum(e["persistent"] for _, e in evs)
    cid = spec["campaign_id"]
    screened = "residual_screen" in o
    nss_out = (o.get("astrometric_vetting") or {}).get("result", {}).get("targets", {})

    L = [DRAFT_MARKER, f"# {rec.get('title', cid)}", "",
         "> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved",
         "> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and",
         "> delete the first line (the draft marker) once reviewed.", "",
         f"- Campaign spec: `{spec['_path'].relative_to(root).as_posix() if hasattr(spec['_path'], 'relative_to') else spec['_path']}`",
         f"- Parent queue: `{spec.get('parent', '—')}`",
         f"- Ledger runs: " + ", ".join(f"{k} #{v}" for k, v in runs.items() if v) if runs else "- Ledger runs: —",
         f"- Runner finished (UTC): {summ.get('finished_utc', '—')}", "",
         "## Bottom line", ""]
    if kstate.get("state") == "passed":
        L.append(f"The calibrated screen **recovered the catalogued transit** of {tgt.get('name')} ({kstate.get('note')}).")
    elif kstate:
        L.append(f"Positive control **{kstate.get('state', 'not_tested').replace('_', ' ')}**: {kstate.get('note', '')}.")
    if not screened:
        L.append("No light curve was screened in this campaign (steps run: "
                 + ", ".join(summ.get("steps_run", [])) + "); see *Checks* for what was tested.")
    elif n_out:
        L.append(f"Outside the catalogued epoch the screen left {n_out} threshold entries forming **{len(evs)} distinct event(s)**, "
                 f"**{n_pers} persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.")
    else:
        L.append("Outside the catalogued epoch the screen left **no** threshold entries: a bounded null within the "
                 "completeness below.")
    if repeats:
        c = repeats[0]
        L.append(f"**Repeat candidate (unverified lead):** a persistent event at BJD {c['event_bjd']:.4f} matches the catalogued "
                 f"transit's depth ({c['depth_ppm']:.0f} vs {c['reference_depth_ppm']:.0f} ppm), {c['delta_t_days']:.3f} d later; "
                 f"{c['n_allowed']} of {c['n_aliases']} period aliases remain. See *Repeat candidates*.")
    for name, r in nss_out.items():
        L.append(f"Gaia DR3 NSS, {name}: **{r.get('state')}** — {r.get('note')}.")
    L += ["", "This is a pipeline check on a known object, not a discovery claim."
          + (" Two transits allow only the listed period aliases; they do not fix the period." if repeats else
             " No period is implied by a single transit." if screened else ""), ""]

    L += ["## Target", "", "| Field | Value | Source |", "|---|---|---|"]
    for k in ("name", "tic", "ra_deg", "dec_deg", "t0_bjd", "period_days", "depth_ppm", "duration_h", "tmag", "catalogue_row_updated"):
        if tgt.get(k) is not None:
            L.append(f"| {k} | {tgt[k]} | {tgt.get('position_source', 'spec')} (copied in the spec) |")
    L += ["", "## Products", "", "| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |", "|---|---|---|---|---|---|"]
    for pid, p in prods.items():
        sector = "—" if p.get("sector") is None else p.get("sector")
        covers = "—" if p.get("covers_known_epoch") is None else p.get("covers_known_epoch")
        L.append(f"| `{pid}` | {p.get('kind', '—')} | {sector} | {covers} | `{p['sha256'][:16]}` | {p.get('fetched_now')} |")

    if nss_out:
        L += ["", "## Gaia DR3 astrometric vetting", "",
              "| Target | Gaia DR3 source | Sep (\") | G | Parallax (mas) | Sources in radius | Identification | NSS solutions | State |",
              "|---|---|---|---|---|---|---|---|---|"]
        for name, r in nss_out.items():
            m = r.get("target_match") or {}
            L.append(f"| {name} | {m.get('source_id', '—')} | {_fmt(m.get('sep_arcsec'), 3)} | {_fmt(m.get('phot_g_mean_mag'), 3)} | "
                     f"{_fmt(m.get('parallax'), 3)} | {m.get('n_sources_in_radius', '—')} | {m.get('identification', '—')} | "
                     f"{r.get('nss_solutions', 0)} | {r.get('state')} |")
        L += ["", "An NSS solution at or above the significance threshold means the companion is already known to Gaia; no"
              " solution is *inconclusive* (Gaia's NSS sensitivity is incomplete), never a pass. Full rows: `nss.json`.", ""]
    if screened:
        L += _transit_sections(known, cal, evs, repeats)
    if prior:
        L += ["## Catalogue cross-match", ""]
    for name, res in prior.items():
        L.append(f"**{name}**")
        L.append("")
        for svc, r in res.items():
            L.append(f"- {svc} ({r.get('state')}, {r.get('retrieved_utc', '')[:10]}): {r.get('result')}")
        L.append("")

    L += ["## Checks", "", "| Check | State | Note |", "|---|---|---|"]
    for c in checks:
        L.append(f"| {c['name']} | {c['state']} | {(c.get('note') or '').replace('|', '/')} |")
    L += ["", "## Reproduction", "", "```bash", f"python -m cygnus.multi run {spec['_path'].relative_to(root).as_posix()}",
          f"python -m cygnus.multi report {spec['_path'].relative_to(root).as_posix()}", "```", ""]
    report = "\n".join(L)

    archive_labels = sorted({p.get("archive", "MAST") for p in prods.values()}) or ["MAST"]
    channel_note = ", ".join(sorted({f"{p.get('format')}" for p in prods.values()})) or "spoc_lc"
    kinds = sorted({p.get("kind") or "?" for p in prods.values()})
    S = [DRAFT_MARKER, f"# Search log: {cid}", "", "> Generated draft; see REPORT.md.", "",
         "| Item | Value |", "|---|---|",
         f"| Archive(s) | {', '.join(archive_labels)} (discovered via the archive adapters; formats {channel_note}) |",
         f"| Products fetched | {len(prods)} (kinds: {', '.join(kinds) or '—'}) |",
         f"| Selection | {'QUALITY = 0 with finite, nonzero channels as read per archive' if screened
                          else 'none — no light-curve product was retrieved, so nothing was screened'} |",
         f"| Veto | {spec.get('veto') or '—'} |"]
    if screened:
        S += [f"| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |",
              f"| Entries outside veto | {n_out} ({len(evs)} distinct events, {n_pers} persistent) |"]
    S += [f"| Catalogue services | {', '.join(sorted({s for r in prior.values() for s in r})) or '—'} |",
          f"| Random seed | {spec.get('random_seed')} |"]
    if screened:
        S += ["", "## Per product", "", "| Product | Rows | Usable | k | Entries | Outside veto |", "|---|---|---|---|---|---|"]
        for pid, v in screen.items():
            S.append(f"| `{pid}` | {v['rows']} | {v['usable']} | {_fmt(v['k_mad'], 2)} | {v['entries']} | {v['entries_outside_veto']} |")
    else:
        S += ["", "## Products fetched (no screen)", "",
              "No light curve was retrieved, so there are no rows, thresholds or entries to report:", ""]
        for pid, p in prods.items():
            S.append(f"- `{pid}` — {p.get('archive')}, {p.get('kind')} ({p.get('description') or p.get('format')})")
    S += ["", "## Not searched / not tested", ""]
    if screened:
        S += ["- Sectors beyond those listed above (at most six light curves per target are retrieved).",
              "- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids;"
              " pointing correlation; ADS literature.", ""]
    else:
        S += ["- No light curve was retrieved or screened: this campaign's questions are answered from catalogue tables"
              " alone, so transit photometry (depths, epochs, centroids) is not tested here.",
              "- Proper-motion propagation of the target position to the Gaia epoch, and the ADS literature search"
              " (both are declared checks marked not_tested in the sky record).", ""]
    log = "\n".join(S)

    written = []
    for fname, text in (("REPORT.md", report), ("SEARCH_LOG.md", log)):
        dest = outdir / fname
        if dest.exists() and DRAFT_MARKER not in dest.read_text(encoding="utf-8"):
            dest = outdir / fname.replace(".md", ".draft.md")
        dest.write_text(text, encoding="utf-8", newline="\n")
        written.append(dest)
    return written


# ------------------------------------------------------------------ queue board
def queue_status(root: Path, queue_csv: Path) -> list[dict]:
    rows = read_queue(queue_csv)
    out = []
    for r in rows:
        slug = slug_for(r["name"])
        spec = root / "campaigns" / f"{slug}.yaml"
        rec = root / "campaigns" / slug / "sky_record.json"
        rep = root / "campaigns" / slug / "REPORT.md"
        st = {"rank": r.get("rank"), "name": r["name"], "campaign": slug if spec.exists() else None,
              "state": "unclaimed", "known_signal": None, "review": None}
        if spec.exists():
            st["state"] = "claimed"
        if rec.is_file():
            recd = json.loads(rec.read_text(encoding="utf-8"))
            st["state"] = recd.get("status")
            st["known_signal"] = next((c["state"] for c in recd.get("checks", []) if c["name"] == CHECK_KNOWN), None)
        if rep.is_file():
            st["review"] = "draft" if DRAFT_MARKER in rep.read_text(encoding="utf-8") else "reviewed"
        out.append(st)
    return out

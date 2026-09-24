"""Design-review mockups for the astronomy-first site redesign.

Every plotted value comes from a recorded worktree file:

* positions   docs/tier1_pack/NAME_RESOLUTIONS.json   (CDS Sesame, ICRS)
* categories  docs/tier1_pack/RUN_CONFIG.json          (the project's own target lists)
* holdings    docs/tier1_pack/MASTER_MANIFEST.csv      (product IDs, sectors, t_min/t_max MJD)
* photometry  reports/tess-wasp12-residual-01/sector{20,43}/normalized_series.csv
* ephemeris   reports/tess-wasp12-residual-01/REPORT.md (NASA Exoplanet Archive, 2026-09-24)

Reference curves (graticule, galactic plane, ecliptic) are computed from
standard constants below. Nothing is drawn that is not in these sources.

Run:  python design-system/mockups/build_mockups.py   (needs numpy)
"""

from __future__ import annotations

import csv
import html
import json
import math
import re
from pathlib import Path

import numpy as np

WT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
PACK = WT / "docs" / "tier1_pack"
REPORT = WT / "reports" / "tess-wasp12-residual-01"

# Recorded ephemeris (REPORT.md: NASA Exoplanet Archive pscomppars, queried 2026-09-24)
P_DAYS = 1.09141890100
T0_BJD = 2457607.51930500
BJDREF = 2457000.0

esc = html.escape


# ------------------------------------------------------------------ data
def load_targets() -> list[dict]:
    res = json.loads((PACK / "NAME_RESOLUTIONS.json").read_text(encoding="utf-8"))
    cfg = json.loads((PACK / "RUN_CONFIG.json").read_text(encoding="utf-8"))
    fields, tess = set(cfg["field_names"]), set(cfg["tess_target_names"])
    rows = list(csv.DictReader((PACK / "MASTER_MANIFEST.csv").open(encoding="utf-8")))
    targets = []
    for name, r in res.items():
        if not r.get("ok"):
            continue
        bench = set(cfg["bench_object_names"])
        cat = "field" if name in fields else ("tess" if name in tess else ("bench" if name in bench else "other"))
        held = []
        for row in rows:
            extra = json.loads(row["extra_json"] or "{}")
            blob = " ".join(str(extra.get(k, "")) for k in ("tag", "field", "field_name", "target")) + " " + row["product_id"]
            if re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", blob) or \
               re.search(re.escape(name.replace(" ", "_")), row["product_id"]):
                held.append({"row": row, "extra": extra})
        targets.append({"name": name, "ra": r["ra_deg"], "dec": r["dec_deg"], "frame": r["frame"],
                        "resolved": r["resolved_utc"], "cat": cat, "held": held})
    return targets


def hms(ra: float) -> str:
    h = ra / 15.0
    hh = int(h); mm = int((h - hh) * 60); ss = ((h - hh) * 60 - mm) * 60
    return f"{hh:02d}ʰ{mm:02d}ᵐ{ss:05.2f}ˢ"


def dms(dec: float) -> str:
    s = "−" if dec < 0 else "+"
    d = abs(dec); dd = int(d); mm = int((d - dd) * 60); ss = ((d - dd) * 60 - mm) * 60
    return f"{s}{dd:02d}°{mm:02d}′{ss:04.1f}″"


# ------------------------------------------------------------------ projection
def hammer(ra_deg: float, dec_deg: float) -> tuple[float, float]:
    """Hammer–Aitoff, centre RA 0h, RA increasing to the left (east left). Unit: x∈[-2√2,2√2]."""
    lon = math.radians(((ra_deg + 180) % 360) - 180)
    lon = -lon  # east to the left
    lat = math.radians(dec_deg)
    z = math.sqrt(1 + math.cos(lat) * math.cos(lon / 2))
    return (2 * math.sqrt(2) * math.cos(lat) * math.sin(lon / 2) / z, math.sqrt(2) * math.sin(lat) / z)


W, H, PAD = 960, 500, 28
SX = (W - 2 * PAD) / (4 * math.sqrt(2))
SY = (H - 2 * PAD) / (2 * math.sqrt(2))


def to_px(ra: float, dec: float) -> tuple[float, float]:
    x, y = hammer(ra, dec)
    return W / 2 + x * SX, H / 2 - y * SY


def path_from(points: list[tuple[float, float]], break_px: float = 200) -> str:
    d, prev = [], None
    for ra, dec in points:
        x, y = to_px(ra, dec)
        if prev is None or abs(x - prev[0]) > break_px:
            d.append(f"M{x:.1f} {y:.1f}")
        else:
            d.append(f"L{x:.1f} {y:.1f}")
        prev = (x, y)
    return " ".join(d)


# Galactic → ICRS (IAU 1958 definition, J2000 pole): pole RA 192.85948°, Dec 27.12825°, l(NCP) 122.93192°
def galactic_to_icrs(l_deg: float, b_deg: float) -> tuple[float, float]:
    ra_p, dec_p, l_ncp = map(math.radians, (192.85948, 27.12825, 122.93192))
    l, b = math.radians(l_deg), math.radians(b_deg)
    sin_dec = math.sin(dec_p) * math.sin(b) + math.cos(dec_p) * math.cos(b) * math.cos(l_ncp - l)
    dec = math.asin(sin_dec)
    y = math.cos(b) * math.sin(l_ncp - l)
    x = math.cos(dec_p) * math.sin(b) - math.sin(dec_p) * math.cos(b) * math.cos(l_ncp - l)
    ra = (ra_p + math.atan2(y, x)) % (2 * math.pi)
    return math.degrees(ra), math.degrees(dec)


def ecliptic_to_icrs(lam_deg: float, eps_deg: float = 23.4392911) -> tuple[float, float]:
    lam, eps = math.radians(lam_deg), math.radians(eps_deg)
    ra = math.atan2(math.sin(lam) * math.cos(eps), math.cos(lam)) % (2 * math.pi)
    dec = math.asin(math.sin(eps) * math.sin(lam))
    return math.degrees(ra), math.degrees(dec)


def sky_map(targets: list[dict], link: dict[str, str]) -> str:
    g = []
    # outline + graticule
    outline = [(179.999, d) for d in range(-90, 91, 2)] + [(-179.999 % 360, d) for d in range(90, -91, -2)]
    g.append(f'<path class="sky-bg" d="{path_from(outline, 9999)} Z"/>')
    for dec in (-60, -30, 0, 30, 60):
        pts = [(ra, dec) for ra in np.linspace(180.001, 540 - 0.001, 181) % 360]
        g.append(f'<path class="grat{" grat-eq" if dec == 0 else ""}" d="{path_from(pts)}"/>')
        x, y = to_px(180.0001, dec)
        g.append(f'<text class="tick" x="{x - 6:.1f}" y="{y + 4:.1f}" text-anchor="end">{"+" if dec > 0 else ("−" if dec < 0 else "")}{abs(dec)}°</text>')
    for h in range(0, 24, 2):
        ra = h * 15
        pts = [(ra, d) for d in np.linspace(-90, 90, 91)]
        g.append(f'<path class="grat" d="{path_from(pts)}"/>')
        x, y = to_px(ra, 0)
        if h not in (12,):
            g.append(f'<text class="tick" x="{x:.1f}" y="{y + 14:.1f}" text-anchor="middle">{h}ʰ</text>')
    gal = [galactic_to_icrs(l, 0) for l in np.linspace(0, 360, 361)]
    gal.sort(key=lambda p: ((p[0] + 180) % 360))
    g.append(f'<path class="ref ref-gal" d="{path_from(gal, 120)}"><title>Galactic plane (b = 0°)</title></path>')
    ecl = [ecliptic_to_icrs(l) for l in np.linspace(0, 360, 361)]
    ecl.sort(key=lambda p: ((p[0] + 180) % 360))
    g.append(f'<path class="ref ref-ecl" d="{path_from(ecl, 120)}"><title>Ecliptic (J2000 obliquity 23.4393°)</title></path>')

    # markers + greedy labels
    placed: list[tuple[float, float, float, float]] = []
    for t in sorted(targets, key=lambda t: -t["dec"]):
        x, y = to_px(t["ra"], t["dec"])
        t["_xy"] = (x, y)
        placed.append((x - 5, y - 5, x + 5, y + 5))
    for t in sorted(targets, key=lambda t: -t["dec"]):
        x, y = t["_xy"]
        cls = {"field": "m-field", "tess": "m-tess", "bench": "m-bench", "other": "m-other"}[t["cat"]]
        tip = f'{t["name"]} · RA {hms(t["ra"])} Dec {dms(t["dec"])} (ICRS) · {len(t["held"])} product rows'
        mark = {"m-field": f'<circle class="{cls}" cx="{x:.1f}" cy="{y:.1f}" r="6"/>',
                "m-tess": f'<circle class="{cls}" cx="{x:.1f}" cy="{y:.1f}" r="3.6"/>',
                "m-bench": f'<rect class="{cls}" x="{x - 3.2:.1f}" y="{y - 3.2:.1f}" width="6.4" height="6.4"/>',
                "m-other": f'<path class="{cls}" d="M{x - 4:.1f} {y:.1f}H{x + 4:.1f}M{x:.1f} {y - 4:.1f}V{y + 4:.1f}"/>'}[cls]
        wlab = 6.3 * len(t["name"]) + 4
        cands = [(x + 9, y + 4, "start"), (x - 9, y + 4, "end"), (x - wlab / 2, y - 10, "start"), (x - wlab / 2, y + 18, "start")]
        for lx, ly, anchor in cands:
            x0 = lx if anchor == "start" else lx - wlab
            box = (x0, ly - 10, x0 + wlab, ly + 3)
            if all(box[2] < b[0] or box[0] > b[2] or box[3] < b[1] or box[1] > b[3] for b in placed):
                break
        placed.append(box)
        href = link.get(t["name"], "#")
        g.append(f'<a href="{href}" class="target"><title>{esc(tip)}</title>{mark}'
                 f'<text class="lab" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}">{esc(t["name"])}</text></a>')
    return (f'<svg class="skymap" viewBox="0 0 {W} {H}" role="img" aria-labelledby="sky-t sky-d">'
            f'<title id="sky-t">Positions queried by the project</title>'
            f'<desc id="sky-d">Hammer–Aitoff projection in ICRS, centre 0h, east to the left, with the galactic plane and ecliptic. '
            f'{len(targets)} Sesame-resolved positions; the same data are in the table below.</desc>'
            + "".join(g) + "</svg>")


# ------------------------------------------------------------------ light curves
def load_series(sector: int) -> dict:
    arr = np.genfromtxt(REPORT / f"sector{sector}" / "normalized_series.csv", delimiter=",", names=True)
    screen = json.loads((REPORT / f"sector{sector}" / "screen.json").read_text(encoding="utf-8"))
    ok = (arr["QUALITY"] == 0) & np.isfinite(arr["PDCSAP_FLUX"]) & np.isfinite(arr["TIME_stored"]) & (arr["PDCSAP_FLUX"] > 0)
    t = arr["TIME_stored"][ok]
    f = arr["PDCSAP_FLUX"][ok] / np.median(arr["PDCSAP_FLUX"][ok])
    return {"t": t, "f": f, "n_rows": len(arr), "n_ok": int(ok.sum()), "screen": screen}


def binned(x: np.ndarray, y: np.ndarray, width: float) -> tuple[np.ndarray, np.ndarray]:
    edges = np.arange(x.min(), x.max() + width, width)
    idx = np.digitize(x, edges)
    xs, ys = [], []
    for i in np.unique(idx):
        m = idx == i
        if m.sum() >= 3:
            xs.append(np.median(x[m])); ys.append(np.median(y[m]))
    return np.array(xs), np.array(ys)


def axes_svg(w, h, xlim, ylim, xlabel, ylabel, xticks, yticks, body, ml=58, mb=38, mt=10, mr=10, fmt_y="{:.3f}"):
    pw, ph = w - ml - mr, h - mt - mb
    X = lambda v: ml + (v - xlim[0]) / (xlim[1] - xlim[0]) * pw
    Y = lambda v: mt + (1 - (v - ylim[0]) / (ylim[1] - ylim[0])) * ph
    g = [f'<rect class="plot-frame" x="{ml}" y="{mt}" width="{pw}" height="{ph}"/>']
    for v in xticks:
        g.append(f'<line class="tickline" x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{mt + ph}" y2="{mt + ph + 4}"/>'
                 f'<text class="tick" x="{X(v):.1f}" y="{mt + ph + 16}" text-anchor="middle">{v:g}</text>')
    for v in yticks:
        g.append(f'<line class="gridline" x1="{ml}" x2="{ml + pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}"/>'
                 f'<text class="tick" x="{ml - 6}" y="{Y(v) + 4:.1f}" text-anchor="end">{fmt_y.format(v)}</text>')
    g.append(f'<text class="axlab" x="{ml + pw / 2:.1f}" y="{h - 4}" text-anchor="middle">{xlabel}</text>')
    g.append(f'<text class="axlab" transform="translate(12 {mt + ph / 2:.1f}) rotate(-90)" text-anchor="middle">{ylabel}</text>')
    return g + [f'<svg x="{ml}" y="{mt}" width="{pw}" height="{ph}" overflow="hidden">' + body(X, Y, ml, mt) + "</svg>"]


def time_series_svg(s: dict, sector: int) -> str:
    bx, by = binned(s["t"], s["f"], 30 / 1440)
    t0, t1 = float(s["t"].min()), float(s["t"].max())
    ylim = (0.978, 1.008)
    def body(X, Y, ml, mt):
        dots = "".join(f"M{X(a) - ml:.1f} {Y(b) - mt:.1f}h0.01" for a, b in zip(bx, by))
        return f'<path class="pts" d="{dots}"/>'
    ticks = [v for v in range(int(math.ceil(t0 / 5) * 5), int(t1) + 1, 5)]
    g = axes_svg(720, 230, (t0 - 0.3, t1 + 0.3), ylim, "BTJD (BJD − 2457000, TDB), days",
                 "Relative flux", ticks, [0.98, 0.99, 1.0], body)
    return (f'<svg class="plot" viewBox="0 0 720 230" role="img" aria-label="TESS Sector {sector} PDCSAP light curve of WASP-12, 30-minute median bins">'
            + "".join(g) + "</svg>")


def fold_svg(s: dict, sector: int) -> str:
    bjd = s["t"] + BJDREF
    ph = ((bjd - T0_BJD) / P_DAYS + 0.5) % 1 - 0.5
    hours = ph * P_DAYS * 24
    win = np.abs(hours) <= 4
    bx, by = binned(hours[win], s["f"][win], 0.1)
    def body(X, Y, ml, mt):
        raw = "".join(f"M{X(a) - ml:.1f} {Y(b) - mt:.1f}h0.01" for a, b in zip(hours[win], s["f"][win]))
        veto = 0.08 * P_DAYS * 24
        band = f'<rect class="veto" x="{X(-veto) - ml:.1f}" y="0" width="{X(veto) - X(-veto):.1f}" height="400"/>'
        dots = "".join(f"M{X(a) - ml:.1f} {Y(b) - mt:.1f}h0.01" for a, b in zip(bx, by))
        return band + f'<path class="raw" d="{raw}"/><path class="pts pts-bin" d="{dots}"/>'
    g = axes_svg(440, 250, (-4, 4), (0.975, 1.01), "Hours from mid-transit (archive ephemeris)", "Relative flux",
                 [-4, -2, 0, 2, 4], [0.98, 0.99, 1.0], body)
    return (f'<svg class="plot" viewBox="0 0 440 250" role="img" aria-label="Sector {sector} flux folded on the NASA Exoplanet Archive ephemeris of WASP-12 b">'
            + "".join(g) + "</svg>")


def coverage_svg(held: list[dict]) -> str:
    rows = []
    for h in held:
        e = h["extra"]
        m = re.search(r"-s(\d{4})-", h["row"]["product_id"])
        if m and e.get("t_min") and e.get("t_max"):
            rows.append((int(m.group(1)), float(e["t_min"]), float(e["t_max"]), h["row"]["product_id"]))
    if not rows:
        return ""
    mjd_year = lambda mjd: 2000 + (mjd - 51544.5) / 365.25
    y0, y1 = 2018, 2027
    w, hgt, ml, mr = 900, 70, 20, 20
    X = lambda y: ml + (y - y0) / (y1 - y0) * (w - ml - mr)
    g = [f'<line class="axisline" x1="{ml}" x2="{w - mr}" y1="40" y2="40"/>']
    for yr in range(y0, y1 + 1):
        g.append(f'<line class="tickline" x1="{X(yr):.1f}" x2="{X(yr):.1f}" y1="40" y2="45"/><text class="tick" x="{X(yr):.1f}" y="58" text-anchor="middle">{yr}</text>')
    last_x, level = -99.0, 0
    for sec, a, b, pid in sorted(rows):
        xa, xb = X(mjd_year(a)), X(mjd_year(b))
        level = (level + 1) % 2 if (xa + xb) / 2 - last_x < 30 else 0
        last_x = (xa + xb) / 2
        g.append(f'<g><title>Sector {sec}: MJD {a:.2f}–{b:.2f} · {esc(pid)}</title>'
                 f'<rect class="cov" x="{xa:.1f}" y="22" width="{max(xb - xa, 2):.1f}" height="14"/>'
                 f'<text class="tick" x="{(xa + xb) / 2:.1f}" y="{16 - 11 * level}" text-anchor="middle">S{sec}</text></g>')
    return (f'<svg class="plot" viewBox="0 -10 {w} {hgt + 10}" role="img" aria-label="TESS sectors held for this target, by observation dates">'
            + "".join(g) + "</svg>")


# ------------------------------------------------------------------ pages
CSS = (OUT / "mockup.css").name


def page(title: str, body: str, current: str) -> str:
    nav = [("index.html", "Sky"), ("target-wasp-12.html", "Targets"), ("log.html", "Log"), ("#", "Campaigns"), ("#", "Method")]
    links = "".join(f'<a href="{h}"{" aria-current=page" if l == current else ""}>{l}</a>' for h, l in nav)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><link rel="stylesheet" href="{CSS}"></head><body>
<p class="mock-note">Design mockup for review · built from recorded worktree data by <code>design-system/mockups/build_mockups.py</code></p>
<header class="mast"><div class="wrap mast-row">
<a class="brand" href="index.html"><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3.5V28.5M4.5 15.5L27.5 10.5" fill="none" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor"><rect x="14.4" y="1.9" width="3.2" height="3.2"/><rect x="14.6" y="11.6" width="2.8" height="2.8"/><rect x="14.8" y="27.3" width="2.4" height="2.4"/><rect x="3.3" y="14.3" width="2.4" height="2.4"/><rect x="26.3" y="9.3" width="2.4" height="2.4"/></g></svg>
<span>Cygnus</span></a><nav aria-label="Primary">{links}</nav>
<button class="mode" type="button" onclick="var r=document.documentElement;r.dataset.theme=r.dataset.theme==='night'?'day':'night';this.textContent=r.dataset.theme==='night'?'Day':'Night'">Night</button>
</div></header><main class="wrap">{body}</main>
<footer class="wrap foot">Positions: CDS Sesame via astropy, ICRS. Photometry: MAST TESS SPOC (public). Working identifiers <span class="mono">CYG-*</span> are not designations.</footer>
</body></html>"""


def build() -> None:
    targets = load_targets()
    link = {"WASP-12": "target-wasp-12.html"}
    n_prod = sum(len(t["held"]) for t in targets)
    trows = "".join(
        f'<tr><td><a href="{link.get(t["name"], "#")}">{esc(t["name"])}</a></td>'
        f'<td class="num mono">{hms(t["ra"])}</td><td class="num mono">{dms(t["dec"])}</td>'
        f'<td class="num mono">{t["ra"]:.5f}</td><td class="num mono">{t["dec"]:+.5f}</td>'
        f'<td>{ {"field": "Benchmark field", "tess": "TESS benchmark host", "bench": "Benchmark object", "other": "Other queried position"}[t["cat"]] }</td>'
        f'<td class="num mono">{len(t["held"])}</td></tr>'
        for t in sorted(targets, key=lambda t: t["ra"]))
    home = f"""
<section class="lead">
  <h1>Where Cygnus has looked</h1>
  <p>Every position the project has queried in a public archive, from its name-resolution record. Select a target for the products held, their epochs, and the analyses run on them.</p>
</section>
<figure class="sky">{sky_map(targets, link)}
<figcaption><span class="key"><svg viewBox="0 0 14 14" aria-hidden="true"><circle class="m-field" cx="7" cy="7" r="5"/></svg>Benchmark field</span>
<span class="key"><svg viewBox="0 0 14 14" aria-hidden="true"><circle class="m-tess" cx="7" cy="7" r="3.6"/></svg>TESS benchmark host</span>
<span class="key"><svg viewBox="0 0 14 14" aria-hidden="true"><rect class="m-bench" x="3.8" y="3.8" width="6.4" height="6.4"/></svg>Benchmark object</span>
<span class="key"><svg viewBox="0 0 14 14" aria-hidden="true"><path class="m-other" d="M3 7H11M7 3V11"/></svg>Other queried position</span>
<span class="key"><svg viewBox="0 0 22 6" aria-hidden="true"><path class="ref ref-gal" d="M0 3H22"/></svg>Galactic plane</span>
<span class="key"><svg viewBox="0 0 22 6" aria-hidden="true"><path class="ref ref-ecl" d="M0 3H22"/></svg>Ecliptic</span>
<span class="src">Hammer–Aitoff, ICRS (J2000), 0ʰ centre, east left. {len(targets)} positions resolved 2026-09-24 via CDS Sesame; {n_prod} manifest rows matched by name.</span></figcaption></figure>
<section class="status-line"><p><b>State of the work, 2026-09-24.</b> One bounded analysis has run (TESS residual screen of WASP-12, two sectors): <i>null — no candidate</i>. One recovery test of the known planet WASP-12 b passed. Campaign <span class="mono">tess-mono-01</span> is drafted, not run. No candidate dossiers exist.</p></section>
<h2>Positions queried</h2>
<div class="tbl"><table><thead><tr><th>Name</th><th class="num">RA (ICRS)</th><th class="num">Dec (ICRS)</th><th class="num">RA °</th><th class="num">Dec °</th><th>Role in project</th><th class="num">Manifest rows</th></tr></thead><tbody>{trows}</tbody></table></div>
"""
    (OUT / "index.html").write_text(page("Cygnus — sky", home, "Sky"), encoding="utf-8")

    # target page
    w12 = next(t for t in targets if t["name"] == "WASP-12")
    s20, s43 = load_series(20), load_series(43)
    hdr = s20["screen"]["headers"]
    def prod_row(h: dict) -> str:
        r = h["row"]
        m = re.search(r"-s(\d{4})-", r["product_id"])
        size = f'{int(r["bytes"]) / 1e6:.2f} MB' if r["bytes"] else '<i class="unset">not recorded</i>'
        return (f'<tr><td class="mono small">{esc(r["product_id"])}</td><td>{esc(r["service"].upper())}</td>'
                f'<td class="mono">{m.group(1).lstrip("0") if m else "—"}</td><td class="num mono">{size}</td></tr>')
    prods = "".join(prod_row(h) for h in w12["held"])
    tgt = f"""
<p class="crumb"><a href="index.html">Sky</a> / Targets</p>
<header class="obj">
  <h1>WASP-12</h1>
  <p class="aka mono">TIC {hdr["TICID"]} · known transiting-planet host (WASP-12 b)</p>
  <dl class="coords">
    <div><dt>RA</dt><dd class="mono">{hms(w12["ra"])}</dd></div>
    <div><dt>Dec</dt><dd class="mono">{dms(w12["dec"])}</dd></div>
    <div><dt>Frame</dt><dd>ICRS, J2000 · CDS Sesame, resolved {w12["resolved"][:10]}</dd></div>
    <div><dt>TESS header</dt><dd class="mono">{hdr["RA_OBJ"]:.5f}°, {hdr["DEC_OBJ"]:+.5f}°</dd></div>
  </dl>
</header>
<section><h2>Coverage held</h2>
<figure>{coverage_svg(w12["held"])}<figcaption>TESS sectors in the Tier-1 manifest, placed at their recorded observation start and end (MJD, from MAST metadata).</figcaption></figure>
<div class="tbl"><table><thead><tr><th>Product</th><th>Archive</th><th>Sector</th><th class="num">Size</th></tr></thead><tbody>{prods}</tbody></table></div></section>
<section><h2>TESS Sector 20 light curve</h2>
<figure>{time_series_svg(s20, 20)}<figcaption>PDCSAP flux divided by its median, 30-min median bins. {s20["n_ok"]:,} of {s20["n_rows"]:,} cadences kept (QUALITY = 0, finite, positive). Product <span class="mono">{esc(s20["screen"]["input"]["file"])}</span>, SPOC data release 73, 120 s cadence, {hdr["DATE-OBS"][:10]} to {hdr["DATE-END"][:10]} UTC.</figcaption></figure></section>
<section><h2>Folded on the published ephemeris</h2>
<div class="pair"><figure>{fold_svg(s20, 20)}<figcaption>Sector 20 ({s20["n_ok"]:,} cadences)</figcaption></figure>
<figure>{fold_svg(s43, 43)}<figcaption>Sector 43 ({s43["n_ok"]:,} cadences)</figcaption></figure></div>
<p class="note">Ephemeris P = {P_DAYS} d, T<sub>0</sub> = BJD<sub>TDB</sub> {T0_BJD} (NASA Exoplanet Archive <span class="mono">pscomppars</span>, queried 2026-09-24). Grey points: individual cadences; dark points: 6-min medians. Shaded: the ±0.08-phase window excluded from the residual screen.</p></section>
<section><h2>Analyses on this target</h2>
<ol class="runs">
<li><span class="date mono">2026-09-24</span> <b>Residual screen, Sectors 20 and 43</b> — <span class="outcome">null</span>: 0 excursions ≥5 robust-MAD outside the transit window across SAP/PDCSAP and 1/2/3-day baselines. Threshold uncalibrated; pixel-level, centroid and injection tests not run. <a href="#">Report</a> · <a href="#">Search log</a></li>
<li><span class="date mono">2026-09-24</span> <b>Known-planet recovery, Sector 20</b> — <span class="outcome">recovered</span>: BLS peak 1.0914183 d, depth 1.42 %, 2.45 h. A pipeline check on a known planet, not a detection. <a href="#">Report</a></li>
</ol></section>
"""
    (OUT / "target-wasp-12.html").write_text(page("WASP-12 — Cygnus", tgt, "Targets"), encoding="utf-8")

    # observing log
    rows = list(csv.DictReader((PACK / "MASTER_MANIFEST.csv").open(encoding="utf-8")))
    NAMES = sorted((t["name"] for t in targets), key=len, reverse=True)
    entries = []
    for r in rows:
        extra = json.loads(r["extra_json"] or "{}")
        tag = extra.get("tag") or extra.get("field") or extra.get("field_name") or ""
        if not tag:
            for nm in NAMES:
                if nm.replace(" ", "_") in r["product_id"] or nm in r["query"]:
                    tag = nm
                    break
        entries.append((r["retrieved_utc"] or "", tag, r["service"].upper(), r["product_id"], r["state"],
                        re.sub(r"(cygnus:\S+|[A-Za-z]:[\\/]\S+)", "[private]", r["note"] or "")))
    entries += [("2026-09-24T—", "WASP-12", "ANALYSIS", "tess-wasp12-residual-01", "null", "S20+S43 residual screen; no excursion outside transit window"),
                ("2026-09-24T—", "WASP-12", "ANALYSIS", "wasp12_sector20 (BLS)", "recovered", "known planet recovered; smoke test")]
    entries.sort(key=lambda e: e[0], reverse=True)
    out, day = [], None
    for ts, tag, arch, pid, state, note in entries:
        d = ts[:10] or "undated"
        if d != day:
            out.append(f'<tr class="day"><th colspan="6" scope="rowgroup">{d}</th></tr>'); day = d
        st = {"drive_only": "held", "local": "held", "excluded": "excluded", "failed": "failed", "null": "null", "recovered": "recovered"}.get(state, state)
        out.append(f'<tr><td class="mono">{esc(ts[11:16] or "—")}</td><td>{esc(tag)}</td><td class="mono">{arch}</td>'
                   f'<td class="mono small">{esc(pid)}</td><td><span class="st st-{st}">{st}</span></td><td class="small">{esc(note)}</td></tr>')
    log = f"""
<section class="lead"><h1>Log</h1><p>Every archive retrieval and analysis run, newest first, in observing-log form. Failures and exclusions stay in the record.</p></section>
<div class="tbl"><table class="log"><thead><tr><th>UTC</th><th>Target / field</th><th>Source</th><th>Product or run</th><th>Outcome</th><th>Remarks</th></tr></thead><tbody>{"".join(out)}</tbody></table></div>
"""
    (OUT / "log.html").write_text(page("Log — Cygnus", log, "Log"), encoding="utf-8")
    print(f"targets {len(targets)}, rows matched {n_prod}, log entries {len(entries)}")


if __name__ == "__main__":
    build()

"""Cygnus logo concepts, generated from real catalogue data.

The marks use the true shape of the Northern Cross asterism of Cygnus from the Yale Bright Star Catalogue
(design-system/mockups/data/bsc5.csv, VizieR V/50): gnomonic projection about Sadr, east to the left, then
rotated as a whole so the long axis (Deneb to Albireo) is vertical. Star sizes follow V magnitude; the colours of
Albireo's two components follow their catalogue B-V. Nothing is drawn freehand except the wordmark and reticle.

Run:  python design-system/brand/build_brand.py   -> design-system/brand/concepts/*.svg + index.html
"""

from __future__ import annotations

import csv
import html
import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "concepts"
BSC = HERE.parent / "mockups" / "data" / "bsc5.csv"

# Northern Cross: HR numbers from BSC5
STARS = {"Deneb": "7924", "Sadr": "7796", "Gienah": "7949", "delta": "7528", "eta": "7615", "Albireo A": "7417", "Albireo B": "7418"}
LINES = [("Deneb", "Sadr"), ("Sadr", "eta"), ("eta", "Albireo A"), ("delta", "Sadr"), ("Sadr", "Gienah")]

INK_DARK, INK_LIGHT, ACCENT, NIGHT = "#ece7de", "#14171c", "#f0c27a", "#c8483a"
SANS = "'IBM Plex Sans','Segoe UI',system-ui,sans-serif"


def bv_rgb(bv: float) -> str:
    """B-V -> sRGB via Ballesteros temperature and a blackbody approximation, lightly desaturated."""
    t = 4600 * (1 / (0.92 * bv + 1.7) + 1 / (0.92 * bv + 0.62)) / 100
    r = 255 if t <= 66 else 329.698727446 * (t - 60) ** -0.1332047592
    g = 99.4708025861 * math.log(t) - 161.1195681661 if t <= 66 else 288.1221695283 * (t - 60) ** -0.0755148492
    b = 255 if t >= 66 else (0 if t <= 19 else 138.5177312231 * math.log(t - 10) - 305.0447927307)
    c = [max(0, min(255, v)) for v in (r, g, b)]
    return "#%02x%02x%02x" % tuple(round(v) for v in c)


def load() -> dict:
    rows = {r["HR"]: r for r in csv.DictReader(BSC.open(encoding="utf-8"))}
    return {k: {"ra": float(rows[v]["RAJ2000"]), "dec": float(rows[v]["DEJ2000"]), "V": float(rows[v]["Vmag"]),
                "bv": float(rows[v]["B-V"])} for k, v in STARS.items()}


def project(stars: dict) -> dict:
    c = stars["Sadr"]
    a0, d0 = math.radians(c["ra"]), math.radians(c["dec"])
    pts = {}
    for k, s in stars.items():
        a, d = math.radians(s["ra"]), math.radians(s["dec"])
        cosc = math.sin(d0) * math.sin(d) + math.cos(d0) * math.cos(d) * math.cos(a - a0)
        xi = math.cos(d) * math.sin(a - a0) / cosc
        eta = (math.cos(d0) * math.sin(d) - math.sin(d0) * math.cos(d) * math.cos(a - a0)) / cosc
        pts[k] = (-xi, -eta)  # east left, SVG y grows downward
    # rotate the whole figure so Deneb is straight above Albireo
    dx, dy = pts["Albireo A"][0] - pts["Deneb"][0], pts["Albireo A"][1] - pts["Deneb"][1]
    rot = math.pi / 2 - math.atan2(dy, dx)
    cr, sr = math.cos(rot), math.sin(rot)
    pts = {k: (x * cr - y * sr, x * sr + y * cr) for k, (x, y) in pts.items()}
    xs, ys = [p[0] for p in pts.values()], [p[1] for p in pts.values()]
    cx, cy, span = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, max(max(xs) - min(xs), max(ys) - min(ys))
    return {k: ((x - cx) / span, (y - cy) / span) for k, (x, y) in pts.items()}, math.degrees(rot)


def radius(V: float, scale: float) -> float:
    return scale * (0.02 + 0.0125 * max(0.0, 5.3 - V))


def asterism(pts, stars, size, cx, cy, ink, *, colour_albireo=True, line_w=None, star_scale=1.0, lines=True, gap=True):
    """Return SVG elements for the Northern Cross fitted in a box `size` wide centred on (cx, cy)."""
    s = size
    P = {k: (cx + x * s, cy + y * s) for k, (x, y) in pts.items()}
    lw = line_w if line_w is not None else s * 0.02
    out = []
    if lines:
        for a, b in LINES:
            (x1, y1), (x2, y2) = P[a], P[b]
            if gap:  # stop lines short of the stars so each star reads as a point of light
                L = math.hypot(x2 - x1, y2 - y1)
                ga, gb = radius(stars[a]["V"], s * star_scale) + s * 0.03, radius(stars[b]["V"], s * star_scale) + s * 0.03
                x1, y1, x2, y2 = x1 + (x2 - x1) * ga / L, y1 + (y2 - y1) * ga / L, x2 - (x2 - x1) * gb / L, y2 - (y2 - y1) * gb / L
            out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{ink}" stroke-width="{lw:.2f}" stroke-linecap="round" opacity=".7"/>')
    for k, (x, y) in P.items():
        if k == "Albireo B":
            continue
        r = radius(stars[k]["V"], s * star_scale)
        fill = bv_rgb(stars[k]["bv"]) if (colour_albireo and k == "Albireo A") else ink
        out.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}"/>')
    # Albireo B: the blue companion (true separation 35", far below this scale) drawn just beside A, as a signature
    xa, ya = P["Albireo A"]
    rb = radius(stars["Albireo B"]["V"], s * star_scale)
    ra = radius(stars["Albireo A"]["V"], s * star_scale)
    fillb = bv_rgb(stars["Albireo B"]["bv"]) if colour_albireo else ink
    out.append(f'<circle cx="{xa + ra + rb + s * 0.02:.2f}" cy="{ya - s * 0.006:.2f}" r="{rb * 1.25:.2f}" fill="{fillb}"/>')
    return out


def reticle(cx, cy, r, ink, w):
    ticks = []
    for k in range(4):
        a = k * math.pi / 2
        x1, y1 = cx + math.cos(a) * r * 0.88, cy + math.sin(a) * r * 0.88
        x2, y2 = cx + math.cos(a) * r * 1.1, cy + math.sin(a) * r * 1.1
        ticks.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{ink}" stroke-width="{w:.2f}" stroke-linecap="round"/>')
    for k in range(36):
        if k % 9 == 0:
            continue
        a = k * math.pi / 18
        x1, y1 = cx + math.cos(a) * r, cy + math.sin(a) * r
        x2, y2 = cx + math.cos(a) * r * 0.955, cy + math.sin(a) * r * 0.955
        ticks.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{ink}" stroke-width="{w * 0.6:.2f}" opacity=".6"/>')
    return [f'<circle cx="{cx}" cy="{cy}" r="{r:.2f}" fill="none" stroke="{ink}" stroke-width="{w:.2f}"/>'] + ticks


def svg(w, h, body, title, bg=None):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">'
            f"<title>{html.escape(title)}</title>{rect}{''.join(body)}</svg>")


def concept_a(pts, stars, ink, colour=True, size=512):
    """A · Northern Cross: the asterism alone."""
    return svg(size, size, asterism(pts, stars, size * 0.82, size / 2, size / 2, ink, colour_albireo=colour), "Cygnus mark: the Northern Cross")


def concept_b(pts, stars, ink, colour=True, size=512):
    """B · Cross in a reticle: the asterism inside a measuring reticle."""
    body = reticle(size / 2, size / 2, size * 0.44, ink, size * 0.014)
    body += asterism(pts, stars, size * 0.6, size / 2, size / 2, ink, colour_albireo=colour, star_scale=1.15)
    return svg(size, size, body, "Cygnus mark: the Northern Cross in a reticle")


def concept_c(pts, stars, ink, colour=True, size=512):
    """C · Transit: a star disc with a planet silhouette crossing it, the light curve beneath."""
    cx, cy, R = size / 2, size * 0.42, size * 0.28
    acc = ACCENT if colour else ink
    body = [f'<circle cx="{cx}" cy="{cy}" r="{R:.1f}" fill="none" stroke="{ink}" stroke-width="{size * 0.018:.1f}"/>',
            f'<circle cx="{cx + R * 0.38:.1f}" cy="{cy + R * 0.12:.1f}" r="{R * 0.2:.1f}" fill="{acc}"/>']
    y0, x0, x1 = size * 0.84, size * 0.14, size * 0.86
    d = f"M{x0:.1f} {y0:.1f} H{cx - size * 0.1:.1f} L{cx - size * 0.07:.1f} {y0 + size * 0.05:.1f} H{cx + size * 0.07:.1f} L{cx + size * 0.1:.1f} {y0:.1f} H{x1:.1f}"
    body.append(f'<path d="{d}" fill="none" stroke="{ink}" stroke-width="{size * 0.016:.1f}" stroke-linejoin="round" stroke-linecap="round"/>')
    return svg(size, size, body, "Cygnus mark: a transit and its light curve")


DEFAULT_SEED = 20260924


def transit_params(seed: int) -> dict:
    """The 'randomized' transit, reproducibly: chord angle, impact offset and planet position from a recorded seed.
    The angle is drawn uniformly from the two hard-diagonal bands (25-65 and 115-155 deg) so it always reads as a strike."""
    rnd = random.Random(seed)
    band = rnd.choice(((25.0, 65.0), (115.0, 155.0)))
    return {"seed": seed, "angle": round(rnd.uniform(*band), 1), "b": round(rnd.uniform(-0.1, 0.1), 3),
            "t": round(rnd.choice((-1, 1)) * rnd.uniform(0.45, 0.7), 3)}


def palette(ink: str, colour: bool) -> dict:
    if ink == INK_DARK:
        return {"bg": "#0b0f17", "ink": INK_DARK, "acc": ACCENT, "albireo": colour}
    if ink == NIGHT:
        return {"bg": "#140908", "ink": NIGHT, "acc": NIGHT, "albireo": False}
    if colour:
        return {"bg": "#f4f2ee", "ink": INK_LIGHT, "acc": "#b8741a", "albireo": True}
    return {"bg": INK_LIGHT, "ink": "#f4f2ee", "acc": "#f4f2ee", "albireo": False}  # one-colour: knocked out of a solid badge


def spike_star(x, y, r, fill, rot=0.0, waist=0.2):
    """A rigid four-point star: straight-edged diffraction spikes, the way a telescope renders a bright star."""
    pts = []
    for k in range(8):
        a = rot + k * math.pi / 4
        rr = r if k % 2 == 0 else r * waist
        pts.append(f"{x + rr * math.sin(a):.2f},{y - rr * math.cos(a):.2f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


def rigid_cross(pts, stars, size, cx, cy, c, star_scale=1.0):
    """The Northern Cross with spike stars and square-ended struts."""
    P = {k: (cx + x * size, cy + y * size) for k, (x, y) in pts.items()}
    R = lambda k: size * star_scale * (0.05 + 0.032 * max(0.0, 5.3 - stars[k]["V"]))
    out, lw = [], size * 0.034
    for a, b in LINES:
        (x1, y1), (x2, y2) = P[a], P[b]
        L = math.hypot(x2 - x1, y2 - y1)
        ga, gb = R(a) * 0.55 + size * 0.03, R(b) * 0.55 + size * 0.03
        x1, y1, x2, y2 = x1 + (x2 - x1) * ga / L, y1 + (y2 - y1) * ga / L, x2 - (x2 - x1) * gb / L, y2 - (y2 - y1) * gb / L
        out.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{c["ink"]}" stroke-width="{lw:.2f}" stroke-linecap="butt" opacity=".8"/>')
    for k, (x, y) in P.items():
        if k == "Albireo B":
            continue
        fill = bv_rgb(stars[k]["bv"]) if (c["albireo"] and k == "Albireo A") else c["ink"]
        out.append(spike_star(x, y, R(k), fill, waist=0.2 if stars[k]["V"] < 2.5 else 0.26))
    xa, ya = P["Albireo A"]
    rb = R("Albireo B") * 1.25
    fillb = bv_rgb(stars["Albireo B"]["bv"]) if c["albireo"] else c["ink"]
    out.append(spike_star(xa + R("Albireo A") * 0.7 + rb * 0.8, ya - rb * 0.25, rb, fillb, waist=0.3))
    return out


def concept_d(pts, stars, ink, colour=True, size=512, seed=DEFAULT_SEED):
    """D · Badged transit: the Northern Cross in a badge, struck through by a heavy transit bar that breaks the rim."""
    c = palette(ink, colour)
    tp = transit_params(seed)
    cx = cy = size / 2
    R = size * 0.4
    rim = size * 0.032
    body = [f'<circle cx="{cx}" cy="{cy}" r="{R:.2f}" fill="{c["bg"]}" stroke="{c["ink"]}" stroke-width="{rim:.2f}"/>']
    body += rigid_cross(pts, stars, size * 0.5, cx, cy, c)
    a = math.radians(tp["angle"])
    ux, uy = math.cos(a), -math.sin(a)
    nx, ny = -uy, ux
    ox, oy = cx + nx * tp["b"] * R, cy + ny * tp["b"] * R
    half, bw = size * 0.49, size * 0.078          # bar reaches past the rim almost to the canvas edge
    # the bar is a parallelogram with ends cut square to the canvas axis, for a hard, "slashed" look
    ex, ey = ux * half, uy * half
    px_, py_ = nx * bw / 2, ny * bw / 2
    cut = size * 0.03
    poly = [(ox - ex + px_, oy - ey + py_), (ox + ex + px_ - ux * cut, oy + ey + py_ - uy * cut),
            (ox + ex - px_, oy + ey - py_), (ox - ex - px_ + ux * cut, oy - ey - py_ + uy * cut)]
    ptxt = " ".join(f"{x:.2f},{y:.2f}" for x, y in poly)
    gap = size * 0.022
    halo = [(x + (nx if i in (0, 1) else -nx) * gap, y + (ny if i in (0, 1) else -ny) * gap) for i, (x, y) in enumerate(poly)]
    htxt = " ".join(f"{x:.2f},{y:.2f}" for x, y in halo)
    body += [f'<polygon points="{htxt}" fill="{c["bg"]}"/>', f'<polygon points="{ptxt}" fill="{c["acc"]}"/>']
    # the planet: a dark disc on the bar, in front of everything, with a hard rim
    t = tp["t"]                                    # signed distance along the bar, kept clear of Sadr at the centre
    qx, qy = ox + ux * R * t, oy + uy * R * t
    pr = size * 0.082
    body += [f'<circle cx="{qx:.2f}" cy="{qy:.2f}" r="{pr + gap:.2f}" fill="{c["bg"]}"/>',
             f'<circle cx="{qx:.2f}" cy="{qy:.2f}" r="{pr:.2f}" fill="{c["bg"]}" stroke="{c["acc"]}" stroke-width="{size * 0.026:.2f}"/>']
    title = f"Cygnus mark: the Northern Cross badged, struck by a transit at {tp['angle']} degrees (seed {seed})"
    return svg(size, size, body, title)


def lockup(mark_fn, pts, stars, ink, colour=True):
    """Mark plus wordmark, horizontal."""
    inner = mark_fn(pts, stars, ink, colour, size=160)
    inner = inner.split(">", 1)[1].rsplit("</svg>", 1)[0].split("</title>", 1)[1]
    body = [f'<g transform="translate(0 0)">{inner}</g>',
            f'<text x="176" y="98" font-family="{SANS}" font-size="58" font-weight="500" letter-spacing="14" fill="{ink}">CYGNUS</text>',
            f'<text x="178" y="126" font-family="{SANS}" font-size="15" letter-spacing="4.2" fill="{ink}" opacity=".6">ASTRONOMICAL DATA FORENSICS</text>']
    return svg(640, 160, body, "Cygnus logo lockup")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    stars = load()
    pts, rot = project(stars)
    concepts = [("d", "Northern Cross, badged, with a transit", concept_d,
                 f"The Northern Cross in its true catalogue shape, inside a round badge, struck through by a transit chord with a planet silhouette in front of the stars. The chord's angle, its offset from centre (an impact parameter) and the planet's place along it (kept clear of the central star) are drawn at random from a recorded seed ({DEFAULT_SEED}: {transit_params(DEFAULT_SEED)['angle']}°), so the mark is reproducible. Other seeds are shown below."),
                ("a", "Northern Cross", concept_a,
                 "The five bright stars of the Northern Cross in their true relative positions from the Yale Bright Star Catalogue, sized by magnitude. Albireo, the swan's head, is drawn as its gold-and-blue double from the catalogue colours of its two stars."),
                ("b", "Cross in a reticle", concept_b,
                 "The same asterism inside a measuring reticle: the sky, and the act of measuring it. Reads well as an app icon and favicon."),
                ("c", "Transit", concept_c,
                 "A planet crossing a star and the dip it makes in the light curve: the project's core measurement. Not tied to Cygnus the constellation.")]
    files = {}
    for key, name, fn, _ in concepts:
        for variant, ink, colour in (("dark", INK_DARK, True), ("light", INK_LIGHT, True), ("mono", INK_LIGHT, False), ("night", NIGHT, False)):
            f = OUT / f"mark-{key}-{variant}.svg"
            f.write_text(fn(pts, stars, ink, colour), encoding="utf-8")
            files[(key, variant)] = f.name
        (OUT / f"lockup-{key}-dark.svg").write_text(lockup(fn, pts, stars, INK_DARK), encoding="utf-8")
        (OUT / f"lockup-{key}-light.svg").write_text(lockup(fn, pts, stars, INK_LIGHT), encoding="utf-8")

    seeds = [DEFAULT_SEED + k for k in range(8)]
    for sd in seeds:
        (OUT / f"mark-d-seed{sd}.svg").write_text(concept_d(pts, stars, INK_DARK, True, seed=sd), encoding="utf-8")
    seed_grid = "".join(f'<figure class="dark seed"><img src="concepts/mark-d-seed{sd}.svg" alt="Seed {sd}"><figcaption>seed {sd} · {transit_params(sd)["angle"]}°</figcaption></figure>' for sd in seeds)
    cards = []
    for key, name, fn, text in concepts:
        cards.append(f"""
<section class="concept">
  <header><span class="k">{key.upper()}</span><h2>{html.escape(name)}</h2></header>
  <p>{html.escape(text)}</p>
  <div class="row">
    <figure class="big dark"><img src="concepts/mark-{key}-dark.svg" alt="{html.escape(name)} on dark"></figure>
    <figure class="big light"><img src="concepts/mark-{key}-light.svg" alt="{html.escape(name)} on light"></figure>
    <div class="small">
      <figure class="dark"><img src="concepts/mark-{key}-dark.svg" width="64" height="64" alt=""><figcaption>64</figcaption></figure>
      <figure class="dark"><img src="concepts/mark-{key}-dark.svg" width="32" height="32" alt=""><figcaption>32</figcaption></figure>
      <figure class="dark"><img src="concepts/mark-{key}-dark.svg" width="16" height="16" alt=""><figcaption>16</figcaption></figure>
      <figure class="light"><img src="concepts/mark-{key}-mono.svg" width="32" height="32" alt=""><figcaption>mono</figcaption></figure>
      <figure class="night"><img src="concepts/mark-{key}-night.svg" width="32" height="32" alt=""><figcaption>night</figcaption></figure>
    </div>
  </div>
  <figure class="lock dark"><img src="concepts/lockup-{key}-dark.svg" alt="{html.escape(name)} lockup on dark"></figure>
  <figure class="lock light"><img src="concepts/lockup-{key}-light.svg" alt="{html.escape(name)} lockup on light"></figure>
  {('<h3>Other seeds</h3><div class="seeds">' + seed_grid + '</div>') if key == 'd' else ''}
</section>""")
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cygnus Logo Concepts</title>
<style>
:root {{ --bg:#0b0f17; --ink:#ece7de; --ink2:#bdb6aa; --ink3:#8b857b; --line:rgba(236,231,222,.12); color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:15px/1.55 {SANS}; }}
main {{ max-width:1100px; margin:0 auto; padding:32px 20px 64px; }}
h1 {{ font:400 32px/1.15 'Source Serif 4',Charter,Georgia,serif; margin:0 0 6px; }}
.lead {{ color:var(--ink2); max-width:70ch; }}
.concept {{ border-top:1px solid var(--line); padding:28px 0 8px; margin-top:28px; }}
.concept header {{ display:flex; align-items:baseline; gap:12px; }}
.k {{ font:600 12px {SANS}; letter-spacing:.12em; color:var(--ink3); border:1px solid var(--line); border-radius:999px; padding:2px 9px; }}
h2 {{ font:400 24px/1.2 'Source Serif 4',Charter,Georgia,serif; margin:0; }}
.concept > p {{ color:var(--ink2); max-width:75ch; }}
.row {{ display:grid; grid-template-columns: 1fr 1fr auto; gap:14px; align-items:stretch; }}
figure {{ margin:0; border-radius:8px; display:grid; place-items:center; }}
.dark {{ background:#03050a; border:1px solid var(--line); }}
.light {{ background:#f4f2ee; }}
.night {{ background:#0c0706; border:1px solid var(--line); }}
.big img {{ width:100%; max-width:300px; height:auto; padding:18px; }}
.small {{ display:grid; grid-template-columns: repeat(2, 76px); gap:8px; align-content:start; }}
.small figure {{ height:76px; grid-template-rows: 1fr auto; padding-top:6px; }}
.small figcaption {{ font:11px {SANS}; color:var(--ink3); padding-bottom:4px; }}
.light figcaption {{ color:#5a554d; }}
.lock {{ margin-top:12px; padding:18px 24px; justify-items:start; }}
.lock img {{ width:100%; max-width:520px; height:auto; }}
.seeds {{ display:grid; grid-template-columns: repeat(4, 1fr); gap:10px; }}
.seed {{ padding:12px 8px 6px; }}
.seed img {{ width:100%; max-width:150px; height:auto; }}
.seed figcaption {{ font:11px {SANS}; color:var(--ink3); padding-top:4px; }}
h3 {{ font:600 11px {SANS}; letter-spacing:.12em; text-transform:uppercase; color:var(--ink3); margin:24px 0 10px; }}
.note {{ font-size:13px; color:var(--ink3); margin-top:36px; border-top:1px solid var(--line); padding-top:16px; }}
@media (max-width:760px) {{ .row {{ grid-template-columns:1fr 1fr; }} .small {{ grid-column:1 / -1; grid-template-columns:repeat(5, 1fr); }} }}
</style></head>
<body><main>
<h1>Cygnus logo concepts</h1>
<p class="lead">D is the chosen direction (Northern Cross, badged, with a transit); A–C are the earlier concepts, kept for comparison. A and B are built from the real positions and colours of the Northern Cross stars; C is built from the measurement the project makes. Each is shown on dark and light, at icon sizes (64, 32, 16 px), in one colour, in night-vision red, and as a lockup with the wordmark.</p>
{''.join(cards)}
<p class="note">Geometry: Yale Bright Star Catalogue positions (VizieR V/50), gnomonic projection about Sadr, east to the left, rotated {rot:.1f}° so Deneb sits above Albireo. Star sizes scale with V magnitude. Albireo A (B−V 1.13) and B (B−V −0.10) take their catalogue colours; their true 35″ separation is far below this scale, so B is drawn touching A as a signature. Wordmark set in IBM Plex Sans for the concept; the final mark would be outlined paths.</p>
</main></body></html>"""
    (HERE / "index.html").write_text(page, encoding="utf-8")
    print(f"wrote {len(list(OUT.glob('*.svg')))} svgs; rotation {rot:.1f} deg")


if __name__ == "__main__":
    main()

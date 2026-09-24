"""Build the data bundle for the sky-explorer prototype (design-system/mockups/explorer/).

Inputs, all recorded files:

* target positions      docs/tier1_pack/NAME_RESOLUTIONS.json   (project, CDS Sesame)
* study footprints      docs/tier1_pack/MASTER_MANIFEST.csv     (project; parsed from each query as recorded)
* target categories     docs/tier1_pack/RUN_CONFIG.json         (project)
* analyses              every sky_record.json under campaigns/ and reports/ (cygnus.skyrecord)
* background sky, star fields, planet parameters, survey images: data/ (see fetch_sky_data.py and
  data/PROVENANCE.json)

Where a footprint cannot be parsed from the recorded query it is listed without a shape rather than
guessed. Run:  python design-system/mockups/build_explorer.py
"""

from __future__ import annotations

import csv
import json
import math
import re
import shutil
from pathlib import Path

import numpy as np

import build_mockups as bm

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from cygnus import skyrecord  # noqa: E402

HERE = Path(__file__).resolve().parent
WT = HERE.parents[1]
DATA = HERE / "data"
OUT = HERE / "explorer"
PACK = WT / "docs" / "tier1_pack"

SVC = {
    "mast": "MAST", "gaia": "ESA Gaia", "skyview": "NASA SkyView", "cds": "CDS",
    "ned": "NED", "eso": "ESO", "irsa": "IRSA", "legacysurvey": "Legacy Surveys",
}

CONST = {
    "And": "Andromeda", "Ant": "Antlia", "Aps": "Apus", "Aqr": "Aquarius", "Aql": "Aquila", "Ara": "Ara",
    "Ari": "Aries", "Aur": "Auriga", "Boo": "Boötes", "Cae": "Caelum", "Cam": "Camelopardalis", "Cnc": "Cancer",
    "CVn": "Canes Venatici", "CMa": "Canis Major", "CMi": "Canis Minor", "Cap": "Capricornus", "Car": "Carina",
    "Cas": "Cassiopeia", "Cen": "Centaurus", "Cep": "Cepheus", "Cet": "Cetus", "Cha": "Chamaeleon",
    "Cir": "Circinus", "Col": "Columba", "Com": "Coma Berenices", "CrA": "Corona Australis",
    "CrB": "Corona Borealis", "Crv": "Corvus", "Crt": "Crater", "Cru": "Crux", "Cyg": "Cygnus",
    "Del": "Delphinus", "Dor": "Dorado", "Dra": "Draco", "Equ": "Equuleus", "Eri": "Eridanus", "For": "Fornax",
    "Gem": "Gemini", "Gru": "Grus", "Her": "Hercules", "Hor": "Horologium", "Hya": "Hydra", "Hyi": "Hydrus",
    "Ind": "Indus", "Lac": "Lacerta", "Leo": "Leo", "LMi": "Leo Minor", "Lep": "Lepus", "Lib": "Libra",
    "Lup": "Lupus", "Lyn": "Lynx", "Lyr": "Lyra", "Men": "Mensa", "Mic": "Microscopium", "Mon": "Monoceros",
    "Mus": "Musca", "Nor": "Norma", "Oct": "Octans", "Oph": "Ophiuchus", "Ori": "Orion", "Pav": "Pavo",
    "Peg": "Pegasus", "Per": "Perseus", "Phe": "Phoenix", "Pic": "Pictor", "Psc": "Pisces",
    "PsA": "Piscis Austrinus", "Pup": "Puppis", "Pyx": "Pyxis", "Ret": "Reticulum", "Sge": "Sagitta",
    "Sgr": "Sagittarius", "Sco": "Scorpius", "Scl": "Sculptor", "Sct": "Scutum", "Ser": "Serpens",
    "Sex": "Sextans", "Tau": "Taurus", "Tel": "Telescopium", "Tri": "Triangulum", "TrA": "Triangulum Australe",
    "Tuc": "Tucana", "UMa": "Ursa Major", "UMi": "Ursa Minor", "Vel": "Vela", "Vir": "Virgo", "Vol": "Volans",
    "Vul": "Vulpecula",
}
GREEK = {"Alp": "α", "Bet": "β", "Gam": "γ", "Del": "δ", "Eps": "ε", "Zet": "ζ", "Eta": "η", "The": "θ",
         "Iot": "ι", "Kap": "κ", "Lam": "λ", "Mu": "μ", "Nu": "ν", "Xi": "ξ", "Omi": "ο", "Pi": "π", "Rho": "ρ",
         "Sig": "σ", "Tau": "τ", "Ups": "υ", "Phi": "φ", "Chi": "χ", "Psi": "ψ", "Ome": "ω"}


def slug(name: str) -> str:
    return re.sub(r"-+", "-", "".join(c.lower() if c.isalnum() else "-" for c in name)).strip("-")


def fnum(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


# ------------------------------------------------------------------ background sky
def load_bsc() -> tuple[list, list]:
    stars, by_const = [], {}
    for r in csv.DictReader((DATA / "bsc5.csv").open(encoding="utf-8")):
        ra, dec, v = fnum(r["RAJ2000"]), fnum(r["DEJ2000"]), fnum(r["Vmag"])
        if ra is None or dec is None or v is None:
            continue
        bv = fnum(r["B-V"])
        name = (r["Name"] or "").strip()
        m = re.match(r"^(\d*)\s*([A-Z][a-z]{1,2})?\s*(\d?)\s*([A-Z][A-Za-z]{2})$", name)
        label, const = "", None
        if m:
            const = m.group(4)
            if m.group(2) in GREEK:
                label = GREEK[m.group(2)] + (m.group(3) or "") + " " + const
            elif m.group(1):
                label = m.group(1) + " " + const
        if const in CONST:
            by_const.setdefault(const, []).append((ra, dec, v))
        stars.append([round(ra, 4), round(dec, 4), round(v, 2), None if bv is None else round(bv, 2),
                      label if v < 4.0 else ""])
    consts = []
    for c, pts in by_const.items():
        w = np.array([10 ** (-0.4 * p[2]) for p in pts])
        ra, dec = np.radians([p[0] for p in pts]), np.radians([p[1] for p in pts])
        vec = np.array([np.cos(dec) * np.cos(ra), np.cos(dec) * np.sin(ra), np.sin(dec)]) @ w
        vec /= np.linalg.norm(vec)
        consts.append([c, CONST[c], round(math.degrees(math.atan2(vec[1], vec[0])) % 360, 2),
                       round(math.degrees(math.asin(vec[2])), 2)])
    return stars, consts


def load_density() -> list:
    f = next(DATA.glob("gaia_density_hpx5_*.csv"), None)
    if not f:
        return []
    out = []
    for r in csv.DictReader(f.open(encoding="utf-8")):
        x, y, z, n = map(float, (r["x"], r["y"], r["z"], r["n"]))
        nrm = math.sqrt(x * x + y * y + z * z)
        out.append([round(math.degrees(math.atan2(y, x)) % 360, 3), round(math.degrees(math.asin(z / nrm)), 3), int(n)])
    return out


# ------------------------------------------------------------------ footprints
def parse_footprint(row: dict, anchors: dict) -> dict | None:
    """Return the sky shape a manifest row's recorded query covered, or None when not position-bounded."""
    q, pid = row["query"], row["product_id"]
    try:
        qj = json.loads(q) if q.strip().startswith("{") else {}
    except json.JSONDecodeError:
        qj = {}
    ex = json.loads(row["extra_json"] or "{}")
    filt = qj.get("filters", {}) if isinstance(qj.get("filters"), dict) else {}
    if "coordinates" in filt and "radius_deg" in filt:
        (ra, dec), r = filt["coordinates"], float(filt["radius_deg"])
        what = f"{filt.get('obs_collection', '')} {filt.get('dataproduct_type', '')} cone".strip()
        return {"shape": "circle", "ra": ra, "dec": dec, "r": r, "what": what}
    if "resolved_ra_dec" in qj and "size_px" in qj:  # TESScut: 21 arcsec pixels
        ra, dec = qj["resolved_ra_dec"]
        s = qj["size_px"] * 21.0 / 3600
        return {"shape": "box", "ra": ra, "dec": dec, "w": s, "h": s, "what": f"TESS FFI cutout, sector {qj.get('sector')}, {qj['size_px']} px"}
    if isinstance(qj.get("radius_deg"), (int, float)) and "resolved_ra_dec" in qj:
        ra, dec = qj["resolved_ra_dec"]
        return {"shape": "circle", "ra": ra, "dec": dec, "r": float(qj["radius_deg"]),
                "what": f"{qj.get('obs_collection', '')} {qj.get('dataproduct_type', '')} cone".strip()}
    m = re.search(r"CIRCLE\('(?:ICRS|J2000)',\s*([-\d.]+),\s*([-\d.]+),\s*([-\d.]+)\)", q)
    if m:
        what = "Gaia DR3 source cone" if row["service"] == "gaia" else "AllWISE source cone"
        return {"shape": "circle", "ra": float(m.group(1)), "dec": float(m.group(2)), "r": float(m.group(3)), "what": what}
    m = re.search(r"position=([-\d.]+) ([-\d.]+), survey='([^']+)'.*size=([\d.]+)deg", row["url"])
    if m:
        s = float(m.group(4))
        return {"shape": "box", "ra": float(m.group(1)), "dec": float(m.group(2)), "w": s, "h": s, "what": f"SkyView {m.group(3)} cutout"}
    field = ex.get("field") or qj.get("field")
    m = re.search(r"within ([\d.]+) deg", q)
    if m and row["service"] == "irsa":
        fname = re.search(r"ztf_lc_(.+?)_\d+as", pid)
        a = anchors.get(fname.group(1).replace("_", " ")) if fname else None
        if a:
            return {"shape": "circle", "ra": a[0], "dec": a[1], "r": float(m.group(1)), "what": "ZTF light-curve cone"}
    m = re.search(r"([\d.]+)x([\d.]+) deg box around Sesame-resolved (.+?) \(", q)
    if m and m.group(3) in anchors:
        a = anchors[m.group(3)]
        return {"shape": "box", "ra": a[0], "dec": a[1], "w": float(m.group(1)), "h": float(m.group(2)), "what": "Legacy Surveys brick search box"}
    m = re.search(r"tractor_dr\d+_\w+?_(\d{4})([pm])(\d{3})$", pid)
    if m:  # Legacy Surveys brick names encode the brick centre; bricks are nominally 0.25 deg square
        dec = int(m.group(3)) / 10 * (1 if m.group(2) == "p" else -1)
        return {"shape": "box", "ra": int(m.group(1)) / 10, "dec": dec, "w": 0.25, "h": 0.25,
                "what": "Legacy Surveys Tractor brick (centre from brick name, nominal 0.25° square)"}
    m = re.search(r"Sesame-resolved (.+?); pixscale ([\d.]+) as; (?:size )?(\d+) px", q)
    if m and m.group(1) in anchors:
        a = anchors[m.group(1)]
        s = float(m.group(2)) * int(m.group(3)) / 3600
        return {"shape": "box", "ra": a[0], "dec": a[1], "w": s, "h": s, "what": "Legacy Surveys image cutout"}
    return None


def target_of(row: dict, names: list[str]) -> str | None:
    ex = json.loads(row["extra_json"] or "{}")
    blob = " ".join(str(ex.get(k, "")) for k in ("tag", "field", "field_name", "target")) + " " + row["product_id"] + " " + row["query"]
    for n in sorted(names, key=len, reverse=True):
        if re.search(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", blob) or n.replace(" ", "_") in row["product_id"]:
            return n
    return None


def sep_deg(a, b) -> float:
    ra1, d1, ra2, d2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    c = math.sin(d1) * math.sin(d2) + math.cos(d1) * math.cos(d2) * math.cos(ra1 - ra2)
    return math.degrees(math.acos(max(-1, min(1, c))))


# ------------------------------------------------------------------ renditions
def planets_by_host() -> dict:
    out: dict = {}
    f = DATA / "planets_pscomppars.csv"
    if not f.exists():
        return out
    for r in csv.DictReader(f.open(encoding="utf-8")):
        ref = re.search(r"refstr=(\S+) href=(\S+?)[ >]", r["pl_orbper_reflink"] or "")
        out.setdefault(r["hostname"], {"star": {k: fnum(r[k]) for k in ("st_teff", "st_rad", "st_mass", "sy_dist")} | {"spt": r["st_spectype"] or None},
                                       "planets": []})["planets"].append({
            "name": r["pl_name"], "P": fnum(r["pl_orbper"]), "a": fnum(r["pl_orbsmax"]), "rade": fnum(r["pl_rade"]),
            "mass_e": fnum(r["pl_bmasse"]), "e": fnum(r["pl_orbeccen"]), "teq": fnum(r["pl_eqt"]),
            "year": r["disc_year"], "method": r["discoverymethod"], "transits": r.get("tran_flag") == "1",
            "ref": ref.group(1).replace("_", " ").replace("  ", " ") if ref else None, "ref_url": ref.group(2) if ref else None,
        })
    return out


def field_stars(name: str) -> dict | None:
    f = DATA / f"field_{slug(name)}.csv"
    if not f.exists():
        return None
    ra, dec, g, c, t = [], [], [], [], []
    rows = list(csv.DictReader(f.open(encoding="utf-8")))
    for r in rows:
        ra.append(round(float(r["ra"]), 6)); dec.append(round(float(r["dec"]), 6)); g.append(round(float(r["g"]), 2))
        c.append(None if not r["bp_rp"] else round(float(r["bp_rp"]), 3)); t.append(None if not r["teff_gspphot"] else round(float(r["teff_gspphot"])))
    return {"ra": ra, "dec": dec, "g": g, "bp_rp": c, "teff": t, "plx": [fnum(r["parallax"]) for r in rows],
            "pmra": [fnum(r["pmra"]) for r in rows], "pmdec": [fnum(r["pmdec"]) for r in rows]}


def central_star(fs: dict, pos: tuple) -> dict | None:
    """Brightest Gaia source within 3 arcsec of the Sesame position after moving it from J2016.0 to J2000.0."""
    best = None
    for i in range(len(fs["ra"])):
        pmra, pmdec = fs["pmra"][i] or 0.0, fs["pmdec"][i] or 0.0
        dec0 = fs["dec"][i] - pmdec * 16.0 / 3.6e6
        ra0 = fs["ra"][i] - pmra * 16.0 / 3.6e6 / math.cos(math.radians(fs["dec"][i]))
        d = sep_deg(pos, (ra0, dec0)) * 3600
        if d < 3 and (best is None or fs["g"][i] < fs["g"][best[0]]):
            best = (i, d)
    if best is None:
        return None
    i, d = best
    return {"g": fs["g"][i], "bp_rp": fs["bp_rp"][i], "teff": fs["teff"][i], "plx": fs["plx"][i], "pmra": fs["pmra"][i],
            "pmdec": fs["pmdec"][i], "ra2016": fs["ra"][i], "dec2016": fs["dec"][i], "sep_j2000_arcsec": round(d, 2)}


def plot_svg(pd: dict) -> str:
    """Render one sky-record plot (numbers from cygnus.skyrecord.plot_data) as SVG, any target."""
    if pd["type"] == "timeseries":
        bx, by = zip(*pd["bins"])
        t0, t1 = pd["t_range"]
        lo, hi = min(by), max(by)
        pad = (hi - lo) * 0.08 or 0.001
        def body(X, Y, ml, mt):
            return '<path class="pts" d="' + "".join(f"M{X(a) - ml:.1f} {Y(b) - mt:.1f}h0.01" for a, b in zip(bx, by)) + '"/>'
        step = 5 if t1 - t0 > 12 else 2
        ticks = list(range(int(math.ceil(t0 / step) * step), int(t1) + 1, step))
        off = pd.get("time_offset_bjd")
        xl = f"{pd['time_col']} (BJD − {off:.0f}), days" if off else f"{pd['time_col']}, days"
        yt = [round(v, 3) for v in np.linspace(lo, hi, 4)]
        g = bm.axes_svg(720, 230, (t0 - 0.3, t1 + 0.3), (lo - pad, hi + pad), xl, "Relative flux", ticks, yt, body)
        return f'<svg class="plot" viewBox="0 0 720 230" role="img" aria-label="{pd["label"]}">' + "".join(g) + "</svg>"
    win = pd["window_hours"]
    raw, bins = pd["raw"], pd["bins"]
    fl = [b for _, b in raw]
    lo, hi = float(np.percentile(fl, 0.5)), float(np.percentile(fl, 99.5))
    pad = (hi - lo) * 0.1
    def body(X, Y, ml, mt):
        out = ""
        if pd.get("veto_phase"):
            v = pd["veto_phase"] * pd["period_days"] * 24
            out += f'<rect class="veto" x="{X(-v) - ml:.1f}" y="0" width="{X(v) - X(-v):.1f}" height="400"/>'
        out += '<path class="raw" d="' + "".join(f"M{X(a) - ml:.1f} {Y(b) - mt:.1f}h0.01" for a, b in raw) + '"/>'
        out += '<path class="pts pts-bin" d="' + "".join(f"M{X(a) - ml:.1f} {Y(b) - mt:.1f}h0.01" for a, b in bins) + '"/>'
        return out
    xt = [v for v in range(-int(win), int(win) + 1) if v % 2 == 0]
    yt = [round(v, 3) for v in np.linspace(lo, hi, 4)]
    g = bm.axes_svg(440, 250, (-win, win), (lo - pad, hi + pad), "Hours from mid-transit (declared ephemeris)",
                    "Relative flux", xt, yt, body)
    return f'<svg class="plot" viewBox="0 0 440 250" role="img" aria-label="{pd["label"]}">' + "".join(g) + "</svg>"


def record_for_site(r: dict) -> dict:
    keep = ("id", "title", "kind", "status", "outcome", "evidence", "date", "summary", "spec", "report", "search_log",
            "checks", "products", "_path")
    out = {k: r.get(k) for k in keep}
    out["plots"] = []
    for pd in r.get("plot_data", []):
        item = {"type": pd["type"], "label": pd["label"], "file": pd["file"], "n": pd["n"], "svg": plot_svg(pd)}
        if pd["type"] == "fold":
            item.update(period_days=pd["period_days"], t0_bjd=pd["t0_bjd"], veto_phase=pd.get("veto_phase"))
            if pd.get("depth"):
                item["depth"] = {**pd["depth"], "value": round(pd["depth"]["value"], 5)}
        out["plots"].append(item)
    return out


# ------------------------------------------------------------------ build
def build() -> None:
    (OUT / "data" / "fields").mkdir(parents=True, exist_ok=True)
    (OUT / "img").mkdir(exist_ok=True)
    prov = json.loads((DATA / "PROVENANCE.json").read_text(encoding="utf-8"))
    res = json.loads((PACK / "NAME_RESOLUTIONS.json").read_text(encoding="utf-8"))
    cfg = json.loads((PACK / "RUN_CONFIG.json").read_text(encoding="utf-8"))
    rows = list(csv.DictReader((PACK / "MASTER_MANIFEST.csv").open(encoding="utf-8")))
    anchors = {k: (v["ra_deg"], v["dec_deg"]) for k, v in res.items() if v.get("ok")}
    names = list(anchors)
    systems = planets_by_host()
    from fetch_sky_data import EXO_HOSTS, FIELD_RADIUS, DEFAULT_RADIUS

    targets = {n: {"name": n, "id": slug(n), "ra": anchors[n][0], "dec": anchors[n][1], "resolved": res[n]["resolved_utc"],
                   "frame": res[n]["frame"], "resolver": res[n]["resolver"],
                   "cat": "field" if n in cfg["field_names"] else "tess" if n in cfg["tess_target_names"]
                   else "bench" if n in cfg["bench_object_names"] else "other",
                   "patches": {}, "unshaped": [], "counts": {}} for n in names}
    unassigned = []
    for row in rows:
        fp = parse_footprint(row, anchors)
        t = target_of(row, names)
        if t is None and fp:  # attach by position when the row names no target
            near = min(names, key=lambda n: sep_deg(anchors[n], (fp["ra"], fp["dec"])))
            t = near if sep_deg(anchors[near], (fp["ra"], fp["dec"])) < max(0.1, fp.get("r", fp.get("w", 0))) else None
        if t is None:
            unassigned.append({"svc": row["service"], "id": row["product_id"], "state": row["state"]})
            continue
        T = targets[t]
        T["counts"][row["state"]] = T["counts"].get(row["state"], 0) + 1
        if fp is None:
            T["unshaped"].append({"svc": row["service"], "id": row["product_id"], "state": row["state"]})
            continue
        key = (row["service"], fp["shape"], round(fp["ra"], 5), round(fp["dec"], 5), round(fp.get("r", fp.get("w", 0)), 6), fp["what"])
        p = T["patches"].setdefault(key, {"svc": row["service"], **{k: (round(v, 7) if isinstance(v, float) else v) for k, v in fp.items()},
                                          "products": [], "states": {}})
        p["products"].append(row["product_id"])
        p["states"][row["state"]] = p["states"].get(row["state"], 0) + 1

    # analyses: every sky_record.json in the worktree (cygnus.skyrecord), no per-target code
    col = skyrecord.collect(WT)
    for n, pos in col["extra_positions"].items():
        targets[n] = {"name": n, "id": slug(n), "ra": pos["ra_deg"], "dec": pos["dec_deg"], "resolved": None,
                      "frame": f"{pos['frame']} ({pos['epoch']})", "resolver": pos["position_source"], "cat": "analysis",
                      "patches": {}, "unshaped": [], "counts": {}}
        anchors[n] = (pos["ra_deg"], pos["dec_deg"])
    field_prov = {k: v for k, v in prov.items() if k.startswith("field_")}
    out_targets = []
    for n, T in targets.items():
        T["patches"] = sorted(T["patches"].values(), key=lambda p: -(p.get("r") or p.get("w") or 0))
        fs = field_stars(n)
        if fs:
            fn = f"data/fields/{T['id']}.json"
            (OUT / fn).write_text(json.dumps({k: fs[k] for k in ("ra", "dec", "g", "bp_rp")}, separators=(",", ":")), encoding="utf-8")
            fp_ = field_prov.get(f"field_{slug(n)}.csv", {})
            T["field"] = {"file": fn, "n": len(fs["ra"]), "radius": fp_.get("radius_deg"), "gmax": fp_.get("g_max"),
                          "query": fp_.get("query"), "retrieved": fp_.get("retrieved_utc")}
            if T["cat"] in ("tess", "bench") and not re.match(r"(NGC|M)\s?\d", n):
                T["central"] = central_star(fs, anchors[n])
        img = DATA / "fields" / f"{T['id']}.jpg"
        if img.exists():
            shutil.copyfile(img, OUT / "img" / img.name)
            ip = prov.get(f"fields/{img.name}", {})
            T["image"] = {"file": f"img/{img.name}", "fov": ip.get("fov_deg"), "source": ip.get("source"), "terms": ip.get("terms"),
                          "retrieved": ip.get("retrieved_utc")}
        host = EXO_HOSTS.get(n)
        if host and host in systems:
            T["system"] = {"host": host, **systems[host]}
        elif host:
            T["system_note"] = f"No planets for host name “{host}” in the NASA Exoplanet Archive pscomppars table on the fetch date."
        recs = col["by_target"].get(n, [])
        if recs:
            T["records"] = [record_for_site(r) for r in recs]
        st = T["counts"]
        done = any(r["status"] == "completed" for r in recs)
        T["status"] = "analysed" if done else "planned" if recs else ("retrieved" if st.get("drive_only") else ("failed" if st else "resolved"))
        out_targets.append(T)

    stars, consts = load_bsc()
    sky = {
        "generated_from": ["docs/tier1_pack/NAME_RESOLUTIONS.json", "docs/tier1_pack/MASTER_MANIFEST.csv",
                           "docs/tier1_pack/RUN_CONFIG.json", "design-system/mockups/data/PROVENANCE.json"],
        "provenance": {k: {kk: vv for kk, vv in v.items() if kk in ("source", "retrieved_utc", "rows", "terms", "note", "query", "endpoint")}
                       for k, v in prov.items() if not k.startswith(("field_", "fields/", "FAILED"))},
        "manifest_rows": len(rows), "unassigned": unassigned,
        "campaigns": [record_for_site(r) for r in col["records"] if not r["targets"]] ,
        "record_count": len(col["records"]),
        "services": SVC, "stars": stars, "consts": consts, "mw": load_density(), "targets": out_targets,
    }
    (OUT / "data" / "sky.json").write_text(json.dumps(sky, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    np_ = sum(len(t["patches"]) for t in out_targets)
    print(f"targets {len(out_targets)}, patches {np_}, unshaped {sum(len(t['unshaped']) for t in out_targets)}, "
          f"unassigned {len(unassigned)}, stars {len(stars)}, mw cells {len(sky['mw'])}")


if __name__ == "__main__":
    build()

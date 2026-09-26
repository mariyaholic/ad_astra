"""Lead vetting for known-object campaigns: ``python -m cygnus.campaign vet campaigns/<slug>.yaml``.

Runs after ``run`` on a campaign whose ``period_aliases`` step found repeat candidates (or on any
campaign, to vet its persistent screen events). It adds the artifact and consistency tests the
screen itself does not make, each marked passed / failed / inconclusive / not_tested per event:

* **sibling ephemerides**: every TOI on the same TIC (NASA Exoplanet Archive ``toi`` table), and
  the target itself if it has since gained a period: does a predicted transit fall on the event?
* **shape**: box fit (quadratic baseline) of the event and of the catalogued (reference) transit:
  depth, duration, mid-time; ratios with uncertainties, and a V-shape index (inner-half depth /
  outer-half depth).
* **detrending alternatives**: event depth under running medians (0.5, 1, 2 d, event masked) and
  local polynomials (order 1–3), PDCSAP and SAP.
* **red-noise significance**: the same box statistic at random epochs in the same light curve
  gives an empirical false-alarm distribution; also for background, centroids and pointing.
* **quality flags** in and around the event (momentum dumps, scattered light, …).
* **difference image** from the SPOC target pixel file: out-of-transit minus in-transit, its
  centroid against the target's position, and against the reference transit's difference image.
* **Gaia neighbours** within 2.5 TESS pixels bright enough to produce the depth if fully eclipsed.
* **common mode**: other SPOC 120-s light curves on the same camera and CCD in the same sector,
  measured at the event time.
* **stellar density**: for each period alias still allowed, the longest central-transit duration
  for a circular orbit; an event longer than that disfavours the alias.

It writes ``campaigns/<slug>/vetting/vetting.json``, ``VETTING.md`` and one figure per event, and
records a ledger run (script ``cygnus.campaign:<id>:lead_vetting``). It never changes the record's
outcome or evidence level: the reviewer reads the results.
"""

from __future__ import annotations

import csv
import io
import json
import math
from pathlib import Path

import numpy as np

from .lightcurve import robust_sigma
from .steps import resolve

EXO_TAP = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"
TESS_PIX_ARCSEC = 21.0
G_SI, RSUN, MSUN = 6.674e-11, 6.957e8, 1.989e30
QUALITY_BITS = {1: "attitude tweak", 2: "safe mode", 4: "coarse point", 8: "earth point", 16: "argabrightening",
                32: "momentum dump", 64: "aperture cosmic", 128: "manual exclude", 256: "discontinuity",
                512: "impulsive outlier", 1024: "collateral cosmic", 2048: "scattered light", 4096: "scattered light 2",
                8192: "planet-search exclude", 16384: "bad calibration", 32768: "insufficient targets"}


# ------------------------------------------------------------------ data
class LC:
    """A SPOC light curve with the engineering columns the vetting needs (normalised fluxes)."""

    def __init__(self, path: Path):
        from astropy.io import fits

        with fits.open(path, memmap=False) as h:
            d, hd0, hd1 = h[1].data, h[0].header, h[1].header
            self.t = np.asarray(d["TIME"], float) + float(hd1.get("BJDREFI", 0)) + float(hd1.get("BJDREFF", 0))
            self.q = np.asarray(d["QUALITY"], int)
            cols = set(d.names)
            self.col = {n: np.asarray(d[n], float) for n in ("SAP_FLUX", "PDCSAP_FLUX", "PDCSAP_FLUX_ERR", "SAP_BKG",
                                                              "MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2") if n in cols}
            self.sector, self.camera, self.ccd = hd0.get("SECTOR"), hd0.get("CAMERA"), hd0.get("CCD")
            self.ra, self.dec, self.tmag = hd0.get("RA_OBJ"), hd0.get("DEC_OBJ"), hd0.get("TESSMAG")
        self.ok = np.isfinite(self.t) & (self.q == 0) & np.isfinite(self.col["PDCSAP_FLUX"]) & np.isfinite(self.col["SAP_FLUX"])
        for n in ("SAP_FLUX", "PDCSAP_FLUX"):
            scale = np.nanmedian(self.col[n][self.ok])
            self.col[n] = self.col[n] / scale
            if n == "PDCSAP_FLUX" and "PDCSAP_FLUX_ERR" in self.col:
                self.col["PDCSAP_FLUX_ERR"] = self.col["PDCSAP_FLUX_ERR"] / scale   # errors in the same normalised units


def _box(t, tmid, dur):
    return np.abs(t - tmid) <= dur / 2


def box_fit(t, y, tguess, dur_guess, half_window, search_hours=None, yerr=None):
    """Grid search over mid-time and duration; per grid point a linear least-squares fit of
    quadratic baseline + box depth. Returns depth (positive = dip), its error, mid, duration,
    χ² improvement over the baseline-only fit, and a V-shape index.

    With per-cadence errors ``yerr`` (e.g. PDCSAP_FLUX_ERR) the best box is refitted by weighted
    least squares and ``weighted`` reports that depth, its formal error, the reduced χ², and the
    ratio of the robust residual scatter to the median quoted error (1 when the pipeline errors
    describe the scatter; > 1 when they understate it). The unweighted fit is unchanged.
    """
    sel = np.isfinite(y) & (np.abs(t - tguess) <= half_window)
    if yerr is not None:
        yerr = np.asarray(yerr, float)
        sel &= np.isfinite(yerr) & (yerr > 0)
        yerr = yerr[sel]
    t, y = t[sel], y[sel]
    if t.size < 20:
        return None
    x = t - tguess
    base = np.vstack([np.ones_like(x), x, x * x]).T
    c0, *_ = np.linalg.lstsq(base, y, rcond=None)
    sig = robust_sigma(y - base @ c0)
    chi0 = float(np.sum(((y - base @ c0) / sig) ** 2))
    search = (search_hours or max(1.0, dur_guess * 24)) / 24
    best = None
    for dur in np.clip(dur_guess * np.array([0.35, 0.5, 0.65, 0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0]), 0.5 / 24, half_window):
        for tm in np.arange(tguess - search, tguess + search + 1e-9, 5 / 1440):
            b = _box(t, tm, dur).astype(float)
            if b.sum() < 4:
                continue
            A = np.column_stack([base, -b])
            c, *_ = np.linalg.lstsq(A, y, rcond=None)
            chi = float(np.sum(((y - A @ c) / sig) ** 2))
            if best is None or chi < best[0]:
                best = (chi, tm, dur, c, A)
    if best is None:
        return None
    chi, tm, dur, c, A = best
    cov = np.linalg.pinv(A.T @ A) * sig ** 2 * max(1.0, chi / max(1, len(y) - 5))
    inb = _box(t, tm, dur)
    resid = y - A[:, :3] @ c[:3]
    inner = np.abs(t - tm) <= dur / 4
    outer = inb & ~inner
    vshape = (float(-np.median(resid[inner])) / float(-np.median(resid[outer]))
              if inner.sum() >= 2 and outer.sum() >= 2 and np.median(resid[outer]) < 0 else None)
    out = {"mid_bjd": float(tm), "duration_h": float(dur * 24), "depth_ppm": float(c[3] * 1e6),
           "depth_err_ppm": float(math.sqrt(cov[3, 3]) * 1e6), "delta_chi2": float(chi0 - chi),
           "n_in": int(inb.sum()), "vshape_index": vshape, "sigma_ppm": float(sig * 1e6)}
    if yerr is not None and yerr.size == y.size:
        w = 1 / yerr ** 2
        Aw = A * np.sqrt(w)[:, None]
        cw, *_ = np.linalg.lstsq(Aw, y * np.sqrt(w), rcond=None)
        covw = np.linalg.pinv(Aw.T @ Aw)
        rw = y - A @ cw
        dof = max(1, y.size - A.shape[1])
        chi2r = float(np.sum(w * rw ** 2) / dof)
        out["weighted"] = {"depth_ppm": float(cw[3] * 1e6), "depth_err_formal_ppm": float(math.sqrt(covw[3, 3]) * 1e6),
                           "depth_err_scaled_ppm": float(math.sqrt(covw[3, 3] * max(1.0, chi2r)) * 1e6),
                           "chi2_reduced": chi2r,
                           "scatter_over_quoted_error": float(robust_sigma(rw) / np.median(yerr)),
                           "errors": "PDCSAP_FLUX_ERR (pipeline), normalised with the flux"}
    return out


def alt_depths(lc: LC, tmid, dur, half_window):
    """Mean in-box residual under several detrendings, the event itself masked from each baseline."""
    from scipy.ndimage import median_filter

    out = {}
    t, ok = lc.t, lc.ok
    inb = _box(t, tmid, dur)
    for flux in ("PDCSAP_FLUX", "SAP_FLUX"):
        y = lc.col[flux]
        good = ok & np.isfinite(y)
        near = good & (np.abs(t - tmid) <= half_window)
        for order in (1, 2, 3):
            fit = near & ~inb
            if fit.sum() < 20 or (near & inb).sum() < 3:
                continue
            x = t - tmid
            c = np.polyfit(x[fit], y[fit], order)
            r = y / np.polyval(c, x) - 1
            out[f"{flux.split('_')[0]} poly{order}"] = float(-np.mean(r[near & inb]) * 1e6)
        idx = np.arange(t.size)
        base_ok = good & ~inb
        if base_ok.sum() < 50:
            continue
        filled = np.interp(idx, idx[base_ok], y[base_ok])
        for days in (0.5, 1.0, 2.0):
            w = max(3, int(round(days * 86400 / 120))) | 1
            r = y / median_filter(filled, size=w, mode="nearest") - 1
            if (good & inb).sum() >= 3:
                out[f"{flux.split('_')[0]} median {days:g} d"] = float(-np.mean(r[good & inb]) * 1e6)
    vals = [v for k, v in out.items() if k.startswith("PDCSAP")]
    return out, (float(np.min(vals)), float(np.max(vals))) if vals else None


def _shift(t, y, ok, tmid, dur, half_window):
    """In-box mean minus a quadratic out-of-box baseline (same units as y)."""
    near = ok & np.isfinite(y) & (np.abs(t - tmid) <= half_window)
    inb = near & _box(t, tmid, dur)
    fit = near & ~inb
    if inb.sum() < 3 or fit.sum() < 20:
        return None
    x = t - tmid
    c = np.polyfit(x[fit], y[fit], 2)
    return float(np.mean(y[inb] - np.polyval(c, x[inb])))


def empirical(lc: LC, series: dict, tmid, dur, half_window, exclude, n=300, seed=0):
    """Each series' in-box shift at the event, and its distribution at random epochs of the same
    light curve (avoiding ``exclude`` times); z = (event − median) / robust σ of the random shifts."""
    rng = np.random.default_rng(seed)
    t, ok = lc.t, lc.ok
    lo, hi = np.nanmin(t[ok]) + half_window, np.nanmax(t[ok]) - half_window
    trials = []
    for _ in range(n * 4):
        if len(trials) >= n:
            break
        tc = rng.uniform(lo, hi)
        if any(abs(tc - e) < half_window + dur for e in exclude):
            continue
        if (ok & _box(t, tc, dur)).sum() < max(3, 0.5 * dur * 86400 / 120):
            continue
        trials.append(tc)
    out = {}
    for name, y in series.items():
        ev = _shift(t, y, ok, tmid, dur, half_window)
        rnd = np.array([s for s in (_shift(t, y, ok, tc, dur, half_window) for tc in trials) if s is not None])
        if ev is None or rnd.size < 30:
            out[name] = {"event": ev, "z": None, "n_random": int(rnd.size)}
            continue
        s = robust_sigma(rnd)
        z = (ev - float(np.median(rnd))) / s if s > 0 else None
        frac = float(np.mean(np.abs(rnd - np.median(rnd)) >= abs(ev - np.median(rnd))))
        out[name] = {"event": ev, "z": z, "n_random": int(rnd.size), "fraction_random_as_extreme": frac}
    return out


def quality_near(lc: LC, tmid, dur, pad_days=0.5):
    w = np.abs(lc.t - tmid) <= dur / 2 + pad_days
    flags = {}
    for bit, name in QUALITY_BITS.items():
        n = int(np.sum((lc.q[w] & bit) > 0))
        if n:
            flags[name] = n
    dumps = lc.t[(lc.q & 32) > 0]
    nearest = float(np.min(np.abs(dumps - tmid)) * 24) if dumps.size else None
    inb = _box(lc.t, tmid, dur)
    expected = dur * 86400 / 120
    return {"flags_within_pad": flags, "pad_days": pad_days, "nearest_momentum_dump_h": nearest,
            "usable_in_box": int((lc.ok & inb).sum()), "expected_in_box": int(round(expected))}


# ------------------------------------------------------------------ catalogue
def tap(query: str, url: str = EXO_TAP) -> list[dict]:
    import requests

    r = requests.post(url, data={"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": query}, timeout=120)
    r.raise_for_status()
    return list(csv.DictReader(io.StringIO(r.text)))


def siblings(tic: int) -> tuple[list[dict], str]:
    q = ("SELECT toi, tid, tfopwg_disp, pl_orbper, pl_orbpererr1, pl_tranmid, pl_tranmiderr1, pl_trandurh, pl_trandep, "
         f"st_rad, st_logg, rowupdate FROM toi WHERE tid = {int(tic)} ORDER BY toi")
    return tap(q), q


def _f(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def ephemeris_hits(sibs: list[dict], tmid: float, dur_h: float) -> list[dict]:
    out = []
    for s in sibs:
        P, T0 = _f(s["pl_orbper"]), _f(s["pl_tranmid"])
        if not P or P <= 0 or T0 is None:
            continue
        n = round((tmid - T0) / P)
        pred = T0 + n * P
        sig = math.hypot(_f(s["pl_tranmiderr1"]) or 0.0, abs(n) * (_f(s["pl_orbpererr1"]) or 0.0))
        off_h = (tmid - pred) * 24
        tol_h = (dur_h + (_f(s["pl_trandurh"]) or 0)) / 2 + 3 * sig * 24
        out.append({"toi": s["toi"], "disposition": s["tfopwg_disp"], "period_days": P, "depth_ppm": _f(s["pl_trandep"]),
                    "duration_h": _f(s["pl_trandurh"]), "predicted_bjd": pred, "offset_h": off_h,
                    "ephemeris_sigma_h": sig * 24, "coincides": abs(off_h) <= tol_h})
    return out


def gaia_neighbours(root: Path, slug: str, ra: float, dec: float, depth_ppm: float) -> dict:
    """Gaia DR3 sources within 2.5 TESS pixels of the target that could produce ``depth_ppm``
    if fully eclipsed (ΔG ≤ −2.5 log10 depth). Uses the explorer's recorded Gaia field."""
    f = root / "design-system" / "mockups" / "data" / f"field_{slug}.csv"
    if not f.is_file():
        return {"state": "not_tested", "note": f"no recorded Gaia field ({f.name}); fetch with fetch_sky_data.py --missing"}
    rows = [r for r in csv.DictReader(f.open(encoding="utf-8")) if _f(r.get("g")) is not None]
    for r in rows:
        dra = (float(r["ra"]) - ra) * math.cos(math.radians(dec)) * 3600
        r["sep"] = math.hypot(dra, (float(r["dec"]) - dec) * 3600)
    rows.sort(key=lambda r: r["sep"])
    if not rows or rows[0]["sep"] > 3:
        return {"state": "inconclusive", "note": "target not identified in the Gaia field within 3″"}
    tgt = rows[0]
    dmax = -2.5 * math.log10(max(depth_ppm, 1) * 1e-6)
    near = [{"source_id": r["source_id"], "sep_arcsec": round(r["sep"], 1), "delta_g": round(float(r["g"]) - float(tgt["g"]), 2)}
            for r in rows[1:] if r["sep"] <= 2.5 * TESS_PIX_ARCSEC]
    capable = [n for n in near if n["delta_g"] <= dmax]
    return {"state": "done", "target_gaia": tgt["source_id"], "target_g": float(tgt["g"]), "radius_arcsec": 2.5 * TESS_PIX_ARCSEC,
            "max_delta_g_for_depth": round(dmax, 2), "neighbours": near[:20], "capable": capable,
            "g_limit_of_field": "G < 17 (explorer field); fainter blends not listed", "source_file": f"design-system/mockups/data/{f.name}"}


# ------------------------------------------------------------------ pixels
def _mast_file(uri: str, dest: Path) -> Path:
    import requests

    if dest.is_file() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    url = "https://mast.stsci.edu/api/v0.1/Download/file?uri=" + uri
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        tmp = dest.with_suffix(".part")
        with tmp.open("wb") as fh:
            for chunk in r.iter_content(1 << 20):
                fh.write(chunk)
    tmp.replace(dest)
    return dest


def tpf_for(lc_product: str, scratch: Path) -> Path:
    fn = lc_product.replace("_lc.fits", "_tp.fits")
    return _mast_file("mast:TESS/product/" + fn, scratch / "tpf" / fn)


def difference_image(tpf: Path, ra: float, dec: float, events: list[tuple[str, float, float]], n_boot: int = 200, seed: int = 0):
    """For each (label, mid, duration): per-pixel depth = linear flank baseline − in-transit mean;
    centroid of the positive difference image (3×3 around its peak) vs the target's pixel position."""
    from astropy.io import fits
    from astropy.wcs import WCS

    rng = np.random.default_rng(seed)
    with fits.open(tpf, memmap=False) as h:
        d = h[1].data
        t = np.asarray(d["TIME"], float) + float(h[1].header.get("BJDREFI", 0)) + float(h[1].header.get("BJDREFF", 0))
        flux = np.asarray(d["FLUX"], float)
        q = np.asarray(d["QUALITY"], int)
        ap = np.asarray(h[2].data, int)
        wcs = WCS(h[2].header)
    tx, ty = (float(v) for v in wcs.world_to_pixel_values(ra, dec))
    good = np.isfinite(t) & (q == 0) & np.all(np.isfinite(flux.reshape(len(t), -1)), axis=1)
    optimal = (ap & 2) > 0
    res = {"target_pixel_xy": [tx, ty], "stamp_shape": list(flux.shape[1:]), "optimal_aperture_pixels": int(optimal.sum()),
           "events": {}}
    for label, tm, dur in events:
        inb = good & _box(t, tm, dur * 0.8)
        flank = good & (np.abs(t - tm) > dur / 2 + 1 / 48) & (np.abs(t - tm) <= dur / 2 + max(dur, 0.25))
        if inb.sum() < 4 or flank.sum() < 10:
            res["events"][label] = {"state": "not_tested", "note": f"{int(inb.sum())} in-transit, {int(flank.sum())} flank cadences"}
            continue
        ii, ff = np.flatnonzero(inb), np.flatnonzero(flank)

        def diff(ii, ff):
            x = t[ff] - tm
            A = np.vstack([np.ones_like(x), x]).T
            c, *_ = np.linalg.lstsq(A, flux[ff].reshape(len(ff), -1), rcond=None)
            base = c[0] + np.outer(t[ii] - tm, c[1]).mean(axis=0)
            return (base - flux[ii].reshape(len(ii), -1).mean(axis=0)).reshape(flux.shape[1:]), c[0].reshape(flux.shape[1:])

        def centroid(img):
            py, px = np.unravel_index(np.nanargmax(img), img.shape)
            ys = slice(max(0, py - 1), min(img.shape[0], py + 2))
            xs = slice(max(0, px - 1), min(img.shape[1], px + 2))
            w = np.clip(img[ys, xs], 0, None)
            if w.sum() <= 0:
                return None
            yy, xx = np.mgrid[ys, xs]
            return float((w * xx).sum() / w.sum()), float((w * yy).sum() / w.sum())

        dimg, oot = diff(ii, ff)
        c_diff, c_oot = centroid(dimg), centroid(oot)
        boots = []
        for _ in range(n_boot):
            b = centroid(diff(rng.choice(ii, ii.size), rng.choice(ff, ff.size))[0])
            if b:
                boots.append(b)
        boots = np.array(boots)
        sx, sy = (float(np.std(boots[:, 0])), float(np.std(boots[:, 1]))) if len(boots) > 10 else (None, None)
        if c_diff is None:
            res["events"][label] = {"state": "inconclusive", "note": "no positive difference signal"}
            continue
        off = (c_diff[0] - tx, c_diff[1] - ty)
        dist = math.hypot(*off)
        sig = math.hypot(sx or 0, sy or 0) or None
        # the WCS position carries PSF and pointing systematics; the out-of-transit centroid of the same
        # stamp is the reference that cancels them (a signal on the target leaves the centroid unmoved)
        roff = (c_diff[0] - c_oot[0], c_diff[1] - c_oot[1]) if c_oot else None
        rdist = math.hypot(*roff) if roff else None
        in_ap = float(dimg[optimal].sum() / np.clip(dimg, 0, None).sum()) if np.clip(dimg, 0, None).sum() > 0 else None
        res["events"][label] = {
            "state": "done", "in_cadences": int(inb.sum()), "flank_cadences": int(flank.sum()),
            "diff_centroid_xy": list(c_diff), "oot_centroid_xy": list(c_oot) if c_oot else None,
            "offset_from_target_pix": [off[0], off[1]], "offset_from_target_arcsec": dist * TESS_PIX_ARCSEC,
            "bootstrap_sigma_pix": [sx, sy], "offset_over_sigma": dist / sig if sig else None,
            "offset_from_oot_centroid_pix": list(roff) if roff else None,
            "offset_from_oot_centroid_arcsec": rdist * TESS_PIX_ARCSEC if rdist is not None else None,
            "oot_offset_over_sigma": rdist / sig if (sig and rdist is not None) else None,
            "fraction_of_positive_difference_in_optimal_aperture": in_ap,
            "peak_pixel": [int(v) for v in np.unravel_index(np.nanargmax(dimg), dimg.shape)[::-1]],
            "image": dimg.tolist()}
    res["aperture"] = optimal.astype(int).tolist()
    return res


# ------------------------------------------------------------------ neighbours (common mode)
def neighbour_lcs(ra, dec, sector, camera, ccd, tic, scratch: Path, n_max=5, radius_deg=1.5):
    from astroquery.mast import Observations

    obs = Observations.query_criteria(coordinates=f"{ra} {dec}", radius=f"{radius_deg} deg", obs_collection="TESS",
                                      provenance_name="SPOC", dataproduct_type="timeseries", sequence_number=int(sector))
    obs = [o for o in obs if str(o["target_name"]) != str(tic) and str(o["target_name"]).isdigit()]
    obs.sort(key=lambda o: (float(o["s_ra"]) - ra) ** 2 * math.cos(math.radians(dec)) ** 2 + (float(o["s_dec"]) - dec) ** 2)
    out = []
    for o in obs[: n_max * 3]:
        if len(out) >= n_max:
            break
        fn = str(o["dataURL"]).split("/")[-1] if o["dataURL"] else ""
        if not fn.endswith("_lc.fits") or "fast" in fn:
            continue
        try:
            p = _mast_file("mast:TESS/product/" + fn, scratch / "neighbours" / fn)
            lc = LC(p)
        except Exception as exc:   # record, never substitute
            out.append({"product": fn, "error": repr(exc)[:200]})
            continue
        if (lc.camera, lc.ccd) != (camera, ccd):
            continue
        sep = math.degrees(math.acos(min(1, math.sin(math.radians(dec)) * math.sin(math.radians(lc.dec)) +
                                         math.cos(math.radians(dec)) * math.cos(math.radians(lc.dec)) * math.cos(math.radians(ra - lc.ra)))))
        out.append({"product": fn, "tic": str(o["target_name"]), "tmag": lc.tmag, "sep_deg": round(sep, 3), "lc": lc})
    return out


# ------------------------------------------------------------------ periods
def max_central_duration_h(P_days, rstar, mstar, k=0.1):
    a = (G_SI * mstar * MSUN * (P_days * 86400) ** 2 / (4 * math.pi ** 2)) ** (1 / 3)
    x = min(1.0, rstar * RSUN * (1 + k) / a)
    return P_days / math.pi * math.asin(x) * 24


# ------------------------------------------------------------------ main
def cluster(cands: list[dict], dur_d: float) -> list[dict]:
    evs = []
    for c in sorted(cands, key=lambda c: (c["product"], c["event_bjd"])):
        if evs and evs[-1]["product"] == c["product"] and c["event_bjd"] - evs[-1]["members"][-1]["event_bjd"] <= max(dur_d, 0.25):
            evs[-1]["members"].append(c)
        else:
            evs.append({"product": c["product"], "members": [c]})
    for e in evs:
        deepest = max(e["members"], key=lambda c: c["depth_ppm"])
        ts = [c["event_bjd"] for c in e["members"]]
        e.update(guess_bjd=float((min(ts) + max(ts)) / 2), span_h=(max(ts) - min(ts)) * 24,
                 max_allowed=max(c["n_allowed"] for c in e["members"]), deepest_ppm=deepest["depth_ppm"])
    return evs


def data_aliases(lcs: dict, t_ref: float, t_ev: float, dur_d: float, depth: float, pmin: float = 1.0,
                 cover: float = 0.5, below: float = 0.3) -> list[dict]:
    """P = ΔT/n ≥ pmin; excluded when a predicted transit other than the two lands on usable data
    (≥ ``cover`` of the window) with a mean residual shallower than ``below`` × ``depth``
    (the period_aliases rule, for events given by hand)."""
    dT = abs(t_ev - t_ref)
    rows = []
    for n in range(1, int(dT / pmin) + 1):
        P = dT / n
        verdict = "allowed"
        for lc in lcs.values():
            span = lc.t[lc.ok]
            for k in range(math.ceil((span.min() - t_ref) / P), math.floor((span.max() - t_ref) / P) + 1):
                tp = t_ref + k * P
                if abs(tp - t_ref) < dur_d or abs(tp - t_ev) < dur_d:
                    continue
                w = _box(lc.t, tp, dur_d)
                if w.sum() == 0 or (w & lc.ok).sum() < cover * max(w.sum(), dur_d * 86400 / 120):
                    continue
                sh = _shift(lc.t, lc.col["PDCSAP_FLUX"], lc.ok, tp, dur_d, max(1.5 * dur_d, dur_d / 2 + 0.6))
                if sh is not None and -sh < below * depth:
                    verdict = "excluded"
                    break
            if verdict == "excluded":
                break
        rows.append({"n": n, "period_days": P, "verdict": verdict})
    return rows


def _cadence_s(lc: "LC") -> float:
    dt = np.diff(lc.t[np.isfinite(lc.t)])
    dt = dt[dt > 0]
    return float(np.median(dt) * 86400) if dt.size else 120.0


def secondary_eclipse_rows(lcs: dict, t_ref: float, periods, dur: float, sib_t=(), n_red: int = 200, seed: int = 1):
    """Weighted mean box depth at phase 0.5 of each circular period alias, with red-noise errors.

    The error of one box measurement is the robust spread of the same statistic at ``n_red`` random
    epochs of that light curve. Phase-0.5 windows with under half their cadences usable (at the
    product's own cadence), or where a sibling TOI transits, are skipped. Returns (rows, red_sigma).
    """
    hw_ = max(1.5 * dur, dur / 2 + 0.6)
    red = {}
    for pid, lc in lcs.items():
        rng = np.random.default_rng(seed)
        span = lc.t[lc.ok]
        vals = []
        for tc in rng.uniform(span.min() + hw_, span.max() - hw_, n_red):
            v = _shift(lc.t, lc.col["PDCSAP_FLUX"], lc.ok, tc, dur, hw_)
            if v is not None:
                vals.append(v)
        red[pid] = robust_sigma(vals) if len(vals) >= 30 else None
    rows = []
    for P in periods:
        meas = []
        for pid, lc in lcs.items():
            span = lc.t[lc.ok]
            need = 0.5 * dur * 86400 / _cadence_s(lc)
            for k in range(math.ceil((span.min() - t_ref - P / 2) / P), math.floor((span.max() - t_ref - P / 2) / P) + 1):
                ts = t_ref + (k + 0.5) * P
                if (lc.ok & _box(lc.t, ts, dur)).sum() < need:
                    continue
                if any(abs(((ts - T0) / Ps) - round((ts - T0) / Ps)) * Ps < (dur + ds) / 2 + 0.1 for T0, Ps, ds in sib_t):
                    continue   # a sibling TOI transits here
                sh = _shift(lc.t, lc.col["PDCSAP_FLUX"], lc.ok, ts, dur, hw_)
                if sh is not None and red.get(pid):
                    meas.append((-sh, red[pid]))
        if meas:
            w = np.array([1 / e_ ** 2 for _, e_ in meas])
            d = float(np.sum(w * np.array([m for m, _ in meas])) / w.sum())
            rows.append({"period_days": P, "n_epochs": len(meas), "secondary_depth_ppm": d * 1e6,
                         "err_ppm": float(w.sum() ** -0.5) * 1e6})
    return rows, red


def vet(spec: dict, root: Path, *, neighbours: bool = True, pixels: bool = True, extra_events=(), echo=print) -> dict:
    from ..config import scratch_dir

    cid = spec["campaign_id"]
    out_dir = root / spec.get("outputs", f"campaigns/{cid}/").rstrip("/")
    rdir = out_dir / "runner"
    vdir = out_dir / "vetting"
    vdir.mkdir(parents=True, exist_ok=True)
    tgt = spec["targets"][0]
    dur_cat_h = float(tgt.get("duration_h") or 3.0)
    prods = json.loads((rdir / "fetch_products.json").read_text(encoding="utf-8"))["result"]["products"]
    unsupported = {pid: p for pid, p in prods.items()
                   if (p.get("archive") or "MAST") != "MAST" or (p.get("format") or "spoc_lc") not in ("spoc_lc", "tess_lc")}
    if unsupported:
        detail = ", ".join(f"{pid} ({p.get('archive')}/{p.get('format')})" for pid, p in list(unsupported.items())[:4])
        raise SystemExit(f"vet supports MAST SPOC light curves only; {len(unsupported)} product(s) are from another "
                         f"archive or format: {detail}. Screen them with the multi-archive steps instead.")
    known = json.loads((rdir / "known_signal_recovery.json").read_text(encoding="utf-8"))["result"]["per_product"]
    pa = json.loads((out_dir / "period_aliases.json").read_text(encoding="utf-8")) if (out_dir / "period_aliases.json").is_file() else {"candidates": []}
    scratch = scratch_dir() / f"campaign_{cid}"
    lcs = {pid: LC(resolve(p["path"])) for pid, p in prods.items()}
    report: dict = {"campaign_id": cid, "target": tgt["name"], "tic": tgt["tic"], "events": [], "reference": None}

    sibs, q = [], None
    try:
        sibs, q = siblings(tgt["tic"])
        report["siblings"] = {"query": q, "service": EXO_TAP, "rows": sibs}
    except Exception as exc:
        report["siblings"] = {"error": repr(exc)[:300]}
    srow = next((s for s in sibs if s["toi"] and tgt["name"].endswith(s["toi"])), sibs[0] if sibs else {})
    rstar, logg = _f(srow.get("st_rad")), _f(srow.get("st_logg"))
    mstar = (10 ** logg / 100) * (rstar * RSUN) ** 2 / G_SI / MSUN if rstar and logg else None
    report["star"] = {"radius_rsun": rstar, "logg_cgs": logg, "mass_msun_from_logg": mstar, "source": "NASA Exoplanet Archive toi table"}

    # reference transit
    ref = None
    for pid, v in known.items():
        for ep in v.get("epochs", []):
            if ep.get("state") in ("recovered", "partial") and ref is None:
                ref = (pid, ep["epoch_bjd"] + (ep.get("entry_offset_hours") or 0) / 24)
    half = lambda d: max(1.5 * d, d / 2 + 0.6)
    ref_fit = None
    if ref:
        lc = lcs[ref[0]]
        ref_fit = box_fit(lc.t[lc.ok], lc.col["PDCSAP_FLUX"][lc.ok], ref[1], dur_cat_h / 24, half(dur_cat_h / 24),
                          yerr=lc.col["PDCSAP_FLUX_ERR"][lc.ok] if "PDCSAP_FLUX_ERR" in lc.col else None)
        report["reference"] = {"product": ref[0], "sector": lc.sector, "fit": ref_fit}
    dur_ref_d = (ref_fit["duration_h"] if ref_fit else dur_cat_h) / 24
    t_ref = ref_fit["mid_bjd"] if ref_fit else None

    events = cluster(pa.get("candidates", []), dur_ref_d)
    for tb in extra_events:   # events given by hand (reviewer flags without a runner repeat candidate)
        pid = next((k for k, lc in lcs.items() if np.nanmin(lc.t) <= tb <= np.nanmax(lc.t)), None)
        if pid is None:
            echo(f"[vet] BJD {tb} is not inside any retrieved light curve; skipped")
            continue
        events.append({"product": pid, "members": [{"event_bjd": tb, "depth_ppm": 0.0, "n_allowed": 0, "allowed_periods_days": []}],
                       "guess_bjd": float(tb), "span_h": 0.0, "max_allowed": 0, "deepest_ppm": 0.0, "given_by_hand": True})
    if t_ref is None and tgt.get("t0_bjd"):
        t_ref = float(tgt["t0_bjd"])   # catalogue epoch (not re-measured: no retrieved light curve covers it)
        report["reference_epoch_note"] = "catalogue t0 used as the reference epoch; the catalogued transit was not measured here"
    tpf_cache: dict = {}
    for i, e in enumerate(events):
        lc = lcs[e["product"]]
        label = f"E{i + 1}"
        echo(f"[vet] {cid} {label} S{lc.sector} BJD {e['guess_bjd']:.3f} ({len(e['members'])} screen candidates)")
        hw = half(dur_ref_d)
        fit = box_fit(lc.t[lc.ok], lc.col["PDCSAP_FLUX"][lc.ok], e["guess_bjd"], dur_ref_d, hw,
                      search_hours=max(1.0, e["span_h"] / 2 + dur_ref_d * 12),
                      yerr=lc.col["PDCSAP_FLUX_ERR"][lc.ok] if "PDCSAP_FLUX_ERR" in lc.col else None)
        ev = {"label": label, "product": e["product"], "sector": lc.sector, "camera": lc.camera, "ccd": lc.ccd,
              "given_by_hand": bool(e.get("given_by_hand")),
              "screen_candidates": len(e["members"]), "screen_span_h": e["span_h"], "max_aliases_allowed": e["max_allowed"],
              "fit": fit, "checks": {}}
        report["events"].append(ev)
        if not fit:
            ev["checks"]["Shape fit"] = ("not_tested", "fewer than 20 usable cadences around the event")
            continue
        tm, dur = fit["mid_bjd"], fit["duration_h"] / 24
        hw = half(dur)
        dip = fit["depth_ppm"] > 3 * fit["depth_err_ppm"]
        ev["significant_dip"] = dip
        wf = fit.get("weighted")
        if wf is None:
            ev["checks"]["Error-weighted box fit"] = ("not_tested", "no PDCSAP_FLUX_ERR column")
        else:
            ratio = wf["scatter_over_quoted_error"]
            agree = abs(wf["depth_ppm"] - fit["depth_ppm"]) <= 2 * math.hypot(fit["depth_err_ppm"], wf["depth_err_scaled_ppm"])
            ev["checks"]["Error-weighted box fit"] = (
                "passed" if agree and 0.7 <= ratio <= 1.5 else "inconclusive",
                f"weighted depth {wf['depth_ppm']:.0f} ± {wf['depth_err_scaled_ppm']:.0f} ppm (χ²ν {wf['chi2_reduced']:.2f}) vs "
                f"unweighted {fit['depth_ppm']:.0f} ± {fit['depth_err_ppm']:.0f} ppm; residual scatter / quoted error "
                f"{ratio:.2f}" + ("" if agree else "; the two depths disagree")
                + ("" if 0.7 <= ratio <= 1.5 else "; the pipeline errors do not describe the scatter"))
        if not dip:
            ev["checks"]["Box fit finds a dip"] = (
                "failed", f"best box depth {fit['depth_ppm']:.0f} ± {fit['depth_err_ppm']:.0f} ppm: no significant dip near the "
                          "screen candidates; the screen entries are not a transit-shaped event")
        if t_ref is not None and fit["depth_ppm"] > 0 and abs(tm - t_ref) > 1.0:
            al = data_aliases(lcs, t_ref, tm, dur, fit["depth_ppm"] * 1e-6)
            e["allowed"] = [a["period_days"] for a in al if a["verdict"] == "allowed"]
            ev["aliases_from_reference"] = {"reference_bjd": t_ref, "delta_t_days": abs(tm - t_ref), "n_aliases": len(al),
                                            "n_allowed": len(e["allowed"]), "allowed_periods_days": [round(x, 4) for x in e["allowed"]],
                                            "rule": "P = dT/n >= 1 d; excluded when a predicted transit lands on usable data "
                                                    "(>=50% of the window) shallower than 0.3 x the event depth"}
        else:
            e["allowed"] = []
        # sibling ephemerides
        hits = ephemeris_hits(sibs, tm, fit["duration_h"])
        ev["ephemerides"] = hits
        on = [h for h in hits if h["coincides"]]
        if "error" in report["siblings"]:
            ev["checks"]["Sibling TOI ephemerides"] = ("inconclusive", "TOI table query failed")
        elif on:
            ev["checks"]["Sibling TOI ephemerides"] = ("failed", "; ".join(
                f"TOI-{h['toi']} ({h['disposition']}, P {h['period_days']:.4f} d, {h['depth_ppm'] or 0:.0f} ppm) predicted "
                f"{h['offset_h']:+.2f} h ± {h['ephemeris_sigma_h']:.2f} h" for h in on))
        else:
            ev["checks"]["Sibling TOI ephemerides"] = ("passed", f"{len(hits)} periodic TOI(s) on this TIC; none predicted at the event"
                                                        if hits else "no periodic TOI on this TIC")
        # shape vs reference
        if ref_fit and dip:
            rd = fit["depth_ppm"] / ref_fit["depth_ppm"]
            rd_e = rd * math.hypot(fit["depth_err_ppm"] / fit["depth_ppm"], ref_fit["depth_err_ppm"] / ref_fit["depth_ppm"])
            rdur = fit["duration_h"] / ref_fit["duration_h"]
            ev["shape_vs_reference"] = {"depth_ratio": rd, "depth_ratio_err": rd_e, "duration_ratio": rdur,
                                        "ref_vshape": ref_fit["vshape_index"], "event_vshape": fit["vshape_index"]}
            depth_ok = abs(rd - 1) <= max(3 * rd_e, 0.2)
            dur_ok = 0.67 <= rdur <= 1.5
            ev["checks"]["Shape matches reference transit"] = (
                "passed" if depth_ok and dur_ok else "failed",
                f"depth ratio {rd:.2f} ± {rd_e:.2f}, duration ratio {rdur:.2f} (box fits; duration grid step ~25%)")
        # detrending
        alts, rng_ = alt_depths(lc, tm, dur, hw)
        ev["detrending_depths_ppm"] = alts
        if rng_ and dip:
            lo, hi = rng_
            ev["checks"]["Detrending alternatives"] = (
                "passed" if lo > 0.5 * fit["depth_ppm"] and hi < 2 * fit["depth_ppm"] else "failed",
                f"PDCSAP depth {lo:.0f}–{hi:.0f} ppm across 6 detrendings (box fit {fit['depth_ppm']:.0f}); "
                f"SAP poly2 {alts.get('SAP poly2', float('nan')):.0f} ppm")
        # red noise and engineering series
        series = {"PDCSAP": lc.col["PDCSAP_FLUX"], "SAP": lc.col["SAP_FLUX"]}
        for n in ("SAP_BKG", "MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2"):
            if n in lc.col:
                series[n] = lc.col[n]
        excl = [tm] + ([ref[1]] if ref and ref[0] == e["product"] else [])
        emp = empirical(lc, series, tm, dur, hw, excl, seed=int(spec.get("random_seed", 0)) + i)
        ev["empirical"] = emp
        zf = emp["PDCSAP"]["z"]
        if zf is not None and dip:
            ev["checks"]["Red-noise significance"] = (
                "passed" if -zf >= 7 else "inconclusive" if -zf >= 4 else "failed",
                f"box statistic at the event is {-zf:.1f} robust σ below {emp['PDCSAP']['n_random']} random epochs of the same light curve; "
                f"fraction as extreme {emp['PDCSAP']['fraction_random_as_extreme']:.3f}")
        eng = {k: v for k, v in emp.items() if k not in ("PDCSAP", "SAP") and v.get("z") is not None}
        worst = max(eng.items(), key=lambda kv: abs(kv[1]["z"])) if eng else None
        if worst:
            ev["checks"]["Background / centroid / pointing"] = (
                "passed" if abs(worst[1]["z"]) < 3 else "inconclusive" if abs(worst[1]["z"]) < 5 else "failed",
                "; ".join(f"{k} {v['z']:+.1f}σ" for k, v in eng.items()) + " (shift at the event vs random epochs)")
        # quality
        qn = quality_near(lc, tm, dur)
        ev["quality"] = qn
        bad = {k: v for k, v in qn["flags_within_pad"].items() if k not in ("aperture cosmic", "collateral cosmic")}
        cov = qn["usable_in_box"] / max(1, qn["expected_in_box"])
        ev["checks"]["Quality flags and coverage"] = (
            "passed" if not bad and cov >= 0.8 else "inconclusive",
            f"{qn['usable_in_box']}/{qn['expected_in_box']} usable in-transit cadences; flags within ±{qn['pad_days']} d: "
            f"{bad or 'none'}; nearest momentum dump {qn['nearest_momentum_dump_h'] and round(qn['nearest_momentum_dump_h'], 1)} h")
        # gaia neighbours
        gn = gaia_neighbours(root, cid, float(tgt["ra_deg"]), float(tgt["dec_deg"]), max(fit["depth_ppm"], 1.0))
        ev["gaia_neighbours"] = gn
        if not dip:
            pass
        elif gn["state"] != "done":
            ev["checks"]["Gaia neighbours able to mimic the depth"] = (gn["state"], gn["note"])
        else:
            cap = gn["capable"]
            ev["checks"]["Gaia neighbours able to mimic the depth"] = (
                "passed" if not cap else "inconclusive",
                f"{len(gn['neighbours'])} Gaia source(s) G<17 within {gn['radius_arcsec']:.0f}″; {len(cap)} bright enough "
                f"(ΔG ≤ {gn['max_delta_g_for_depth']})" + (": " + ", ".join(f"{c['sep_arcsec']}″ ΔG {c['delta_g']}" for c in cap[:4]) if cap else ""))
        # difference image
        if pixels and dip:
            try:
                if e["product"] not in tpf_cache:
                    lab = [(label, tm, dur)]
                    if ref and ref[0] == e["product"] and ref_fit:
                        lab.append(("REF", ref_fit["mid_bjd"], ref_fit["duration_h"] / 24))
                    tpf_cache[e["product"]] = (tpf_for(e["product"], scratch), lab)
                else:
                    tpf_cache[e["product"]][1].append((label, tm, dur))
            except Exception as exc:
                ev["checks"]["Difference-image centroid"] = ("inconclusive", f"target pixel file unavailable: {repr(exc)[:150]}")
        # neighbours
        if neighbours:
            try:
                nb = neighbour_lcs(lc.ra, lc.dec, lc.sector, lc.camera, lc.ccd, tgt["tic"], scratch)
                rows = []
                for n in nb:
                    if "lc" not in n:
                        rows.append(n)
                        continue
                    nlc = n.pop("lc")
                    em = empirical(nlc, {"PDCSAP": nlc.col["PDCSAP_FLUX"], "SAP": nlc.col["SAP_FLUX"]}, tm, dur, hw, [tm], n=150)
                    n.update(pdcsap_shift_ppm=(em["PDCSAP"]["event"] or 0) * 1e6 if em["PDCSAP"]["event"] is not None else None,
                             pdcsap_z=em["PDCSAP"]["z"], sap_z=em["SAP"]["z"])
                    rows.append(n)
                ev["neighbours"] = rows
                zs = [r for r in rows if r.get("pdcsap_z") is not None]
                dips = [r for r in zs if r["pdcsap_z"] <= -4 or (r.get("sap_z") or 0) <= -4]
                ev["checks"]["Common mode (same camera/CCD)"] = (
                    "not_tested" if not zs else "failed" if len(dips) >= 2 else "inconclusive" if dips else "passed",
                    f"{len(zs)} neighbour light curve(s) in S{lc.sector} cam {lc.camera} CCD {lc.ccd}; {len(dips)} dip ≥ 4σ at the event")
            except Exception as exc:
                ev["checks"]["Common mode (same camera/CCD)"] = ("inconclusive", f"neighbour query failed: {repr(exc)[:150]}")
        # stellar density on aliases
        if rstar and mstar and dip:
            allowed = e["allowed"]
            k = math.sqrt(max(fit["depth_ppm"], 1) * 1e-6)
            rows = [{"period_days": P, "max_central_duration_h": max_central_duration_h(P, rstar, mstar, k)} for P in allowed]
            for r in rows:
                r["disfavoured_circular"] = fit["duration_h"] > 1.2 * r["max_central_duration_h"]
            ev["aliases_density"] = rows
            if rows:
                ok_ = [r["period_days"] for r in rows if not r["disfavoured_circular"]]
                ev["checks"]["Stellar-density duration limit"] = (
                    "passed" if ok_ else "failed",
                    f"{len(ok_)} of {len(rows)} allowed aliases compatible with a {fit['duration_h']:.1f}-h transit on a "
                    f"{rstar:.2f} R☉, {mstar:.2f} M☉ star (circular, central); shortest compatible "
                    f"{min(ok_):.2f} d" if ok_ else "no allowed alias is long enough for the measured duration")

    # secondary eclipses at the allowed aliases (circular orbits: phase 0.5)
    for ev in report["events"]:
        f = ev.get("fit")
        e = next((x for x in events if x["product"] == ev["product"] and abs(x["guess_bjd"] - (f or {}).get("mid_bjd", 0)) < 1), None)
        if not f or t_ref is None or not e or not ev.get("significant_dip"):
            continue
        allowed = e.get("allowed") or []
        if not allowed:
            continue
        dur = f["duration_h"] / 24
        sib_t = [(_f(x["pl_tranmid"]), _f(x["pl_orbper"]), (_f(x["pl_trandurh"]) or 3) / 24) for x in sibs
                 if _f(x.get("pl_orbper")) and _f(x.get("pl_tranmid"))]
        rows, red = secondary_eclipse_rows(lcs, t_ref, allowed, dur, sib_t)
        ev["secondary_red_noise_ppm"] = {str(lcs[k].sector): (v * 1e6 if v else None) for k, v in red.items()}
        ev["secondary_eclipse"] = rows
        sig = [r_ for r_ in rows if r_["secondary_depth_ppm"] > 4 * r_["err_ppm"]]
        ev["checks"]["Secondary eclipse (circular aliases)"] = (
            "not_tested" if not rows else "failed" if sig else "passed",
            f"phase 0.5 covered for {len(rows)} of {len(allowed)} allowed aliases (red-noise errors, sibling transits masked); "
            + (f"{len(sig)} with a ≥4σ dip: " + ", ".join(f"P {r_['period_days']:.2f} d {r_['secondary_depth_ppm']:.0f}±{r_['err_ppm']:.0f} ppm" for r_ in sig[:4])
               if sig else (f"no ≥4σ dip; median 1σ limit {np.median([r_['err_ppm'] for r_ in rows]):.0f} ppm" if rows else "")))

    # difference images per sector
    for pid, (path, labs) in tpf_cache.items():
        try:
            di = difference_image(path, float(tgt["ra_deg"]), float(tgt["dec_deg"]), labs)
        except Exception as exc:
            for lab, *_ in labs:
                ev = next((x for x in report["events"] if x["label"] == lab), None)
                if ev:
                    ev["checks"]["Difference-image centroid"] = ("inconclusive", f"difference image failed: {repr(exc)[:150]}")
            continue
        for lab, *_ in labs:
            r = di["events"].get(lab, {})
            if lab == "REF":
                report["reference"]["difference_image"] = {k: v for k, v in r.items()}
                continue
            ev = next(x for x in report["events"] if x["label"] == lab)
            ev["difference_image"] = {**r, "target_pixel_xy": di["target_pixel_xy"], "aperture": di["aperture"]}
            if r.get("state") != "done":
                ev["checks"]["Difference-image centroid"] = (r.get("state", "inconclusive"), r.get("note", ""))
                continue
            off, s = r["offset_from_oot_centroid_arcsec"], r["oot_offset_over_sigma"]
            if off is None:
                ev["checks"]["Difference-image centroid"] = ("inconclusive", "no out-of-transit centroid")
                continue
            # a small offset passes; a large one fails only when the bootstrap makes it significant; a large but
            # insignificant offset (a noisy stamp) is inconclusive, not passed
            state = ("passed" if off < 0.25 * TESS_PIX_ARCSEC
                     else "failed" if s and s >= 3 and off >= 0.5 * TESS_PIX_ARCSEC else "inconclusive")
            refd = (report.get("reference") or {}).get("difference_image") or di["events"].get("REF") or {}
            ev["checks"]["Difference-image centroid"] = (
                state, f"difference-image centroid {off:.1f}″ from the out-of-transit centroid ({(s or 0):.1f}σ bootstrap); "
                       f"{r['offset_from_target_arcsec']:.1f}″ from the catalogue position; "
                       f"{100 * (r['fraction_of_positive_difference_in_optimal_aperture'] or 0):.0f}% of the deficit in the optimal aperture")
    # reference difference images for sectors without a lead event
    if ref and ref_fit and ref[0] not in tpf_cache and pixels:
        try:
            di = difference_image(tpf_for(ref[0], scratch), float(tgt["ra_deg"]), float(tgt["dec_deg"]),
                                  [("REF", ref_fit["mid_bjd"], ref_fit["duration_h"] / 24)])
            report["reference"]["difference_image"] = {**di["events"]["REF"], "target_pixel_xy": di["target_pixel_xy"],
                                                       "aperture": di["aperture"]}
        except Exception as exc:
            report["reference"]["difference_image"] = {"state": "inconclusive", "note": repr(exc)[:200]}

    # joint periods for several events
    t0 = t_ref
    fitted = [e for e in report["events"] if e.get("fit") and e["fit"]["depth_ppm"] > 0]
    fitted = [e for e in fitted if (e.get("aliases_from_reference") or {}).get("n_allowed")]
    if t0 and len(fitted) >= 2:
        tol_h = 0.75
        for first in fitted:
            others = [e for e in fitted if e is not first]
            first["joint_periods_days"] = [
                P for P in first["aliases_from_reference"]["allowed_periods_days"]
                if all(abs(((e["fit"]["mid_bjd"] - t0) / P) - round((e["fit"]["mid_bjd"] - t0) / P)) * P * 24 <= tol_h for e in others)]
        best = min(fitted, key=lambda e: len(e["joint_periods_days"]))
        report["joint_periods_days"] = {"tolerance_h": tol_h, "events": [e["label"] for e in fitted], "periods": best["joint_periods_days"],
                                        "note": f"aliases of the reference-to-{best['label']} interval allowed by the data that also put "
                                                f"every other listed event within {tol_h} h of a predicted transit"}
    (vdir / "vetting.json").write_text(json.dumps(report, indent=1, default=float), encoding="utf-8")
    try:
        plot(report, lcs, vdir)
    except Exception as exc:   # figures are a convenience
        report["plot_error"] = repr(exc)[:200]
    (vdir / "VETTING.md").write_text(summary_md(report), encoding="utf-8")
    return report


def plot(report: dict, lcs: dict, vdir: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    ref = report.get("reference") or {}
    rfit = ref.get("fit")
    for ev in report["events"]:
        f = ev.get("fit")
        if not f:
            continue
        lc = lcs[ev["product"]]
        fig, ax = plt.subplots(2, 3, figsize=(15, 8))
        tm, d = f["mid_bjd"], f["duration_h"] / 24
        w = np.abs(lc.t - tm) <= max(1.5 * d, d / 2 + 0.6)
        h = (lc.t - tm) * 24
        a = ax[0, 0]
        a.plot(h[w & lc.ok], (lc.col["PDCSAP_FLUX"][w & lc.ok] - 1) * 1e3, ".", ms=2, color="k", label=f"{ev['label']} PDCSAP")
        a.plot(h[w & lc.ok], (lc.col["SAP_FLUX"][w & lc.ok] - 1) * 1e3 - 3 * f["depth_ppm"] / 1e3, ".", ms=2, color="0.6", label="SAP (offset)")
        if rfit:
            rl = lcs[ref["product"]]
            rw = (np.abs(rl.t - rfit["mid_bjd"]) <= max(1.5 * d, d / 2 + 0.6)) & rl.ok
            a.plot((rl.t[rw] - rfit["mid_bjd"]) * 24, (rl.col["PDCSAP_FLUX"][rw] - 1) * 1e3 + 1.5 * f["depth_ppm"] / 1e3, ".", ms=2,
                   color="tab:blue", label="reference (offset)")
        a.axvspan(-f["duration_h"] / 2, f["duration_h"] / 2, color="tab:red", alpha=0.08)
        a.set(xlabel="hours from event mid", ylabel="ppt", title=f"{report['target']} {ev['label']} S{ev['sector']} BJD {tm:.4f}")
        a.legend(fontsize=7)
        for a, names in ((ax[0, 1], ("SAP_BKG",)), (ax[0, 2], ("MOM_CENTR1", "MOM_CENTR2")), (ax[1, 0], ("POS_CORR1", "POS_CORR2"))):
            for n in names:
                if n in lc.col:
                    y = lc.col[n][w & lc.ok]
                    a.plot(h[w & lc.ok], y - np.nanmedian(y), ".", ms=2, label=f"{n} z={ev['empirical'].get(n, {}).get('z') or 0:+.1f}")
            a.axvspan(-f["duration_h"] / 2, f["duration_h"] / 2, color="tab:red", alpha=0.08)
            a.legend(fontsize=7)
            a.set_xlabel("hours")
        a = ax[1, 1]
        di = ev.get("difference_image")
        if di and di.get("image"):
            img = np.array(di["image"])
            a.imshow(img, origin="lower", cmap="viridis")
            apm = np.array(di["aperture"])
            a.contour(apm, levels=[0.5], colors="w", linewidths=0.8)
            a.plot(*di["target_pixel_xy"], "r+", ms=12, mew=2)
            a.plot(*di["diff_centroid_xy"], "wx", ms=10, mew=2)
            a.set_title(f"difference image; offset {di['offset_from_target_arcsec']:.1f}″", fontsize=9)
        else:
            a.text(0.5, 0.5, "no difference image", ha="center")
        a = ax[1, 2]
        nb = [n for n in ev.get("neighbours", []) if n.get("pdcsap_z") is not None]
        if nb:
            a.bar(range(len(nb)), [n["pdcsap_z"] for n in nb], color="tab:purple")
            a.set_xticks(range(len(nb)), [f"TIC{n['tic']}\n{n['sep_deg']}°" for n in nb], fontsize=6)
            a.axhline(-4, color="r", lw=0.8)
            a.set_title("neighbours: PDCSAP z at the event", fontsize=9)
        else:
            a.text(0.5, 0.5, "no neighbour light curves", ha="center")
        fig.tight_layout()
        fig.savefig(vdir / f"{ev['label']}_S{ev['sector']}.png", dpi=90)
        plt.close(fig)


def summary_md(r: dict) -> str:
    L = [f"# Lead vetting: {r['target']} (TIC {r['tic']})", "",
         "Generated by `python -m cygnus.campaign vet`. States are the tool's; the reviewer's reading goes in REPORT.md. "
         "Nothing here changes the record's evidence level.", ""]
    ref = r.get("reference") or {}
    if ref.get("fit"):
        f = ref["fit"]
        L.append(f"**Reference transit** (S{ref['sector']}): BJD {f['mid_bjd']:.4f}, depth {f['depth_ppm']:.0f} ± {f['depth_err_ppm']:.0f} ppm, "
                 f"duration {f['duration_h']:.2f} h, V-shape index {f['vshape_index'] and round(f['vshape_index'], 2)}.")
        di = ref.get("difference_image") or {}
        if di.get("state") == "done":
            L.append(f"Reference difference-image centroid {di['offset_from_target_arcsec']:.1f}″ from the target "
                     f"({(di.get('offset_over_sigma') or 0):.1f}σ).")
        L.append("")
    sib = [s for s in (r.get("siblings") or {}).get("rows", []) if _f(s.get("pl_orbper"))]
    if sib:
        L.append("**Periodic TOIs on this TIC:** " + "; ".join(f"TOI-{s['toi']} P {float(s['pl_orbper']):.4f} d, {s['pl_trandep']} ppm, {s['tfopwg_disp']}" for s in sib))
        L.append("")
    if r.get("joint_periods_days"):
        j = r["joint_periods_days"]
        L.append(f"**Periods consistent with the reference and events {', '.join(j['events'])}** (±{j['tolerance_h']} h, data-allowed): {len(j['periods'])}: "
                 + ", ".join(f"{p:.3f}" for p in j["periods"][:15]) + (" …" if len(j["periods"]) > 15 else ""))
        L.append("")
    for ev in r["events"]:
        f = ev.get("fit")
        head = f"## {ev['label']}: S{ev['sector']}"
        if f:
            head += f", BJD {f['mid_bjd']:.4f}, depth {f['depth_ppm']:.0f} ± {f['depth_err_ppm']:.0f} ppm, {f['duration_h']:.2f} h"
        al = ev.get("aliases_from_reference") or {}
        L += [head, "", f"{ev['screen_candidates']} screen candidate(s) merged{' (given by hand)' if ev.get('given_by_hand') else ''}; "
              f"ΔT from the reference {al.get('delta_t_days', float('nan')):.3f} d, {al.get('n_allowed', 0)} of {al.get('n_aliases', 0)} "
              f"aliases P = ΔT/n ≥ 1 d allowed by the data.", "",
              "| Check | State | Detail |", "|---|---|---|"]
        for k, (s, d) in ev["checks"].items():
            L.append(f"| {k} | {s} | {d} |")
        L.append("")
    return "\n".join(L) + "\n"

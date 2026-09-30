"""Bounded lead follow-up: exact archive refresh and gap-aware box stress tests.

Run with --mode archives or photometry (or all). Original campaign outputs are
never overwritten. Scientific dependencies use the existing campaign extra.
Random centres preserve the observed time ordering within each window; this
is an empirical local null, not a calibrated original-search false alarm rate.
Injections test fixed-epoch box sensitivity, not blind transit recovery.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))


def box_measure(
    t, y, mid, duration, degree, min_coverage=0.8, *, exposure=None, min_points=4
):
    """Joint additive polynomial + box fit; require event and both flanks.

    Duration in days, absolute times and mid in the same scale. Cadence is
    measured from the actual finite times. No interpolation across gaps.
    """
    t, y = np.asarray(t), np.asarray(y)
    finite = np.isfinite(t) & np.isfinite(y)
    t, y = t[finite], y[finite]
    cadence = float(np.median(np.diff(np.sort(t)))) if len(t) > 1 else np.inf
    x = t - mid
    local = np.abs(x) <= CONFIG["baseline_half_window_days"]
    x, yy = x[local], y[local]
    weight = (np.abs(x) <= duration / 2).astype(float)
    if exposure is not None:
        weight = (
            np.clip(
                np.minimum(x + exposure / 2, duration / 2)
                - np.maximum(x - exposure / 2, -duration / 2),
                0,
                exposure,
            )
            / exposure
        )
    event = weight > 0
    expected = duration / cadence
    left = x < -duration / 2
    right = x > duration / 2
    coverage = float(weight.sum() / expected) if expected > 0 else 0
    if (
        coverage < min_coverage
        or event.sum() < min_points
        or left.sum() < 10
        or right.sum() < 10
    ):
        return {"state": "uncovered", "coverage": coverage, "n_event": int(event.sum())}
    design = np.column_stack([x**i for i in range(degree + 1)] + [-weight])
    coef, *_ = np.linalg.lstsq(design, yy, rcond=None)
    baseline = float(coef[0])
    if baseline <= 0:
        return {"state": "invalid_baseline", "coverage": coverage}
    residual = yy - design @ coef
    return {
        "state": "measured",
        "depth_ppm": float(coef[-1] / baseline * 1e6),
        "coverage": coverage,
        "n_event": int(event.sum()),
        "n_flank": int((~event).sum()),
        "residual_rms_ppm": float(np.std(residual) / baseline * 1e6),
    }


def save(name, payload):
    """Durably replace a JSON output without exposing a partial destination."""
    target = HERE / name
    encoded = json.dumps(payload, indent=2, allow_nan=False) + "\n"
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=HERE,
            prefix=f".{target.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def archives():
    import requests
    from astroquery.mast import Observations, Tesscut

    Observations.TIMEOUT = 60
    result = {"retrieved_utc": datetime.now(timezone.utc).isoformat(), "queries": []}

    def tap(label, endpoint, query):
        row = {
            "label": label,
            "endpoint": endpoint,
            "query": query,
            "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        }
        try:
            response = requests.get(
                endpoint,
                params={
                    "REQUEST": "doQuery",
                    "LANG": "ADQL",
                    "FORMAT": "json",
                    "QUERY": query,
                },
                timeout=45,
            )
            response.raise_for_status()
            row.update(state="answered", result=response.json())
        except Exception as exc:
            row.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
        result["queries"].append(row)
        save("archive_refresh.json", result)

    for lead in CONFIG["leads"]:
        tic, slug = lead["tic"], lead["slug"]
        tap(
            slug + ":toi",
            "https://exoplanetarchive.ipac.caltech.edu/TAP/sync",
            f"SELECT * FROM toi WHERE tid = {tic}",
        )
        ids = lead["gaia"]
        if slug == "toi-3500-02":
            ids += ",3471495419656596352"
        tap(
            slug + ":gaia",
            "https://gea.esac.esa.int/tap-server/tap/sync",
            f"SELECT source_id,ra,dec,ref_epoch,pmra,pmdec,parallax,parallax_error,ruwe,non_single_star,radial_velocity,radial_velocity_error,rv_nb_transits,rv_amplitude_robust,phot_g_mean_mag FROM gaiadr3.gaia_source WHERE source_id IN ({ids})",
        )
        tap(
            slug + ":gaia_rv_quality",
            "https://gea.esac.esa.int/tap-server/tap/sync",
            f"SELECT source_id,rv_method_used,rv_visibility_periods_used,rv_expected_sig_to_noise,rv_renormalised_gof,rv_chisq_pvalue,rv_time_duration,rv_template_teff,rv_template_logg,rv_template_fe_h FROM gaiadr3.gaia_source WHERE source_id IN ({ids})",
        )
        tap(
            slug + ":nss",
            "https://gea.esac.esa.int/tap-server/tap/sync",
            f"SELECT * FROM gaiadr3.nss_two_body_orbit WHERE source_id IN ({ids})",
        )
        for selection in ("spoc", "all_target", "cone"):
            kwargs = (
                {"target_name": str(tic)}
                if selection != "cone"
                else {
                    "coordinates": f"{lead['ra']} {lead['dec']}",
                    "radius": "0.02 deg",
                }
            )
            if selection == "cone":
                kwargs["obs_collection"] = "TESS"
            if selection == "spoc":
                kwargs.update(
                    obs_collection="TESS",
                    provenance_name="SPOC",
                    dataproduct_type="timeseries",
                )
            row = {
                "label": slug + ":mast:" + selection,
                "endpoint": "MAST Observations.query_criteria",
                "query": kwargs,
            }
            try:
                table = Observations.query_criteria(**kwargs)
                keys = [
                    k
                    for k in (
                        "obsid",
                        "obs_id",
                        "target_name",
                        "obs_collection",
                        "provenance_name",
                        "sequence_number",
                        "dataURL",
                        "t_min",
                        "t_max",
                        "s_ra",
                        "s_dec",
                    )
                    if k in table.colnames
                ]
                row.update(
                    state="answered",
                    count=len(table),
                    rows=[{k: str(r[k]) for k in keys} for r in table],
                )
            except Exception as exc:
                row.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
            result["queries"].append(row)
            save("archive_refresh.json", result)
        row = {
            "label": slug + ":tesscut_sectors",
            "endpoint": "MAST Tesscut.get_sectors",
            "query": {"ra": lead["ra"], "dec": lead["dec"]},
        }
        try:
            table = Tesscut.get_sectors(coordinates=f"{lead['ra']} {lead['dec']}")
            row.update(
                state="answered",
                rows=[{k: str(r[k]) for k in table.colnames} for r in table],
            )
        except Exception as exc:
            row.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
        result["queries"].append(row)
        save("archive_refresh.json", result)
        print(slug, "archive queries recorded", flush=True)
    try:
        control = Observations.query_criteria(
            target_name="261136679",
            obs_collection="TESS",
            provenance_name="SPOC",
            dataproduct_type="timeseries",
        )
        result["control"] = {
            "tic": 261136679,
            "state": "answered",
            "count": len(control),
        }
    except Exception as exc:
        result["control"] = {"state": "unavailable", "error": str(exc)}
    save("archive_refresh.json", result)


def photometry(scratch):
    from cygnus.campaign.lightcurve import read_spoc
    from importlib.metadata import version

    rng = np.random.default_rng(CONFIG["seed"])
    out = {
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "config": CONFIG,
        "versions": {p: version(p) for p in ("numpy", "astropy", "scipy")},
        "products": [],
        "leads": {},
    }
    for lead in CONFIG["leads"]:
        slug, dur = lead["slug"], lead["duration_h"] / 24
        events = {int(s): float(t) for s, t in lead["events"]}
        excluded_times = [t for _, t in lead["events"] + lead["rejected"]]
        rows = []
        for path in sorted((scratch / ("campaign_" + slug)).glob("tess*_lc.fits")):
            lc = read_spoc(path)
            good = lc.usable
            t = lc.time_bjd[good]
            sector = int(lc.primary["SECTOR"])
            product = {
                "id": path.name,
                "archive": "MAST/TESS SPOC",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "bytes": path.stat().st_size,
                "header": lc.primary,
                "time_header": lc.table_header,
                "usable_cadences": int(good.sum()),
                "usable_bjd_bounds": [float(t.min()), float(t.max())],
            }
            out["products"].append(product)
            for channel, flux in (("SAP", lc.sap), ("PDCSAP", lc.pdc)):
                y = flux[good] / np.median(flux[good])
                for degree in (1, 2):
                    allowed = np.ones(len(t), dtype=bool)
                    for ev in excluded_times:
                        allowed &= (
                            np.abs(t - ev) > CONFIG["baseline_half_window_days"] + dur
                        )
                    centres = rng.choice(
                        t[allowed],
                        min(CONFIG["null_draws"], int(allowed.sum())),
                        replace=False,
                    )
                    null = []
                    valid_centres = []
                    for mid in centres:
                        m = box_measure(t, y, mid, dur, degree)
                        if m["state"] == "measured":
                            null.append(m["depth_ppm"])
                            valid_centres.append(float(mid))
                    threshold = float(np.quantile(null, 0.99)) if null else None
                    recovered = 0
                    injections = min(CONFIG["injections"], len(valid_centres))
                    for mid in valid_centres[:injections]:
                        injected = y.copy()
                        injected[np.abs(t - mid) <= dur / 2] -= lead["depth_ppm"] / 1e6
                        m = box_measure(t, injected, mid, dur, degree)
                        recovered += m["state"] == "measured" and m["depth_ppm"] > max(
                            threshold, 0.5 * lead["depth_ppm"]
                        )
                    row = {
                        "product": path.name,
                        "sector": sector,
                        "channel": channel,
                        "baseline_degree": degree,
                        "null_drawn": len(centres),
                        "null_covered": len(null),
                        "null_threshold_99pct_ppm": threshold,
                        "injection_depth_ppm": lead["depth_ppm"],
                        "injected": injections,
                        "recovered": int(recovered),
                        "null_centres_bjd_tdb": valid_centres,
                        "null_depths_ppm": null,
                    }
                    if sector in events:
                        m = box_measure(t, y, events[sector], dur, degree)
                        row["event"] = m
                        if m["state"] == "measured":
                            row["null_exceedances"] = int(
                                np.count_nonzero(np.asarray(null) >= m["depth_ppm"])
                            )
                    if "period_hypothesis_days" in lead:
                        p, ref = lead["period_hypothesis_days"], lead["events"][0][1]
                        predicted = []
                        for n in range(
                            int(np.floor((t.min() - ref) / p)),
                            int(np.ceil((t.max() - ref) / p)) + 1,
                        ):
                            mid = ref + n * p
                            if t.min() <= mid <= t.max():
                                predicted.append(
                                    {
                                        "cycle": n,
                                        "mid_bjd_tdb": mid,
                                        "measurement": box_measure(
                                            t, y, mid, dur, degree
                                        ),
                                    }
                                )
                        row["period_hypothesis_windows"] = predicted
                    rows.append(row)
            print(slug, sector, "photometry finished", flush=True)
            out["leads"][slug] = rows
            save("photometry.json", out)
    # Fit only a specified cycle family; neither uniqueness nor timing errors are inferred.
    times = np.asarray([t for _, t in CONFIG["leads"][0]["events"]])
    cycles = np.rint((times - times[0]) / CONFIG["leads"][0]["period_hypothesis_days"])
    design = np.column_stack([np.ones(len(times)), cycles])
    coef = np.linalg.lstsq(design, times - times[0], rcond=None)[0]
    out["toi224_fixed_cycle_fit"] = {
        "cycles": cycles.tolist(),
        "t0_bjd_tdb": float(times[0] + coef[0]),
        "period_days": float(coef[1]),
        "timing_residual_minutes": ((times - times[0] - design @ coef) * 1440).tolist(),
        "caveat": "legacy box times; no new timing covariance; S69 localization inconclusive; S106 excluded",
    }
    save("photometry.json", out)


def fetch_prfs(scratch):
    """Retrieve eight 225-KB bracketing calibration grids, cached once."""
    import requests
    from astropy.io import fits

    folder = scratch / "lead-resolution-2026-09-30" / "prf"
    folder.mkdir(parents=True, exist_ok=True)
    result = []
    for ccd, cols in ((1, (45, 557)), (2, (1580, 2092))):
        stamp = "tess2019107181900" if ccd == 1 else "tess2019107181901"
        for row in (1025, 1536):
            for col in cols:
                name = f"{stamp}-prf-1-{ccd}-row{row:04d}-col{col:04d}.fits"
                url = f"https://archive.stsci.edu/missions/tess/models/prf_fitsfiles/start_s0004/cam1_ccd{ccd}/{name}"
                path = folder / name
                if not path.exists():
                    response = requests.get(url, timeout=45)
                    response.raise_for_status()
                    path.write_bytes(response.content)
                with fits.open(path) as hdul:
                    entry = {
                        "id": name,
                        "archive": "MAST TESS UPDATED_2.0 PRF",
                        "url": url,
                        "bytes": path.stat().st_size,
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "header": {
                            k: hdul[0].header[k]
                            for k in hdul[0].header
                            if k not in ("COMMENT", "HISTORY", "")
                        },
                        "shape": list(hdul[0].data.shape),
                    }
                    result.append(entry)
    save("prf_manifest.json", result)
    print("8 PRF calibration grids retrieved", flush=True)


def cutouts(scratch):
    """Retrieve two newly useful 7x7 FFI time-series cutouts, not full FFIs."""
    from astroquery.mast import Tesscut
    from astropy.io import fits

    folder = scratch / "lead-resolution-2026-09-30" / "cutouts"
    folder.mkdir(parents=True, exist_ok=True)
    result = []
    for index, sector in ((0, 107), (1, 8)):
        lead = CONFIG["leads"][index]
        cached = list(folder.glob(f"*s{sector:04d}*.fits"))
        if not cached:
            table = Tesscut.download_cutouts(
                coordinates=f"{lead['ra']} {lead['dec']}",
                size=7,
                sector=sector,
                path=str(folder),
            )
            cached = [Path(str(row["Local Path"])) for row in table]
        for path in cached:
            with fits.open(path) as hdul:
                result.append(
                    {
                        "id": path.name,
                        "archive": "MAST TESScut calibrated FFI",
                        "sector": sector,
                        "tic": lead["tic"],
                        "query": {
                            "ra": lead["ra"],
                            "dec": lead["dec"],
                            "size_pixels": 7,
                            "sector": sector,
                        },
                        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "bytes": path.stat().st_size,
                        "primary": {
                            k: hdul[0].header.get(k)
                            for k in (
                                "CAMERA",
                                "CCD",
                                "SECTOR",
                                "TICID",
                                "RA_OBJ",
                                "DEC_OBJ",
                                "TIMESYS",
                            )
                        },
                        "time_header": {
                            k: hdul[1].header.get(k)
                            for k in (
                                "BJDREFI",
                                "BJDREFF",
                                "TIMESYS",
                                "TIMEREF",
                                "TIMEDEL",
                            )
                        },
                        "cadences": len(hdul[1].data),
                        "columns": list(hdul[1].data.names),
                    }
                )
        save("cutout_manifest.json", result)
        print(lead["slug"], sector, "FFI cutout cached", flush=True)


def sample_prf(image, xx, yy, x0, y0):
    """Sample the already pixel-integrated PRF on the 9x9 subpixel grid.

    Official FITS CRPIX is 59 (one-based); centre is 58 in numpy coordinates.
    This is bilinear interpolation, not an additional pixel integration.
    """
    from scipy.ndimage import map_coordinates

    return map_coordinates(
        image,
        [(yy - y0) * 9 + 58, (xx - x0) * 9 + 58],
        order=1,
        mode="constant",
        cval=0.0,
    )


def calibrated_prf(scratch):
    import importlib.util
    from astropy.io import fits
    from astropy.wcs import WCS
    from astropy.coordinates import SkyCoord
    from astropy.time import Time
    import astropy.units as u
    from scipy.optimize import lsq_linear

    path = ROOT / "reports/lead-followup-2026-09-27/toi3500_two_source_test.py"
    spec = importlib.util.spec_from_file_location("two_source", path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    catalog = json.loads((HERE / "archive_refresh.json").read_text())
    payload = next(
        q["result"] for q in catalog["queries"] if q["label"] == "toi-3500-02:gaia"
    )
    names = [m["name"] for m in payload["metadata"]]
    stars = {str(r[0]): dict(zip(names, r)) for r in payload["data"]}
    folder = scratch / "lead-resolution-2026-09-30" / "prf"
    manifest = json.loads((HERE / "prf_manifest.json").read_text())
    out = {
        "method": "UPDATED_2.0 calibrated PRF; OOT registration profile; 1/3/5 percent per-pixel control-flux model floors",
        "events": {},
    }
    for sector, mid, duration_h in (
        (64, 2460056.6956505855, 7.9079384),
        (90, 2460757.3198817656, 7.9079384),
    ):
        tpf = next(
            (scratch / "campaign_toi-3500-02" / "tpf").glob(f"*s{sector:04d}-*.fits")
        )
        with fits.open(tpf) as h:
            table = h[1].data
            t = (
                np.asarray(table["TIME"], float)
                + h[1].header["BJDREFI"]
                + h[1].header["BJDREFF"]
            )
            flux = np.asarray(table["FLUX"], float)
            quality = np.asarray(table["QUALITY"], int)
            hdr = h[2].header.copy()
            ccd = int(h[0].header["CCD"])
        ev, fl = old.event_selection(t, mid, duration_h, quality)
        finite = np.all(np.isfinite(flux.reshape(len(t), -1)), axis=1)
        ev &= finite
        fl &= finite
        diff, noise = old.difference_and_noise(t, flux, ev, fl)
        control = flux[fl].mean(axis=0)
        wcs = WCS(hdr)
        xy = []
        for sid in ("3471495415361216512", "3471495419656596352"):
            star = stars[sid]
            coord = SkyCoord(
                ra=star["ra"] * u.deg,
                dec=star["dec"] * u.deg,
                pm_ra_cosdec=star["pmra"] * u.mas / u.yr,
                pm_dec=star["pmdec"] * u.mas / u.yr,
                obstime=Time(star["ref_epoch"], format="jyear"),
            )
            prop = coord.apply_space_motion(
                new_obstime=Time(mid, format="jd", scale="tdb")
            )
            xy.append(np.asarray(wcs.world_to_pixel_values(prop.ra.deg, prop.dec.deg)))
        col = hdr["CRVAL1P"] + xy[0][0] - (hdr["CRPIX1P"] - 1)
        row = hdr["CRVAL2P"] + xy[0][1] - (hdr["CRPIX2P"] - 1)
        entries = [m for m in manifest if int(m["header"]["CCD"]) == ccd]
        cols = sorted({m["header"]["CCD_CREF"] for m in entries})
        rs = sorted({m["header"]["CCD_RREF"] for m in entries})
        a = (col - cols[0]) / (cols[1] - cols[0])
        b = (row - rs[0]) / (rs[1] - rs[0])
        assert 0 <= a <= 1 and 0 <= b <= 1, (
            "PRF interpolation must bracket detector location"
        )
        image = np.zeros((117, 117))
        for m in entries:
            wc = a if m["header"]["CCD_CREF"] == cols[1] else 1 - a
            wr = b if m["header"]["CCD_RREF"] == rs[1] else 1 - b
            with fits.open(folder / m["id"]) as h:
                image += wc * wr * h[0].data
        yy, xx = np.indices(diff.shape)
        mask = np.hypot(xx - xy[0][0], yy - xy[0][1]) <= 3
        back = np.column_stack(
            [np.ones(mask.sum()), xx[mask] - xy[0][0], yy[mask] - xy[0][1]]
        )
        trials = []
        for floor in (0.01, 0.03, 0.05):
            sigma = np.sqrt(noise[mask] ** 2 + (floor * np.abs(control[mask])) ** 2)
            for dx in np.linspace(-0.2, 0.2, 21):
                for dy in np.linspace(-0.2, 0.2, 21):
                    tm = sample_prf(image, xx, yy, xy[0][0] + dx, xy[0][1] + dy)[mask]
                    nm = sample_prf(image, xx, yy, xy[1][0] + dx, xy[1][1] + dy)[mask]
                    design = np.column_stack([tm, nm, back])
                    oot = lsq_linear(
                        design / sigma[:, None],
                        control[mask] / sigma,
                        bounds=([0, 0, -np.inf, -np.inf, -np.inf], [np.inf] * 5),
                    )
                    oot_chi = float(
                        np.sum((control[mask] / sigma - design @ oot.x / sigma) ** 2)
                    )
                    tc, tc2 = old.weighted_fit(diff[mask], sigma, [tm, *back.T])
                    nc, nc2 = old.weighted_fit(diff[mask], sigma, [nm, *back.T])
                    corr, cond = old.residualized_source_correlation(
                        tm, nm, back, sigma
                    )
                    trials.append(
                        {
                            "model_floor": floor,
                            "dx": float(dx),
                            "dy": float(dy),
                            "oot_chi2": oot_chi,
                            "oot_residual_peak_fraction": float(
                                np.max(np.abs(control[mask] - design @ oot.x))
                                / np.max(control[mask])
                            ),
                            "delta_chi2_neighbour_minus_target": nc2 - tc2,
                            "source_correlation": corr,
                            "condition": cond,
                            "target_amplitude": float(tc[0]),
                            "neighbour_amplitude": float(nc[0]),
                        }
                    )
        summaries = []
        for floor in (0.01, 0.03, 0.05):
            rows = [r for r in trials if r["model_floor"] == floor]
            best = min(rows, key=lambda r: r["oot_chi2"])
            accepted = [r for r in rows if r["oot_chi2"] <= best["oot_chi2"] + 9]
            deltas = [r["delta_chi2_neighbour_minus_target"] for r in accepted]
            summaries.append(
                {
                    "model_floor": floor,
                    "best_oot": best,
                    "accepted_registration_trials": len(accepted),
                    "delta_chi2_range": [min(deltas), max(deltas)],
                    "target_preference_fraction": float(
                        np.mean(np.asarray(deltas) > 0)
                    ),
                }
            )
        out["events"][str(sector)] = {
            "tpf": tpf.name,
            "sha256": hashlib.sha256(tpf.read_bytes()).hexdigest(),
            "time_bjd_tdb": mid,
            "proper_motion_propagated_pixels": [z.tolist() for z in xy],
            "raw_detector_col_row": [float(col), float(row)],
            "prf_inputs": [m["id"] for m in entries],
            "summaries": summaries,
            "trials": trials,
            "caveat": "profile grid and model floors are sensitivity choices; correlated pixel noise and calibration covariance not fully modeled; no orbital inference",
        }
        save("calibrated_prf.json", out)
        print("TOI3500 calibrated PRF sector", sector, "finished", flush=True)


def ffi_photometry(scratch):
    from astropy.io import fits
    from astropy.wcs import WCS

    manifest = json.loads((HERE / "cutout_manifest.json").read_text())
    previous = json.loads((HERE / "photometry.json").read_text())
    out = {
        "time_caveat": "TESScut TDB times retain CCD-centre barycentric correction; not precise target BJD_TDB timing. No high precision timing claim.",
        "products": [],
    }
    rng = np.random.default_rng(CONFIG["seed"])
    for item in manifest:
        lead = next(entry for entry in CONFIG["leads"] if entry["tic"] == item["tic"])
        path = scratch / "lead-resolution-2026-09-30" / "cutouts" / item["id"]
        with fits.open(path) as h:
            t = (
                np.asarray(h[1].data["TIME"], float)
                + h[1].header["BJDREFI"]
                + h[1].header["BJDREFF"]
            )
            flux = np.asarray(h[1].data["FLUX"], float)
            quality = np.asarray(h[1].data["QUALITY"], int)
            xy = WCS(h[2].header).world_to_pixel_values(lead["ra"], lead["dec"])
        yy, xx = np.indices(flux.shape[1:])
        rad = np.hypot(xx - xy[0], yy - xy[1])
        background = np.nanmedian(flux[:, rad > 3.0], axis=1)
        rows = []
        dur = lead["duration_h"] / 24
        for aperture in (1.5, 2.0):
            ap = rad <= aperture
            series = np.sum(flux[:, ap], axis=1) - ap.sum() * background
            good = (quality == 0) & np.isfinite(t) & np.isfinite(series)
            tt = t[good]
            y = series[good] / np.median(series[good])
            for degree in (1, 2):
                row = {
                    "aperture_radius_pix": aperture,
                    "baseline_degree": degree,
                    "usable": int(good.sum()),
                    "bjd_ccd_bounds": [float(tt.min()), float(tt.max())],
                    "quality_rule": "QUALITY==0; finite aperture sum and timestamp",
                }
                centres = np.arange(tt.min() + 0.75, tt.max() - 0.75, dur / 2)
                scan = [
                    (float(mid), box_measure(tt, y, mid, dur, degree))
                    for mid in centres
                ]
                covered = [(m, r) for m, r in scan if r["state"] == "measured"]
                row["grid_trials"] = len(scan)
                row["covered_trials"] = len(covered)
                row["deepest_windows"] = sorted(
                    [{"mid_bjd_ccd_tdb": m, **r} for m, r in covered],
                    key=lambda r: r["depth_ppm"],
                    reverse=True,
                )[:10]
                if "period_hypothesis_days" in lead:
                    fit = previous["toi224_fixed_cycle_fit"]
                    p = fit["period_days"]
                    ref = fit["t0_bjd_tdb"]
                    predictions = []
                    for n in range(
                        int(np.floor((tt.min() - ref) / p)),
                        int(np.ceil((tt.max() - ref) / p)) + 1,
                    ):
                        mid = ref + n * p
                        if not tt.min() <= mid <= tt.max():
                            continue
                        measurement = box_measure(tt, y, mid, dur, degree)
                        injected = y.copy()
                        in_ev = np.abs(tt - mid) <= dur / 2
                        injected[in_ev] -= lead["depth_ppm"] / 1e6
                        inject = box_measure(tt, injected, mid, dur, degree)
                        predictions.append(
                            {
                                "cycle": n,
                                "mid_target_hypothesis_bjd_tdb": mid,
                                "measurement": measurement,
                                "fixed_window_injection": inject,
                            }
                        )
                    row["predictions"] = predictions
                null_candidates = [(m, r) for m, r in covered]
                if null_candidates:
                    choices = rng.choice(
                        len(null_candidates),
                        min(100, len(null_candidates)),
                        replace=False,
                    )
                    recovered = 0
                    threshold = np.quantile(
                        [r["depth_ppm"] for _, r in null_candidates], 0.99
                    )
                    for ix in choices:
                        mid, _ = null_candidates[int(ix)]
                        inj = y.copy()
                        inj[np.abs(tt - mid) <= dur / 2] -= lead["depth_ppm"] / 1e6
                        result = box_measure(tt, inj, mid, dur, degree)
                        recovered += result["state"] == "measured" and result[
                            "depth_ppm"
                        ] > max(threshold, 0.5 * lead["depth_ppm"])
                    row["injections"] = {
                        "draws": len(choices),
                        "recovered": int(recovered),
                        "depth_ppm": lead["depth_ppm"],
                        "threshold99_ppm": float(threshold),
                    }
                rows.append(row)
        localization = None
        if item["sector"] == 107:
            # Hold-out event is fitted on its own, with no prior depth constraint.
            fit = previous["toi224_fixed_cycle_fit"]
            pred = fit["t0_bjd_tdb"] + 92 * fit["period_days"]
            aperture = rad <= 2.0
            series = np.sum(flux[:, aperture], axis=1) - aperture.sum() * background
            ok = (quality == 0) & np.isfinite(t) & np.isfinite(series)
            tt = t[ok]
            y = series[ok] / np.median(series[ok])
            grid = np.arange(pred - dur, pred + dur, 200 / 86400 / 2)
            fits_grid = [(float(mid), box_measure(tt, y, mid, dur, 2)) for mid in grid]
            best = min(
                [(m, r) for m, r in fits_grid if r["state"] == "measured"],
                key=lambda mr: mr[1]["residual_rms_ppm"],
            )
            mid = best[0]
            window = (
                ok & (np.abs(t - mid) <= 0.75) & np.all(np.isfinite(flux), axis=(1, 2))
            )
            tw = t[window] - mid
            cube = flux[window].reshape(window.sum(), -1)
            event = np.abs(tw) <= dur / 2
            design = np.column_stack(
                [np.ones(len(tw)), tw, tw**2, -event.astype(float)]
            )
            coeff = np.linalg.lstsq(design, cube, rcond=None)[0]
            diff = coeff[-1].reshape(rad.shape)
            control = coeff[0].reshape(rad.shape)
            residual = cube - design @ coeff

            def centroid(img):
                values = np.where(rad <= 2.5, np.clip(img, 0, None), 0)
                return (
                    np.array([(values * xx).sum(), (values * yy).sum()]) / values.sum()
                )

            cc = centroid(control - np.median(control[rad > 3.0]))
            dc = centroid(diff)
            offsets = []
            length = 5
            for _ in range(300):
                starts = rng.integers(
                    0, len(tw) - length + 1, size=int(np.ceil(len(tw) / length))
                )
                idx = np.concatenate([np.arange(s, s + length) for s in starts])[
                    : len(tw)
                ]
                simulated = design @ coeff + residual[idx]
                bc = np.linalg.lstsq(design, simulated, rcond=None)[0]
                offsets.append(centroid(bc[-1].reshape(rad.shape)) - cc)
            boot = np.asarray(offsets)
            sigma = boot.std(axis=0, ddof=1)
            pixel_scale = (
                21.0  # approximate TESS angular pixel scale, not a WCS error model
            )
            offset = dc - cc
            localization = {
                "mid_bjd_ccd_tdb": mid,
                "duration_fixed_h": lead["duration_h"],
                "box_measurement": best[1],
                "timing_caveat": "minimum-RMS fixed-duration box grid; no timing posterior; CCD-centre barycentric time retained",
                "event_cadences": int(event.sum()),
                "difference_image": diff.tolist(),
                "control_image": control.tolist(),
                "control_centroid_xy": cc.tolist(),
                "difference_centroid_xy": dc.tolist(),
                "offset_arcsec": float(np.linalg.norm(offset) * pixel_scale),
                "bootstrap_sigma_pix": sigma.tolist(),
                "offset_over_bootstrap_sigma": float(
                    np.linalg.norm(offset) / np.linalg.norm(sigma)
                ),
                "block_length_cadences": length,
                "bootstrap_draws": 300,
                "note": "positive difference centroid in radius2.5; block residual bootstrap; no close-companion separation or PRF/WCS covariance",
                "background_box": box_measure(t[ok], background[ok], mid, dur, 2),
            }
            save("ffi_localization.json", localization)
        out["products"].append(
            {
                "id": item["id"],
                "tic": lead["tic"],
                "sector": item["sector"],
                "cadence_s": float(np.nanmedian(np.diff(t))) * 86400,
                "rows": rows,
                "localization": localization,
            }
        )
        save("ffi_photometry.json", out)
        print(lead["slug"], item["sector"], "FFI photometry complete", flush=True)


def coarse_alias_test(scratch):
    """Conditional alias exclusions using exposure integration and timing slack."""
    from astropy.io import fits
    from astropy.wcs import WCS

    lead = CONFIG["leads"][1]
    path = next(
        (scratch / "lead-resolution-2026-09-30" / "cutouts").glob("*s0008*.fits")
    )
    with fits.open(path) as h:
        t = np.asarray(h[1].data["TIME"], float) + h[1].header["BJDREFI"]
        flux = np.asarray(h[1].data["FLUX"], float)
        quality = np.asarray(h[1].data["QUALITY"], int)
        xy = WCS(h[2].header).world_to_pixel_values(lead["ra"], lead["dec"])
    yy, xx = np.indices(flux.shape[1:])
    radius = np.hypot(xx - xy[0], yy - xy[1])
    background = np.nanmedian(flux[:, radius > 3], axis=1)
    vet = json.loads((ROOT / "campaigns/toi-2666-01/vetting/vetting.json").read_text())
    original = vet["events"][0]["aliases_from_reference"]
    dt = lead["events"][1][1] - lead["events"][0][1]
    ref = lead["events"][0][1]
    rows = []
    for rounded in original["allowed_periods_days"]:
        n = int(round(dt / rounded))
        p = dt / n
        cycles = range(
            int(np.floor((np.nanmin(t) - ref) / p)),
            int(np.ceil((np.nanmax(t) - ref) / p)) + 1,
        )
        predictions = [
            ref + k * p for k in cycles if np.nanmin(t) <= ref + k * p <= np.nanmax(t)
        ]
        trials = []
        for mid in predictions:
            for ap_radius in (1.5, 2.0):
                ap = radius <= ap_radius
                series = flux[:, ap].sum(axis=1) - ap.sum() * background
                good = (quality == 0) & np.isfinite(t) & np.isfinite(series)
                tt = t[good]
                y = series[good] / np.median(series[good])
                for degree in (1, 2):
                    for duration_h in (1.156, 1.445):
                        dur = duration_h / 24
                        for shift in np.linspace(-0.05, 0.05, 11):
                            center = mid + shift
                            m = box_measure(
                                tt,
                                y,
                                center,
                                dur,
                                degree,
                                exposure=1 / 48,
                                min_points=2,
                            )
                            w = (
                                np.clip(
                                    np.minimum(tt + 1 / 96, center + dur / 2)
                                    - np.maximum(tt - 1 / 96, center - dur / 2),
                                    0,
                                    1 / 48,
                                )
                                * 48
                            )
                            injected = box_measure(
                                tt,
                                y - lead["depth_ppm"] / 1e6 * w,
                                center,
                                dur,
                                degree,
                                exposure=1 / 48,
                                min_points=2,
                            )
                            reject = (
                                m["state"] == "measured"
                                and m["depth_ppm"] < 0.3 * lead["depth_ppm"]
                                and injected["state"] == "measured"
                                and injected["depth_ppm"] - m["depth_ppm"]
                                > 0.5 * lead["depth_ppm"]
                            )
                            trials.append(
                                {
                                    "mid_bjd_ccd_tdb": float(center),
                                    "aperture_radius_pix": ap_radius,
                                    "baseline_degree": degree,
                                    "duration_h": duration_h,
                                    "measurement": m,
                                    "injection": injected,
                                    "conditional_reject": bool(reject),
                                }
                            )
        rows.append(
            {
                "cycle_divisor": n,
                "period_days": p,
                "predictions_bjd_tdb": predictions,
                "state": "conditional_exclusion"
                if trials and all(r["conditional_reject"] for r in trials)
                else "not_excluded",
                "trials": trials,
            }
        )
    save(
        "toi2666_s8_aliases.json",
        {
            "method": "exposure-integrated 30-min box; two apertures, linear/quadratic baselines; durations1.156/1.445h; timing slack plus/minus.05d; fixed-window injections",
            "caveat": "conditional equal-depth box-model exclusions, not arbitrary eclipse/TTV model rejection; uncertainty posterior and full noise covariance not available",
            "product": path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "baseline_aliases": len(rows),
            "excluded": sum(r["state"] == "conditional_exclusion" for r in rows),
            "aliases": rows,
        },
    )
    print("TOI2666 S8 conditional aliases tested", flush=True)


def download_spectra(scratch, limit, target=None):
    """Inspect DATALINK and size, then cache bounded public science spectra."""
    import io
    import requests
    from astropy.io import fits
    from astropy.io.votable import parse_single_table

    queries = json.loads((HERE / "rv_name_archive.json").read_text())["queries"]
    folder = scratch / "lead-resolution-2026-09-30" / "spectra"
    folder.mkdir(parents=True, exist_ok=True)
    prior = HERE / "spectra_manifest.json"
    out = json.loads(prior.read_text()) if prior.exists() else {"products": []}
    seen = {
        entry["datalink"] for entry in out["products"] if entry["state"] == "downloaded"
    }
    for query in queries:
        if query["target"].startswith("control-"):
            continue
        if target is not None and query["target"] != target:
            continue
        for row in query.get("rows", [])[:limit]:
            link = row["access_url"]
            if link in seen:
                continue
            entry = {
                "target": query["target"],
                "archive": "ESO Phase3 public spectra",
                "datalink": link,
                "source_row": row,
                "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            }
            try:
                response = requests.get(link, timeout=45)
                response.raise_for_status()
                table = parse_single_table(io.BytesIO(response.content)).to_table()
                links = [{key: str(r[key]) for key in table.colnames} for r in table]
                entry["links"] = links
                science = [
                    r
                    for r in links
                    if r.get("semantics") == "#this"
                    and r.get("access_url", "").startswith("https://")
                ]
                if not science:
                    raise ValueError("No science #this DATALINK URL")
                product = science[0]
                size = int(product.get("content_length", "0") or "0")
                if size > 25_000_000:
                    raise ValueError(
                        f"resource screen: {size}bytes exceeds25MB per spectrum"
                    )
                url = product["access_url"]
                name = link.split("ADP.")[-1].split("&")[0]
                filename = "ADP." + name + ".fits"
                path = folder / filename.replace(":", "-")
                if not path.exists():
                    data = requests.get(url, timeout=90)
                    data.raise_for_status()
                    path.write_bytes(data.content)
                with fits.open(path, memmap=True) as h:
                    header = {
                        k: h[0].header[k]
                        for k in h[0].header
                        if k not in ("COMMENT", "HISTORY", "")
                    }
                entry.update(
                    state="downloaded",
                    id=filename,
                    url=url,
                    bytes=path.stat().st_size,
                    sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    header=header,
                )
            except Exception as exc:
                entry.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
            out["products"].append(entry)
            seen.add(link)
            save("spectra_manifest.json", out)
            print(
                query["target"],
                entry["state"],
                entry.get("bytes", entry.get("error")),
                flush=True,
            )


def harps_bundles(scratch, limit):
    """Read CCF headers directly inside public TARs without extracting paths."""
    import io
    import tarfile
    import requests
    from astropy.io import fits
    from astropy.io.votable import parse_single_table

    rows = next(
        q["rows"]
        for q in json.loads((HERE / "rv_name_archive.json").read_text())["queries"]
        if q["target"] == "toi-3500-02"
    )
    folder = scratch / "lead-resolution-2026-09-30" / "harps"
    folder.mkdir(parents=True, exist_ok=True)
    prior = HERE / "harps_rv.json"
    out = json.loads(prior.read_text()) if prior.exists() else {"products": []}
    seen = {r["datalink"] for r in out["products"] if r["state"] == "downloaded"}
    for row in rows[:limit]:
        if row["instrument_name"] != "HARPS":
            continue
        link = row["access_url"]
        if link in seen:
            continue
        entry = {
            "datalink": link,
            "source_row": row,
            "archive": "ESO HARPS DRS3.8 ancillary pipeline products",
        }
        try:
            response = requests.get(link, timeout=45)
            response.raise_for_status()
            table = parse_single_table(io.BytesIO(response.content)).to_table()
            bundles = [
                r
                for r in table
                if str(r["semantics"]) == "#auxiliary"
                and "tar" in str(r["content_type"])
            ]
            if not bundles:
                raise ValueError("No ancillary HARPS TAR")
            bundle = bundles[0]
            size = int(bundle["content_length"])
            if size > 25_000_000:
                raise ValueError("resource limit25MB/bundle")
            url = str(bundle["access_url"])
            pid = url.rsplit("/", 1)[-1]
            path = folder / (pid.replace(":", "-") + ".tar")
            if not path.exists():
                data = requests.get(url, timeout=90)
                data.raise_for_status()
                path.write_bytes(data.content)
            ccfs = []
            with tarfile.open(path) as archive:
                members = archive.getmembers()
                entry["members"] = [m.name for m in members]
                for member in members:
                    if "ccf" not in member.name.lower() or not member.name.endswith(
                        "_A.fits"
                    ):
                        continue
                    raw = archive.extractfile(member).read()
                    with fits.open(io.BytesIO(raw)) as h:
                        header = {
                            k: h[0].header[k]
                            for k in h[0].header
                            if k not in ("COMMENT", "HISTORY", "")
                        }
                    ccfs.append(
                        {
                            "member": member.name,
                            "sha256": hashlib.sha256(raw).hexdigest(),
                            "header": header,
                        }
                    )
            entry.update(
                state="downloaded",
                id=pid,
                url=url,
                bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                ccfs=ccfs,
            )
        except Exception as exc:
            entry.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
        out["products"].append(entry)
        seen.add(link)
        save("harps_rv.json", out)
        print("HARPS bundle", entry["state"], len(entry.get("ccfs", [])), flush=True)


def range_ccfs(url):
    """Read only TAR headers and science-fibre CCF members using HTTP Range.

    No arbitrary TAR paths are extracted. Exact member bytes are hashed;
    an entire-bundle checksum is not asserted for sparse retrieval.
    """
    import io
    import tarfile
    import requests
    from astropy.io import fits

    transferred = 0

    def read_range(start, length):
        nonlocal transferred
        with requests.get(
            url,
            headers={"Range": f"bytes={start}-{start + length - 1}"},
            stream=True,
            timeout=45,
        ) as response:
            response.raise_for_status()
            if response.status_code != 206:
                raise ValueError(
                    "archive does not honor HTTP Range; resource screen retained"
                )
            data = response.raw.read(length)
            if len(data) != length:
                raise ValueError("incomplete range")
            transferred += len(data)
            return data

    offset = 0
    members = []
    ccfs = []
    for _ in range(200):
        block = read_range(offset, 512)
        if block == b"\0" * 512:
            break
        member = tarfile.TarInfo.frombuf(block, "utf-8", "replace")
        members.append({"name": member.name, "size": member.size, "offset": offset})
        if "ccf" in member.name.lower() and member.name.endswith("_A.fits"):
            if member.size > 5_000_000:
                raise ValueError("CCF member exceeds5MB")
            raw = read_range(offset + 512, member.size)
            with fits.open(io.BytesIO(raw)) as h:
                header = {
                    k: h[0].header[k]
                    for k in h[0].header
                    if k not in ("COMMENT", "HISTORY", "")
                }
            ccfs.append(
                {
                    "member": member.name,
                    "sha256": hashlib.sha256(raw).hexdigest(),
                    "header": header,
                }
            )
        offset += 512 + ((member.size + 511) // 512) * 512
    return ccfs, members, transferred


def stream_ccfs(url, folder):
    """Stream compressed TAR, retain the exact target CCF, never extract paths."""
    import io
    import tarfile
    import requests
    from astropy.io import fits

    folder.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=90) as response:
        response.raise_for_status()
        ccfs = []
        with tarfile.open(fileobj=response.raw, mode="r|gz") as archive:
            for member in archive:
                if "ccf" not in member.name.lower() or not member.name.endswith(
                    "_A.fits"
                ):
                    continue
                if member.size > 5_000_000:
                    raise ValueError("CCF member exceeds5MB")
                raw = archive.extractfile(member).read()
                digest = hashlib.sha256(raw).hexdigest()
                (folder / (digest + ".fits")).write_bytes(raw)
                with fits.open(io.BytesIO(raw)) as h:
                    header = {
                        k: h[0].header[k]
                        for k in h[0].header
                        if k not in ("COMMENT", "HISTORY", "")
                    }
                ccfs.append(
                    {
                        "member": member.name,
                        "sha256": digest,
                        "header": header,
                        "cache_file": digest + ".fits",
                    }
                )
                # Only the first target-fibre mask is retained; its identity is explicit.
                break
        return ccfs


def sparse_harps(limit, scratch):
    import io
    import requests
    from astropy.io.votable import parse_single_table

    rows = next(
        q["rows"]
        for q in json.loads((HERE / "rv_name_archive.json").read_text())["queries"]
        if q["target"] == "toi-3500-02"
    )
    prior = HERE / "harps_rv.json"
    out = json.loads(prior.read_text())
    seen = {
        r["datalink"]
        for r in out["products"]
        if r["state"] in ("downloaded", "sparse_ccf")
    }
    pending = [r for r in rows if r["access_url"] not in seen][:limit]
    for row in pending:
        if row["instrument_name"] != "HARPS":
            continue
        link = row["access_url"]
        entry = {
            "datalink": link,
            "source_row": row,
            "archive": "ESO HARPS sparse ancillary CCF",
        }
        try:
            response = requests.get(link, timeout=45)
            response.raise_for_status()
            table = parse_single_table(io.BytesIO(response.content)).to_table()
            bundle = next(
                r
                for r in table
                if str(r["semantics"]) == "#auxiliary"
                and "tar" in str(r["content_type"])
            )
            url = str(bundle["access_url"])
            size = int(bundle["content_length"])
            if size > 120_000_000:
                raise ValueError("resource screen: compressed bundle exceeds120MB")
            ccfs = stream_ccfs(url, scratch / "lead-resolution-2026-09-30" / "ccfs")
            if not ccfs:
                raise ValueError("TAR has no recognized target-fibre CCF")
            entry.update(
                state="sparse_ccf",
                id=url.rsplit("/", 1)[-1],
                url=url,
                full_bundle_bytes=size,
                ccfs=ccfs,
                retrieval="gzip streaming until first target-fibre CCF; exact member retained; full bundle not retained or hashed",
            )
        except Exception as exc:
            entry.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
        out["products"].append(entry)
        save("harps_rv.json", out)
        print(
            "Sparse HARPS",
            entry["state"],
            entry.get("bytes_transferred", entry.get("error")),
            flush=True,
        )


def rv_linear_fit(rv, sigma, template, nuisance):
    design = np.column_stack([nuisance, template])
    weighted = design / sigma[:, None]
    coeff = np.linalg.lstsq(weighted, rv / sigma, rcond=None)[0]
    residual = rv - design @ coeff
    covariance = np.linalg.pinv(weighted.T @ weighted)
    return {
        "semiamplitude_kms": float(coeff[-1]),
        "formal_error_kms": float(np.sqrt(covariance[-1, -1])),
        "residual_rms_kms": float(np.sqrt(np.mean(residual**2))),
        "chi2": float(np.sum((residual / sigma) ** 2)),
    }


def rv_template(time, period, transit, eccentricity, omega):
    f_transit = np.pi / 2 - omega
    e_transit = 2 * np.arctan2(
        np.sqrt(1 - eccentricity) * np.sin(f_transit / 2),
        np.sqrt(1 + eccentricity) * np.cos(f_transit / 2),
    )
    m_transit = e_transit - eccentricity * np.sin(e_transit)
    mean = (2 * np.pi * (time - transit) / period + m_transit + np.pi) % (
        2 * np.pi
    ) - np.pi
    eccentric = mean.copy()
    for _ in range(60):
        step = (eccentric - eccentricity * np.sin(eccentric) - mean) / (
            1 - eccentricity * np.cos(eccentric)
        )
        eccentric -= np.clip(step, -1.0, 1.0)
    if np.max(np.abs(eccentric - eccentricity * np.sin(eccentric) - mean)) > 1e-8:
        raise ValueError("Kepler solver did not converge")
    true = 2 * np.arctan2(
        np.sqrt(1 + eccentricity) * np.sin(eccentric / 2),
        np.sqrt(1 - eccentricity) * np.cos(eccentric / 2),
    )
    return np.cos(true + omega) + eccentricity * np.cos(omega)


def harps_profiles():
    """Conditional circular profiles; sparse sampling cannot identify an orbit."""
    archive = json.loads((HERE / "harps_rv.json").read_text())
    epochs = {}
    for product in archive["products"]:
        if product.get("source_row", {}).get("instrument_name") != "HARPS":
            continue
        for ccf in product.get("ccfs", []):
            h = ccf["header"]
            if h.get("ESO DRS CCF MASK") != "G2":
                continue
            t = float(h["ESO DRS BJD"])
            epochs[t] = {
                "bjd_tdb": t,
                "rv_kms": float(h["ESO DRS CCF RVC"]),
                "formal_error_kms": float(h["ESO DRS CCF NOISE"]),
                "fwhm_kms": float(h["ESO DRS CCF FWHM"]),
                "member": ccf["member"],
                "sha256": ccf["sha256"],
                "datalink": product["datalink"],
                "pipeline": h.get("ESO DRS VERSION"),
                "object": h.get("OBJECT"),
            }
    rows = sorted(epochs.values(), key=lambda r: r["bjd_tdb"])
    t = np.array([r["bjd_tdb"] for r in rows])
    v = np.array([r["rv_kms"] for r in rows])
    err = np.array([r["formal_error_kms"] for r in rows])
    if len(rows) < 5 or np.any(err <= 0):
        raise ValueError("Insufficient valid HARPS epochs")
    frozen = json.loads(
        (HERE.parents[1] / "campaigns/toi-3500-02/vetting/vetting.json").read_text()
    )
    aliases = frozen["events"][0]["aliases_from_reference"]
    transit = aliases["reference_bjd"]
    profile = []
    for nuisance_model in ("constant", "constant_plus_sibling_free_phase"):
        columns = [np.ones(len(t))]
        if nuisance_model.endswith("free_phase"):
            phase = 2 * np.pi * (t - t.mean()) / 7.3436151
            columns.extend((np.sin(phase), np.cos(phase)))
        nuisance = np.column_stack(columns)
        for jitter in (0.0, 0.01, 0.05, 0.1):
            sigma = np.sqrt(err**2 + jitter**2)
            baseline = rv_linear_fit(v, sigma, np.zeros(len(t)), nuisance)
            for period in aliases["allowed_periods_days"]:
                fit = rv_linear_fit(
                    v, sigma, rv_template(t, period, transit, 0.0, 0.0), nuisance
                )
                profile.append(
                    {
                        "period_days": period,
                        "nuisance_model": nuisance_model,
                        "adopted_jitter_kms": jitter,
                        "sensitivity_only_density_rejected": period < 35.0,
                        "residual_dof": len(t) - nuisance.shape[1] - 1,
                        "baseline_chi2": baseline["chi2"],
                        **fit,
                    }
                )
    save(
        "harps_profiles.json",
        {
            "epochs": rows,
            "count": len(rows),
            "time_standard": "HARPS DRS barycentric Julian day; interpreted as BJD_TDB per instrument documentation, exact original headers retained",
            "rv_unit": "km/s, corrected RVC rather than uncorrected RV",
            "span_days": float(np.ptp(t)),
            "range_kms": float(np.ptp(v)),
            "median_formal_error_kms": float(np.median(err)),
            "constant_rms_kms": float(np.std(v)),
            "rv_fwhm_pearson": float(
                np.corrcoef(v, [r["fwhm_kms"] for r in rows])[0, 1]
            ),
            "profiles": profile,
            "caveats": [
                "Only six public HARPS epochs;18 additional metadata rows return HTTP401 for ancillary products.",
                "Signed K is a conditional linear coefficient, not a validated orbital semiamplitude or companion mass.",
                "Circular edge-on transit hypothesis only; eccentric orbits, offsets, activity and unresolved source alternatives remain.",
                "Known7.3436151-day sibling permitted a free sinusoidal phase/amplitude as nuisance.",
                "Formal errors exclude stellar jitter and correlated calibration; jitter choices are sensitivity assumptions.",
                "16 baseline aliases retained; extra18.4375-day density-rejected row shown only as sensitivity. No alias rejected by these profiles.",
                "No search-wide false-alarm probability or RV detection claim from this small sample.",
            ],
        },
    )
    print("HARPS conditional profiles", len(rows), "epochs", flush=True)


def spectral_shift(velocity, template, observed):
    """Relative logarithmic Doppler shift; positive means redshift."""
    from scipy.signal import correlate, correlation_lags
    from scipy.optimize import minimize_scalar

    step = float(np.median(np.diff(velocity)))
    correlation = correlate(observed, template, mode="full", method="fft")
    lags = correlation_lags(len(observed), len(template)) * step
    selected = np.abs(lags) < 100.0
    peak = lags[selected][np.argmax(correlation[selected])]
    keep = (velocity > velocity.min() + 110) & (velocity < velocity.max() - 110)
    # For narrow synthetic controls use a smaller edge trim.
    if np.count_nonzero(keep) < 10:
        keep = (velocity > velocity.min() + 20) & (velocity < velocity.max() - 20)

    def objective(shift):
        model = np.interp(velocity[keep] - shift, velocity, template)
        y = observed[keep]
        scale = np.dot(y, model) / np.dot(model, model)
        return np.mean((y - scale * model) ** 2)

    fit = minimize_scalar(
        objective,
        bounds=(peak - step, peak + step),
        method="bounded",
        options={"xatol": 1e-7},
    )
    return float(fit.x)


def relative_spectra(scratch):
    """Air-wavelength barycentric science spectra; block scatter is descriptive."""
    from astropy.io import fits
    from scipy.ndimage import median_filter

    manifest = json.loads((HERE / "spectra_manifest.json").read_text())
    groups = {}
    for product in manifest["products"]:
        if product["state"] != "downloaded":
            continue
        instrument = product["header"].get("INSTRUME")
        groups.setdefault((product["target"], instrument), {})[product["id"]] = product
    out = {
        "method": "Continuum median filtering, six disjoint air-wavelength blocks, logarithmic0.5km/s resampling, FFT coarse CCF and interpolated least-squares subpixel shift. Separate instrument templates; no cross-instrument zero point.",
        "blocks_angstrom": [
            [5000, 5200],
            [5200, 5400],
            [5400, 5600],
            [5600, 5800],
            [6000, 6200],
            [6400, 6500],
        ],
        "caveats": [
            "Relative shifts only; blended SB2 profiles can change shape rather than translate.",
            "Block scatter is descriptive; not a validated uncertainty or independent-noise standard error.",
            "Interpolation, blaze/continuum variations, tellurics and template covariance remain.",
            "BARYCENT header required; no barycentric correction added twice. No orbit or mass inference.",
        ],
        "groups": [],
    }
    folder = scratch / "lead-resolution-2026-09-30" / "spectra"
    for (target, instrument), products in groups.items():
        if len(products) < 2:
            continue
        ordered = sorted(products.values(), key=lambda p: float(p["header"]["MJD-OBS"]))
        processed = []
        for product in ordered:
            path = folder / product["id"].replace(":", "-")
            if product["header"].get("SPECSYS") != "BARYCENT":
                raise ValueError("Not barycentric science spectrum")
            with fits.open(path) as h:
                wave = np.array(h[1].data["WAVE"][0], dtype=float)
                flux = np.array(h[1].data["FLUX"][0], dtype=float)
                if (
                    h[1].header.get("TUNIT1") != "angstrom"
                    or h[1].header.get("TUCD1") != "em.wl;obs.atmos"
                ):
                    raise ValueError("Unexpected wavelength unit/frame")
            blocks = []
            for lo, hi in out["blocks_angstrom"]:
                use = (wave >= lo) & (wave <= hi) & np.isfinite(flux) & (flux > 0)
                if np.count_nonzero(use) < 500:
                    raise ValueError("Spectrum block insufficient")
                w = wave[use]
                f = flux[use]
                continuum = median_filter(f, size=301, mode="nearest")
                velocity = np.arange(0.0, 299792.458 * np.log(hi / lo), 0.5)
                normalized = np.interp(
                    velocity, 299792.458 * np.log(w / lo), f / continuum - 1.0
                )
                blocks.append((velocity, normalized))
            processed.append((product, blocks))
        reference, templates = processed[0]
        rows = []
        for product, blocks in processed:
            shifts = [
                spectral_shift(grid, templ, observed)
                for (grid, templ), (_, observed) in zip(templates, blocks)
            ]
            rows.append(
                {
                    "id": product["id"],
                    "sha256": product["sha256"],
                    "mjd_obs_utc": float(product["header"]["MJD-OBS"]),
                    "relative_shift_kms": float(np.median(shifts)),
                    "block_scatter_kms": float(np.std(shifts, ddof=1)),
                    "block_shifts_kms": shifts,
                }
            )
        out["groups"].append(
            {
                "target": target,
                "instrument": instrument,
                "reference": reference["id"],
                "count": len(rows),
                "epochs": rows,
            }
        )
        save("relative_spectra.json", out)
        print(target, instrument, "relative spectral shifts", len(rows), flush=True)
    validate_relative_spectra()


def validate_relative_spectra():
    """Independent pipeline comparison is required before using derived RVs."""
    out = json.loads((HERE / "relative_spectra.json").read_text())
    group = next(
        g
        for g in out["groups"]
        if g["target"] == "toi-3500-02" and g["instrument"] == "HARPS"
    )
    pilot = json.loads((HERE / "harps_profiles.json").read_text())["epochs"]
    by_id = {r["datalink"].split("ADP.")[-1]: r for r in pilot}
    matched = [
        (r, by_id[r["id"][4:-5]]) for r in group["epochs"] if r["id"][4:-5] in by_id
    ]
    reference = matched[0][1]["rv_kms"]
    differences = [
        r["relative_shift_kms"] - (p["rv_kms"] - reference) for r, p in matched
    ]
    rms = float(np.sqrt(np.mean(np.array(differences[1:]) ** 2)))
    out["validation"] = {
        "state": "passed" if rms < 0.01 else "failed",
        "nonreference_comparisons": len(differences) - 1,
        "rms_difference_kms": rms,
        "required_precision_kms": 0.01,
        "difference_kms": differences,
        "reason": "Require10m/s agreement to investigate a roughly39m/s conditional amplitude. Current derived spectral shifts are not accepted as RVs or used to reject aliases.",
    }
    save("relative_spectra.json", out)
    print("Relative RV validation", out["validation"]["state"], rms, flush=True)


def rv_archive(*, names_only=False):
    import csv
    import io
    import requests

    endpoint = "https://archive.eso.org/tap_obs/sync"
    out = {"retrieved_utc": datetime.now(timezone.utc).isoformat(), "queries": []}
    targets = [
        (entry["slug"], entry["ra"], entry["dec"]) for entry in CONFIG["leads"]
    ] + [("control-any-spectrum", 0.0, 0.0)]
    for slug, ra, dec in targets:
        query = f"SELECT TOP 100 target_name,obs_id,dataproduct_type,instrument_name,t_min,t_max,access_url FROM ivoa.ObsCore WHERE dataproduct_type='spectrum' AND CONTAINS(POINT('ICRS',s_ra,s_dec),CIRCLE('ICRS',{ra},{dec},0.0083333333))=1"
        if slug.startswith("control-"):
            query = "SELECT TOP 1 target_name,obs_id,dataproduct_type,instrument_name,t_min,t_max,access_url FROM ivoa.ObsCore WHERE dataproduct_type='spectrum'"
        elif names_only:
            names = {
                "toi-224-01": ("TOI-224", "TIC70797900", "TIC 70797900"),
                "toi-2666-01": (
                    "HD80133",
                    "HD 80133",
                    "HIP45621",
                    "HIP 45621",
                    "TOI-2666",
                    "TIC170889511",
                ),
                "toi-3500-02": ("TOI-3500", "TIC443666343", "TIC 443666343"),
            }[slug]
            literals = ",".join("'" + name + "'" for name in names)
            query = f"SELECT TOP 100 target_name,obs_id,dataproduct_type,instrument_name,t_min,t_max,access_url FROM ivoa.ObsCore WHERE dataproduct_type='spectrum' AND target_name IN ({literals})"
        entry = {
            "target": slug,
            "endpoint": endpoint,
            "query": query,
            "radius_arcsec": 30,
            "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        }
        try:
            response = requests.get(
                endpoint,
                params={
                    "REQUEST": "doQuery",
                    "LANG": "ADQL",
                    "FORMAT": "csv",
                    "QUERY": query,
                },
                timeout=45,
            )
            response.raise_for_status()
            rows = list(csv.DictReader(io.StringIO(response.text)))
            if "obs_id" not in (
                rows[0] if rows else next(csv.reader(io.StringIO(response.text)), [])
            ):
                raise ValueError("response is not expected ObsCore CSV")
            entry.update(state="answered", count=len(rows), rows=rows)
        except Exception as exc:
            entry.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
        out["queries"].append(entry)
        save("rv_name_archive.json" if names_only else "rv_archive.json", out)
        print(slug, "ESO", entry["state"], flush=True)


def covered_mask_lines(wave, mask, velocities, valid=None):
    beta = np.asarray(velocities) / 299792.458
    factors = np.sqrt((1 + beta) / (1 - beta))
    mask = np.asarray(mask, dtype=float)
    use = (mask[:, 0] * factors.min() > wave.min()) & (
        mask[:, 1] * factors.max() < wave.max()
    )
    mask = mask[use]
    if valid is not None:
        bad = np.concatenate(([0], np.cumsum(~np.asarray(valid, dtype=bool))))
        left = np.clip(
            np.searchsorted(wave, mask[:, 0] * factors.min()) - 1, 0, len(wave)
        )
        right = np.clip(
            np.searchsorted(wave, mask[:, 1] * factors.max()) + 1, 0, len(wave)
        )
        mask = mask[(bad[right] - bad[left]) == 0]
    return mask


def integrated_mask_ccf(wave, normalized_flux, mask, velocities, *, valid=None):
    """Integrate a binary line mask over piecewise-linear flux in air Angstrom.

    Spectra and mask must share wavelength frame. Positive velocity redshifts
    the mask. No barycentric correction is added here.
    """
    from scipy.integrate import cumulative_trapezoid

    wave = np.asarray(wave, dtype=float)
    flux = np.asarray(normalized_flux, dtype=float)
    if np.any(np.diff(wave) <= 0) or not np.all(np.isfinite(flux)):
        raise ValueError("Mask CCF requires sorted finite input")
    integral = cumulative_trapezoid(flux, wave, initial=0.0)
    beta = np.asarray(velocities) / 299792.458
    factors = np.sqrt((1 + beta) / (1 - beta))
    mask = covered_mask_lines(wave, mask, velocities, valid)
    if not len(mask):
        raise ValueError("No fully covered mask lines")
    result = []
    for factor in factors:
        edges = mask * factor

        # Exact antiderivative of the linearly interpolated spectrum.
        def evaluate(x):
            idx = np.clip(np.searchsorted(wave, x) - 1, 0, len(wave) - 2)
            delta = x - wave[idx]
            slope = (flux[idx + 1] - flux[idx]) / (wave[idx + 1] - wave[idx])
            return integral[idx] + flux[idx] * delta + 0.5 * slope * delta**2

        area = evaluate(edges[:, 1]) - evaluate(edges[:, 0])
        result.append(np.sum(area) / np.sum(edges[:, 1] - edges[:, 0]))
    return np.array(result)


def fit_mask_ccf(velocities, ccf):
    """Descriptive Gaussian plus slope; covariance is not calibrated RV error."""
    from scipy.optimize import curve_fit

    v = np.asarray(velocities)
    y = np.asarray(ccf)
    peak = float(v[np.argmin(y)])
    keep = np.abs(v - peak) < 15.0
    x = v[keep]
    z = y[keep]

    def model(t, base, slope, depth, center, width):
        return (
            base
            + slope * (t - peak)
            - depth * np.exp(-0.5 * ((t - center) / width) ** 2)
        )

    coef, cov = curve_fit(
        model,
        x,
        z,
        p0=[float(np.median(z)), 0.0, float(np.max(z) - np.min(z)), peak, 3.0],
        bounds=([0.0, -0.1, 0.0, peak - 5.0, 0.3], [3.0, 0.1, 2.0, peak + 5.0, 15.0]),
        maxfev=10000,
    )
    residual = z - model(x, *coef)
    return {
        "center_kms": float(coef[3]),
        "gaussian_sigma_kms": float(coef[4]),
        "contrast": float(coef[2]),
        "formal_fit_error_kms": float(np.sqrt(cov[3, 3])),
        "profile_rms": float(np.sqrt(np.mean(residual**2))),
        "n_profile_points": int(len(x)),
        "caveat": "CCF points correlated; fit covariance excludes pixel/calibration noise and is not a validated RV uncertainty",
    }


def relative_ccf_shift(velocities, reference, observed, center):
    """Align a static asymmetric profile while profiling scale/offset/slope."""
    from scipy.interpolate import CubicSpline
    from scipy.optimize import minimize_scalar

    v = np.asarray(velocities)
    ref = np.asarray(reference)
    obs = np.asarray(observed)
    keep = np.abs(v - center) < 12.0
    x = v[keep]
    y = obs[keep]
    template = CubicSpline(v, ref)

    def loss(shift):
        design = np.column_stack([np.ones(len(x)), x - center, template(x - shift)])
        coef = np.linalg.lstsq(design, y, rcond=None)[0]
        return float(np.mean((y - design @ coef) ** 2))

    fit = minimize_scalar(
        loss, bounds=(-3.0, 3.0), method="bounded", options={"xatol": 1e-8}
    )
    return {
        "shift_kms": float(fit.x),
        "profile_rms": float(np.sqrt(fit.fun)),
        "state": "failed_boundary" if abs(fit.x) > 2.9 else "measured_profile",
        "caveat": "No CCF noise/covariance calibration; this shift is descriptive until empirical precision validation",
    }


def ccf_alignment():
    masked_path = HERE / "masked_spectra.json"
    masked_digest = hashlib.sha256(masked_path.read_bytes()).hexdigest()
    profiles = json.loads(masked_path.read_text())
    science = json.loads((HERE / "spectra_manifest.json").read_text())
    snrs = {
        p["datalink"]: float(p["header"].get("SNR", 0))
        for p in science["products"]
        if p["state"] == "downloaded"
    }
    pilot = json.loads((HERE / "harps_profiles.json").read_text())["epochs"]
    pipeline = {p["datalink"]: p["rv_kms"] for p in pilot}
    groups = {}
    for product in profiles["products"]:
        if product["state"] != "measured_profile":
            continue
        for mask in product["masks"]:
            groups.setdefault(
                (product["target"], product["instrument"], mask["name"]), []
            ).append((product, mask))
    out = {
        "method": "Cubic-spline CCF template alignment with linear nuisance offset/slope/scale in plusminus12km/s about reference; shift rangeplusminus3km/s. Reference chosen by highest original headerSNR, before period fitting.",
        "groups": [],
        "input": "masked_spectra.json",
        "input_sha256": masked_digest,
        "resolve_leads_py_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
    }
    velocity = np.array(profiles["velocity_grid_kms"])
    for key, rows in groups.items():
        reference, mask_ref = max(rows, key=lambda pm: snrs[pm[0]["datalink"]])
        results = []
        differences = []
        for product, mask in rows:
            shift = relative_ccf_shift(
                velocity, mask_ref["ccf"], mask["ccf"], mask_ref["fit"]["center_kms"]
            )
            results.append(
                {
                    "id": product["id"],
                    "datalink": product["datalink"],
                    "mjd_obs_utc": product["mjd_obs_utc"],
                    **shift,
                }
            )
            if (
                product["datalink"] in pipeline
                and product["datalink"] != reference["datalink"]
            ):
                differences.append(
                    shift["shift_kms"]
                    - (pipeline[product["datalink"]] - pipeline[reference["datalink"]])
                )
        validation = None
        if differences:
            rms = float(np.sqrt(np.mean(np.array(differences) ** 2)))
            validation = {
                "state": "passed" if rms < 0.01 else "failed",
                "rms_pipeline_difference_kms": rms,
                "differences_kms": differences,
                "comparisons": len(differences),
                "requirement_kms": 0.01,
            }
        out["groups"].append(
            {
                "target": key[0],
                "instrument": key[1],
                "mask": key[2],
                "reference_id": reference["id"],
                "reference_header_snr": snrs[reference["datalink"]],
                "epochs": results,
                "harps_precision_validation": validation,
            }
        )
    save("ccf_alignment.json", out)
    print(
        "CCF alignment",
        [
            (g["instrument"], g["mask"], g["harps_precision_validation"])
            for g in out["groups"]
        ],
        flush=True,
    )


def barycentric_audit():
    """Compare the already-applied FEROS correction with an independent one.

    This records correction replacement deltas, not repaired stellar RVs.
    Start/mid/end times bound the unknown photon-weighted exposure time.
    """
    import astropy
    import astropy.units as u
    from astropy.coordinates import EarthLocation, SkyCoord, Distance
    from astropy.time import Time
    from astropy.utils import iers

    iers.conf.auto_download = False
    earth_orientation = iers.IERS_Auto.open()
    refresh = json.loads((HERE / "archive_refresh.json").read_text())
    spectra = json.loads((HERE / "spectra_manifest.json").read_text())
    exact = {"toi-3500-02": 3471495415361216512, "toi-2666-01": 3837451574150437120}
    rows = []
    unique = {
        p["datalink"]: p
        for p in spectra["products"]
        if p["state"] == "downloaded" and p["header"].get("INSTRUME") == "FEROS"
    }
    for product in unique.values():
        target = product["target"]
        query = next(q for q in refresh["queries"] if q["label"] == target + ":gaia")
        data = query["result"]
        names = [meta["name"] for meta in data["metadata"]]
        star = next(
            dict(zip(names, row))
            for row in data["data"]
            if row[names.index("source_id")] == exact[target]
        )
        h = product["header"]
        location = EarthLocation.from_geodetic(
            h["ESO TEL GEOLON"] * u.deg,
            h["ESO TEL GEOLAT"] * u.deg,
            h["ESO TEL GEOELEV"] * u.m,
        )
        start = float(h["MJD-OBS"])
        duration = float(h["EXPTIME"])
        times = Time(
            start + np.array([0.0, 0.5, 1.0]) * duration / 86400.0,
            format="mjd",
            scale="utc",
            location=location,
        )
        if times.mjd.min() < float(
            earth_orientation["MJD"][0].value
        ) or times.mjd.max() > float(earth_orientation["MJD"][-1].value):
            raise ValueError("Epoch outside IERS coverage")
        coordinate = SkyCoord(
            ra=star["ra"] * u.deg,
            dec=star["dec"] * u.deg,
            pm_ra_cosdec=star["pmra"] * u.mas / u.yr,
            pm_dec=star["pmdec"] * u.mas / u.yr,
            distance=Distance(parallax=star["parallax"] * u.mas),
            obstime=Time(star["ref_epoch"], format="jyear", scale="tcb"),
            radial_velocity=(star["radial_velocity"] or 0.0) * u.km / u.s,
        )
        propagated = coordinate.apply_space_motion(new_obstime=times)
        correction = propagated.radial_velocity_correction(
            obstime=times, kind="barycentric"
        ).to_value(u.km / u.s)
        applied = float(h["ESO DRS BARYCORR"])
        rows.append(
            {
                "id": product["id"],
                "sha256": product["sha256"],
                "target": target,
                "source_id": star["source_id"],
                "input_gaia_astrometry": star,
                "mjd_obs_utc": start,
                "exposure_seconds": duration,
                "site": {
                    "longitude_deg": h["ESO TEL GEOLON"],
                    "latitude_deg": h["ESO TEL GEOLAT"],
                    "elevation_m": h["ESO TEL GEOELEV"],
                },
                "stored_applied_correction_kms": applied,
                "astropy_start_mid_end_kms": correction.tolist(),
                "replacement_delta_start_mid_end_kms": (correction - applied).tolist(),
                "state": "correction_audited_not_applied",
            }
        )
    save(
        "feros_barycentric_audit.json",
        {
            "astropy_version": astropy.__version__,
            "ephemeris": "Astropy builtin/ERFA",
            "iers_mjd_bounds": [
                float(earth_orientation["MJD"][0].value),
                float(earth_orientation["MJD"][-1].value),
            ],
            "iers_predictive_rows_involved": bool(
                any(
                    int(
                        earth_orientation.ut1_utc(
                            Time(r["mjd_obs_utc"], format="mjd", scale="utc"),
                            return_status=True,
                        )[1]
                    )
                    == iers.FROM_IERS_A_PREDICTION
                    for r in rows
                )
            ),
            "products": rows,
            "method": "Gaia DR3 exact source ICRS/J2016 propagated to observation; header observatory; UTC start/mid/end; Astropy optical barycentric velocity correction. Compare with stored already-applied FEROS correction, do not add it twice.",
            "caveats": [
                "Optical velocity correction and relativistic mask Doppler conventions differ at fewm/s; conversion needed before precision replacement.",
                "Photon-weighted exposure times unknown; start/end range is timing sensitivity, not a measured posterior.",
                "Target/header accuracy, wavelength calibration, simultaneous-reference drift, sky contamination and product noise remain unresolved.",
                "No corrected stellar RV or orbital fit is asserted by this audit.",
            ],
        },
    )
    print("FEROS barycentric audit", len(rows), "epochs", flush=True)


def koa_screen():
    """Bounded public HIRES metadata screen supporting component-RV follow-up."""
    import csv
    import io
    import requests

    endpoint = "https://koa.ipac.caltech.edu/TAP/sync"
    columns = (
        "koaid,filehand,object,ra,dec,mjd,utdatetime,exptime,iodout,obstype,datlevel"
    )
    out = {
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "endpoint": endpoint,
        "documentation": "https://koa.ipac.caltech.edu/UserGuide/PyKOA/TAPClients.html",
        "queries": [],
    }
    specs = []
    for lead in CONFIG["leads"]:
        ra, dec = lead["ra"], lead["dec"]
        specs.append(
            (
                lead["slug"],
                f"SELECT TOP 100 {columns} FROM koa_hires WHERE ra BETWEEN {ra - 0.02} AND {ra + 0.02} AND dec BETWEEN {dec - 0.02} AND {dec + 0.02}",
            )
        )
    specs.append(
        (
            "toi-2666-01:exact_names",
            f"SELECT TOP 100 {columns} FROM koa_hires WHERE object IN ('HD80133','HD 80133','HIP45621','HIP 45621','TOI-2666','TOI2666','TIC170889511')",
        )
    )
    specs.append(("control-any-HIRES", f"SELECT TOP 1 {columns} FROM koa_hires"))
    for label, query in specs:
        entry = {
            "target": label,
            "query": query,
            "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            "selection": "coordinate box plusminus0.02deg (equinoxJ2000 archive fields); exact names and positive control separate; no precise epoch/source assignment until headers checked",
        }
        try:
            response = requests.get(
                endpoint,
                params={
                    "REQUEST": "doQuery",
                    "LANG": "ADQL",
                    "FORMAT": "csv",
                    "QUERY": query,
                },
                timeout=45,
            )
            response.raise_for_status()
            reader = csv.DictReader(io.StringIO(response.text))
            if "koaid" not in (reader.fieldnames or []):
                raise ValueError("Not expected KOA CSV")
            rows = list(reader)
            entry.update(
                state="answered",
                count=len(rows),
                cap=1 if label.startswith("control") else 100,
                rows=rows,
            )
        except Exception as exc:
            entry.update(state="unavailable", error=f"{type(exc).__name__}: {exc}")
        out["queries"].append(entry)
        save("koa_hires_archive.json", out)
        print(
            "KOA",
            label,
            entry["state"],
            entry.get("count", entry.get("error")),
            flush=True,
        )


def fetch_masks(scratch):
    import requests

    commit = "89ba7d5bbdfa7ef7332a2b1a5bfb9646504ac618"
    base = f"https://raw.githubusercontent.com/szunigaf/CCF_functions/{commit}/"
    folder = scratch / "lead-resolution-2026-09-30" / "masks"
    folder.mkdir(parents=True, exist_ok=True)
    products = []
    for name in ("masks/R50G2.mas", "masks/K0.mas", "LICENSE"):
        path = folder / Path(name).name
        if not path.exists():
            r = requests.get(base + name, timeout=45)
            r.raise_for_status()
            path.write_bytes(r.content)
        products.append(
            {
                "id": f"szunigaf/CCF_functions@{commit}:{name}",
                "archive": "Primary published CCF implementation repository",
                "url": base + name,
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "retrieved_utc": datetime.now(timezone.utc).isoformat(),
            }
        )
    save(
        "mask_manifest.json",
        {
            "commit": commit,
            "products": products,
            "license": (folder / "LICENSE").read_text(),
            "method_source": "https://github.com/szunigaf/CCF_functions",
            "note": "Only mask data used, no downloaded code executed.Independent integrator retains all lines rather than source routine's last-line omission.",
        },
    )


def masked_spectra(scratch, limit, target=None):
    from astropy.io import fits
    from scipy.ndimage import median_filter

    manifest = json.loads((HERE / "spectra_manifest.json").read_text())
    if (HERE / "masked_spectra.json").exists() and not (
        HERE / "masked_spectra_initial_pilot.json"
    ).exists():
        save(
            "masked_spectra_initial_pilot.json",
            json.loads((HERE / "masked_spectra.json").read_text()),
        )
    products = {
        p["datalink"]: p
        for p in manifest["products"]
        if p["state"] == "downloaded" and (target is None or p["target"] == target)
    }
    bands = (
        (4500.0, 5000.0),
        (5000.0, 5500.0),
        (5500.0, 5870.0),
        (6000.0, 6260.0),
        (6350.0, 6550.0),
        (6570.0, 6800.0),
    )
    velocities = np.arange(-120.0, 120.01, 0.25)
    masks_folder = scratch / "lead-resolution-2026-09-30" / "masks"
    masks = {
        name: np.loadtxt(masks_folder / (name + ".mas"))[:, :2]
        for name in ("R50G2", "K0")
    }
    out = {
        "retrieved_inputs": "spectra_manifest.json;mask_manifest.json",
        "provenance": {
            "generated_utc": datetime.now(timezone.utc).isoformat(),
            "resolve_leads_py_sha256": hashlib.sha256(
                Path(__file__).read_bytes()
            ).hexdigest(),
            "spectra_manifest_sha256": hashlib.sha256(
                (HERE / "spectra_manifest.json").read_bytes()
            ).hexdigest(),
            "mask_manifest_sha256": hashlib.sha256(
                (HERE / "mask_manifest.json").read_bytes()
            ).hexdigest(),
            "selection_limit_per_target_instrument": limit,
        },
        "method": "Exact piecewise-linear spectral integration over pinned binary-mask windows, relativistic Doppler factor; six bands avoid major telluric/Halpha/NaD regions;501pixel median continuum; Gaussian+slope descriptive profile fit.",
        "wavelength": "Air Angstrom; requireBARYCENT; no correction added twice",
        "known_feros_limits": "ESO release description94: low-precision barycentric correction already applied; no simultaneous-reference drift correction; ERR dummyNaN; no precision orbital use without calibration audit",
        "velocity_grid_kms": velocities.tolist(),
        "bands_angstrom": bands,
        "products": [],
    }
    counters = {}
    for product in sorted(
        products.values(), key=lambda p: float(p["header"]["MJD-OBS"])
    ):
        key = (product["target"], product["header"]["INSTRUME"])
        if counters.get(key, 0) >= limit:
            continue
        counters[key] = counters.get(key, 0) + 1
        entry = {
            "id": product["id"],
            "sha256": product["sha256"],
            "datalink": product["datalink"],
            "target": key[0],
            "instrument": key[1],
            "mjd_obs_utc": float(product["header"]["MJD-OBS"]),
            "pipeline_barycorr_kms": product["header"].get("ESO DRS BARYCORR"),
            "masks": [],
        }
        path = (
            scratch
            / "lead-resolution-2026-09-30"
            / "spectra"
            / product["id"].replace(":", "-")
        )
        try:
            if product["header"].get("SPECSYS") != "BARYCENT":
                raise ValueError("Unexpected spectral frame")
            with fits.open(path) as h:
                if (
                    h[1].header.get("TUNIT1") != "angstrom"
                    or h[1].header.get("TUCD1") != "em.wl;obs.atmos"
                ):
                    raise ValueError("Unexpected wavelength units or medium")
                wave = np.array(h[1].data["WAVE"][0], dtype=float)
                flux = np.array(h[1].data["FLUX"][0], dtype=float)
                err = np.array(h[1].data["ERR"][0], dtype=float)
            parts = []
            health = []
            for lo, hi in bands:
                use = (wave >= lo) & (wave <= hi)
                w = wave[use]
                f = flux[use]
                bad = ~np.isfinite(f)
                health.append(
                    {
                        "band": [lo, hi],
                        "pixels": int(len(w)),
                        "nonfinite_flux": int(bad.sum()),
                        "positive_finite_errors": int(
                            np.sum(np.isfinite(err[use]) & (err[use] > 0))
                        ),
                    }
                )
                if len(w) < 500 or np.mean(bad) > 0.01:
                    raise ValueError("Band lacks usable coverage")
                f[bad] = 0.0
                continuum = median_filter(f, size=501, mode="nearest")
                valid = (continuum > 0) & (f > 0) & (~bad)
                health[-1]["invalid_pixels_for_mask"] = int((~valid).sum())
                if np.mean(valid) < 0.5:
                    raise ValueError("Band has insufficient positive continuum")
                normalized = np.zeros_like(f)
                normalized[valid] = f[valid] / continuum[valid]
                parts.append((w, normalized, valid))
            entry["health"] = health
            for name, mask in masks.items():
                profiles = []
                line_counts = []
                band_fits = []
                for (lo, hi), (w, f, valid) in zip(bands, parts):
                    selected = mask[(mask[:, 0] > lo + 3) & (mask[:, 1] < hi - 3)]
                    selected = covered_mask_lines(w, selected, velocities, valid)
                    profile = integrated_mask_ccf(
                        w, f, selected, velocities, valid=valid
                    )
                    profiles.append(profile)
                    line_counts.append(len(selected))
                    band_fits.append(fit_mask_ccf(velocities, profile))
                combined = np.average(profiles, axis=0, weights=line_counts)
                entry["masks"].append(
                    {
                        "name": name,
                        "line_counts": line_counts,
                        "fit": fit_mask_ccf(velocities, combined),
                        "band_fits": band_fits,
                        "ccf": combined.tolist(),
                    }
                )
            entry["state"] = "measured_profile"
        except Exception as exc:
            entry.update(state="failed", error=f"{type(exc).__name__}: {exc}")
        out["products"].append(entry)
        save("masked_spectra.json", out)
        print(key, entry["state"], flush=True)
    pilot = json.loads((HERE / "harps_profiles.json").read_text())["epochs"]
    pipeline = {p["datalink"]: p["rv_kms"] for p in pilot}
    validations = []
    for name in masks:
        matches = [
            (
                p,
                pipeline[p["datalink"]],
                next(m["fit"]["center_kms"] for m in p["masks"] if m["name"] == name),
            )
            for p in out["products"]
            if p["datalink"] in pipeline and p["state"] == "measured_profile"
        ]
        if len(matches) < 2:
            continue
        zero = matches[0][2] - matches[0][1]
        delta = [center - rv - zero for _, rv, center in matches][1:]
        rms = float(np.sqrt(np.mean(np.array(delta) ** 2)))
        validations.append(
            {
                "mask": name,
                "state": "passed" if rms < 0.01 else "failed",
                "rms_pipeline_difference_kms": rms,
                "differences_kms": delta,
                "constant_mask_zero_point_kms": zero,
                "requirement_kms": 0.01,
                "comparisons": len(delta),
            }
        )
    out["harps_precision_validation"] = validations
    save("masked_spectra.json", out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=(
            "all",
            "archives",
            "photometry",
            "prf-download",
            "cutouts",
            "prf",
            "ffi",
            "coarse-aliases",
            "rv",
            "rv-names",
            "spectra",
            "harps",
            "harps-sparse",
            "rv-profiles",
            "relative-spectra",
            "validate-spectra",
            "masks",
            "masked-spectra",
            "ccf-alignment",
            "barycentric-audit",
            "koa",
        ),
        default="all",
    )
    parser.add_argument(
        "--scratch", type=Path, default=Path(r"D:\AO_Artifacts\cygnus_scratch")
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=1,
        help="per-target pilot spectrum count; raise after resource inspection",
    )
    parser.add_argument(
        "--target",
        choices=tuple(entry["slug"] for entry in CONFIG["leads"]),
        help="restrict spectrum download to one target",
    )
    args = parser.parse_args()
    if args.mode in ("archives", "all"):
        archives()
    if args.mode in ("photometry", "all"):
        photometry(args.scratch)
    if args.mode == "prf-download":
        fetch_prfs(args.scratch)
    if args.mode == "cutouts":
        cutouts(args.scratch)
    if args.mode == "prf":
        calibrated_prf(args.scratch)
    if args.mode == "ffi":
        ffi_photometry(args.scratch)
    if args.mode == "coarse-aliases":
        coarse_alias_test(args.scratch)
    if args.mode == "rv":
        rv_archive()
    if args.mode == "rv-names":
        rv_archive(names_only=True)
    if args.mode == "spectra":
        download_spectra(args.scratch, args.limit, args.target)
    if args.mode == "harps":
        harps_bundles(args.scratch, args.limit)
    if args.mode == "harps-sparse":
        sparse_harps(args.limit, args.scratch)
    if args.mode == "rv-profiles":
        harps_profiles()
    if args.mode == "relative-spectra":
        relative_spectra(args.scratch)
    if args.mode == "validate-spectra":
        validate_relative_spectra()
    if args.mode == "masks":
        fetch_masks(args.scratch)
    if args.mode == "masked-spectra":
        masked_spectra(args.scratch, args.limit, args.target)
    if args.mode == "ccf-alignment":
        ccf_alignment()
    if args.mode == "barycentric-audit":
        barycentric_audit()
    if args.mode == "koa":
        koa_screen()

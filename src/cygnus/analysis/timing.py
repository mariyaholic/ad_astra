"""Barycentric-correction audit. Records deltas; never overwrites a pipeline's applied correction."""

from __future__ import annotations

import numpy as np


def barycentric_audit(*, ra_deg, dec_deg, pmra_masyr, pmdec_masyr, parallax_mas, ref_epoch_jyear,
                      rv_kms, site_lon_deg, site_lat_deg, site_elev_m, mjd_obs_utc, exposure_s,
                      applied_kms) -> dict:
    """Compare an already-applied correction with Astropy's, at exposure start/mid/end (UTC).

    Start/end bound the unknown photon-weighted time, so they are a timing sensitivity, not a posterior.
    Returned deltas are (independent - applied) in km/s. Optical vs relativistic conventions differ at
    a few m/s; convert before any precision replacement.
    """
    import astropy.units as u
    from astropy.coordinates import Distance, EarthLocation, SkyCoord
    from astropy.time import Time
    from astropy.utils import iers

    iers.conf.auto_download = False
    eo = iers.IERS_Auto.open()
    loc = EarthLocation.from_geodetic(site_lon_deg * u.deg, site_lat_deg * u.deg, site_elev_m * u.m)
    times = Time(mjd_obs_utc + np.array([0.0, 0.5, 1.0]) * exposure_s / 86400.0, format="mjd", scale="utc",
                 location=loc)
    if times.mjd.min() < float(eo["MJD"][0].value) or times.mjd.max() > float(eo["MJD"][-1].value):
        raise ValueError("Epoch outside IERS coverage")
    star = SkyCoord(ra=ra_deg * u.deg, dec=dec_deg * u.deg, pm_ra_cosdec=pmra_masyr * u.mas / u.yr,
                    pm_dec=pmdec_masyr * u.mas / u.yr, distance=Distance(parallax=parallax_mas * u.mas),
                    obstime=Time(ref_epoch_jyear, format="jyear", scale="tcb"),
                    radial_velocity=(rv_kms or 0.0) * u.km / u.s)
    corr = star.apply_space_motion(new_obstime=times).radial_velocity_correction(
        obstime=times, kind="barycentric").to_value(u.km / u.s)
    return {"applied_kms": float(applied_kms), "independent_start_mid_end_kms": corr.tolist(),
            "delta_start_mid_end_kms": (corr - applied_kms).tolist(), "state": "audited_not_applied"}

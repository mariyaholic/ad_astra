"""Light-curve access for the multi-archive runner.

The screen primitives and the SPOC reader are the production ones
(``cygnus.campaign.lightcurve``), so a SPOC product is read and screened exactly as
``cygnus.campaign`` does. This module adds only :func:`read_campaign_lc`, which maps a
light curve from any archive onto the screen's two-channel shape.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from ..campaign.lightcurve import (SpocLightCurve, contiguous_runs, in_veto, local_resid, phase_of,  # noqa: F401
                                   read_spoc, robust_sigma, screen_events)

# Channel pairs that are genuinely different reductions of the same photometry (raw aperture
# flux vs a systematics-corrected flux). Any other pair — e.g. FLUX and MAG, which are one
# measurement in two units — is *not* an independent comparison.
INDEPENDENT_PAIRS = {("SAP", "PDCSAP"), ("SAP", "KSPSAP"), ("FLUX", "FLUX_CORR")}


def read_campaign_lc(path: str | Path, *, fmt: str = "spoc_lc") -> SpocLightCurve:
    """Read a light curve from *any* archive into the screen's :class:`SpocLightCurve` shape.

    The residual screen and calibration compare two channels (``sap`` and ``pdc``). For a
    SPOC product those are SAP and PDCSAP; for a generic archive the reader picks the first
    available raw/corrected pair and records the mapping in ``primary['_channels']``. The
    pair counts as ``independent`` only when it is a known raw-vs-corrected reduction pair
    (:data:`INDEPENDENT_PAIRS`); otherwise ``sap`` and ``pdc`` are both the single chosen
    channel and the caller screens it once, with the non-independence visible in the record.
    """
    from .readers import read_lightcurve

    lc = read_lightcurve(path, fmt=fmt)
    chans = list(lc.channels)
    if not chans:
        raise ValueError(f"{Path(path).name}: no flux channels recognised")
    pair = next(((a, b) for a, b in sorted(INDEPENDENT_PAIRS) if a in chans and b in chans), None)
    if pair:
        sap, pdc = pair
    else:
        sap = pdc = next((c for c in ("PDCSAP", "KSPSAP", "FLUX_CORR", "SAP", "FLUX", "MAG") if c in chans), chans[0])
    sap_f = np.asarray(lc.fluxes[sap], float)
    pdc_f = np.asarray(lc.fluxes[pdc], float)
    converted = None
    if sap == "MAG":
        # magnitudes grow when a star dims: the screen looks for negative flux excursions, so convert
        # to relative flux (sentinels such as 99 become NaN) before screening
        m = np.where(np.isfinite(sap_f) & (sap_f < 90), sap_f, np.nan)
        ref = np.nanmedian(m) if np.isfinite(m).any() else 0.0
        sap_f = pdc_f = 10 ** (-0.4 * (m - ref))
        converted = "MAG -> relative flux 10^(-0.4 (m - median m))"
    t = np.asarray(lc.time, float)
    cadence = float(lc.cadence_s or 0.0)
    cadence_source = "product header"
    if cadence <= 0:
        dt = np.diff(np.sort(t[np.isfinite(t)]))
        dt = dt[dt > 0]
        cadence = float(np.median(dt) * 86400) if dt.size else 0.0
        cadence_source = "median time step (no cadence metadata)"
    centroids = {}
    for n in ("MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2"):
        if n in lc.engineering:          # the reader keeps engineering series apart from the flux channels
            centroids[n] = np.asarray(lc.engineering[n], float)
    primary = dict(lc.primary)
    primary["_channels"] = {"sap": sap, "pdc": pdc, "all": chans, "archive_format": fmt,
                            "independent": pair is not None, "converted": converted,
                            "cadence_source": cadence_source, "time_scale": getattr(lc, "time_scale", None)}
    return SpocLightCurve(
        path=Path(path), time=t, sap=sap_f, pdc=pdc_f,
        quality=np.asarray(lc.quality, int) if lc.quality is not None else np.zeros(lc.time.size, int),
        bjdref=float(lc.bjdref), cadence_s=cadence,
        primary=primary, table_header=dict(lc.table_header), centroids=centroids,
    )

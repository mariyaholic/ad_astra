"""Light-curve primitives shared by the residual screen, its calibration and the BLS recovery.

The numerics are moved verbatim from ``tools/analyze_tess_residual.py`` and
``campaigns/run_wasp12_sector20.py`` (2026-09-24) so re-running a campaign through the runner
reproduces the recorded outputs; ``tests/test_campaign.py`` checks that equivalence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


def robust_sigma(x) -> float:
    x = np.asarray(x, float)
    med = np.nanmedian(x)
    return float(1.4826 * np.nanmedian(np.abs(x - med)))


def local_resid(y, valid, seconds: float, window_days: float):
    """Fractional residual from a centred running median; NaNs interpolated only for the baseline."""
    from scipy.ndimage import median_filter

    idx = np.arange(y.size)
    good = valid & np.isfinite(y)
    filled = np.interp(idx, idx[good], y[good])
    width = max(3, int(round(window_days * 86400 / seconds)))
    if width % 2 == 0:
        width += 1
    base = median_filter(filled, size=width, mode="nearest")
    resid = y / base - 1.0
    resid[~good] = np.nan
    return resid


def contiguous_runs(mask, min_len: int = 2) -> list[np.ndarray]:
    ii = np.flatnonzero(mask)
    if not len(ii):
        return []
    cuts = np.flatnonzero(np.diff(ii) > 1) + 1
    return [g for g in np.split(ii, cuts) if len(g) >= min_len]


@dataclass
class SpocLightCurve:
    path: Path
    time: np.ndarray            # as stored (BTJD for TESS SPOC)
    sap: np.ndarray
    pdc: np.ndarray
    quality: np.ndarray
    bjdref: float
    cadence_s: float
    primary: dict = field(default_factory=dict)
    table_header: dict = field(default_factory=dict)
    centroids: dict = field(default_factory=dict)

    @property
    def time_bjd(self) -> np.ndarray:
        return self.time + self.bjdref

    @property
    def usable(self) -> np.ndarray:
        """QUALITY == 0 with finite, nonzero TIME, SAP and PDCSAP (the residual screen's rule)."""
        base = np.isfinite(self.time) & (self.quality == 0)
        return base & np.isfinite(self.sap) & np.isfinite(self.pdc) & (self.sap != 0) & (self.pdc != 0)


PRIMARY_KEYS = ("OBJECT", "TICID", "SECTOR", "CAMERA", "CCD", "RA_OBJ", "DEC_OBJ", "DATE-OBS", "DATE-END", "TSTART", "TSTOP",
                "TIMESYS", "TIMEUNIT", "TELESCOP", "INSTRUME", "FILTER", "PROCVER", "DATA_REL")
TABLE_KEYS = ("BJDREFI", "BJDREFF", "TIMEZERO", "TIMESYS", "TIMEUNIT", "TUNIT1", "TIMEDEL", "TIMEPIXR")


def read_spoc(path: str | Path) -> SpocLightCurve:
    from astropy.io import fits

    path = Path(path)
    with fits.open(path, memmap=True) as hdul:
        hdr, ext, tab = hdul[0].header, hdul[1].header, hdul[1].data
        names = set(tab.names)
        need = {"TIME", "SAP_FLUX", "PDCSAP_FLUX", "QUALITY"}
        if not need <= names:
            raise ValueError(f"{path.name}: missing columns {sorted(need - names)}")
        return SpocLightCurve(
            path=path,
            time=np.asarray(tab["TIME"], float), sap=np.asarray(tab["SAP_FLUX"], float),
            pdc=np.asarray(tab["PDCSAP_FLUX"], float), quality=np.asarray(tab["QUALITY"], int),
            bjdref=float(ext.get("BJDREFI", 0)) + float(ext.get("BJDREFF", 0)),
            cadence_s=float(hdr.get("TIMEDEL", 120 / 86400)) * 86400,
            primary={k: hdr.get(k) for k in PRIMARY_KEYS},
            table_header={k: ext.get(k) for k in TABLE_KEYS},
            centroids={n: np.asarray(tab[n], float) for n in ("MOM_CENTR1", "MOM_CENTR2") if n in names},
        )


def screen_events(lc: SpocLightCurve, *, sap=None, pdc=None, windows_days=(1.0, 2.0, 3.0),
                  k_mad: float = 5.0, min_cadences: int = 2, sign: int = -1) -> list[dict]:
    """Excursions beyond ``k_mad`` robust sigmas (``sign=-1`` dips, ``+1`` brightenings) lasting
    ``min_cadences``, for SAP and PDCSAP at each baseline window. ``sap``/``pdc`` override the
    stored fluxes (used for injection–recovery)."""
    sap = lc.sap if sap is None else sap
    pdc = lc.pdc if pdc is None else pdc
    finite = lc.usable
    out = []
    for days in windows_days:
        for label, flux in (("SAP", sap), ("PDCSAP", pdc)):
            rr = local_resid(flux, finite, lc.cadence_s, days)
            sig = robust_sigma(rr[finite])
            hit = finite & np.isfinite(rr) & ((rr < -k_mad * sig) if sign < 0 else (rr > k_mad * sig))
            for g in contiguous_runs(hit, min_cadences):
                out.append({"detrend_days": days, "flux_type": label, "start_index": int(g[0]), "stop_index": int(g[-1]),
                            "n_cadences": int(len(g)), "median_fractional_residual": float(np.nanmedian(rr[g])),
                            "robust_sigma_fraction": float(sig)})
    return out


def phase_of(t_bjd, period_days: float, t0_bjd: float):
    """Orbital phase in [0, 1) with the transit at 0."""
    return ((np.asarray(t_bjd, float) - t0_bjd) / period_days) % 1


def in_veto(phase, veto_phase: float):
    return (phase < veto_phase) | (phase > 1 - veto_phase)

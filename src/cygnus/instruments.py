"""Instrument profiles — the 'no universal cutoffs' rule made executable.

Per AGENTS.md, artifact-audit thresholds must be instrument-specific:
``psf_fwhm_px=None`` is deliberate — detector modules must either measure the
PSF from field stars, use an instrument library value passed per campaign, or
record the test as ``not_tested``. Numerical values below are approximate
starting points; pin per-campaign values from instrument documentation.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class InstrumentProfile:
    name: str
    pixel_scale_as: float | None = None  # arcsec per pixel
    psf_fwhm_px: float | None = None  # None => must be measured/library-set
    cadence_s_default: float | None = None  # seconds; None => varies by era
    quirks: tuple[str, ...] = ()
    notes: str = ""


REGISTRY: dict[str, InstrumentProfile] = {
    "TESS": InstrumentProfile(
        name="TESS",
        pixel_scale_as=21.0,
        psf_fwhm_px=None,
        cadence_s_default=120.0,
        quirks=(
            "scattered light from Earth/Moon limb varies over the orbit",
            "pointing-systematics enter via attitude quaternions and centroid columns",
            "FFI cadence varies by sector/era — pin per campaign",
        ),
        notes="Values approximate; see TESS instrument handbooks.",
    ),
    "TESS_FFI": InstrumentProfile(
        name="TESS_FFI",
        pixel_scale_as=21.0,
        psf_fwhm_px=None,
        cadence_s_default=None,
        quirks=("cutout-based light curves carry reduced sampling;",),
        notes="For cutout work via Tesscut/eleanor.",
    ),
    "Kepler": InstrumentProfile(
        name="Kepler",
        pixel_scale_as=3.98,
        psf_fwhm_px=None,
        cadence_s_default=1765.5,
        quirks=(
            "long cadence 29.4 min; short cadence 58.85 s",
            "monthly modal thermal events; safe-mode gaps",
        ),
        notes="Static pointing means systematics differ qualitatively from TESS.",
    ),
    "K2": None,  # populated below as an alias of Kepler
    "generic_ccd": InstrumentProfile(
        name="generic_ccd",
        pixel_scale_as=None,
        psf_fwhm_px=None,
        cadence_s_default=None,
        quirks=("all quantitative thresholds must be measured before audit use",),
    ),
}


REGISTRY["K2"] = REGISTRY["Kepler"]  # K2 mission reuses the Kepler hardware profile


class InstrumentUnknownError(KeyError):
    pass


def get(name: str) -> InstrumentProfile:
    try:
        return REGISTRY[name]
    except KeyError as exc:
        raise InstrumentUnknownError(
            f"unknown instrument {name!r}; known: {sorted(REGISTRY)}"
        ) from exc


def require_psf_fwhm(profile: InstrumentProfile) -> float:
    """Return the pinned PSF FWHM or explain exactly why the audit cannot run."""
    if profile.psf_fwhm_px is None:
        raise RuntimeError(
            f"instrument {profile.name!r} has no pinned PSF FWHM: measure it "
            "from field stars or load a campaign-specific library value "
            "(no universal pixel-width cutoffs — AGENTS.md)."
        )
    return profile.psf_fwhm_px

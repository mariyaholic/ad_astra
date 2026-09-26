"""Format readers for multi-archive products.

Every downloaded product is turned into one of a small number of in-memory
objects:

* :class:`LightCurve` — a time series with one or more named flux channels
  (SPOC ``SAP``/``PDCSAP``, Kepler/K2 the same, IRSA/ZTF ``mag``, generic
  ``flux``). Column detection is explicit and recorded; nothing is assumed.
* :class:`Image` — a FITS image/cube (SkyView, Legacy Survey, ESO, TESScut).
* :class:`Table` — a catalogue table (VizieR, SIMBAD, NED, Gaia, ExoFAP, IRSA).

Only ``astropy``/``numpy`` are required, and only inside the reader functions,
so the module imports on a bare interpreter.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

LIGHTCURVE_FORMATS = ("fits_table", "spoc_lc", "kepler_lc", "tess_lc", "ztf_lc", "csv_lc")
IMAGE_FORMATS = ("fits_image", "fits_cube", "coadd_image")
TABLE_FORMATS = ("csv", "votable", "table", "json")
TEXT_FORMATS = ("text",)
RV_FORMATS = ("rv_table", "eso_spectrum")
ENGINEERING_COLUMNS = ("MOM_CENTR1", "MOM_CENTR2", "POS_CORR1", "POS_CORR2", "SAP_BKG")

#: candidate flux columns in priority order, with the channel name we give them
_FLUX_COLUMNS = (
    ("PDCSAP_FLUX", "PDCSAP"), ("SAP_FLUX", "SAP"),
    ("KSPSAP_FLUX", "KSPSAP"),
    ("FLUX_CORR", "FLUX_CORR"), ("FLUX", "FLUX"),
    ("MAG", "MAG"), ("MAG_APER", "MAG"),
)


class ReaderError(RuntimeError):
    pass


@dataclass
class LightCurve:
    """A generic light curve: one time axis and named flux channels.

    ``time`` is exactly as stored; ``bjdref`` (when present) is added by
    :meth:`time_bjd`, consistent with the campaign layer's convention. The
    caller must state the time standard — it is exposed, not converted.
    """

    path: Path
    time: np.ndarray
    fluxes: dict[str, np.ndarray]
    quality: np.ndarray
    flux_errs: dict[str, np.ndarray] = field(default_factory=dict)
    bjdref: float = 0.0
    cadence_s: float = 120.0
    time_scale: str | None = None
    time_unit: str | None = None
    primary: dict[str, Any] = field(default_factory=dict)
    table_header: dict[str, Any] = field(default_factory=dict)
    channels_order: tuple[str, ...] = ()
    #: engineering series (centroids, pointing, background) when the product carries them
    engineering: dict[str, np.ndarray] = field(default_factory=dict)

    @property
    def time_bjd(self) -> np.ndarray:
        return self.time + self.bjdref

    @property
    def channels(self) -> tuple[str, ...]:
        return self.channels_order or tuple(self.fluxes)

    def usable(self, channel: str) -> np.ndarray:
        """QUALITY == 0 (when a quality array exists) with finite, nonzero flux."""
        base = np.isfinite(self.time)
        if self.quality is not None and self.quality.size == self.time.size:
            base = base & (self.quality == 0)
        f = self.fluxes[channel]
        good = np.isfinite(f) & (f != 0)
        # ZTF/IRSA magnitudes are usable when finite and not the sentinel 99.0
        if channel == "MAG":
            good = good & (f < 90)
        return base & good

    def normalized(self, channel: str) -> np.ndarray:
        f = np.asarray(self.fluxes[channel], float)
        m = np.nanmedian(f[self.usable(channel)]) if self.usable(channel).any() else np.nan
        return f / m - 1.0


def _as_float(a) -> np.ndarray:
    return np.asarray(a, float)


def read_product(path: str | Path, *, fmt: str | None = None, ref: Any = None) -> Any:
    """Dispatch a product to the right reader by ``fmt`` (or the file extension)."""
    path = Path(path)
    fmt = fmt or _guess_format(path)
    if fmt in LIGHTCURVE_FORMATS:
        return read_lightcurve(path, fmt=fmt)
    if fmt in IMAGE_FORMATS:
        return read_image(path)
    if fmt in TABLE_FORMATS:
        return read_table(path, fmt=fmt)
    if fmt in TEXT_FORMATS:
        return {"text": path.read_text(encoding="utf-8", errors="replace")}
    if fmt in RV_FORMATS:
        rv = read_rv(path, fmt=fmt)
        return {"rows": len(rv["bjd"]), "columns": ["bjd", "rv_ms", "err_ms"], "source": rv["source"]}
    raise ReaderError(f"unknown product format {fmt!r} for {path.name}")


def _guess_format(path: Path) -> str:
    s = path.name.lower()
    if s.endswith((".fits", ".fit", ".fts")):
        return "fits_table"
    if s.endswith((".xml", ".vot")):
        return "votable"
    if s.endswith(".csv"):
        return "csv"
    if s.endswith(".json"):
        return "json"
    return "text"


def read_lightcurve(path: str | Path, *, fmt: str = "fits_table") -> LightCurve:
    """Read a time series from a FITS table, a VOTable or a CSV light curve.

    Column detection is by known names; the chosen channels are recorded in
    ``LightCurve.channels``. A product without a recognisable time column raises
    rather than silently guessing.
    """
    path = Path(path)
    if fmt == "ztf_lc" or path.suffix.lower() in (".vot", ".xml"):
        return _read_votable_lightcurve(path)
    if fmt == "csv_lc" or path.suffix.lower() in (".csv", ".txt"):
        return _read_csv_lightcurve(path)
    return _read_fits_lightcurve(path)


def _read_votable_lightcurve(path: Path) -> LightCurve:
    """ZTF/IRSA-style VOTable light curve: first time column, first magnitude/flux column."""
    from astropy.io.votable import parse as votable_parse

    vt = votable_parse(str(path))
    tab = vt.get_first_table().to_table()
    names = {str(c).lower(): c for c in tab.colnames}
    # prefer a barycentric/heliocentric midpoint; ZTF ``mjd`` is the exposure *start* in UTC
    tcol = next((names[c] for c in ("bjd", "hjd", "jd", "mjd", "time") if c in names), None)
    if tcol is None:
        raise ReaderError(f"{path.name}: no time column in VOTable (columns: {', '.join(map(str, tab.colnames[:12]))})")
    time = np.asarray(tab[tcol], float)
    tname = str(tcol).lower()
    bjdref = 2400000.5 if tname == "mjd" else 0.0
    time_scale = {"bjd": "BJD as supplied", "hjd": "HJD (UTC) exposure midpoint; within ~1-2 min of BJD_TDB",
                  "jd": "JD as supplied (not barycentric)", "mjd": "MJD (UTC) exposure start; not barycentric",
                  }.get(tname, "time column as supplied; standard not established")
    fluxes: dict[str, np.ndarray] = {}
    errs: dict[str, np.ndarray] = {}
    order: list[str] = []
    for name, chan in (("mag", "MAG"), ("magpsf", "MAG"), ("mag_auto", "MAG"),
                       ("flux", "FLUX"), ("flux_corr", "FLUX_CORR")):
        if name in names and chan not in fluxes:
            fluxes[chan] = np.asarray(tab[names[name]], float)
            order.append(chan)
            if f"{name}err" in names:
                errs[chan] = np.asarray(tab[names[f"{name}err"]], float)
    if not fluxes:
        raise ReaderError(f"{path.name}: no recognised magnitude/flux column in VOTable")
    qcol = next((names[c] for c in ("catflags", "quality", "flags") if c in names), None)
    quality = np.asarray(tab[qcol], int) if qcol else np.zeros(time.size, int)
    return LightCurve(path=path, time=time, fluxes=fluxes, quality=quality, flux_errs=errs,
                      bjdref=bjdref, cadence_s=0.0, time_scale=time_scale, time_unit="d",
                      primary={"OBJECT": "ZTF/IRSA VOTable", "TIMECOL": str(tcol)},
                      table_header={"TIMESYS": time_scale}, channels_order=tuple(order))


def _read_fits_lightcurve(path: Path) -> LightCurve:
    from astropy.io import fits

    with fits.open(path, memmap=True) as hdul:
        if len(hdul) < 2 or hdul[1].data is None:
            raise ReaderError(f"{path.name}: no table extension")
        hdr0, hdr1, tab = hdul[0].header, hdul[1].header, hdul[1].data
        names = list(tab.names or ())
        if "TIME" not in names:
            raise ReaderError(f"{path.name}: no TIME column (columns: {', '.join(names[:12])})")
        time = _as_float(tab["TIME"])
        quality = np.asarray(tab["QUALITY"], int) if "QUALITY" in names else np.zeros(time.size, int)
        fluxes: dict[str, np.ndarray] = {}
        errs: dict[str, np.ndarray] = {}
        order: list[str] = []
        for col, chan in _FLUX_COLUMNS:
            if col in names and chan not in fluxes:
                fluxes[chan] = _as_float(tab[col])
                order.append(chan)
                if f"{col}_ERR" in names:
                    errs[chan] = _as_float(tab[f"{col}_ERR"])
        if not fluxes:
            raise ReaderError(f"{path.name}: no recognised flux column (looked for {', '.join(c for c, _ in _FLUX_COLUMNS)})")
        engineering = {c: _as_float(tab[c]) for c in ENGINEERING_COLUMNS if c in names}
        bjdref = float(hdr1.get("BJDREFI", 0)) + float(hdr1.get("BJDREFF", 0))
        cadence = float(hdr0.get("TIMEDEL", hdr1.get("TIMEDEL", 120 / 86400))) * 86400
        primary = {k: hdr0.get(k) for k in
                   ("OBJECT", "TICID", "KEPLERID", "SECTOR", "QUARTER", "CAMPAIGN", "CAMERA", "CCD",
                    "RA_OBJ", "DEC_OBJ", "TELESCOP", "INSTRUME", "FILTER")}
        table_header = {k: hdr1.get(k) for k in ("BJDREFI", "BJDREFF", "TIMEZERO", "TIMESYS", "TIMEUNIT", "TIMEDEL")}
        return LightCurve(path=path, time=time, fluxes=fluxes, quality=quality, flux_errs=errs,
                          bjdref=bjdref, cadence_s=cadence, time_scale=hdr1.get("TIMESYS"), time_unit=hdr1.get("TIMEUNIT"),
                          primary=primary, table_header=table_header, channels_order=tuple(order),
                          engineering=engineering)


def _read_csv_lightcurve(path: Path) -> LightCurve:
    import csv

    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        cols = reader.fieldnames or []
        rows = list(reader)
    if not rows:
        raise ReaderError(f"{path.name}: empty light curve")
    lower = {c.lower(): c for c in cols}

    def pick(*names: str) -> str | None:
        for n in names:
            if n.lower() in lower:
                return lower[n.lower()]
        return None

    tcol = pick("time", "bjd", "hjd", "mjd", "btjd")
    if tcol is None:
        raise ReaderError(f"{path.name}: no time column (columns: {', '.join(cols)})")
    quality_col = pick("quality", "flags", "flag")
    time = np.array([_to_f(r.get(tcol)) for r in rows], float)
    quality = np.array([int(_to_f(r.get(quality_col)) or 0) for r in rows], int) if quality_col else np.zeros(time.size, int)
    fluxes: dict[str, np.ndarray] = {}
    errs: dict[str, np.ndarray] = {}
    order: list[str] = []
    for name, chan in (("pdcsap_flux", "PDCSAP"), ("sap_flux", "SAP"), ("kspsap_flux", "KSPSAP"),
                       ("flux_corr", "FLUX_CORR"), ("flux", "FLUX"),
                       ("mag", "MAG"), ("mag_aper", "MAG")):
        col = pick(name)
        if col and chan not in fluxes:
            fluxes[chan] = np.array([_to_f(r.get(col)) for r in rows], float)
            order.append(chan)
            ecol = pick(name + "_err")
            if ecol:
                errs[chan] = np.array([_to_f(r.get(ecol)) for r in rows], float)
    if not fluxes:
        raise ReaderError(f"{path.name}: no recognised flux column")
    # a CSV carries no cadence or time-standard metadata: cadence is measured by the caller
    return LightCurve(path=path, time=time, fluxes=fluxes, quality=quality, flux_errs=errs,
                      bjdref=0.0, cadence_s=0.0, primary={"TIMECOL": str(tcol)}, table_header={},
                      channels_order=tuple(order))


def _to_f(v) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return float("nan")


def read_image(path: str | Path) -> dict[str, Any]:
    """Return a FITS image as ``{data, header, wcs, path, shape}`` (data is a numpy array)."""
    from astropy.io import fits

    path = Path(path)
    with fits.open(path, memmap=True) as hdul:
        hdu = None
        for h in hdul:
            if getattr(h, "data", None) is not None and getattr(h.data, "ndim", 0) >= 2:
                hdu = h
                break
        if hdu is None:
            raise ReaderError(f"{path.name}: no 2-D image HDU")
        wcs, wcs_note = None, None
        try:
            from astropy.wcs import WCS

            w = WCS(hdu.header, naxis=2)
            wcs = w if w.has_celestial else None
            wcs_note = None if wcs is not None else "header has no celestial WCS"
        except Exception as exc:  # noqa: BLE001 - an image without a usable WCS is still an image
            wcs_note = f"WCS unreadable: {type(exc).__name__}: {str(exc)[:120]}"
        return {"path": path, "data": np.asarray(hdu.data), "header": hdu.header,
                "shape": tuple(hdu.data.shape), "n_hdus": len(hdul), "wcs": wcs, "wcs_note": wcs_note}


def read_table(path: str | Path, *, fmt: str = "csv") -> dict[str, Any]:
    """Return a catalogue table as ``{columns, rows, path}`` (rows are dicts)."""
    path = Path(path)
    if fmt == "json" or path.suffix.lower() == ".json":
        import json

        data = json.loads(path.read_text(encoding="utf-8"))
        rows = data if isinstance(data, list) else data.get("data", [])
        cols = sorted(rows[0].keys()) if rows else []
        return {"path": path, "columns": cols, "rows": rows}
    if fmt == "votable" or path.suffix.lower() in (".xml", ".vot"):
        from astropy.io.votable import parse as votable_parse

        vt = votable_parse(str(path))
        tab = vt.get_first_table().to_table()
        return {"path": path, "columns": list(tab.colnames),
                "rows": [{c: _scalar(tab[c][i]) for c in tab.colnames} for i in range(len(tab))]}
    import csv

    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        return {"path": path, "columns": list(reader.fieldnames or []), "rows": list(reader)}


# ESO pipeline radial-velocity keywords: (RV, RV error, BJD), RVs in km/s. HARPS/HARPS-N DRS, then ESPRESSO/NIRPS DRS.
ESO_RV_KEYWORDS = (
    ("HIERARCH ESO DRS CCF RVC", "HIERARCH ESO DRS CCF NOISE", "HIERARCH ESO DRS BJD"),
    ("HIERARCH ESO QC CCF RV", "HIERARCH ESO QC CCF RV ERROR", "HIERARCH ESO QC BJD"),
)


def read_rv(path: str | Path, *, fmt: str | None = None) -> dict[str, Any]:
    """Radial velocities as ``{bjd, rv_ms, err_ms, source}``.

    ``rv_table``: a CSV with a BJD column (``bjd``/``bjd_tdb``/``time``), an RV column (``rv_ms`` in
    m/s or ``rv_kms`` in km/s) and its error (``err_ms``/``rv_err_ms`` or ``err_kms``/``rv_err_kms``).
    A FITS product: one RV from the ESO pipeline keywords in :data:`ESO_RV_KEYWORDS`. Anything else
    raises :class:`ReaderError`; units are never guessed.
    """
    path = Path(path)
    if (fmt or "").lower() == "rv_table" or path.suffix.lower() == ".csv":
        tab = read_table(path, fmt="csv")
        cols = {c.lower(): c for c in tab["columns"]}
        tcol = next((cols[c] for c in ("bjd", "bjd_tdb", "time") if c in cols), None)
        for rc, ec, scale in (("rv_ms", "err_ms", 1.0), ("rv_ms", "rv_err_ms", 1.0), ("rv_kms", "err_kms", 1e3),
                              ("rv_kms", "rv_err_kms", 1e3)):
            if tcol and rc in cols and ec in cols:
                rows = [r for r in tab["rows"] if all(np.isfinite(_to_f(r[x])) for x in (tcol, cols[rc], cols[ec]))]
                return {"bjd": [_to_f(r[tcol]) for r in rows], "rv_ms": [_to_f(r[cols[rc]]) * scale for r in rows],
                        "err_ms": [_to_f(r[cols[ec]]) * scale for r in rows], "source": f"{path.name} columns {tcol}/{rc}/{ec}"}
        raise ReaderError(f"{path.name}: no BJD + RV + RV-error columns with stated units")
    from astropy.io import fits

    with fits.open(path, memmap=False) as hdul:
        hdr = hdul[0].header
        for rk, ek, tk in ESO_RV_KEYWORDS:
            if rk in hdr and ek in hdr and tk in hdr:
                return {"bjd": [float(hdr[tk])], "rv_ms": [float(hdr[rk]) * 1e3], "err_ms": [float(hdr[ek]) * 1e3],
                        "source": f"{path.name} header {rk}"}
    raise ReaderError(f"{path.name}: no ESO pipeline RV keywords")


def _scalar(v):
    try:
        return v.item()
    except AttributeError:
        return v
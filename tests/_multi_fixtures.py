"""Shared synthetic fixtures for the cygnus.multi step/runner tests (not collected: no ``test_`` prefix).

Everything is built in tmp_path: small SPOC-shaped FITS light curves, a runner ``Context`` over an
in-memory ledger, and fetch_products result entries pointing at staged files. No network.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np

SPOC_PID = "tess-fixture-s0007-0000000000000001-s_lc.fits"


def write_spoc(path: Path, *, n: int = 3000, cadence_s: float = 120.0, t_start: float = 1500.0,
               dips=(), depth: float = 0.03, half_width_d: float = 0.06, periodic=None,
               noise: float = 0.001, seed: int = 1, bad_windows=(), bad_index=None, sector: int | None = 7,
               bjdrefi: int = 2457000) -> Path:
    """A SPOC-shaped light curve (TIME/SAP_FLUX/PDCSAP_FLUX/QUALITY/MOM_CENTR*).

    ``dips``: box centres (stored time) of depth ``depth`` and half width ``half_width_d``.
    ``periodic``: (period_d, epoch, depth, half_width_d) for a repeating box.
    ``bad_windows``: (lo, hi) stored-time windows flagged QUALITY=512.
    ``bad_index``: a boolean mask (or slice) of cadences flagged QUALITY=512.
    """
    from astropy.io import fits

    rng = np.random.default_rng(seed)
    t = t_start + np.arange(n) * (cadence_s / 86400)
    flux = 1000.0 * (1 + rng.normal(0, noise, n))
    for c in dips:
        flux[np.abs(t - c) < half_width_d] *= 1 - depth
    if periodic:
        p, e, d, hw = periodic
        ph = ((t - e + p / 2) % p) - p / 2
        flux[np.abs(ph) < hw] *= 1 - d
    q = np.zeros(n, int)
    for lo, hi in bad_windows:
        q[(t >= lo) & (t <= hi)] = 512
    if bad_index is not None:
        q[bad_index] = 512
    cols = [fits.Column(name=nm, format="D", array=a) for nm, a in
            (("TIME", t), ("SAP_FLUX", flux * 1.01), ("PDCSAP_FLUX", flux), ("MOM_CENTR1", np.full(n, 10.0)),
             ("MOM_CENTR2", np.full(n, 11.0)))] + [fits.Column(name="QUALITY", format="J", array=q)]
    hdu0 = fits.PrimaryHDU()
    hdr = {"OBJECT": "TIC 1", "TICID": 1, "TIMEDEL": cadence_s / 86400, "RA_OBJ": 10.0, "DEC_OBJ": 20.0}
    if sector is not None:
        hdr["SECTOR"] = sector
    hdu0.header.update(hdr)
    tab = fits.BinTableHDU.from_columns(cols)
    tab.header.update({"BJDREFI": bjdrefi, "BJDREFF": 0.0, "TIMESYS": "TDB", "TIMEUNIT": "d"})
    path.parent.mkdir(parents=True, exist_ok=True)
    fits.HDUList([hdu0, tab]).writeto(path, overwrite=True)
    return path


def sha256(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def product_entry(path: Path, *, target=None, tic=None, sector=7, pinned=True, archive="MAST",
                  fmt="spoc_lc", kind="lightcurve") -> dict:
    """A fetch_products result entry for a staged file, as step_fetch_products writes it."""
    from cygnus.multi.steps import portable

    return {"path": portable(path), "sha256": sha256(path), "bytes": Path(path).stat().st_size, "fetched_now": False,
            "pinned": pinned, "target": target, "tic": tic, "sector": sector, "covers_known_epoch": None,
            "archive": archive, "format": fmt, "url": None, "kind": kind, "description": ""}


def make_ctx(root: Path, spec: dict | None = None, results: dict | None = None, ledger=None):
    """A runner Context over an in-memory ledger with an open run (so ctx.measure works)."""
    from cygnus.ledger import Ledger
    from cygnus.multi.runner import Context

    led = ledger or Ledger(":memory:")
    full = {"campaign_id": "unit-ctx", "outputs": "out/", "random_seed": 3, **(spec or {})}
    full.setdefault("_path", root / "campaigns" / f"{full['campaign_id']}.yaml")
    ctx = Context(full, led, root)
    ctx.run_id = led.log_run("unit:test")
    ctx.step = "unit"
    ctx._results.update(results or {})
    return ctx


def measurements(ledger) -> list[dict]:
    return [dict(r) for r in ledger.db.execute("SELECT * FROM measurements ORDER BY id")]


RECORD_TAIL = """record:
  path: {outputs}sky_record.json
  title: Fixture {cid}
  kind: residual screen
  outcome: {outcome}
  date: "2026-01-02"
  report: {outputs}REPORT.md
  summary: Synthetic.
  checks:
    - {{name: "Pixel-level audit", state: not_tested}}
"""

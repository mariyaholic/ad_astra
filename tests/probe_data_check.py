"""End-to-end data probe: real TESS cutout -> scratch + ledger + basic sanity.

Records the retrieved data volume and simple health statistics as ledgered
measurements, per AGENTS.md provenance rules. Safe to rerun (idempotent).
"""

from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import numpy as np  # noqa: E402
from astropy.io import fits  # noqa: E402

from cygnus.ingest.mast import download_tesscut  # noqa: E402
from cygnus.ledger import Ledger  # noqa: E402


def main() -> int:
    led = Ledger()  # default worktree ledger: <worktree>/state/ledger.sqlite
    run = led.log_run("data_probe.mast_tesscut", seed=None)
    try:
        paths = download_tesscut(
            ra_deg=219.757,
            dec_deg=-80.531,  # pi Men region (southern CVZ)
            ledger=led,
            size_px=5,
            sector=12,  # verified live: a covering sector of these coordinates
        )
        if not paths:
            print("NO DATA: no cutouts returned")
            led.close_run(run, "failed", summary="no cutouts")
            return 1

        p = paths[0]
        with fits.open(p) as hdul:
            header = hdul[0].header
            table = hdul[1].data
            names = list(table.names)
            time_col = np.asarray(table["TIME"])
            flux = np.asarray(table["FLUX"])
            quality = np.asarray(table["QUALITY"])

            n_rows = int(len(table))
            finite = np.isfinite(flux)
            finite_frac = float(finite.mean())
            good_rows = int((quality == 0).sum())

            print(f"cutout: {p}")
            print(
                f"header: SECTOR={header.get('SECTOR')} CAMERA={header.get('CAMERA')} "
                f"CCD={header.get('CCD')} TELESCOP={header.get('TELESCOP','?')}"
            )
            print(f"columns: {names}")
            print(f"rows: {n_rows}  (quality==0: {good_rows})")
            print(f"TIME range: [{np.nanmin(time_col):.4f}, {np.nanmax(time_col):.4f}] d")
            print(f"FLUX shape: {flux.shape}  finite fraction: {finite_frac:.4f}")
            print(f"FLUX median: {np.nanmedian(flux):.3f}")

            pid = f"tesscut-{219.757:.4f}-{-80.531:.4f}-sec{header.get('SECTOR')}"
            led.add_measurement(
                run,
                "tesscut_rows",
                n_rows,
                unit="cadences",
                method="mast.Tesscut.get_cutouts",
                candidate_id=None,
                product_ids=[pid],
                notes="data-population probe",
            )
            led.add_measurement(
                run,
                "tesscut_finite_fraction",
                finite_frac,
                unit="dimensionless",
                method="np.isfinite.mean",
                candidate_id=None,
                product_ids=[pid],
            )
            led.close_run(run, "completed", summary=f"{n_rows} cadences in scratch+ledger")
        print(f"ledger products (MAST): {led.count_products('MAST')}")
        return 0
    except Exception as exc:
        led.close_run(run, "failed", summary=f"{exc.__class__.__name__}: {exc}")
        raise


if __name__ == "__main__":
    sys.exit(main())

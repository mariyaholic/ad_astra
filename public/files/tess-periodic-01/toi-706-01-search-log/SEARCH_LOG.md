<!-- [private Drive store] -->
# Search log: toi-706-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 224 (99 distinct events, 8 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018292075959-s0004-0000000219345200-0124-s_lc.fits` | 18684 | 14737 | 2.50 | 78 | 56 |
| `tess2018319095959-s0005-0000000219345200-0125-s_lc.fits` | 18944 | 17286 | 3.50 | 0 | 0 |
| `tess2018349182500-s0006-0000000219345200-0126-s_lc.fits` | 15678 | 14619 | 2.50 | 22 | 22 |
| `tess2020294194027-s0031-0000000219345200-0198-s_lc.fits` | 18314 | 16586 | 3.00 | 30 | 30 |
| `tess2020324010417-s0032-0000000219345200-0200-s_lc.fits` | 18730 | 17610 | 3.00 | 4 | 4 |
| `tess2025258001959-s0097-0000000219345200-0294-s_lc.fits` | 39335 | 30323 | 2.50 | 112 | 112 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

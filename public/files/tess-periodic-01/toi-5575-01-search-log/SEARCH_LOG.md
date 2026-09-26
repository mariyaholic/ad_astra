<!-- [private Drive store] -->
# Search log: toi-5575-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 72 (16 distinct events, 11 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022330142927-s0059-0000000160162137-0248-s_lc.fits` | 19029 | 16013 | 2.50 | 23 | 23 |
| `tess2022357055054-s0060-0000000160162137-0249-s_lc.fits` | 18494 | 12595 | 3.00 | 12 | 12 |
| `tess2023341045131-s0073-0000000160162137-0268-s_lc.fits` | 19337 | 11952 | 3.00 | 9 | 9 |
| `tess2024142205832-s0079-0000000160162137-0274-s_lc.fits` | 19542 | 19073 | 2.50 | 10 | 10 |
| `tess2024326142117-s0086-0000000160162137-0283-s_lc.fits` | 19132 | 10881 | 3.50 | 18 | 18 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

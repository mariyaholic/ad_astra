<!-- [private Drive store] -->
# Search log: toi-1149-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 110 (55 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022190063128-s0054-0000000117789567-0227-s_lc.fits` | 18890 | 15257 | 2.50 | 59 | 59 |
| `tess2021204101404-s0041-0000000117789567-0212-s_lc.fits` | 19149 | 18316 | 3.00 | 9 | 9 |
| `tess2022217014003-s0055-0000000117789567-0242-s_lc.fits` | 19562 | 18879 | 2.50 | 15 | 15 |
| `tess2024196212429-s0081-0000000117789567-0276-s_lc.fits` | 19174 | 16078 | 2.50 | 27 | 27 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

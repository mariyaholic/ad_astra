<!-- cygnus:generated-draft -->
# Search log: toi-527-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 156 (57 distinct events, 10 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018349182500-s0006-0000000148228019-0126-s_lc.fits` | 15678 | 14682 | 3.50 | 18 | 9 |
| `tess2019006130736-s0007-0000000148228019-0131-s_lc.fits` | 17612 | 16330 | 3.00 | 7 | 7 |
| `tess2020351194500-s0033-0000000148228019-0203-s_lc.fits` | 18609 | 17455 | 3.00 | 16 | 16 |
| `tess2021014023720-s0034-0000000148228019-0204-s_lc.fits` | 18231 | 16949 | 3.00 | 79 | 79 |
| `tess2024353092137-s0087-0000000148228019-0284-s_lc.fits` | 19370 | 16140 | 3.00 | 2 | 2 |
| `tess2025014115807-s0088-0000000148228019-0285-s_lc.fits` | 20000 | 19430 | 3.00 | 43 | 43 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

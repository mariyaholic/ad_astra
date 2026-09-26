<!-- cygnus:generated-draft -->
# Search log: toi-911-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 1221 (493 distinct events, 23 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000389070884-0290-s_lc.fits` | 18862 | 16418 | 3.00 | 189 | 189 |
| `tess2019140104343-s0012-0000000389070884-0144-s_lc.fits` | 20119 | 14344 | 2.50 | 149 | 149 |
| `tess2021146024351-s0039-0000000389070884-0210-s_lc.fits` | 20126 | 18554 | 3.00 | 512 | 512 |
| `tess2023153011303-s0066-0000000389070884-0260-s_lc.fits` | 20707 | 15310 | 3.50 | 371 | 371 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

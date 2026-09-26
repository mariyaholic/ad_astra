<!-- cygnus:generated-draft -->
# Search log: toi-588-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 675 (314 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000130415266-0250-s_lc.fits` | 18312 | 15521 | 3.00 | 263 | 67 |
| `tess2020351194500-s0033-0000000130415266-0203-s_lc.fits` | 18609 | 17454 | 3.00 | 0 | 0 |
| `tess2021014023720-s0034-0000000130415266-0204-s_lc.fits` | 18231 | 16826 | 2.50 | 371 | 371 |
| `tess2021039152502-s0035-0000000130415266-0205-s_lc.fits` | 17997 | 13689 | 6.00 | 1 | 1 |
| `tess2024353092137-s0087-0000000130415266-0284-s_lc.fits` | 19370 | 15085 | 2.50 | 105 | 105 |
| `tess2025014115807-s0088-0000000130415266-0285-s_lc.fits` | 20000 | 18555 | 2.50 | 131 | 131 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

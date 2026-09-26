<!-- [private Drive store] -->
# Search log: toi-1192-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 45 (18 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024196212429-s0081-0000000158276040-0276-s_lc.fits` | 19174 | 16880 | 3.00 | 22 | 0 |
| `tess2020160202036-s0026-0000000158276040-0188-s_lc.fits` | 17909 | 16940 | 3.50 | 0 | 0 |
| `tess2021175071901-s0040-0000000158276040-0211-s_lc.fits` | 20309 | 19611 | 2.50 | 20 | 20 |
| `tess2021204101404-s0041-0000000158276040-0212-s_lc.fits` | 19149 | 18322 | 3.00 | 6 | 6 |
| `tess2022164095748-s0053-0000000158276040-0226-s_lc.fits` | 17992 | 15270 | 2.50 | 18 | 18 |
| `tess2022217014003-s0055-0000000158276040-0242-s_lc.fits` | 19562 | 18879 | 3.00 | 1 | 1 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

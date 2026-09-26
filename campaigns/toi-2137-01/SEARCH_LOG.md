<!-- cygnus:generated-draft -->
# Search log: toi-2137-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 132 (30 distinct events, 19 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020160202036-s0026-0000000023059280-0188-s_lc.fits` | 17909 | 16042 | 3.00 | 26 | 16 |
| `tess2021175071901-s0040-0000000023059280-0211-s_lc.fits` | 20309 | 16918 | 2.50 | 40 | 40 |
| `tess2022164095748-s0053-0000000023059280-0226-s_lc.fits` | 17992 | 10768 | 3.00 | 39 | 39 |
| `tess2024003055635-s0074-0000000023059280-0269-s_lc.fits` | 19232 | 17231 | 3.00 | 10 | 10 |
| `tess2024170053053-s0080-0000000023059280-0275-s_lc.fits` | 19047 | 16517 | 3.00 | 27 | 27 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

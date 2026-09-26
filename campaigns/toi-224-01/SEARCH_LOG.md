<!-- cygnus:generated-draft -->
# Search log: toi-224-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 24 (4 distinct events, 4 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018234235059-s0002-0000000070797900-0121-s_lc.fits` | 19737 | 18298 | 10.00 | 6 | 0 |
| `tess2020238165205-s0029-0000000070797900-0193-s_lc.fits` | 18864 | 14036 | 8.00 | 6 | 6 |
| `tess2023237165326-s0069-0000000070797900-0264-s_lc.fits` | 18569 | 14715 | 5.00 | 6 | 6 |
| `tess2025232030459-s0096-0000000070797900-0293-s_lc.fits` | 18487 | 14609 | 4.50 | 6 | 6 |
| `tess2026192185000-s0106-0000000070797900-0308-s_lc.fits` | 20484 | 13017 | 5.00 | 6 | 6 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

<!-- [private Drive store] -->
# Search log: toi-1455-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 324 (58 distinct events, 50 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024326142117-s0086-0000000387259626-0283-s_lc.fits` | 19132 | 14977 | 3.00 | 63 | 57 |
| `tess2019279210107-s0017-0000000387259626-0161-s_lc.fits` | 18012 | 14117 | 3.00 | 70 | 70 |
| `tess2019306063752-s0018-0000000387259626-0162-s_lc.fits` | 17554 | 15218 | 3.00 | 41 | 41 |
| `tess2022138205153-s0052-0000000387259626-0224-s_lc.fits` | 17602 | 15687 | 3.50 | 51 | 51 |
| `tess2022244194134-s0056-0000000387259626-0243-s_lc.fits` | 20079 | 18668 | 3.00 | 50 | 50 |
| `tess2022302161335-s0058-0000000387259626-0247-s_lc.fits` | 19962 | 18997 | 4.00 | 55 | 55 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

<!-- [private Drive store] -->
# Search log: toi-3586-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 216 (48 distinct events, 24 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022217014003-s0055-0000000286080865-0242-s_lc.fits` | 19562 | 18882 | 3.00 | 20 | 20 |
| `tess2022244194134-s0056-0000000286080865-0243-s_lc.fits` | 20079 | 19612 | 2.50 | 18 | 18 |
| `tess2024030031500-s0075-0000000286080865-0270-s_lc.fits` | 19947 | 19474 | 3.00 | 39 | 39 |
| `tess2024058030222-s0076-0000000286080865-0271-s_lc.fits` | 19502 | 19025 | 2.50 | 37 | 37 |
| `tess2024223182411-s0082-0000000286080865-0278-s_lc.fits` | 18619 | 18137 | 2.50 | 85 | 85 |
| `tess2024249191853-s0083-0000000286080865-0280-s_lc.fits` | 17967 | 17330 | 3.00 | 17 | 17 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

<!-- [private Drive store] -->
# Search log: toi-3531-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 280 (53 distinct events, 38 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2022244194134-s0056-0000000316038054-0243-s_lc.fits` | 20079 | 19612 | 2.50 | 88 | 58 |
| `tess2022273165103-s0057-0000000316038054-0245-s_lc.fits` | 20712 | 17991 | 3.00 | 42 | 42 |
| `tess2024058030222-s0076-0000000316038054-0271-s_lc.fits` | 19502 | 19025 | 2.50 | 48 | 48 |
| `tess2024085201119-s0077-0000000316038054-0272-s_lc.fits` | 20209 | 12874 | 3.00 | 45 | 45 |
| `tess2024249191853-s0083-0000000316038054-0280-s_lc.fits` | 17967 | 17330 | 2.50 | 53 | 53 |
| `tess2024274222008-s0084-0000000316038054-0281-s_lc.fits` | 18545 | 12898 | 3.00 | 34 | 34 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

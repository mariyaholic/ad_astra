<!-- [private Drive store] -->
# Search log: toi-6650-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 4 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 134 (37 distinct events, 13 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2024249191853-s0083-0000000064837857-0280-s_lc.fits` | 17967 | 17329 | 2.50 | 46 | 38 |
| `tess2022273165103-s0057-0000000064837857-0245-s_lc.fits` | 20712 | 17990 | 6.00 | 47 | 47 |
| `tess2024085201119-s0077-0000000064837857-0272-s_lc.fits` | 20209 | 12874 | 3.50 | 21 | 21 |
| `tess2024274222008-s0084-0000000064837857-0281-s_lc.fits` | 18545 | 16718 | 2.50 | 28 | 28 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

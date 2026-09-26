<!-- [private Drive store] -->
# Search log: toi-1059-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 318 (128 distinct events, 23 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2025154050500-s0093-0000000380783252-0290-s_lc.fits` | 18862 | 16180 | 3.00 | 112 | 105 |
| `tess2019169103026-s0013-0000000380783252-0146-s_lc.fits` | 20479 | 17220 | 3.00 | 60 | 60 |
| `tess2021146024351-s0039-0000000380783252-0210-s_lc.fits` | 20126 | 19321 | 3.00 | 38 | 38 |
| `tess2023153011303-s0066-0000000380783252-0260-s_lc.fits` | 20707 | 14707 | 3.00 | 34 | 34 |
| `tess2026033082000-s0100-0000000380783252-0302-s_lc.fits` | 19064 | 16774 | 4.50 | 41 | 41 |
| `tess2026086090000-s0102-0000000380783252-0304-s_lc.fits` | 17790 | 15609 | 5.50 | 40 | 40 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

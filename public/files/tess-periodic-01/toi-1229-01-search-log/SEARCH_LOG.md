<!-- [private Drive store] -->
# Search log: toi-1229-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 130 (22 distinct events, 14 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000140760434-0250-s_lc.fits` | 18312 | 15095 | 3.00 | 21 | 3 |
| `tess2019112060037-s0011-0000000140760434-0143-s_lc.fits` | 19527 | 11700 | 2.50 | 21 | 21 |
| `tess2019140104343-s0012-0000000140760434-0144-s_lc.fits` | 20119 | 14345 | 3.00 | 33 | 33 |
| `tess2019169103026-s0013-0000000140760434-0146-s_lc.fits` | 20479 | 17222 | 3.50 | 23 | 23 |
| `tess2020212050318-s0028-0000000140760434-0190-s_lc.fits` | 18182 | 14304 | 3.00 | 17 | 17 |
| `tess2020238165205-s0029-0000000140760434-0193-s_lc.fits` | 18864 | 15111 | 3.50 | 33 | 33 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

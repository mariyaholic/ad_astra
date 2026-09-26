<!-- [private Drive store] -->
# Search log: toi-173-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 340 (89 distinct events, 30 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018206045859-s0001-0000000270341214-0120-s_lc.fits` | 20076 | 18274 | 2.50 | 22 | 10 |
| `tess2019169103026-s0013-0000000270341214-0146-s_lc.fits` | 20479 | 17217 | 3.50 | 163 | 163 |
| `tess2020186164531-s0027-0000000270341214-0189-s_lc.fits` | 17546 | 16155 | 3.50 | 8 | 8 |
| `tess2020212050318-s0028-0000000270341214-0190-s_lc.fits` | 18182 | 15086 | 2.50 | 17 | 17 |
| `tess2021146024351-s0039-0000000270341214-0210-s_lc.fits` | 20126 | 19334 | 3.00 | 33 | 33 |
| `tess2023153011303-s0066-0000000270341214-0260-s_lc.fits` | 20707 | 15435 | 3.00 | 109 | 109 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

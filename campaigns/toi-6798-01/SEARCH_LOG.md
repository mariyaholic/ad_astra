<!-- cygnus:generated-draft -->
# Search log: toi-6798-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 907 (185 distinct events, 73 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023181235917-s0067-0000000290403522-0261-s_lc.fits` | 19987 | 12869 | 2.50 | 6 | 6 |
| `tess2020186164531-s0027-0000000290403522-0189-s_lc.fits` | 17546 | 16781 | 2.50 | 111 | 111 |
| `tess2025180145000-s0094-0000000290403522-0291-s_lc.fits` | 18620 | 15116 | 2.50 | 238 | 238 |
| `tess2025206162959-s0095-0000000290403522-0292-s_lc.fits` | 18167 | 15167 | 3.00 | 247 | 247 |
| `tess2026060005000-s0101-0000000290403522-0303-s_lc.fits` | 18814 | 14851 | 3.00 | 201 | 201 |
| `tess2026086090000-s0102-0000000290403522-0304-s_lc.fits` | 17790 | 15103 | 2.50 | 104 | 104 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

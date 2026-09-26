<!-- [private Drive store] -->
# Search log: toi-630-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 218 (38 distinct events, 33 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2020351194500-s0033-0000000123898871-0203-s_lc.fits` | 18609 | 17453 | 3.50 | 55 | 49 |
| `tess2024353092137-s0087-0000000123898871-0284-s_lc.fits` | 19370 | 14969 | 4.00 | 99 | 99 |
| `tess2025312202959-s0098-0000000123898871-0298-s_lc.fits` | 41332 | 26931 | 4.00 | 70 | 70 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

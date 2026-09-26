<!-- cygnus:generated-draft -->
# Search log: toi-768-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 96 (16 distinct events, 11 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2021091135823-s0037-0000000229811538-0208-s_lc.fits` | 18249 | 15500 | 2.50 | 24 | 12 |
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | 18900 | 14855 | 3.00 | 29 | 29 |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 19385 | 17260 | 2.50 | 55 | 55 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

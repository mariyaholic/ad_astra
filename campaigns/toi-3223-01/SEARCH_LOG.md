<!-- cygnus:generated-draft -->
# Search log: toi-3223-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 3 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 851 (189 distinct events, 110 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000297668572-0257-s_lc.fits` | 19385 | 18854 | 2.50 | 572 | 572 |
| `tess2023124020739-s0065-0000000297668572-0259-s_lc.fits` | 20085 | 19515 | 3.50 | 181 | 181 |
| `tess2026005125623-s0099-0000000297668572-0300-s_lc.fits` | 19922 | 13905 | 4.00 | 98 | 98 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

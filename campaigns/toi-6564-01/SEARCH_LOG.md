<!-- cygnus:generated-draft -->
# Search log: toi-6564-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 389 (137 distinct events, 34 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000453668803-0259-s_lc.fits` | 20085 | 15822 | 3.00 | 65 | 53 |
| `tess2026005125623-s0099-0000000453668803-0300-s_lc.fits` | 19922 | 13996 | 3.00 | 112 | 112 |
| `tess2026033082000-s0100-0000000453668803-0302-s_lc.fits` | 19064 | 17122 | 3.00 | 85 | 85 |
| `tess2026060005000-s0101-0000000453668803-0303-s_lc.fits` | 18814 | 16038 | 3.00 | 64 | 64 |
| `tess2026086090000-s0102-0000000453668803-0304-s_lc.fits` | 17790 | 16088 | 3.50 | 75 | 75 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

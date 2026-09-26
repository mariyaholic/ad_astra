<!-- cygnus:generated-draft -->
# Search log: toi-3241-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 790 (297 distinct events, 36 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000241326434-0257-s_lc.fits` | 19385 | 18854 | 2.50 | 70 | 70 |
| `tess2023124020739-s0065-0000000241326434-0259-s_lc.fits` | 20085 | 17165 | 2.50 | 248 | 248 |
| `tess2026005125623-s0099-0000000241326434-0300-s_lc.fits` | 19922 | 13969 | 2.50 | 96 | 96 |
| `tess2026033082000-s0100-0000000241326434-0302-s_lc.fits` | 19064 | 17080 | 2.50 | 102 | 102 |
| `tess2026060005000-s0101-0000000241326434-0303-s_lc.fits` | 18814 | 15979 | 2.50 | 128 | 128 |
| `tess2026086090000-s0102-0000000241326434-0304-s_lc.fits` | 17790 | 15669 | 2.50 | 146 | 146 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

<!-- cygnus:generated-draft -->
# Search log: toi-3157-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 330 (83 distinct events, 45 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000456962262-0257-s_lc.fits` | 19385 | 18852 | 3.00 | 19 | 19 |
| `tess2023124020739-s0065-0000000456962262-0259-s_lc.fits` | 20085 | 15880 | 3.00 | 18 | 18 |
| `tess2026005125623-s0099-0000000456962262-0300-s_lc.fits` | 19922 | 14078 | 2.50 | 191 | 191 |
| `tess2026033082000-s0100-0000000456962262-0302-s_lc.fits` | 19064 | 18010 | 3.00 | 50 | 50 |
| `tess2026060005000-s0101-0000000456962262-0303-s_lc.fits` | 18814 | 15918 | 3.50 | 16 | 16 |
| `tess2026086090000-s0102-0000000456962262-0304-s_lc.fits` | 17790 | 16130 | 3.00 | 36 | 36 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

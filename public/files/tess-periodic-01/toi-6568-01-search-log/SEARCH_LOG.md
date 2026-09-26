<!-- [private Drive store] -->
# Search log: toi-6568-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 5 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 400 (149 distinct events, 7 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 1 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000253126207-0259-s_lc.fits` | 20085 | 18722 | 2.50 | 150 | 150 |
| `tess2023096110322-s0064-0000000253126207-0257-s_lc.fits` | 19385 | 18852 | 2.50 | 42 | 42 |
| `tess2026005125623-s0099-0000000253126207-0300-s_lc.fits` | 19922 | 13909 | 2.50 | 101 | 101 |
| `tess2026033082000-s0100-0000000253126207-0302-s_lc.fits` | 19064 | 17211 | 3.00 | 57 | 57 |
| `tess2026060005000-s0101-0000000253126207-0303-s_lc.fits` | 18814 | 15963 | 2.50 | 50 | 50 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

# Search log: toi-285-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 35 (17 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018263035959-s0003-0000000220459976-0123-s_lc.fits` | 19692 | 12695 | 2.50 | 10 | 9 |
| `tess2018234235059-s0002-0000000220459976-0121-s_lc.fits` | 19737 | 18296 | 3.00 | 0 | 0 |
| `tess2018292075959-s0004-0000000220459976-0124-s_lc.fits` | 18684 | 14551 | 4.00 | 12 | 12 |
| `tess2018319095959-s0005-0000000220459976-0125-s_lc.fits` | 18944 | 16955 | 3.00 | 0 | 0 |
| `tess2018349182500-s0006-0000000220459976-0126-s_lc.fits` | 15678 | 14433 | 2.50 | 14 | 14 |
| `tess2019006130736-s0007-0000000220459976-0131-s_lc.fits` | 17612 | 16072 | 3.00 | 0 | 0 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

# Search log: toi-429-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 49 (22 distinct events, 1 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018319095959-s0005-0000000259592689-0125-s_lc.fits` | 18944 | 17212 | 3.00 | 16 | 0 |
| `tess2018263035959-s0003-0000000259592689-0123-s_lc.fits` | 19692 | 12524 | 3.00 | 0 | 0 |
| `tess2018292075959-s0004-0000000259592689-0124-s_lc.fits` | 18684 | 14504 | 3.00 | 6 | 6 |
| `tess2018349182500-s0006-0000000259592689-0126-s_lc.fits` | 15678 | 14508 | 3.00 | 2 | 2 |
| `tess2020266004630-s0030-0000000259592689-0195-s_lc.fits` | 19687 | 16434 | 3.00 | 2 | 2 |
| `tess2020294194027-s0031-0000000259592689-0198-s_lc.fits` | 18314 | 16595 | 2.50 | 39 | 39 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

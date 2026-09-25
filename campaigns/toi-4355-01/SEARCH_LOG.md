# Search log: toi-4355-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 366 (185 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019006130736-s0007-0000000260655847-0131-s_lc.fits` | 17612 | 16169 | 2.50 | 79 | 66 |
| `tess2018206045859-s0001-0000000260655847-0120-s_lc.fits` | 20076 | 18276 | 3.00 | 95 | 95 |
| `tess2018234235059-s0002-0000000260655847-0121-s_lc.fits` | 19737 | 18295 | 3.00 | 33 | 33 |
| `tess2018263035959-s0003-0000000260655847-0123-s_lc.fits` | 19692 | 12642 | 3.00 | 5 | 5 |
| `tess2018292075959-s0004-0000000260655847-0124-s_lc.fits` | 18684 | 14689 | 3.00 | 64 | 64 |
| `tess2018319095959-s0005-0000000260655847-0125-s_lc.fits` | 18944 | 17117 | 2.50 | 103 | 103 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

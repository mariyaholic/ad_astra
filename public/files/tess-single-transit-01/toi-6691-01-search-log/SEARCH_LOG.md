# Search log: toi-6691-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 207 (92 distinct events, 6 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2019006130736-s0007-0000000382258844-0131-s_lc.fits` | 17612 | 16167 | 2.50 | 49 | 46 |
| `tess2018206045859-s0001-0000000382258844-0120-s_lc.fits` | 20076 | 18279 | 2.50 | 62 | 62 |
| `tess2018263035959-s0003-0000000382258844-0123-s_lc.fits` | 19692 | 12939 | 3.00 | 5 | 5 |
| `tess2018292075959-s0004-0000000382258844-0124-s_lc.fits` | 18684 | 14685 | 2.50 | 62 | 62 |
| `tess2018319095959-s0005-0000000382258844-0125-s_lc.fits` | 18944 | 17274 | 2.50 | 30 | 30 |
| `tess2018349182500-s0006-0000000382258844-0126-s_lc.fits` | 15678 | 14506 | 3.00 | 2 | 2 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

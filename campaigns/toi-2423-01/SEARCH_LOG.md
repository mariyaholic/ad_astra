# Search log: toi-2423-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 5 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 190 (69 distinct events, 8 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2018234235059-s0002-0000000197807043-0121-s_lc.fits` | 19737 | 18298 | 3.00 | 0 | 0 |
| `tess2018292075959-s0004-0000000197807043-0124-s_lc.fits` | 18684 | 14788 | 2.50 | 94 | 94 |
| `tess2023237165326-s0069-0000000197807043-0264-s_lc.fits` | 18569 | 14463 | 4.50 | 0 | 0 |
| `tess2025232030459-s0096-0000000197807043-0293-s_lc.fits` | 18487 | 15420 | 2.50 | 27 | 27 |
| `tess2025258001959-s0097-0000000197807043-0294-s_lc.fits` | 39335 | 28994 | 3.50 | 69 | 69 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

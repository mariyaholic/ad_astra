# Search log: toi-125-04

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive | MAST (TESS SPOC 120-s light curves), discovered with the MAST Observations API |
| Products screened | 6 |
| Selection | QUALITY = 0 with finite, nonzero TIME, SAP_FLUX, PDCSAP_FLUX |
| Veto | {'kind': 'single_epoch', 'veto_hours': 12} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 104 (53 distinct events, 3 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000052368076-0264-s_lc.fits` | 18569 | 14693 | 2.50 | 26 | 26 |
| `tess2018206045859-s0001-0000000052368076-0120-s_lc.fits` | 20076 | 18276 | 3.00 | 7 | 7 |
| `tess2018234235059-s0002-0000000052368076-0121-s_lc.fits` | 19737 | 18298 | 3.00 | 1 | 1 |
| `tess2020212050318-s0028-0000000052368076-0190-s_lc.fits` | 18182 | 15219 | 2.50 | 18 | 18 |
| `tess2023209231226-s0068-0000000052368076-0262-s_lc.fits` | 19824 | 15309 | 2.50 | 48 | 48 |
| `tess2025206162959-s0095-0000000052368076-0292-s_lc.fits` | 18167 | 15140 | 3.50 | 4 | 4 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

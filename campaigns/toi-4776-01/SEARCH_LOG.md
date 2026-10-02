<!-- cygnus:generated-draft -->
# Search log: toi-4776-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 1 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 10.4137997, 't0_bjd': 2459245.97102, 'veto_phase': 0.0227, 'depth_ppm': 6720.0, 'duration_h': 3.774, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 63), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:30:25Z (rowupdate 2024-08-22 10:08:01)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 16 (7 distinct events, 0 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000196286578-0250-s_lc.fits` | 18312 | 15652 | 3.50 | 16 | 16 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

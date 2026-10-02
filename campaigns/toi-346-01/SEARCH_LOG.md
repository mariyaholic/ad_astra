<!-- cygnus:generated-draft -->
# Search log: toi-346-01

> Generated draft; see REPORT.md.

| Item | Value |
|---|---|
| Archive(s) | MAST (discovered via the archive adapters; formats spoc_lc) |
| Products fetched | 6 (kinds: lightcurve) |
| Selection | QUALITY = 0 with finite, nonzero channels as read per archive |
| Veto | {'kind': 'ephemeris', 'period_days': 16.56308, 't0_bjd': 2460192.019645, 'veto_phase': 0.02, 'depth_ppm': 14010.0, 'duration_h': 2.317, 'source': 'campaigns/tess-periodic-02/target_queue.csv (rank 86), NASA Exoplanet Archive TOI row refreshed 2026-09-30T21:31:55Z (rowupdate 2024-04-23 10:09:23)'} |
| Threshold | calibrated per light curve (k*), SAP and PDCSAP both, ≥ 2 cadences, baselines 1/2/3 d |
| Entries outside veto | 162 (32 distinct events, 22 persistent) |
| Catalogue services | NASA_Exoplanet_Archive, SIMBAD, TESS_TOI, VSX |
| Random seed | 20260927 |

## Per product

| Product | Rows | Usable | k | Entries | Outside veto |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000118327533-0264-s_lc.fits` | 18569 | 14680 | 2.50 | 33 | 3 |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 18864 | 14926 | 2.50 | 39 | 39 |
| `tess2025232030459-s0096-0000000118327533-0293-s_lc.fits` | 18487 | 15003 | 3.50 | 0 | 0 |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 19167 | 15697 | 3.00 | 74 | 74 |
| `tess2026164183000-s0105-0000000118327533-0307-s_lc.fits` | 19915 | 15444 | 3.50 | 22 | 22 |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 20484 | 12997 | 3.00 | 24 | 24 |

## Not searched / not tested

- Sectors beyond those listed above (at most six light curves per target are retrieved).
- Full-frame-image and non-SPOC light curves; alternative detrending; difference-image centroids; pointing correlation; ADS literature.

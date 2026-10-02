<!-- cygnus:generated-draft -->
# Known-object test, TOI-346.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-346-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5115, calibrate_screen #5021, event_census #5028, fetch_independent #5108, fetch_products #5008, known_signal_recovery #5023, moving_objects #5100, period_aliases #5030, prior_art #5122, residual_screen #5025, stellar_context #5024, variability_guard #5116
- Runner finished (UTC): 2026-09-30T23:02:36Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-346.01 (BJD 2460192.0196: recovered, depth 21072 ± 764 ppm (catalogue 14010 ppm); BJD 2459098.8564: gap (catalogue 14010 ppm); BJD 2460920.7952: gap (catalogue 14010 ppm); BJD 2461185.8044: not recovered, depth -1757 ± 663 ppm (catalogue 14010 ppm); BJD 2461202.3675: not recovered, depth -2751 ± 696 ppm (catalogue 14010 ppm); BJD 2461218.9306: gap (catalogue 14010 ppm); BJD 2461235.4937: not recovered, depth 4211 ± 590 ppm (catalogue 14010 ppm); BJD 2461252.0568: not recovered, depth -268 ± 675 ppm (catalogue 14010 ppm)).
Outside the catalogued epoch the screen left 162 threshold entries forming **32 distinct event(s)**, **22 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461185.0876 matches the catalogued transit's depth (14119 vs 21072 ppm), 993.067 d later; 16 of 993 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-346.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 118327533 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 10.344507 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -37.34302 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460192.019645 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 16.56308 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 14010.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.317 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.7291 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-04-23 10:09:23 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000118327533-0264-s_lc.fits` | lightcurve | 69 | True | `6c851f43f3101e87` | True |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | lightcurve | 29 | False | `b976ef27e98fa35b` | True |
| `tess2025232030459-s0096-0000000118327533-0293-s_lc.fits` | lightcurve | 96 | False | `e080f68513f060ac` | True |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | lightcurve | 104 | False | `5580f43041e3ad2a` | True |
| `tess2026164183000-s0105-0000000118327533-0307-s_lc.fits` | lightcurve | 105 | False | `12765e6e609c8d59` | True |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | lightcurve | 106 | False | `9bcf2e6182045e82` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000118327533-0264-s_lc.fits` | 2460192.01964 | recovered | 70 | 21072 ± 764 | 14010 | 0.01 |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459098.85636 | gap | 0 | — | 14010 | — |
| `tess2025232030459-s0096-0000000118327533-0293-s_lc.fits` | 2460920.79517 | gap | 0 | — | 14010 | — |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461185.80444 | not_recovered | 70 | -1757 ± 663 | 14010 | — |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461202.36752 | not_recovered | 69 | -2751 ± 696 | 14010 | — |
| `tess2026164183000-s0105-0000000118327533-0307-s_lc.fits` | 2461218.93060 | gap | 0 | — | 14010 | — |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 2461235.49368 | not_recovered | 69 | 4211 ± 590 | 14010 | — |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 2461252.05676 | not_recovered | 68 | -268 ± 675 | 14010 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023237165326-s0069-0000000118327533-0264-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2025232030459-s0096-0000000118327533-0293-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: —, 8h: — |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026164183000-s0105-0000000118327533-0307-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461185.09874 | -0.03095 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 2461251.31524 | -0.02830 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000118327533-0307-s_lc.fits` | 2461218.22068 | -0.02815 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000118327533-0307-s_lc.fits` | 2461218.19637 | -0.02669 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461185.12443 | -0.02638 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461201.67776 | -0.02635 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461201.64443 | -0.02478 | 22 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026164183000-s0105-0000000118327533-0307-s_lc.fits` | 2461218.24291 | -0.02457 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461201.68749 | -0.02382 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461185.08763 | -0.02248 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461185.14110 | -0.02149 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461201.64026 | -0.02148 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 2461251.28538 | -0.02146 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 2461251.34094 | -0.02088 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000118327533-0308-s_lc.fits` | 2461251.29094 | -0.02077 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461201.63332 | -0.01957 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459112.43534 | -0.01704 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459112.10618 | -0.01625 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459112.25340 | -0.01616 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459108.60481 | -0.01532 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459108.86731 | -0.01453 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459112.33256 | -0.01443 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026137223500-s0104-0000000118327533-0306-s_lc.fits` | 2461185.14874 | -0.02082 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000118327533-0264-s_lc.fits` | 2460205.86403 | -0.01745 | 2 | SAP | 2, 3 | no |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459094.98946 | -0.01653 | 2 | SAP | 1, 2, 3 | no |
| `tess2023237165326-s0069-0000000118327533-0264-s_lc.fits` | 2460205.98764 | -0.01476 | 2 | SAP | 2 | no |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459112.31590 | -0.01458 | 2 | PDCSAP | 3 | no |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459102.44232 | -0.01451 | 2 | SAP | 1, 2, 3 | no |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459111.71451 | -0.01424 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459111.99646 | -0.01342 | 2 | PDCSAP | 3 | no |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459111.94368 | -0.01288 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000118327533-0193-s_lc.fits` | 2459091.28246 | -0.01271 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461185.08763 | 14119 | 21072 | 993.0674 | 16 / 993 | 993.067, 496.534, 331.022, 248.267, 198.613, 165.511, 141.867, 124.133, 99.3067, 82.7556, 76.3898, 66.2045, 62.0667, 49.6534, 33.1022, 16.5511 |
| 2461185.09874 | 16089 | 21072 | 993.0785 | 16 / 993 | 993.078, 496.539, 331.026, 248.27, 198.616, 165.513, 141.868, 124.135, 99.3079, 82.7565, 76.3907, 66.2052, 62.0674, 49.6539, 33.1026, 16.5513 |
| 2461185.12443 | 16757 | 21072 | 993.1042 | 16 / 993 | 993.104, 496.552, 331.035, 248.276, 198.621, 165.517, 141.872, 124.138, 99.3104, 82.7587, 76.3926, 66.2069, 62.069, 49.6552, 33.1035, 16.5517 |
| 2461185.14110 | 13326 | 21072 | 993.1209 | 16 / 993 | 993.121, 496.56, 331.04, 248.28, 198.624, 165.52, 141.874, 124.14, 99.3121, 82.7601, 76.3939, 66.2081, 62.0701, 49.656, 33.104, 16.552 |
| 2461201.63332 | 16489 | 21072 | 1009.6131 | 14 / 1009 | 1009.61, 504.807, 336.538, 252.403, 201.923, 168.269, 126.202, 112.179, 100.961, 63.1008, 59.389, 53.1375, 32.5682, 16.551 |
| 2461201.64026 | 17570 | 21072 | 1009.6200 | 14 / 1009 | 1009.62, 504.81, 336.54, 252.405, 201.924, 168.27, 126.203, 112.18, 100.962, 63.1013, 59.3894, 53.1379, 32.5684, 16.5511 |
| 2461201.64443 | 18731 | 21072 | 1009.6242 | 14 / 1009 | 1009.62, 504.812, 336.541, 252.406, 201.925, 168.271, 126.203, 112.18, 100.962, 63.1015, 59.3897, 53.1381, 32.5685, 16.5512 |
| 2461201.67776 | 19437 | 21072 | 1009.6575 | 14 / 1009 | 1009.66, 504.829, 336.553, 252.414, 201.931, 168.276, 126.207, 112.184, 100.966, 63.1036, 59.3916, 53.1399, 32.5696, 16.5518 |
| 2461201.68749 | 17552 | 21072 | 1009.6673 | 14 / 1009 | 1009.67, 504.834, 336.556, 252.417, 201.934, 168.278, 126.208, 112.185, 100.967, 63.1042, 59.3922, 53.1404, 32.5699, 16.5519 |
| 2461218.19637 | 22444 | 21072 | 1026.1761 | 16 / 1026 | 1026.18, 513.088, 342.059, 256.544, 205.235, 171.029, 128.272, 114.02, 93.2887, 85.5147, 78.9366, 64.136, 46.6444, 44.6164, 33.1025, 16.5512 |
| 2461218.22068 | 22713 | 21072 | 1026.2005 | 16 / 1026 | 1026.2, 513.1, 342.067, 256.55, 205.24, 171.033, 128.275, 114.022, 93.291, 85.5167, 78.9385, 64.1375, 46.6455, 44.6174, 33.1032, 16.5516 |
| 2461218.24291 | 18330 | 21072 | 1026.2227 | 16 / 1026 | 1026.22, 513.111, 342.074, 256.556, 205.244, 171.037, 128.278, 114.025, 93.293, 85.5186, 78.9402, 64.1389, 46.6465, 44.6184, 33.104, 16.552 |
| 2461251.28538 | 15014 | 21072 | 1059.2652 | 17 / 1059 | 1059.27, 529.633, 353.088, 264.816, 211.853, 176.544, 151.324, 132.408, 117.696, 105.927, 96.2968, 88.2721, 75.6618, 66.2041, 58.8481, 33.102, 16.551 |
| 2461251.29094 | 16627 | 21072 | 1059.2707 | 17 / 1059 | 1059.27, 529.635, 353.09, 264.818, 211.854, 176.545, 151.324, 132.409, 117.697, 105.927, 96.2973, 88.2726, 75.6622, 66.2044, 58.8484, 33.1022, 16.5511 |
| 2461251.31524 | 20297 | 21072 | 1059.2950 | 17 / 1059 | 1059.3, 529.648, 353.098, 264.824, 211.859, 176.549, 151.328, 132.412, 117.699, 105.93, 96.2995, 88.2746, 75.6639, 66.2059, 58.8497, 33.103, 16.5515 |
| 2461251.34094 | 16627 | 21072 | 1059.3207 | 17 / 1059 | 1059.32, 529.66, 353.107, 264.83, 211.864, 176.554, 151.332, 132.415, 117.702, 105.932, 96.3019, 88.2767, 75.6658, 66.2075, 58.8512, 33.1038, 16.5519 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-346.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T23:02:24Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T23:02:27Z: TOI-346.01 (TIC 118327533, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T23:02:30Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T23:02:33Z: BPS CS 22188-0057 (*); TOI-346.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460192.0196: recovered, depth 21072 ± 764 ppm (catalogue 14010 ppm); BJD 2459098.8564: gap (catalogue 14010 ppm); BJD 2460920.7952: gap (catalogue 14010 ppm); BJD 2461185.8044: not recovered, depth -1757 ± 663 ppm (catalogue 14010 ppm); BJD 2461202.3675: not recovered, depth -2751 ± 696 ppm (catalogue 14010 ppm); BJD 2461218.9306: gap (catalogue 14010 ppm); BJD 2461235.4937: not recovered, depth 4211 ± 590 ppm (catalogue 14010 ppm); BJD 2461252.0568: not recovered, depth -268 ± 675 ppm (catalogue 14010 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3.5, 3, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 16 repeat-candidate event(s); first at BJD 2461185.0876, ΔT = 993.067 d, 16 of 993 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (993.067, 496.534, 331.022, 248.267, 198.613, 165.511, 141.867, 124.133, 99.3067, 82.7556, 76.3898, 66.2045 … d); duration likelihood under Gaia priors (circular orbits) peaks at 16.6 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-346.01: Gaia DR3 5001039273555456768 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-346.01: Teff 6100 K, R* 1.31 ± 0.11, M* 1.21 ± 0.12, ρ* 0.54 ± 0.14 ρ☉ (dwarf sequence, M_G 3.69, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-346.01: 2 Gaia neighbour(s) within 52.5", contamination 0.45%; depth 21072 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 22 persistent event(s), 9 clean; BJD 2459108.6048 caution: coarse point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d); BJD 2459112.1062 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+6.4; BJD 2459112.2534 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+8.0; BJD 2459112.3326 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+8.5 |
| Moving objects at screen-event epochs | inconclusive | 22 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-346.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-346.01: TOI-346.01 otype Pl? (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 16 possible published-ephemeris overlap(s) within 1 d (TOI-346.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-346-01.yaml
python -m cygnus.multi report campaigns/toi-346-01.yaml
```

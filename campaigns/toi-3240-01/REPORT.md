<!-- cygnus:generated-draft -->
# Known-object test, TOI-3240.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3240-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4295, calibrate_screen #4275, event_census #4280, fetch_independent #4286, fetch_products #4269, known_signal_recovery #4276, moving_objects #4282, period_aliases #4281, prior_art #4297, residual_screen #4279, stellar_context #4277, variability_guard #4296
- Runner finished (UTC): 2026-09-30T21:46:23Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3240.01 (BJD 2460041.1472: not recovered, depth 3727 ± 1242 ppm (catalogue 16960 ppm); BJD 2460045.0073: recovered, depth 16333 ± 1053 ppm (catalogue 16960 ppm); BJD 2460048.8673: not recovered, depth 18472 ± 1078 ppm (catalogue 16960 ppm); BJD 2460052.7274: recovered, depth 17578 ± 1093 ppm (catalogue 16960 ppm); BJD 2460056.5875: recovered, depth 16097 ± 1100 ppm (catalogue 16960 ppm); BJD 2460060.4476: not recovered, depth 15693 ± 1062 ppm (catalogue 16960 ppm); BJD 2460064.3076: partial, depth 15624 ± 1114 ppm (catalogue 16960 ppm); BJD 2460072.0278: recovered, depth 16382 ± 785 ppm (catalogue 16960 ppm); BJD 2460075.8878: recovered, depth 19228 ± 823 ppm (catalogue 16960 ppm); BJD 2460079.7479: recovered, depth 15655 ± 896 ppm (catalogue 16960 ppm); BJD 2460083.6080: gap (catalogue 16960 ppm); BJD 2460087.4681: recovered, depth 15330 ± 879 ppm (catalogue 16960 ppm); BJD 2460091.3281: recovered, depth 14350 ± 835 ppm (catalogue 16960 ppm); BJD 2460095.1882: gap (catalogue 16960 ppm); BJD 2461102.6670: not recovered, depth 13033 ± 940 ppm (catalogue 16960 ppm); BJD 2461106.5271: partial, depth 17830 ± 933 ppm (catalogue 16960 ppm); BJD 2461110.3872: recovered, depth 18789 ± 953 ppm (catalogue 16960 ppm); BJD 2461114.2473: recovered, depth 16753 ± 957 ppm (catalogue 16960 ppm); BJD 2461118.1073: recovered, depth 15249 ± 934 ppm (catalogue 16960 ppm); BJD 2461121.9674: not recovered, depth 17158 ± 939 ppm (catalogue 16960 ppm); BJD 2461125.8275: gap (catalogue 16960 ppm); BJD 2461129.6876: recovered, depth 16796 ± 865 ppm (catalogue 16960 ppm); BJD 2461133.5476: recovered, depth 17863 ± 872 ppm (catalogue 16960 ppm); BJD 2461137.4077: recovered, depth 15612 ± 922 ppm (catalogue 16960 ppm); BJD 2461141.2678: recovered, depth 15570 ± 931 ppm (catalogue 16960 ppm); BJD 2461145.1278: recovered, depth 15488 ± 974 ppm (catalogue 16960 ppm); BJD 2461148.9879: recovered, depth 15989 ± 884 ppm (catalogue 16960 ppm)).
Outside the catalogued epoch the screen left 72 threshold entries forming **32 distinct event(s)**, **4 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460094.6319 matches the catalogued transit's depth (9897 vs 16333 ppm), 49.618 d later; 0 of 49 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3240.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 241514551 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 206.327123 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -50.480521 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459357.914411 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.8600722 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16960.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.93 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.8713 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | lightcurve | 64 | False | `fd54e48ad33a7d97` | True |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | lightcurve | 65 | False | `d81b247610c9af55` | True |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | lightcurve | 101 | False | `2253f0ee2aa0e708` | True |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | lightcurve | 102 | False | `5c7e99efeaac712d` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 2460041.14719 | not_recovered | 50 | 3727 ± 1242 | 16960 | — |
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 2460045.00726 | recovered | 58 | 16333 ± 1053 | 16960 | 0.16 |
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 2460048.86733 | not_recovered | 57 | 18472 ± 1078 | 16960 | — |
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 2460052.72741 | recovered | 58 | 17578 ± 1093 | 16960 | -0.05 |
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 2460056.58748 | recovered | 58 | 16097 ± 1100 | 16960 | -0.38 |
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 2460060.44755 | not_recovered | 58 | 15693 ± 1062 | 16960 | — |
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 2460064.30762 | partial | 58 | 15624 ± 1114 | 16960 | -0.16 |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460072.02777 | recovered | 58 | 16382 ± 785 | 16960 | -0.02 |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460075.88784 | recovered | 58 | 19228 ± 823 | 16960 | 0.00 |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460079.74791 | recovered | 58 | 15655 ± 896 | 16960 | 0.09 |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.60798 | gap | 0 | — | 16960 | — |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460087.46806 | recovered | 53 | 15330 ± 879 | 16960 | -0.03 |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460091.32813 | recovered | 58 | 14350 ± 835 | 16960 | -0.27 |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460095.18820 | gap | 0 | — | 16960 | — |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 2461102.66705 | not_recovered | 57 | 13033 ± 940 | 16960 | — |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 2461106.52712 | partial | 58 | 17830 ± 933 | 16960 | -0.52 |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 2461110.38719 | recovered | 58 | 18789 ± 953 | 16960 | -0.55 |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 2461114.24726 | recovered | 58 | 16753 ± 957 | 16960 | -0.26 |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 2461118.10733 | recovered | 58 | 15249 ± 934 | 16960 | -0.09 |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 2461121.96741 | not_recovered | 58 | 17158 ± 939 | 16960 | — |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 2461125.82748 | gap | 0 | — | 16960 | — |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461129.68755 | recovered | 58 | 16796 ± 865 | 16960 | -0.10 |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461133.54762 | recovered | 58 | 17863 ± 872 | 16960 | -0.32 |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461137.40770 | recovered | 58 | 15612 ± 922 | 16960 | 0.00 |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461141.26777 | recovered | 57 | 15570 ± 931 | 16960 | -0.15 |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461145.12784 | recovered | 53 | 15488 ± 974 | 16960 | -0.06 |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461148.98791 | recovered | 58 | 15989 ± 884 | 16960 | -0.26 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000241514551-0257-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026060005000-s0101-0000000241514551-0303-s_lc.fits` | 4 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460094.63194 | -0.02169 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460082.49195 | -0.01920 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460094.63888 | -0.01908 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460094.67777 | -0.01803 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460094.65971 | -0.02214 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460089.76124 | -0.02019 | 2 | SAP | 2, 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461127.30670 | -0.01884 | 2 | PDCSAP | 1, 2 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460094.41250 | -0.01697 | 2 | PDCSAP+SAP | 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.16138 | -0.01665 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460089.78902 | -0.01535 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.19749 | -0.01504 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.20166 | -0.01493 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460082.95166 | -0.01482 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460082.97389 | -0.01449 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460089.63069 | -0.01403 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.06555 | -0.01401 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460089.92235 | -0.01399 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461144.94630 | -0.01389 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460089.87790 | -0.01389 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461145.90188 | -0.01383 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.25166 | -0.01371 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460082.57667 | -0.01370 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461145.83382 | -0.01363 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460094.55555 | -0.01331 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460089.54736 | -0.01320 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460090.10290 | -0.01318 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.10861 | -0.01316 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461145.67965 | -0.01306 | 3 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000241514551-0259-s_lc.fits` | 2460083.20583 | -0.01286 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461127.41643 | -0.01194 | 2 | SAP | 1, 2, 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461145.71021 | -0.01175 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000241514551-0304-s_lc.fits` | 2461133.12365 | -0.01143 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460094.63194 | 9897 | 16333 | 49.6181 | 0 / 49 |  |
| 2460094.63888 | 10266 | 16333 | 49.6251 | 0 / 49 |  |
| 2460094.67777 | 10845 | 16333 | 49.6640 | 0 / 49 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3240.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:46:12Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:46:15Z: TOI-3240.01 (TIC 241514551, disposition PC)
- VSX (done, 2026-09-30): 1 match(es) in VSX within 30" as of 2026-09-30T21:46:17Z: Gaia DR3 6069644282317331200 (type ROT, P — d)
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:46:19Z: TOI-3240 (*); TOI-3240.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460041.1472: not recovered, depth 3727 ± 1242 ppm (catalogue 16960 ppm); BJD 2460045.0073: recovered, depth 16333 ± 1053 ppm (catalogue 16960 ppm); BJD 2460048.8673: not recovered, depth 18472 ± 1078 ppm (catalogue 16960 ppm); BJD 2460052.7274: recovered, depth 17578 ± 1093 ppm (catalogue 16960 ppm); BJD 2460056.5875: recovered, depth 16097 ± 1100 ppm (catalogue 16960 ppm); BJD 2460060.4476: not recovered, depth 15693 ± 1062 ppm (catalogue 16960 ppm); BJD 2460064.3076: partial, depth 15624 ± 1114 ppm (catalogue 16960 ppm); BJD 2460072.0278: recovered, depth 16382 ± 785 ppm (catalogue 16960 ppm); BJD 2460075.8878: recovered, depth 19228 ± 823 ppm (catalogue 16960 ppm); BJD 2460079.7479: recovered, depth 15655 ± 896 ppm (catalogue 16960 ppm); BJD 2460083.6080: gap (catalogue 16960 ppm); BJD 2460087.4681: recovered, depth 15330 ± 879 ppm (catalogue 16960 ppm); BJD 2460091.3281: recovered, depth 14350 ± 835 ppm (catalogue 16960 ppm); BJD 2460095.1882: gap (catalogue 16960 ppm); BJD 2461102.6670: not recovered, depth 13033 ± 940 ppm (catalogue 16960 ppm); BJD 2461106.5271: partial, depth 17830 ± 933 ppm (catalogue 16960 ppm); BJD 2461110.3872: recovered, depth 18789 ± 953 ppm (catalogue 16960 ppm); BJD 2461114.2473: recovered, depth 16753 ± 957 ppm (catalogue 16960 ppm); BJD 2461118.1073: recovered, depth 15249 ± 934 ppm (catalogue 16960 ppm); BJD 2461121.9674: not recovered, depth 17158 ± 939 ppm (catalogue 16960 ppm); BJD 2461125.8275: gap (catalogue 16960 ppm); BJD 2461129.6876: recovered, depth 16796 ± 865 ppm (catalogue 16960 ppm); BJD 2461133.5476: recovered, depth 17863 ± 872 ppm (catalogue 16960 ppm); BJD 2461137.4077: recovered, depth 15612 ± 922 ppm (catalogue 16960 ppm); BJD 2461141.2678: recovered, depth 15570 ± 931 ppm (catalogue 16960 ppm); BJD 2461145.1278: recovered, depth 15488 ± 974 ppm (catalogue 16960 ppm); BJD 2461148.9879: recovered, depth 15989 ± 884 ppm (catalogue 16960 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2460094.6319, ΔT = 49.618 d, 0 of 49 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3240.01: Gaia DR3 6069644282317331200 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-3240.01: Teff 4849 K, R* 0.77 ± 0.06, M* 0.80 ± 0.08, ρ* 1.77 ± 0.46 ρ☉ (dwarf sequence, M_G 6.05, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3240.01: 51 Gaia neighbour(s) within 52.5", contamination 58.23%; depth 16333 ppm (measured depth of the recovered catalogued transit); 8 could produce it if fully eclipsed (brightest 6069644282317331968, 21.5", ΔG 0.54); a centroid test is needed |
| Pointing and quality census per event | failed | 4 persistent event(s), 0 clean; BJD 2460082.4919 suspect: SAP_BKG z=+599.7; BJD 2460094.6319 suspect: scattered light 2 (within ±0.25 d), POS_CORR2 z=-6.4, SAP_BKG z=+16.9; BJD 2460094.6389 suspect: scattered light 2 (within ±0.25 d), POS_CORR2 z=-6.2, SAP_BKG z=+17.5; BJD 2460094.6778 suspect: scattered light 2 (within ±0.25 d), POS_CORR2 z=-5.1, SAP_BKG z=+20.8 |
| Moving objects at screen-event epochs | inconclusive | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-3240.01: Gaia DR3 6069644282317331200   ROT                            P=None at 0.3" |
| Object-class guard (SIMBAD) | passed | TOI-3240.01: TOI-3240 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 3 possible published-ephemeris overlap(s) within 1 d (TOI-3240.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-3240-01.yaml
python -m cygnus.multi report campaigns/toi-3240-01.yaml
```

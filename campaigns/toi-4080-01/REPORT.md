<!-- cygnus:generated-draft -->
# Known-object test, TOI-4080.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4080-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4497, calibrate_screen #4472, event_census #4477, fetch_independent #4488, fetch_products #4462, known_signal_recovery #4473, moving_objects #4484, period_aliases #4479, prior_art #4499, residual_screen #4475, stellar_context #4474, variability_guard #4498
- Runner finished (UTC): 2026-09-30T21:56:29Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4080.01 (BJD 2459746.2229: recovered, depth 12581 ± 991 ppm (catalogue 17240 ppm); BJD 2459749.9749: recovered, depth 11471 ± 981 ppm (catalogue 17240 ppm); BJD 2459753.7269: recovered, depth 14604 ± 856 ppm (catalogue 17240 ppm); BJD 2459757.4789: recovered, depth 10538 ± 948 ppm (catalogue 17240 ppm); BJD 2459761.2309: recovered, depth 13260 ± 929 ppm (catalogue 17240 ppm); BJD 2459764.9829: recovered, depth 13647 ± 916 ppm (catalogue 17240 ppm); BJD 2459768.7348: recovered, depth 13525 ± 832 ppm (catalogue 17240 ppm); BJD 2459393.5365: not recovered, depth 12278 ± 1116 ppm (catalogue 17240 ppm); BJD 2459397.2885: partial, depth 11257 ± 1009 ppm (catalogue 17240 ppm); BJD 2459401.0405: recovered, depth 14125 ± 975 ppm (catalogue 17240 ppm); BJD 2459404.7925: gap (catalogue 17240 ppm); BJD 2459408.5445: partial, depth 12585 ± 1039 ppm (catalogue 17240 ppm); BJD 2459412.2964: not recovered, depth 13995 ± 914 ppm (catalogue 17240 ppm); BJD 2459416.0484: not recovered, depth 13511 ± 869 ppm (catalogue 17240 ppm); BJD 2459719.9591: recovered, depth 14582 ± 1148 ppm (catalogue 17240 ppm); BJD 2459723.7110: recovered, depth 13847 ± 1055 ppm (catalogue 17240 ppm); BJD 2459727.4630: recovered, depth 15026 ± 982 ppm (catalogue 17240 ppm); BJD 2459731.2150: gap (catalogue 17240 ppm); BJD 2459734.9670: not recovered, depth 13169 ± 1044 ppm (catalogue 17240 ppm); BJD 2459738.7190: recovered, depth 9950 ± 1097 ppm (catalogue 17240 ppm); BJD 2459742.4710: recovered, depth 13878 ± 884 ppm (catalogue 17240 ppm); BJD 2459911.3102: gap (catalogue 17240 ppm); BJD 2459915.0622: recovered, depth 13613 ± 812 ppm (catalogue 17240 ppm); BJD 2459918.8142: recovered, depth 12563 ± 852 ppm (catalogue 17240 ppm); BJD 2459922.5662: recovered, depth 12878 ± 857 ppm (catalogue 17240 ppm); BJD 2459926.3181: recovered, depth 15034 ± 901 ppm (catalogue 17240 ppm); BJD 2459930.0701: recovered, depth 14325 ± 827 ppm (catalogue 17240 ppm); BJD 2459933.8221: recovered, depth 14574 ± 823 ppm (catalogue 17240 ppm); BJD 2459937.5741: gap (catalogue 17240 ppm); BJD 2459941.3261: not recovered, depth 14651 ± 915 ppm (catalogue 17240 ppm); BJD 2459945.0780: not recovered, depth 12514 ± 853 ppm (catalogue 17240 ppm); BJD 2459948.8300: recovered, depth 15353 ± 836 ppm (catalogue 17240 ppm); BJD 2459952.5820: gap (catalogue 17240 ppm); BJD 2459956.3340: gap (catalogue 17240 ppm); BJD 2459960.0860: recovered, depth 14131 ± 874 ppm (catalogue 17240 ppm); BJD 2460286.5085: gap (catalogue 17240 ppm); BJD 2460290.2605: not recovered, depth 16221 ± 1390 ppm (catalogue 17240 ppm); BJD 2460294.0125: recovered, depth 18546 ± 1386 ppm (catalogue 17240 ppm); BJD 2460297.7645: not recovered, depth 18949 ± 1356 ppm (catalogue 17240 ppm); BJD 2460301.5164: gap (catalogue 17240 ppm); BJD 2460305.2684: gap (catalogue 17240 ppm); BJD 2460309.0204: recovered, depth 19386 ± 1332 ppm (catalogue 17240 ppm)).
Outside the catalogued epoch the screen left 25 threshold entries forming **8 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459912.1818 matches the catalogued transit's depth (6795 vs 12581 ppm), 165.968 d later; 0 of 165 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4080.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 428892437 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 84.865203 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 81.54345 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459764.98286 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 3.7519831 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 17240.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.891 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 13.3593 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-10-01 12:02:54 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | lightcurve | 53 | True | `dcd3465ebcdc23f6` | True |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | lightcurve | 40 | False | `82eaca024e7aa5bf` | True |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | lightcurve | 52 | False | `1bdcf05106796a99` | True |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | lightcurve | 59 | False | `bb9d0feaadcf417c` | True |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | lightcurve | 60 | False | `2f33f45b737c5d30` | True |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | lightcurve | 73 | False | `63e40024565d6c2c` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2459746.22294 | recovered | 87 | 12581 ± 991 | 17240 | -0.23 |
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2459749.97493 | recovered | 80 | 11471 ± 981 | 17240 | 0.59 |
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2459753.72691 | recovered | 87 | 14604 ± 856 | 17240 | -0.32 |
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2459757.47889 | recovered | 86 | 10538 ± 948 | 17240 | 0.13 |
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2459761.23088 | recovered | 87 | 13260 ± 929 | 17240 | -0.25 |
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2459764.98286 | recovered | 87 | 13647 ± 916 | 17240 | 0.52 |
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2459768.73484 | recovered | 87 | 13525 ± 832 | 17240 | -0.14 |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 2459393.53653 | not_recovered | 87 | 12278 ± 1116 | 17240 | — |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 2459397.28852 | partial | 86 | 11257 ± 1009 | 17240 | -0.33 |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 2459401.04050 | recovered | 87 | 14125 ± 975 | 17240 | 0.36 |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 2459404.79248 | gap | 0 | — | 17240 | — |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 2459408.54447 | partial | 86 | 12585 ± 1039 | 17240 | -0.33 |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 2459412.29645 | not_recovered | 87 | 13995 ± 914 | 17240 | — |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 2459416.04843 | not_recovered | 87 | 13511 ± 869 | 17240 | — |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459719.95906 | recovered | 87 | 14582 ± 1148 | 17240 | -0.65 |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459723.71105 | recovered | 86 | 13847 ± 1055 | 17240 | 0.18 |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459727.46303 | recovered | 87 | 15026 ± 982 | 17240 | -0.51 |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459731.21501 | gap | 0 | — | 17240 | — |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459734.96700 | not_recovered | 87 | 13169 ± 1044 | 17240 | — |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459738.71898 | recovered | 87 | 9950 ± 1097 | 17240 | 0.07 |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459742.47096 | recovered | 87 | 13878 ± 884 | 17240 | -0.44 |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459911.31020 | gap | 0 | — | 17240 | — |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459915.06218 | recovered | 87 | 13613 ± 812 | 17240 | -0.43 |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459918.81417 | recovered | 87 | 12563 ± 852 | 17240 | -0.06 |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459922.56615 | recovered | 87 | 12878 ± 857 | 17240 | -0.19 |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459926.31813 | recovered | 86 | 15034 ± 901 | 17240 | -0.53 |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459930.07012 | recovered | 87 | 14325 ± 827 | 17240 | -0.26 |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459933.82210 | recovered | 87 | 14574 ± 823 | 17240 | -0.29 |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459937.57408 | gap | 0 | — | 17240 | — |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459941.32607 | not_recovered | 87 | 14651 ± 915 | 17240 | — |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459945.07805 | not_recovered | 87 | 12514 ± 853 | 17240 | — |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459948.83003 | recovered | 87 | 15353 ± 836 | 17240 | -0.10 |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459952.58201 | gap | 0 | — | 17240 | — |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459956.33400 | gap | 0 | — | 17240 | — |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459960.08598 | recovered | 86 | 14131 ± 874 | 17240 | 0.56 |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 2460286.50851 | gap | 0 | — | 17240 | — |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 2460290.26049 | not_recovered | 87 | 16221 ± 1390 | 17240 | — |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 2460294.01248 | recovered | 86 | 18546 ± 1386 | 17240 | 0.40 |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 2460297.76446 | not_recovered | 87 | 18949 ± 1356 | 17240 | — |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 2460301.51644 | gap | 0 | — | 17240 | — |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 2460305.26843 | gap | 0 | — | 17240 | — |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 2460309.02041 | recovered | 87 | 19386 ± 1332 | 17240 | -0.53 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022164095748-s0053-0000000428892437-0226-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2021175071901-s0040-0000000428892437-0211-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: 20000, 8h: — |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: 20000, 4h: —, 8h: — |
| `tess2023341045131-s0073-0000000428892437-0268-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022138205153-s0052-0000000428892437-0224-s_lc.fits` | 2459720.15424 | -0.03248 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459912.18183 | -0.03006 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459911.87627 | -0.02570 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459912.03044 | -0.02488 | 2 | PDCSAP | 3 | no |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459955.07211 | -0.02457 | 2 | SAP | 3 | no |
| `tess2022357055054-s0060-0000000428892437-0249-s_lc.fits` | 2459939.97369 | -0.02309 | 2 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459936.62510 | -0.01897 | 2 | SAP | 2, 3 | no |
| `tess2022330142927-s0059-0000000428892437-0248-s_lc.fits` | 2459926.63896 | -0.01779 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459912.18183 | 6795 | 12581 | 165.9683 | 0 / 165 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4080.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:56:19Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:56:23Z: TOI-4080.01 (TIC 428892437, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:56:25Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T21:56:27Z: TOI-4080.01 (Pl?); TOI-4080 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459746.2229: recovered, depth 12581 ± 991 ppm (catalogue 17240 ppm); BJD 2459749.9749: recovered, depth 11471 ± 981 ppm (catalogue 17240 ppm); BJD 2459753.7269: recovered, depth 14604 ± 856 ppm (catalogue 17240 ppm); BJD 2459757.4789: recovered, depth 10538 ± 948 ppm (catalogue 17240 ppm); BJD 2459761.2309: recovered, depth 13260 ± 929 ppm (catalogue 17240 ppm); BJD 2459764.9829: recovered, depth 13647 ± 916 ppm (catalogue 17240 ppm); BJD 2459768.7348: recovered, depth 13525 ± 832 ppm (catalogue 17240 ppm); BJD 2459393.5365: not recovered, depth 12278 ± 1116 ppm (catalogue 17240 ppm); BJD 2459397.2885: partial, depth 11257 ± 1009 ppm (catalogue 17240 ppm); BJD 2459401.0405: recovered, depth 14125 ± 975 ppm (catalogue 17240 ppm); BJD 2459404.7925: gap (catalogue 17240 ppm); BJD 2459408.5445: partial, depth 12585 ± 1039 ppm (catalogue 17240 ppm); BJD 2459412.2964: not recovered, depth 13995 ± 914 ppm (catalogue 17240 ppm); BJD 2459416.0484: not recovered, depth 13511 ± 869 ppm (catalogue 17240 ppm); BJD 2459719.9591: recovered, depth 14582 ± 1148 ppm (catalogue 17240 ppm); BJD 2459723.7110: recovered, depth 13847 ± 1055 ppm (catalogue 17240 ppm); BJD 2459727.4630: recovered, depth 15026 ± 982 ppm (catalogue 17240 ppm); BJD 2459731.2150: gap (catalogue 17240 ppm); BJD 2459734.9670: not recovered, depth 13169 ± 1044 ppm (catalogue 17240 ppm); BJD 2459738.7190: recovered, depth 9950 ± 1097 ppm (catalogue 17240 ppm); BJD 2459742.4710: recovered, depth 13878 ± 884 ppm (catalogue 17240 ppm); BJD 2459911.3102: gap (catalogue 17240 ppm); BJD 2459915.0622: recovered, depth 13613 ± 812 ppm (catalogue 17240 ppm); BJD 2459918.8142: recovered, depth 12563 ± 852 ppm (catalogue 17240 ppm); BJD 2459922.5662: recovered, depth 12878 ± 857 ppm (catalogue 17240 ppm); BJD 2459926.3181: recovered, depth 15034 ± 901 ppm (catalogue 17240 ppm); BJD 2459930.0701: recovered, depth 14325 ± 827 ppm (catalogue 17240 ppm); BJD 2459933.8221: recovered, depth 14574 ± 823 ppm (catalogue 17240 ppm); BJD 2459937.5741: gap (catalogue 17240 ppm); BJD 2459941.3261: not recovered, depth 14651 ± 915 ppm (catalogue 17240 ppm); BJD 2459945.0780: not recovered, depth 12514 ± 853 ppm (catalogue 17240 ppm); BJD 2459948.8300: recovered, depth 15353 ± 836 ppm (catalogue 17240 ppm); BJD 2459952.5820: gap (catalogue 17240 ppm); BJD 2459956.3340: gap (catalogue 17240 ppm); BJD 2459960.0860: recovered, depth 14131 ± 874 ppm (catalogue 17240 ppm); BJD 2460286.5085: gap (catalogue 17240 ppm); BJD 2460290.2605: not recovered, depth 16221 ± 1390 ppm (catalogue 17240 ppm); BJD 2460294.0125: recovered, depth 18546 ± 1386 ppm (catalogue 17240 ppm); BJD 2460297.7645: not recovered, depth 18949 ± 1356 ppm (catalogue 17240 ppm); BJD 2460301.5164: gap (catalogue 17240 ppm); BJD 2460305.2684: gap (catalogue 17240 ppm); BJD 2460309.0204: recovered, depth 19386 ± 1332 ppm (catalogue 17240 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, ≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459912.1818, ΔT = 165.968 d, 0 of 165 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4080.01: Gaia DR3 557190475293941760 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4080.01: Teff 5206 K, R* 0.90 ± 0.07, M* 0.93 ± 0.09, ρ* 1.26 ± 0.33 ρ☉ (dwarf sequence, M_G 5.14, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4080.01: 5 Gaia neighbour(s) within 52.5", contamination 40.48%; depth 12581 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 557190269135511936, 37.1", ΔG 0.49); a centroid test is needed |
| Pointing and quality census per event | failed | 3 persistent event(s), 0 clean; BJD 2459720.1542 caution: manual exclude (within ±0.25 d); BJD 2459911.8763 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=-9.6, POS_CORR1 z=+9.0, POS_CORR2 z=-12.4, SAP_BKG z=+22.7; BJD 2459912.1818 suspect: POS_CORR2 z=-9.7, SAP_BKG z=+20.2 |
| Moving objects at screen-event epochs | passed | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-4080.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4080.01: TOI-4080 otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | 1 possible published-ephemeris overlap(s) within 1 d (TOI-4080.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4080-01.yaml
python -m cygnus.multi report campaigns/toi-4080-01.yaml
```

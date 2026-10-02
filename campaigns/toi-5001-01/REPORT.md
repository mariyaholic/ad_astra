<!-- cygnus:generated-draft -->
# Known-object test, TOI-5001.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-5001-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4712, calibrate_screen #4684, event_census #4698, fetch_independent #4708, fetch_products #4676, known_signal_recovery #4691, moving_objects #4705, period_aliases #4700, prior_art #4715, residual_screen #4697, stellar_context #4692, variability_guard #4714
- Runner finished (UTC): 2026-09-30T22:12:52Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-5001.01 (BJD 2460069.1193: partial, depth 6844 ± 409 ppm (catalogue 8170 ppm); BJD 2460074.1883: recovered, depth 8294 ± 390 ppm (catalogue 8170 ppm); BJD 2460079.2573: recovered, depth 9376 ± 439 ppm (catalogue 8170 ppm); BJD 2460084.3264: recovered, depth 9061 ± 411 ppm (catalogue 8170 ppm); BJD 2460089.3954: recovered, depth 9185 ± 387 ppm (catalogue 8170 ppm); BJD 2460094.4645: recovered, depth -371 ± 418 ppm (catalogue 8170 ppm); BJD 2461153.8945: recovered, depth 9879 ± 501 ppm (catalogue 8170 ppm); BJD 2461158.9635: not recovered, depth 4079 ± 1136 ppm (catalogue 8170 ppm); BJD 2461164.0326: recovered, depth 6391 ± 453 ppm (catalogue 8170 ppm); BJD 2461169.1016: recovered, depth 8954 ± 446 ppm (catalogue 8170 ppm); BJD 2461174.1706: recovered, depth 8282 ± 449 ppm (catalogue 8170 ppm)).
Outside the catalogued epoch the screen left 124 threshold entries forming **67 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461177.4815 matches the catalogued transit's depth (7832 vs 8294 ppm), 1103.292 d later; 46 of 1103 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-5001.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 95709395 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 243.403564 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -33.496496 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459379.729414 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 5.069043 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8170.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.185 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.1641 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-08-22 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | lightcurve | 65 | False | `d8f1484bdbb2d91f` | True |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | lightcurve | 103 | False | `0c9f6f02c0735de3` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460069.11926 | partial | 126 | 6844 ± 409 | 8170 | 1.69 |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460074.18831 | recovered | 126 | 8294 ± 390 | 8170 | 0.04 |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460079.25735 | recovered | 125 | 9376 ± 439 | 8170 | 0.15 |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460084.32639 | recovered | 126 | 9061 ± 411 | 8170 | 0.23 |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.39543 | recovered | 126 | 9185 ± 387 | 8170 | -0.04 |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460094.46448 | recovered | 125 | -371 ± 418 | 8170 | -0.16 |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461153.89446 | recovered | 125 | 9879 ± 501 | 8170 | 0.68 |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461158.96351 | not_recovered | 20 | 4079 ± 1136 | 8170 | — |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461164.03255 | recovered | 125 | 6391 ± 453 | 8170 | 0.85 |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461169.10159 | recovered | 126 | 8954 ± 446 | 8170 | 0.20 |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461174.17064 | recovered | 125 | 8282 ± 449 | 8170 | 0.17 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461177.48154 | -0.02028 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460086.18605 | -0.01392 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460090.00899 | -0.01833 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460090.00413 | -0.01622 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.48349 | -0.01580 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.85899 | -0.01492 | 3 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.76316 | -0.01458 | 5 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.97844 | -0.01435 | 3 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.98764 | -0.01434 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.42238 | -0.01432 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.92514 | -0.01430 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.99997 | -0.01416 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460090.07080 | -0.01391 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.26959 | -0.01356 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.90413 | -0.01325 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.78469 | -0.01323 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.88069 | -0.01316 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.11517 | -0.01312 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.20848 | -0.01302 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460090.08122 | -0.01283 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.79024 | -0.01270 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.95361 | -0.01247 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.18556 | -0.01242 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.08903 | -0.01229 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.16239 | -0.01226 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460090.03886 | -0.01221 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.25267 | -0.01182 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.24320 | -0.01176 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.84736 | -0.01166 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.36960 | -0.01159 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.13626 | -0.01151 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.30293 | -0.01131 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.95413 | -0.01115 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.18878 | -0.01098 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.88955 | -0.01088 | 3 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.41404 | -0.01078 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.85205 | -0.01077 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.94181 | -0.01072 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.91524 | -0.01066 | 4 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.40154 | -0.01060 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.22029 | -0.01057 | 7 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.87653 | -0.01056 | 2 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.03209 | -0.01055 | 4 | SAP | 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.93486 | -0.01054 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.16751 | -0.01047 | 3 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.93885 | -0.01040 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.55155 | -0.01038 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.20545 | -0.01033 | 6 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460090.06524 | -0.01031 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460094.13470 | -0.01016 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.98330 | -0.01011 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.14156 | -0.01007 | 2 | SAP | 1, 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.22767 | -0.00989 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.99181 | -0.00956 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460094.01665 | -0.00956 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.92149 | -0.00946 | 3 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.29320 | -0.00943 | 4 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460090.05691 | -0.00943 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461177.34195 | -0.00916 | 2 | SAP | 1, 2, 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.67096 | -0.00893 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.74163 | -0.00892 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460089.66802 | -0.00891 | 2 | SAP | 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460083.24851 | -0.00889 | 2 | SAP | 1 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460082.91378 | -0.00889 | 2 | SAP | 2, 3 | no |
| `tess2023124020739-s0065-0000000095709395-0259-s_lc.fits` | 2460093.80831 | -0.00887 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461171.11959 | -0.00845 | 2 | SAP | 3 | no |
| `tess2026111101500-s0103-0000000095709395-0305-s_lc.fits` | 2461170.64735 | -0.00842 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461177.48154 | 7832 | 8294 | 1103.2916 | 46 / 1103 | 1103.29, 551.646, 367.764, 275.823, 220.658, 183.882, 157.613, 137.911, 122.588, 110.329, 100.299, 91.941, 84.8686, 78.8065, 73.5528, 68.9557, 64.8995, 61.294, 58.068, 55.1646 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-5001.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:12:39Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:12:42Z: TOI-5001.01 (TIC 95709395, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:12:46Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T22:12:48Z: UCAC4 283-090178 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460069.1193: partial, depth 6844 ± 409 ppm (catalogue 8170 ppm); BJD 2460074.1883: recovered, depth 8294 ± 390 ppm (catalogue 8170 ppm); BJD 2460079.2573: recovered, depth 9376 ± 439 ppm (catalogue 8170 ppm); BJD 2460084.3264: recovered, depth 9061 ± 411 ppm (catalogue 8170 ppm); BJD 2460089.3954: recovered, depth 9185 ± 387 ppm (catalogue 8170 ppm); BJD 2460094.4645: recovered, depth -371 ± 418 ppm (catalogue 8170 ppm); BJD 2461153.8945: recovered, depth 9879 ± 501 ppm (catalogue 8170 ppm); BJD 2461158.9635: not recovered, depth 4079 ± 1136 ppm (catalogue 8170 ppm); BJD 2461164.0326: recovered, depth 6391 ± 453 ppm (catalogue 8170 ppm); BJD 2461169.1016: recovered, depth 8954 ± 446 ppm (catalogue 8170 ppm); BJD 2461174.1706: recovered, depth 8282 ± 449 ppm (catalogue 8170 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2461177.4815, ΔT = 1103.292 d, 46 of 1103 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1103.29, 551.646, 367.764, 275.823, 220.658, 183.882, 157.613, 137.911, 122.588, 110.329, 100.299, 91.941 … d); duration likelihood under Gaia priors (circular orbits) peaks at 24 d (weight 0.05) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-5001.01: Gaia DR3 6035444660343695616 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-5001.01: Teff 6001 K, R* 1.38 ± 0.11, M* 1.27 ± 0.13, ρ* 0.48 ± 0.12 ρ☉ (dwarf sequence, M_G 3.49, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-5001.01: 94 Gaia neighbour(s) within 52.5", contamination 45.85%; depth 8294 ppm (measured depth of the recovered catalogued transit); 7 could produce it if fully eclipsed (brightest 6035444660343696384, 8.4", ΔG 1.09); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 1 clean; BJD 2461177.4815 suspect: manual exclude (in event), scattered light 2 (in event), POS_CORR2 z=-5.0, SAP_BKG z=+587.7 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-5001.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-5001.01: UCAC4 283-090178 otype * (star_or_other) at 0.0" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-5001-01.yaml
python -m cygnus.multi report campaigns/toi-5001-01.yaml
```

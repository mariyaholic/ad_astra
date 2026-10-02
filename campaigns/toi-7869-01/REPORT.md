<!-- cygnus:generated-draft -->
# Known-object test, TOI-7869.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-7869-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #4509, calibrate_screen #4487, event_census #4495, fetch_independent #4503, fetch_products #4470, known_signal_recovery #4489, moving_objects #4502, period_aliases #4496, prior_art #4513, residual_screen #4491, stellar_context #4490, variability_guard #4510
- Runner finished (UTC): 2026-09-30T21:57:44Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-7869.01 (BJD 2460200.3359: recovered, depth 3767 ± 187 ppm (catalogue 5134 ppm); BJD 2459114.1155: gap (catalogue 5134 ppm); BJD 2459461.7060: partial, depth 3714 ± 168 ppm (catalogue 5134 ppm)).
Outside the catalogued epoch the screen left 100 threshold entries forming **50 distinct event(s)**, **1 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459112.2280 matches the catalogued transit's depth (2537 vs 3767 ppm), 1088.100 d later; 17 of 1088 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-7869.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 188620407 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 350.051137 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -13.049459 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460200.335931 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 43.4488182 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 5134.3277128 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 6.2736347 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.5725 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-07-25 12:04:08 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000188620407-0264-s_lc.fits` | lightcurve | 69 | True | `9dcae7684d75e871` | True |
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | lightcurve | 29 | False | `391c3d123d4df08b` | True |
| `tess2021232031932-s0042-0000000188620407-0213-s_lc.fits` | lightcurve | 42 | False | `2a7f6b79257a1261` | True |
| `tess2023263165758-s0070-0000000188620407-0265-s_lc.fits` | lightcurve | 70 | False | `3ca1e2c2a7008614` | True |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | lightcurve | 96 | False | `4f89107d68eab4ad` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023237165326-s0069-0000000188620407-0264-s_lc.fits` | 2460200.33593 | recovered | 188 | 3767 ± 187 | 5134 | -0.20 |
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | 2459114.11548 | gap | 0 | — | 5134 | — |
| `tess2021232031932-s0042-0000000188620407-0213-s_lc.fits` | 2459461.70602 | partial | 188 | 3714 ± 168 | 5134 | -1.57 |
| `tess2023263165758-s0070-0000000188620407-0265-s_lc.fits` | — | epoch not in this light curve | — | — | 5134 | — |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | — | epoch not in this light curve | — | — | 5134 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023237165326-s0069-0000000188620407-0264-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2021232031932-s0042-0000000188620407-0213-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023263165758-s0070-0000000188620407-0265-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | 2459112.22805 | -0.01214 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.27202 | -0.01530 | 5 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.26160 | -0.01456 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460925.91165 | -0.01390 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.10397 | -0.01380 | 5 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.75328 | -0.01346 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460925.96374 | -0.01226 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.58106 | -0.01224 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460927.14499 | -0.01221 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.19077 | -0.01211 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.92966 | -0.01209 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460927.07416 | -0.01200 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.28313 | -0.01192 | 5 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.01022 | -0.01187 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.23244 | -0.01186 | 4 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460925.58179 | -0.01158 | 3 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460925.81999 | -0.01154 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.05883 | -0.01128 | 4 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.89633 | -0.01120 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.81022 | -0.01109 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.29494 | -0.01093 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.14980 | -0.01092 | 7 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.18452 | -0.01078 | 5 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.80189 | -0.01074 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.77411 | -0.01053 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.02688 | -0.01048 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460920.22551 | -0.01031 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.83661 | -0.01021 | 2 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.07202 | -0.01017 | 3 | SAP | 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460926.13388 | -0.01007 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.97550 | -0.01006 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.81647 | -0.00993 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.59148 | -0.00991 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.01508 | -0.00983 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.94147 | -0.00982 | 3 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.35049 | -0.00957 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.02133 | -0.00947 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.96508 | -0.00937 | 3 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | 2459112.26694 | -0.00931 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.28938 | -0.00927 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.16091 | -0.00926 | 5 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | 2459112.20166 | -0.00918 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.71161 | -0.00918 | 4 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460927.10610 | -0.00916 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.72133 | -0.00905 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460925.55193 | -0.00886 | 2 | SAP | 1, 2, 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460932.84911 | -0.00885 | 2 | SAP | 3 | no |
| `tess2025232030459-s0096-0000000188620407-0293-s_lc.fits` | 2460933.19910 | -0.00841 | 2 | SAP | 3 | no |
| `tess2020238165205-s0029-0000000188620407-0193-s_lc.fits` | 2459112.24749 | -0.00811 | 2 | SAP | 3 | no |
| `tess2023237165326-s0069-0000000188620407-0264-s_lc.fits` | 2460188.41099 | -0.00730 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459112.22805 | 2537 | 3767 | 1088.0996 | 17 / 1088 | 1088.1, 544.05, 272.025, 217.62, 155.443, 136.012, 108.81, 98.9181, 83.7, 77.7214, 68.0062, 64.0059, 57.2684, 54.405, 49.4591, 43.524, 34.0031 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-7869.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T21:57:33Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T21:57:36Z: TOI-7869.01 (TIC 188620407, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T21:57:38Z
- SIMBAD (done, 2026-09-30): 1 match(es) in SIMBAD within 30" as of 2026-09-30T21:57:40Z: UCAC2  27218365 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460200.3359: recovered, depth 3767 ± 187 ppm (catalogue 5134 ppm); BJD 2459114.1155: gap (catalogue 5134 ppm); BJD 2459461.7060: partial, depth 3714 ± 168 ppm (catalogue 5134 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459112.2280, ΔT = 1088.100 d, 17 of 1088 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (1088.1, 544.05, 272.025, 217.62, 155.443, 136.012, 108.81, 98.9181, 83.7, 77.7214, 68.0062, 64.0059 … d); duration likelihood under Gaia priors (circular orbits) peaks at 34 d (weight 0.16) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-7869.01: Gaia DR3 2412246975681462656 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-7869.01: Teff 6044 K, R* 1.24 ± 0.10, M* 1.19 ± 0.12, ρ* 0.62 ± 0.16 ρ☉ (dwarf sequence, M_G 3.86, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-7869.01: 2 Gaia neighbour(s) within 52.5", contamination 0.74%; depth 3767 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 2412247083056104576, 47.2", ΔG 5.43); a centroid test is needed |
| Pointing and quality census per event | failed | 1 persistent event(s), 0 clean; BJD 2459112.2280 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+11.2 |
| Moving objects at screen-event epochs | failed | 1 event epoch(s) queried in SkyBoT (observer C57, r=600"); 1 with a known object bright enough (≥0.1× the depth in flux) within 63" plus its motion over 1 h |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 3 light curve × candidate pair(s); aliases supported: none; excluded: none; 51 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-7869.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-7869.01: UCAC2  27218365 otype * (star_or_other) at 0.3" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-7869-01.yaml
python -m cygnus.multi report campaigns/toi-7869-01.yaml
```

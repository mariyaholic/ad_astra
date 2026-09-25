# Known-object test, TOI-7857.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

The runner flagged a repeat candidate at BJD 2459800.06377 (reported depth 5849 ppm, ΔT = 743.135 d; 34 aliases remain). The flagged epoch is a 2-cadence event adjacent to a broad, ~3.55% 107-cadence depression centered 0.0785 d later; another ~3.3% broad depression occurs in the same sector, and two ~3.6% broad events occur in S82. Those profiles are far deeper than the 0.31% catalogue / 0.39% measured positive-control signal. SIMBAD returned a nearby SB* match. The feature may be an eclipsing-binary/blend event or multiple detections within a broad complex; its transit morphology and source identity are unverified. Preserve the runner's Unverified-lead label; do not claim a planet or period. Highest-value next checks: TOI/ExoFOP and SPOC DV, difference-image centroids/contamination for both epochs, then compare the full event shapes and aliases with a second reduction.


- Campaign spec: `campaigns/toi-7857-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #370, fetch_products #369, known_signal_recovery #371, period_aliases #373, prior_art #374, residual_screen #372
- Runner finished (UTC): 2026-09-25T05:10:18Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-7857.01 (BJD 2460543.2097: recovered, depth 3930 ± 253 ppm (catalogue 3119 ppm)).
Outside the catalogued epoch the screen left 48 threshold entries forming **9 distinct event(s)**, **8 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459800.0638 matches the catalogued transit's depth (5849 vs 3930 ppm), 743.135 d later; 34 of 743 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Reviewer notes (2026-09-25)

Positive control passed in sector 82 (109 usable in-transit cadences; recovered 3930 ± 253 ppm vs catalogue 3119 ppm, ratio 1.26). The reported 90%-completeness floor at k* = 3 is 10000 ppm at all durations, so the screen's null sensitivity remains shallow relative to the 3.62-h catalogue signal.

The runner set one **unverified lead** at BJD 2459800.06377 (34/743 aliases remain). The event itself is only a 2-cadence marker; its ±0.15-d profile contains a much larger broad event beginning about 18 min later. The table's nearby 107-cadence event centered at 2459800.14224 is a ~3.55% SAP+PDCSAP dip, far deeper than the 0.39% measured catalogued control and about 9× the TOI depth. The lead timestamp is ~1.88 h before that deep event's center, so these should not be conflated as one transit without checking the cadence-level shape.

Related persistent features include S55 at 2459817.62125 (~3.3%, ~30 cadences) and S82 at 2460541.92408 / 2460550.65239 (~3.6%, ~100 cadences each); the two-cadence rows at 2459817.54278, 2460541.99769 and 2460550.57531 overlap these complexes. The broad dips are coherent in SAP and PDCSAP, with clean QUALITY and 2-min maximum gaps; inspected centroids show no large shift, but image-level blend tests remain untested. Their depths do not match the ~0.31–0.39% catalogue/control dip. SIMBAD returned TYC 530-1018-1 (SB*) within 30 arcsec; verify association, as an eclipsing binary/blend is a leading alternative. Keep the runner's Unverified-lead evidence and 34 alias count; do not assign a unique period or planetary nature.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-7857.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 408313280 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 316.5329 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | 2.576408 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2460543.209681 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 3118.5413545 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 3.6197227 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 11.6684 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2026-07-25 12:04:08 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2024223182411-s0082-0000000408313280-0278-s_lc.fits` | 82 | True | `0633ea200ffafeaf` | True |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | 55 | False | `653213d9a6f035e6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000408313280-0278-s_lc.fits` | 2460543.20968 | recovered | 109 | 3930 ± 253 | 3119 | -0.25 |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | — | epoch not in this light curve | — | — | 3119 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024223182411-s0082-0000000408313280-0278-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024223182411-s0082-0000000408313280-0278-s_lc.fits` | 2460550.65239 | -0.03637 | 105 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | 2459817.62125 | -0.03606 | 67 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000408313280-0278-s_lc.fits` | 2460541.92408 | -0.03557 | 102 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | 2459800.14224 | -0.03552 | 107 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | 2459817.54278 | -0.03260 | 30 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000408313280-0278-s_lc.fits` | 2460541.99769 | -0.01109 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024223182411-s0082-0000000408313280-0278-s_lc.fits` | 2460550.57531 | -0.00979 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | 2459800.06377 | -0.00906 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022217014003-s0055-0000000408313280-0242-s_lc.fits` | 2459803.34294 | -0.01065 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459800.06377 | 5849 | 3930 | 743.1353 | 34 / 743 | 743.135, 371.568, 247.712, 185.784, 148.627, 123.856, 106.162, 92.8919, 82.5706, 74.3135, 67.5578, 61.9279, 57.1643, 53.0811, 49.5424, 46.446, 43.7138, 41.2853, 39.1124, 37.1568 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-7857.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T05:09:53Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T05:09:55Z: TOI-7857.01 (TIC 408313280, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T05:10:00Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T05:10:01Z: TYC  530-1018-1 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460543.2097: recovered, depth 3930 ± 253 ppm (catalogue 3119 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2459800.0638, ΔT = 743.135 d, 34 of 743 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (743.135, 371.568, 247.712, 185.784, 148.627, 123.856, 106.162, 92.8919, 82.5706, 74.3135, 67.5578, 61.9279 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-7857-01.yaml
python -m cygnus.campaign report campaigns/toi-7857-01.yaml
```

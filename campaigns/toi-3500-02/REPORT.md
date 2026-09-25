# Known-object test, TOI-3500.02

> **Generated draft** (`python -m cygnus.campaign report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-3500-02.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #122, fetch_products #121, known_signal_recovery #123, period_aliases #125, prior_art #126, residual_screen #124
- Runner finished (UTC): 2026-09-25T00:49:04Z

## Escalation (2026-09-25 — repeat candidate found)

`period_aliases` flagged **15 repeat candidates** (persistent PDCSAP+SAP events within 0.5–2× of the
catalogued transit depth). Per `docs/AGENT_RUNBOOK.md` this stops the loop for this target pending a
reviewer. The candidates cluster into three time complexes, not 15 independent events:

1. **Sector 90, BJD 2460757.18–46 (~6.7 h):** the repeat-candidate band. Depth 4575–7401 ppm across 11
   merged sub-events against measured reference 7220 ± 102 ppm. QUALITY = 0 throughout, gaps ≤ 2 min.
   Are the candidates: **conditional periods** (aliases ΔT/n) 700.5, 350.3, 233.5, 175.2 d... only
   aliases whose predicted transits fall on retrieved usable data were excluded; the rest stay allowed.
2. **Sector 101, BJD 2461107.49–79:** deepest −0.0078 (up to 188 melded cadences ≈ 6.3 h). BUT the
   ±1.5 d window carries a **312-minute gap**, and the row-axis centroid shifts −0.0596 px against
   0.0014 px scatter (~43×) — treat as artifact-suspect until difference imaging says otherwise.
3. **Sector 37, BJD 2459322.64–249 (shallow, 2–3 cadences):** centroid baseline too small to judge.

Kernel-blocker: the pipeline's built checks cannot distinguish these — difference-image centroids and
pointing correlation are **not built** (`ANALYSIS_STACK.md`), so no evidence level above
*Unverified lead* is possible; do not raise it.

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-3500.02 (BJD 2460056.7063: recovered, depth 7220 ± 102 ppm (catalogue 8095 ppm)).
Outside the catalogued epoch the screen left 185 threshold entries forming **44 distinct event(s)**, **21 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460757.1825 matches the catalogued transit's depth (4967 vs 7220 ppm), 700.532 d later; 8 of 700 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Reviewer notes (2026-09-25)

**Evidence level: Unverified lead (not raised by reviewer).** Per-complex probes
(`sectorNN/normalized_series.csv`, `sectorNN/screen.json`):

| Complex (representative mid) | Quality | Gaps | Centroid (in vs out) | Verdict |
|---|---|---|---|---|
| S90, BJD 2460757.3 (repeat band) | 0 flags / 168 cad | ≤ 2 min | -0.0100 px col vs 0.0042 scatter; -0.0046 px row vs 0.0023; baseline n=4 (weak) | clean data, unresolved shape origin; candidates stand as *Unverified lead* |
| S101, BJD 2461107.58737 | 0 flags / 168 cad | **312-min gap** in ±1.5 d | +0.0087 col / -0.0596 row vs 0.0022 / 0.0014 scatter (n=11) — ~43× row | artifact-suspect (gap + centroid); not vetted |
| S37, BJD 2459322.69010 | 0 flags / 168 cad | ≤ 2 min | ~-0.003/-0.006 px, scatter 0 (n=6 baseline — unusable) | inconclusive; not vetted |

The sector-90 band is plausible as a transit-shaped feature but a momentum-dump / scattered-light arc is
not excluded — its ~6.7 h width vs the 7.9 h catalogue duration is suggestive, not diagnostic. Surviving
alias periods to test elsewhere: 350.4 d and 233.5 d (predicted transits not covered by retrieved data).

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-3500.02 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 443666343 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 186.816884 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -29.832996 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2460056.706283 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 8094.9889377 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 7.9079384 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 10.8298 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2025-07-22 12:04:25 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 64 | True | `c4389b8d731f77fc` | True |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 37 | False | `a49c554877f7022b` | True |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 90 | False | `5999cb0ff0ae9579` | True |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 101 | False | `dcd7275ffce925f8` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460056.70628 | recovered | 238 | 7220 ± 102 | 8095 | -1.35 |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | — | epoch not in this light curve | — | — | 8095 | — |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | — | epoch not in this light curve | — | — | 8095 | — |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | — | epoch not in this light curve | — | — | 8095 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.36380 | -0.00910 | 18 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.30130 | -0.00875 | 16 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.25616 | -0.00843 | 47 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.33394 | -0.00836 | 29 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.18255 | -0.00806 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.19574 | -0.00776 | 23 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461107.58737 | -0.00775 | 188 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.44158 | -0.00750 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.46172 | -0.00749 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.45686 | -0.00734 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.42700 | -0.00724 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460757.39991 | -0.00722 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461107.51028 | -0.00686 | 11 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461107.78112 | -0.00616 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461107.49639 | -0.00583 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459322.69010 | -0.00559 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459322.69565 | -0.00538 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459324.84562 | -0.00502 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459322.65538 | -0.00462 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459322.64149 | -0.00443 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459322.88871 | -0.00430 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.71616 | -0.00633 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.87310 | -0.00613 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.84949 | -0.00602 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460061.38407 | -0.00587 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.80921 | -0.00585 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460759.76664 | -0.00557 | 2 | SAP | 2, 3 | no |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461119.86494 | -0.00529 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460062.02294 | -0.00526 | 2 | SAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.78630 | -0.00525 | 3 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.81893 | -0.00523 | 4 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.85782 | -0.00523 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.39533 | -0.00520 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460768.16679 | -0.00510 | 2 | SAP | 1 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.86893 | -0.00509 | 2 | SAP | 3 | no |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461107.48944 | -0.00504 | 2 | PDCSAP | 2, 3 | no |
| `tess2023096110322-s0064-0000000443666343-0257-s_lc.fits` | 2460054.55644 | -0.00499 | 2 | SAP | 3 | no |
| `tess2025071122000-s0090-0000000443666343-0287-s_lc.fits` | 2460759.63192 | -0.00491 | 2 | SAP | 3 | no |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459322.74010 | -0.00481 | 2 | PDCSAP | 2 | no |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461102.06416 | -0.00473 | 2 | PDCSAP | 3 | no |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461119.82049 | -0.00469 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461114.52725 | -0.00465 | 2 | SAP | 1, 2, 3 | no |
| `tess2026060005000-s0101-0000000443666343-0303-s_lc.fits` | 2461101.63636 | -0.00463 | 2 | PDCSAP | 3 | no |
| `tess2021091135823-s0037-0000000443666343-0208-s_lc.fits` | 2459323.00954 | -0.00448 | 2 | PDCSAP+SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460757.18255 | 4967 | 7220 | 700.5324 | 8 / 700 | 700.532, 233.511, 140.107, 100.076, 77.8369, 63.6848, 53.8871, 36.8701 |
| 2460757.19574 | 5478 | 7220 | 700.5456 | 8 / 700 | 700.546, 233.515, 140.109, 100.078, 77.8384, 63.686, 53.8881, 36.8708 |
| 2460757.25616 | 7088 | 7220 | 700.6060 | 17 / 700 | 700.606, 350.303, 233.535, 175.151, 140.121, 116.768, 100.087, 87.5758, 77.8451, 70.0606, 63.6915, 58.3838, 53.8928, 50.0433, 36.874, 35.0303, 18.437 |
| 2460757.30130 | 7388 | 7220 | 700.6512 | 17 / 700 | 700.651, 350.326, 233.55, 175.163, 140.13, 116.775, 100.093, 87.5814, 77.8501, 70.0651, 63.6956, 58.3876, 53.8962, 50.0465, 36.8764, 35.0326, 18.4382 |
| 2460757.33394 | 7401 | 7220 | 700.6838 | 17 / 700 | 700.684, 350.342, 233.561, 175.171, 140.137, 116.781, 100.098, 87.5855, 77.8538, 70.0684, 63.6985, 58.3903, 53.8988, 50.0488, 36.8781, 35.0342, 18.439 |
| 2460757.36380 | 7138 | 7220 | 700.7137 | 17 / 700 | 700.714, 350.357, 233.571, 175.178, 140.143, 116.786, 100.102, 87.5892, 77.8571, 70.0714, 63.7012, 58.3928, 53.9011, 50.051, 36.8797, 35.0357, 18.4398 |
| 2460757.39991 | 6908 | 7220 | 700.7498 | 16 / 700 | 700.75, 350.375, 233.583, 175.187, 140.15, 116.792, 100.107, 87.5937, 77.8611, 70.075, 63.7045, 58.3958, 53.9038, 50.0536, 35.0375, 17.5187 |
| 2460757.42700 | 6286 | 7220 | 700.7769 | 8 / 700 | 700.777, 233.592, 140.155, 100.111, 77.8641, 63.707, 53.9059, 46.7185 |
| 2460757.44158 | 5863 | 7220 | 700.7914 | 8 / 700 | 700.791, 233.597, 140.158, 100.113, 77.8657, 63.7083, 53.907, 46.7194 |
| 2460757.45686 | 4777 | 7220 | 700.8067 | 8 / 700 | 700.807, 233.602, 140.161, 100.115, 77.8674, 63.7097, 53.9082, 46.7204 |
| 2460757.46172 | 4575 | 7220 | 700.8116 | 8 / 700 | 700.812, 233.604, 140.162, 100.116, 77.868, 63.7101, 53.9086, 46.7208 |
| 2461107.49639 | 4364 | 7220 | 1050.8462 | 22 / 1050 | 1050.85, 525.423, 350.282, 262.712, 210.169, 175.141, 150.121, 131.356, 116.761, 105.085, 95.5315, 87.5705, 75.0604, 70.0564, 65.6779, 58.3803, 55.3077, 52.5423, 50.0403, 35.0282 |
| 2461107.51028 | 5239 | 7220 | 1050.8601 | 22 / 1050 | 1050.86, 525.43, 350.287, 262.715, 210.172, 175.143, 150.123, 131.357, 116.762, 105.086, 95.5327, 87.5717, 75.0614, 70.0573, 65.6788, 58.3811, 55.3084, 52.543, 50.041, 35.0287 |
| 2461107.58737 | 6798 | 7220 | 1050.9372 | 22 / 1050 | 1050.94, 525.469, 350.312, 262.734, 210.187, 175.156, 150.134, 131.367, 116.771, 105.094, 95.5397, 87.5781, 75.0669, 70.0625, 65.6836, 58.3854, 55.3125, 52.5469, 50.0446, 35.0312 |
| 2461107.78112 | 4226 | 7220 | 1051.1310 | 22 / 1051 | 1051.13, 525.566, 350.377, 262.783, 210.226, 175.189, 150.162, 131.391, 116.792, 105.113, 95.5574, 87.5942, 75.0808, 70.0754, 65.6957, 58.3962, 55.3227, 52.5565, 50.0539, 35.0377 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-3500.02**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T00:48:51Z
- TESS_TOI (done, 2026-09-25): 2 match(es) in TESS_TOI within 30" as of 2026-09-25T00:48:57Z: TOI-3500.01 (TIC 443666343, disposition PC); TOI-3500.02 (TIC 443666343, disposition PC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T00:49:01Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T00:49:02Z: UCAC2  19403154 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460056.7063: recovered, depth 7220 ± 102 ppm (catalogue 8095 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 50%, 0%, 40% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 15 repeat-candidate event(s); first at BJD 2460757.1825, ΔT = 700.532 d, 8 of 700 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (700.532, 233.511, 140.107, 100.076, 77.8369, 63.6848, 53.8871, 36.8701 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-3500-02.yaml
python -m cygnus.campaign report campaigns/toi-3500-02.yaml
```

<!-- cygnus:generated-draft -->
# Known-object test, TOI-768.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-768-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #850, calibrate_screen #817, event_census #821, fetch_products #814, known_signal_recovery #818, moving_objects #823, period_aliases #822, prior_art #852, residual_screen #820, stellar_context #819, variability_guard #851
- Runner finished (UTC): 2026-09-26T10:21:08Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-768.01 (BJD 2459316.2917: recovered, depth 21097 ± 300 ppm (catalogue 25630 ppm)).
Outside the catalogued epoch the screen left 96 threshold entries forming **16 distinct event(s)**, **11 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459327.7342 matches the catalogued transit's depth (11284 vs 21097 ppm), 11.485 d later; 0 of 11 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-768.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 229811538 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 198.635626 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -24.14419 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459316.29169 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 25630.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.881 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.2864 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-01-24 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021091135823-s0037-0000000229811538-0208-s_lc.fits` | lightcurve | 37 | True | `1a6b6a44e0afcbb6` | True |
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | lightcurve | 10 | False | `2b4a7153873be9bd` | True |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | lightcurve | 64 | False | `453eb9f7abbbd8c2` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021091135823-s0037-0000000229811538-0208-s_lc.fits` | 2459316.29169 | recovered | 146 | 21097 ± 300 | 25630 | -1.03 |
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | — | epoch not in this light curve | — | — | 25630 | — |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | — | epoch not in this light curve | — | — | 25630 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021091135823-s0037-0000000229811538-0208-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | 2458578.40176 | -0.02339 | 120 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | 2458589.97411 | -0.02306 | 123 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460042.65400 | -0.02253 | 120 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000229811538-0208-s_lc.fits` | 2459327.82588 | -0.02227 | 123 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460054.17907 | -0.02206 | 122 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460065.70601 | -0.02182 | 126 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460042.56719 | -0.02000 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460042.55816 | -0.01519 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460054.08880 | -0.01269 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021091135823-s0037-0000000229811538-0208-s_lc.fits` | 2459327.73421 | -0.01203 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460042.55122 | -0.01188 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | 2458578.49482 | -0.01636 | 2 | SAP | 1, 2, 3 | no |
| `tess2019085135100-s0010-0000000229811538-0140-s_lc.fits` | 2458579.94763 | -0.01313 | 2 | SAP | 3 | no |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460054.74435 | -0.01181 | 2 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460065.61365 | -0.01037 | 4 | SAP | 1, 2, 3 | no |
| `tess2023096110322-s0064-0000000229811538-0257-s_lc.fits` | 2460054.43741 | -0.01029 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459327.73421 | 11284 | 21097 | 11.4854 | 0 / 11 |  |
| 2459327.82588 | 20508 | 21097 | 11.5771 | 0 / 11 |  |
| 2458578.40176 | 19157 | 21097 | 737.8470 | 43 / 737 | 737.847, 368.923, 245.949, 184.462, 147.569, 122.975, 105.407, 92.2309, 81.983, 73.7847, 67.077, 61.4873, 56.7575, 52.7034, 49.1898, 46.1154, 43.4028, 40.9915, 38.8341, 36.8924 |
| 2458589.97411 | 19993 | 21097 | 726.2747 | 0 / 726 |  |
| 2460042.56719 | 14897 | 21097 | 726.3184 | 31 / 726 | 726.318, 363.159, 242.106, 181.58, 145.264, 121.053, 103.76, 90.7898, 80.702, 72.6318, 66.0289, 60.5265, 55.8706, 51.8799, 48.4212, 45.3949, 42.7246, 40.351, 38.2273, 36.3159 |
| 2460042.65400 | 20335 | 21097 | 726.4052 | 0 / 726 |  |
| 2460054.17907 | 17498 | 21097 | 737.9303 | 43 / 737 | 737.93, 368.965, 245.977, 184.483, 147.586, 122.988, 105.419, 92.2413, 81.9923, 73.793, 67.0846, 61.4942, 56.7639, 52.7093, 49.1954, 46.1206, 43.4077, 40.9961, 38.8384, 36.8965 |
| 2460065.70601 | 19669 | 21097 | 749.4572 | 27 / 749 | 749.457, 374.729, 249.819, 187.364, 149.891, 124.909, 107.065, 93.6822, 83.273, 74.9457, 68.1325, 62.4548, 57.6506, 53.5327, 49.9638, 46.8411, 44.0857, 41.6365, 39.4451, 37.4729 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-768.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:21:05Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:21:06Z: TOI-768.01 (TIC 229811538, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:21:07Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:21:08Z: TOI-768.01 (err); TOI-768 (SB*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459316.2917: recovered, depth 21097 ± 300 ppm (catalogue 25630 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 8 repeat-candidate event(s); first at BJD 2459327.7342, ΔT = 11.485 d, 0 of 11 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-768.01: Gaia DR3 6194034953338162816 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-768.01: Teff 5688 K, R* 1.10 ± 0.09, M* 1.06 ± 0.11, ρ* 0.79 ± 0.21 ρ☉ (dwarf sequence, M_G 4.32, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-768.01: 7 Gaia neighbour(s) within 52.5", contamination 1.19%; depth 21097 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 11 persistent event(s), 8 clean; BJD 2458589.9741 caution: manual exclude (within ±0.25 d); BJD 2460054.1791 suspect: MOM_CENTR1 z=-7.9, POS_CORR1 z=-9.7, SAP_BKG z=+6.2; BJD 2460065.7060 suspect: MOM_CENTR1 z=-14.6, MOM_CENTR2 z=-14.2, POS_CORR1 z=-17.8, POS_CORR2 z=-20.5, SAP_BKG z=+56.8 |
| Moving objects at screen-event epochs | inconclusive | 11 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 3 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-768.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-768.01: TOI-768 otype SB* (multiple) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-768-01.yaml
python -m cygnus.multi report campaigns/toi-768-01.yaml
```

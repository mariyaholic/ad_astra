<!-- cygnus:generated-draft -->
# Known-object test, TOI-224.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-224-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #116, calibrate_screen #30, event_census #51, fetch_products #3, known_signal_recovery #35, moving_objects #99, period_aliases #52, prior_art #122, residual_screen #46, stellar_context #37, variability_guard #117
- Runner finished (UTC): 2026-09-26T09:54:46Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-224.01 (BJD 2458365.8437: recovered, depth 55291 ± 579 ppm (catalogue 101205 ppm)).
Outside the catalogued epoch the screen left 24 threshold entries forming **4 distinct event(s)**, **4 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459092.1803 matches the catalogued transit's depth (59629 vs 55291 ppm), 726.336 d later; 18 of 726 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-224.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 70797900 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 1.977969 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -29.979603 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2458365.843684 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 101204.8459939 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 1.9189212 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.1427 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-02-02 16:00:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2018234235059-s0002-0000000070797900-0121-s_lc.fits` | lightcurve | 2 | True | `d447b0465590144e` | True |
| `tess2020238165205-s0029-0000000070797900-0193-s_lc.fits` | lightcurve | 29 | False | `978659fd91ba33ec` | True |
| `tess2023237165326-s0069-0000000070797900-0264-s_lc.fits` | lightcurve | 69 | False | `083ee384b35db62b` | True |
| `tess2025232030459-s0096-0000000070797900-0293-s_lc.fits` | lightcurve | 96 | False | `a6185f305da5a4da` | True |
| `tess2026192185000-s0106-0000000070797900-0308-s_lc.fits` | lightcurve | 106 | False | `330f5f327a60ccf4` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2018234235059-s0002-0000000070797900-0121-s_lc.fits` | 2458365.84368 | recovered | 57 | 55291 ± 579 | 101205 | 0.00 |
| `tess2020238165205-s0029-0000000070797900-0193-s_lc.fits` | — | epoch not in this light curve | — | — | 101205 | — |
| `tess2023237165326-s0069-0000000070797900-0264-s_lc.fits` | — | epoch not in this light curve | — | — | 101205 | — |
| `tess2025232030459-s0096-0000000070797900-0293-s_lc.fits` | — | epoch not in this light curve | — | — | 101205 | — |
| `tess2026192185000-s0106-0000000070797900-0308-s_lc.fits` | — | epoch not in this light curve | — | — | 101205 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2018234235059-s0002-0000000070797900-0121-s_lc.fits` | 10 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2020238165205-s0029-0000000070797900-0193-s_lc.fits` | 8 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2023237165326-s0069-0000000070797900-0264-s_lc.fits` | — | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: —, 2h: —, 4h: —, 8h: — |
| `tess2025232030459-s0096-0000000070797900-0293-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026192185000-s0106-0000000070797900-0308-s_lc.fits` | — | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: —, 2h: —, 4h: —, 8h: — |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020238165205-s0029-0000000070797900-0193-s_lc.fits` | 2459092.18026 | -0.08589 | 45 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000070797900-0308-s_lc.fits` | 2461239.58662 | -0.07714 | 47 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025232030459-s0096-0000000070797900-0293-s_lc.fits` | 2460923.79502 | -0.07430 | 48 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023237165326-s0069-0000000070797900-0264-s_lc.fits` | 2460197.47152 | -0.07119 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459092.18026 | 59629 | 55291 | 726.3364 | 18 / 726 | 726.336, 363.168, 242.112, 181.584, 145.267, 121.056, 103.762, 90.7921, 80.704, 72.6336, 66.0306, 60.528, 55.872, 51.8812, 45.396, 40.352, 36.3168, 31.5798 |
| 2460197.47152 | 62055 | 55291 | 1831.6277 | 21 / 1831 | 1831.63, 915.814, 610.543, 457.907, 305.271, 228.953, 203.514, 166.512, 152.636, 140.894, 114.477, 107.743, 83.2558, 76.3178, 70.4472, 67.8381, 63.1596, 59.0848, 53.8714, 46.9648 |
| 2460923.79502 | 55314 | 55291 | 2557.9512 | 35 / 2557 | 2557.95, 1278.98, 852.65, 639.488, 511.59, 426.325, 284.217, 255.795, 232.541, 213.163, 196.766, 170.53, 150.468, 142.108, 134.629, 127.898, 116.27, 102.318, 98.3827, 94.7389 |
| 2461239.58662 | 51064 | 55291 | 2873.7428 | 41 / 2873 | 2873.74, 1436.87, 957.914, 718.436, 574.749, 478.957, 410.535, 359.218, 287.374, 261.249, 239.479, 221.057, 205.267, 191.583, 179.609, 169.044, 151.25, 143.687, 136.845, 130.625 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-224.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:54:43Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:54:44Z: TOI-224.01 (TIC 70797900, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:54:45Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T09:54:45Z: TOI-224.01 (err); G 267-34 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 5 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2458365.8437: recovered, depth 55291 ± 579 ppm (catalogue 101205 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | inconclusive | screen run at each light curve's own k* (10, 8, none, 4.5, none; ≤ 0 persistent null events outside the veto); 2 light curve(s) reached no k* on the grid and used the declared k, uncalibrated |
| Synthetic signal injection–recovery | inconclusive | completeness for 2000 ppm, 4.0 h boxes at the declared threshold: 0%, 0%, 0%, 0%, 0% per light curve (pass mark 90%) |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 4 repeat-candidate event(s); first at BJD 2459092.1803, ΔT = 726.336 d, 18 of 726 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (726.336, 363.168, 242.112, 181.584, 145.267, 121.056, 103.762, 90.7921, 80.704, 72.6336, 66.0306, 60.528 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 5 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-224.01: Gaia DR3 2320703325475764864 at 0.00" (propagated 2016.0 → J2015.5; 0.10" unpropagated, proper-motion shift 0.10") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-224.01: dwarf priors not applied — RUWE 9.183665 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-224.01: 2 Gaia neighbour(s) within 52.5", contamination 0.86%; depth 55291 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 4 persistent event(s), 1 clean; BJD 2459092.1803 caution: manual exclude (within ±0.25 d); BJD 2460923.7950 suspect: argabrightening (within ±0.25 d), scattered light 2 (within ±0.25 d), MOM_CENTR2 z=-17.5, POS_CORR1 z=-7.3, POS_CORR2 z=-16.9, SAP_BKG z=+51.3; BJD 2461239.5866 caution: argabrightening (within ±0.25 d), coarse point (within ±0.25 d), manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 4 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-224.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-224.01: G 267-34 otype PM* (star_or_other) at 3.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-224-01.yaml
python -m cygnus.multi report campaigns/toi-224-01.yaml
```

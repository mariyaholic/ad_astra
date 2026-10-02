<!-- cygnus:generated-draft -->
# Known-object test, TOI-2961.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2961-01.yaml`
- Parent queue: `tess-periodic-02`
- Ledger runs: alias_cross_instrument #5064, calibrate_screen #5051, event_census #5058, fetch_independent #5062, fetch_products #5049, known_signal_recovery #5053, moving_objects #5060, period_aliases #5059, prior_art #5066, residual_screen #5055, stellar_context #5054, variability_guard #5065
- Runner finished (UTC): 2026-09-30T22:56:43Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2961.01 (BJD 2460015.2536: recovered, depth 7568 ± 511 ppm (catalogue 10220 ppm); BJD 2460019.8795: recovered, depth 10175 ± 485 ppm (catalogue 10220 ppm); BJD 2460024.5054: recovered, depth 7992 ± 493 ppm (catalogue 10220 ppm); BJD 2460029.1313: recovered, depth 10257 ± 495 ppm (catalogue 10220 ppm); BJD 2460033.7572: recovered, depth 10581 ± 519 ppm (catalogue 10220 ppm); BJD 2460038.3831: recovered, depth 10601 ± 526 ppm (catalogue 10220 ppm); BJD 2460750.7739: recovered, depth 10280 ± 526 ppm (catalogue 10220 ppm); BJD 2460755.3998: recovered, depth 10865 ± 521 ppm (catalogue 10220 ppm); BJD 2460760.0257: recovered, depth 8747 ± 578 ppm (catalogue 10220 ppm); BJD 2460764.6516: recovered, depth 9375 ± 540 ppm (catalogue 10220 ppm); BJD 2460769.2775: recovered, depth 9637 ± 515 ppm (catalogue 10220 ppm); BJD 2460773.9034: partial, depth 9586 ± 651 ppm (catalogue 10220 ppm); BJD 2461046.8323: recovered, depth 8310 ± 497 ppm (catalogue 10220 ppm); BJD 2461051.4583: partial, depth 10052 ± 500 ppm (catalogue 10220 ppm); BJD 2461056.0842: gap (catalogue 10220 ppm); BJD 2461060.7101: gap (catalogue 10220 ppm); BJD 2461065.3360: recovered, depth 10409 ± 487 ppm (catalogue 10220 ppm); BJD 2461069.9619: recovered, depth 10898 ± 497 ppm (catalogue 10220 ppm)).
Outside the catalogued epoch the screen left 24 threshold entries forming **9 distinct event(s)**, **2 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460040.8408 matches the catalogued transit's depth (6646 vs 7568 ppm), 25.615 d later; 0 of 25 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2961.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 446684383 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 156.12964 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -49.765876 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459325.992412 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| period_days | 4.6259138 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 10220.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.91 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 12.2985 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-02-03 12:03:45 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | lightcurve | 63 | False | `4567a21a891aeac9` | True |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | lightcurve | 90 | False | `f0d17d0882c359a2` | True |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | lightcurve | 99 | False | `ae60791d6f9e0ed1` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460015.25357 | recovered | 87 | 7568 ± 511 | 10220 | -0.68 |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460019.87948 | recovered | 88 | 10175 ± 485 | 10220 | -0.28 |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460024.50540 | recovered | 87 | 7992 ± 493 | 10220 | -0.55 |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460029.13131 | recovered | 87 | 10257 ± 495 | 10220 | 0.04 |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460033.75722 | recovered | 82 | 10581 ± 519 | 10220 | -0.58 |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460038.38314 | recovered | 87 | 10601 ± 526 | 10220 | -0.67 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 2460750.77386 | recovered | 87 | 10280 ± 526 | 10220 | -0.21 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 2460755.39978 | recovered | 88 | 10865 ± 521 | 10220 | -0.64 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 2460760.02569 | recovered | 87 | 8747 ± 578 | 10220 | -0.16 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 2460764.65160 | recovered | 87 | 9375 ± 540 | 10220 | 0.70 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 2460769.27752 | recovered | 88 | 9637 ± 515 | 10220 | 0.11 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 2460773.90343 | partial | 87 | 9586 ± 651 | 10220 | 1.08 |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 2461046.83235 | recovered | 87 | 8310 ± 497 | 10220 | 0.04 |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 2461051.45826 | partial | 88 | 10052 ± 500 | 10220 | 0.10 |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 2461056.08417 | gap | 0 | — | 10220 | — |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 2461060.71009 | gap | 0 | — | 10220 | — |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 2461065.33600 | recovered | 87 | 10409 ± 487 | 10220 | -0.32 |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 2461069.96191 | recovered | 88 | 10898 ± 497 | 10220 | 0.05 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025071122000-s0090-0000000446684383-0287-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 3 | False | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460040.84075 | -0.01645 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460040.88242 | -0.01586 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026005125623-s0099-0000000446684383-0300-s_lc.fits` | 2461072.72310 | -0.01986 | 2 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460040.50256 | -0.01603 | 3 | SAP | 1, 2, 3 | no |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460040.49770 | -0.01470 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460040.80742 | -0.01392 | 2 | PDCSAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460040.71853 | -0.01325 | 2 | SAP | 3 | no |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460039.86993 | -0.01244 | 2 | SAP | 2, 3 | no |
| `tess2023069172124-s0063-0000000446684383-0255-s_lc.fits` | 2460040.19215 | -0.01153 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460040.84075 | 6646 | 7568 | 25.6154 | 0 / 25 |  |
| 2460040.88242 | 6991 | 7568 | 25.6570 | 0 / 25 |  |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2961.01**

- NASA_Exoplanet_Archive (done, 2026-09-30): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-30T22:56:26Z
- TESS_TOI (done, 2026-09-30): 1 match(es) in TESS_TOI within 30" as of 2026-09-30T22:56:30Z: TOI-2961.01 (TIC 446684383, disposition PC)
- VSX (done, 2026-09-30): no match in VSX within 30" as of 2026-09-30T22:56:34Z
- SIMBAD (done, 2026-09-30): 2 match(es) in SIMBAD within 30" as of 2026-09-30T22:56:38Z: TOI-2961 (*); TOI-2961.01 (Pl?)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460015.2536: recovered, depth 7568 ± 511 ppm (catalogue 10220 ppm); BJD 2460019.8795: recovered, depth 10175 ± 485 ppm (catalogue 10220 ppm); BJD 2460024.5054: recovered, depth 7992 ± 493 ppm (catalogue 10220 ppm); BJD 2460029.1313: recovered, depth 10257 ± 495 ppm (catalogue 10220 ppm); BJD 2460033.7572: recovered, depth 10581 ± 519 ppm (catalogue 10220 ppm); BJD 2460038.3831: recovered, depth 10601 ± 526 ppm (catalogue 10220 ppm); BJD 2460750.7739: recovered, depth 10280 ± 526 ppm (catalogue 10220 ppm); BJD 2460755.3998: recovered, depth 10865 ± 521 ppm (catalogue 10220 ppm); BJD 2460760.0257: recovered, depth 8747 ± 578 ppm (catalogue 10220 ppm); BJD 2460764.6516: recovered, depth 9375 ± 540 ppm (catalogue 10220 ppm); BJD 2460769.2775: recovered, depth 9637 ± 515 ppm (catalogue 10220 ppm); BJD 2460773.9034: partial, depth 9586 ± 651 ppm (catalogue 10220 ppm); BJD 2461046.8323: recovered, depth 8310 ± 497 ppm (catalogue 10220 ppm); BJD 2461051.4583: partial, depth 10052 ± 500 ppm (catalogue 10220 ppm); BJD 2461056.0842: gap (catalogue 10220 ppm); BJD 2461060.7101: gap (catalogue 10220 ppm); BJD 2461065.3360: recovered, depth 10409 ± 487 ppm (catalogue 10220 ppm); BJD 2461069.9619: recovered, depth 10898 ± 497 ppm (catalogue 10220 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 2 repeat-candidate event(s); first at BJD 2460040.8408, ΔT = 25.615 d, 0 of 25 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2961.01: Gaia DR3 5358915190124718464 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2961.01: Teff 6677 K, R* 1.49 ± 0.12, M* 1.35 ± 0.13, ρ* 0.40 ± 0.11 ρ☉ (dwarf sequence, M_G 3.20, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2961.01: 73 Gaia neighbour(s) within 52.5", contamination 32.37%; depth 7568 ppm (measured depth of the recovered catalogued transit); 11 could produce it if fully eclipsed (brightest 5358915155764975488, 42.6", ΔG 2.81); a centroid test is needed |
| Pointing and quality census per event | failed | 2 persistent event(s), 0 clean; BJD 2460040.8408 suspect: manual exclude (within ±0.25 d), MOM_CENTR2 z=-5.1, SAP_BKG z=+8.2; BJD 2460040.8824 suspect: manual exclude (within ±0.25 d), SAP_BKG z=+7.0 |
| Moving objects at screen-event epochs | passed | 2 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-2961.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2961.01: TOI-2961 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2961-01.yaml
python -m cygnus.multi report campaigns/toi-2961-01.yaml
```

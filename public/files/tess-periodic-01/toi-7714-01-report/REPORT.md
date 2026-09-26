<!-- [private Drive store] -->
# Known-object test, TOI-7714.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-7714-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #452, calibrate_screen #430, event_census #436, fetch_products #429, known_signal_recovery #431, moving_objects #449, period_aliases #437, prior_art #454, residual_screen #435, stellar_context #432, variability_guard #453
- Runner finished (UTC): 2026-09-26T10:08:29Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-7714.01 (BJD 2461002.6835: recovered, depth 17365 ± 168 ppm (catalogue 20632 ppm)).
Outside the catalogued epoch the screen left 82 threshold entries forming **33 distinct event(s)**, **6 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461027.4163 matches the catalogued transit's depth (17676 vs 17365 ppm), 24.733 d later; 0 of 24 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-7714.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 423785115 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 70.919714 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -26.650255 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2461002.68347 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 20632.2954454 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.791716 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.2457 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-04-10 12:04:53 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | lightcurve | 98 | True | `b5c6e5b9802782ad` | True |
| `tess2020324010417-s0032-0000000423785115-0200-s_lc.fits` | lightcurve | 32 | False | `7757e393834fd851` | True |
| `tess2026192185000-s0106-0000000423785115-0308-s_lc.fits` | lightcurve | 106 | False | `197c6589a60d4a66` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461002.68347 | recovered | 144 | 17365 ± 168 | 20632 | -0.01 |
| `tess2020324010417-s0032-0000000423785115-0200-s_lc.fits` | — | epoch not in this light curve | — | — | 20632 | — |
| `tess2026192185000-s0106-0000000423785115-0308-s_lc.fits` | — | epoch not in this light curve | — | — | 20632 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2 | True | 1h: 10000, 2h: 20000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2020324010417-s0032-0000000423785115-0200-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026192185000-s0106-0000000423785115-0308-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 20000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2020324010417-s0032-0000000423785115-0200-s_lc.fits` | 2459196.97259 | -0.01930 | 65 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461027.41630 | -0.01868 | 118 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000423785115-0200-s_lc.fits` | 2459197.05106 | -0.01836 | 46 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020324010417-s0032-0000000423785115-0200-s_lc.fits` | 2459196.92467 | -0.00870 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461027.50241 | -0.00776 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026192185000-s0106-0000000423785115-0308-s_lc.fits` | 2461250.55527 | -0.00675 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.60903 | -0.00837 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461024.29553 | -0.00802 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461038.03401 | -0.00790 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.56250 | -0.00752 | 3 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.48403 | -0.00725 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461024.23859 | -0.00718 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.46945 | -0.00695 | 3 | SAP | 1, 2 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461038.03957 | -0.00688 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461038.58260 | -0.00685 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461024.18859 | -0.00682 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.86735 | -0.00656 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461024.21290 | -0.00655 | 3 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461024.19415 | -0.00651 | 2 | SAP | 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.81110 | -0.00649 | 3 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461023.80526 | -0.00643 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.89304 | -0.00643 | 3 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.75277 | -0.00627 | 3 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2460999.36241 | -0.00613 | 2 | SAP | 1 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461038.18192 | -0.00607 | 3 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461045.23373 | -0.00587 | 2 | SAP | 1 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.96040 | -0.00586 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461024.28998 | -0.00578 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461009.46796 | -0.00571 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461038.42983 | -0.00569 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461038.37844 | -0.00559 | 2 | SAP | 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461037.42987 | -0.00558 | 2 | SAP | 1, 2, 3 | no |
| `tess2025312202959-s0098-0000000423785115-0298-s_lc.fits` | 2461038.45900 | -0.00530 | 2 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461027.41630 | 17676 | 17365 | 24.7330 | 0 / 24 |  |
| 2459196.97259 | 17933 | 17365 | 1805.7107 | 39 / 1805 | 1805.71, 902.855, 601.904, 451.428, 361.142, 300.952, 257.959, 225.714, 200.635, 180.571, 164.155, 150.476, 138.901, 128.979, 112.857, 106.218, 100.317, 95.0374, 90.2855, 85.9862 |
| 2459197.05106 | 17801 | 17365 | 1805.6322 | 39 / 1805 | 1805.63, 902.816, 601.877, 451.408, 361.126, 300.939, 257.947, 225.704, 200.626, 180.563, 164.148, 150.469, 138.895, 128.974, 112.852, 106.214, 100.313, 95.0333, 90.2816, 85.9825 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-7714.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:08:25Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:08:27Z: TOI-7714.01 (TIC 423785115, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:08:28Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:08:28Z: TYC 6468-912-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2461002.6835: recovered, depth 17365 ± 168 ppm (catalogue 20632 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 30% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 3 repeat-candidate event(s); first at BJD 2461027.4163, ΔT = 24.733 d, 0 of 24 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-7714.01: Gaia DR3 4893207488161006464 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-7714.01: dwarf priors not applied — parallax/error 4.4 < 5; RUWE 42.489223 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-7714.01: 6 Gaia neighbour(s) within 52.5", contamination 2.57%; depth 17365 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 6 persistent event(s), 5 clean; BJD 2461250.5553 suspect: manual exclude (within ±0.25 d), scattered light 2 (within ±0.25 d), SAP_BKG z=+12.7 |
| Moving objects at screen-event epochs | inconclusive | 6 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-7714.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-7714.01: TYC 6468-912-1 otype * (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-7714-01.yaml
python -m cygnus.multi report campaigns/toi-7714-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** No new signal.

Source: `campaigns/toi-7714-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.

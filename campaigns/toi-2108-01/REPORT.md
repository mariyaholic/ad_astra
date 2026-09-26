<!-- cygnus:generated-draft -->
# Known-object test, TOI-2108.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-2108-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #503, calibrate_screen #442, event_census #447, fetch_products #441, known_signal_recovery #443, moving_objects #451, period_aliases #448, prior_art #505, residual_screen #445, stellar_context #444, variability_guard #504
- Runner finished (UTC): 2026-09-26T10:09:13Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-2108.01 (BJD 2459698.9717: recovered, depth 11200 ± 149 ppm (catalogue 16385 ppm)).
Outside the catalogued epoch the screen left 264 threshold entries forming **63 distinct event(s)**, **24 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459719.3550 matches the catalogued transit's depth (9305 vs 11200 ppm), 20.383 d later; 0 of 20 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-2108.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 347538174 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 247.481601 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 21.495162 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459698.971706 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 16385.4766601 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.9266235 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 10.223 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-18 16:00:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022112184951-s0051-0000000347538174-0223-s_lc.fits` | lightcurve | 51 | True | `3b6cb550fcbe8472` | True |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | lightcurve | 52 | False | `27860b260e40907f` | True |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | lightcurve | 78 | False | `4cc37cbaa9acefc1` | True |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | lightcurve | 79 | False | `ff4d91af5edbda60` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022112184951-s0051-0000000347538174-0223-s_lc.fits` | 2459698.97171 | recovered | 88 | 11200 ± 149 | 16385 | 0.02 |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | — | epoch not in this light curve | — | — | 16385 | — |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | — | epoch not in this light curve | — | — | 16385 | — |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | — | epoch not in this light curve | — | — | 16385 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022112184951-s0051-0000000347538174-0223-s_lc.fits` | 3 | False | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2 | True | 1h: —, 2h: —, 4h: —, 8h: — | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 2 | True | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 5000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459739.78533 | -0.01828 | 26 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459720.55982 | -0.01803 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459737.42496 | -0.01802 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459720.33343 | -0.01731 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459728.17508 | -0.01716 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459726.16398 | -0.01715 | 31 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459732.99031 | -0.01691 | 33 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459719.39246 | -0.01645 | 28 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459739.76519 | -0.01631 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459720.40010 | -0.01595 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459726.21537 | -0.01506 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459728.11675 | -0.01467 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 2460440.46105 | -0.01459 | 73 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459719.35496 | -0.01451 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459720.55427 | -0.01421 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459727.13342 | -0.01400 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459738.30480 | -0.01350 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459720.20010 | -0.01337 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | 2460454.06670 | -0.01289 | 63 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459739.81241 | -0.01279 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | 2460467.67143 | -0.01241 | 56 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459726.93064 | -0.01230 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459719.40427 | -0.01227 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 2460440.40689 | -0.00487 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459729.12925 | -0.02161 | 2 | SAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459742.78875 | -0.01584 | 2 | SAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459742.31514 | -0.01546 | 2 | SAP | 1 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459742.00126 | -0.01505 | 4 | SAP | 1 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459720.18899 | -0.01491 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459739.84436 | -0.01477 | 2 | SAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459718.66886 | -0.01459 | 11 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459718.65566 | -0.01368 | 4 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459738.46800 | -0.01348 | 2 | SAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459727.08620 | -0.01332 | 2 | SAP | 1 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459732.95142 | -0.01322 | 2 | SAP | 1 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459731.51117 | -0.01311 | 6 | SAP | 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459739.81797 | -0.01294 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459731.46673 | -0.01290 | 22 | SAP | 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459731.50423 | -0.01280 | 2 | SAP | 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459727.57648 | -0.01255 | 2 | SAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459729.92369 | -0.01254 | 2 | SAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459731.49173 | -0.01244 | 5 | SAP | 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459728.35008 | -0.01240 | 2 | SAP | 1, 2 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459731.52506 | -0.01240 | 2 | SAP | 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459718.64733 | -0.01239 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459718.72927 | -0.01212 | 2 | PDCSAP | 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459726.88481 | -0.01206 | 2 | SAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459726.15287 | -0.01201 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459731.56395 | -0.01186 | 4 | SAP | 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459719.41469 | -0.01185 | 5 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459718.70011 | -0.01184 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459728.29731 | -0.01183 | 2 | SAP | 1 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459737.52079 | -0.01167 | 2 | SAP | 1 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459719.40844 | -0.01159 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459718.70636 | -0.01094 | 3 | PDCSAP | 2, 3 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459733.01253 | -0.01045 | 2 | PDCSAP | 1 | no |
| `tess2022138205153-s0052-0000000347538174-0224-s_lc.fits` | 2459733.01739 | -0.01000 | 3 | PDCSAP | 1 | no |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | 2460474.46501 | -0.00801 | 13 | SAP | 2, 3 | no |
| `tess2024142205832-s0079-0000000347538174-0274-s_lc.fits` | 2460474.45251 | -0.00733 | 3 | SAP | 3 | no |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 2460452.11532 | -0.00450 | 3 | PDCSAP | 1, 2, 3 | no |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 2460452.23684 | -0.00409 | 2 | PDCSAP | 3 | no |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 2460451.94240 | -0.00395 | 2 | PDCSAP | 2, 3 | no |
| `tess2024114025118-s0078-0000000347538174-0273-s_lc.fits` | 2460452.27157 | -0.00362 | 2 | PDCSAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459719.35496 | 9305 | 11200 | 20.3826 | 0 / 20 |  |
| 2459719.39246 | 9910 | 11200 | 20.4201 | 0 / 20 |  |
| 2459719.40427 | 9440 | 11200 | 20.4319 | 0 / 20 |  |
| 2459726.16398 | 9281 | 11200 | 27.1916 | 1 / 27 | 27.1916 |
| 2459726.21537 | 8042 | 11200 | 27.2430 | 0 / 27 |  |
| 2459732.99031 | 8576 | 11200 | 34.0180 | 1 / 34 | 34.018 |
| 2459739.76519 | 9484 | 11200 | 40.7928 | 0 / 40 |  |
| 2459739.78533 | 9673 | 11200 | 40.8130 | 0 / 40 |  |
| 2459739.81241 | 9294 | 11200 | 40.8401 | 2 / 40 | 40.8401, 13.6134 |
| 2460440.46105 | 12772 | 11200 | 741.4887 | 18 / 741 | 741.489, 370.744, 247.163, 185.372, 148.298, 123.581, 105.927, 92.6861, 82.3876, 74.1489, 67.4081, 61.7907, 57.0376, 52.9635, 49.4326, 46.343, 35.309, 22.4694 |
| 2460454.06670 | 9967 | 11200 | 755.0943 | 24 / 755 | 755.094, 377.547, 251.698, 188.774, 151.019, 125.849, 107.871, 94.3868, 83.8994, 75.5094, 68.6449, 62.9245, 58.0842, 53.9353, 50.3396, 47.1934, 44.4173, 37.7547, 35.9569, 31.4623 |
| 2460467.67143 | 9640 | 11200 | 768.6991 | 23 / 768 | 768.699, 384.349, 256.233, 192.175, 153.74, 128.117, 109.814, 96.0874, 85.411, 76.8699, 69.8817, 64.0583, 59.1307, 54.9071, 51.2466, 48.0437, 45.2176, 36.6047, 34.9409, 24.7967 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-2108.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:09:10Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:09:11Z: TOI-2108.01 (TIC 347538174, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:09:12Z
- SIMBAD (done, 2026-09-26): 3 match(es) in SIMBAD within 30" as of 2026-09-26T10:09:13Z: TOI-2108 (**); ** TOI 2108A (*); ** TOI 2108B (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 4 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459698.9717: recovered, depth 11200 ± 149 ppm (catalogue 16385 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, ≤2.5, ≤2.5, 4; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 33%, 20%, 20%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 12 repeat-candidate event(s); first at BJD 2459719.3550, ΔT = 20.383 d, 0 of 20 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | inconclusive | TOI-2108.01: Gaia DR3 1297566382410874496 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00"; another source 1.20" away, ΔG 2.203138000000001) |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2108.01: Teff 6204 K, R* 1.35 ± 0.11, M* 1.24 ± 0.12, ρ* 0.51 ± 0.13 ρ☉ (dwarf sequence, M_G 3.59, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2108.01: 4 Gaia neighbour(s) within 52.5", contamination 11.74%; depth 11200 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 1297566386706664704, 1.2", ΔG 2.20); a centroid test is needed |
| Pointing and quality census per event | failed | 24 persistent event(s), 8 clean; BJD 2459719.3550 suspect: MOM_CENTR2 z=-5.5, SAP_BKG z=-5.2; BJD 2459719.3925 suspect: MOM_CENTR2 z=-5.6, SAP_BKG z=-6.3; BJD 2459719.4043 suspect: MOM_CENTR2 z=-5.2, SAP_BKG z=-6.4; BJD 2459720.2001 suspect: argabrightening (in event), manual exclude (in event), MOM_CENTR1 z=-5.3, MOM_CENTR2 z=+6.6, POS_CORR1 z=-6.6, POS_CORR2 z=+7.8, SAP_BKG z=+6.9 |
| Moving objects at screen-event epochs | inconclusive | 24 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-2108.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2108.01: ** TOI 2108A otype * (star_or_other) at 0.1" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-2108-01.yaml
python -m cygnus.multi report campaigns/toi-2108-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit** (three periods after the reference). No new signal.

Source: `campaigns/toi-2108-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.

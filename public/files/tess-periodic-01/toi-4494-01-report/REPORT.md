<!-- [private Drive store] -->
# Known-object test, TOI-4494.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4494-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #531, calibrate_screen #495, event_census #506, fetch_products #492, known_signal_recovery #496, moving_objects #508, period_aliases #507, prior_art #533, residual_screen #501, stellar_context #497, variability_guard #532
- Runner finished (UTC): 2026-09-26T10:09:33Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4494.01 (BJD 2460318.2125: recovered, depth 3380 ± 40 ppm (catalogue 3821 ppm)).
Outside the catalogued epoch the screen left 208 threshold entries forming **79 distinct event(s)**, **13 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460350.7444 matches the catalogued transit's depth (3273 vs 3380 ppm), 32.534 d later; 1 of 32 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4494.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 40466976 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 293.328194 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 33.482606 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460318.212526 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 3821.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.67 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 7.3664 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-04-02 10:08:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | lightcurve | 74 | True | `4ce5cf0589714511` | True |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | lightcurve | 75 | False | `7b5899a444ab138b` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | 2460318.21253 | recovered | 111 | 3380 ± 40 | 3821 | -0.05 |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | — | epoch not in this light curve | — | — | 3821 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | 4 | False | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2 | True | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 | 1h: 1000, 2h: 1000, 4h: 1000, 8h: 1000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.74440 | -0.00353 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | 2460312.87441 | -0.00280 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | 2460312.93135 | -0.00205 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.87975 | -0.00163 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.95343 | -0.00128 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.81940 | -0.00118 | 3 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.57981 | -0.00112 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.62078 | -0.00110 | 5 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.61176 | -0.00109 | 4 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.65342 | -0.00107 | 8 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.62981 | -0.00104 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.64301 | -0.00101 | 5 | PDCSAP+SAP | 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460356.69451 | -0.00098 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.51864 | -0.00310 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.92350 | -0.00237 | 3 | SAP | 2, 3 | no |
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | 2460312.86469 | -0.00213 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.88392 | -0.00209 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.74989 | -0.00202 | 5 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.76586 | -0.00194 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.00752 | -0.00190 | 3 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.35613 | -0.00189 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.43391 | -0.00180 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.87281 | -0.00178 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.93531 | -0.00174 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.76169 | -0.00171 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.84156 | -0.00166 | 6 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.89503 | -0.00163 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.58044 | -0.00159 | 5 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.79572 | -0.00156 | 3 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.71100 | -0.00153 | 3 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.14641 | -0.00152 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.15474 | -0.00151 | 2 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | 2460318.90900 | -0.00151 | 2 | SAP | 1 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.54919 | -0.00148 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.73114 | -0.00147 | 6 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.91378 | -0.00143 | 7 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.98114 | -0.00142 | 4 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.82975 | -0.00141 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.77975 | -0.00139 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.75683 | -0.00138 | 3 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.74364 | -0.00138 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.94364 | -0.00136 | 4 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.81933 | -0.00135 | 7 | SAP | 1, 2, 3 | no |
| `tess2024003055635-s0074-0000000040466976-0269-s_lc.fits` | 2460318.92428 | -0.00134 | 2 | SAP | 1 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.04641 | -0.00132 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.71933 | -0.00132 | 5 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.34850 | -0.00131 | 3 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.79086 | -0.00130 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.81100 | -0.00127 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.46516 | -0.00126 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.96378 | -0.00123 | 3 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.44641 | -0.00123 | 6 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.37975 | -0.00121 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.61933 | -0.00120 | 5 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.67419 | -0.00119 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.48322 | -0.00118 | 5 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460353.89168 | -0.00117 | 3 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.01724 | -0.00117 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.49989 | -0.00117 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.64503 | -0.00115 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.80544 | -0.00115 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.87565 | -0.00115 | 2 | PDCSAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.70405 | -0.00114 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.95614 | -0.00114 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460346.00197 | -0.00112 | 2 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.33599 | -0.00110 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.69433 | -0.00107 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460344.45335 | -0.00107 | 2 | SAP | 1, 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.83398 | -0.00106 | 2 | PDCSAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.32072 | -0.00104 | 3 | SAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.90065 | -0.00103 | 2 | PDCSAP+SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.63537 | -0.00103 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.60891 | -0.00102 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.88121 | -0.00101 | 2 | PDCSAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.56030 | -0.00100 | 2 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460345.65822 | -0.00098 | 3 | SAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460350.86801 | -0.00095 | 3 | PDCSAP | 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460353.85904 | -0.00093 | 2 | PDCSAP | 2, 3 | no |
| `tess2024030031500-s0075-0000000040466976-0270-s_lc.fits` | 2460342.12417 | -0.00078 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460350.74440 | 3273 | 3380 | 32.5340 | 1 / 32 | 32.534 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4494.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:09:30Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:09:31Z: TOI-4494.01 (TIC 40466976, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:09:33Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:09:33Z: HD 184470 (**)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460318.2125: recovered, depth 3380 ± 40 ppm (catalogue 3821 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 1 repeat-candidate event(s); first at BJD 2460350.7444, ΔT = 32.534 d, 1 of 32 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (32.534 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4494.01: Gaia DR3 2045712375004610944 at 0.01" (propagated 2016.0 → J2015.5; 0.01" unpropagated) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-4494.01: dwarf priors not applied — no positive parallax or G magnitude; RUWE n/a ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4494.01: 106 Gaia neighbour(s) within 52.5", contamination 2.71%; depth 3380 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 2045711928341545088, 43.6", ΔG 4.77); a centroid test is needed |
| Pointing and quality census per event | failed | 13 persistent event(s), 10 clean; BJD 2460312.8744 suspect: coarse point (in event), earth point (in event), manual exclude (in event), momentum dump (in event), MOM_CENTR1 z=+13.8, MOM_CENTR2 z=-13.2, POS_CORR1 z=+12.6, POS_CORR2 z=-12.2; BJD 2460312.9314 suspect: coarse point (within ±0.25 d), earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), MOM_CENTR1 z=+14.5, MOM_CENTR2 z=-16.1, POS_CORR1 z=+13.5, POS_CORR2 z=-14.4; BJD 2460345.8797 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | passed | 13 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-4494.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-4494.01: HD 184470 otype ** (multiple) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4494-01.yaml
python -m cygnus.multi report campaigns/toi-4494-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit** (one period after the reference). No new signal.

Source: `campaigns/toi-4494-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.

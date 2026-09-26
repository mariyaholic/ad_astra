<!-- cygnus:generated-draft -->
# Known-object test, TOI-4543.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4543-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #143, calibrate_screen #111, event_census #123, fetch_products #108, known_signal_recovery #113, moving_objects #126, period_aliases #124, prior_art #146, residual_screen #118, stellar_context #115, variability_guard #144
- Runner finished (UTC): 2026-09-26T09:55:17Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4543.01 (BJD 2460212.2478: recovered, depth 3931 ± 44 ppm (catalogue 4820 ppm)).
Outside the catalogued epoch the screen left 133 threshold entries forming **50 distinct event(s)**, **9 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460218.0188 matches the catalogued transit's depth (3283 vs 3931 ppm), 5.768 d later; 1 of 5 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4543.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 435336785 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 55.140851 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 13.552772 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460212.247805 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 4820.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.551 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 6.7943 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-11-15 16:02:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | lightcurve | 70 | True | `841f537448164491` | True |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | lightcurve | 71 | False | `c88b879b24559004` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460212.24780 | recovered | 136 | 3931 ± 44 | 4820 | 0.06 |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | — | epoch not in this light curve | — | — | 4820 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 3 | False | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 | 1h: 2000, 2h: 2000, 4h: 2000, 8h: 2000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460258.44283 | -0.00435 | 114 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.66842 | -0.00433 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460241.12081 | -0.00412 | 117 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460229.57161 | -0.00410 | 119 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460223.79415 | -0.00390 | 113 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460218.01876 | -0.00356 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460226.98742 | -0.00214 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.75314 | -0.00207 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460229.65703 | -0.00179 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.91356 | -0.00272 | 2 | SAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.23466 | -0.00271 | 2 | SAP | 1, 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.19021 | -0.00244 | 2 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.02537 | -0.00229 | 11 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.06079 | -0.00227 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.08162 | -0.00220 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.98301 | -0.00213 | 5 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.97468 | -0.00209 | 2 | SAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.15827 | -0.00204 | 2 | SAP | 1, 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.00409 | -0.00204 | 2 | SAP | 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.05965 | -0.00197 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.18163 | -0.00197 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.96912 | -0.00196 | 2 | SAP | 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460226.95895 | -0.00194 | 3 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.05662 | -0.00192 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.84689 | -0.00186 | 2 | SAP | 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460226.95339 | -0.00186 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.89690 | -0.00184 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.03996 | -0.00184 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.04551 | -0.00183 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460245.77862 | -0.00180 | 3 | SAP | 1, 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460240.27703 | -0.00177 | 2 | SAP | 1, 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.03882 | -0.00177 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.17399 | -0.00174 | 7 | SAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460226.80130 | -0.00173 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460253.15662 | -0.00171 | 2 | SAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.93648 | -0.00170 | 3 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460252.78717 | -0.00168 | 4 | SAP | 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460219.49941 | -0.00167 | 2 | SAP | 1, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.02145 | -0.00167 | 3 | SAP | 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460227.24161 | -0.00167 | 2 | SAP | 1, 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460226.99576 | -0.00163 | 2 | SAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460245.55362 | -0.00160 | 2 | PDCSAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460217.94792 | -0.00158 | 2 | SAP | 1, 2 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460245.57306 | -0.00153 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460245.56473 | -0.00150 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460245.49667 | -0.00149 | 2 | PDCSAP | 2, 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460245.54112 | -0.00147 | 2 | PDCSAP | 3 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460245.54667 | -0.00146 | 4 | PDCSAP | 2, 3 | no |
| `tess2023263165758-s0070-0000000435336785-0265-s_lc.fits` | 2460223.15800 | -0.00138 | 2 | PDCSAP | 1 | no |
| `tess2023289093419-s0071-0000000435336785-0266-s_lc.fits` | 2460241.20623 | -0.00131 | 2 | PDCSAP | 1 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460218.01876 | 3283 | 3931 | 5.7685 | 1 / 5 | 5.7685 |
| 2460223.79415 | 3577 | 3931 | 11.5439 | 2 / 11 | 11.5439, 5.7719 |
| 2460229.57161 | 3895 | 3931 | 17.3213 | 2 / 17 | 17.3213, 5.7738 |
| 2460241.12081 | 3970 | 3931 | 28.8706 | 2 / 28 | 28.8706, 5.7741 |
| 2460252.66842 | 3543 | 3931 | 40.4182 | 2 / 40 | 40.4182, 5.774 |
| 2460258.44283 | 4196 | 3931 | 46.1926 | 4 / 46 | 46.1926, 23.0963, 11.5481, 5.7741 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4543.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T09:55:14Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T09:55:16Z: TOI-4543.01 (TIC 435336785, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T09:55:17Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T09:55:17Z: HD  22833 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460212.2478: recovered, depth 3931 ± 44 ppm (catalogue 4820 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | passed | completeness for the reference box (2000ppm_4h) at each light curve's k*: 100%, 100% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 6 repeat-candidate event(s); first at BJD 2460218.0188, ΔT = 5.768 d, 1 of 5 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (5.7685 d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4543.01: Gaia DR3 41107205006988800 at 0.01" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-4543.01: dwarf priors not applied — RUWE 2.850778 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-4543.01: 4 Gaia neighbour(s) within 52.5", contamination 0.00%; depth 3931 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 9 persistent event(s), 6 clean; BJD 2460241.1208 suspect: MOM_CENTR2 z=+13.4, POS_CORR2 z=+13.4, SAP_BKG z=-5.8; BJD 2460252.6684 caution: manual exclude (within ±0.25 d); BJD 2460252.7531 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 9 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-4543.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4543.01: HD  22833 otype * (star_or_other) at 0.2" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4543-01.yaml
python -m cygnus.multi report campaigns/toi-4543-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** The joint period (5.7712 d) is the catalogued period (5.7740 d); both events are single periods from the reference. No new signal.

Source: `campaigns/toi-4543-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.

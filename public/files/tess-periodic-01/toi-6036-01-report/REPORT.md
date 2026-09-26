<!-- [private Drive store] -->
# Known-object test, TOI-6036.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6036-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #885, calibrate_screen #846, event_census #858, fetch_products #845, known_signal_recovery #848, moving_objects #860, period_aliases #859, prior_art #889, residual_screen #853, stellar_context #849, variability_guard #886
- Runner finished (UTC): 2026-09-26T10:22:13Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6036.01 (BJD 2460623.0373: recovered, depth 6352 ± 72 ppm (catalogue 7191 ppm)).
Outside the catalogued epoch the screen left 147 threshold entries forming **26 distinct event(s)**, **23 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2460616.4167 matches the catalogued transit's depth (3724 vs 6352 ppm), 6.619 d later; 1 of 6 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6036.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 129756316 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 34.836888 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 40.993944 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2460623.037278 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 7191.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 5.814 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.74061 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2025-07-08 10:08:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | lightcurve | 85 | True | `c663c0006842e3d2` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460623.03728 | recovered | 174 | 6352 ± 72 | 7191 | -0.04 |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.54031 | -0.00989 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.52225 | -0.00988 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.55975 | -0.00981 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.50906 | -0.00976 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.49725 | -0.00968 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.51670 | -0.00944 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.42364 | -0.00933 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.48336 | -0.00911 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.43545 | -0.00907 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.45559 | -0.00902 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.52989 | -0.00888 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.46600 | -0.00882 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.58128 | -0.00876 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.44378 | -0.00865 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.61462 | -0.00857 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.60281 | -0.00843 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.47503 | -0.00825 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.55003 | -0.00820 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.56809 | -0.00798 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.41670 | -0.00768 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460629.56321 | -0.00736 | 163 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.40350 | -0.00606 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.62781 | -0.00568 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.36392 | -0.00381 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460616.70420 | -0.00327 | 2 | SAP | 3 | no |
| `tess2024300212641-s0085-0000000129756316-0282-s_lc.fits` | 2460629.44724 | -0.00319 | 2 | SAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2460616.41670 | 3724 | 6352 | 6.6188 | 1 / 6 | 6.6188 |
| 2460616.42364 | 4548 | 6352 | 6.6118 | 1 / 6 | 6.6118 |
| 2460616.43545 | 4785 | 6352 | 6.6000 | 1 / 6 | 6.6 |
| 2460616.44378 | 5105 | 6352 | 6.5917 | 1 / 6 | 6.5917 |
| 2460616.45559 | 5222 | 6352 | 6.5799 | 1 / 6 | 6.5799 |
| 2460616.46600 | 5324 | 6352 | 6.5695 | 1 / 6 | 6.5695 |
| 2460616.47503 | 5458 | 6352 | 6.5604 | 1 / 6 | 6.5604 |
| 2460616.48336 | 5574 | 6352 | 6.5521 | 1 / 6 | 6.5521 |
| 2460616.49725 | 5590 | 6352 | 6.5382 | 1 / 6 | 6.5382 |
| 2460616.50906 | 5577 | 6352 | 6.5264 | 1 / 6 | 6.5264 |
| 2460616.51670 | 5603 | 6352 | 6.5188 | 1 / 6 | 6.5188 |
| 2460616.52225 | 5603 | 6352 | 6.5132 | 1 / 6 | 6.5132 |
| 2460616.52989 | 5603 | 6352 | 6.5056 | 0 / 6 |  |
| 2460616.54031 | 5577 | 6352 | 6.4952 | 0 / 6 |  |
| 2460616.55003 | 5405 | 6352 | 6.4854 | 0 / 6 |  |
| 2460616.55975 | 5235 | 6352 | 6.4757 | 0 / 6 |  |
| 2460616.56809 | 5118 | 6352 | 6.4674 | 0 / 6 |  |
| 2460616.58128 | 4972 | 6352 | 6.4542 | 0 / 6 |  |
| 2460616.60281 | 4543 | 6352 | 6.4327 | 0 / 6 |  |
| 2460616.61462 | 3898 | 6352 | 6.4209 | 0 / 6 |  |
| 2460629.56321 | 6041 | 6352 | 6.5277 | 1 / 6 | 6.5277 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6036.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:22:10Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:22:11Z: TOI-6036.01 (TIC 129756316, disposition APC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:22:12Z
- SIMBAD (done, 2026-09-26): 1 match(es) in SIMBAD within 30" as of 2026-09-26T10:22:12Z: TYC 2834-650-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 1 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2460623.0373: recovered, depth 6352 ± 72 ppm (catalogue 7191 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 21 repeat-candidate event(s); first at BJD 2460616.4167, ΔT = 6.619 d, 1 of 6 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (6.6188 d); duration likelihood under Gaia priors (circular orbits) peaks at 6.62 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 1 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6036.01: Gaia DR3 338980607371641600 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6036.01: Teff 6339 K, R* 1.65 ± 0.13, M* 1.48 ± 0.15, ρ* 0.33 ± 0.09 ρ☉ (dwarf sequence, M_G 2.79, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | passed | TOI-6036.01: 7 Gaia neighbour(s) within 52.5", contamination 0.21%; depth 6352 ppm (measured depth of the recovered catalogued transit); none bright enough to produce it alone |
| Pointing and quality census per event | failed | 23 persistent event(s), 0 clean; BJD 2460616.4035 suspect: manual exclude (in event); BJD 2460616.4167 suspect: manual exclude (in event); BJD 2460616.4236 suspect: manual exclude (in event); BJD 2460616.4354 suspect: manual exclude (in event) |
| Moving objects at screen-event epochs | inconclusive | 23 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 6 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-6036.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6036.01: TYC 2834-650-1 otype * (star_or_other) at 0.5" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6036-01.yaml
python -m cygnus.multi report campaigns/toi-6036-01.yaml
```

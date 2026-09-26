<!-- cygnus:generated-draft -->
# Known-object test, TOI-1528.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-1528-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #943, calibrate_screen #919, event_census #928, fetch_products #916, known_signal_recovery #920, moving_objects #933, period_aliases #929, prior_art #945, residual_screen #927, stellar_context #921, variability_guard #944
- Runner finished (UTC): 2026-09-26T10:24:01Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-1528.01 (BJD 2459885.2843: recovered, depth 4618 ± 97 ppm (catalogue 8147 ppm)).
Outside the catalogued epoch the screen left 110 threshold entries forming **18 distinct event(s)**, **13 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459895.1592 matches the catalogued transit's depth (3350 vs 4618 ppm), 9.878 d later; 0 of 9 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-1528.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 285543785 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 13.222022 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 60.891685 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459885.284263 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 8146.5394648 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 3.9821296 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 9.716 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2026-09-18 16:00:01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | lightcurve | 58 | True | `ece78e1c47d56999` | True |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | lightcurve | 78 | False | `d00997a6d816a4b1` | True |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | lightcurve | 85 | False | `3c2f96f66e7378e5` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 2459885.28426 | recovered | 120 | 4618 ± 97 | 8147 | -0.09 |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | — | epoch not in this light curve | — | — | 8147 | — |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | — | epoch not in this light curve | — | — | 8147 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 3 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 5000 |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 5000, 2h: 5000, 4h: 5000, 8h: 10000 |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 4 | False | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 | 1h: 10000, 2h: 5000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 2459905.15903 | -0.00760 | 78 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | 2460441.84122 | -0.00757 | 51 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | 2460451.78648 | -0.00735 | 54 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460610.79168 | -0.00726 | 48 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460620.75005 | -0.00697 | 28 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460630.67219 | -0.00694 | 46 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 2459895.21402 | -0.00655 | 75 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460620.71116 | -0.00651 | 24 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | 2460441.88219 | -0.00608 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460610.83473 | -0.00594 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460610.76112 | -0.00567 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460630.63469 | -0.00552 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 2459895.15916 | -0.00392 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2024300212641-s0085-0000000285543785-0282-s_lc.fits` | 2460620.77783 | -0.00526 | 2 | PDCSAP | 1, 2, 3 | no |
| `tess2024114025118-s0078-0000000285543785-0273-s_lc.fits` | 2460441.79677 | -0.00457 | 2 | PDCSAP | 1 | no |
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 2459895.26888 | -0.00435 | 2 | PDCSAP | 1 | no |
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 2459909.99226 | -0.00382 | 2 | SAP | 2 | no |
| `tess2022302161335-s0058-0000000285543785-0247-s_lc.fits` | 2459895.28277 | -0.00360 | 2 | SAP | 1, 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459895.15916 | 3350 | 4618 | 9.8785 | 0 / 9 |  |
| 2459895.21402 | 5139 | 4618 | 9.9333 | 0 / 9 |  |
| 2459905.15903 | 5938 | 4618 | 19.8783 | 2 / 19 | 19.8783, 9.9392 |
| 2460441.84122 | 4951 | 4618 | 556.5605 | 20 / 556 | 556.561, 278.28, 185.52, 139.14, 111.312, 92.7601, 79.5086, 69.5701, 61.8401, 55.6561, 50.5964, 46.38, 39.7543, 37.104, 32.7389, 30.92, 27.828, 26.5029, 19.8772, 9.9386 |
| 2460441.88219 | 4945 | 4618 | 556.6015 | 20 / 556 | 556.601, 278.301, 185.534, 139.15, 111.32, 92.7669, 79.5145, 69.5752, 61.8446, 55.6601, 50.6001, 46.3835, 39.7572, 37.1068, 32.7413, 30.9223, 27.8301, 26.5048, 19.8786, 9.9393 |
| 2460451.78648 | 4146 | 4618 | 566.5058 | 16 / 566 | 566.506, 283.253, 188.835, 141.626, 113.301, 94.4176, 70.8132, 62.9451, 51.5005, 47.2088, 43.5774, 37.7671, 35.4066, 31.4725, 29.8161, 9.9387 |
| 2460610.76112 | 4729 | 4618 | 725.4804 | 20 / 725 | 725.48, 362.74, 241.827, 181.37, 145.096, 120.913, 103.64, 90.6851, 72.548, 65.9528, 60.4567, 51.82, 48.3654, 45.3425, 38.1832, 36.274, 31.5426, 30.2284, 25.91, 9.9381 |
| 2460610.79168 | 4776 | 4618 | 725.5110 | 20 / 725 | 725.511, 362.755, 241.837, 181.378, 145.102, 120.918, 103.644, 90.6889, 72.5511, 65.9555, 60.4592, 51.8222, 48.3674, 45.3444, 38.1848, 36.2755, 31.544, 30.2296, 25.9111, 9.9385 |
| 2460610.83473 | 4729 | 4618 | 725.5540 | 20 / 725 | 725.554, 362.777, 241.851, 181.388, 145.111, 120.926, 103.651, 90.6943, 72.5554, 65.9595, 60.4628, 51.8253, 48.3703, 45.3471, 38.1871, 36.2777, 31.5458, 30.2314, 25.9126, 9.9391 |
| 2460620.71116 | 4562 | 4618 | 735.4305 | 18 / 735 | 735.431, 367.715, 245.143, 147.086, 122.572, 105.061, 81.7145, 73.543, 66.8573, 52.5307, 49.0287, 40.8572, 38.7069, 33.4287, 31.9752, 27.2382, 19.8765, 9.9382 |
| 2460620.75005 | 4562 | 4618 | 735.4693 | 18 / 735 | 735.469, 367.735, 245.156, 147.094, 122.578, 105.067, 81.7188, 73.5469, 66.8608, 52.5335, 49.0313, 40.8594, 38.7089, 33.4304, 31.9769, 27.2396, 19.8775, 9.9388 |
| 2460630.63469 | 4235 | 4618 | 745.3540 | 20 / 745 | 745.354, 372.677, 248.451, 149.071, 124.226, 106.479, 82.8171, 74.5354, 67.7595, 57.3349, 53.2396, 49.6903, 43.8444, 41.4086, 35.493, 33.8797, 29.8142, 28.6675, 24.8451, 9.9381 |
| 2460630.67219 | 4432 | 4618 | 745.3915 | 20 / 745 | 745.391, 372.696, 248.464, 149.078, 124.232, 106.484, 82.8213, 74.5391, 67.7629, 57.3378, 53.2422, 49.6928, 43.8466, 41.4106, 35.4948, 33.8814, 29.8157, 28.6689, 24.8464, 9.9386 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-1528.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:23:58Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:23:59Z: TOI-1528.01 (TIC 285543785, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:24:00Z: Gaia DR3 427295580344901632 (type L, P — d)
- SIMBAD (done, 2026-09-26): 4 match(es) in SIMBAD within 30" as of 2026-09-26T10:24:01Z: GSC 04017-00325 (**); TYC 4017-325-2 (*); 2MASS J00525156+6053290 (LP?); TYC 4017-325-1 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 3 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459885.2843: recovered, depth 4618 ± 97 ppm (catalogue 8147 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 4, 4.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 30%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 13 repeat-candidate event(s); first at BJD 2459895.1592, ΔT = 9.878 d, 0 of 9 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | inconclusive | TOI-1528.01: Gaia DR3 427295614699192704 at 0.10" (propagated 2016.0 → J2015.5; 0.10" unpropagated, proper-motion shift 0.00"; another source 0.33" away, ΔG 0.04590400000000017) |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-1528.01: dwarf priors not applied — parallax/error 3.2 < 5; RUWE 15.722608 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-1528.01: 63 Gaia neighbour(s) within 52.5", contamination 50.02%; depth 4618 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 427295614707985792, 0.4", ΔG 0.05); a centroid test is needed |
| Pointing and quality census per event | failed | 13 persistent event(s), 5 clean; BJD 2459895.1592 suspect: manual exclude (within ±0.25 d), SAP_BKG z=-5.0; BJD 2459895.2140 suspect: manual exclude (within ±0.25 d), SAP_BKG z=-9.3; BJD 2460451.7865 suspect: SAP_BKG z=-9.4; BJD 2460610.7611 caution: earth point (within ±0.25 d), manual exclude (within ±0.25 d), momentum dump (within ±0.25 d), scattered light 2 (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 13 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 2 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-1528.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | inconclusive | TOI-1528.01: GSC 04017-00325 otype ** (multiple) at 0.0" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-1528-01.yaml
python -m cygnus.multi report campaigns/toi-1528-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit** (one period after the reference). No new signal.

Source: `campaigns/toi-1528-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.

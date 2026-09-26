<!-- [private Drive store] -->
# Known-object test, TOI-4597.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-4597-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #304, calibrate_screen #292, event_census #299, fetch_products #290, known_signal_recovery #293, moving_objects #301, period_aliases #300, prior_art #307, residual_screen #297, stellar_context #294, variability_guard #305
- Runner finished (UTC): 2026-09-26T10:00:24Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-4597.01 (BJD 2459523.1972: recovered, depth 6712 ± 415 ppm (catalogue 6900 ppm)).
Outside the catalogued epoch the screen left 19 threshold entries forming **4 distinct event(s)**, **3 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459476.5408 matches the catalogued transit's depth (6701 vs 6712 ppm), 46.678 d later; 4 of 46 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-4597.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 68573534 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 73.705654 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | 22.146384 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459523.197223 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 6900.0 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 2.526 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 7.82403 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2024-11-21 12:03:02 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2021284114741-s0044-0000000068573534-0215-s_lc.fits` | lightcurve | 44 | True | `4467ce2be9c4346e` | True |
| `tess2021258175143-s0043-0000000068573534-0214-s_lc.fits` | lightcurve | 43 | False | `9ec973560dc1a19d` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2021284114741-s0044-0000000068573534-0215-s_lc.fits` | 2459523.19722 | recovered | 75 | 6712 ± 415 | 6900 | 0.52 |
| `tess2021258175143-s0043-0000000068573534-0214-s_lc.fits` | — | epoch not in this light curve | — | — | 6900 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2021284114741-s0044-0000000068573534-0215-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2021258175143-s0043-0000000068573534-0214-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2021258175143-s0043-0000000068573534-0214-s_lc.fits` | 2459481.20445 | -0.01514 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021258175143-s0043-0000000068573534-0214-s_lc.fits` | 2459476.54080 | -0.01469 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021258175143-s0043-0000000068573534-0214-s_lc.fits` | 2459490.57406 | -0.01314 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2021284114741-s0044-0000000068573534-0215-s_lc.fits` | 2459513.85088 | -0.01283 | 3 | SAP | 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459476.54080 | 6701 | 6712 | 46.6780 | 4 / 46 | 46.678, 23.339, 9.3356, 4.6678 |
| 2459481.20445 | 7165 | 6712 | 42.0144 | 3 / 42 | 42.0144, 14.0048, 4.6683 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-4597.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:00:21Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:00:22Z: TOI-4597.01 (TIC 68573534, disposition PC)
- VSX (done, 2026-09-26): no match in VSX within 30" as of 2026-09-26T10:00:23Z
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:00:24Z: HD  31221b (Pl?); HD  31221 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459523.1972: recovered, depth 6712 ± 415 ppm (catalogue 6900 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 2 repeat-candidate event(s); first at BJD 2459476.5408, ΔT = 46.678 d, 4 of 46 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (46.678, 23.339, 9.3356, 4.6678 d); duration likelihood under Gaia priors (circular orbits) peaks at 4.67 d (weight 0.71) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-4597.01: Gaia DR3 3412431441720096128 at 0.00" (propagated 2016.0 → J2015.5; 0.02" unpropagated, proper-motion shift 0.02") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-4597.01: Teff 7618 K, R* 1.72 ± 0.14, M* 1.60 ± 0.16, ρ* 0.31 ± 0.08 ρ☉ (dwarf sequence, M_G 2.53, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-4597.01: 9 Gaia neighbour(s) within 52.5", contamination 1.05%; depth 6712 ppm (measured depth of the recovered catalogued transit); 1 could produce it if fully eclipsed (brightest 3412431471783190016, 43.9", ΔG 5.08); a centroid test is needed |
| Pointing and quality census per event | inconclusive | 3 persistent event(s), 2 clean; BJD 2459490.5741 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 3 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-4597.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-4597.01: HD  31221 otype * (star_or_other) at 0.5" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-4597-01.yaml
python -m cygnus.multi report campaigns/toi-4597-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead events are the target's own catalogued ephemeris transits.** The joint period (4.6656 d) is the catalogued period (4.6664 d) within its uncertainty; predicted-transit offsets +0.01/-0.06 h at sigma 0.14-0.15 h. The shape/duration mismatches (ratio 0.91, duration 1.50) and the extreme chi2_nu (95-108) additionally mark the events as poor-quality windows. No new signal.

Source: `campaigns/toi-4597-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.

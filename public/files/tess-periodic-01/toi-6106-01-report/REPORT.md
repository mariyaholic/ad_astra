<!-- [private Drive store] -->
# Known-object test, TOI-6106.01

> **Generated draft** (`python -m cygnus.multi report`). Numbers are copied from the runner's saved
> outputs; the interpretation lines are templates. Review against `docs/AGENT_RUNBOOK.md`, edit, and
> delete the first line (the draft marker) once reviewed.

- Campaign spec: `campaigns/toi-6106-01.yaml`
- Parent queue: `tess-periodic-01`
- Ledger runs: alias_cross_instrument #968, calibrate_screen #942, event_census #955, fetch_products #940, known_signal_recovery #946, moving_objects #965, period_aliases #956, prior_art #970, residual_screen #951, stellar_context #947, variability_guard #969
- Runner finished (UTC): 2026-09-26T10:25:23Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6106.01 (BJD 2459964.6245: recovered, depth 18891 ± 299 ppm (catalogue 19638 ppm)).
Outside the catalogued epoch the screen left 195 threshold entries forming **24 distinct event(s)**, **22 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2459971.0381 matches the catalogued transit's depth (16176 vs 18891 ppm), 6.387 d later; 0 of 6 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6106.01 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tic | 258234731 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| ra_deg | 127.019217 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| dec_deg | -24.166962 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| t0_bjd | 2459964.624513 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| depth_ppm | 19637.6137844 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| duration_h | 4.0307342 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| tmag | 11.646 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |
| catalogue_row_updated | 2023-03-31 12:03:09 | NASA Exoplanet Archive TOI table (Gaia DR2 epoch J2015.5, verified reports/position-epoch-audit-01) (copied in the spec) |

## Products

| Product | Kind | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | lightcurve | 61 | True | `02fcd7b1fd601390` | True |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | lightcurve | 88 | False | `0fee5a3f76aefbe6` | True |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459964.62451 | recovered | 121 | 18891 ± 299 | 19638 | 0.64 |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | — | epoch not in this light curve | — | — | 19638 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 10000, 8h: 10000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460703.35258 | -0.02163 | 103 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459977.46316 | -0.01949 | 13 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459977.47566 | -0.01929 | 38 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459983.92082 | -0.01896 | 40 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459977.43746 | -0.01847 | 14 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459971.03810 | -0.01802 | 79 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460709.76096 | -0.01779 | 89 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459977.53052 | -0.01730 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459983.86110 | -0.01712 | 44 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460716.16860 | -0.01706 | 50 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459971.09782 | -0.01684 | 5 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460716.22277 | -0.01661 | 32 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459977.42010 | -0.01622 | 17 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459983.95693 | -0.01576 | 10 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459971.10893 | -0.01505 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460709.71512 | -0.01476 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460716.26305 | -0.01451 | 8 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460716.20749 | -0.01383 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460709.71026 | -0.01365 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460690.17035 | -0.01202 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460709.84499 | -0.01167 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2025014115807-s0088-0000000258234731-0285-s_lc.fits` | 2460696.99760 | -0.01143 | 3 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459977.40552 | -0.01414 | 2 | PDCSAP | 1 | no |
| `tess2023018032328-s0061-0000000258234731-0250-s_lc.fits` | 2459981.72915 | -0.00880 | 2 | SAP | 2, 3 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2459971.03810 | 16176 | 18891 | 6.3869 | 0 / 6 |  |
| 2459971.09782 | 15122 | 18891 | 6.4467 | 0 / 6 |  |
| 2459971.10893 | 13093 | 18891 | 6.4578 | 0 / 6 |  |
| 2459977.42010 | 13586 | 18891 | 12.7689 | 1 / 12 | 12.7689 |
| 2459977.43746 | 15227 | 18891 | 12.7863 | 0 / 12 |  |
| 2459977.46316 | 15750 | 18891 | 12.8120 | 0 / 12 |  |
| 2459977.47566 | 15750 | 18891 | 12.8245 | 0 / 12 |  |
| 2459977.53052 | 12177 | 18891 | 12.8794 | 0 / 12 |  |
| 2459983.86110 | 15149 | 18891 | 19.2099 | 0 / 19 |  |
| 2459983.92082 | 15912 | 18891 | 19.2697 | 2 / 19 | 19.2697, 6.4232 |
| 2459983.95693 | 13997 | 18891 | 19.3058 | 0 / 19 |  |
| 2460703.35258 | 19012 | 18891 | 738.7014 | 33 / 738 | 738.701, 369.351, 246.234, 184.675, 147.74, 123.117, 105.529, 92.3377, 82.0779, 73.8701, 67.1547, 61.5585, 56.8232, 52.7644, 49.2468, 46.1688, 43.453, 41.039, 38.879, 36.9351 |
| 2460709.71026 | 9462 | 18891 | 745.0591 | 34 / 745 | 745.059, 372.53, 248.353, 186.265, 149.012, 124.177, 106.437, 93.1324, 82.7843, 74.5059, 67.7326, 62.0883, 57.3122, 53.2185, 49.6706, 46.5662, 43.827, 41.3922, 39.2136, 37.253 |
| 2460709.71512 | 11103 | 18891 | 745.0640 | 34 / 745 | 745.064, 372.532, 248.355, 186.266, 149.013, 124.177, 106.438, 93.133, 82.7849, 74.5064, 67.7331, 62.0887, 57.3126, 53.2189, 49.6709, 46.5665, 43.8273, 41.3924, 39.2139, 37.2532 |
| 2460709.76096 | 14954 | 18891 | 745.1098 | 35 / 745 | 745.11, 372.555, 248.37, 186.277, 149.022, 124.185, 106.444, 93.1387, 82.79, 74.511, 67.7373, 62.0925, 57.3161, 53.2221, 49.674, 46.5694, 43.83, 41.395, 39.2163, 37.2555 |
| 2460716.16860 | 14476 | 18891 | 751.5174 | 34 / 751 | 751.517, 375.759, 250.506, 187.879, 150.304, 125.253, 107.36, 93.9397, 83.5019, 75.1517, 68.3198, 62.6265, 57.809, 53.6798, 50.1012, 46.9698, 44.2069, 41.751, 39.5535, 37.5759 |
| 2460716.20749 | 15154 | 18891 | 751.5563 | 34 / 751 | 751.556, 375.778, 250.519, 187.889, 150.311, 125.259, 107.365, 93.9445, 83.5063, 75.1556, 68.3233, 62.6297, 57.812, 53.6826, 50.1038, 46.9723, 44.2092, 41.7531, 39.5556, 37.5778 |
| 2460716.22277 | 15098 | 18891 | 751.5716 | 34 / 751 | 751.572, 375.786, 250.524, 187.893, 150.314, 125.262, 107.367, 93.9465, 83.508, 75.1572, 68.3247, 62.631, 57.8132, 53.6837, 50.1048, 46.9732, 44.2101, 41.754, 39.5564, 37.5786 |
| 2460716.26305 | 10913 | 18891 | 751.6119 | 33 / 751 | 751.612, 375.806, 250.537, 187.903, 150.322, 125.269, 107.373, 93.9515, 83.5124, 75.1612, 68.3284, 62.6343, 57.8163, 53.6866, 50.1075, 46.9757, 44.2125, 41.7562, 39.5585, 37.5806 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6106.01**

- NASA_Exoplanet_Archive (done, 2026-09-26): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-26T10:25:19Z
- TESS_TOI (done, 2026-09-26): 1 match(es) in TESS_TOI within 30" as of 2026-09-26T10:25:21Z: TOI-6106.01 (TIC 258234731, disposition APC)
- VSX (done, 2026-09-26): 1 match(es) in VSX within 30" as of 2026-09-26T10:25:22Z: Gaia DR3 5696528202583814400 (type ROT, P — d)
- SIMBAD (done, 2026-09-26): 2 match(es) in SIMBAD within 30" as of 2026-09-26T10:25:22Z: 2MASS J08280462-2410011 (SB*); 2MASS J08280553-2409573 (*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 2 product(s) from MAST checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459964.6245: recovered, depth 18891 ± 299 ppm (catalogue 19638 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 19 repeat-candidate event(s); first at BJD 2459971.0381, ΔT = 6.387 d, 0 of 6 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 2 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6106.01: Gaia DR3 5696528202583814400 at 0.00" (propagated 2016.0 → J2015.5; 0.01" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6106.01: Teff 5557 K, R* 0.99 ± 0.08, M* 0.99 ± 0.10, ρ* 1.01 ± 0.26 ρ☉ (dwarf sequence, M_G 4.74, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6106.01: 44 Gaia neighbour(s) within 52.5", contamination 55.12%; depth 18891 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 5696528202589468800, 13.0", ΔG 0.55); a centroid test is needed |
| Pointing and quality census per event | failed | 22 persistent event(s), 13 clean; BJD 2460690.1704 suspect: earth point (in event), manual exclude (in event), momentum dump (in event), MOM_CENTR1 z=+6.5, MOM_CENTR2 z=-11.1, POS_CORR1 z=-9.9, POS_CORR2 z=-30.4, SAP_BKG z=-61.0; BJD 2460696.9976 suspect: manual exclude (in event), momentum dump (in event), MOM_CENTR1 z=-7.6, POS_CORR1 z=-5.0; BJD 2460703.3526 suspect: MOM_CENTR1 z=-7.5; BJD 2460709.7103 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 22 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 4 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no light curve from this instrument was fetched (add Kepler/K2/HLSP collections to fetch_products) |
| Independent-epoch confirmation (ZTF) | not_tested | no light curve from this instrument was fetched |
| Variable-catalogue collision (VSX) | passed | TOI-6106.01: Gaia DR3 5696528202583814400   ROT                            P=None at 0.7" |
| Object-class guard (SIMBAD) | inconclusive | TOI-6106.01: 2MASS J08280462-2410011 otype SB* (multiple) at 0.3" |

## Reproduction

```bash
python -m cygnus.multi run campaigns/toi-6106-01.yaml
python -m cygnus.multi report campaigns/toi-6106-01.yaml
```

## Reviewer notes (2026-09-26, lead vetting)

**Rejected: the lead event is the target's own catalogued ephemeris transit** (one period after the reference). No new signal.

Source: `campaigns/toi-6106-01/vetting/VETTING.md` and `campaigns/tess-periodic-01/LEAD_VETTING_LOG.md`.

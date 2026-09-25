# Known-object test, TOI-6667.01

> Drafted by `python -m cygnus.campaign report` from the runner's outputs; reviewed 2026-09-25.
> The escalation and reviewer notes below were added by hand; every other number is the runner's.

## Escalation (2026-09-25)

**Repeat candidate — unverified lead.** The calibrated screen found persistent events in sector 104 at
BJD 2461197.35–.55 whose depths (7145–8156 ppm) fall inside the 0.5–2× window of the catalogued depth
(7982 ppm), ΔT ≈ 2114.0 d from the catalogued epoch (2459083.31, sector 28); 29 of 2114 period aliases
remain allowed. `docs/AGENT_RUNBOOK.md` makes a repeat candidate an escalation: the evidence level is
**not** raised here, and a reviewer should decide the follow-up. The hand tests done so far are in
*Reviewer notes*; difference-image centroids, an eclipsing-binary check and the TOI/ExoFOP record are
still open.

The catalogue cross-match was first `inconclusive` (NASA_Exoplanet_Archive and TESS_TOI failed with a
proxy/tunnel `ProxyError`). It was re-run at 2026-09-25T11:18Z with all four services answering and is now
`passed`: TESS_TOI returns TOI-6667.01 (TIC 161169240, disposition APC), with no Exoplanet Archive or VSX
match. The TOI record should still be read for a catalogue period before the lead is advanced.

Points to weigh: the cluster's six mid-times span only ≈ 0.13 d, so it is one contiguous feature rather
than six transits; the recovered depth is ≈ 0.9–1.0× the catalogue's; and with 29 aliases surviving the
period is not constrained by this data.


- Campaign spec: `campaigns/toi-6667-01.yaml`
- Parent queue: `tess-mono-01`
- Ledger runs: calibrate_screen #603, fetch_products #602, known_signal_recovery #604, period_aliases #606, prior_art #607, residual_screen #605
- Runner finished (UTC): 2026-09-25T11:19:05Z

## Bottom line

The calibrated screen **recovered the catalogued transit** of TOI-6667.01 (BJD 2459083.3107: recovered, depth 7982 ± 239 ppm (catalogue 5127 ppm)).
Outside the catalogued epoch the screen left 93 threshold entries forming **31 distinct event(s)**, **11 persistent** (SAP and PDCSAP, two or more baselines). None is vetted; see *Screen events*.
**Repeat candidate (unverified lead):** a persistent event at BJD 2461197.3537 matches the catalogued transit's depth (7145 vs 7982 ppm), 2114.028 d later; 29 of 2114 period aliases remain. See *Repeat candidates*.

This is a pipeline check on a known object, not a discovery claim. Two transits allow only the listed period aliases; they do not fix the period.

## Reviewer notes (2026-09-25)

Positive control **passed**: the sector-28 profile (`sector28/normalized_series.csv`) shows a
flat-bottomed dip centred on the catalogued epoch (BJD 2459083.3107), recovered at 7982 ± 239 ppm
against a catalogue depth of 5127 ppm. The screen left 11 persistent events; the runner raised a repeat
candidate, so this is escalated above.

Hand checks:

- **2461197.35 / .39 / .43 / .45 / .46 / .49 (sector 104)** — the repeat-candidate cluster. All mid-times
  span ≈ 0.13 d, i.e. one contiguous feature, not six transits. Flux-centroid residual is ≈ 0.8σ in
  MOM_CENTR1 (−0.0015 px vs sd 0.0018) and ≈ 1.2σ in MOM_CENTR2 (−0.0027 px vs sd 0.0023).
- **2459075.21439 (sector 28)** — a separate persistent event ≈ 8 d before the catalogued epoch;
  centroid residual ≤ 0.5σ.
- **Catalogue cross-match** first ran at 2026-09-25T04:23Z with NASA_Exoplanet_Archive and TESS_TOI
  failing (`ProxyError: Tunnel connection failed`); VSX (no match) and SIMBAD (UCAC4 184-215750, a
  high-proper-motion star) answered. The re-run at 2026-09-25T11:18Z answered on all four services
  (see *Catalogue cross-match* below), so the check is now `passed`.

Not decided here; the record's `lead`/`Unverified lead` is left unchanged.

## Target

| Field | Value | Source |
|---|---|---|
| name | TOI-6667.01 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tic | 161169240 | NASA Exoplanet Archive TOI table (copied in the spec) |
| ra_deg | 339.35783 | NASA Exoplanet Archive TOI table (copied in the spec) |
| dec_deg | -53.31905 | NASA Exoplanet Archive TOI table (copied in the spec) |
| t0_bjd | 2459083.310651 | NASA Exoplanet Archive TOI table (copied in the spec) |
| depth_ppm | 5126.8337118 | NASA Exoplanet Archive TOI table (copied in the spec) |
| duration_h | 6.6621453 | NASA Exoplanet Archive TOI table (copied in the spec) |
| tmag | 12.122 | NASA Exoplanet Archive TOI table (copied in the spec) |
| catalogue_row_updated | 2024-03-28 10:08:02 | NASA Exoplanet Archive TOI table (copied in the spec) |

## Products

| Product | Sector | Covers catalogued epoch | SHA-256 (first 16) | Retrieved now |
|---|---|---|---|---|
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 28 | True | `73a4057aae2d7bee` | False |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 68 | False | `ebc654c917f89114` | False |
| `tess2025206162959-s0095-0000000161169240-0292-s_lc.fits` | 95 | False | `6f0b908a1b441a0f` | False |
| `tess2026086090000-s0102-0000000161169240-0304-s_lc.fits` | 102 | False | `8335cdfacd48b2d9` | False |
| `tess2026111101500-s0103-0000000161169240-0305-s_lc.fits` | 103 | False | `b430989f7c3a97d7` | False |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 104 | False | `3e6fde9208e9141d` | False |

## Positive control (catalogued transit)

| Product | Epoch (BJD) | State | Usable in-transit cadences | Measured depth (ppm) | Catalogue depth (ppm) | Entry offset (h) |
|---|---|---|---|---|---|---|
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2459083.31065 | recovered | 200 | 7982 ± 239 | 5127 | 0.35 |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | — | epoch not in this light curve | — | — | 5127 | — |
| `tess2025206162959-s0095-0000000161169240-0292-s_lc.fits` | — | epoch not in this light curve | — | — | 5127 | — |
| `tess2026086090000-s0102-0000000161169240-0304-s_lc.fits` | — | epoch not in this light curve | — | — | 5127 | — |
| `tess2026111101500-s0103-0000000161169240-0305-s_lc.fits` | — | epoch not in this light curve | — | — | 5127 | — |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | — | epoch not in this light curve | — | — | 5127 | — |

Depth: median PDCSAP residual inside ±duration/2 about the catalogued epoch, against a 2-d running median; the error is statistical only. A depth unlike the catalogue's may reflect dilution, detrending or an epoch/duration error; it is reported, not used as a pass mark.

## Calibration and sensitivity

| Product | k* (sign-flip null) | At grid floor | 90 % completeness depth at k = 5, by duration | at k* |
|---|---|---|---|---|
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2 | True | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2025206162959-s0095-0000000161169240-0292-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 10000 |
| `tess2026086090000-s0102-0000000161169240-0304-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |
| `tess2026111101500-s0103-0000000161169240-0305-s_lc.fits` | 4 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 20000, 2h: 10000, 4h: 20000, 8h: 20000 |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 3 | False | 1h: 20000, 2h: 20000, 4h: 20000, 8h: 20000 | 1h: 10000, 2h: 10000, 4h: 10000, 8h: 20000 |

The null result (if any) excludes only dips deeper than the 90 %-completeness depth for their duration.

## Screen events outside the catalogued epoch

Entries merged where they overlap in time. *Persistent* = SAP and PDCSAP at two or more baselines.

| Product | Mid time (BJD) | Deepest median residual | Max cadences | Flux | Baselines (d) | Persistent |
|---|---|---|---|---|---|---|
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.35367 | -0.01458 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.38700 | -0.01405 | 9 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.48840 | -0.01396 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.54604 | -0.01384 | 7 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.46201 | -0.01312 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.43284 | -0.01288 | 6 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2459075.21439 | -0.01263 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.44673 | -0.01243 | 2 | PDCSAP+SAP | 2, 3 | yes |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2460165.31391 | -0.01133 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2460165.32503 | -0.01114 | 4 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2460165.31808 | -0.01079 | 2 | PDCSAP+SAP | 1, 2, 3 | yes |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.33978 | -0.01322 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.41201 | -0.01301 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.31825 | -0.01272 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.53354 | -0.01266 | 3 | SAP | 1, 2, 3 | no |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.43978 | -0.01186 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.45645 | -0.01185 | 2 | SAP | 3 | no |
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2459075.27550 | -0.01184 | 2 | SAP | 3 | no |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461197.31061 | -0.01169 | 2 | SAP | 3 | no |
| `tess2026086090000-s0102-0000000161169240-0304-s_lc.fits` | 2461151.15729 | -0.01120 | 2 | SAP | 2, 3 | no |
| `tess2026137223500-s0104-0000000161169240-0306-s_lc.fits` | 2461196.37166 | -0.01079 | 2 | SAP | 1 | no |
| `tess2026086090000-s0102-0000000161169240-0304-s_lc.fits` | 2461151.14201 | -0.01071 | 2 | SAP | 3 | no |
| `tess2025206162959-s0095-0000000161169240-0292-s_lc.fits` | 2460900.39232 | -0.01045 | 2 | SAP | 3 | no |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2460165.09447 | -0.00972 | 2 | SAP | 2, 3 | no |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2460165.17642 | -0.00965 | 2 | SAP | 2 | no |
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2459075.31022 | -0.00963 | 2 | SAP | 2, 3 | no |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2460165.24030 | -0.00938 | 2 | SAP | 2 | no |
| `tess2023209231226-s0068-0000000161169240-0262-s_lc.fits` | 2460174.61666 | -0.00936 | 2 | SAP | 2, 3 | no |
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2459075.24772 | -0.00924 | 2 | SAP | 3 | no |
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2459075.21022 | -0.00900 | 2 | SAP | 2 | no |
| `tess2020212050318-s0028-0000000161169240-0190-s_lc.fits` | 2459079.49768 | -0.00881 | 2 | SAP | 2 | no |

None has been vetted: centroids, pointing, background, momentum dumps and other reductions are **not tested**. Most screen events in TESS light curves are systematics; each is at most an unverified lead.

## Repeat candidates

Persistent screen events whose depth matches the catalogued transit (0.5–2×). Periods P = ΔT/n are excluded only where a predicted transit falls on usable retrieved data and is absent; all others remain allowed. Full per-alias evidence: `period_aliases.json`.

| Event (BJD) | Depth (ppm) | Reference depth (ppm) | ΔT (d) | Aliases allowed | Allowed periods (d), first 20 |
|---|---|---|---|---|---|
| 2461197.35367 | 7145 | 7982 | 2114.0283 | 29 / 2114 | 2114.03, 1057.01, 704.676, 528.507, 422.806, 352.338, 302.004, 264.253, 234.892, 211.403, 192.184, 176.169, 162.618, 151.002, 140.935, 132.127, 124.355, 117.446, 111.265, 105.701 |
| 2461197.38700 | 7355 | 7982 | 2114.0616 | 29 / 2114 | 2114.06, 1057.03, 704.687, 528.515, 422.812, 352.344, 302.009, 264.258, 234.896, 211.406, 192.187, 176.172, 162.62, 151.004, 140.937, 132.129, 124.357, 117.448, 111.266, 105.703 |
| 2461197.43284 | 8156 | 7982 | 2114.1074 | 29 / 2114 | 2114.11, 1057.05, 704.702, 528.527, 422.822, 352.351, 302.015, 264.263, 234.901, 211.411, 192.192, 176.176, 162.624, 151.008, 140.94, 132.132, 124.359, 117.45, 111.269, 105.705 |
| 2461197.44673 | 8156 | 7982 | 2114.1213 | 29 / 2114 | 2114.12, 1057.06, 704.707, 528.53, 422.824, 352.354, 302.017, 264.265, 234.902, 211.412, 192.193, 176.177, 162.625, 151.009, 140.941, 132.133, 124.36, 117.451, 111.269, 105.706 |
| 2461197.46201 | 7924 | 7982 | 2114.1366 | 29 / 2114 | 2114.14, 1057.07, 704.712, 528.534, 422.827, 352.356, 302.019, 264.267, 234.904, 211.414, 192.194, 176.178, 162.626, 151.01, 140.942, 132.133, 124.361, 117.452, 111.27, 105.707 |
| 2461197.48840 | 7445 | 7982 | 2114.1630 | 29 / 2114 | 2114.16, 1057.08, 704.721, 528.541, 422.833, 352.361, 302.023, 264.27, 234.907, 211.416, 192.197, 176.18, 162.628, 151.012, 140.944, 132.135, 124.362, 117.454, 111.272, 105.708 |
| 2461197.54604 | 6044 | 7982 | 2114.2206 | 29 / 2114 | 2114.22, 1057.11, 704.74, 528.555, 422.844, 352.37, 302.031, 264.278, 234.913, 211.422, 192.202, 176.185, 162.632, 151.016, 140.948, 132.139, 124.366, 117.457, 111.275, 105.711 |

To advance: compare the two transit shapes, check difference-image centroids and the TOI/ExoFOP record for a period, and escalate to a reviewer (docs/AGENT_RUNBOOK.md). Do not raise the evidence level yourself.

## Catalogue cross-match

**TOI-6667.01**

- NASA_Exoplanet_Archive (done, 2026-09-25): no match in NASA_Exoplanet_Archive within 30" as of 2026-09-25T11:18:51Z
- TESS_TOI (done, 2026-09-25): 1 match(es) in TESS_TOI within 30" as of 2026-09-25T11:18:55Z: TOI-6667.01 (TIC 161169240, disposition APC)
- VSX (done, 2026-09-25): no match in VSX within 30" as of 2026-09-25T11:18:57Z
- SIMBAD (done, 2026-09-25): 1 match(es) in SIMBAD within 30" as of 2026-09-25T11:18:59Z: UCAC4 184-215750 (PM*)

## Checks

| Check | State | Note |
|---|---|---|
| Product integrity (SHA-256) | passed | 6 product(s) checksummed at first retrieval |
| Known-signal recovery (positive control) | passed | BJD 2459083.3107: recovered, depth 7982 ± 239 ppm (catalogue 5127 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, 3, 3, 3.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 7 repeat-candidate event(s); first at BJD 2461197.3537, ΔT = 2114.028 d, 29 of 2114 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (2114.03, 1057.01, 704.676, 528.507, 422.806, 352.338, 302.004, 264.253, 234.892, 211.403, 192.184, 176.169 … d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested |  |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |

## Reproduction

```bash
python -m cygnus.campaign run campaigns/toi-6667-01.yaml
python -m cygnus.campaign report campaigns/toi-6667-01.yaml
```

# tess-periodic-01 lead vetting log

Started 2026-09-26 with `python -m cygnus.campaign vet campaigns/<slug>.yaml` on the 57 `colab-p01`
leads (the single-transit pool's log is `campaigns/tess-mono-01/LEAD_VETTING_LOG.md`). Each vet run writes
`campaigns/<slug>/vetting/` (`vetting.json`, `VETTING.md`, per-event figures) and a ledger run
`cygnus.campaign:<id>:lead_vetting`. Nothing here changes a record's outcome by itself; the record/report
reconciliation happens after each verdict is read.

Batch context: the colab-p01 specs were generated from TOI rows with **no catalogued period**
(`period_days: null`, single-epoch veto), so the vet's sibling-TOI check runs each lead event against the
*current* NASA Exoplanet Archive ephemerides. Several leads fail exactly there: their repeat events are
transits of the target's own now-catalogued ephemeris, not new signals.

## Results (tool states; reviewer reading in brackets)

| Target | Event(s) | Tool result | Reading |
|---|---|---|---|
| toi-6806-01 | E1-E5 (S68/S96/S103/S104/S105) | **Sibling TOI ephemerides failed on all 5**: every event within 0.01-0.34 h (σ ≤ 0.22 h) of a predicted TOI-6806.01 transit (APC, P 23.2491 d, 48,641 ppm); VSX KELT EA P 23.249 d at 0.9″ is the same object; E5 additionally pointing +54-108σ and a 9.6″/22σ difference image | **Rejected: the lead events are the target's own catalogued ephemeris transits** (the catalogued EB's recurring transits, not new signals). |
| toi-630-01 | E1-E17 (S33, S87, …) | Sibling TOI ephemerides failed: events within ≤0.26 h of predicted TOI-630.01 transits (APC, P 4.9092 d, 13,100 ppm = the reference depth); SIMBAD EB* at 0.1″ | **Rejected: the lead events are the target's own catalogued ephemeris transits.** |
| toi-1192-01 | E1 (S41) | Sibling ephemerides failed: 2459422.3355 is 24.00 × P 45.9403 d before the reference (−0.06 ± 0.02 h) | **Rejected: the event is the catalogued signal's own transit** (24 periods before the reference epoch). |
| toi-4381-01 | E1-E32 (mostly S100) | Sibling ephemerides **failed on all 32**: the catalogued signal is P 1.4974 d (PC, 39,325 ppm; row updated 2022-08-19) and the "repeat candidate" train at ΔT 1711.53 d = 1143 × P_cat is the catalogued ephemeris recurring; the phase-0.5 test additionally finds a **3,200 ± 622 ppm secondary at P 1.50 d** — the catalogued EB's own secondary eclipse, independently confirming its binary nature | **Rejected: the lead train is the catalogued signal's own transit train** (the "22 surviving aliases" were aliases of ΔT = 1143 × P_cat). |
| toi-1229-01 | E1-E18 (S11/S12, …) | Sibling ephemerides failed: the joint period of the events is **exactly the catalogued P 31.8132 d** (APC, row updated 2023-07-12); events within 0.06-0.11 h of its predictions | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-706-01 | E1 (S31), E2 (S97) | E1: sibling ephemerides failed — 2459153.9493 = T0_cat + 1 × P 719.0381 d (PC), the catalogued signal's next transit. E2: no catalogue transit at 2460951.5448 (ΔT 2516.64 d = 3.5 × P_cat = **7 × 359.52 d**); shape/depth/duration consistent; difference image on target (2.5″, 1.6σ); Gaia not_tested (cone pending) | **The lead (E1) is rejected as a self-match. E2 remains a real event consistent with P = 359.52 d = P_cat/2** (the catalogued period's even alias; the joint family 719.04/m requires m even). Re-check the Gaia gap after the cone sweep. |
| toi-224-01 | E1-E4 (S29/S69/S96/S106) | Sibling check passed on all four (the catalogued P 705.5845 d is **incommensurate** with the observed intervals); **one common data-allowed period fits all four events: P = 31.5798 d** (n = 23, 58, 81, 91); depths 7.81/7.79/7.43/7.41 ppt, duration ratio 1.00, no odd/even alternation, no ≥4σ secondary at 8-19 covered aliases; difference images on target for E1-E3 (0.3-0.5″), E4 displaced 9.6″/7.1σ with 81 manual-exclude cadences; ZTF: 279 usable points, no phase coverage at the trial ephemeris, no ≥0.12-mag dips | **Survives: the strongest colab lead — a 31.5798-d signal with four on-target events; the TOI-table's own P 705.58 d does not reproduce the observed train** (705.58/31.58 = 22.34). E4 photometrically consistent but diff-image displaced (heavily flagged window). RV and future sectors are the next tests. |
| toi-7610-01 | E1 (S99) | (above) | **Survives vet; Gaia-field gap pending** (re-check after the cone sweep). 21 of 365 aliases data-allowed, none equal to the catalogued period. |
| toi-173-01 | E1 (S13), E2 (S27) | Sibling ephemerides failed on both: TOI-173.01 (PC, P 29.7537 d) predicted +0.00 and −0.15 h (σ 0.01 h); the TIC also carries TOI-173.02 (P 9.1702 d, PC) | **Rejected: the lead events are the catalogued signal's own transits** (11 × and 24 × P_cat). |
| toi-1709-01 | E1 (S47), E2 (S47) | Sibling ephemerides failed on both: the catalogued P 7.6288 d's adjacent transits (ΔT −2 × and −1 × P_cat) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-1356-01 | E1 (S55), E2 (S57) | Sibling ephemerides failed on both: catalogued P 24.2545 d, offsets +0.02/+0.04 h (σ 0.01 h) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-3460-01 | E1 (S39), E2 (S39) | Sibling ephemerides failed on both: the catalogued P 4.6288 d's transits one and two periods after the reference (sigma 0.00 h) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-6106-01 | E1 (S61) | Sibling ephemerides failed: DeltaT 6.43 d = 1 x catalogued P 6.4241 d (APC), +0.05 +/- 0.02 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-7464-01 | E1 (S47) | Sibling ephemerides failed: DeltaT 20.04 d = 1 x catalogued P 20.0417 d (PC), -0.06 +/- 0.01 h; diff image 148.5 arcsec off at 313 sigma | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-573-01 | E1 (S8) | Sibling ephemerides failed: the joint period equals the catalogued P 13.5773 d (APC), -0.02 h at sigma 0.00 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-6564-01 | E1 (S65) | Sibling ephemerides failed: DeltaT 3.99 d = 1 x catalogued P 3.9854 d (PC), +0.08 +/- 0.01 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-4398-01 | E1 (S66) | Sibling ephemerides failed: DeltaT -753.58 d = -131 x catalogued P 5.7525 d (APC), +0.02 +/- 0.01 h; diff image 11.2 arcsec off at 3.3 sigma | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-760-01 | E1 (S10) | Sibling ephemerides failed: DeltaT 12.35 d = 1 x catalogued P 12.3396 d (APC), +0.16 +/- 0.02 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-768-01 | E1 (S10) | Sibling ephemerides failed: the joint period equals the catalogued P 11.5294 d (APC), -0.09 +/- 0.03 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-450-01 | E1 (S5), E2 (S5) | Sibling ephemerides failed on both: the joint period equals the catalogued P 10.7149 d (APC), offsets within 0.13 h (sigma 0.99 h) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-4422-01 | E1 (S66) | Sibling ephemerides failed: DeltaT -746.06 d = -152 x catalogued P 4.9083 d (PC), -0.02 +/- 0.03 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-4427-01 | E1 (S40) | Sibling ephemerides failed: DeltaT -549.57 d = -119 x catalogued P 4.6183 d (PC), +0.03 +/- 0.01 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-2137-01 | E1 (S26) | Sibling ephemerides failed: the joint period equals the catalogued P 14.1503 d (APC), +0.04 +/- 0.01 h; diff image 132.7 arcsec off at 254 sigma | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-2613-01 | E1 (S68) | Sibling ephemerides failed: DeltaT 15.20 d = 1 x catalogued P 15.2011 d (PC), +0.06 +/- 0.04 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-3972-01 | E1 (S58) | Sibling ephemerides failed: the joint period equals the catalogued P 10.5114 d (PC), +0.05 +/- 0.01 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-1976-01 | E1 (S38) | Sibling ephemerides failed: the joint period equals the catalogued P 7.6943 d (APC), -0.10 +/- 0.01 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-2108-01 | E1 (S52) | Sibling ephemerides failed: DeltaT 20.41 d = 3 x catalogued P 6.8026 d (APC), +0.04 +/- 0.01 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-1351-01 | E1-E2 | Sibling ephemerides failed: the joint period equals the catalogued P 5.9294 d (APC); 3 same-CCD neighbours dip at the event | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-3501-01 | E1 (S37), E2 (S63) | Sibling ephemerides failed on both: the joint period equals the catalogued P 15.3503 d (APC) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-1457-01 | E1 (S17) | Sibling ephemerides failed: the joint period equals the catalogued P 6.3768 d (APC), -0.07 +/- 0.14 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-2031-01 | E1 (S52) | Sibling ephemerides failed: DeltaT -165.75 d = -29 x catalogued P 5.7156 d (PC), +0.11 +/- 0.12 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-1528-01 | E1 (S58) | Sibling ephemerides failed: the joint period equals the catalogued P 9.9385 d (APC), -0.15 +/- 0.03 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-2349-01 | E1 (S62) | Sibling ephemerides failed: the joint period equals the catalogued P 11.5738 d (APC), -0.01 +/- 0.03 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-1455-01 | E1 (S17), E2 (S17) | Sibling ephemerides failed on both: the catalogued P 3.6231 d's transits 521-522 periods before the reference; phase-0.5 dips at P 3.62/10.87 d are the EB's own harmonics | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-1019-01 | E1 (S34), E2 (S34) | Sibling ephemerides failed on both: the catalogued P 5.2341 d's transits one and two periods after the reference (+0.02 h at sigma 0.00 h) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-1461-01 | E1-E2 (S17) | Sibling ephemerides failed: the catalogued P 3.5686 d's adjacent transits (-0.02 +/- 0.01 h) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-1124-01 | E1 (S13) | Sibling ephemerides failed: DeltaT -1491.95 d = -424 x catalogued P 3.5188 d (APC); heavy in-window flags (planet-search exclude 93, manual exclude 54, SAP_BKG -25 sigma), diff image 16.4 arcsec off | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-1433-01 | E1 (S15) | Sibling ephemerides failed: DeltaT 24.87 d = 2 x catalogued P 12.4380 d (APC), -0.09 +/- 0.01 h; shape ratio 1.29, duration ratio 0.80, diff image 82.6 arcsec off at 146 sigma | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-6650-01 | E1 (S57) | Sibling ephemerides failed: DeltaT -711.55 d = -35 x catalogued P 20.3292 d (PC), offset -0.59 h inside the tolerance | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-1114-01 | E1 (S13) | Sibling ephemerides failed: DeltaT -2192.61 d = -881 x catalogued P 2.4888 d (APC), -0.05 +/- 0.02 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-527-01 | E1 (S6), E2 (S7) | Sibling ephemerides failed on both: the joint period equals the catalogued P 18.0892 d (APC); offsets +0.07/+0.01 h (σ 0.01 h) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-6036-01 | E1-E2 (S85) | Sibling ephemerides failed: the joint period 6.522 d is the catalogued P 6.5235 d (APC) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-4543-01 | E1 (S70), E2 (S70) | Sibling ephemerides failed: the joint period 5.7712 d is the catalogued P 5.7740 d (PC) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-4494-01 | E1 (S75) | Sibling ephemerides failed: the catalogued P 32.5350 d's next transit (+0.04 ± 0.02 h) | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-5379-01 | E1 (S47) | Sibling ephemerides failed: ΔT −356.68 d = −28 × catalogued P 12.7427 d (APC), +0.02 ± 0.02 h | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-5394-01 | E1 (S45) | Sibling ephemerides failed: the catalogued P 15.1935 d's transit one period before the reference (−0.07 ± 0.01 h) | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-5149-01 | E1-E7 (S41/S56/S75, …) | Sibling ephemerides failed on all events: the catalogued P 27.3715 d (PC) reproduces every event (ΔT 383.20 = 14 × P_cat, +27.37 = 1 × P_cat, +547.4 = 20 × P_cat, …) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-1059-01 | E1-E2 (S13) | Sibling ephemerides failed on both (ΔT 2192.32 d = 232 × P 9.4497 d and 2182.87 d = 231 × P_cat; the joint period equals the catalogued period exactly); E1's difference image is additionally 11.7″ off at 3.2σ | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-7610-01 | E1 (S99) | Sibling check passed (ΔT 634.62 d = 28.66 × P 22.1441 d — **not** an integer multiple; no catalogued ephemeris transit at the event); shape/red-noise/detrending/common mode pass; difference image 2.9″ from the OOT centroid (5.9σ bootstrap, below the 0.25-pixel = 5.25″ pass rule); Gaia neighbours **passed** after the re-vet with the now-fetched explorer field (no capable neighbour within 52 arcsec); pointing MOM_CENTR2 +5.9σ is the one flagged check | **Survives with a complete audit (Unverified lead).** 21 of 365 aliases data-allowed, none equal to the catalogued period; the +5.9-sigma MOM_CENTR2 excursion at the event is the residual caveat against the on-target difference image. |

| toi-447-01 | E1 (S5) | Sibling ephemerides failed: the catalogued P 5.5293 d's transit (offset +0.20 h within sigma 0.29 h) | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-764-01 | E1-E2 (S10) | Sibling ephemerides failed on both: the catalogued P 5.6317 d's transits; diff image 96.7 arcsec off at 26.9 sigma | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-7714-01 | E1 (S32), E2 (S98) | Sibling ephemerides failed on both: E1 = 73 periods before, E2 = 1 period after the catalogued P 24.7350 d (PC) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-890-01 | E1 (S33), E2 (S33) | Sibling ephemerides failed on both: the catalogued P 3.2023 d's transits 7 and 6 periods before the reference (sigma 0.01 h) | **Rejected: the lead events are the catalogued signal's own transits.** |
| toi-668-01 | E1 (S9) | Sibling ephemerides failed: the joint period equals the catalogued P 4.3787 d (APC), +0.50 h within sigma 0.73 h; the P 4.38 d phase-0.5 dip is the EB's own secondary | **Rejected: the lead event is the catalogued signal's own transit.** |
| toi-6022-01 | E1-E2 (S17) | Sibling ephemerides failed: the joint period equals the catalogued P 1.9281 d (PC), +0.08 +/- 0.01 h; diff images ~99 arcsec off (105 sigma) | **Rejected: the lead events are the catalogued signal's own transits.** |
## Systemic finding 2026-09-26: the batch pool's self-matches

The `colab-p01` queue was built from periodic PC/APC TOI rows, but the queue CSV carried **no period column**
(columns: name, tic, position, tmag, depth, duration, t0, disposition, rowupdate, score) — every spec got
`period_days: null` and a single-epoch veto, even though the TOI table already held catalogued periods for
these rows (row updates 2022-2026, all predating the 2026-09-26 build; verified live for TICs 144327080,
123898871, 158276040, 140760434, 219345200, 305767364, 121341000, 70797900). The runner therefore treated the
catalogued ephemeris's own transits in later sectors as repeat candidates. The vet's sibling-TOI ephemerides
check identifies every such event (predicted-transit coincidence within the accumulated ephemeris σ). Affected
leads are recorded above and reconciled to `pipeline_check` — the signals are real but are the catalogued
objects, not new candidates. A maintainer fix would re-query the TOI period at scaffold time (and/or extend the
veto to the folded ephemeris); it is recorded in `docs/STATUS.md`, not patched here.

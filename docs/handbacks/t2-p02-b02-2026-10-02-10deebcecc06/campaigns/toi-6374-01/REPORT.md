# T2 follow-up: toi-6374-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 4 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460438.6590: recovered, depth 9351 ± 473 ppm (catalogue 10846 ppm); BJD 2460443.2534: recovered, depth 11360 ± 567 ppm (catalogue 10846 ppm); BJD 2460447.8479: recovered, depth 10624 ± 623 ppm (catalogue 10846 ppm); BJD 2460457.0369: recovered, depth 8677 ± 615 ppm (catalogue 10846 ppm); BJD 2460461.6314: recovered, depth 9047 ± 541 ppm (catalogue 10846 ppm); BJD 2460466.2259: recovered, depth 9600 ± 476 ppm (catalogue 10846 ppm); BJD 2460470.8204: recovered, depth 9875 ± 600 ppm (catalogue 10846 ppm); BJD 2460475.4149: not recovered, depth 9615 ± 552 ppm (catalogue 10846 ppm); BJD 2460613.2498: not recovered, depth 11097 ± 665 ppm (catalogue 10846 ppm); BJD 2460617.8442: not recovered, depth 10635 ± 516 ppm (catalogue 10846 ppm); BJD 2460622.4387: not recovered, depth 10659 ± 513 ppm (catalogue 10846 ppm); BJD 2460627.0332: not recovered, depth 10949 ± 606 ppm (catalogue 10846 ppm); BJD 2460631.6277: not recovered, depth 11919 ± 506 ppm (catalogue 10846 ppm); BJD 2460640.8167: not recovered, depth 8488 ± 656 ppm (catalogue 10846 ppm); BJD 2460645.4112: not recovered, depth 10780 ± 522 ppm (catalogue 10846 ppm); BJD 2460650.0057: recovered, depth 11316 ± 622 ppm (catalogue 10846 ppm); BJD 2460654.6002: recovered, depth 10478 ± 711 ppm (catalogue 10846 ppm); BJD 2460659.1947: not recovered, depth 10305 ± 608 ppm (catalogue 10846 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 4, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 10%, 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 4 repeat-candidate event(s); first at BJD 2460435.0948, ΔT = 3.563 d, 0 of 3 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | not_tested | Worst defining-event pixel localization: no pixel localization was produced; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 4 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6374.01: Gaia DR3 538296944221523840 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-6374.01: dwarf priors not applied — 1.19 mag above (brighter: evolved, unresolved binary or young) the dwarf sequence at this colour; dwarf priors not applied |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6374.01: 28 Gaia neighbour(s) within 52.5", contamination 71.50%; depth 9351 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 538297528337075968, 50.8", ΔG -0.82); a centroid test is needed |
| Pointing and quality census per event | failed | 7 persistent event(s), 0 clean; BJD 2460435.0948 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+19.3, MOM_CENTR2 z=+6.0, POS_CORR1 z=+18.9, SAP_BKG z=+948.0; BJD 2460435.1546 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+19.4, POS_CORR1 z=+19.2, SAP_BKG z=+1491.2; BJD 2460435.2115 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+19.9, POS_CORR1 z=+18.7, SAP_BKG z=+1875.4; BJD 2460435.2601 suspect: scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+20.9, POS_CORR1 z=+18.4, SAP_BKG z=+2203.3 |
| Moving objects at screen-event epochs | passed | 7 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-6374.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6374.01: UCAC4 818-002803 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | failed | BJD 2460435.155: 20/273 event-free windows at least as deep; resolution 1/273, not a probability of zero; BJD 2460435.212: 245/269 event-free windows at least as deep; resolution 1/269, not a probability of zero; BJD 2460435.260: 192/273 event-free windows at least as deep; resolution 1/273, not a probability of zero |
| Event-depth injection-recovery | failed | BJD 2460435.155: 63/89 recovered; BJD 2460435.212: 19/90 recovered; BJD 2460435.260: 33/87 recovered |

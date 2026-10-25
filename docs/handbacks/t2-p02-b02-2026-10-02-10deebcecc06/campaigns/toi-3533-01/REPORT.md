# T2 follow-up: toi-3533-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 3 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2459797.9936: recovered, depth 10752 ± 476 ppm (catalogue 8360 ppm); BJD 2459802.3104: recovered, depth 9845 ± 480 ppm (catalogue 8360 ppm); BJD 2459806.6272: gap (catalogue 8360 ppm); BJD 2459810.9440: recovered, depth 10445 ± 490 ppm (catalogue 8360 ppm); BJD 2459815.2608: recovered, depth 9160 ± 499 ppm (catalogue 8360 ppm); BJD 2459819.5776: recovered, depth 10544 ± 618 ppm (catalogue 8360 ppm); BJD 2459823.8943: recovered, depth 11630 ± 568 ppm (catalogue 8360 ppm); BJD 2460341.9081: gap (catalogue 8360 ppm); BJD 2460346.2249: not recovered, depth 2595 ± 2123 ppm (catalogue 8360 ppm); BJD 2460350.5417: recovered, depth 9933 ± 493 ppm (catalogue 8360 ppm); BJD 2460354.8585: recovered, depth 10077 ± 534 ppm (catalogue 8360 ppm); BJD 2460359.1753: recovered, depth 8782 ± 551 ppm (catalogue 8360 ppm); BJD 2460363.4920: recovered, depth 10669 ± 475 ppm (catalogue 8360 ppm); BJD 2460536.1633: not recovered, depth 9687 ± 441 ppm (catalogue 8360 ppm); BJD 2460540.4801: not recovered, depth 10081 ± 471 ppm (catalogue 8360 ppm); BJD 2460544.7969: recovered, depth 9604 ± 519 ppm (catalogue 8360 ppm); BJD 2460549.1137: not recovered, depth 10133 ± 461 ppm (catalogue 8360 ppm); BJD 2460553.4304: partial, depth 9583 ± 474 ppm (catalogue 8360 ppm); BJD 2460557.7472: not recovered, depth 9894 ± 500 ppm (catalogue 8360 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, 3, 3.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 20%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 5 repeat-candidate event(s); first at BJD 2459820.3160, ΔT = 22.337 d, 0 of 22 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 104.2″ from the out-of-transit centroid (1.4σ bootstrap); 103.7″ from the catalogue position; -10% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-3533.01: Gaia DR3 2056621798082974592 at 0.04" (propagated 2016.0 → J2015.5; 0.05" unpropagated, proper-motion shift 0.01") |
| Stellar priors (Gaia colour and parallax) | inconclusive | TOI-3533.01: dwarf priors not applied — RUWE 72.37238 ≥ 1.4 (or missing): astrometry may be perturbed |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-3533.01: 111 Gaia neighbour(s) within 52.5", contamination 59.72%; depth 10752 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 2056621793787000704, 2.5", ΔG -0.19); a centroid test is needed |
| Pointing and quality census per event | failed | 5 persistent event(s), 0 clean; BJD 2459820.3160 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+5.5; BJD 2459820.3299 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+5.3; BJD 2459820.4028 caution: scattered light 2 (within ±0.25 d); BJD 2459824.2583 suspect: MOM_CENTR2 z=+11.3, POS_CORR1 z=-6.5, POS_CORR2 z=+12.2 |
| Moving objects at screen-event epochs | inconclusive | 5 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 1 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | inconclusive | 2 light curve × candidate pair(s); aliases supported: none; excluded: none; 22 alias test(s) without in-transit data |
| Variable-catalogue collision (VSX) | passed | TOI-3533.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-3533.01: ** TOI 3533B otype * (star_or_other) at 0.2" |
| Event-time prior art | inconclusive | 10 possible published-ephemeris overlap(s) within 1 d (TOI-3533.01, TOI-3565.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |
| Vetting difference-image localization (E1) | not_tested | no pixel localization was produced |
| Vetting difference-image localization (E2) | inconclusive | difference-image centroid 104.2″ from the out-of-transit centroid (1.4σ bootstrap); 103.7″ from the catalogue position; -10% of the deficit in the optimal aperture |
| Vetting difference-image localization (E3) | not_tested | no pixel localization was produced |
| Event-epoch null exceedance (k/N) | not_tested | BJD 2459820.316: 67/188 event-free windows at least as deep; resolution 1/188, not a probability of zero; BJD 2459820.330: 47/171 event-free windows at least as deep; resolution 1/171, not a probability of zero |
| Event-depth injection-recovery | not_tested | BJD 2459820.316: 38/74 recovered; BJD 2459820.330: 47/69 recovered |

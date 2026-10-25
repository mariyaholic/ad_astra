# T2 follow-up: toi-6614-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 6 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2460677.0758: gap (catalogue 12286 ppm); BJD 2460727.2178: recovered, depth 7704 ± 544 ppm (catalogue 12286 ppm); BJD 2460752.2888: recovered, depth 7212 ± 531 ppm (catalogue 12286 ppm); BJD 2460877.6438: recovered, depth 6868 ± 495 ppm (catalogue 12286 ppm); BJD 2460902.7148: recovered, depth 6749 ± 475 ppm (catalogue 12286 ppm); BJD 2460927.7858: partial, depth 8474 ± 596 ppm (catalogue 12286 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (3, 3, 3, 3, ≤2.5, 3; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0%, 10%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 5 repeat-candidate event(s); first at BJD 2460906.8159, ΔT = 179.589 d, 2 of 179 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data (179.589, 89.7946 d); duration likelihood under Gaia priors (circular orbits) peaks at 89.8 d (weight 1.00) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | inconclusive | Worst defining-event pixel localization: difference-image centroid 9.0″ from the out-of-transit centroid (0.3σ bootstrap); 88.7″ from the catalogue position; 9% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 6 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-6614.01: Gaia DR3 4660956856772302464 at 0.00" (propagated 2016.0 → J2015.5; 0.03" unpropagated, proper-motion shift 0.03") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-6614.01: Teff 5393 K, R* 0.91 ± 0.07, M* 0.94 ± 0.09, ρ* 1.23 ± 0.32 ρ☉ (dwarf sequence, M_G 5.09, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-6614.01: 119 Gaia neighbour(s) within 52.5", contamination 22.26%; depth 7704 ppm (measured depth of the recovered catalogued transit); 4 could produce it if fully eclipsed (brightest 4660956856772302592, 10.5", ΔG 4.56); a centroid test is needed |
| Pointing and quality census per event | failed | 6 persistent event(s), 0 clean; BJD 2460666.0270 suspect: scattered light 2 (within ±0.25 d), SAP_BKG z=+18.0; BJD 2460906.8159 suspect: manual exclude (in event), scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+10.4, MOM_CENTR2 z=+6.2, POS_CORR1 z=+13.6, POS_CORR2 z=+7.7, SAP_BKG z=+125.1; BJD 2460906.8881 suspect: manual exclude (in event), scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+8.2, MOM_CENTR2 z=+5.9, POS_CORR1 z=+13.8, POS_CORR2 z=+6.7, SAP_BKG z=+736.4; BJD 2460906.9145 suspect: manual exclude (within ±0.25 d), scattered light 2 (within ±0.25 d), MOM_CENTR1 z=+6.4, MOM_CENTR2 z=+5.8, POS_CORR1 z=+13.9, POS_CORR2 z=+5.7, SAP_BKG z=+978.0 |
| Moving objects at screen-event epochs | passed | 6 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin) |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-6614.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-6614.01: UCAC4 124-006704 otype PM* (star_or_other) at 0.9" |
| Event-time prior art | inconclusive | no 1-d published-ephemeris overlap in answered catalogue rows; missing ephemerides and TTVs remain untested |
| Vetting difference-image localization (E1) | inconclusive | difference-image centroid 9.0″ from the out-of-transit centroid (0.3σ bootstrap); 88.7″ from the catalogue position; 9% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | not_tested | BJD 2460906.816: 223/252 event-free windows at least as deep; resolution 1/252, not a probability of zero; BJD 2460906.888: 0/246 event-free windows at least as deep; resolution 1/246, not a probability of zero |
| Event-depth injection-recovery | not_tested | BJD 2460906.816: 26/90 recovered; BJD 2460906.888: 82/82 recovered |

# T2 follow-up: toi-2191-01

<!-- cygnus:generated-draft -->

Source: `p02-b02-2026-10-02` at `9250aee3b91d7da7d664681195a250ec85d8c43d`. Executed tier: T2.
Evidence remains **Unverified lead**. No T3/T4 execution or candidate promotion.

Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.
Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.

| Check | State | Note |
| --- | --- | --- |
| Product integrity (SHA-256) | passed | 3 product(s) verified; pinned checksums matched |
| Known-signal recovery (positive control) | passed | BJD 2459037.3497: recovered, depth 10319 ± 809 ppm (catalogue 14588 ppm); BJD 2459041.3612: recovered, depth 11361 ± 690 ppm (catalogue 14588 ppm); BJD 2459045.3728: recovered, depth 9027 ± 765 ppm (catalogue 14588 ppm); BJD 2459049.3843: recovered, depth 15480 ± 729 ppm (catalogue 14588 ppm); BJD 2459053.3958: recovered, depth 9039 ± 688 ppm (catalogue 14588 ppm); BJD 2459057.4074: recovered, depth 9949 ± 748 ppm (catalogue 14588 ppm); BJD 2460882.6578: gap (catalogue 14588 ppm); BJD 2460886.6693: not recovered, depth -74 ± 722 ppm (catalogue 14588 ppm); BJD 2460890.6809: not recovered, depth 734 ± 753 ppm (catalogue 14588 ppm); BJD 2460894.6924: gap (catalogue 14588 ppm); BJD 2460898.7040: not recovered, depth -17 ± 757 ppm (catalogue 14588 ppm); BJD 2460902.7155: not recovered, depth 1075 ± 752 ppm (catalogue 14588 ppm); BJD 2460906.7270: not recovered, depth -6479 ± 821 ppm (catalogue 14588 ppm); BJD 2461207.5925: not recovered, depth 1404 ± 757 ppm (catalogue 14588 ppm); BJD 2461211.6040: not recovered, depth -1277 ± 711 ppm (catalogue 14588 ppm); BJD 2461215.6156: not recovered, depth -50 ± 683 ppm (catalogue 14588 ppm); BJD 2461219.6271: gap (catalogue 14588 ppm); BJD 2461223.6387: not recovered, depth -1607 ± 736 ppm (catalogue 14588 ppm); BJD 2461227.6502: not recovered, depth 1078 ± 723 ppm (catalogue 14588 ppm); BJD 2461231.6617: partial, depth -84 ± 908 ppm (catalogue 14588 ppm) |
| Calibrated false-alarm threshold (sign-flip null) | passed | screen run at each light curve's own k* (≤2.5, ≤2.5, ≤2.5; ≤ 0 persistent null events outside the veto) |
| Synthetic signal injection–recovery | inconclusive | completeness for the reference box (2000ppm_4h) at each light curve's k*: 0%, 0%, 0% (pass mark 90%); 90%-completeness depths are in calibration.json |
| Catalogue cross-match | passed | 1 target(s) × 4 services, radius 30″; 4 answered, 0 errored; results in the ledger prior_art table |
| Period aliases (repeat events) | inconclusive | 34 repeat-candidate event(s); first at BJD 2459048.0863, ΔT = 10.736 d, 0 of 10 aliases P = ΔT/n ≥ 1 d allowed by the retrieved data ( d) |
| Alternative detrending | not_tested |  |
| Difference-image centroids / blend audit | failed | Worst defining-event pixel localization: difference-image centroid 140.6″ from the out-of-transit centroid (4.1σ bootstrap); 4.5″ from the catalogue position; 53% of the deficit in the optimal aperture; a blend census is a separate check |
| Pointing / jitter correlation | not_tested |  |
| Literature (ADS) audit | not_tested |  |
| Light-curve suitability for the residual screen | passed | 3 light curve(s) screenable |
| Target-to-Gaia identification (proper motion propagated) | passed | TOI-2191.01: Gaia DR3 6778500115933513088 at 0.00" (propagated 2016.0 → J2015.5; 0.00" unpropagated, proper-motion shift 0.00") |
| Stellar priors (Gaia colour and parallax) | passed | TOI-2191.01: Teff 5712 K, R* 1.06 ± 0.08, M* 1.03 ± 0.10, ρ* 0.87 ± 0.23 ρ☉ (dwarf sequence, M_G 4.47, no extinction) |
| Blend and dilution census (Gaia DR3 cone) | inconclusive | TOI-2191.01: 8 Gaia neighbour(s) within 52.5", contamination 7.97%; depth 10319 ppm (measured depth of the recovered catalogued transit); 2 could produce it if fully eclipsed (brightest 6778500012854297344, 17.9", ΔG 3.09); a centroid test is needed |
| Pointing and quality census per event | failed | 38 persistent event(s), 25 clean; BJD 2459047.6112 suspect: POS_CORR1 z=+6.5; BJD 2459048.0863 suspect: MOM_CENTR2 z=-6.1, POS_CORR1 z=+19.2, POS_CORR2 z=-10.6, SAP_BKG z=-84.7; BJD 2460886.5018 caution: manual exclude (within ±0.25 d); BJD 2460886.5094 caution: manual exclude (within ±0.25 d) |
| Moving objects at screen-event epochs | inconclusive | 38 event epoch(s) queried in SkyBoT (observer C57, r=600"); no known object bright enough within 63" plus its motion at any queried epoch (supports, does not prove, a non-asteroid origin); 9 epoch(s) not answered |
| Independent repetition (other MAST collections) | not_tested | no usable light curve from this instrument (Kepler/K2 answered, 0 light curve(s) within 4.0") |
| Independent-epoch confirmation (ZTF) | not_tested | no usable light curve from this instrument (ZTF answered, 1 light curve(s) within 3.0") |
| Variable-catalogue collision (VSX) | passed | TOI-2191.01: no VSX entry within 10" |
| Object-class guard (SIMBAD) | passed | TOI-2191.01: UCAC4 266-190884 otype * (star_or_other) at 0.1" |
| Event-time prior art | inconclusive | 33 possible published-ephemeris overlap(s) within 1 d (TOI-2191.01); inspect individual published mid-times/TTVs before candidate promotion; the screening tolerance does not prove identity |
| Vetting difference-image localization (E1) | inconclusive | difference-image centroid 91.8″ from the out-of-transit centroid (1.5σ bootstrap); 63.5″ from the catalogue position; 11% of the deficit in the optimal aperture |
| Vetting difference-image localization (E2) | inconclusive | difference-image centroid 7.3″ from the out-of-transit centroid (1.8σ bootstrap); 3.0″ from the catalogue position; 42% of the deficit in the optimal aperture |
| Event-time comparison vs published ephemerides | failed | E11: TOI-2191.01 (PC, P 4.0115 d, 14588 ppm) predicted -4.60 h ± 6.16 h; primary-literature/TTV review still required |
| Vetting difference-image localization (E3) | not_tested | no pixel localization was produced |
| Vetting difference-image localization (E4) | passed | difference-image centroid 1.6″ from the out-of-transit centroid (0.6σ bootstrap); 2.0″ from the catalogue position; 46% of the deficit in the optimal aperture |
| Vetting difference-image localization (E5) | passed | difference-image centroid 2.3″ from the out-of-transit centroid (1.4σ bootstrap); 5.4″ from the catalogue position; 38% of the deficit in the optimal aperture |
| Vetting difference-image localization (E6) | inconclusive | difference-image centroid 136.1″ from the out-of-transit centroid (2.0σ bootstrap); 4.6″ from the catalogue position; 47% of the deficit in the optimal aperture |
| Vetting difference-image localization (E7) | failed | difference-image centroid 140.6″ from the out-of-transit centroid (4.1σ bootstrap); 4.5″ from the catalogue position; 53% of the deficit in the optimal aperture |
| Vetting difference-image localization (E8) | inconclusive | difference-image centroid 139.6″ from the out-of-transit centroid (1.9σ bootstrap); 5.3″ from the catalogue position; 42% of the deficit in the optimal aperture |
| Vetting difference-image localization (E9) | inconclusive | difference-image centroid 9.9″ from the out-of-transit centroid (0.2σ bootstrap); 148.9″ from the catalogue position; 32% of the deficit in the optimal aperture |
| Vetting difference-image localization (E10) | inconclusive | difference-image centroid 9.0″ from the out-of-transit centroid (0.1σ bootstrap); 148.3″ from the catalogue position; 38% of the deficit in the optimal aperture |
| Vetting difference-image localization (E11) | failed | difference-image centroid 7.7″ from the out-of-transit centroid (8.0σ bootstrap); 147.7″ from the catalogue position; 17% of the deficit in the optimal aperture |
| Event-epoch null exceedance (k/N) | not_tested | not run: current vetting closed the tool route; event-identity review is required |
| Event-depth injection-recovery | not_tested | not run: current vetting closed the tool route; event-identity review is required |

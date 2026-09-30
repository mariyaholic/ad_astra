# HD 80133 / HIP 45621 CHIRON and legacy-RV access audit

**Screen date:** 2026-09-30. **Scope:** six-query public-source screen for individual CHIRON/RECONS spectra or RV epochs, California/Carnegie RV data, and a published component orbit for the exact TOI-2666 target. No credentials, observer contact, or bulk retrieval was used. This supplement does not infer which component produced a TESS event from the SB2 classification.

## Exact identity and source records

The exact target aliases are **TOI-2666.01 / TIC 170889511 / HIP 45621 / HD 80133 / RKS0917-0323**. The Hubbard-James thesis appendix gives the RKS identifier and HD 80133 name together with the approximate catalog position `09 17 55.3 -03 23 14`, parallax `30.980 mas`, and distance `32.28 pc`; the local Gaia mapping is source `3837451574150437120` at RA `139.4808681132`, Dec `-3.3875337972`. This identity agrees with the Zhang et al. HIP 45621/TOI-2666 entry and the local SIMBAD/Gaia record.

## Public CHIRON/RECONS material found

1. [Hubbard-James, *Spectral Characterization of a Complete Equatorial Sample of 615 K Dwarfs* (2023 thesis PDF)](https://www.astro.gsu.edu/RECONS/thesis.2023.james.pdf) is the primary observing record. Chapter 5 says the project created a library of exactly 600 CHIRON spectra and links the [public spectral-library site](https://hodarijames.github.io/spectral_library/page1.html). The target is explicitly listed as `RKS0917-0323 : HD 80133`, a newly identified SB2. The thesis states that the binary status comes from distinct double-line features in CHIRON, especially the Ca I 6717 Å feature, and that the 2.7 arcsec CHIRON fiber contains both stars.
2. The thesis supplies a reproducible **binary-identification observation**, but the target-specific material located in this screen contains no exposure dates/BJD, no per-exposure component velocities, no velocity uncertainties, no component flux-ratio time series, and no SB2 orbital fit. The thesis explicitly presents the result as a visual spectral-library discovery; it does not claim that the library yields an orbit for HD 80133.
3. The public [spectral-library landing page](https://hodarijames.github.io/spectral_library/page1.html) was reachable on 2026-09-30 and rendered only page/group headings in the archive text view. Its “Next Page” link to `page2.html` failed with a cache-miss in the available archival reader. No machine-readable target spectrum, FITS/ASCII download, epoch metadata, or RV table was exposed by the page during this bounded screen. This is an access limitation, not evidence that the underlying observing files do not exist.
4. The [GSU/SMARTS CHIRON publications index](https://www.astro.gsu.edu/~thenry/SMARTS/CHIRON.publications.html) lists Hubbard-James 2023 as a RECONS/SMARTS PhD data product and Paredes 2022 as a related radial-velocity-survey thesis. The index does not expose a target-specific HD 80133 epoch table or an orbit in the indexed entry. Direct page rendering was unavailable in this screen, so the listing is provenance only.

## Legacy California/Carnegie RV coverage

[Absil et al. 2021, A&A 651 A45](https://doi.org/10.1051/0004-6361/202140561), the primary interferometric detection paper, states that HD 80133 had been included in the California/Carnegie Planet Search programs (citing Valenti & Fischer 2005 and Takeda et al. 2007) but had **not** been identified as a binary from RV measurements. The authors give two possible explanations: very poor RV time coverage or an almost face-on orbit. They therefore do not provide individual legacy RV epochs, a published RV orbit, or an event-phase comparison for TOI-2666.

This statement is a negative coverage result with an explicit limitation. It cannot be read as a null RV test against the interferometric companion or the CHIRON SB2. The public source material located here also did not expose the California/Carnegie raw spectra or a target-specific epoch table. No component orbit was found in this bounded screen.

## Relation to the current Cygnus lead

The exact TESS/Cygnus times remain the local source-record values: reference BJD_TDB `2459259.15794` and E1 `2461049.16442`; Zhang et al. (2024) describe TOI-2666.01 as a single transit and report Keck/HIRES SB2 evidence with a 35 km/s separation, but neither that paper nor the CHIRON thesis publishes a time-matched orbit. The CHIRON thesis does not provide dates that can be compared with either event. Gaia DR3 source `3837451574150437120` has no RVS measurement and no `gaiadr3.nss_two_body_orbit` row in the exact-source refresh, so Gaia does not fill this gap.

**Result:** public primary material independently establishes that HD 80133 is an SB2, and it documents why the older California/Carnegie RV record cannot be treated as a binary non-detection. No public individual RV epochs or component orbit were located in this finite screen. The current event remains Unverified at event/source level. The next discriminating action is to obtain the underlying CHIRON/HIRES/legacy epoch products through their archive route, or acquire new phase-spread SB2 spectroscopy, then test all 52 aliases against an actual component orbit.

## Screen log

| Date | Source/query | Result |
|---|---|---|
| 2026-09-30 | Web search: HD 80133, HIP 45621, CHIRON, RECONS, Hubbard-James | Located thesis, CHIRON index, and Absil primary paper. |
| 2026-09-30 | Open Hubbard-James thesis; find `RKS0917-0323`, `HD 80133`, `observation date`, `Table 5.3` | Exact SB2 identity and spectral-window evidence; no target epoch table or observation-date text found. |
| 2026-09-30 | Open thesis around Chapter 5 and Appendix A | 600-spectrum library, RKS/HD identity, catalog position/parallax; no RV orbit. |
| 2026-09-30 | Open public spectral-library landing page and follow next-page link | Page 1 reachable; target-specific data not exposed in text; page 2 archival fetch failed with cache miss. |
| 2026-09-30 | Open Absil et al. primary PDF around HD 80133 discussion | California/Carnegie inclusion and poor-coverage/face-on caveat; no individual RV epochs or orbit. |
| 2026-09-30 | Open Zhang et al. primary PDF around Appendix A | Confirms HIP 45621/TOI-2666 identity and Keck/HIRES SB2 statement; no event-matched orbit. |


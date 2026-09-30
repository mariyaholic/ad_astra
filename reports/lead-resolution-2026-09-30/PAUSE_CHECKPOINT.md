# Safe pause checkpoint — 2026-09-30

The user explicitly requested a safe checkpoint and pause. The overall proof/disproof goal is **paused, not complete**. Three event interpretations remain Unverified; the two historical retractions remain closed. No analysis continues between interactions.

## Saved findings

Pinned R50G2 and K0 mask data from primary CCF repository commit `89ba7d5bbdfa7ef7332a2b1a5bfb9646504ac618` are recorded in `mask_manifest.json` with URLs, hashes and BSD license. No external code was executed. The independent integration excludes detector gaps over the entire Doppler grid, uses air Angstrom wavelengths and requires already-barycentric spectra. Saved `masked_spectra.json` and `ccf_alignment.json` retain the preceding reduction: five non-reference HARPS pipeline comparisons have R50G2 RMS **11.5937 m/s**, K0 **12.3714 m/s**, both failing the **10 m/s** requirement. This improves the prior167.945m/s extraction failure without validating FEROS orbital velocities. Failed profiles and boundary solutions remain recorded.

`feros_barycentric_audit.json` audits25 unique FEROS products with exact Gaia source rows, propagated coordinates, observatory headers and UTC start/mid/end exposure times. Builtin Astropy ephemeris and nonpredictive IERS rows were used. TOI3500 midpoint replacement deltas span approximately **−103 to +173 m/s**; start/end corrections differ by up to **36.77 m/s**. These are correction discrepancies, not stellar velocities. No replacement was applied. Photon weighting, optical correction cross terms and wavelength drift remain unresolved. [ESO release description94](https://www.eso.org/rm/api/v1/public/releaseDescriptions/94) warns that unsupervised reductions are not science-grade, low-precision barycentric correction is already applied, ERR is dummyNaN, and simultaneous-reference drift correction is absent. The [primary FEROS study](https://arxiv.org/abs/1307.5072) concerns other targets; its artifact amplitude is not assigned to these leads.

`koa_hires_archive.json` records five answered public Keck TAP queries. The TOI2666 coordinate box returns `HI.19981226.50823.fits`, `HI.20210223.23526.fits`, `HI.20210527.19968.fits`; exact-name selection returns zero. TOI224/3500 boxes return zero and the positive control one. Raw headers, epoch propagation and calibration are **not inspected**. Archive object strings are`k27`/empty, so these are possible data routes, not established additional target spectra. No Keck products were downloaded. [KOA tutorial](https://koa.ipac.caltech.edu/UserGuide/PyKOA/notebooks/PyKOA_HIRES_introduction.html) warns quick-look extractions are not for scientific analysis.

`CHIRON_ACCESS_AUDIT.md` retains the subagent's finite primary-source search. Published SB2 evidence supports stellar binarity of HD80133; no individual component RV series or solved eclipse orbit was recovered in that screen.

## Interrupted rerun and recovery contract

The final exact-covered-line-count weighting refinement computed profiles but failed saving `masked_spectra.json` with `OSError: [Errno22] Invalid argument`. Existing JSON remains parseable and retains the preceding reduction. The dependent CCF alignment command did not execute. **Current code includes a weighting refinement that saved numbers do not yet represent.** Do not treat them as a successful current-source run. Synthetic controls pass; this real-data rerun is pending.

First on resumption: inspect output persistence including possible temporary locking, preserve preceding JSON as history, then rerun `--mode masked-spectra --limit 53` and `--mode ccf-alignment`. Reuse cached originals/masks. Update both outputs, precision assessment and canonical records after successful save. A changed validation result is not an orbit confirmation.

Then screen three public KOA raw rows and associated calibration availability, starting with metadata/header sizes. Verify proper-motion-propagated source identity and iodine state before planning a science-grade reduction. No private account, outreach or observing campaign is authorized by this checkpoint.

Remaining gates: component/eclipse orbit identity for224/2666; source/activity/orbit discrimination for3500; S107 same-CCD/pointing/moving-object controls; search-wide noise/selection calibration. No discovery is asserted.

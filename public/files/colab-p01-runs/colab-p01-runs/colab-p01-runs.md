# Colab batch colab-p01: standardized run record

Maintained: 2026-09-26 (UTC). This page is the publication record of the first Colab stress batch
(`colab-p01`, the first 100 of 1,000 queued periodic PC/APC TOIs). It exists so the run can be
inspected through the same site mechanisms as every other dataset: a sanitized product manifest,
the run journal as a downloadable CSV, and the batch summary — without merging the companion
ledger into the project's local provenance ledger.

## Provenance chain

- **Code:** pinned commit `2b65d44` (public repository), cloned on the Colab runtime; test gate
  passed there before the batch ran (Python 3.13.15, CPU High-RAM: 8 vCPU / 51 GB RAM, `--jobs 7`).
- **Run window:** 2026-09-26 09:52:44Z – 10:43:14Z; batch wall time 3,088.7 s; exit 0.
- **Storage:** checkpoint under Google Drive `Cygnus/colab_runs/colab-p01/` — 3,330 objects,
  982.2 MiB — indexed in `storage/locations.jsonl` with the manifest SHA-256
  `5dc41ce7…a0ffdaa`.
- **Verification:** all 3,327 manifest-listed files hash-match (`rclone hashsum sha256`, 0
  mismatches); all 100 executed specs byte-match the committed specs; all 387 product SHA-256s
  inside the sky records match the Drive files.

## Runs

The journal holds **1,107 runs: 1,100 completed, 7 aborted**. The 7 aborts are one mid-run
interrupt (2026-09-26 10:25:47Z, when the batch was cut to 100 targets); every interrupted step was
re-run and completed (84 campaigns in pass 1 + 16 on resume = 100/100, 0 failed). Per-campaign
step counts: 11 canonical steps × 100 campaigns, no missing steps, no step-order violations.

The downloadable CSV is the companion ledger's `runs` table projected through the site's own
public-run allowlist (id, script, config_hash, code_version, seed, started_utc, finished_utc,
status, summary). The companion ledger itself is archived beside the batch on Drive and is
**never merged** into the local ledger; these run ids are therefore companion-ledger ids
(`cygnus_multi:<campaign>:<step>`), stated here rather than hidden.

## Products

The 387 products are public NASA TESS SPOC 120-s light curves (MAST), held on Drive and
checksum-verified. They are presented as the site's standard sanitized manifest
(`archive_manifest` view): per-product state, bytes, SHA-256, and the public MAST download link.
They are **linked, never re-hosted**.

## What this page does not claim

- No science conclusions belong to this page; outcomes live in the campaign records and the
  [tess-periodic-01 collection](/collections/tess-periodic-01/).
- Compute units consumed were not read from Colab's Resources panel (user-side check); no rate is
  quoted.
- The 900 remaining queued targets have not been run.

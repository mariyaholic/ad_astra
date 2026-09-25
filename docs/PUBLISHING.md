# Publishing the Cygnus public repository site

Maintained: 2026-09-24 (UTC). Code: `src/cygnus/publish/`. Tests: `tests/test_publish.py`.

## What it is

A static website generated from **curated publication manifests** plus a
**read-only** view of the provenance ledger. There is no server-side code in
production, no upload path, and no login: publishing is an edit to files in
`publish/`, reviewed like code, followed by a rebuild.

```
publish/collections/*.json ─┐
publish/site.json           │    python -m cygnus.publish build     build/site/
publish/pages/methods.md    ├──────────────────────────────────▶   (static HTML, CSS, JS,
publish/data/** (snapshots) │   • validate manifests                 downloads, catalog.json)
AGENTS.md etc. (allowlisted)│   • confine sources, redact text
state/ledger.sqlite (mode=ro)┘  • render, then leak-scan output
```

Why static: the project's source of truth stays the ledger and the worktree;
the site adds no database and no second copy of scientific logic. Candidate
pages call the package's own `CandidateRecord.validate_strict()` and
`emit_dossier_markdown()`, and rank with `reporting.leads_board`'s ordering.

## Setup

```bash
python -m venv venv
venv/Scripts/python -m pip install -e ".[site,test]"
```

The existing science venv under the scratch root (see `ANALYSIS_STACK.md`)
already has `jinja2` and `pyyaml`. Without installing,
prefix commands with `PYTHONPATH=src`.

Environment variables (all optional):

| Variable | Default | Used for |
| --- | --- | --- |
| `CYGNUS_LEDGER` | `state/ledger.sqlite` | ledger opened read-only at build |
| `CYGNUS_SCRATCH` | the scratch root | `snapshot` default pack root; `check` dry-build location |

No credentials are needed or read. The site never touches the Drive remote.

## Commands

```bash
python -m cygnus.publish check                  # validate + dry build into scratch; prints what would be public
python -m cygnus.publish build                  # writes build/site/
python -m cygnus.publish serve --port 8765      # preview on 127.0.0.1 only
python -m cygnus.publish snapshot --name tier1-pack   # scratch pack manifests -> publish/data/tier1-pack/
python -m cygnus.publish withdraw <id> --reason "..."
```

Exit code 2 means a publication rule was violated; the message lists every
problem. A failed leak scan deletes the partial output.

## What is public and what stays private

| Public (only when listed in a published collection) | Always private |
| --- | --- |
| Rendered project docs (private paths redacted) | `state/ledger.sqlite` as a file or table dump |
| Campaign specs | Scratch and staging storage, bulky downloads |
| Sanitized manifest snapshots (IDs, checksums, queries, outcomes) | Drive remote contents, rclone config, OAuth tokens |
| Chosen ledger runs / run logs (allowlisted fields) | `local_path`, `extra_json`, unlisted runs, measurements, candidates |
| Candidate dossiers that pass `validate_strict` | Draft collections; restricted items; anything not listed |
| Ledger **totals** on home/candidates pages | E-mail addresses, absolute paths |

Third-party archive products are **linked, never re-hosted**. An item with
`origin: third_party` cannot set `download: true` unless it also sets
`redistribution_ok: true`, which you should do only after checking and
recording the archive's redistribution terms.

## Adding a collection (no page markup needed)

1. Create `publish/collections/<id>.json`. The file name must equal `id`, a
   lowercase slug; it becomes the permanent URL `/collections/<id>/`.
2. Start with `"status": "draft"`, run `check`, then switch to `"published"`
   with a `published` date.
3. Rebuild and deploy.

```json
{
  "id": "example-collection",
  "title": "Human title",
  "type": "dataset",
  "status": "draft",
  "published": null,
  "summary": "One or two sentences shown in listings.",
  "description_md": "Optional longer Markdown (redacted on render).",
  "research_status": "e.g. Engineering baseline · not a scientific result",
  "license": null,
  "citation": null,
  "related": ["document:analysis-stack", "campaign:tess-mono-01", "collection:other-id"],
  "items": [
    {"id": "readme", "kind": "document", "source": "SOME_DOC.md", "download": true},
    {"id": "table", "kind": "file", "source": "publish/files/table.csv", "download": true, "origin": "derived"},
    {"id": "pending", "kind": "file", "source": "publish/files/x.zip", "access": "restricted",
     "access_note": "Why it is listed but not public."}
  ]
}
```

`type`: `documents | dataset | campaign | software | candidates | measurements`.

| `kind` | `source` must be under | Renders |
| --- | --- | --- |
| `document` | worktree top level, `publish/pages/`, `docs/` (`.md`) | `/documents/<item-id>/` |
| `campaign` | `campaigns/` (`.yaml`) | `/campaigns/<campaign>/` with step status from the module register |
| `archive_manifest` | `publish/data/` (snapshot `.json`) | product table, state bar, verbatim queries |
| `ledger_run` | — (`params.run_id`) | run + measurements + product resolution |
| `ledger_runs` | — (`params.script`) | run table in `/log/` |
| `module_register` | worktree top level (`.md`, `params.heading`) | status table |
| `candidate` | `publish/candidates/` (CandidateRecord `.json`) | `/candidates/<CYG-id>/` + generated dossier |
| `file` | `publish/files/` (allowlisted extensions, ≤ 50 MB) | download with sha256 |

Missing metadata is left `null`; pages show "not recorded". Do not fill in
guesses to make a page look complete.

### Publishing a candidate

Save the record with `CandidateRecord.save("publish/candidates/CYG-….json")`.
The build refuses the record if: `validate_strict()` fails (e.g. evidence above
`unverified_lead` while any audit item is not `passed`); its evidence level
differs from the ledger's `candidates` row; it claims `established`; or its ID
contains `/`. Prior-art rows and measurements come from the ledger.

## Withdrawing content

```bash
python -m cygnus.publish withdraw <id> --reason "Superseded by <id2>"
python -m cygnus.publish build
```

The collection keeps its URL as a dated notice; its item pages and files are
not generated. **Rebuild and redeploy** — withdrawal takes effect on the host
only when the new build replaces the old one (use a deploy that deletes files
absent from the build, e.g. `rsync --delete` or a fresh Pages deployment).
Withdrawal does not delete anything in the worktree, ledger, scratch or Drive.
Setting `"status": "draft"` instead removes the URL entirely (404).

## Refreshing snapshots

Scratch is disposable, so manifests are copied into `publish/data/` with
`snapshot`. It drops non-allowlisted fields, redacts free text, reduces
upload-verification notes to a neutral sentence, and records the source
manifest's sha256 and modification time. Re-run it after a pack changes and
review the diff before rebuilding.

## Deployment

`build/site/` is a self-contained static tree. Any static host works
(GitHub Pages, Cloudflare Pages, Netlify, S3 + CDN, nginx). Set `base_path` in
`publish/site.json` if serving from a sub-path. Recommended response headers
(the preview server already sends them):

```
Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer
Content-Disposition: attachment   (for /files/*)
```

Serve `404.html` for missing paths. The pages load no third-party resources.

**The published site (since 2026-09-25)** is the bundle from `tools/build_pages_bundle.py`: the sky
explorer (`design-system/mockups/explorer/`) is the home page at `/`, and every other path is this
generator's output, whose own home page is also written to `/about/`. Old `/preview/…` links
redirect to `/` (`_redirects`). Build and deploy by hand (not connected to git):

```bash
python design-system/mockups/fetch_sky_data.py --missing   # Gaia field + survey image for new targets (network)
python design-system/mockups/build_explorer.py
python -m cygnus.publish check && python -m cygnus.publish build
python tools/build_pages_bundle.py                          # leak-scans the whole bundle
npx wrangler@4 pages deploy build/pages --project-name cygnus-sky --branch main
```

## Storage, backup, retention

- Build output is small (≈ 1 MB today) and fully reproducible; do not back it up.
- Back up `publish/` with the worktree: it is the publication record.
- The site never stores uploads; there is nothing on the host to back up.
- Removal: withdraw (tombstone) or delete the collection file (404), rebuild,
  redeploy. External caches or archives of earlier builds may persist.

## Verification record (2026-09-24)

- `pytest`: 95 passed (42 existing + 53 publication tests), 2 network tests deselected (2026-09-24 record; the current gate is 188 passed, 2 deselected as of 2026-09-25).
- Built 16 pages and 24 public files; leak scan clean; checked in a browser at
  `http://localhost:8765/` in light and dark themes at desktop and 375 px width
  (no horizontal page overflow), keyboard order (skip link → nav → filters),
  and the repository filter with URL sync.
- Token contrast: every text/background pair ≥ 4.5:1 in both themes.

## Design system

The site's visual and verbal rules are documented as the **Ad Astra** design
system: source files in `design-system/project/` (brand book `README.md`,
`tokens.json`, one README + preview per component) and a browsable copy at
https://claude.ai/artifact/KwjsvzHFkTnBphVwdY1mxz (private; reachable only from Claude, so treat
`design-system/project/` as the source of truth).
`site.css` remains the implementation; token names match its custom
properties. When a token or component changes in `site.css`, update the design
system in the same change.

## Known data issues surfaced by the site

- Ledger measurements from run #1 cite product `tesscut-219.7570--80.5310-sec12`,
  but the ledger product row is `…-sec12-cam3-ccd1`. Shown as **unresolved**.
- Several `cygnus.ingest.tier1` runs are `open` (no close recorded).
- The ledger is still being written by ingest jobs; home-page totals are as of
  each build.
- The project is licensed Apache-2.0 (set on every collection). The source
  archive in `cygnus-software-0-1-0` is still restricted until the user decides
  to publish it (see `docs/STATUS.md`).

# Where Cygnus data lives

Every CLI, harness and notebook finds stored Cygnus data the same way: **`storage/locations.jsonl`** in this repository. It is one JSON object per location, in git, so every harness can read it whatever its Drive access. `python -m cygnus.storage list` prints it with links.

```bash
python -m cygnus.storage where            # how THIS harness reaches the Drive folder Cygnus/
python -m cygnus.storage list             # every recorded location: link, writer, who can see it
python -m cygnus.storage check [ID]       # record whether this harness can see a location
python -m cygnus.storage upload LOCAL batches/<id> --kind batch --producer "…"   # copy, verify, record
python -m cygnus.storage add LOCATION.json   # record an entry another runtime wrote (e.g. Colab)
```

## Rules

1. **Name locations by their path inside `Cygnus/`**, e.g. `colab_runs/<batch>`, never by an rclone remote name. Remote names are local configuration: this workstation's Claude Code harness has `gdrive:`, another harness has `cygnus:`, and Colab mounts `/content/drive/MyDrive`. Each harness resolves `Cygnus/` itself, in this order:
   1. `$CYGNUS_DRIVE`: an rclone spec (`gdrive:Cygnus`) or a directory (`/content/drive/MyDrive/Cygnus`, `G:/My Drive/Cygnus`);
   2. the Colab mount;
   3. the first rclone Drive remote that has a `Cygnus/` folder.
2. **Every location gets an index entry**, and the same entry sits beside the data as `LOCATION.json`. An entry records:
   - kind, writer and producer (notebook, batch id, harness);
   - the pinned commit;
   - the SHA-256 of its `MANIFEST.sha256` and the file count;
   - links:
     - `folder` opens the exact Drive folder when its ID is known;
     - `search` is a Drive search for the folder name, which works in any browser for the account owner;
   - `visible_via`: each access route that was checked, with `visible` / `not_visible` and the date;
   - the local copy, only scratch-relative (`scratch:…`), never a machine path.
3. **Visibility is observed, never assumed.** A token with the `drive.file` scope sees only files created by the same OAuth app. Folders a Colab `drive.mount()` writes are therefore **invisible to this workstation's rclone token**: `rclone cat` exits 3, directory not found (checked 2026-09-26). A harness with a broader token does see them. Run `check` in each harness and commit the result.
4. **One writer kind per area**, so a logical path always means one folder:

   | Area | Written through | Holds |
   |---|---|---|
   | `colab_runs/` | a mounted folder (Colab `drive.mount()`) | Colab batch evidence: companion ledger, journal, reports, manifest |
   | `batches/` | rclone | workstation batch state: journal, summary, logs, ledger snapshot |
   | `data/` | rclone | archive packs (`data/tier1/`) |

   A `drive.file` token that wrote into `colab_runs/` would create a second folder of the same name beside Colab's (Drive allows duplicates). `cygnus.storage upload` refuses that.
5. **Uploads are verified from Drive's side**: after the copy, every file's SHA-256 is read back through the same route and must match the manifest. Only then is the entry written.
6. **Nothing outside `Cygnus/`** is read, written or deleted (AGENTS.md). Credentials never go into an entry, a manifest, a log or a commit.

## Links in a public repository

The repository is public, so folder IDs in the index are visible to anyone. A folder link opens only for accounts the folder is shared with. Nothing in `Cygnus/` is shared, so a link reveals that a folder exists, not what is in it. If that is unwanted, drop `drive_folder_id` and keep the `search` link, which contains only the folder name.

## Current locations (2026-09-26)

See `python -m cygnus.storage list`:
- the three workstation batches (`batches/nss-2026-09-26`, `batches/regen-2026-09-26`, and `batches/suite-2026-09-26` with a ledger snapshot);
- the Tier-1 pack (`data/tier1`, 149 files);
- the Colab equivalence pilot (`colab_runs/equiv-colab-2026-09-26`). Its folder is not visible to this workstation's `gdrive:` token, and a verified copy is in scratch.

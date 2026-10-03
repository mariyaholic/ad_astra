# Colab output sync and tier marks

The post-run sky record determines which tools a target has earned. The historical
`p02-b02-2026-10-02` board was calculated before execution; its T0 entries describe
the starting state. Its 99 saved checkpoints retain `run_at: T0`.

Use the tier policy in `src/cygnus/campaign/tiers.py`; never assign tiers by editing
a queue CSV or use T2 eligibility as a vetted-candidate evidence claim.

```bash
python -m cygnus.colab_sync --run p02-b02-2026-10-02 --update-notes
```

The command resolves the route through `cygnus.storage`, stays under
`Cygnus/colab_runs/<run>/`, and downloads only LOCATION, manifest, board, done,
sky records and rejection notes. It reuses cached files when their SHA-256 agrees
with the current manifest. Raw products and companion ledgers remain separate.
On a mounted Drive route the same command works without rclone.

For an already retrieved packet, pass `--local <packet-directory>` to audit
offline. Omit `--update-notes` for a read-only preview.

The manifest digest must agree with LOCATION, and every tier input must agree
with its manifest hash. The board and LOCATION must identify the same run and
commit. Unknown check names, missing listed inputs, unsafe paths, mismatched
identities and checksum failures stop the audit before STATUS is updated.
These checks establish source-package consistency, not independent scientific
validation or authenticity of a signed release. No heavy-tier budget is assumed.

Outputs are `docs/colab_runs/<run>/TIER_MARKS.json` and `TIER_MARKS.md`, with all
requested targets retained, including missing/incomplete ones. STATUS changes
are limited to a run-specific managed block; manual decisions remain intact.
Repeated identical runs produce identical marks and notes. The source records,
draft markers, evidence labels and companion ledger are not overwritten.

The official `notebooks/cygnus_lead_colab.ipynb` now refreshes earned tiers from
the newly written sky record at each checkpoint. `run_at` retains the actual tier
selected for execution. This change applies when the notebook runs a new commit
containing `cygnus.colab_sync`; a notebook pinned to an older commit does not
receive it automatically. A T0 run that earns T2 still needs a subsequent T2
execution; the checkpoint refresh does not run pixel vetting.

## Canonical scheduler — agents must reuse it

**Windows Task Scheduler owns this workflow.** The one canonical task is
`\Cygnus-Colab-Sync`, registered on the workstation on 2026-10-03. It runs daily
at **09:00 local UTC+08:00 (Asia/Manila)**. The former Codex heartbeat
`cygnus-colab-tier-sync` is **PAUSED**, superseded by this task.

**Do not create another Codex automation, per-batch Windows task, startup helper,
or separate scheduled script for this sync.** Inspect the canonical task first;
update it in place if a change is authorized. New exports are discovered by the
same task automatically. Task identity is the root task path `\` plus the exact
name `Cygnus-Colab-Sync`; folder/run names are not scheduler identities.

The action runs the detected `pythonw.exe` directly, with the repository as its
working directory, using:

```bash
python -m cygnus.colab_sync --all --update-notes --log state/colab_sync/latest.json
```

`--all` lists direct folders inside `Cygnus/colab_runs`, identifies tiered packets,
skips legacy folders without a board, reports incomplete packets as errors, and
compares LOCATION manifest hashes with existing marks to skip unchanged runs.
Verified new/changed exports get tier marks, managed STATUS blocks and storage
index entries. Errors produce a nonzero task result and a JSON result log; no
scientific promotion is inferred from an incomplete upload.

The task runs without Codex and without an authenticated Colab browser. It uses
the existing signed-in user's rclone configuration; no password or new Drive
credential is stored. Windows sign-in must remain active (a locked session is
fine). Codex may be fully quit. A powered-off PC cannot run it. WakeToRun and
StartWhenAvailable are enabled, but actual wake requires permitted Windows and
hardware wake timers; wake-from-sleep was not physically tested. The task retries
twice at 15-minute intervals after failure, has a one-hour execution limit, and
ignores overlapping scheduled instances. Both Python and all rclone subprocesses
run without console windows (`pythonw.exe` plus Windows `CREATE_NO_WINDOW`). The
initial live check exposed child-console flashes; the launcher was corrected
and covered by a Windows regression test before final scheduler verification.

Inspect or trigger the existing task in PowerShell:

```powershell
Get-ScheduledTask -TaskName 'Cygnus-Colab-Sync' -TaskPath '\'
Get-ScheduledTaskInfo -TaskName 'Cygnus-Colab-Sync' -TaskPath '\'
Start-ScheduledTask -TaskName 'Cygnus-Colab-Sync' -TaskPath '\'
Get-Content -LiteralPath 'state/colab_sync/latest.json'
```

The reproducible, idempotent registration tool is
`tools/register_colab_sync.ps1` (`Get-Help` describes it; `-VerifyOnly` inspects).
It detects Python, rclone and the repository directory, and registers the same
task name with `-Force`. If the PC's time zone changes, review the 09:00 trigger.
Do not run a manual writer while the scheduled task is active. The task writes
local repo notes only: no commits, pushes, publication, ledger merge or science.
It logs results rather than sending Codex notifications. History and private
runtime logs stay under ignored `state/`; repo documentation records ownership.

Live verification on 2026-10-03: the corrected Windows task completed with
`LastTaskResult: 0` and JSON `exit_code: 0`, no errors, two unchanged exports
and three skipped probe/legacy folders. This exercised the scheduled Pythonw
action, existing Drive credentials, automatic discovery and result logging.
The earlier run discovered and marked `smoke-2026-10-01` (three T2-eligible
targets); its record checks remain a gate audit, not completed scientific review.

Validation: `python -m pytest -q`. Focused regressions live in
`tests/test_colab_sync.py`: post-run promotion from a stale starting board,
missing/incomplete targets, corrupt inputs, unsafe manifest paths, idempotent
notes and notebook checkpoint refresh.

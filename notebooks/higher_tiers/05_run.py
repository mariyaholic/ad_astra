# Target-level resumability: completed byte-verified targets skip, failed targets retry.
# Each checkpoint produces a scheduler-compatible export. Source and reviewed campaigns are read-only.
import traceback
open_run(RUN_DIR, CONTRACT)
LEDGER_PATH = REPO_DIR / 'state' / f'{RUN_ID}.sqlite'
LEDGER_PATH.parent.mkdir(exist_ok=True)
if (RUN_DIR / 'ledger.sqlite').is_file():
    with sqlite3.connect(RUN_DIR / 'ledger.sqlite') as saved_db, sqlite3.connect(LEDGER_PATH) as active_db:
        saved_db.backup(active_db)
for target_index, target_id in enumerate(ELIGIBLE, 1):
    print(f'[{target_index}/{len(ELIGIBLE)}] {target_id}', flush=True)
    if completed_target(RUN_DIR, target_id):
        print('  resumed: verified completed checkpoint; skipped', flush=True)
        continue
    error_path = RUN_DIR / 'errors' / f'{target_id}.json'
    try:
        target_result = run_target(SOURCE_DIR, SOURCE_AUDIT, target_id, SOURCE_SPECS[target_id], REPO_DIR, RUN_DIR, null_params=NULL_PARAMS)
        if error_path.exists():
            error_path.unlink()
        print('  checkpointed; earned:', target_result['earned'], '| evidence not promoted', flush=True)
    except Exception as exc:
        atomic_write_json(error_path, {'target': target_id, 'state': 'failed', 'error': repr(exc), 'traceback': traceback.format_exc()})
        print('  FAILED, retained for retry/review:', repr(exc), flush=True)
    print('  verifying checkpoint export on Drive; do not interrupt this write', flush=True)
    export_run(RUN_DIR, CONTRACT, SOURCE_AUDIT, ELIGIBLE, EXCLUDED, REPO_DIR)
print('Target loop finished. Read the final summary: loop completion does not mean all targets passed.')

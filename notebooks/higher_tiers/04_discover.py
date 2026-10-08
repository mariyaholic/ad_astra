# Read stage one in place. No bulk product downloads during this step.
print('Discovering and checksum-verifying the first-stage export; progress follows below.', flush=True)
SOURCE_DIR, SOURCE_AUDIT, ELIGIBLE, EXCLUDED = select_source(CYGNUS_ROOT, SOURCE_RUN)
CONTRACT = run_contract(SOURCE_AUDIT, NOTEBOOK_REVISION, PINNED_COMMIT, ELIGIBLE, null_params=NULL_PARAMS)
CONTRACT_DIGEST = hashlib.sha256(json.dumps(CONTRACT, sort_keys=True).encode('utf-8')).hexdigest()[:12]
RUN_ID = 't2-' + SOURCE_AUDIT['run'] + '-' + CONTRACT_DIGEST
RUN_DIR = CYGNUS_ROOT / 'colab_runs' / RUN_ID
print('Source:', SOURCE_AUDIT['run'], '| checkpointed:', SOURCE_AUDIT['checkpointed'], '/', SOURCE_AUDIT['requested'])
print('Re-derived tiers:', SOURCE_AUDIT['counts'], '| T2 targets:', len(ELIGIBLE), '| excluded:', len(EXCLUDED))
print('Output/resume:', 'Cygnus/colab_runs/' + RUN_ID)
SOURCE_SPECS = {}
FIRST_STAGE_BYTES = 0
SOURCE_ENTRIES = read_manifest(SOURCE_DIR / 'MANIFEST.sha256')
for target_index, target_id in enumerate(ELIGIBLE, 1):
    source_spec = subprocess.run(['git', '-C', str(REPO_DIR), 'show', SOURCE_AUDIT['commit'] + ':campaigns/' + target_id + '.yaml'], capture_output=True, text=True, check=True).stdout
    SOURCE_SPECS[target_id] = source_spec
    source_products = checked_json(SOURCE_DIR, SOURCE_ENTRIES, f'campaigns/{target_id}/runner/fetch_products.json')['result']['products']
    FIRST_STAGE_BYTES += sum(int(item['bytes']) for item in source_products.values())
    print(f'  {target_index}/{len(ELIGIBLE)} {target_id}: source spec found; {len(source_products)} exact LC products', flush=True)
print(f'Exact LC inputs: {FIRST_STAGE_BYTES / 1e6:.1f} MB if re-fetched; additional TPF/neighbour downloads are archive-dependent.')
print('Resource plan: one target at a time, one target light-curve set in memory; FITS stay in VM scratch.')
print('Pixel-vetting time depends on event count, archive latency, and alias count; no whole-batch ETA is asserted.')
if not ELIGIBLE:
    print('NO ELIGIBLE TARGETS: this is a valid empty follow-up, not a reason to bypass the gates.')

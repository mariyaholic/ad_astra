# Shared, notebook-embedded orchestration. Science stays in the existing campaign tools.
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import math
import re
import shutil
import sqlite3
import subprocess  # noqa: F401 - shared namespace for later notebook cells
import sys
from pathlib import Path, PurePosixPath

from cygnus.colab import build_manifest, read_manifest, sha256_file, write_manifest
from cygnus.colab_sync import audit
from cygnus.fileio import atomic_write_json, atomic_write_text
from cygnus.campaign.tiers import decide, rank, require_tier, unmapped_checks

PRODUCER = 'notebooks/cygnus_higher_tiers_colab.ipynb'
FIRST_STAGE = 'notebooks/cygnus_lead_colab.ipynb'
SPECIALIST_LEADS = {'toi-224-01', 'toi-2666-01', 'toi-3500-02', 'toi-7610-01'}


def safe_id(value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', value):
        raise ValueError(f'unsafe identifier: {value!r}')
    return value


def select_source(drive_root, requested='latest'):
    # Only a finalized first-stage export can feed this stage. Never ingest our own outputs.
    root = Path(drive_root).resolve()
    exports = root / 'colab_runs'
    if requested != 'latest':
        choices = [exports / safe_id(requested)]
    else:
        choices = sorted(p for p in exports.iterdir() if p.is_dir() and not p.is_symlink())
    candidates = []
    for directory in choices:
        if not (directory / 'LOCATION.json').is_file() or not (directory / 'tier_board.json').is_file():
            if requested != 'latest':
                raise ValueError(f'{directory.name}: first-stage export is not finalized')
            continue
        location = json.loads((directory / 'LOCATION.json').read_text(encoding='utf-8'))
        if location.get('producer') != FIRST_STAGE:
            if requested != 'latest':
                raise ValueError('SOURCE_RUN must identify the first-stage lead notebook, not a follow-up')
            continue
        board = json.loads((directory / 'tier_board.json').read_text(encoding='utf-8'))
        timestamp = datetime.fromisoformat(board['utc'].replace('Z', '+00:00'))
        if timestamp.tzinfo is None:
            raise ValueError(f'{directory.name}: source UTC must include its time zone')
        candidates.append((timestamp, directory.name, directory))
    if not candidates:
        raise ValueError('No finalized first-stage lead export under Cygnus/colab_runs. Finish/export stage one first.')
    source = max(candidates)[2]
    if not source.resolve().is_relative_to(root) or source.is_symlink():
        raise ValueError('source escaped the mounted Cygnus root')
    result = audit(source)  # checksum failure in the newest packet STOPS; never silently choose an older one
    eligible, skipped = [], {}
    for cid, row in result['targets'].items():
        if cid in SPECIALIST_LEADS:
            skipped[cid] = 'specialist/frozen lead: follow LEAD_PURSUIT_PLAN_2026-09-27.md'
        elif row['checkpointed'] and row.get('status') == 'completed' and rank(row['tier']) >= rank('T2'):
            eligible.append(cid)
        else:
            skipped[cid] = '; '.join(row['blockers']) or f"tier {row['tier']}; not a completed T2 checkpoint"
    return source, result, eligible, skipped


def run_contract(source_audit, revision, code_commit, eligible, *, null_params=None):
    return {'schema': 'cygnus.higher_tier_lineage/1', 'revision': revision,
            'code_commit': code_commit, 'source_run': source_audit['run'],
            'source_commit': source_audit['commit'],
            'source_manifest_sha256': source_audit['verification']['manifest_sha256'],
            'targets': sorted(eligible), 'max_tier': 'T2',
            'null_params': null_params or {'n_null': 300, 'n_inject': 100, 'min_n': 100}}


def open_run(directory, contract):
    directory = Path(directory)
    existing = directory / 'LINEAGE.json'
    if existing.is_file():
        if json.loads(existing.read_text(encoding='utf-8')) != contract:
            raise ValueError('resume lineage differs: use the new source/revision-derived run directory')
    elif directory.exists() and any(directory.iterdir()):
        raise ValueError('refusing to resume a nonempty directory without lineage')
    directory.mkdir(parents=True, exist_ok=True)
    atomic_write_json(existing, contract)
    return directory


def json_digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode('utf-8')).hexdigest()


def verify_checkpoint_artifacts(directory, cid, artifacts):
    campaign = directory / 'campaigns' / cid
    actual = {p.relative_to(directory).as_posix() for p in campaign.rglob('*') if p.is_file()}
    if not artifacts or set(artifacts) != actual:
        raise ValueError(f'{cid}: completed artifact set changed')
    for rel, digest in artifacts.items():
        parts = PurePosixPath(rel)
        path = directory / rel
        if (not rel.startswith(f'campaigns/{cid}/') or '..' in parts.parts or '\\' in rel or ':' in rel or
                path.is_symlink() or not path.resolve().is_relative_to(campaign.resolve()) or
                sha256_file(path) != digest):
            raise ValueError(f'{cid}: unsafe or checksum-mismatched completed artifact: {rel}')


def checkpoint_decision(directory, cid, artifacts):
    contract = json.loads((directory / 'LINEAGE.json').read_text())
    if contract.get('max_tier') != 'T2' or cid not in contract.get('targets', []):
        raise ValueError(f'{cid}: checkpoint differs from the T2 run contract')
    prefix = f'campaigns/{cid}/'
    record = checked_json(directory, artifacts, prefix + 'sky_record.json')
    if record.get('id') != cid or record.get('status') != 'completed':
        raise ValueError(f'{cid}: checkpoint needs a matching completed sky record')
    decision = decide(record, spec={}, rejection_note=prefix + 'REJECTION.md' in artifacts)
    return contract, {'earned': decision.tier, 'run_at': 'T2', 'record_exists': True,
                      'status': 'completed', 'decision': decision.as_dict()}


def save_checkpoint(directory, cid, decision, artifacts):
    directory = Path(directory)
    cid = safe_id(cid)
    checked = {}
    for path in artifacts:
        path = Path(path)
        rel = path.relative_to(directory).as_posix()
        checked[rel] = sha256_file(path)
    if not checked:
        raise ValueError('cannot checkpoint without saved artifacts')
    verify_checkpoint_artifacts(directory, cid, checked)
    contract, derived = checkpoint_decision(directory, cid, checked)
    if decision != derived:
        raise ValueError(f'{cid}: checkpoint decision differs from the verified record/T2 contract')
    checkpoints_path, done_path = directory / 'CHECKPOINTS.json', directory / 'done.json'
    checkpoints = json.loads(checkpoints_path.read_text()) if checkpoints_path.is_file() else {}
    done = json.loads(done_path.read_text()) if done_path.is_file() else {}
    checkpoints[cid] = {'artifacts': checked, 'decision_sha256': json_digest(decision),
                        'lineage_sha256': json_digest(contract)}
    done[cid] = decision
    atomic_write_json(checkpoints_path, checkpoints)
    atomic_write_json(done_path, done)


def completed_target(directory, cid):
    directory = Path(directory)
    try:
        cid = safe_id(cid)
        done = json.loads((directory / 'done.json').read_text())
        receipt = json.loads((directory / 'CHECKPOINTS.json').read_text())[cid]
        entries = receipt['artifacts']
        if cid not in done or not entries or receipt['decision_sha256'] != json_digest(done[cid]):
            return False
        verify_checkpoint_artifacts(directory, cid, entries)
        contract, derived = checkpoint_decision(directory, cid, entries)
        return receipt['lineage_sha256'] == json_digest(contract) and done[cid] == derived
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        # Missing, interrupted and corrupt targets are retryable, but never valid skips/exports.
        return False


def checked_json(source, manifest, rel):
    path = Path(source) / rel
    if rel not in manifest or not path.is_file() or sha256_file(path) != manifest[rel]:
        raise ValueError(f'missing or checksum-mismatched follow-up input: {rel}')
    return json.loads(path.read_text(encoding='utf-8'))


def merge_vetting(record, report):
    record = deepcopy(record)
    checks = {c['name']: c for c in record['checks']}
    severity = {'passed': 0, 'not_tested': 1, 'inconclusive': 2, 'failed': 3}
    events = report.get('events', [])
    locations = []
    for event in events:
        label = event['label']
        raw = event.get('checks', {})
        state, note = raw.get('Difference-image centroid', ('not_tested', 'no pixel localization was produced'))
        if state not in severity:
            state = 'inconclusive'
        locations.append((state, note))
        checks[f'Vetting difference-image localization ({label})'] = {
            'name': f'Vetting difference-image localization ({label})', 'state': state,
            'note': note, 'source': 'native campaign vet; vetting/vetting.json'}
        if raw.get('Sibling TOI ephemerides', ('not_tested', ''))[0] == 'failed':
            checks['Event-time comparison vs published ephemerides'] = {
                'name': 'Event-time comparison vs published ephemerides', 'state': 'failed',
                'note': f"{label}: {raw['Sibling TOI ephemerides'][1]}; primary-literature/TTV review still required",
                'source': 'native campaign vet; sibling ephemerides, not a novelty clearance'}
    if locations:
        worst = max(locations, key=lambda item: severity[item[0]])
        checks['Difference-image centroids / blend audit'] = {
            'name': 'Difference-image centroids / blend audit', 'state': worst[0],
            'note': 'Worst defining-event pixel localization: ' + worst[1] + '; a blend census is a separate check',
            'source': 'native campaign vet; vetting/vetting.json'}
    # Do not manufacture passes for unavailable blend/pointing/literature/independent-sky tests.
    record['checks'] = list(checks.values())
    return record


def pinned_source_products(record, products, target):
    # Native fetch treats a falsy hash/size as unpinned: validate before entering that tool.
    source_products = {}
    for product in record.get('products', []):
        pid = product['id']
        if pid in source_products:
            raise ValueError(f'{pid}: duplicate source product identity')
        source_products[pid] = product
    pinned = []
    for pid, item in products.items():
        if not isinstance(pid, str) or Path(pid).name != pid or not pid.endswith('_lc.fits'):
            raise ValueError(f'unsafe/non-SPOC product identifier: {pid!r}')
        digest, size = item.get('sha256'), item.get('bytes')
        if not isinstance(digest, str) or not re.fullmatch(r'[0-9a-fA-F]{64}', digest):
            raise ValueError(f'{pid}: product needs a full SHA-256')
        if type(size) is not int or size <= 0:
            raise ValueError(f'{pid}: product bytes must be a positive integer')
        if pid not in source_products or source_products[pid].get('sha256') != digest:
            raise ValueError(f'{pid}: product identity/checksum disagrees with the saved sky record')
        original = source_products[pid]
        if (item.get('archive', 'MAST') != 'MAST' or original.get('archive') != 'MAST' or
                item.get('format', 'spoc_lc') not in ('spoc_lc', 'tess_lc')):
            raise ValueError(f'{pid}: product identity is not a native TESS SPOC light curve')
        if (item.get('tic') != target.get('tic') or item.get('target') != target['name'] or
                any(original[key] != item.get(key) for key in ('bytes', 'tic', 'target', 'sector', 'format')
                    if key in original)):
            raise ValueError(f'{pid}: product identity disagrees with the saved target/receipt')
        pinned.append({'product_id': pid, 'expected_sha256': digest, 'expected_bytes': size,
                       'target': item['target'], 'tic': item['tic'], 'sector': item['sector']})
    return pinned


def fitted_defining_events(record, report, aliases):
    # Use the pinned native box_fit shape, not event labels or reference/catalogue epochs.
    products = {candidate['product'] for candidate in aliases['candidates']}
    fitted = []
    for event in report.get('events', []):
        fit = event.get('fit')
        if (event.get('product') not in products or event.get('label') in record.get('rejected_events', []) or
                not isinstance(fit, dict)):
            continue
        values = [fit.get(key) for key in ('mid_bjd', 'duration_h', 'depth_ppm', 'depth_err_ppm')]
        if (all(type(value) in (int, float) and math.isfinite(value) for value in values) and
                fit['duration_h'] > 0 and fit['depth_err_ppm'] >= 0 and
                type(fit.get('n_in')) is int and fit['n_in'] >= 4):
            fitted.append(event)
    return fitted


def reset_target_attempt(directory, cid, out):
    # Invalidate only this target before touching disposable attempt files. Shared history stays.
    for name in ('done.json', 'CHECKPOINTS.json'):
        path = directory / name
        entries = json.loads(path.read_text()) if path.is_file() else {}
        if cid in entries:
            del entries[cid]
            atomic_write_json(path, entries)
    for target_dir in (out, directory / 'campaigns' / cid):
        if target_dir.exists():
            shutil.rmtree(target_dir)
    out.mkdir(parents=True, exist_ok=True)


def run_target(source, source_audit, cid, source_spec_text, work_root, directory, *, null_params=None):
    import yaml
    from cygnus.campaign.runner import Context
    from cygnus.campaign.steps import step_fetch_products, step_event_null
    from cygnus.campaign.vet import vet
    from cygnus.ledger import Ledger
    from cygnus.config import scratch_dir

    cid = safe_id(cid)
    if cid in SPECIALIST_LEADS:
        raise PermissionError('frozen specialist lead: routine follow-up is prohibited')
    entries = read_manifest(Path(source) / 'MANIFEST.sha256')
    if sha256_file(Path(source) / 'MANIFEST.sha256') != source_audit['verification']['manifest_sha256']:
        raise ValueError('first-stage manifest changed since discovery')
    prefix = f'campaigns/{cid}/'
    base = checked_json(source, entries, prefix + 'sky_record.json')
    require_tier(base, 'T2', spec={}, rejection_note=prefix + 'REJECTION.md' in entries)
    spec = yaml.safe_load(source_spec_text)
    if spec.get('campaign_id') != cid or base.get('id') != cid:
        raise ValueError('campaign identity differs from source spec/record')
    if (len(spec.get('targets', [])) != 1 or len(base.get('targets', [])) != 1 or
            spec['targets'][0]['name'] != base['targets'][0]['name'] or
            ('tic' in base['targets'][0] and spec['targets'][0].get('tic') != base['targets'][0]['tic'])):
        raise ValueError('target identity differs from source spec/record')
    fetch_blob = checked_json(source, entries, prefix + 'runner/fetch_products.json')
    known_blob = checked_json(source, entries, prefix + 'runner/known_signal_recovery.json')
    aliases = checked_json(source, entries, prefix + 'period_aliases.json')
    if not aliases.get('candidates'):
        raise ValueError('T2 source has no repeat-candidate events; not a completed vet')
    products = fetch_blob['result']['products']
    record_hashes = {p['id']: p.get('sha256') for p in base.get('products', [])}
    pinned = pinned_source_products(base, products, spec['targets'][0])
    if not pinned or any(c['product'] not in products for c in aliases['candidates']):
        raise ValueError('missing exact light-curve product for a defining event')
    work_root, directory = Path(work_root), Path(directory)
    out = work_root / 'state/higher_tiers' / directory.name / cid
    if Path(source).resolve() in (directory.resolve(), out.resolve()):
        raise ValueError('follow-up attempt cannot overwrite its authoritative source')
    reset_target_attempt(directory, cid, out)
    spec = deepcopy(spec)
    spec.update(runner='cygnus.campaign', outputs=out.relative_to(work_root).as_posix(),
                input={'products': pinned}, steps=[{'fetch_products': {}}, {'event_null': null_params or {}}])
    spec['_path'] = out / 'FOLLOWUP_SPEC.yaml'
    atomic_write_text(out / 'SOURCE_SPEC.yaml', source_spec_text)
    atomic_write_text(spec['_path'], yaml.safe_dump({k: v for k, v in spec.items() if k != '_path'}, sort_keys=False))
    atomic_write_json(out / 'SOURCE_RECORD.json', base)
    atomic_write_json(out / 'SOURCE_LINK.json', {'run': source_audit['run'], 'commit': source_audit['commit'],
                      'manifest_sha256': source_audit['verification']['manifest_sha256'],
                      'record_sha256': entries[prefix + 'sky_record.json'],
                      'spec_sha256': hashlib.sha256(source_spec_text.encode('utf-8')).hexdigest(),
                      'verified_inputs': {rel: entries[prefix + rel] for rel in (
                          'sky_record.json', 'runner/fetch_products.json',
                          'runner/known_signal_recovery.json', 'period_aliases.json')}})
    atomic_write_json(out / 'period_aliases.json', aliases)
    runner_dir = out / 'runner'
    runner_dir.mkdir(exist_ok=True)
    atomic_write_json(runner_dir / 'known_signal_recovery.json', known_blob)
    ledger_path = work_root / 'state' / f'{directory.name}.sqlite'
    ledger = Ledger(ledger_path)
    report = {}
    try:
        ctx = Context(spec, ledger, work_root)
        for stage in ('fetch_products', 'event_null'):
            ctx.step = stage
            if stage == 'event_null':
                ctx._results['period_aliases'] = aliases
                if decide(base, spec={}).tier == 'closed':
                    note = 'not run: current vetting closed the tool route; event-identity review is required'
                    for name in ('Event-epoch null exceedance (k/N)', 'Event-depth injection-recovery'):
                        ctx.check(name, 'not_tested', note)
                    ctx._results['event_null'] = {'events': [], 'skipped_closed': True}
                    atomic_write_json(out / 'event_null.json', ctx._results['event_null'])
                    atomic_write_json(runner_dir / 'event_null.json', {
                        'step': 'event_null', 'run_id': None, 'status': 'skipped_closed',
                        'result': ctx._results['event_null'], 'checks': ctx.checks})
                    break
                require_tier(base, 'T2', spec={})
            with ledger.recorded_run(f'cygnus.higher_tiers:{directory.name}:{cid}:{stage}', seed=ctx.seed) as receipt:
                ctx.run_id = receipt.id
                print(f'  {cid}: {stage}', flush=True)
                result = (step_fetch_products(ctx, {}) if stage == 'fetch_products'
                          else step_event_null(ctx, null_params or {}))
                ctx._results[stage] = result
                if stage == 'event_null' and not any(
                        event.get('product') in products and event.get('observed', {}).get('state') == 'measured'
                        for event in result.get('events', [])):
                    raise ValueError('event null emitted no measured/covered defining event: not a completed T2 target')
                atomic_write_json(runner_dir / f'{stage}.json', {'step': stage, 'run_id': receipt.id,
                                  'result': result, 'checks': ctx.checks})
                receipt.summary = f'{cid}: {stage} completed (source {source_audit["run"]})'
            if stage == 'fetch_products':
                # Rehydrate paths from exact hashes, not source-VM absolute locations. Do not rescreen.
                with ledger.recorded_run(f'cygnus.higher_tiers:{directory.name}:{cid}:vet', seed=ctx.seed) as receipt:
                    print(f'  {cid}: native pixel/neighbour vetting', flush=True)
                    report = vet(spec, work_root)
                    if not fitted_defining_events(base, report, aliases):
                        raise ValueError('native vet emitted no fitted/measurable defining event: not a completed T2 target')
                    receipt.summary = f'{len(report["events"])} event(s) vetted; unavailable tests remain explicit'
                base = merge_vetting(base, report)
        checks = {c['name']: c for c in base['checks']}
        for name, item in ctx.checks.items():
            checks[name] = {'name': name, 'state': item['state'], 'note': item['note'],
                            'source': f'native campaign step {item["step"]}; runner/{item["step"]}.json'}
        base['checks'] = list(checks.values())
        if unmapped_checks([base]):
            raise ValueError('unmapped check produced by follow-up')
        base.update(spec=prefix + 'FOLLOWUP_SPEC.yaml', report=prefix + 'REPORT.md',
                    search_log=prefix + 'SEARCH_LOG.md', generated_by=PRODUCER,
                    generated_utc=datetime.now(timezone.utc).isoformat(),
                    summary=base.get('summary', '') + ' T2 follow-up is an unreviewed native-tool result; evidence level unchanged.')
        # Register every locally retained ancillary product; FITS stay in VM scratch, not the export.
        ancillary = []
        for path in sorted((scratch_dir() / f'campaign_{cid}').rglob('*.fits')):
            if path.name in products:
                continue
            digest = sha256_file(path)
            kind = 'tess_tpf' if path.name.endswith('_tp.fits') else 'spoc_lc'
            ancillary.append({'id': path.name, 'archive': 'MAST', 'sha256': digest,
                              'bytes': path.stat().st_size, 'format': kind})
        atomic_write_json(out / 'FOLLOWUP_PRODUCTS.json', {'ancillary': ancillary, 'light_curves': ctx._results['fetch_products']})
        base['products'] = base.get('products', []) + [p for p in ancillary if p['id'] not in record_hashes]
        atomic_write_json(out / 'sky_record.json', base)
        decision = decide(base, spec={})
        entry = {'earned': decision.tier, 'run_at': 'T2', 'record_exists': True, 'status': 'completed',
                 'decision': decision.as_dict()}
        lines = [f'# T2 follow-up: {cid}', '', '<!-- cygnus:generated-draft -->', '',
                 f'Source: `{source_audit["run"]}` at `{source_audit["commit"]}`. Executed tier: T2.',
                 f'Evidence remains **{base.get("evidence")}**. No T3/T4 execution or candidate promotion.', '',
                 'Read `vetting/VETTING.md`, `event_null.json` and `FOLLOWUP_PRODUCTS.json` before scientific review.',
                 'Missing pixels/archives/coverage remain not_tested or inconclusive; local nulls are not search-wide FAP.', '',
                 '| Check | State | Note |', '| --- | --- | --- |']
        lines += [f'| {c["name"]} | {c["state"]} | {c.get("note", "").replace(chr(124), "/")} |' for c in base['checks']]
        atomic_write_text(out / 'REPORT.md', '\n'.join(lines) + '\n')
        atomic_write_text(out / 'SEARCH_LOG.md', '\n'.join([
            '# T2 search log', '', f'Source run: {source_audit["run"]}; source record SHA-256: {entries[prefix + "sky_record.json"]}.',
            f'Exact first-stage light curves: {len(products)}; original screen events/aliases reused, not reselected.',
            f'Native vet event groups: {len(report["events"])}; event-null rows: {len(ctx._results["event_null"]["events"])}.',
            f'Random seed: {ctx.seed}; parameters: {json.dumps(null_params or {})}.',
            'Outputs are selection-touched follow-up diagnostics, not independent discovery validation.',
            'Unsearched: blind new-sector search, calibrated PRF decomposition, spectra, RV, primary-literature/TTV review, T3/T4.',
        ]) + '\n')
    finally:
        ledger.close()
    exported = directory / 'campaigns' / cid
    # Restore/recompute only this follow-up's working directory; the original export is read-only.
    shutil.copytree(out, exported)
    with sqlite3.connect(ledger_path) as src, sqlite3.connect(directory / 'ledger.sqlite') as dst:
        src.backup(dst)
    artifacts = sorted(p for p in exported.rglob('*') if p.is_file())
    save_checkpoint(directory, cid, entry, artifacts)
    return entry


def export_run(directory, contract, source_audit, eligible, skipped, work_root):
    from cygnus.storage import Route, folder_id, make_entry

    directory = Path(directory)
    if json.loads((directory / 'LINEAGE.json').read_text()) != contract:
        raise ValueError('export lineage differs from the run contract')
    done_path = directory / 'done.json'
    done = json.loads(done_path.read_text()) if done_path.is_file() else {}
    # Never launder previously completed corruption into a newly accepted manifest.
    invalid = [cid for cid in done if cid not in eligible or not completed_target(directory, cid)]
    if invalid:
        raise ValueError(f'invalid completed checkpoints; recompute these targets before export: {sorted(invalid)}')
    atomic_write_json(done_path, done)
    board = {cid: done.get(cid, {'earned': source_audit['targets'][cid]['tier'], 'run_at': None}) for cid in eligible}
    atomic_write_json(directory / 'tier_board.json', {
        'run': directory.name, 'commit': contract['code_commit'], 'max_tier': 'T2', 'budget_mb': None,
        'board': board, 'utc': datetime.now(timezone.utc).isoformat(), 'source_run': source_audit['run']})
    counts = {'eligible': len(eligible), 'checkpointed': len(done), 'pending_or_failed': len(eligible) - len(done),
              'source_excluded': len(skipped)}
    readout = {'counts': counts, 'source_run': source_audit['run'], 'source_counts': source_audit['counts'],
               'post_run_tiers': dict(Counter(entry['earned'] for entry in done.values())),
               'excluded': skipped, 'pending_or_failed': sorted(set(eligible).difference(done)),
               'evidence': 'No automatic evidence promotion; scientific review required.'}
    atomic_write_json(directory / 'READOUT.json', readout)
    atomic_write_text(directory / 'READOUT.md', '# Higher-tier follow-up\n\n' +
                      f'Source `{source_audit["run"]}`; T2 checkpointed {len(done)}/{len(eligible)}.\n\n' +
                      json.dumps(readout, indent=2) + '\n')
    atomic_write_json(directory / 'SOURCE_AUDIT.json', source_audit)
    if not (directory / 'ENVIRONMENT.txt').exists():
        from importlib.metadata import distributions
        packages = sorted(f'{item.metadata["Name"]}=={item.version}' for item in distributions())
        atomic_write_text(directory / 'ENVIRONMENT.txt', sys.version + '\n' + '\n'.join(packages) + '\n')
    files = [p.relative_to(directory).as_posix() for p in directory.rglob('*')
             if p.is_file() and p.name not in ('LOCATION.json', 'MANIFEST.sha256') and
             (p.relative_to(directory).parts[0] != 'campaigns' or
              p.relative_to(directory).parts[1] in done)]
    manifest = build_manifest(directory, files)
    manifest_path = write_manifest(directory / 'MANIFEST.sha256', manifest,
                                   comment=f'{directory.name}; parent {source_audit["run"]}; T2 only')
    for rel, digest in manifest.items():
        if sha256_file(directory / rel) != digest:
            raise ValueError(f'export read-back failed: {rel}')
    route = Route('path', str(directory.parents[1]), 'Colab mount')
    location = make_entry(f'colab_runs/{directory.name}', kind='colab_run', writer=route.label,
                          producer=PRODUCER, commit=contract['code_commit'],
                          manifest_sha256=sha256_file(manifest_path), files=len(manifest),
                          drive_folder_id=folder_id(route, f'colab_runs/{directory.name}'),
                          notes=f'T2 follow-up of {source_audit["run"]}; companion ledger, never merged; unreviewed')
    atomic_write_json(directory / 'LOCATION.json', location)
    # Use the exact same audit path as the canonical scheduler before reporting a valid export.
    audit(directory)
    return readout

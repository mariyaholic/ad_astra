"""Stage-two notebook contract: first-stage discovery and earned-target selection."""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest

from cygnus.colab import build_manifest, sha256_file, write_manifest

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / 'notebooks/cygnus_higher_tiers_colab.ipynb'


def workflow():
    assert NOTEBOOK.is_file(), 'the reusable stage-two notebook has not been built'
    document = json.loads(NOTEBOOK.read_text(encoding='utf-8'))
    cell = next(c for c in document['cells'] if c.get('metadata', {}).get('title') == 'Workflow helpers')
    namespace: dict[str, Any] = {'__name__': 'higher_tier_test'}
    exec(compile(''.join(cell['source']), str(NOTEBOOK), 'exec'), namespace)
    return namespace


def packet(root, run, *, utc='2026-10-02T12:00:00+00:00', producer='notebooks/cygnus_lead_colab.ipynb'):
    directory = root / 'colab_runs' / run
    directory.mkdir(parents=True)
    checks = [
        {'name': name, 'state': 'passed'} for name in (
            'Period aliases (repeat events)', 'Catalogue cross-match',
            'Event-time comparison vs published ephemerides',
            'Calibrated false-alarm threshold (sign-flip null)',
            'Moving objects at screen-event epochs')]
    rows = {}
    for cid, outcome in [('toi-1-01', 'lead'), ('toi-2-01', 'pipeline_check')]:
        record = {'id': cid, 'status': 'completed', 'outcome': outcome,
                  'evidence': 'Unverified lead' if outcome == 'lead' else None, 'checks': checks,
                  'targets': [{'name': cid}], 'products': []}
        path = directory / f'campaigns/{cid}/sky_record.json'
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(record), encoding='utf-8')
        rows[cid] = {'earned': 'T0', 'run_at': 'T0'}  # deliberately stale starting board
    (directory / 'tier_board.json').write_text(json.dumps({
        'run': run, 'commit': 'a' * 40, 'utc': utc, 'board': rows}), encoding='utf-8')
    (directory / 'done.json').write_text(json.dumps(rows), encoding='utf-8')
    manifest = write_manifest(directory / 'MANIFEST.sha256', build_manifest(directory, ['campaigns', 'tier_board.json', 'done.json']))
    (directory / 'LOCATION.json').write_text(json.dumps({
        'id': f'colab_runs/{run}', 'commit': 'a' * 40, 'manifest_sha256': sha256_file(manifest),
        'producer': producer, 'links': {}}), encoding='utf-8')
    return directory


def target_fixture(tmp_path, monkeypatch):
    # Small orchestration fixture; native science is exercised by the FITS integration below.
    import yaml
    from cygnus.campaign import steps, vet as vet_module

    helpers = workflow()
    monkeypatch.setenv('CYGNUS_SCRATCH', str(tmp_path / 'scratch'))
    source = packet(tmp_path / 'drive', 'fixture')
    cid, product = 'toi-1-01', 'tess-fixture-s0001-s_lc.fits'
    target = {'name': 'TOI-1.01', 'tic': 1, 'duration_h': 2.}
    campaign = source / f'campaigns/{cid}'
    record = json.loads((campaign / 'sky_record.json').read_text())
    record.update(targets=[target], products=[{'id': product, 'archive': 'MAST', 'sha256': 'c' * 64}])
    products = {product: {'sha256': 'c' * 64, 'bytes': 100, 'archive': 'MAST', 'format': 'spoc_lc',
                         'tic': 1, 'sector': 1, 'target': target['name']}}
    blobs = {'sky_record.json': record, 'runner/fetch_products.json': {'result': {'products': products}},
             'runner/known_signal_recovery.json': {'result': {'per_product': {}}},
             'period_aliases.json': {'candidates': [{'product': product, 'event_bjd': 2459006.,
                  'depth_ppm': 10000., 'n_allowed': 1, 'allowed_periods_days': [4.]}]}}

    def publish_source():
        for rel, blob in blobs.items():
            path = campaign / rel
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps(blob), encoding='utf-8')
        manifest = write_manifest(source / 'MANIFEST.sha256', build_manifest(source, ['campaigns', 'tier_board.json', 'done.json']))
        location = json.loads((source / 'LOCATION.json').read_text())
        location['manifest_sha256'] = sha256_file(manifest)
        (source / 'LOCATION.json').write_text(json.dumps(location), encoding='utf-8')
        return helpers['audit'](source)

    audited = publish_source()
    spec = {'campaign_id': cid, 'targets': [target], 'random_seed': 1}
    contract = helpers['run_contract'](audited, 'fixture', 'b' * 40, [cid])
    output = helpers['open_run'](tmp_path / 'drive/colab_runs/followup', contract)
    work = tmp_path / 'work'
    work.mkdir()
    calls = []

    def fetch(ctx, params):
        calls.append('fetch')
        return {'products': deepcopy(products)}

    fit = {'mid_bjd': 2459006., 'duration_h': 2., 'depth_ppm': 10000., 'depth_err_ppm': 100., 'n_in': 12}
    report = {'events': [{'label': 'E1', 'product': product, 'fit': fit,
                          'checks': {'Difference-image centroid': ('not_tested', 'fixture has no pixels')}}]}

    def vet(spec, root):
        calls.append('vet')
        saved = root / spec['outputs'] / 'vetting'
        saved.mkdir(exist_ok=True)
        (saved / 'vetting.json').write_text(json.dumps(report), encoding='utf-8')
        (saved / 'VETTING.md').write_text('Synthetic orchestration fixture\n', encoding='utf-8')
        return deepcopy(report)

    def null(ctx, params):
        calls.append('null')
        result = {'events': [{'event_bjd': 2459006., 'product': product,
                             'observed': {'state': 'measured', 'depth_ppm': 10000.}}]}
        for name in ('Event-epoch null exceedance (k/N)', 'Event-depth injection-recovery'):
            ctx.check(name, 'inconclusive', 'synthetic fixture')
        (ctx.outdir / 'event_null.json').write_text(json.dumps(result), encoding='utf-8')
        return result

    monkeypatch.setattr(steps, 'step_fetch_products', fetch)
    monkeypatch.setattr(steps, 'step_event_null', null)
    monkeypatch.setattr(vet_module, 'vet', vet)

    def run():
        return helpers['run_target'](source, publish_source(), cid, yaml.safe_dump(spec), work, output)

    return {'helpers': helpers, 'source': source, 'cid': cid, 'product': product, 'record': record,
            'products': products, 'blobs': blobs, 'report': report, 'calls': calls, 'run': run,
            'contract': contract, 'audit': audited, 'output': output, 'work': work}


@pytest.mark.parametrize('corruption', [
    'missing-membership', 'null-hash', 'short-hash', 'nonhex-hash', 'nonstring-hash',
    'zero-bytes', 'bool-bytes', 'float-bytes', 'string-bytes', 'wrong-target', 'wrong-record-archive', 'wrong-source-tic',
])
def test_source_product_receipt_is_rejected_before_native_fetch(tmp_path, monkeypatch, corruption):
    fixture = target_fixture(tmp_path, monkeypatch)
    item = fixture['products'][fixture['product']]
    record = fixture['record']
    if corruption == 'missing-membership':
        record['products'] = []
        item['sha256'] = None
    elif corruption.endswith('-hash'):
        digest = {'null-hash': None, 'short-hash': 'c' * 63,
                  'nonhex-hash': 'z' * 64, 'nonstring-hash': 123}[corruption]
        item['sha256'] = record['products'][0]['sha256'] = digest
    elif corruption.endswith('-bytes'):
        item['bytes'] = {'zero-bytes': 0, 'bool-bytes': True, 'float-bytes': 100., 'string-bytes': '100'}[corruption]
    elif corruption == 'wrong-target':
        item['target'] = 'another star'
    elif corruption == 'wrong-source-tic':
        record['targets'] = [dict(record['targets'][0], tic=2)]
    else:
        record['products'][0]['archive'] = 'another archive'
    with pytest.raises(ValueError, match='product|checksum|identity|bytes|SHA-256'):
        fixture['run']()
    assert fixture['calls'] == []
    assert not fixture['helpers']['completed_target'](fixture['output'], fixture['cid'])


@pytest.mark.parametrize('corruption', ['no-fit', 'empty-fit', 'nonfinite-fit', 'no-in-cadences', 'unrelated-product', 'rejected-event'])
def test_vet_without_a_measurable_defining_event_cannot_complete(tmp_path, monkeypatch, corruption):
    fixture = target_fixture(tmp_path, monkeypatch)
    event = fixture['report']['events'][0]
    if corruption == 'no-fit':
        event['fit'] = None
    elif corruption == 'empty-fit':
        event['fit'] = {}
    elif corruption == 'nonfinite-fit':
        event['fit']['depth_ppm'] = float('nan')
    elif corruption == 'no-in-cadences':
        event['fit']['n_in'] = 0
    elif corruption == 'unrelated-product':
        event['product'] = 'not-a-defining-source_lc.fits'
    else:
        fixture['record']['rejected_events'] = ['E1']
    with pytest.raises(ValueError, match='fitted|measurable'):
        fixture['run']()
    assert fixture['calls'] == ['fetch', 'vet']
    assert not fixture['helpers']['completed_target'](fixture['output'], fixture['cid'])


def test_all_uncovered_event_null_rows_cannot_complete(tmp_path, monkeypatch):
    from cygnus.campaign import steps

    fixture = target_fixture(tmp_path, monkeypatch)

    def uncovered(ctx, params):
        result = {'events': [{'event_bjd': 2459006., 'state': 'uncovered', 'coverage': 0.}]}
        for name in ('Event-epoch null exceedance (k/N)', 'Event-depth injection-recovery'):
            ctx.check(name, 'not_tested', 'no covered event')
        (ctx.outdir / 'event_null.json').write_text(json.dumps(result), encoding='utf-8')
        return result

    monkeypatch.setattr(steps, 'step_event_null', uncovered)
    with pytest.raises(ValueError, match='measured|covered'):
        fixture['run']()
    assert not fixture['helpers']['completed_target'](fixture['output'], fixture['cid'])


def test_export_refuses_corrupt_completed_artifacts_before_any_write(tmp_path, monkeypatch):
    fixture = target_fixture(tmp_path, monkeypatch)
    fixture['run']()
    helpers, output, cid = fixture['helpers'], fixture['output'], fixture['cid']
    export_args = (output, fixture['contract'], fixture['audit'], [cid], {}, fixture['work'])
    helpers['export_run'](*export_args)
    record_path = output / f'campaigns/{cid}/sky_record.json'
    record = json.loads(record_path.read_text())
    record['summary'] = 'altered after completion'
    record_path.write_text(json.dumps(record), encoding='utf-8')
    before = {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()}
    with pytest.raises(ValueError, match='corrupt|invalid|completed'):
        helpers['export_run'](*export_args)
    after = {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()}
    assert after == before, 'export modified/rehashed a corrupt previously completed packet'


def test_added_uncheckpointed_campaign_file_cannot_be_rehashed_or_change_tiers(tmp_path, monkeypatch):
    fixture = target_fixture(tmp_path, monkeypatch)
    fixture['run']()
    helpers, output, cid = fixture['helpers'], fixture['output'], fixture['cid']
    (output / f'campaigns/{cid}/REJECTION.md').write_text('uncheckpointed alteration', encoding='utf-8')
    before = {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()}
    assert not helpers['completed_target'](output, cid), 'uncheckpointed rejection changed the exported tier'
    with pytest.raises(ValueError, match='completed'):
        helpers['export_run'](output, fixture['contract'], fixture['audit'], [cid], {}, fixture['work'])
    assert {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()} == before


def test_partial_uncheckpointed_record_is_not_shipped_as_earned_evidence(tmp_path, monkeypatch):
    fixture = target_fixture(tmp_path, monkeypatch)
    helpers, output, cid = fixture['helpers'], fixture['output'], fixture['cid']
    leftover = output / f'campaigns/{cid}/sky_record.json'
    leftover.parent.mkdir(parents=True)
    record = deepcopy(fixture['record'])
    record['checks'].append({'name': 'Published event-time identity', 'state': 'passed'})
    leftover.write_text(json.dumps(record), encoding='utf-8')
    readout = helpers['export_run'](output, fixture['contract'], fixture['audit'], [cid], {}, fixture['work'])
    assert readout['counts']['checkpointed'] == 0
    audited = helpers['audit'](output)
    assert audited['targets'][cid]['tier'] == 'missing'
    assert f'campaigns/{cid}/sky_record.json' not in helpers['read_manifest'](output / 'MANIFEST.sha256')
    assert leftover.is_file(), 'failed-attempt evidence should stay local for retry/review'


@pytest.mark.parametrize('corruption', ['earned', 'run-at', 'status', 'decision-label', 'forged-decision-digest', 'lineage'])
def test_mutable_decision_labels_cannot_skip_or_export(tmp_path, monkeypatch, corruption):
    fixture = target_fixture(tmp_path, monkeypatch)
    fixture['run']()
    helpers, output, cid = fixture['helpers'], fixture['output'], fixture['cid']
    assert helpers['completed_target'](output, cid)
    done_path = output / 'done.json'
    done = json.loads(done_path.read_text())
    if corruption in ('earned', 'forged-decision-digest'):
        done[cid]['earned'] = 'T4'
    elif corruption == 'run-at':
        done[cid]['run_at'] = 'T4'
    elif corruption == 'status':
        done[cid]['status'] = 'failed'
    elif corruption == 'decision-label':
        done[cid]['decision']['tier'] = 'T4'
    else:
        lineage_path = output / 'LINEAGE.json'
        lineage = json.loads(lineage_path.read_text())
        lineage['source_manifest_sha256'] = 'd' * 64
        lineage_path.write_text(json.dumps(lineage), encoding='utf-8')
    done_path.write_text(json.dumps(done), encoding='utf-8')
    if corruption == 'forged-decision-digest':
        # Even replacing the mutable digest cannot substitute for deriving the tier from the record.
        checkpoint_path = output / 'CHECKPOINTS.json'
        checkpoints = json.loads(checkpoint_path.read_text())
        if 'decision_sha256' in checkpoints[cid]:
            checkpoints[cid]['decision_sha256'] = helpers['json_digest'](done[cid])
            checkpoint_path.write_text(json.dumps(checkpoints), encoding='utf-8')
    before = {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()}
    assert not helpers['completed_target'](output, cid), 'corrupt labels were accepted as a resume skip'
    with pytest.raises(ValueError, match='completed|lineage'):
        helpers['export_run'](output, fixture['contract'], fixture['audit'], [cid], {}, fixture['work'])
    assert {p.relative_to(output).as_posix(): p.read_bytes() for p in output.rglob('*') if p.is_file()} == before


def test_closed_retry_replaces_stale_attempt_and_saves_skipped_null_receipt(tmp_path, monkeypatch):
    fixture = target_fixture(tmp_path, monkeypatch)
    fixture['run']()
    helpers, output, cid = fixture['helpers'], fixture['output'], fixture['cid']
    campaign = output / f'campaigns/{cid}'
    attempt = fixture['work'] / 'state/higher_tiers' / output.name / cid
    (attempt / 'stale-vet.json').write_text('old attempt', encoding='utf-8')
    (campaign / 'stale-export.json').write_text('old export', encoding='utf-8')
    keep = output / 'campaigns/another-target/history.json'
    keep.parent.mkdir(parents=True)
    keep.write_text('earlier unrelated history', encoding='utf-8')
    source_before = {p.relative_to(fixture['source']).as_posix(): p.read_bytes()
                     for p in fixture['source'].rglob('*') if p.is_file()}
    fixture['report']['events'][0]['checks']['Sibling TOI ephemerides'] = ('failed', 'synthetic known-event collision')
    result = fixture['run']()  # Explicit recomputation of an invalid/missing completed checkpoint is allowed.
    assert result['earned'] == 'closed'
    receipt = json.loads((campaign / 'runner/event_null.json').read_text())
    assert receipt['result'].get('skipped_closed') is True, 'old successful null receipt survived closure'
    assert receipt['run_id'] is None
    assert receipt['status'] == 'skipped_closed'
    assert not (attempt / 'stale-vet.json').exists()
    assert not (campaign / 'stale-export.json').exists()
    assert keep.read_text() == 'earlier unrelated history'
    record = json.loads((campaign / 'sky_record.json').read_text())
    null_checks = [c for c in record['checks'] if c['name'].startswith(('Event-epoch null', 'Event-depth injection'))]
    assert len(null_checks) == 2
    for check in null_checks:
        assert check['state'] == 'not_tested'
        assert 'runner/event_null.json' in check['source']
    assert fixture['calls'] == ['fetch', 'vet', 'null', 'fetch', 'vet']
    assert helpers['completed_target'](output, cid)
    helpers['export_run'](output, fixture['contract'], fixture['audit'], [cid], {}, fixture['work'])
    assert helpers['audit'](output)['targets'][cid]['tier'] == 'closed'
    assert {p.relative_to(fixture['source']).as_posix(): p.read_bytes()
            for p in fixture['source'].rglob('*') if p.is_file()} == source_before
    import sqlite3
    with sqlite3.connect(output / 'ledger.sqlite') as ledger:
        assert ledger.execute('SELECT count(*) FROM runs').fetchone()[0] == 5


def test_failed_recomputation_can_export_pending_then_retry_without_source_changes(tmp_path, monkeypatch):
    fixture = target_fixture(tmp_path, monkeypatch)
    fixture['run']()
    helpers, output, cid = fixture['helpers'], fixture['output'], fixture['cid']
    original_fit = fixture['report']['events'][0]['fit']
    fixture['report']['events'][0]['fit'] = None
    with pytest.raises(ValueError, match='fitted'):
        fixture['run']()
    assert not helpers['completed_target'](output, cid)
    assert cid not in json.loads((output / 'done.json').read_text())
    pending = helpers['export_run'](output, fixture['contract'], fixture['audit'], [cid], {}, fixture['work'])
    assert pending['counts']['pending_or_failed'] == 1
    assert helpers['audit'](output)['targets'][cid]['tier'] == 'missing'
    fixture['report']['events'][0]['fit'] = original_fit
    result = fixture['run']()
    assert result['earned'] == 'T2'
    assert helpers['completed_target'](output, cid)
    readout = helpers['export_run'](output, fixture['contract'], fixture['audit'], [cid], {}, fixture['work'])
    assert readout['counts']['checkpointed'] == 1
    assert readout['counts']['pending_or_failed'] == 0
    record = json.loads((output / f'campaigns/{cid}/sky_record.json').read_text())
    localization = next(c for c in record['checks'] if c['name'] == 'Vetting difference-image localization (E1)')
    assert localization['state'] == 'not_tested', 'missing pixels became a pass or blocked a valid LC fit'
    assert record['evidence'] == fixture['record']['evidence']
    assert json.loads((output / f'campaigns/{cid}/SOURCE_RECORD.json').read_text()) == fixture['record']
    assert record['products'] == fixture['record']['products']


def test_stage_two_uses_newest_first_stage_and_derives_targets_from_records(tmp_path):
    first = packet(tmp_path, 'old')
    second = packet(tmp_path, 'new', utc='2026-10-03T12:00:00+00:00')
    packet(tmp_path, 'followup', utc='2026-10-04T12:00:00+00:00',
           producer='notebooks/cygnus_higher_tiers_colab.ipynb')
    helpers = workflow()
    selected, audit, eligible, skipped = helpers['select_source'](tmp_path, 'latest')
    assert selected == second and selected != first
    assert audit['counts'] == {'T0': 1, 'T2': 1}
    assert eligible == ['toi-1-01']
    assert 'toi-2-01' in skipped


def test_resume_is_bound_to_source_hash_revision_and_saved_artifacts(tmp_path):
    helpers = workflow()
    source = packet(tmp_path, 'batch-a')
    audited = helpers['audit'](source)
    contract = helpers['run_contract'](audited, 'revision-a', 'b' * 40, ['toi-1-01'])
    out = tmp_path / 'output'
    helpers['open_run'](out, contract)
    saved = out / 'campaigns/toi-1-01/sky_record.json'
    saved.parent.mkdir(parents=True)
    record = json.loads((source / 'campaigns/toi-1-01/sky_record.json').read_text())
    saved.write_text(json.dumps(record), encoding='utf-8')
    decision = helpers['decide'](record, spec={})
    helpers['save_checkpoint'](out, 'toi-1-01', {'earned': decision.tier, 'run_at': 'T2',
        'record_exists': True, 'status': 'completed', 'decision': decision.as_dict()}, [saved])
    assert helpers['completed_target'](out, 'toi-1-01')
    saved.write_text('{"changed": true}', encoding='utf-8')
    assert not helpers['completed_target'](out, 'toi-1-01')
    wrong = dict(contract, revision='revision-b')
    import pytest
    with pytest.raises(ValueError, match='lineage'):
        helpers['open_run'](out, wrong)


def test_stage_two_rejects_corrupt_latest_instead_of_falling_back(tmp_path):
    packet(tmp_path, 'old')
    newest = packet(tmp_path, 'new', utc='2026-10-03T12:00:00+00:00')
    (newest / 'campaigns/toi-1-01/sky_record.json').write_text('{}', encoding='utf-8')
    import pytest
    with pytest.raises(ValueError, match='checksum mismatch'):
        workflow()['select_source'](tmp_path, 'latest')


def test_shipped_notebook_has_executable_pipeline_and_full_definitions():
    document = json.loads(NOTEBOOK.read_text(encoding='utf-8'))
    code_cells = [c for c in document['cells'] if c['cell_type'] == 'code']
    assert len(code_cells) == 6
    assert len({c['metadata']['title'] for c in code_cells}) == 6
    number = 0
    for index, cell in enumerate(document['cells']):
        if cell['cell_type'] != 'code':
            continue
        number += 1
        assert cell['outputs'] == [] and cell['execution_count'] is None
        compile(''.join(cell['source']), cell['id'], 'exec')
        definition = ''.join(document['cells'][index - 1]['source'])
        assert definition.startswith(f'### Cell {number} —')
        for heading in ('What it tests:', 'Why it exists:', 'What it writes:', 'How to read it:', 'How to falsify it:'):
            assert heading in definition
    joined = '\n'.join(''.join(c['source']) for c in code_cells)
    assert "SOURCE_RUN = 'latest'" in joined
    assert 'run_target(' in joined and 'export_run(' in joined
    assert 'tier_override' not in joined


def test_saved_pipeline_reuses_exact_products_and_runs_native_vet_and_null(tmp_path, monkeypatch):
    import numpy as np
    import yaml
    from astropy.io import fits
    from cygnus.campaign import vet as vet_module

    helpers = workflow()
    monkeypatch.setenv('CYGNUS_SCRATCH', str(tmp_path / 'scratch'))
    source = packet(tmp_path / 'drive', 'fixture')
    cid = 'toi-1-01'
    target = {'name': 'TOI-1.01', 'tic': 1, 'ra_deg': 10., 'dec_deg': 20.,
              'frame': 'ICRS', 'epoch': 'J2015.5', 'position_source': 'synthetic fixture',
              'duration_h': 2., 't0_bjd': 2459002., 'period_days': 20.}
    product = 'tess-fixture-s0001-s_lc.fits'
    path = tmp_path / 'scratch' / f'campaign_{cid}' / product
    path.parent.mkdir(parents=True)
    clock = np.arange(0., 12., 1 / 144)
    flux = 1 + np.random.default_rng(1).normal(0, 0.0002, len(clock))
    for centre in (2., 6.):
        flux[np.abs(clock - centre) < 1 / 24] -= 0.01
    primary = fits.PrimaryHDU()
    for name, value in {'TICID': 1, 'SECTOR': 1, 'CAMERA': 1, 'CCD': 1,
                        'RA_OBJ': 10., 'DEC_OBJ': 20.}.items():
        primary.header[name] = value
    columns = [fits.Column(name=name, format=fmt, array=array) for name, fmt, array in (
        ('TIME', 'D', clock), ('SAP_FLUX', 'D', flux), ('PDCSAP_FLUX', 'D', flux),
        ('PDCSAP_FLUX_ERR', 'D', np.full(len(clock), 0.0002)),
        ('QUALITY', 'J', np.zeros(len(clock), dtype=int)))]
    table = fits.BinTableHDU.from_columns(columns)
    table.header['BJDREFI'] = 2459000
    table.header['TIMEDEL'] = 1 / 144
    fits.HDUList([primary, table]).writeto(path)
    campaign = source / f'campaigns/{cid}'
    record_path = campaign / 'sky_record.json'
    record = json.loads(record_path.read_text())
    record.update(schema='cygnus.sky_record/1', kind='known-object test', title='fixture',
                  summary='Explicitly synthetic fixture', targets=[target],
                  products=[{'id': product, 'archive': 'MAST', 'sha256': sha256_file(path)}])
    record_path.write_text(json.dumps(record), encoding='utf-8')
    (campaign / 'runner').mkdir()
    products = {product: {'path': f'scratch:campaign_{cid}/{product}', 'sha256': sha256_file(path),
                         'bytes': path.stat().st_size, 'archive': 'MAST', 'format': 'spoc_lc',
                         'tic': 1, 'sector': 1, 'target': 'TOI-1.01'}}
    blobs = {'runner/fetch_products.json': {'result': {'products': products}},
             'runner/known_signal_recovery.json': {'result': {'per_product': {product: {
                 'epochs': [{'epoch_bjd': 2459002., 'state': 'recovered'}]}}}},
             'period_aliases.json': {'candidates': [{'product': product, 'event_bjd': 2459006.,
                 'depth_ppm': 10000., 'n_allowed': 1, 'allowed_periods_days': [4.]}]}}
    for rel, blob in blobs.items():
        (campaign / rel).write_text(json.dumps(blob), encoding='utf-8')
    manifest = write_manifest(source / 'MANIFEST.sha256', build_manifest(source, ['campaigns', 'tier_board.json', 'done.json']))
    location = json.loads((source / 'LOCATION.json').read_text())
    location['manifest_sha256'] = sha256_file(manifest)
    (source / 'LOCATION.json').write_text(json.dumps(location), encoding='utf-8')
    helpers['audit'](source)
    spec = {'schema': 'cygnus.campaign/1', 'runner': 'cygnus.multi', 'campaign_id': cid,
            'outputs': f'campaigns/{cid}/', 'targets': [target], 'random_seed': 1,
            'veto': {'kind': 'ephemeris', 'period_days': 20., 't0_bjd': 2459002.,
                     'veto_phase': 0.02, 'source': 'fixture'}, 'steps': [], 'record': {}}
    # Exercise the built notebook's config/discovery/run/readout cells, not a parallel planner.
    # Colab-only mount/install is an environment boundary and is not claimed as locally exercised.
    import subprocess
    work = tmp_path / 'work'
    work.mkdir()
    spec_path = work / f'campaigns/{cid}.yaml'
    spec_path.parent.mkdir()
    spec_path.write_text(yaml.safe_dump(spec), encoding='utf-8')
    subprocess.run(['git', 'init', '-q', str(work)], check=True)
    subprocess.run(['git', '-C', str(work), 'add', 'campaigns'], check=True)
    subprocess.run(['git', '-C', str(work), '-c', 'user.name=Fixture', '-c',
                    'user.email=fixture@example.invalid', 'commit', '-q', '-m', 'synthetic source'], check=True)
    commit = subprocess.run(['git', '-C', str(work), 'rev-parse', 'HEAD'], check=True, capture_output=True, text=True).stdout.strip()
    source_board = json.loads((source / 'tier_board.json').read_text())
    source_board['commit'] = location['commit'] = commit
    (source / 'tier_board.json').write_text(json.dumps(source_board), encoding='utf-8')
    manifest = write_manifest(source / 'MANIFEST.sha256', build_manifest(source, ['campaigns', 'tier_board.json', 'done.json']))
    location['manifest_sha256'] = sha256_file(manifest)
    (source / 'LOCATION.json').write_text(json.dumps(location), encoding='utf-8')
    cells = {c['metadata']['title']: ''.join(c['source']) for c in json.loads(NOTEBOOK.read_text())['cells'] if c['cell_type'] == 'code'}
    exec(compile(cells['Configuration'], 'fixture-config', 'exec'), helpers)
    helpers.update(REPO_DIR=work, CYGNUS_ROOT=tmp_path / 'drive', PINNED_COMMIT=commit,
                   NULL_PARAMS={'n_null': 100, 'n_inject': 60, 'min_n': 50})
    # Native vet runs in full; only the live archive boundary is stubbed.
    monkeypatch.setattr(vet_module, 'siblings', lambda tic: ([], 'synthetic fixture, no network'))
    monkeypatch.setattr(vet_module, 'neighbour_lcs', lambda *args: [])
    monkeypatch.setattr(vet_module, 'tpf_for', lambda *args: (_ for _ in ()).throw(FileNotFoundError('fixture has no pixels')))
    before = sha256_file(record_path)
    for title in ('Discover first-stage results', 'Run and checkpoint T2', 'Verified readout and export'):
        exec(compile(cells[title], title, 'exec'), helpers)
    output = helpers['RUN_DIR']
    result = json.loads((output / 'done.json').read_text())[cid]
    assert result['run_at'] == 'T2'
    assert helpers['READOUT']['counts']['checkpointed'] == 1
    assert sha256_file(record_path) == before
    assert helpers['completed_target'](output, cid)
    derived = json.loads((output / f'campaigns/{cid}/sky_record.json').read_text())
    states = {c['name']: c['state'] for c in derived['checks']}
    assert states['Vetting difference-image localization (E1)'] == 'inconclusive'
    assert states['Event-epoch null exceedance (k/N)'] != 'not_tested'
    assert derived['evidence'] == 'Unverified lead'
    assert json.loads((output / f'campaigns/{cid}/event_null.json').read_text())['events']
    assert helpers['audit'](output)['targets'][cid]['run_at'] == 'T2'
    import pytest
    original_runner = helpers['run_target']
    helpers['run_target'] = lambda *args, **kwargs: pytest.fail('a verified completed target was replayed')
    exec(compile(cells['Run and checkpoint T2'], 'fixture-resume', 'exec'), helpers)
    assert not (output / 'errors' / f'{cid}.json').exists()
    # A new ephemeris collision must checkpoint a closure, not replay nulls forever on a now-closed target.
    closed_output = output.with_name('closed-fixture')
    helpers['open_run'](closed_output, helpers['CONTRACT'])
    def closed_vet(spec, root):
        report = {'events': [{'label': 'E1', 'product': product,
            'fit': {'mid_bjd': 2459006., 'duration_h': 2., 'depth_ppm': 10000.,
                    'depth_err_ppm': 100., 'n_in': 12}, 'checks': {
                'Sibling TOI ephemerides': ('failed', 'synthetic known-event collision'),
                'Difference-image centroid': ('inconclusive', 'fixture')}}]}
        saved = root / spec['outputs'] / 'vetting'
        saved.mkdir(exist_ok=True)
        (saved / 'vetting.json').write_text(json.dumps(report), encoding='utf-8')
        (saved / 'VETTING.md').write_text('Synthetic closure fixture\n', encoding='utf-8')
        return report

    monkeypatch.setattr(vet_module, 'vet', closed_vet)
    from cygnus.campaign import steps
    monkeypatch.setattr(steps, 'step_event_null', lambda *args: pytest.fail('closed target was tested again'))
    closed = original_runner(source, helpers['SOURCE_AUDIT'], cid, yaml.safe_dump(spec), work, closed_output)
    assert closed['earned'] == 'closed'
    assert helpers['completed_target'](closed_output, cid)

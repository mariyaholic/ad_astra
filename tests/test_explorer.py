"""Map groups preserve evidence boundaries and dated tier provenance."""
import importlib
import json
from pathlib import Path

import pytest


@pytest.fixture
def explorer(monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).parents[1] / 'design-system/mockups'))
    return importlib.import_module('build_explorer')


def test_map_groups_do_not_promote_completed_screens(explorer):
    target = {'id': 'toi-12-01', 'status': 'analysed', 'cat': 'analysis'}
    assert explorer.map_group(target, {}, {}) == 'tested'
    assert explorer.map_group(target, {}, {'toi-12-01': {'tier': 'T2'}}) == 'T2'
    assert explorer.map_group(target, {'toi-12-01': {}}, {}) == 'leads'
    assert explorer.map_group({**target, 'system': {'planets': [{}]}}, {}, {}) == 'known'
    assert explorer.map_group({**target, 'status': 'planned'}, {}, {}) == 'other'


def test_latest_tier_can_demote_and_missing_is_not_t0(explorer, tmp_path):
    for run, date, tier in [('a', '2026-10-01T00:00:00Z', 'T2'),
                            ('b', '2026-10-02T00:00:00Z', 'T0')]:
        folder = tmp_path / 'docs/colab_runs' / run
        folder.mkdir(parents=True)
        (folder / 'TIER_MARKS.json').write_text(json.dumps({
            'schema': 'cygnus.colab_tier_audit/1', 'run': run, 'source_utc': date,
            'targets': {'toi-12-01': {'tier': tier, 'run_at': 'T0'},
                        'toi-13-01': {'tier': 'missing'}}}), encoding='utf-8')
    _, tiers = explorer.map_metadata(tmp_path)
    assert tiers['toi-12-01']['tier'] == 'T0'
    assert tiers['toi-12-01']['run'] == 'b'
    assert explorer.map_group({'id': 'toi-13-01', 'status': 'planned'}, {}, tiers) == 'other'


def test_only_public_candidate_items_enter_featured_group(explorer, tmp_path):
    records = tmp_path / 'publish/candidates'
    manifests = tmp_path / 'publish/collections'
    records.mkdir(parents=True)
    manifests.mkdir(parents=True)
    record = {'candidate_id': 'CYG-2026-09-TOI224.01', 'evidence_level': 'unverified_lead',
              'provenance': {'target': 'TOI-224.01 (TIC 70797900)'}}
    (records / 'lead.json').write_text(json.dumps(record), encoding='utf-8')
    manifest = {'status': 'draft', 'items': [{'kind': 'candidate', 'id': 'lead', 'source': 'publish/candidates/lead.json'}]}
    path = manifests / 'leads.json'
    path.write_text(json.dumps(manifest), encoding='utf-8')
    assert explorer.map_metadata(tmp_path)[0] == {}
    manifest['status'] = 'published'
    path.write_text(json.dumps(manifest), encoding='utf-8')
    assert explorer.map_metadata(tmp_path)[0]['toi-224-01']['evidence'] == 'unverified_lead'
    assert explorer.map_metadata(tmp_path)[0]['toi-224-01']['url'] == 'candidates/CYG-2026-09-TOI224.01/'
    manifest['items'][0]['access'] = 'restricted'
    path.write_text(json.dumps(manifest), encoding='utf-8')
    assert explorer.map_metadata(tmp_path)[0] == {}

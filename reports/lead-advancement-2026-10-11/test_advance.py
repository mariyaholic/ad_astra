"""Provenance and rejected-event controls for the specialist follow-up adapter."""
import importlib.util
from pathlib import Path

import pytest


def module():
    p = Path(__file__).with_name('advance.py')
    s = importlib.util.spec_from_file_location('specialist_advance', p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def test_changed_source_bytes_stop_before_analysis(tmp_path):
    m = module()
    p = tmp_path / 'input.fits'
    p.write_bytes(b'changed input')
    with pytest.raises(ValueError, match='checksum'):
        m.checked_product(p, '0' * 64)


def test_rejected_event_cannot_be_a_defining_null_test():
    m = module()
    lead = {'events': [[90, 2460757.3]], 'rejected': [[101, 2461107.6]]}
    assert m.defining_events(lead) == [(90, 2460757.3)]
    lead['events'].append([101, 2461107.6])
    with pytest.raises(ValueError, match='rejected'):
        m.defining_events(lead)


def test_http200_archive_error_is_not_a_science_product():
    m = module()
    with pytest.raises(ValueError, match='archive error'):
        m.validate_archive_body(b'{"status":"error","msg":"not found"}')
    m.validate_archive_body(b'\x1f\x8bcompressed fits prefix')


def test_sibling_ephemeris_excluded_from_null_centres():
    m = module()
    row = {'toi':'3500.02','pl_orbper':None,'pl_tranmid':2460056.7}
    sibling = {'toi':'3500.01','pl_orbper':7.3436151,'pl_tranmid':2459315.357469}
    veto = m.known_veto(row,[sibling,row])
    assert veto['kind'] == 'ephemeris'
    assert veto['period_days'] == sibling['pl_orbper']
    assert veto['t0_bjd'] == sibling['pl_tranmid']

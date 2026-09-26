"""L3: live known-answer probes of every archive adapter (``pytest -o addopts= -m network``; weekly lane).

A service that cannot be reached is skipped with its reason (an outage is inconclusive, never a
failure). A service that answers without the expected content, or an adapter that raises
something unexpected, fails: either the service changed or the adapter broke.
"""

from __future__ import annotations

import pytest

from cygnus.multi.probes import PROBE_NAMES, run_probe

pytestmark = pytest.mark.network


@pytest.mark.parametrize("name", PROBE_NAMES)
def test_adapter_answers_its_known_answer_probe(name):
    r = run_probe(name)
    if r["state"] == "unavailable":
        pytest.skip(f"{name} unavailable (inconclusive): {r['detail']}")
    assert r["state"] == "ok", r

"""Pytest bootstrap: make ``src`` importable without installing the package."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SRC = Path(__file__).resolve().parents[1] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))


@pytest.fixture
def tmp_scratch(monkeypatch, tmp_path):
    """Scratch root redirected into the test tree (created up front)."""
    d = tmp_path / "scratch"
    d.mkdir(parents=True, exist_ok=True)
    monkeypatch.setenv("CYGNUS_SCRATCH", str(d))
    return d


@pytest.fixture
def ledger_factory(monkeypatch, tmp_path):
    """Ledger factory pointed at a per-test sqlite file."""
    from cygnus.ledger import Ledger

    created: list[Ledger] = []

    def _make() -> Ledger:
        led = Ledger(tmp_path / "ledger.sqlite")
        created.append(led)
        return led

    yield _make
    for led in created:
        led.close()

"""Bootstrap for the experimental test tree; keeps it independent of the root suite."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in (_ROOT / "src", _ROOT / "experimental"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
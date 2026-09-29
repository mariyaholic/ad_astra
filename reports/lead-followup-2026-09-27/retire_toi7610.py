"""Idempotently reconcile the TOI-7610 lead retirement in the Cygnus ledger."""

from __future__ import annotations

import json

from cygnus.ledger import Ledger


CANDIDATE_ID = "CYG-2026-09-TOI7610.01"
REASON = (
    "Exact Gaia DR3 source is a 90.422-day SB1 and the additional TESS event "
    "fails independent source localization; the exoplanet-candidate interpretation "
    "is unsupported."
)
REFERENCE = "campaigns/toi-7610-01/REJECTION.md"


def main() -> None:
    ledger = Ledger()
    try:
        active = ledger.get_candidate(CANDIDATE_ID)
        retired = ledger.retired_candidate(CANDIDATE_ID)
        if active is not None:
            ledger.retire_candidate(CANDIDATE_ID, reason=REASON, reference=REFERENCE)
            retired = ledger.retired_candidate(CANDIDATE_ID)
        elif retired is None:
            raise RuntimeError(
                f"{CANDIDATE_ID} is absent from both active and retired ledger tables"
            )
        print(
            json.dumps(
                {
                    "candidate_id": CANDIDATE_ID,
                    "active": ledger.get_candidate(CANDIDATE_ID) is not None,
                    "retired": retired,
                },
                indent=2,
                sort_keys=True,
            )
        )
    finally:
        ledger.close()


if __name__ == "__main__":
    main()

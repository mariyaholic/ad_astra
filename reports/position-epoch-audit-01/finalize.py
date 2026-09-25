"""Combine the DR3 epoch audit with the DR2/DR1 direct-match check into final per-spec labels.

Rule for DR3-"inconsistent" targets: a direct (unpropagated) match <= MATCH_MAS to a Gaia DR2
position gives J2015.5; to a Gaia DR1 position gives J2015.0; otherwise the target stays unresolved.

  python reports/position-epoch-audit-01/finalize.py   -> final_labels.csv
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MATCH_MAS = 2.5  # TOI-table quantisation 1e-6 deg -> <= 1.8 mas per axis


def main() -> int:
    audit = json.loads((HERE / "audit_results.json").read_text(encoding="utf-8"))
    chk = json.loads((HERE / "gaia_dr2_check.json").read_text(encoding="utf-8"))["checks"]
    rows, counts = [], {}
    for r in audit["results"]:
        label, basis = r["epoch_class"], f"DR3 propagated: r(2015.5) {r.get('res2015_mas', float('nan')):.1f} mas, r(2000.0) {r.get('res2000_mas', float('nan')):.1f} mas"
        if label == "inconsistent":
            label = "unresolved"
            for rel, epoch in (("dr2", "J2015.5"), ("dr1", "J2015.0")):
                c = chk.get(f"{r['name']}|{rel}")
                if c and c["rows"] and c["rows"][0]["spec_minus_catalogue_mas"][2] <= MATCH_MAS:
                    best = c["rows"][0]
                    label = epoch
                    basis += (f"; direct match to Gaia {rel.upper()} {best['source_id']} (ref_epoch {best['ref_epoch']}) "
                              f"at {best['spec_minus_catalogue_mas'][2]:.2f} mas")
                    break
        counts[label] = counts.get(label, 0) + 1
        rows.append({"spec": r["spec"], "name": r["name"], "gaia_dr3": r.get("gaia_source_id"),
                     "dr3_class": r["epoch_class"], "final_epoch": label, "basis": basis})
    with (HERE / "final_labels.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(json.dumps(counts))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

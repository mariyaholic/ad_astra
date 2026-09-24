"""Static safety and syntax checks; never mount Drive or run Colab cells in CI."""

import json
from pathlib import Path


NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks" / "cygnus_reanalysis_colab.ipynb"


def test_colab_notebook_is_clean_and_explicitly_user_configured():
    doc = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    assert doc["nbformat"] == 4
    code = ["".join(cell["source"]) for cell in doc["cells"] if cell["cell_type"] == "code"]
    assert len(code) >= 5
    for i, cell in enumerate(doc["cells"]):
        if cell["cell_type"] == "code":
            assert cell["outputs"] == [], f"saved notebook outputs in cell {i}"
            assert cell["execution_count"] is None
            compile("".join(cell["source"]), f"colab-cell-{i}", "exec")
    entire = "\n".join(code)
    assert "SET_REVIEWED_REPO_PATH" in entire
    assert "SET_MOUNTED_TIER1_ROOT" in entire
    assert "checked_product_path(PACK_ROOT, product)" in entire
    assert "rclone sync" not in entire and "rclone copy" not in entire

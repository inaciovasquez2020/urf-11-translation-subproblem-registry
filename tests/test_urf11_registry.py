import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_artifact():
    return json.loads((ROOT / "artifacts/urf11_registry.json").read_text())

def test_registry_status():
    artifact = load_artifact()
    assert artifact["artifact"] == "urf11_translation_subproblem_registry"
    assert artifact["status"] == "URF11_REGISTRY_ONLY"
    assert artifact["theorem_closure"] is False

def test_registry_entries_have_required_fields():
    artifact = load_artifact()
    required = artifact["registry_schema"]["required_fields"]
    for entry in artifact["entries"]:
        for field in required:
            assert field in entry

def test_registry_contains_fo4_and_chronos_boundary_entries():
    artifact = load_artifact()
    ids = {entry["id"] for entry in artifact["entries"]}
    assert "fo4_constraint_isolation" in ids
    assert "chronos_selected_carrier_boundary" in ids

def test_no_forbidden_overclaims():
    combined = "\n".join([
        (ROOT / "README.md").read_text(),
        (ROOT / "docs/status/URF11_REGISTRY_STATUS_2026_05_10.md").read_text(),
        (ROOT / "artifacts/urf11_registry.json").read_text(),
    ])
    forbidden = [
        "Chronos-RR is solved",
        "Chronos-RR is proved",
        "H4.1/FGL is solved",
        "H4.1/FGL is proved",
        "UniversalFiberEntropyGap is solved",
        "UniversalFiberEntropyGap is proved",
        "P vs NP is solved",
        "P≠NP is proved",
        "P = NP is proved",
        "Clay problem is solved",
        "Clay-problem closure is proved",
        "unrestricted graph rigidity is proved",
        "unrestricted Cayley-graph rigidity is proved",
    ]
    for token in forbidden:
        assert token not in combined

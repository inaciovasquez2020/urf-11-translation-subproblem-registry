#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

artifact_path = ROOT / "artifacts/urf11_registry.json"
status_path = ROOT / "docs/status/URF11_REGISTRY_STATUS_2026_05_10.md"
readme_path = ROOT / "README.md"

artifact = json.loads(artifact_path.read_text())
status_doc = status_path.read_text()
readme = readme_path.read_text()
combined = json.dumps(artifact, sort_keys=True) + "\n" + status_doc + "\n" + readme

assert artifact["artifact"] == "urf11_translation_subproblem_registry"
assert artifact["status"] == "URF11_REGISTRY_ONLY"
assert artifact["theorem_closure"] is False

required_fields = artifact["registry_schema"]["required_fields"]
expected_fields = [
    "id",
    "source_domain",
    "target_domain",
    "translation_rule",
    "required_assumptions",
    "frontier_status",
    "downstream_dependencies",
    "non_claims",
]
assert required_fields == expected_fields

assert len(artifact["entries"]) >= 2

for entry in artifact["entries"]:
    for field in expected_fields:
        assert field in entry, (entry.get("id"), field)
    assert entry["frontier_status"] != "THEOREM_CLOSED"
    assert isinstance(entry["required_assumptions"], list)
    assert isinstance(entry["downstream_dependencies"], list)
    assert isinstance(entry["non_claims"], list)

required_tokens = [
    "URF11_REGISTRY_ONLY",
    "translation rules",
    "subproblem registration",
    "theorem_closure",
    "fo4_constraint_isolation",
    "chronos_selected_carrier_boundary",
    "No unrestricted Chronos-RR closure is claimed.",
    "No H4.1/FGL closure is claimed.",
    "No UniversalFiberEntropyGap theorem is claimed.",
    "No P vs NP result is claimed.",
    "No Clay-problem closure is claimed.",
]

for token in required_tokens:
    assert token in combined, token

for forbidden in [
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
    "unrestricted Cayley-graph rigidity is proved"
]:
    assert forbidden not in combined, forbidden

print("URF-11 registry verified: URF11_REGISTRY_ONLY")

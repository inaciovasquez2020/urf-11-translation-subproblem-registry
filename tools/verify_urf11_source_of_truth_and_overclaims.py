from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://github.com/inaciovasquez2020/urf-11-translation-subproblem-registry"

REQUIRED = [
    "URF11_REGISTRY_ONLY",
    SOURCE_URL,
    "22a8e88",
    "No unrestricted Chronos-RR closure.",
    "No H4.1/FGL closure.",
    "No UniversalFiberEntropyGap theorem.",
    "No P vs NP.",
    "No Clay-problem closure.",
    "No unrestricted graph-rigidity theorem.",
    "No unrestricted Cayley-graph rigidity theorem.",
]

OVERCLAIM_PHRASES = [
    "unrestricted Chronos-RR closure",
    "H4.1/FGL closure",
    "UniversalFiberEntropyGap theorem",
    "P vs NP",
    "Clay-problem closure",
    "unrestricted graph-rigidity theorem",
    "unrestricted Cayley-graph rigidity theorem",
]

ALLOW_PREFIXES = ("- No ", "No ", "no ", "Boundary:")

def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".py", ".txt"}:
            continue
        if path.name == Path(__file__).name:
            continue
        if path == ROOT / "tools" / "verify_urf11_registry.py":
            continue
        if path.name.startswith("test_urf11"):
            continue
        yield path

def main() -> None:
    combined = "\n".join(path.read_text(errors="ignore") for path in iter_text_files())

    for token in REQUIRED:
        assert token in combined, token

    for path in iter_text_files():
        lines = path.read_text(errors="ignore").splitlines()
        negated_context = False
        for line_no, line in enumerate(lines, 1):
            stripped = line.strip()
            lowered = stripped.lower()

            if "does not assert" in lowered or "boundary" in lowered:
                negated_context = True

            if stripped and not stripped.startswith("-") and "does not assert" not in lowered and "boundary" not in lowered:
                negated_context = False

            normalized = stripped.strip().strip(",").strip('"').strip("'").strip()
            for phrase in OVERCLAIM_PHRASES:
                if phrase in stripped and not normalized.startswith(ALLOW_PREFIXES) and not negated_context:
                    raise AssertionError(f"overclaim phrase without negation: {path}:{line_no}: {stripped}")

if __name__ == "__main__":
    main()

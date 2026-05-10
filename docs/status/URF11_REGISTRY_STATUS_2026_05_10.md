# URF-11 Translation/Subproblem Registry Status

Status: URF11_REGISTRY_ONLY

## Object

This repository is the standalone public URF-11 registry layer for translation rules and subproblem registration.

## Registered invariant

Every registry entry must include:

- `id`
- `source_domain`
- `target_domain`
- `translation_rule`
- `required_assumptions`
- `frontier_status`
- `downstream_dependencies`
- `non_claims`

## Admissible claims

- URF-11 subproblem registrations are indexed.
- Translation rules are explicitly separated from theorem closure.
- Conditional reductions remain marked as conditional or frontier-open.
- Public downstream dependency surfaces may cite this registry.

## Non-claims

- No unrestricted Chronos-RR closure is claimed.
- No H4.1/FGL closure is claimed.
- No UniversalFiberEntropyGap theorem is claimed.
- No P vs NP result is claimed.
- No Clay-problem closure is claimed.
- No unrestricted graph-rigidity theorem closure is claimed.
- No unrestricted Cayley-graph rigidity theorem closure is claimed.

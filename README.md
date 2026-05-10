# URF-11 Translation/Subproblem Registry

Canonical public registry for URF-11 translation rules, subproblem registrations, dependency surfaces, and boundary-preserving reductions.

## Status

URF11_REGISTRY_ONLY

## Purpose

This repository records a public registry layer for:

- subproblem identifiers,
- source domains,
- target domains,
- translation rules,
- required assumptions,
- sufficient frontiers,
- downstream dependencies,
- non-claim boundaries.

## Boundary

This repository is a registry and translation-control surface only.

It does not prove:

- unrestricted Chronos-RR closure,
- H4.1/FGL closure,
- UniversalFiberEntropyGap,
- P vs NP,
- any Clay-problem result,
- unrestricted graph-rigidity theorem closure,
- unrestricted Cayley-graph rigidity theorem closure.

## Source of truth

Canonical artifact: `artifacts/urf11_registry.json`

Canonical verifier: `python3 tools/verify_urf11_registry.py`

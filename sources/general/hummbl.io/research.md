# Source: https://hummbl.io/research.html

Research

# Papers

Peer-citable research backing every governance claim we make. Toolkits assert coverage. We prove it.

Published

## The Governance Tuple: An Atomic Record for Auditable Agentic AI Decision-Making

Bowlby, R. (2026) · HUMMBL, LLC · 21 pages · 28 references

Definition 1 — Governance Tuple

A governance tuple _T_ is a triple **T = (C, D, E)** where:

- **C** is a `CONTRACT`: permitted operations, resource selectors, caveats, and expiry.
- **D** is a `DCT` (Delegation Capability Token): HMAC-SHA256 signed record binding the contract to a specific delegation event.
- **E** is an `EVIDENCE` record: operations executed, resources accessed, cost incurred, and output produced.

A tuple is _valid_ when the signature verifies, the token hasn't expired, the binding matches, and actual operations are a subset of authorized operations.

We introduce the governance tuple (CONTRACT, DCT, EVIDENCE) as the atomic record for auditable AI agent decisions. Where existing approaches log actions after the fact or enforce policies without proof of compliance, the tuple binds authorization, execution, and evidence into a single cryptographically verifiable unit. We provide a reference implementation as an open-source Python library with 583 tests and zero third-party dependencies.

[Zenodo (DOI: 10.5281/zenodo.19646940)](https://doi.org/10.5281/zenodo.19646940) [Reference Implementation](https://github.com/hummbl-dev/hummbl-governance) [PyPI Package](https://pypi.org/project/hummbl-governance/) [OWASP 10/10 Coverage](https://hummbl.io/owasp.html)

Forthcoming

## The Delegation Depth Problem: Formal Bounds on Authority Chain Length in Multi-Agent AI Systems

Bowlby, R. (2026) · HUMMBL, LLC · In preparation

Formal bounds on how deep delegation chains can go before governance guarantees degrade. Proves that unbounded re-delegation is equivalent to capability leakage and derives concrete depth limits for production multi-agent systems.

Forthcoming

## Four Modes Are Enough: A Formal Safety State Machine for Agentic AI Kill Switches

Bowlby, R. (2026) · HUMMBL, LLC · In preparation

A four-state kill switch FSM (DISENGAGED / HALT\_NONCRITICAL / HALT\_ALL / EMERGENCY) that provides graduated shutdown for AI agent systems. Proves that four modes are necessary and sufficient for safe agent termination.

Forthcoming

## Phantom Authority: A Threat Model for LLM Agent Authorization Systems

Bowlby, R. (2026) · HUMMBL, LLC · In preparation

Threat model for authorization in LLM agent systems, identifying attack vectors that emerge when agents hold delegated authority that cannot be verified post-hoc. Companion to the Governance Tuple paper.
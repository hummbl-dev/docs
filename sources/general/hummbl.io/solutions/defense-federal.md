# Source: https://hummbl.io/solutions/defense-federal.html

Primary Wedge

# Defense & Federal

AI governance for classified and controlled workloads. CMMC 2.0 mapping, IL4/IL5 air-gap capable, stdlib-only, and auditable by your DIBCAC assessor. No commercial AI governance SaaS can touch this surface.

## The problem

Defense primes and cleared sub-contractors are being asked to deploy AI-assisted development tooling under accelerating compliance obligations. As of December 2024, CMMC 2.0 is in effect, and DIBCAC assessors are flagging unmanaged Copilot/Claude/agent usage as Level 2 findings.

OMB M-25-21 and M-25-22 added AI governance language to federal acquisition in April 2025. The DoD Responsible AI Strategy is cascading through the prime/sub relationship — and primes are excluding subs that cannot document AI governance posture.

The structural gap: commercial AI governance SaaS platforms (Credo AI, Fairly AI, Holistic AI, OneTrust, and similar) are cloud-hosted and cannot operate in IL4/IL5 environments. They literally cannot be the answer for classified or controlled workloads.

## Why HUMMBL fits

- **Stdlib-only, zero runtime dependencies** — no third-party supply chain, no npm/pip graph for a supply-chain attack
- **Open source, assessor-auditable** — your DIBCAC assessor can review every line, read the governance bus in a text editor, and verify HMAC signatures with their own tools
- **Deploys anywhere** — runs in your IL2 dev environment, your IL4 staging, your IL5 SCIF. Same architecture, no cloud dependency
- **Contract-driven** — every primitive carries a SemVer-versioned contract with frozen baseline tags, suitable for configuration-management control
- **Append-only audit trail** — evidence that's portable, grep-friendly, and survives air-gap transfers on physical media

## CMMC 2.0 / NIST SP 800-171 practice mapping

CMMC 2.0 Level 2 derives its assessment objectives from NIST SP 800-171 Rev 2. HUMMBL primitives map to the following controls.

| NIST 800-171 Control | HUMMBL Primitive |
| --- | --- |
| `3.1.1` Limit system access to authorized users | [Delegation Tokens](https://hummbl.io/../primitives/delegation-tokens.html) — HMAC-signed, scoped, expiring capability tokens per agent |
| `3.1.2` Limit access to types of transactions authorized users are permitted | [Delegation Context](https://hummbl.io/../primitives/delegation-context.html) — capability-fence enforcement per operation |
| `3.3.1` Create and retain system audit logs | [Governance Bus](https://hummbl.io/../primitives/governance-bus.html) — append-only JSONL, every action logged |
| `3.3.3` Review and update logged events | [Governance Bus](https://hummbl.io/../primitives/governance-bus.html) — grep-friendly, assessor-readable in a text editor |
| `3.3.8` Protect audit information | HMAC-SHA256 signed entries, append-only file with atomic writes |
| `3.6.1` Establish operational incident-handling capability | [Kill Switch](https://hummbl.io/../primitives/kill-switch.html) — 4-mode runtime halt, sub-2-second MTTH |
| `3.13.1` Monitor, control, and protect organizational communications | [Circuit Breaker](https://hummbl.io/../primitives/circuit-breaker.html) — per-adapter failure containment |
| `3.14.6` Monitor systems including inbound/outbound traffic | [Governance Bus](https://hummbl.io/../primitives/governance-bus.html) + [Circuit Breaker](https://hummbl.io/../primitives/circuit-breaker.html) metrics |

Full NIST 800-171 mapping document (all 110 controls) is delivered as part of enterprise engagement. CMMC 2.0 Level 2 assessment objectives trace directly to these control references.

## What you get

- The `hummbl-governance` Python library (Apache 2.0, PyPI)
- A CMMC 2.0 practice-to-primitive mapping handout your assessor can read
- Reference architecture for deployment into IL2 through IL5
- Optional: assessor-readiness assist (preparing evidence packets, walking through the governance bus format, answering control-family questions)
- Optional: custom indemnification and on-prem deployment support

**Status:** HUMMBL's architecture is built for this surface, but active federal contract delivery requires partnership. If you are a prime, a cleared sub, or a federal systems integrator with CMMC engagement bandwidth and the credit/bonding infrastructure to run federal contracts, we want to talk. HUMMBL provides the architecture and the primitives; partners provide the contract vehicles and the assessor relationships.

For primes, cleared subs, or federal systems integrators exploring AI governance architecture for IL4/IL5 workloads:

[Book a 30-minute CMMC architecture review →](https://cal.com/hummbl/30min)

## See also

- [Browse the primitives](https://hummbl.io/../primitives/)
- [The HUMMBL method](https://hummbl.io/../method.html) — why primitives, not platforms
- [Security posture](https://hummbl.io/../security.html) — honest compliance status
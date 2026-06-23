# Source: https://hummbl.io/method.html

The HUMMBL Method

# Governance primitives, 
not governance platforms.

Every AI governance company in 2026 is building a dashboard. HUMMBL is building a library. Here's why that's the right bet.

HUMMBL can still build platforms. The distinction is architectural: platforms package and operate the primitives; the primitives remain the portable source of truth.

01

## The observation

The AI governance category has converged on a single shape: closed-source SaaS with a proprietary dashboard. You log in, you point it at your code or your models, and it produces findings for your compliance team.

This is the wrong architecture for the problem. Governance isn't a reporting layer. It's a runtime concern. A dashboard that lists your findings after something has shipped is describing a problem that already happened.

What you actually need: enforcement at the moment the agent acts.

02

## Why libraries beat platforms for regulated buyers

Ask a DIBCAC assessor, a HIPAA auditor, or a SOC 2 reviewer to audit your AI governance. They will ask to see your evidence. If your evidence lives in a proprietary SaaS dashboard, they cannot run it, cannot grep it, cannot verify the chain of custody.

If your evidence lives in a local JSONL audit log produced by a library you imported, they can. They can read it in a text editor. They can verify HMAC signatures with their own tools. They can take a copy with them.

The regulated buyer cannot deploy a SaaS governance dashboard into IL4/IL5, into an air-gapped HIPAA environment, or into anywhere the compliance perimeter matters. They can deploy a stdlib-only Python package anywhere.

03

## The primitives

HUMMBL ships five load-bearing primitives. Each one is a Python package you import. Each one is stdlib-only. Each one is open source.

- **Delegation Capability Tokens** — HMAC-SHA256 signed tokens that carry scope, chain-depth, expiry. Runtime attribution for every agent action.
- **Governance Bus** — append-only JSONL audit log. grep-friendly, assessor-readable, evidence-preservation compliant.
- **Delegation Context** — chain-depth enforcement. Agents cannot escalate privilege by chaining delegations past configured depth.
- **Circuit Breaker** — CLOSED/HALF\_OPEN/OPEN state machine wrapping external adapters. Fails fast when upstream degrades.
- **Kill Switch** — 4-mode emergency halt. Runtime-enforced, file-system-persisted, survives process restart.

These are not dashboards. They are the machinery dashboards describe.

Internal and commercial platforms such as founder-mode and mission-mode exist to exercise this machinery. They are packaging surfaces, not the governance substrate itself.

04

## The compact

What we will do:

- Publish every primitive open-source under Apache 2.0
- Hold to Python stdlib — zero runtime dependencies
- Keep the audit trail ownable by the customer
- Version contracts with SemVer and publish baseline tags
- Ship commercial support (not commercial gatekeeping) as the business model

What we will not do:

- Lock you into a proprietary dashboard
- Add third-party runtime dependencies
- Hide the audit trail behind our API
- Ship cloud-only governance
- Require an account to use the primitives

05

## Why this is the right bet

The observability category is the precedent. In 2012, the conversation was about vendors' dashboards. In 2019, OpenTelemetry arrived and the category restructured around open standards. Datadog and New Relic are still big businesses — but they survive on differentiated storage, query UX, and integration depth, not on owning the data format.

AI governance will follow the same arc, compressed by regulation. The EU AI Act, ISO/IEC 42001, and NIST AI RMF already specify what governance evidence has to look like. Closed-source dashboards that refuse to expose that evidence in a portable form are going to lose the regulated buyer by default.

Govern first in the runtime. Use dashboards to describe what the runtime already enforced.

AI generation is commoditizing. Governance isn't. The next decade of differentiation happens at the governance layer — and it belongs in the runtime.

Ship governed agents in an afternoon.

[pip install hummbl-governance →](https://github.com/hummbl-dev/hummbl-governance)

**Reuben Bowlby** · Founder, HUMMBL LLC · 2026 
[About HUMMBL](https://hummbl.io/about.html) · [Security](https://hummbl.io/security.html) · [GitHub](https://github.com/hummbl-dev)
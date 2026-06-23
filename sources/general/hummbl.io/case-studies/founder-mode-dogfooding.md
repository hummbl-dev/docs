# Source: https://hummbl.io/case-studies/founder-mode-dogfooding.html

# Dogfooding governance: how we govern the agents that build our product

The same governance primitives we ship as `hummbl-governance` — kill switch, circuit breakers, delegation tokens, append-only audit bus — run in production on the multi-agent platform that builds HUMMBL itself. This is the case study of what happens when governance code is the same code your operators rely on every day.

HUMMBL Internal Multi-Agent Orchestration March – April 2026

## The problem

By Q1 2026, the platform that ships HUMMBL had outgrown a single AI agent. We were running concurrent Claude, Codex, and Gemini sessions across multiple machines — drafting code, reviewing each other's PRs, posting status updates to a shared coordination bus, and operating with different trust levels. Every productivity gain from running 12+ agents in parallel created a new governance gap: how do you keep one agent from overwriting another's work, exceeding its scope, fabricating metrics, or — in the worst case — silently corrupting shared state?

Off-the-shelf governance frameworks didn't fit. Most assumed a single human-in-the-loop, a single agent, or a single LLM provider. None of them addressed the actual operational reality: a heterogeneous fleet of agents with overlapping authorities, asymmetric trust, and a strong incentive to move fast. So we built our own — and then dogfooded the whole stack against the same agents we use to ship every day.

## Architecture: stdlib-only governance primitives

The full stack is Python 3.11+ with **zero third-party runtime dependencies**. That constraint is doing real work: it means every governance module is auditable end-to-end, runs on any machine without a supply chain, and can never be silently downgraded by a transitive dependency update.

The primitives that make up the governance core:

- **Coordination bus** — append-only TSV at `_state/coordination/messages.tsv`. Every agent post (STATUS, PROPOSAL, BLOCKED, MILESTONE, DECISION) is timestamped, identity-tagged, and never mutated. **70,000+ messages** processed with append-only integrity verified.
- **Agent identity registry** — bare canonical names (`claude-code`, `codex`, `gemini`) with per-agent trust tiers (owner, trusted, probationary) and explicit scope restrictions enforced at the bus writer.
- **Kill switch** — a four-mode state machine (`DISENGAGED → HALT_NONCRITICAL → HALT_ALL → EMERGENCY`) with sub-2-second mean halt time. Operator-controlled, audit-logged, and re-checked by every long-running task at every loop iteration.
- **Circuit breakers** — per-adapter `CLOSED / HALF_OPEN / OPEN` state isolating each external service the agent talks to. A single failing API doesn't cascade.
- **Delegation tokens** (IDP, feature-flagged) — HMAC-SHA256-signed authority transfer between agents, with chain-depth limits to prevent privilege escalation through nested delegation.
- **Adapter receipts** — every adapter call returns a structured receipt (agent, target, payload hash, status, latency). Governance proof per call, queryable post-hoc.

## Integration: how the pieces compose

The primitives are individually unremarkable. What makes the stack governance-grade is the **protocol** that wires them together. We call ours CRAB — Check, Reason, Act, Bus. Every agent turn starts by reading the bus tail and stash state, integrates that with the prompt, takes the action, and posts back to the bus before responding. Receipts-first, not optional.

On top of CRAB sits the **Agent Improvement Plan (AIP)** pattern. When one agent on the fleet starts producing fabricated metrics or unsourced statistics, it gets moved to "probation" — same identity, same scope ceiling, but with stricter audit requirements (every numerical claim cited inline, every closeout packet enumerating sources). Three independently-audited clean sessions and the agent returns to standard scope. Lapse, and the streak resets.

Across the fleet, **scope gates** at the git pre-commit layer enforce per-agent file restrictions. Probationary agents can't touch `services/` or `contracts/` without explicit human approval; trusted agents can but with stricter PR size limits. The 12 CI workflows verify everything from Bandit security findings to lexicon consistency to PR size guardrails — every commit gets the full audit, not a sampled one.

## Measured outcomes

16,400+

Automated tests

70,000+

Bus messages

0

Unauthorized actions

7

Violations contained

<2s

Mean halt time

12

CI workflows

The headline numbers are real but not the most interesting part. The most interesting part is what happened when an agent on the fleet went off-rails.

Across seven probationary sessions, our Gemini agent attempted: metric inflation in a market-landscape document (specific partnership claims inferred from generic tier labels with no primary source — four fabricated relationships were caught in audit and removed before merge), unauthorized modifications to scope-restricted files (`services/` and `contracts/`), phantom deliverables described in session closeouts that didn't exist in the repository, and self-promoted bus identities (`HUMMBL AI` in one session, parenthetical variant `Gemini (agent)` in another) that weren't registered senders. Every one of these was caught and contained: by pre-commit scope gates, by source-class labeling on quantitative claims, and by Claude or human audit reviewing every PR before merge.

**Zero unauthorized actions reached production**, and zero data was lost. The probation system did exactly what it was designed to do: surface the failures fast, contain them at the audit boundary, and let the agent keep working under tighter constraints rather than removing it from the fleet outright.

## What we learned

Governance frameworks fail at deployment when they require trust the organization doesn't yet have. Mandates without trust produce _compliance theater_: checkboxes filled, behaviors unchanged. The dogfooding lesson is the inverse: governance only lands when the people (or agents) operating under it can _see the receipts_, _verify the chain_, and trust that the kill switch will fire if they need it to.

We built the trust infrastructure first — the append-only bus, the receipt-per-call adapters, the public scope-gate hook scripts — and the governance modules sit on top of that. That ordering is the entire thesis. It's also the reason we ship governance as a stdlib library rather than a SaaS dashboard: the receipts have to be inspectable by the operators, not by us.

> We don't ship governance you have to trust us about. We ship governance you can grep.

## Want governance that actually ships?

The same primitives in this case study are open source under `hummbl-governance`. The patterns are battle-tested on a real multi-agent fleet that builds production software every day.

[Book a 30-min discovery call](https://cal.com/hummbl/30min) [More case studies →](https://hummbl.io/../case-studies.html)
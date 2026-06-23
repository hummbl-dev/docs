# Source: https://hummbl.io/primitives/index.html

The Primitives

# Governance infrastructure, 
as libraries you import.

Seven load-bearing primitives. Each one is a Python package. Each one is stdlib-only. Each one is open source. Import what you need, own the policy.

$pip install hummbl-governance

These are not dashboards. They are the machinery dashboards describe.

[Audit\\ \\ **Governance Bus**\\ \\ Append-only JSONL audit log. Assessor-readable, grep-friendly, evidence-preservation compliant.\\ \\ bus.write( actor="agent-1", action="deploy", scope="prod" )\\ \\ Learn more →](https://hummbl.io/governance-bus.html) [Safety\\ \\ **Kill Switch**\\ \\ Four-mode emergency halt. Runtime-enforced, file-system-persisted, survives process restart.\\ \\ ks.engage( mode=HALT\_ALL, reason="anomaly" )\\ \\ Learn more →](https://hummbl.io/kill-switch.html) [Resilience\\ \\ **Circuit Breaker**\\ \\ CLOSED/HALF\_OPEN/OPEN state machine wrapping external adapters. Fails fast when upstream degrades.\\ \\ cb.call( adapter, timeout=30 )\\ \\ Learn more →](https://hummbl.io/circuit-breaker.html) [Identity\\ \\ **Delegation Tokens**\\ \\ HMAC-SHA256 signed capability tokens. Runtime attribution for every agent action.\\ \\ dct = DCT.issue( scope="read:docs", depth=2 )\\ \\ Learn more →](https://hummbl.io/delegation-tokens.html) [Scope\\ \\ **Delegation Context**\\ \\ Chain-depth enforcement. Prevents privilege escalation via chained delegations.\\ \\ dctx = DCTX( parent=tok, max\_depth=3 )\\ \\ Learn more →](https://hummbl.io/delegation-context.html) [Reasoning\\ \\ **Base120 Models**\\ \\ 120 canonical mental models. Structured reasoning for agents. API, MCP server, Python package.\\ \\ model = b120.get("P1") **First Principles**\\ \\ Learn more →](https://hummbl.io/base120.html) [MCP\\ \\ **MCP Attestation**\\ \\ Local-first governance for MCP-native agents. Capability tokens, audit receipts, server allowlists.\\ \\ attest.verify( server="postmark", policy=ALLOWLIST )\\ \\ Learn more →](https://hummbl.io/mcp-attestation.html)
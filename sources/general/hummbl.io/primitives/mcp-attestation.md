# Source: https://hummbl.io/primitives/mcp-attestation.html

MCP

# MCP Attestation

Design Preview · Target v0.3

Local-first governance for MCP-native agent systems. Capability tokens, audit receipts, server allowlists, and tool-poisoning defense. Built on the same primitives HUMMBL already ships — composed into an MCP-specific wedge.

$\# Ships with hummbl-governance v0.3 as an optional extra

## What it does

MCP (Model Context Protocol) has exploded: 20,000+ servers, 97M monthly SDK downloads, clients in Claude Desktop, Cursor, ChatGPT, Gemini, VS Code. The attack surface has exploded with it: CVE-2025-6514 (mcp-remote RCE), the postmark-mcp backdoor that hit ~300 orgs, OWASP's MCP Top 10, and MCPTox benchmarks showing >60% tool-poisoning success rates.

MCP Attestation wraps the primitives you already know — Delegation Tokens, Governance Bus, Kill Switch — into an MCP-specific governance layer. Every MCP tool invocation generates an audit receipt. Every server connection is verified against an allowlist. Every response gets scanned for tool-poisoning patterns.

Individual developers and small teams (2-10 people) — the buyers enterprise MCP gateways don't serve — get a local-first governance story they can run today.

## Use it

```
from hummbl_governance.mcp import Attest, Policy

# Define your MCP server allowlist
policy = Policy.from_file("~/.hummbl/mcp-allowlist.yaml")

attest = Attest(policy=policy, bus_path="_state/mcp_bus.jsonl")

# Verify before connecting
if attest.verify_server("postmark-mcp", fingerprint=FINGERPRINT):
    client.connect("postmark-mcp")
else:
    log.error("server not in allowlist or fingerprint mismatch")

# Attest every tool call
receipt = attest.record(
    server="filesystem-mcp",
    tool="write_file",
    args={"path": "/tmp/x.md"},
    capability_token=current_dct,
)
```

## When to reach for it

- You use MCP servers in Claude Desktop, Cursor, VS Code, or agent frameworks
- You run third-party MCP servers and need supply-chain visibility
- You're a small team (2-10 devs) — enterprise MCP gateways don't serve you
- You need audit trails that survive when a third-party server gets rug-pulled

## The contract

```
class Policy:
    allowlist: list[str]
    required_fingerprints: dict[str, str]
    denied_tools: list[str]  # e.g., "shell.exec"
    max_payload_bytes: int

Attest.verify_server(name: str, fingerprint: str) -> bool
Attest.record(
    server: str,
    tool: str,
    args: dict,
    capability_token: str | None = None,
) -> Receipt

Attest.scan_response(payload: str) -> list[Finding]
# Checks for known tool-poisoning patterns
```

Maps to OWASP MCP Top 10: Tool Poisoning (LLM01), Server Impersonation (LLM04), Excessive Agency (LLM08), Sensitive Info Disclosure (LLM06).

## See also

- [Delegation Tokens](https://hummbl.io/delegation-tokens.html) — capability tokens that flow into MCP attestation
- [Governance Bus](https://hummbl.io/governance-bus.html) — stores MCP audit receipts
- [MCP Server Audit](https://hummbl.io/../audit/mcp-server.html) — audit your deployed MCP servers
- [hummbl-governance SDK](https://hummbl.io/../docs/hummbl-governance.html#mcp-attestation) — full MCP Attestation API reference
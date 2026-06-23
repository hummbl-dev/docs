# Source: https://hummbl.io/solutions/agent-platforms.html

Builders · Frameworks

# Agent Platforms

Building an agent framework, MCP host, or orchestration platform? Your customers will need governance — audit trails, kill switches, capability attestation. HUMMBL primitives drop in as the layer they import on top of your platform. Compose, don't rebuild.

## Who this is for

- Agent framework authors (LangChain, LlamaIndex, CrewAI, AutoGen, custom internal frameworks)
- MCP server authors and MCP host platforms
- Agent orchestration platforms (workflow engines, task routers, multi-agent coordinators)
- LLM gateway/proxy vendors wanting to add governance as a layer customers can enable

## The composition pattern

Your platform does what it does. HUMMBL primitives sit next to it, as an optional governance layer your customers can turn on. You don't have to build an audit bus, design a capability token system, or write a kill switch. You reference HUMMBL in your docs, show the pattern in an example, and let your customers own the policy.

For your platform, this means: you ship the agent framework, HUMMBL ships the accountability infrastructure. For your enterprise customers, this means: they can point to a governance story that isn't coupled to your platform's long-term availability.

## Integration patterns

- **Middleware integration** — wrap your platform's tool-call dispatch with HUMMBL's [GovernanceBus](https://hummbl.io/../primitives/governance-bus.html) and [DCT](https://hummbl.io/../primitives/delegation-tokens.html) verification
- **Adapter wrapping** — ship your platform's external adapters pre-wrapped in [CircuitBreaker](https://hummbl.io/../primitives/circuit-breaker.html)
- **Kill switch as first-class** — expose HUMMBL's [KillSwitch](https://hummbl.io/../primitives/kill-switch.html) as a platform-level control customers can wire to their incident response
- **MCP attestation** — if you host MCP servers, ship [MCP Attestation](https://hummbl.io/../primitives/mcp-attestation.html) as the default policy layer

## Partnership model

HUMMBL is open source (Apache 2.0). Use it freely. If you want to co-market the integration, cross-link documentation, or build a deeper technical partnership, we're interested. If your customers are asking for governance you don't want to build from scratch, that's the conversation.

For agent platform, framework, and MCP host builders:

[Book a technical integration conversation →](https://cal.com/hummbl/30min)

## See also

- [Browse the primitives](https://hummbl.io/../primitives/)
- [MCP Attestation](https://hummbl.io/../primitives/mcp-attestation.html) — for MCP-specific use cases
- [The HUMMBL method](https://hummbl.io/../method.html) — why libraries beat platforms for regulated customers
- [hummbl-governance on GitHub](https://github.com/hummbl-dev/hummbl-governance)
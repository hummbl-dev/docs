# Source: https://hummbl.io/index.html

## The Governance Tuple

Every governed AI decision produces a triple: **CONTRACT** (what was authorized), **DCT** (who authorized it, cryptographically signed), and **EVIDENCE** (what actually happened). This is the atomic record that makes AI governance auditable.

CONTRACT

Permitted operations, resources, caveats, expiry

×

DCT

HMAC-signed delegation binding issuer → subject

×

EVIDENCE

Actual operations, resources accessed, cost, output

governance\_tuple.py

from hummbl\_governance import DelegationTokenManager, BusWriter, CostGovernor

# CONTRACT: define what the agent may do
contract = {
 "ops\_allowed": \["read", "summarize"\],
 "resources": \["docs/\*"\],
 "expiry": "2026-12-31T23:59:59Z"
}

# DCT: cryptographically bind the delegation
dtm = DelegationTokenManager()
token = dtm.issue(
 issuer="orchestrator",
 subject="summarizer-agent",
 operations=contract\["ops\_allowed"\],
 resources=contract\["resources"\]
)

# EVIDENCE: audit what actually happened
bus = BusWriter("governance.jsonl")
bus.append(agent="summarizer-agent", action="read", resource="docs/report.md")
bus.append(agent="summarizer-agent", action="summarize", resource="docs/report.md")

[Read the Paper →](https://hummbl.io/research.html) [OWASP 10/10 Coverage →](https://hummbl.io/owasp.html)

## Cognitive Layer: Base120 Mental Models

The reasoning substrate that operates _over_ governance primitives. 120 validated mental models across 6 transformation types.

P

Perspective

Frame and anchor viewpoint. Change how you see the problem.

IN

Inversion

Flip to see what avoiding failure reveals. Think backwards.

CO

Composition

Combine for emergent properties. Build complexity from simplicity.

DE

Decomposition

Break complexity down. Understand the parts.

RE

Recursion

Apply patterns at multiple scales. Iterate and refine.

SY

Systems

Understand governing rules. See the meta-patterns.

Need governance for your agents?

Free Readiness Assessment

30-minute call. I'll review your agent architecture against EU AI Act Annex III requirements and tell you where the gaps are.

[Take the Free Assessment →](https://hummbl.io/assessment.html?utm_source=hummbl-homepage&utm_medium=cta&utm_campaign=traffic-activation-2026-06-15)

## Try It Now

Describe a problem you're facing and get recommended mental models instantly. No signup required.

Describe the problem you want model recommendations for Get Recommendations

### Recommended Models

[Explore All 120 Models →](https://hummbl.io/explorer.html)

## Claude Desktop Setup

Install the MCP server to give Claude direct access to all 120 models.

### Step 1: Install

terminal

Copy

$ `npm install -g @hummbl/mcp-server`

### Step 2: Configure

Add to `claude_desktop_config.json`

claude\_desktop\_config.json

Copy

{
 "mcpServers": {
 "hummbl": {
 "command": "npx",
 "args": \["@hummbl/mcp-server"\]
 }
 }
}

### Step 3: Available Tools

- `select_model` Select appropriate mental models for a problem
- `apply_transformation` Apply a transformation type to reframe a problem (P, IN, CO, DE, RE, SY)
- `analyze_problem` Comprehensive analysis using multiple mental models

### Step 4: Available Resources

- `models://all` All 120 mental models
- `models://by-transformation` Models grouped by transformation type
- `relationships://all` Validated relationships between mental models
- `transformations://overview` Overview of the 6 transformations

### Step 5: Available Prompts

- `problem_decomposition` Systematic 6-transformation problem analysis framework

## Use Cases

HUMMBL provides structured reasoning infrastructure for AI systems. Use it via API, Claude Desktop MCP integration, or direct framework integration:

### Agent Frameworks

LangChain, CrewAI, AutoGPT, Semantic Kernel - invoke mental models programmatically to guide agent reasoning.

### Claude Desktop

MCP server gives Claude direct access to all 120 models. Search, retrieve, and apply cognitive frameworks in real-time.

### Custom Applications

REST API for decision support tools, prompt engineering systems, or reasoning-enhanced workflows. No framework required.

### Prompt Engineering

Retrieve relevant mental models based on problem context, then inject into system prompts for better LLM outputs.

### Knowledge Systems

Build cognitive enhancement tools, decision support systems, or structured thinking applications on top of Base120.

### Research & Education

Access validated mental models programmatically for cognitive science research, educational tools, or training systems.

Book a call to see how Base120 fits your use case.

[Schedule Discovery Call →](https://cal.com/hummbl/30min)
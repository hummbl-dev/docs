# Source: https://hummbl.io/primitives/base120.html

Reasoning

# Base120 Models

120 canonical mental models as a structured, queryable API. Classified across six transformation types. The structured-reasoning substrate for agents that need to think about problems in named, auditable ways.

$curl https://api.hummbl.io/v1/models/P1

## What it does

Base120 is a taxonomy of 120 mental models — First Principles, Inversion, Systems Thinking, Pareto, Regression to the Mean, and 115 more — organized into six transformation types: **P**erspective, **I**n version, **CO**mposition, **DE**composition, **RE**cursion, and **SY**stems.

Each model has a code (`P1`, `IN6`, `SY13`), a definition, usage guidance, worked examples, and metadata. Agents can query by problem shape, retrieve by code, or recommend matches against a freeform problem statement.

It ships in two forms today: a free REST API (sub-50ms latency, no auth, Cloudflare edge) and an MCP server for Claude Desktop and other MCP clients. A dedicated Python client package (`hummbl-base120`) is available now — install with `pip install hummbl-base120` (v2, stdlib-only, 148 tests).

## Use it

```
# Retrieve by code
curl https://api.hummbl.io/v1/models/P1

# Recommend for a problem (POST)
curl https://api.hummbl.io/v1/recommend \
  -H 'Content-Type: application/json' \
  -d '{"problem":"How do I prioritize features for my MVP?","limit":5}'
```

```
# Stdlib Python client (no dependency)
import urllib.request, json

def get_model(code: str) -> dict:
    url = f"https://api.hummbl.io/v1/models/{code}"
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())

model = get_model("P1")  # First Principles Framing
print(model["definition"])
```

## When to reach for it

- You want agents that reason explicitly with named, auditable frameworks
- You need structured prompt scaffolds that aren't ad-hoc JSON-prompt soup
- You're building decision-support tooling where "which model was applied" matters
- You want the prompt engineering layer of your agent to be reviewable by humans

## The contract

```
Base120.get(code: str) -> Model
Base120.list(transformation: str | None = None) -> list[Model]
Base120.recommend(problem: str, limit: int = 5) -> list[Recommendation]

class Model:
    code: str            # "P1", "IN6", etc.
    name: str
    transformation: str  # "P", "IN", "CO", "DE", "RE", "SY"
    definition: str
    usage: str
    examples: list[str]
```

API contract frozen under `fm-contracts-v0.1`. Explore the full taxonomy at [the Explorer](https://hummbl.io/../explorer.html).

## See also

- [Base120 Explorer](https://hummbl.io/../explorer.html) — browse all 120 models visually
- [API Playground](https://hummbl.io/../playground.html) — test the recommendation endpoint
- [MCP Attestation](https://hummbl.io/mcp-attestation.html) — governance for the Base120 MCP server
- [hummbl-base120 SDK](https://hummbl.io/../docs/hummbl-base120.html) — full `Engine`, Krineia ledger, CLI, and MCP server reference
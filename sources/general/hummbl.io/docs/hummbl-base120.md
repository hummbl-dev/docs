# Source: https://hummbl.io/docs/hummbl-base120.html

# hummbl-base120

v2.0  ·  Python 3.11+  ·  stdlib-only  ·  Apache 2.0  ·  148 tests  ·  score 100/100

## Install

$pip install hummbl-base120

stdlib-only air-gap ready Python 3.11+ Apache 2.0 148 tests 100/100 audit

Zero third-party runtime dependencies. The 120 models are embedded in the package — no network call required for offline use. The REST API and MCP server require network access but the Python SDK does not.

## 6 transformation families

120 models organized into six families. Each model has a code (`P1`, `IN6`, `SY13`), definition, usage guidance, and worked examples.

P

Perspective / Identity

Frame and anchor point of view. Define what something is.

IN

Inversion

Reverse assumptions. Examine opposites, edges, negations.

CO

Composition

Combine parts into coherent wholes.

DE

Decomposition

Break complex systems into constituent parts.

RE

Recursion

Apply operations iteratively; outputs become inputs.

SY

Systems

Understand systems of systems; coordination and emergence.

## Engine.select()

Select a model by code. Returns the full model object with definition, usage guidance, and examples.

### Import

```
from hummbl_base120 import Engine
```

### Signature

```
Engine.select(code: str) -> Model
# Raises: ModelNotFoundError if code is invalid
```

### Example

```
from hummbl_base120 import Engine

model = Engine.select("P1")
print(model.name)        # "First Principles Framing"
print(model.definition)  # "Break a problem down to its most fundamental..."
print(model.usage)       # "Use when inherited assumptions are blocking..."

# Iterate a transformation family
p_models = Engine.list(transformation="P")
for m in p_models:
    print(m.code, m.name)
```

## Engine.apply()

Apply a transformation type to a problem statement. Returns structured output with the applied framing.

### Signature

```
Engine.apply(
    problem: str,
    transformation: str,     # "P", "IN", "CO", "DE", "RE", or "SY"
    model_code: str | None = None,  # specific model; None = auto-select
) -> TransformationResult
```

### Example

```
from hummbl_base120 import Engine

result = Engine.apply(
    problem="Our deployment pipeline takes 45 minutes",
    transformation="DE",  # Decomposition
)
print(result.model.code)    # "DE1" (Root Cause Analysis)
print(result.reframing)     # The decomposed framing of the problem
print(result.audit_tuple)   # (model_code, transformation, timestamp) for Krineia
```

## Engine.recommend()

Given a freeform problem statement, returns ranked model recommendations. Uses keyword extraction, pattern matching, and synonym expansion — no external API call required.

### Signature

```
Engine.recommend(
    problem: str,
    limit: int = 5,
) -> list[Recommendation]

class Recommendation:
    model: Model
    score: float      # 0.0–1.0
    reason: str       # one-line explanation of why this model fits
```

### Example

```
from hummbl_base120 import Engine

recs = Engine.recommend(
    problem="How do I prioritize features for my MVP?",
    limit=3,
)

for r in recs:
    print(f"{r.model.code}: {r.model.name} (score={r.score:.2f})")
    print(f"  {r.reason}")

# Output:
# DE7: Pareto Decomposition (score=0.87)
#   Focus on the 20% of features delivering 80% of value
# P6: Point-of-View Anchoring (score=0.74)
#   Define whose MVP this is before prioritizing
# IN17: Counterfactual Negation (score=0.71)
#   Ask what a bad MVP would look like, then invert
```

## Model object

The `Model` dataclass returned by all Engine methods:

```
class Model:
    code: str             # "P1", "IN6", "DE7", etc.
    name: str             # Human-readable name
    transformation: str   # "P", "IN", "CO", "DE", "RE", or "SY"
    definition: str       # What this model is
    usage: str            # When and how to use it
    examples: list[str]   # 2-3 worked examples
    related: list[str]    # Codes of related models
```

The full model catalog (120 models) is accessible at [the Explorer](https://hummbl.io/../explorer.html) or via the REST API at `GET /v1/models`. The Python package embeds the catalog at install time — no network required.

## Krineia Ledger — overview

Krineia (formerly named VERUM, renamed 2026-05-04 per HUMMBL namespace audit) is the append-only audit layer inside `hummbl-base120`. It records which reasoning operators were applied, when, and in what sequence — creating a provable governance trace without feeding back into the inference loop. Note: Python module path `hummbl_base120.verum` and the `verum-overview` HTML anchor are retained as intentional migration debt; the public name is Krineia.

Four node fields per entry: **id** (who/what), **time** (when), **state** (current condition), **drift** (deviation from setpoint).

Three operators: `append()`, `project()`, `cut()`. The ledger grows; it never shrinks. External tools inspect it; the system never reads its own log.

## Krineia Ledger — API

### Import

```
from hummbl_base120.verum import Ledger
```

### Constructor

```
Ledger(
    path: Path | str,          # JSONL file path
    agent_id: str,             # Identity of the reasoning agent
)
```

### Key methods

| Method | Returns | Notes |
| --- | --- | --- |
| append(model\_code, context, state, drift) | None | Records an operator application |
| project(since, until) | list\[LedgerEntry\] | Read-only view of a time range |
| cut(threshold) | list\[LedgerEntry\] | Returns entries where drift exceeds threshold |

### Example

```
from pathlib import Path
from hummbl_base120 import Engine
from hummbl_base120.verum import Ledger

ledger = Ledger(path=Path("_state/reasoning.jsonl"), agent_id="analyst-1")

# Apply a model and record the trace
result = Engine.apply(problem="...", transformation="DE")
ledger.append(
    model_code=result.model.code,
    context="feature-prioritization-session",
    state="in_progress",
    drift=0.0,
)

# Audit: what reasoning happened today?
entries = ledger.project(since="2026-04-14T00:00:00Z", until="2026-04-14T23:59:59Z")
for e in entries:
    print(e.model_code, e.timestamp, e.drift)
```

## CLI

The package ships a CLI for quick lookups and recommendations. Available after install:

```
# Get a model by code
python -m hummbl_base120 get P1

# Recommend models for a problem
python -m hummbl_base120 recommend "how do I scale a database"

# List all models in a transformation family
python -m hummbl_base120 list --transformation DE

# List all 120 models as JSON
python -m hummbl_base120 list --json
```

## MCP Server

The package bundles an MCP server exposable to Claude Desktop, Cursor, and other MCP clients. A standalone npm package is also available for Node.js environments.

### Python MCP server (bundled)

```
# Start the MCP server locally
python -m hummbl_base120.mcp_server

# Add to claude_desktop_config.json:
{
  "mcpServers": {
    "hummbl": {
      "command": "python",
      "args": ["-m", "hummbl_base120.mcp_server"]
    }
  }
}
```

### npm MCP server (standalone)

```
npm install -g @hummbl/mcp-server

# claude_desktop_config.json:
{
  "mcpServers": {
    "hummbl": {
      "command": "npx",
      "args": ["@hummbl/mcp-server"]
    }
  }
}
```

### Available MCP tools

| Tool | Description |
| --- | --- |
| select\_model | Get a specific model by code |
| apply\_transformation | Apply a transformation type to a problem |
| analyze\_problem | Multi-model analysis using all 6 transformations |

## REST API

The REST API is an alternative to the Python SDK — no install required. Free, no auth, sub-50ms latency on Cloudflare edge.

```
# Base URL
https://api.hummbl.io

# Get a model
GET /v1/models/P1

# List all models
GET /v1/models

# Recommend
POST /v1/recommend
{"problem": "How do I reduce churn?", "limit": 5}

# List transformations
GET /v1/transformations
```

Full REST API reference: [HUMMBL Docs →](https://hummbl.io/../docs.html)
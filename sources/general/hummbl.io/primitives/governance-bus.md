# Source: https://hummbl.io/primitives/governance-bus.html

Audit

# Governance Bus

Append-only JSONL audit log for every agent action. Assessor-readable in a text editor, grep-friendly from the command line, evidence-preservation compliant out of the box.

$pip install hummbl-governance

## What it does

Every agent action — decision, delegation, API call, error, policy evaluation — writes a single JSON line to an append-only file. No updates, no deletes. Each line is timestamped, actor-attributed, and optionally HMAC-signed.

When an auditor, assessor, GC, or regulator asks for evidence, you give them the file. They open it in whatever tool they want. They can grep for actors, filter by time window, verify signatures, export to their own systems.

The governance bus is the evidence substrate. Every other HUMMBL primitive writes to it. Delegation tokens log issuance and use. Kill switch engagements log timestamps and reasons. Circuit breakers log trips and recoveries.

## Use it

```
from hummbl_governance import BusWriter

bus = BusWriter(bus_path="_state/governance/events.jsonl")

bus.post(
    from_id="agent-claude-1",
    to_id="all",
    msg_type="STATUS",
    message="file.write src/api.py (42 lines added)",
)

# Query later
for event in bus.read_since(timestamp="2026-04-05T00:00:00Z"):
    print(event.from_id, event.msg_type, event.message)
```

## When to reach for it

- You need a defensible audit trail for AI-generated or agent-executed actions
- Your compliance team or assessor needs portable, human-readable evidence
- You're preparing for SOC 2 Type II, ISO 42001, or EU AI Act documentation
- Your agents run in air-gapped or regulated environments where SaaS auditing is blocked

## The contract

```
BusWriter(
    bus_path: str | Path,
    *,
    policy: PolicyLevel = PolicyLevel.PERMISSIVE,
)

BusWriter.post(
    from_id: str,       # Actor / sender
    to_id: str,         # Recipient ("all" for broadcast)
    msg_type: str,      # STATUS | SITREP | DECISION | ...
    message: str,
    *,
    timestamp: str | None = None,
    validate: bool = True,
) -> None

BusWriter.read_all() -> list[Message]
BusWriter.read_since(timestamp: str) -> list[Message]
```

Wire format is frozen under `fm-contracts-v0.1`. Breaking changes require a SemVer major bump and a new baseline tag.

## See also

- [Delegation Tokens](https://hummbl.io/delegation-tokens.html) — attribution for bus writes
- [Kill Switch](https://hummbl.io/kill-switch.html) — emergency halt, logs engagement to bus
- [Circuit Breaker](https://hummbl.io/circuit-breaker.html) — state transitions logged to bus
- [hummbl-governance SDK](https://hummbl.io/../docs/hummbl-governance.html#governance-bus) — full `BusWriter` API reference
# Source: https://hummbl.io/docs/hummbl-governance.html

# hummbl-governance

v0.4.0  ·  Python 3.11+  ·  stdlib-only  ·  Apache 2.0  ·  546 tests  ·  score 99.5/100

## Install

$pip install hummbl-governance

stdlib-only air-gap ready Python 3.11+ Apache 2.0 546 tests

Zero third-party runtime dependencies. Works on air-gapped deployments, Docker without internet access, and regulated environments that prohibit external packages.

Test dependencies (`pytest`, `coverage`) are optional: `pip install hummbl-governance[test]`.

## Module index

Six primitives in one package. Import what you need:

DelegationTokenManager

HMAC-SHA256 signed capability tokens. Scope, chain depth, expiry. Every agent action traceable to an authorized delegation.

[→ DelegationTokenManager reference](https://hummbl.io/#delegation-tokens)

BusWriter

Append-only JSONL audit log. Never mutated. Assessor-readable. Grep-friendly. Evidence-preservation compliant.

[→ BusWriter reference](https://hummbl.io/#governance-bus)

KillSwitch

Four-mode emergency halt (DISENGAGED → HALT\_NONCRITICAL → HALT\_ALL → EMERGENCY). File-system-persisted. Survives process restart.

[→ KillSwitch reference](https://hummbl.io/#kill-switch)

CircuitBreaker

CLOSED/HALF\_OPEN/OPEN state machine. Wraps any external adapter call. Auto-recovery with configurable thresholds.

[→ CircuitBreaker reference](https://hummbl.io/#circuit-breaker)

CapabilityFence (Delegation Context)

Scope-narrowing for nested agent delegations. Prevents privilege escalation. Context manager + token binding.

[→ CapabilityFence reference](https://hummbl.io/#capability-fence)

MCP Attestation

Server allowlists, capability tokens, and tool-poisoning defense for MCP-native agent systems.

[→ MCP Attestation reference](https://hummbl.io/#mcp-attestation)

## DelegationTokenManager

HMAC-SHA256 signed capability tokens for agent authority. Every token carries scope, chain depth limit, and expiry. Feature-flagged via `ENABLE_IDP=true`.

Primitive page: [Delegation Tokens →](https://hummbl.io/../primitives/delegation-tokens.html)

### Import

```
from hummbl_governance import DelegationTokenManager
from hummbl_governance.delegation import TokenBinding
```

### Constructor

```
DelegationTokenManager(
    secret: bytes | None = None,
    # If None, generates a random secret. Pass bytes for reproducible tokens.
)
```

### Key methods

| Method | Returns | Notes |
| --- | --- | --- |
| create\_token(agent\_id, scope, ttl, chain\_depth) | str | Signs and returns base64url token |
| validate\_token(token) | TokenBinding | None | None if expired, invalid sig, or depth exceeded |
| check\_least\_privilege(token, op) | bool | True if op is within token scope |

### Example

```
import os
from hummbl_governance import DelegationTokenManager

os.environ["ENABLE_IDP"] = "true"
mgr = DelegationTokenManager()

# Issue a token for an agent
token = mgr.create_token(
    agent_id="research-agent-1",
    scope=["read:docs", "write:drafts"],
    ttl=3600,          # seconds
    chain_depth=2,     # can sub-delegate once
)

# Validate before executing
binding = mgr.validate_token(token)
if binding and mgr.check_least_privilege(token, op="write:drafts"):
    write_draft(content)
```

## BusWriter

Append-only JSONL audit log. Every write is a line. Lines are never deleted or modified. The log is the proof of governance.

Primitive page: [Governance Bus →](https://hummbl.io/../primitives/governance-bus.html)

### Import

```
from hummbl_governance import BusWriter
```

### Constructor

```
BusWriter(
    bus_path: str | Path,                    # Path to the JSONL audit file
    *,
    policy: PolicyLevel = PolicyLevel.PERMISSIVE,
)
```

### Key methods

| Method | Returns | Notes |
| --- | --- | --- |
| post(msg\_type, message, metadata) | None | Appends a timestamped JSONL entry |
| read\_since(timestamp) | list\[Message\] | Returns entries after given ISO timestamp |
| read\_all() | list\[Message\] | Returns all entries in the log |
| message\_count() | int | Number of entries in the log |

### Example

```
from pathlib import Path
from hummbl_governance import BusWriter

bus = BusWriter(
    bus_path=Path("_state/governance_bus.jsonl"),
)

# Log an action
bus.post(
    msg_type="ACTION",
    message="fetched arxiv paper 2401.00001",
    metadata={"source": "arxiv", "doi": "2401.00001"},
)

# Read recent activity
for entry in bus.read_since("2026-04-14T00:00:00Z"):
    print(entry.from_id, entry.msg_type, entry.message)
```

Wire format is frozen under `fm-contracts-v0.1`. Each JSONL line contains: `timestamp`, `from_id`, `msg_type`, `message`, and optional `metadata`. Never use raw `open().write()` — always use `BusWriter` to preserve append-only integrity.

## KillSwitch

Four-mode emergency halt. File-system-persisted state survives process restart. Non-delegable: no agent can override the kill switch.

Primitive page: [Kill Switch →](https://hummbl.io/../primitives/kill-switch.html)

### Import

```
from hummbl_governance import KillSwitch, KillSwitchMode
```

### Modes

| Mode | Effect |
| --- | --- |
| DISENGAGED | Normal operation |
| HALT\_NONCRITICAL | Non-critical agents pause; critical tasks continue |
| HALT\_ALL | All agent actions blocked |
| EMERGENCY | Halt + alerting + state snapshot |

### Constructor

```
KillSwitch(
    state_dir: Path | None = None,       # Default: ./_state/
    require_hmac: bool = True,
    signing_secret: bytes | None = None,
    critical_tasks: frozenset[str] | None = None,
)
```

### Example

```
from pathlib import Path
from hummbl_governance import KillSwitch, KillSwitchMode

ks = KillSwitch(state_dir=Path("_state"))

# Check before every agent action
if ks.check_task_allowed(task.id):
    agent.execute(task)
else:
    logger.info("halted: %s", ks.get_status())

# Engage from anywhere in your system
ks.engage(
    mode=KillSwitchMode.HALT_ALL,
    reason="anomaly detected in prod",
    triggered_by="ops-agent-1",
)

# Release after incident resolution
ks.disengage(reason="incident resolved", triggered_by="ops-agent-1")
```

## CircuitBreaker

Wraps any callable — LLM API, vector store, webhook — and isolates failures. Prevents cascading degradation and runaway cost from retrying failing paid APIs.

Primitive page: [Circuit Breaker →](https://hummbl.io/../primitives/circuit-breaker.html)

### Import

```
from hummbl_governance import CircuitBreaker, CircuitBreakerState
```

### Constructor

```
CircuitBreaker(
    failure_threshold: int = 5,          # failures before OPEN
    recovery_timeout: float = 30.0,      # seconds before HALF_OPEN probe
    on_state_change: Callable | None = None,
)
```

### Key methods

| Method / Property | Returns | Notes |
| --- | --- | --- |
| call(fn, \*args, \*\*kwargs) | Any | Records success/failure; raises if OPEN |
| .state | CircuitBreakerState | CLOSED / HALF\_OPEN / OPEN |
| .failure\_count | int | Consecutive failures since last reset |
| .success\_count | int | Successes in HALF\_OPEN state |
| reset() | None | Force transition to CLOSED |

### Example

```
from hummbl_governance import CircuitBreaker, CircuitBreakerState

cb = CircuitBreaker(failure_threshold=5, recovery_timeout=30.0)

try:
    result = cb.call(anthropic_client.messages.create, **params)
except Exception:
    result = fallback_handler()

if cb.state == CircuitBreakerState.OPEN:
    logger.warning("anthropic-api breaker is open")
```

## CapabilityFence

Scope-narrowing context manager for multi-agent delegation chains. Prevents privilege escalation. Can be created standalone or bound to a delegation token.

Primitive page: [Delegation Context →](https://hummbl.io/../primitives/delegation-context.html)

### Import

```
from hummbl_governance import CapabilityFence, CapabilityDenied
```

### Constructor

```
CapabilityFence(
    allowed: list[str] | None = None,
    denied: list[str] | None = None,
    audit_log: list[CapabilityAuditEntry] | None = None,
)
```

### Key methods

| Method | Returns | Notes |
| --- | --- | --- |
| check(capability) | bool | True if capability is allowed and not denied |
| guard(capability) | context manager | Raises CapabilityDenied on violation |
| CapabilityFence.from\_delegation\_token(token, denied) | CapabilityFence | Classmethod; derives fence from token scope |

### Example

```
from hummbl_governance import CapabilityFence, CapabilityDenied

fence = CapabilityFence(
    allowed=["read:docs", "write:drafts"],
    denied=["deploy:prod", "delete:*"],
)

# Explicit check
if fence.check("write:drafts"):
    write_draft(content)

# Context manager — raises on violation
with fence.guard("read:docs"):
    read_docs()

# Bind to a delegation token
fence_from_token = CapabilityFence.from_delegation_token(
    token,
    denied=["deploy:prod"],
)
```

## MCP Attestation

Local-first governance for MCP-native agents. Server allowlists, capability tokens per server, tool-poisoning defense, and audit receipts for every tool call.

Primitive page: [MCP Attestation →](https://hummbl.io/../primitives/mcp-attestation.html)

MCP Attestation is a Design Preview targeting v0.3. Ships with `hummbl-governance` as an optional extra: `pip install hummbl-governance[mcp]`.

### Import

```
from hummbl_governance.mcp import Attest, Policy
```

### Example

```
from hummbl_governance.mcp import Attest, Policy

policy = Policy.from_file("~/.hummbl/mcp-allowlist.yaml")
attest = Attest(policy=policy, bus_path="_state/mcp_bus.jsonl")

# Verify before connecting to a server
if attest.verify_server("postmark-mcp", fingerprint=FINGERPRINT):
    client.connect("postmark-mcp")
else:
    log.error("server not in allowlist")

# Generate an audit receipt for every tool call
receipt = attest.record(
    server="filesystem-mcp",
    tool="write_file",
    args={"path": "/tmp/x.md"},
    capability_token=current_token,
)
```

## Feature flags

Some primitives are feature-flagged to allow gradual adoption in existing codebases:

| Flag | Enables | Default |
| --- | --- | --- |
| ENABLE\_IDP=true | DelegationTokenManager, CapabilityFence token binding | false |
| BUS\_SECURITY\_POLICY=strict | Reject unregistered bus senders | warn |

Set in environment or `.env`. Feature flags are checked at runtime, not import time.

## Contracts

Wire formats for `BusWriter` and `DelegationTokenManager` are frozen under `fm-contracts-v0.1`. Breaking changes require a SemVer major bump and a new baseline tag.

The contracts directory (`contracts/` in the source repo) is the source of truth. If your code checks for specific JSONL fields, pin to a released version and test against the schema.

Source: [github.com/hummbl-dev/hummbl-governance →](https://github.com/hummbl-dev/hummbl-governance)
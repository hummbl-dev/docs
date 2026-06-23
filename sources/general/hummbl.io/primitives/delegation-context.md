# Source: https://hummbl.io/primitives/delegation-context.html

Scope

# Delegation Context

Chain-depth enforcement for agent delegation. Ensures that an agent cannot escalate its authority by chaining delegations past a configured depth — the classic confused-deputy problem, solved.

$pip install hummbl-governance

## What it does

When a parent agent delegates to a worker, the resulting Delegation Context (DCTX) tracks: who delegated, at what depth, with what scope, and for how long. The worker can further delegate — but each hop decrements depth. When depth reaches zero, delegation stops.

DCTX also tracks the _scope narrowing_ constraint: every re-delegation must be a subset of the parent's scope. A worker cannot synthesize new authority that its parent didn't have. This prevents the confused-deputy problem where a lightly-trusted agent gets upstream capabilities by asking a more-trusted parent to relay.

DCTX is Singapore Agentic AI Framework's "delegation chain depth limits and identity verification" requirement, implemented as a Python primitive.

## Use it

```
from hummbl_governance import CapabilityFence, CapabilityDenied

# Build a fence directly from an allow list
fence = CapabilityFence(
    allowed=["read:docs", "write:drafts"],
    denied=["deploy:prod", "delete:*"],
)

# Check before acting
if fence.check("write:drafts"):
    write_draft(content)

# Guard around a callable — raises CapabilityDenied on violation
with fence.guard("read:docs"):
    read_docs()

# Or bind a fence to a delegation token (scope narrowing)
fence_from_tok = CapabilityFence.from_delegation_token(
    token,
    denied=["deploy:prod"],
)
```

## When to reach for it

- You run supervisor/worker multi-agent architectures
- You need to satisfy Singapore Agentic AI delegation governance requirements
- You need to prove scope-narrowing for audit (regulators love this)
- You've already been bitten by confused-deputy or privilege-escalation bugs

## The contract

```
CapabilityFence(
    allowed: list[str] | None = None,
    denied: list[str] | None = None,
    audit_log: list[CapabilityAuditEntry] | None = None,
)

CapabilityFence.check(capability: str) -> bool
CapabilityFence.guard(capability: str)  # context manager, raises CapabilityDenied

@classmethod
CapabilityFence.from_delegation_token(
    token,
    denied: list[str] | None = None,
    audit_log: list[CapabilityAuditEntry] | None = None,
) -> "CapabilityFence"
```

Works with or without Delegation Tokens — you can wrap DCTX around a token chain or use it as pure in-process scope enforcement.

## See also

- [Delegation Tokens](https://hummbl.io/delegation-tokens.html) — the cryptographic layer under DCTX
- [Governance Bus](https://hummbl.io/governance-bus.html) — logs delegation events and scope decisions
- [hummbl-governance SDK](https://hummbl.io/../docs/hummbl-governance.html#capability-fence) — full `DelegationContext` API reference
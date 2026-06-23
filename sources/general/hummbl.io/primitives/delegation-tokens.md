# Source: https://hummbl.io/primitives/delegation-tokens.html

Identity

# Delegation Tokens

HMAC-SHA256 signed capability tokens that carry scope, chain-depth, and expiry. Runtime attribution for every agent action — so when you need to answer "which agent did this, and who authorized it," the evidence is cryptographic.

$pip install hummbl-governance

## What it does

When an agent wants to act on a resource, it presents a Delegation Capability Token (DCT). The token is signed with a shared secret, carries the exact scope being exercised, and has an expiry. Every downstream system verifies the signature before executing.

Tokens can be chained: a supervisor agent issues a DCT to a worker agent, scoped narrower than its own. The worker can further delegate, but chain depth is enforced — it cannot escalate by chaining past the configured maximum.

Every issuance, use, and revocation writes to the Governance Bus. When an auditor asks "show me who had what authority when," the answer is a grep.

## Use it

```
from hummbl_governance import DelegationTokenManager
from hummbl_governance.delegation import TokenBinding

mgr = DelegationTokenManager(secret=SHARED_SECRET)

# Issue a token
token = mgr.create_token(
    issuer="supervisor-agent",
    subject="agent-worker-1",
    ops_allowed=["read:docs", "write:drafts"],
    binding=TokenBinding(task_id="task-42"),
    expiry_minutes=60,
)

# Validate + act
ok, reason = mgr.validate_token(
    token,
    expected_subject="agent-worker-1",
    expected_task_id="task-42",
)
if ok:
    write_draft(content)
else:
    raise PermissionError(f"insufficient authority: {reason}")

# Check least-privilege against an operation
mgr.check_least_privilege(token, op="write:drafts")
```

## When to reach for it

- You run multi-agent systems where authority needs to flow between agents
- You need runtime attribution: "which agent, with what authority, acted on what"
- You need to satisfy NIST AI RMF, ISO 42001, or EU AI Act evidence requirements
- You want cryptographic proof for post-incident forensics, not just logs

## The contract

```
DelegationTokenManager(secret: bytes | None = None)

DelegationTokenManager.create_token(
    issuer: str,
    subject: str,
    ops_allowed: list[str],
    binding: TokenBinding,
    resource_selectors: list[ResourceSelector] | None = None,
    caveats: list[Caveat] | None = None,
    expiry_minutes: int | None = 120,
) -> DelegationToken

DelegationTokenManager.validate_token(
    token: DelegationToken,
    expected_task_id: str | None = None,
    expected_contract_id: str | None = None,
    expected_subject: str | None = None,
) -> tuple[bool, str | None]  # (ok, reason_if_denied)

DelegationTokenManager.check_least_privilege(
    token, op: str,
) -> bool
```

Signing uses HMAC-SHA256 (stdlib `hmac`). Tokens are base64url-encoded JSON payloads. Feature-flagged via `ENABLE_IDP=true`.

## See also

- [Delegation Context](https://hummbl.io/delegation-context.html) — chain-depth enforcement across calls
- [Governance Bus](https://hummbl.io/governance-bus.html) — where issuances and uses are logged
- [Kill Switch](https://hummbl.io/kill-switch.html) — fleet halt can invalidate all tokens
- [hummbl-governance SDK](https://hummbl.io/../docs/hummbl-governance.html#delegation-tokens) — full `DelegationTokenManager` API reference
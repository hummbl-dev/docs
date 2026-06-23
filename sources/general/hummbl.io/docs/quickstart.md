# Source: https://hummbl.io/docs/quickstart.html

# Quickstart

Zero to a governed AI agent in 5 minutes. Stdlib-only, copy-paste ready. No accounts. No SaaS. No dashboard.

01 Install

One package, no third-party dependencies.

$pip install hummbl-governance

Requires Python 3.11+. Works in any environment including Docker without internet access and air-gapped deployments. If you want the mental models layer too:

$pip install hummbl-governance hummbl-base120

02 Wire the kill switch first

The kill switch is the first thing to wire. It's the one control that cannot be overridden by any agent. Every agent action should check it before executing.

```
from pathlib import Path
from hummbl_governance import KillSwitch, KillSwitchMode

# Create once; state is file-system-persisted
ks = KillSwitch(state_dir=Path("_state"))

# The check: every agent loop starts here
if ks.engaged():
    print("halted:", ks.get_status())
    raise SystemExit(0)

# Your agent logic goes here
print("system is running normally")
```

`state_dir` defaults to `./_state/`. The kill switch persists its mode in a signed state file — it survives process restarts, container rebuilds, and reboots.

03 Issue a delegation token

Delegation tokens give each agent a signed scope. Every action is traceable to an authorized delegation. Enable the IDP feature flag first.

```
import os
from hummbl_governance import DelegationTokenManager

os.environ["ENABLE_IDP"] = "true"

mgr = DelegationTokenManager()

# Issue a token for this agent session
token = mgr.create_token(
    agent_id="research-agent-1",
    scope=["read:docs", "write:drafts"],
    ttl=3600,      # 1 hour
    chain_depth=1, # can sub-delegate once
)

# Verify scope before each action
if mgr.check_least_privilege(token, op="write:drafts"):
    write_draft(content)
else:
    raise PermissionError("agent not authorized for write:drafts")
```

04 Log every action to the governance bus

The governance bus is the audit trail. Append-only JSONL. Every agent action gets a timestamped, identity-tagged entry. This is what an assessor reads.

```
from pathlib import Path
from hummbl_governance import BusWriter

bus = BusWriter(
    log_path=Path("_state/governance_bus.jsonl"),
    agent_id="research-agent-1",
)

# Log before acting
bus.write(
    msg_type="ACTION",
    message="writing draft: product-spec-v1.md",
    metadata={"token": token[:16] + "...", "scope": "write:drafts"},
)

# The action
write_draft(content, path="product-spec-v1.md")

# Log the result
bus.write(
    msg_type="RECEIPT",
    message="draft complete",
    metadata={"lines": 142, "path": "product-spec-v1.md"},
)
```

The bus log is plain JSONL. An assessor can read it with `cat` or `grep`. No database, no tool required. This is what "assessor-readable" means.

05 Full working example

All four primitives wired together. Copy-paste this into a single file, run it, and you have a governed agent loop.

```
"""
governed_agent.py — minimal governed AI agent
Requires: pip install hummbl-governance
Python 3.11+, stdlib-only
"""
import os
from pathlib import Path
from hummbl_governance import (
    KillSwitch, KillSwitchMode,
    DelegationTokenManager,
    BusWriter,
    CircuitBreaker,
)

os.environ["ENABLE_IDP"] = "true"

# ── 1. State directory ────────────────────────────────────────────
state = Path("_state")
state.mkdir(exist_ok=True)

# ── 2. Kill switch ────────────────────────────────────────────────
ks = KillSwitch(state_dir=state)
if ks.engaged():
    raise SystemExit(f"kill switch active: {ks.get_status()}")

# ── 3. Delegation token ───────────────────────────────────────────
mgr = DelegationTokenManager()
token = mgr.create_token(
    agent_id="research-agent-1",
    scope=["read:web", "write:drafts"],
    ttl=3600,
    chain_depth=1,
)

# ── 4. Governance bus ─────────────────────────────────────────────
bus = BusWriter(
    log_path=state / "governance_bus.jsonl",
    agent_id="research-agent-1",
)

# ── 5. Circuit breaker (wrap any external call) ───────────────────
cb = CircuitBreaker(failure_threshold=3, recovery_timeout=60.0)

# ── 6. Governed agent loop ────────────────────────────────────────
def fetch_page(url: str) -> str:
    import urllib.request
    with urllib.request.urlopen(url, timeout=10) as r:
        return r.read().decode()

tasks = [
    "https://api.hummbl.io/health",
]

for url in tasks:
    # Check kill switch before each task
    if ks.engaged():
        bus.write("HALT", f"kill switch engaged mid-loop: {url}")
        break

    # Check authorization
    if not mgr.check_least_privilege(token, op="read:web"):
        bus.write("DENIED", f"no scope for read:web — skipping {url}")
        continue

    bus.write("ACTION", f"fetching {url}", metadata={"token_prefix": token[:12]})

    try:
        result = cb.call(fetch_page, url)
        bus.write("RECEIPT", f"fetched {url}", metadata={"bytes": len(result)})
        print(f"[OK] {url}: {len(result)} bytes")
    except Exception as e:
        bus.write("ERROR", f"failed {url}: {e}")
        print(f"[ERR] {url}: {e}")

print(f"\nAudit log: {state / 'governance_bus.jsonl'}")
```

### What just happened

- The kill switch checked system state before the loop started and before each task
- Every action was authorized against a scoped delegation token
- Every action and result was logged with agent identity and timestamp
- External network calls were wrapped in a circuit breaker to prevent cascading failures
- The audit log at `_state/governance_bus.jsonl` proves all of the above happened

Run it:

$python governed\_agent.py

Then read the audit log:

$cat \_state/governance\_bus.jsonl

## Next steps

[SDK Reference\\ \\ Full API signatures for all six primitives](https://hummbl.io/hummbl-governance.html) [hummbl-base120\\ \\ Add 120 mental models to your agent](https://hummbl.io/hummbl-base120.html) [EU AI Act Readiness\\ \\ 12-question compliance assessment](https://hummbl.io/../readiness/eu-ai-act.html) [Primitive Guides\\ \\ Deep dives on each governance primitive](https://hummbl.io/../primitives/) [Get Help\\ \\ Work directly with Reuben to wire governance](https://hummbl.io/../consulting.html)
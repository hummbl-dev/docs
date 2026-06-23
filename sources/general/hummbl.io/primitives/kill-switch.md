# Source: https://hummbl.io/primitives/kill-switch.html

Safety

# Kill Switch

Four-mode emergency halt for agent systems. Runtime-enforced, file-system-persisted, and survives process restart. When something goes wrong, you need one control that stops everything — fast.

$pip install hummbl-governance

## What it does

The kill switch defines four modes: `DISENGAGED` (normal operation), `HALT_NONCRITICAL` (agents pause non-essential work, critical paths continue), `HALT_ALL` (all agent actions blocked), and `EMERGENCY` (halt + alerting + state snapshot).

The mode lives in a single file. Every agent checks that file before every action. Setting the mode from anywhere — API, CLI, or just editing the file — halts the fleet in under two seconds.

File-system-persisted means the halt survives a process crash, a restart, or a machine reboot. The safety state is sticky until explicitly cleared.

## Use it

```
from pathlib import Path
from hummbl_governance import KillSwitch, KillSwitchMode

ks = KillSwitch(state_dir=Path("_state"))

# Engage from anywhere
ks.engage(
    mode=KillSwitchMode.HALT_ALL,
    reason="anomaly detected in prod",
    triggered_by="ops-agent-1",
)

# Check before acting
if not ks.engaged():
    agent.execute(task)
else:
    logger.info("halted: %s", ks.get_status())

# Release
ks.disengage(reason="incident resolved", triggered_by="ops-agent-1")
```

## When to reach for it

- You run autonomous agents and need a single button to halt the fleet
- You need a non-delegable, non-overridable safety control for incident response
- You're deploying into regulated environments that require documented halt capability
- You're worried about runaway autonomous loops or cost-burn scenarios

## The contract

```
class KillSwitchMode(Enum):
    DISENGAGED = "disengaged"
    HALT_NONCRITICAL = "halt_noncritical"
    HALT_ALL = "halt_all"
    EMERGENCY = "emergency"

KillSwitch(
    state_dir: Path | None = None,
    require_hmac: bool = True,
    signing_secret: bytes | None = None,
    critical_tasks: frozenset[str] | None = None,
)

KillSwitch.engage(mode, reason, triggered_by, affected_tasks=0) -> KillSwitchEvent
KillSwitch.disengage(reason, triggered_by) -> KillSwitchEvent
KillSwitch.mode() -> KillSwitchMode
KillSwitch.engaged() -> bool
KillSwitch.get_status() -> dict
```

All engagements and releases are written to the Governance Bus. State file uses atomic rename for concurrent-safety.

## See also

- [Governance Bus](https://hummbl.io/governance-bus.html) — logs engagement/release events
- [Circuit Breaker](https://hummbl.io/circuit-breaker.html) — per-adapter degradation, complementary to kill switch
- [Delegation Tokens](https://hummbl.io/delegation-tokens.html) — tokens can be revoked via kill switch
- [hummbl-governance SDK](https://hummbl.io/../docs/hummbl-governance.html#kill-switch) — full `KillSwitch` API reference
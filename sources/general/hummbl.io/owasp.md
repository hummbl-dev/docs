# Source: https://hummbl.io/owasp.html

Security Coverage

# OWASP Top 10 for 
Agentic Applications

How hummbl-governance addresses every risk in the [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/). Every claim below links to source code and tests.

10/10

Risks Covered

1032

Tests

26

Primitives

0

Dependencies

ASI01 Agent Goal Hijack

Attackers manipulate an agent's planning or objective by injecting malicious instructions through prompts, documents, or tool outputs.

HUMMBL Mitigation

[`KillSwitch`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/kill_switch.py) provides 4-mode graduated shutdown (DISENGAGED → HALT\_NONCRITICAL → HALT\_ALL → EMERGENCY). Survives process restart via filesystem persistence. Stops hijacked agents mid-execution.

27 tests · [test\_kill\_switch.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_kill_switch.py)

ASI02 Tool Misuse & Exploitation

Agents misuse legitimate tools when excessive permissions or unsafe interfaces enable unintended actions.

HUMMBL Mitigation

[`CapabilityFence`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/capability_fence.py) enforces allowlist/blocklist per tool. Agents cannot invoke tools outside their granted capabilities. Deny-by-default.

27 tests · [test\_capability\_fence.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_capability_fence.py)

ASI03 Identity & Privilege Abuse

Agents improperly inherit, misuse, or retain privileges across sessions, users, or delegated workflows.

HUMMBL Mitigation

[`DelegationTokenManager`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/delegation.py) issues HMAC-signed scoped tokens with chain-depth limits. [`AgentRegistry`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/identity.py) tracks canonical identities, trust tiers, and alias resolution.

42 tests · [test\_delegation.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_delegation.py) + [test\_identity.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_identity.py)

ASI04 Supply Chain Vulnerabilities

Agents dynamically load prompts, plugins, tools, and models at runtime — introducing risk from compromised third-party components.

HUMMBL Mitigation

Zero third-party runtime dependencies. Python stdlib only. `pip audit` finds nothing because there is nothing to audit. No transitive dependency tree to compromise.

Verified by CI · `pip install hummbl-governance` pulls 0 packages

ASI05 Unexpected Code Execution

Agents that generate or execute code can be manipulated into running malicious instructions via prompt injection.

HUMMBL Mitigation

[`OutputValidator`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/output_validator.py) with `InjectionDetector` scans agent outputs for prompt injection patterns, blocked terms, PII leakage, and missing provenance before downstream consumption.

49 tests · [test\_output\_validator.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_output_validator.py)

ASI06 Memory & Context Poisoning

Attackers inject malicious data into memory systems that influence future agent reasoning.

HUMMBL Mitigation

[`BusWriter`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/coordination_bus.py) enforces append-only semantics with content hashing. [`AuditLog`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/audit_log.py) provides tamper-evident logging. Poisoned entries are cryptographically detectable.

80 tests · [test\_coordination\_bus.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_coordination_bus.py) + [test\_audit\_log.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_audit_log.py)

ASI07 Insecure Inter-Agent Communication

Multi-agent systems communicating without authentication or message integrity are vulnerable to spoofing and replay attacks.

HUMMBL Mitigation

[`LamportClock`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/lamport_clock.py) provides causal ordering for distributed agent messages. [`ContractNetManager`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/contract_net.py) implements structured multi-agent task allocation with bid verification.

37 tests · [test\_lamport\_clock.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_lamport_clock.py) + [test\_contract\_net.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_contract_net.py)

ASI08 Cascading Failures

A single failure propagates across agents or tenants, causing automation storms and systemic impact.

HUMMBL Mitigation

[`CircuitBreaker`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/circuit_breaker.py) isolates failing components with CLOSED/HALF\_OPEN/OPEN state machine. [`HealthProbe`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/health_probe.py) detects degradation before cascade. [`CostGovernor`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/cost_governor.py) enforces budget ceilings to prevent runaway spend.

63 tests · [test\_circuit\_breaker.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_circuit_breaker.py) + [test\_health\_probe.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_health_probe.py) + [test\_cost\_governor.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_cost_governor.py)

ASI09 Human-Agent Trust Exploitation

Humans over-trust confident agent outputs and approve dangerous actions without adequate review.

HUMMBL Mitigation

[`ReasoningEngine`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/reasoning.py) generates structured decision traces that explain _why_ a governance decision was made. [`ComplianceMapper`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/compliance_mapper.py) maps decisions to external frameworks (NIST, ISO) for independent validation.

41 tests · [test\_explain.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_explain.py) + [test\_compliance\_mapper.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_compliance_mapper.py)

ASI10 Rogue Agents

Agents drift from intended behavior due to model updates, memory mutation, or emergent multi-step behavior not anticipated at design time.

HUMMBL Mitigation

[`BehaviorMonitor`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/reward_monitor.py) detects behavioral drift via Jensen-Shannon divergence and entropy collapse. [`GovernanceLifecycle`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/lifecycle.py) enforces state machine transitions (PROVISIONED → ACTIVE → SUSPENDED → DECOMMISSIONED).

37 tests · [test\_reward\_monitor.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_reward_monitor.py) + [test\_lifecycle.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_lifecycle.py)

## Start in 30 seconds

Every primitive above ships in one package. No frameworks. No lock-in. No dependencies.

pip install hummbl-governance

For the formal governance primitive underlying all 10 mitigations, see [The Governance Tuple](https://doi.org/10.5281/zenodo.19646940) (Bowlby, 2026).
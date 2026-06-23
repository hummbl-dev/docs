# Source: https://hummbl.io/security.html

# Security

HUMMBL builds governance infrastructure. Taking security seriously is table stakes. Here is how to reach us, and what we're doing.

## Responsible Disclosure

If you believe you've found a security vulnerability in a HUMMBL product, service, or domain, please report it privately before public disclosure.

**Security contact** 
[/.well-known/security.txt](https://hummbl.io/.well-known/security.txt) 
 
**Fallback** 
[Schedule private report](https://cal.com/hummbl/30min) 
 
**Machine-readable contact** 
[/.well-known/security.txt](https://hummbl.io/.well-known/security.txt)

What to include:

1. Description of the issue and affected component
2. Steps to reproduce (or proof-of-concept)
3. Impact assessment
4. Any suggested remediation (optional — welcome but not required)

What to expect:

1. Acknowledgment within 72 hours (HUMMBL is solo-operated; we aim for faster)
2. Triage and severity assignment within 7 days of acknowledgment
3. Remediation timeline scoped to severity — critical within 14 days, high within 30 days, medium within 90 days
4. Credit in the disclosure changelog if you'd like it (or anonymous if you prefer)

We ask that you do not exploit the vulnerability, do not access data beyond what's needed to demonstrate the issue, and give us reasonable time to remediate before public disclosure.

## Security Posture

### Runtime Dependencies

**Zero** — hummbl-governance is Python stdlib-only. No supply chain for an attacker to poison.

### Security Scanning

Bandit (Python) + Semgrep + pip-audit run on every push. Bandit fails on HIGH; Semgrep blocks on ERROR.

### Secrets Handling

No credentials committed. Tests scan for and reject `sk-` patterns and similar tokens.

### Audit Trail

Governance bus is append-only JSONL. Every agent action produces a signed, timestamped receipt.

### Signed Delegation

HMAC-SHA256 signed capability tokens with scope and chain-depth enforcement.

### Kill Switch

4-mode runtime halt (DISENGAGED, HALT\_NONCRITICAL, HALT\_ALL, EMERGENCY). File-system-persisted.

## Compliance Posture

Programs we are actively aligning against:

- NIST AI Risk Management Framework 1.0 (AI RMF)
- ISO/IEC 42001:2023 AI management system standard
- EU AI Act high-risk system requirements (expected Dec 2 2027 per May 2026 provisional agreement)
- SOC 2 Type II In planning
- CMMC 2.0 Level 2 mapping In progress

HUMMBL is a solo operation building toward enterprise-grade compliance. We publish our posture honestly — including what's not yet done.

## What We Don't Do

- We do not run bug bounties (yet) — we haven't validated the economic model as a solo operator.
- We do not gate vulnerability reports behind legal paperwork — report first, we'll work out terms together.
- We do not punish researchers for good-faith disclosure. Ever.

## GitHub Security Advisories

Published security advisories are listed at [github.com/hummbl-dev/hummbl-governance/security/advisories](https://github.com/hummbl-dev/hummbl-governance/security/advisories).
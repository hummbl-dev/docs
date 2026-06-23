# Source: https://hummbl.io/validation.html

Reference

# Validation Metrics

How HUMMBL reports validation metrics: what test counts, audit scores, checks, and deployments mean, and how public repo metrics differ from aggregate validation.

## Four things we measure

HUMMBL publishes four kinds of validation signals. They are related but not interchangeable.

| Signal | What it counts | Example | Scope |
| --- | --- | --- | --- |
| **Tests** | Automated unit, integration, and property tests | 1,032 passing tests in hummbl-governance | Per repo or aggregate |
| **Checks** | Static analysis, linting, format, and policy checks | Prettier, Bandit, Semgrep, Base120 ref lint | Per repo or CI |
| **Audits** | Automated governance audits against HUMMBL criteria | Arbiter audit score 99.5/100 | Per repo |
| **Deployments** | Production environments running the artifact | hummbl.io served by Cloudflare Pages | Per service |

## What the audit score means

HUMMBL runs an automated governance audit on every open-source repository. The score is computed from a fixed rubric. It is not a subjective rating and it is not a certification.

| Dimension | Weight | What it checks |
| --- | --- | --- |
| Test coverage | High | Passing tests, assertion quality, edge cases |
| Stdlib-only constraint | High | No runtime third-party dependencies |
| Security scan | Medium | Bandit HIGH, Semgrep ERROR |
| Type annotations | Medium | Public functions typed |
| Conventional commits | Low | Commit format and PR history |
| Documentation | Low | README, docstrings, API reference |

The score is published as a proof artifact, not a marketing claim. It does not replace third-party certification, penetration testing, or customer due diligence.

## Public repo metrics vs. aggregate validation

Public repo metrics are the counts visible in each open-source GitHub repository. Aggregate validation includes the public tests plus the private internal founder/operator systems that test orchestration, delegation, governance buses, kill switches, circuit breakers, and receipts.

| Metric | Public repo | Aggregate |
| --- | --- | --- |
| hummbl-governance tests | 1,032 | 1,032 |
| hummbl-base120 tests | 148 | 148 |
| Internal operator tests | Not visible | Included |
| Total | Per-repo counts | 15,600+ |

When a public page or README cites a number, it should specify whether it is a public repo count or the aggregate. If it does not, it is a public repo count.

## What the public page does not claim

HUMMBL does not publish self-issued compliance grades, government approvals, or clinical validation. The public claims are limited to:

- Test counts from open-source repositories
- Framework coverage mappings
- Automated audit scores with the rubric described above
- Deployment status of public services

Any claim that implies legal certification, guaranteed truth, or external authority is not a HUMMBL public claim and should be treated as unsupported.

## How to verify

Every public repo score and test count can be checked independently:

- [hummbl-governance on GitHub](https://github.com/hummbl-dev/hummbl-governance)
- [hummbl-base120 on GitHub](https://github.com/hummbl-dev/base120)
- [Public namespace manifest](https://hummbl.io/manifest/hummbl-public-namespace.json)
- [Public boundary policy](https://hummbl.io/manifest/public-boundaries.json)
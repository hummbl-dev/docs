# HUMMBL Public Docs Claim Ledger

This file tracks public-facing claims in HUMMBL documentation. Every compliance, primitive-count, test-count, or capability claim must have an entry here before it appears in published docs.

## Claim policy

1. **Every quantitative claim must cite a source-of-record.** "34 governance primitives" must link to the current `hummbl-governance` inventory.
2. **Compliance-framework claims must distinguish coverage levels:**
   - `maps to` — the framework's controls have corresponding primitives (weakest)
   - `supports evidence for` — primitives produce artifacts usable in an assessment
   - `fully complies with` — the system meets all requirements of the framework (strongest; requires external audit)
   - `readiness assessment` — a self-assessment tool is available
3. **Count claims must be dated snapshots.** "34 governance primitives (as of 2026-07-11)" or link to a live source.
4. **Promotional shorthand must be marked.** If a docs simplification differs from the source-of-record, note it.
5. **Claim drift detection:** before default-branch deploy, CI should diff public claims against this ledger.

## Active claims

| Claim | Location | Source-of-record | Last verified | Confidence |
|---|---|---|---|---|
| 34 governance primitives across 10 categories | `introduction.mdx` | [hummbl-governance/CLAUDE.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CLAUDE.md) | 2026-07-11 | High — matches current source |
| Maps to NIST AI RMF | `introduction.mdx` | [hummbl-governance/docs/nist-rmf-mapping.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/docs/nist-rmf-mapping.md) | 2026-07-11 | High — mapping doc exists |
| Maps to ISO 42001 | `introduction.mdx` | [hummbl-governance/docs/iso27001-mapping.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/docs/iso27001-mapping.md) | 2026-07-11 | Medium — ISO 27001 mapping exists; 42001 crosswalk in progress |
| Maps to EU AI Act | `introduction.mdx` | [hummbl-governance/docs/coverage/](https://github.com/hummbl-dev/hummbl-governance/tree/main/docs/coverage) | 2026-07-11 | Medium — coverage docs exist |
| Maps to SOC 2 | `introduction.mdx` | [hummbl-governance/docs/soc2-mapping.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/docs/soc2-mapping.md) | 2026-07-11 | High — mapping doc exists |
| 120 Base120 reasoning models | `introduction.mdx` | [hummbl-agent/registry.json](https://github.com/hummbl-dev/hummbl-agent) | 2026-07-11 | High — registry validated in CI |
| Zero third-party runtime dependencies | `introduction.mdx` | [hummbl-governance/pyproject.toml](https://github.com/hummbl-dev/hummbl-governance/blob/main/pyproject.toml) | 2026-07-11 | High — enforced by dep-check |

## Retired/superseded claims

| Claim | Retired date | Reason |
|---|---|---|
| "seven governance primitives" | 2026-07-11 | Replaced with "34 governance primitives" — the seven shown are now framed as the most commonly composed user-facing subset |

## Review cadence

- Claims reviewed monthly or when source-of-record repos ship a major version.
- Compliance-framework claims reviewed before any public marketing, sales, or audit engagement.
- Count claims re-verified against source on every docs PR that touches them.

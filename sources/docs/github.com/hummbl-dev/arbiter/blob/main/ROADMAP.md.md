# Source: https://github.com/hummbl-dev/arbiter/blob/main/ROADMAP.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# ROADMAP.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/ROADMAP.md)

History

94 lines (69 loc) · 5.75 KB

## FilesExpand file tree

 main

/

# ROADMAP.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

94 lines (69 loc) · 5.75 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/ROADMAP.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Arbiter Roadmap

Deterministic, transparent, decomposable code quality scoring — expanding from Python-first to polyglot, from CLI to platform.

**Current state** (v0.3.0): 22 CLI subcommands, 6 analyzers, 273 tests, 8 PRs shipped, 6 OSS contributions tracked. Python-only scoring with noise filtering, fleet audit, HTML/PDF reports, weekly leaderboard automation, and a contribution tracker.

---

## Phase 1: Contribution Engine (Q2 2026)

_Turn Arbiter from a scorer into an OSS contribution machine._

| Feature | Description | Status |
| --- | --- | --- |
| `arbiter contribute` | One-command contribution pipeline: scan repo → find fixable findings → prepare branch → generate PR description → record in tracker | **Done** (#34) |
| `arbiter watch` | Monitor upstream PR status via GitHub API — auto-update contribution tracker when PRs merge/close | **Done** (#29) |
| `arbiter badge` | Generate SVG badge ("Arbiter Score: 96 A") for README.md — instant visibility for scored repos | **Done** (#32) |
| CI quality gate template | GitHub Action template: `arbiter diff --fail-under 80` as a PR check — the enterprise on-ramp | **Done** (#30) |
| `.arbiter.yml` config | Per-repo configuration: custom weights, excluded paths, rule overrides, noise threshold defaults | **Done** (#31) |
| Benchmark dataset | Curated 100-repo reference set with pinned scores — regression testing for Arbiter itself | **Done** (#33) |

## Phase 2: Polyglot Expansion (Q3 2026)

_Score any repo, not just Python._

| Feature | Description | Tool | Status |
| --- | --- | --- | --- |
| Shell analyzer | Parse shellcheck JSON output → findings | shellcheck | **Done** (#36) |
| JavaScript/TypeScript analyzer | Parse eslint JSON output → findings | eslint | **Done** (#40) |
| Go analyzer | Parse golangci-lint JSON output → findings | golangci-lint | **Done** (#40) |
| Rust analyzer | Parse clippy JSON output → findings | clippy | **Done** (#40) |
| Language detection | Auto-detect primary languages, select applicable analyzers, report coverage | stdlib | **Done** (#40) |
| Polyglot scoring weights | Adjust dimension weights per language (e.g., Rust security weight higher) | — | **Done** (#41) |

## Phase 3: Intelligence Layer (Q3-Q4 2026)

_Go from "what's wrong" to "what to do about it."_

| Feature | Description | Status |
| --- | --- | --- |
| `arbiter suggest` | AI-powered: rank findings by impact, suggest the 3 highest-ROI fixes | Planned |
| `arbiter explain` | Natural language explanation of a score: why it's C, what would make it B | Planned |
| Custom rule profiles | "Enterprise", "startup", "OSS maintainer" presets with different weights and thresholds | Planned |
| Historical scoring | Weekly snapshots → trend graphs. "Your code improved from C to B this quarter" | Planned |
| Team attribution | Who introduced which findings? Quality by contributor — agent leaderboard generalized to humans | Planned |
| Dependency scoring | Score a repo's dependencies: maintained? CVEs? license conflicts? Last release date? | Planned |

## Phase 4: Governance Integration (Q4 2026)

_Connect Arbiter to HUMMBL's governance stack._

| Feature | Description | Status |
| --- | --- | --- |
| Governance scoring dimension | Score repos on governance maturity: CONTRIBUTING.md, LICENSE, SECURITY.md, DCO, CoC | Planned |
| VERUM-aligned audit trail | Every score is an append-only signed record — provable governance for enterprise | Planned |
| Certified Adapter scoring | Score third-party adapters against HUMMBL certification criteria | Planned |
| Compliance report mapping | Map Arbiter findings to NIST CSF / ISO 27001 / SOC 2 controls | Planned |
| `arbiter certify` | Full certification workflow: score + governance + audit trail → certification decision | Planned |

## Phase 5: Platform (2027)

_Arbiter as a service._

| Feature | Description | Status |
| --- | --- | --- |
| Arbiter Cloud | Hosted scoring API — score any public repo via REST endpoint | Planned |
| GitHub App | Install on org → automatic PR quality checks on every push | Planned |
| Dashboard | Web UI showing fleet scores, trends, team leaderboard, contribution tracker | Planned |
| Webhook integration | Post score changes to Slack, Discord, email | Planned |
| Public leaderboard | hummbl.io/leaderboard — weekly ranking of top OSS repos by quality | Planned |
| PyPI package | `pip install arbiter-score` — the OSS distribution | Planned |

---

## Shipped (v0.1–v0.3)

| Version | Date | Features |
| --- | --- | --- |
| v0.1 | 2026-03 | Core scoring engine, ruff + bandit + radon analyzers, SQLite persistence, agent attribution |
| v0.2 | 2026-04 | Fleet audit, triage, auto-fix, HTML/PDF reports, improvement loop (gaps), artifact scorers |
| v0.3 | 2026-04-18 | `github-top`, `score-url`, `compare`, `leaderboard`, `contributions`, weekly Action, noise-threshold, CONTRIBUTING.md with DCO |
| v0.4 | 2026-04-18 | Phase 1 (badge, watch, config, CI gate, contribute, benchmark) + Phase 2 (shellcheck, eslint, golangci-lint, clippy, lang-detect, polyglot weights). 19 PRs, 427 tests, 6 languages. |

## Design Principles

1. **Deterministic** — same code always produces the same score. No LLM in the scoring path.
2. **Transparent** — every score decomposes into dimensions, every dimension into findings, every finding into a file:line.
3. **Stdlib-only core** — analyzers call external tools via subprocess, but Arbiter itself has zero runtime dependencies.
4. **Append-only tracking** — contribution ledger and gap tracker are JSONL, never mutated in place.
5. **Polyglot by design** — the `Analyzer` interface is language-agnostic. Adding a language = one new analyzer class.

---

_Powered by [HUMMBL](https://hummbl.io) — governed AI for enterprise._
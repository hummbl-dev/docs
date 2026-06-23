# Source: https://github.com/hummbl-dev/arbiter/releases

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

# Releases: hummbl-dev/arbiter

 

Releases · hummbl-dev/arbiter

## v0.7.0

14 Jun 21:07

![@hummbl-dev](https://avatars.githubusercontent.com/u/238336761?s=40&v=4) [hummbl-dev](https://github.com/hummbl-dev)

[v0.7.0](https://github.com/hummbl-dev/arbiter/tree/v0.7.0)

[`cdf2680`](https://github.com/hummbl-dev/arbiter/commit/cdf2680559f8d3a0eac616b502b379b85ca3b561)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page]().

## No results found

[View all tags](https://github.com/hummbl-dev/arbiter/tags)

[v0.7.0](https://github.com/hummbl-dev/arbiter/releases/tag/v0.7.0) [Latest](https://github.com/hummbl-dev/arbiter/releases/latest)

[Latest](https://github.com/hummbl-dev/arbiter/releases/latest)

## What's New

- Agent-aware code quality scoring for multi-agent codebases
- Tracks who wrote each line (human or AI)
- Per-commit agent attribution
- Agent leaderboard and quality trends
- Dashboard with per-agent timelines
- Core is stdlib Python (zero runtime dependencies)

## Installation

```shell
pip install arbiter
pip install "arbiter[analyzers]"  # + ruff, radon, vulture, bandit
```

## Documentation

See [README.md](https://github.com/hummbl-dev/arbiter/blob/main/README.md) for full documentation.

## License

Apache 2.0

Assets 2

Loading

### Uh oh!

There was an error while loading. [Please reload this page]().

 

All reactions

## v0.6.0 — Governance Integration

19 Apr 02:17

![@hummbl-dev](https://avatars.githubusercontent.com/u/238336761?s=40&v=4) [hummbl-dev](https://github.com/hummbl-dev)

[v0.6.0](https://github.com/hummbl-dev/arbiter/tree/v0.6.0)

[`e9f32c7`](https://github.com/hummbl-dev/arbiter/commit/e9f32c7e25dd23c15ef8bf771aab6fe9357007f9)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.

GPG key ID: B5690EEEBB952194

Verified

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page]().

## No results found

[View all tags](https://github.com/hummbl-dev/arbiter/tags)

[v0.6.0 — Governance Integration](https://github.com/hummbl-dev/arbiter/releases/tag/v0.6.0)

## Phase 4: Governance Integration (5/5)

- `arbiter governance` — repo maturity scoring: LICENSE, CONTRIBUTING, SECURITY, CoC, CI ([#52](https://github.com/hummbl-dev/arbiter/pull/52))
- `arbiter audit-trail` — VERUM-aligned append-only hash-chained score records ([#53](https://github.com/hummbl-dev/arbiter/pull/53))
- `arbiter compliance` — map findings to NIST CSF 2.0 + ISO 27001:2022 ([#54](https://github.com/hummbl-dev/arbiter/pull/54))
- `arbiter certify` — full certification: CERTIFIED / PROVISIONAL / FAILED ([#55](https://github.com/hummbl-dev/arbiter/pull/55))

## Arbiter certifies itself

```
Certification: CERTIFIED
  Code Quality:  96.1 / 100
  Governance:    70.0 / 100
  Dependencies: 100.0 / 100
  Overall:       89.0 / 100
```

## Stats

- **38+** CLI subcommands
- **600+** tests
- **33** PRs merged in one session
- **Phases 1-4 complete** — only Phase 5 (Platform) remains

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Assets 2

Loading

### Uh oh!

There was an error while loading. [Please reload this page]().

 

All reactions

## v0.5.0 — Intelligence Layer

19 Apr 02:01

![@hummbl-dev](https://avatars.githubusercontent.com/u/238336761?s=40&v=4) [hummbl-dev](https://github.com/hummbl-dev)

[v0.5.0](https://github.com/hummbl-dev/arbiter/tree/v0.5.0)

[`150ccd8`](https://github.com/hummbl-dev/arbiter/commit/150ccd8446402ec863f85c222c63d1280e0843c8)

This commit was created on GitHub.com and signed with GitHub’s **verified signature**.

GPG key ID: B5690EEEBB952194

Verified

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits).

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page]().

## No results found

[View all tags](https://github.com/hummbl-dev/arbiter/tags)

[v0.5.0 — Intelligence Layer](https://github.com/hummbl-dev/arbiter/releases/tag/v0.5.0)

## Phase 3: Intelligence Layer (6/6)

- `arbiter suggest` — rank findings by impact, recommend highest-ROI fixes ([#48](https://github.com/hummbl-dev/arbiter/pull/48))
- `arbiter explain` — natural language score explanation ([#49](https://github.com/hummbl-dev/arbiter/pull/49))
- `arbiter profiles` — enterprise/startup/oss/strict presets ([#47](https://github.com/hummbl-dev/arbiter/pull/47))
- `arbiter history` — score tracking over time with deltas ([#46](https://github.com/hummbl-dev/arbiter/pull/46))
- `arbiter team` — quality metrics by contributor ([#51](https://github.com/hummbl-dev/arbiter/pull/51))
- `arbiter deps` — Python dependency scoring ([#50](https://github.com/hummbl-dev/arbiter/pull/50))

## Also in this release

- Preflight v2: try-import, notebook, comment-reexport checks — 100% false positive coverage ([#44](https://github.com/hummbl-dev/arbiter/pull/44))
- Contribute v2: duplicate PR check + temp dir cleanup ([#45](https://github.com/hummbl-dev/arbiter/pull/45))
- Learnings tracker: false positive and rejection ledger ([#43](https://github.com/hummbl-dev/arbiter/pull/43))

## Stats

- **35+** CLI subcommands
- **500+** tests
- **10** analyzers across **6** languages
- **29** PRs merged in one session
- **8** OSS contributions to top repos
- **Phases 1-3 complete**

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Assets 2

Loading

### Uh oh!

There was an error while loading. [Please reload this page]().

 

All reactions

## v0.4.0 — Polyglot Contribution Engine

18 Apr 18:27

![@hummbl-dev](https://avatars.githubusercontent.com/u/238336761?s=40&v=4) [hummbl-dev](https://github.com/hummbl-dev)

[v0.4.0](https://github.com/hummbl-dev/arbiter/tree/v0.4.0)

[`28e7b57`](https://github.com/hummbl-dev/arbiter/commit/28e7b57efd9260e35d1ba9bd6c4fbefd23e8f8ed)

Compare

# Choose a tag to compare

## Sorry, something went wrong.

Filter

Loading 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading. [Please reload this page]().

## No results found

[View all tags](https://github.com/hummbl-dev/arbiter/tags)

[v0.4.0 — Polyglot Contribution Engine](https://github.com/hummbl-dev/arbiter/releases/tag/v0.4.0)

## What's New

### Phase 1: Contribution Engine

- `arbiter contribute` — automated scan → fix → prepare pipeline ([#34](https://github.com/hummbl-dev/arbiter/pull/34))
- `arbiter watch` — GitHub API PR status tracking ([#29](https://github.com/hummbl-dev/arbiter/pull/29))
- `arbiter badge` — SVG score badges for README.md ([#32](https://github.com/hummbl-dev/arbiter/pull/32))
- `.arbiter.yml` / `.arbiter.json` — per-repo configuration ([#31](https://github.com/hummbl-dev/arbiter/pull/31))
- CI quality gate — reusable GitHub Action workflow ([#30](https://github.com/hummbl-dev/arbiter/pull/30))
- Benchmark dataset — 13 reference repos with score ranges ([#33](https://github.com/hummbl-dev/arbiter/pull/33))

### Phase 2: Polyglot Expansion

- Shell analyzer via shellcheck ([#36](https://github.com/hummbl-dev/arbiter/pull/36))
- JavaScript/TypeScript analyzer via ESLint ([#40](https://github.com/hummbl-dev/arbiter/pull/40))
- Go analyzer via golangci-lint ([#40](https://github.com/hummbl-dev/arbiter/pull/40))
- Rust analyzer via cargo clippy ([#40](https://github.com/hummbl-dev/arbiter/pull/40))
- Language detection for 25+ languages ([#40](https://github.com/hummbl-dev/arbiter/pull/40))
- Per-language scoring weight profiles ([#41](https://github.com/hummbl-dev/arbiter/pull/41))

### Also in this release

- `arbiter github-top` — score popular GitHub repos by stars ([#20](https://github.com/hummbl-dev/arbiter/pull/20))
- `arbiter score-url` — score any repo by GitHub URL ([#21](https://github.com/hummbl-dev/arbiter/pull/21))
- `arbiter compare` — side-by-side repo comparison ([#25](https://github.com/hummbl-dev/arbiter/pull/25))
- `arbiter leaderboard` — markdown quality index ([#22](https://github.com/hummbl-dev/arbiter/pull/22))
- `--noise-threshold` — per-rule finding cap ([#23](https://github.com/hummbl-dev/arbiter/pull/23))
- Weekly leaderboard GitHub Action ([#24](https://github.com/hummbl-dev/arbiter/pull/24))
- CONTRIBUTING.md with DCO requirement ([#26](https://github.com/hummbl-dev/arbiter/pull/26))
- Contribution tracker with JSONL ledger ([#27](https://github.com/hummbl-dev/arbiter/pull/27))
- Product roadmap through 2027 ([#28](https://github.com/hummbl-dev/arbiter/pull/28))

### Stats

- **28** CLI subcommands
- **10** analyzers across **6** languages
- **427** tests
- **19** PRs merged in one session
- **6** OSS contributions submitted to top repos

---

_Powered by [HUMMBL](https://hummbl.io) — governed AI for enterprise._

Assets 2

Loading

### Uh oh!

There was an error while loading. [Please reload this page]().

 

All reactions
# Source: https://github.com/hummbl-dev/arbiter/blob/main/CHANGELOG.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# CHANGELOG.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/CHANGELOG.md)

History

81 lines (66 loc) · 3.25 KB

 main

/

# CHANGELOG.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

81 lines (66 loc) · 3.25 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/CHANGELOG.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## \[Unreleased\]

### Added

- (placeholder for upcoming changes)

## \[v0.7.0\] - 2026-06-14

### Added

- Agent-aware code quality scoring for multi-agent codebases
- Tracks who wrote each line (human or AI)
- Per-commit agent attribution
- Agent leaderboard and quality trends
- Dashboard with per-agent timelines
- Core is stdlib Python (zero runtime dependencies)

## \[v0.6.0\] - 2026-04-19

### Added

- `arbiter governance` — repo maturity scoring: LICENSE, CONTRIBUTING, SECURITY, CoC, CI (#52)
- `arbiter audit-trail` — VERUM-aligned append-only hash-chained score records (#53)
- `arbiter compliance` — map findings to NIST CSF 2.0 + ISO 27001:2022 (#54)
- `arbiter certify` — full certification: CERTIFIED / PROVISIONAL / FAILED (#55)

### Notes

- Arbiter certifies itself: Certification CERTIFIED (Overall 89.0 / 100)
- 38+ CLI subcommands, 600+ tests, 33 PRs merged in one session
- Phases 1-4 complete — only Phase 5 (Platform) remains

## \[v0.5.0\] - 2026-04-19

### Added

- `arbiter suggest` — rank findings by impact, recommend highest-ROI fixes (#48)
- `arbiter explain` — natural language score explanation (#49)
- `arbiter profiles` — enterprise/startup/oss/strict presets (#47)
- `arbiter history` — score tracking over time with deltas (#46)
- `arbiter team` — quality metrics by contributor (#51)
- `arbiter deps` — Python dependency scoring (#50)
- Preflight v2: try-import, notebook, comment-reexport checks — 100% false positive coverage (#44)
- Contribute v2: duplicate PR check + temp dir cleanup (#45)
- Learnings tracker: false positive and rejection ledger (#43)

### Notes

- 35+ CLI subcommands, 500+ tests, 10 analyzers across 6 languages
- 29 PRs merged in one session, 8 OSS contributions to top repos
- Phases 1-3 complete

## \[v0.4.0\] - 2026-04-18

### Added

- `arbiter contribute` — automated scan → fix → prepare pipeline (#34)
- `arbiter watch` — GitHub API PR status tracking (#29)
- `arbiter badge` — SVG score badges for README.md (#32)
- `.arbiter.yml` / `.arbiter.json` — per-repo configuration (#31)
- CI quality gate — reusable GitHub Action workflow (#30)
- Benchmark dataset — 13 reference repos with score ranges (#33)
- Shell analyzer via shellcheck (#36)
- JavaScript/TypeScript analyzer via ESLint (#40)
- Go analyzer via golangci-lint (#40)
- Rust analyzer via cargo clippy (#40)
- Language detection for 25+ languages (#40)
- Per-language scoring weight profiles (#41)
- `arbiter github-top` — score popular GitHub repos by stars (#20)
- `arbiter score-url` — score any repo by GitHub URL (#21)
- `arbiter compare` — side-by-side repo comparison (#25)
- `arbiter leaderboard` — markdown quality index (#22)
- `--noise-threshold` — per-rule finding cap (#23)
- Weekly leaderboard GitHub Action (#24)
- CONTRIBUTING.md with DCO requirement (#26)
- Contribution tracker with JSONL ledger (#27)
- Product roadmap through 2027 (#28)

### Notes

- 28 CLI subcommands, 10 analyzers across 6 languages, 427 tests
- 19 PRs merged in one session, 6 OSS contributions submitted to top repos
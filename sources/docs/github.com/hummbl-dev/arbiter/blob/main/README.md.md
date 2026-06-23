# Source: https://github.com/hummbl-dev/arbiter/blob/main/README.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# README.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/README.md)

History

168 lines (122 loc) · 6.45 KB

 main

/

# README.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

168 lines (122 loc) · 6.45 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/README.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Arbiter

[![CI](https://github.com/hummbl-dev/arbiter/actions/workflows/ci.yml/badge.svg)](https://github.com/hummbl-dev/arbiter/actions/workflows/ci.yml) [![PyPI](https://camo.githubusercontent.com/7d06c0550230ae55966c32c569ae9aff8c69ba289053e22550e3f07ebb199017/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f617262697465722d73636f7265)](https://pypi.org/project/arbiter-score/) [![Python 3.11+](https://camo.githubusercontent.com/96abf9b704f80578ea56dd10cab0d911c56d46dbec347f431ece9cf60ac175ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31312532422d626c7565)](https://www.python.org/downloads/) [![License](https://camo.githubusercontent.com/39a434c39c97856247fc55ebc90e8cc1cb9871558a37bf1bf83cbaca3be89d69/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d417061636865253230322e302d626c7565)](https://github.com/hummbl-dev/arbiter/blob/main/LICENSE) [![Dependencies](https://camo.githubusercontent.com/0959b932631a36b4e8a25379fa5d17905cd053643464bc3fabcea8e058c35005/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f72655f646570732d7374646c69625f6f6e6c792d627269676874677265656e)](https://github.com/hummbl-dev/arbiter/blob/main) [![Last commit](https://camo.githubusercontent.com/d60e535bc56d6cdb3a120a467372ae61cff12e9f701be611691e5ff0bb6066dc/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f68756d6d626c2d6465762f617262697465722f6d61696e)](https://github.com/hummbl-dev/arbiter/commits/main) [![Arbiter Score](https://camo.githubusercontent.com/153e8edc41a2ae8067f018713da01879254c2d16c65bf8ad8907b04f8243f7a0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f417262697465722d39362e36253230412d627269676874677265656e)](https://github.com/hummbl-dev/arbiter) [![Complexity](https://camo.githubusercontent.com/fd52052c9e4e261aa696b008643f81148d4731851b55252e3bd88a91b10b76d2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6d706c65786974792d39312e31253230412d627269676874677265656e)](https://github.com/hummbl-dev/arbiter)

**Agent-aware code quality scoring for multi-agent codebases.**

In 2026, code is written by fleets of AI agents. Arbiter knows _who_ wrote each line -- human or AI -- and scores quality accordingly.

Learn more at [hummbl.io](https://hummbl.io).

Repository health, validation, and stewardship expectations are tracked in [docs/REPO\_HEALTH.md](https://github.com/hummbl-dev/arbiter/blob/main/docs/REPO_HEALTH.md).

## Quick Start -- 5 Minutes

```shell
pip install "arbiter-score[analyzers]"
arbiter score .
```

**Example output:**

```
Arbiter Scorecard: my-repo (main)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall:  87.3  →  Grade: B

By Analyzer:
  Lint       91.2  (ruff — 3 style issues)
  Security   95.0  (bandit — clean)
  Complexity 78.5  (radon — 2 functions > complexity 10)
  Dead Code  92.0  (vulture — 1 unused import)

By Agent (last 30 days):
  claude-code   89.1  (42 commits, 1,240 LOC)
  codex         85.3  (18 commits, 890 LOC)
  human         92.7  (5 commits, 120 LOC)

Top Issues:
  • src/api/routes.py:47  complexity C (15)  — agent: codex
  • src/utils.py:12       unused import os   — agent: claude-code
  • src/models.py:89      line too long      — agent: codex

Run `arbiter serve` to view the full dashboard.
```

## Install

The Python distribution is `arbiter-score`; the installed CLI command is `arbiter`. Do not install the separate PyPI project named `arbiter` for this tool.

```shell
pip install arbiter-score                  # core (stdlib only)
pip install "arbiter-score[analyzers]"     # + ruff, radon, vulture, bandit

# Or from source
git clone https://github.com/hummbl-dev/arbiter.git && cd arbiter
pip install -e ".[analyzers]"
```

## Usage

```shell
# Quick score -- no persistence, instant feedback
arbiter score /path/to/repo

# Full analysis with per-commit agent attribution
arbiter analyze /path/to/repo

# Agent leaderboard -- who writes the best code?
arbiter agents

# Start the dashboard (single HTML file, no build step)
arbiter serve --port 8080
```

## What It Scores

Arbiter wraps tools you already trust and combines them into a deterministic composite score:

| Analyzer | Tool | Weight | What It Finds |
| --- | --- | --- | --- |
| Lint | ruff | 35% | Style violations, import errors, bugbear patterns |
| Security | bandit | 30% | Hardcoded secrets, shell injection, dangerous patterns |
| Complexity | radon | 35% | Cyclomatic complexity (grade A-F per function) |
| Dead Code | vulture | penalty | Unused functions, imports, variables |
| Duplication | AST hash | penalty | Near-duplicate function bodies |
| Semgrep | semgrep | opt-in | Custom rule enforcement (enable via config) |

**Scoring:** `100 - (penalty / LOC) * normalization`. Grades: A (90+) | B (80+) | C (70+) | D (60+) | F (<60).

## What Makes Arbiter Different

| Feature | Traditional Tools | Arbiter |
| --- | --- | --- |
| Agent attribution | None | First-class: tracks Claude, Codex, Gemini, Copilot, humans |
| Per-commit scoring | Repo-wide only | Scores each commit's changed files individually |
| Diff analysis | N/A | Score only what changed in a PR/branch |
| Agent-specific gates | N/A | Different quality thresholds per agent trust tier |
| Dashboard | SaaS login | Single HTML file with per-agent timelines and fleet view |
| Dependencies | Heavy | Analysis tools only; core is stdlib Python |

## CLI Reference

```shell
arbiter analyze <repo>                     # Full analysis + per-commit scoring + persist
arbiter score <repo> [--json] [--exclude]  # Quick score (no persist)
arbiter diff <repo> [--base main] [--json] # Score changed files vs base branch
arbiter agents                             # Agent leaderboard
arbiter trend [--days 30]                  # Quality trend
arbiter worst [--limit 20]                 # Worst files
arbiter commits [--agent claude]           # Recent commits with scores
arbiter audit-fleet <directory>            # Audit all repos in a directory
arbiter triage                             # Auto-classify repos: green/yellow/red/archive
arbiter fix <repo> [--dry-run]             # Auto-fix ruff findings + before/after score
arbiter serve [--port 8080]                # API + dashboard
```

## Tests

```shell
pip install ".[test]"
PYTHONPATH=src python -m pytest tests/ -v
```

## Quality Gate

Arbiter grades itself on every push and PR. The CI runs `arbiter score .` and fails if the score drops below **90 (A grade)**.

```shell
# Run the same check locally
arbiter score . --fail-under 90

# Score only your changed files against main
arbiter diff . --base main --fail-under 80
```

## Requirements

- Python 3.11+
- git (for historian)
- Optional: ruff, radon, vulture, bandit (install via `[analyzers]` extra)

## HUMMBL Ecosystem

Part of the [HUMMBL](https://github.com/hummbl-dev) cognitive AI architecture:

- [hummbl-governance](https://github.com/hummbl-dev/hummbl-governance) -- Governance primitives that Arbiter scores against
- [base120](https://github.com/hummbl-dev/base120) -- 120 mental models for structured reasoning
- [hummbl-agent](https://github.com/hummbl-dev/hummbl-agent) -- Governed control plane for AI agent systems
- [hummbl-bibliography](https://github.com/hummbl-dev/hummbl-bibliography) -- Bibliography for the HUMMBL cognitive framework
- [mcp-server](https://github.com/hummbl-dev/mcp-server) -- MCP server for AI agent integration

Learn more at [hummbl.io](https://hummbl.io).

## License

Apache 2.0 -- see [LICENSE](https://github.com/hummbl-dev/arbiter/blob/main/LICENSE).

---

Built by [HUMMBL LLC](https://hummbl.io) from production experience coordinating Claude, Codex, Gemini, and human engineers on a 14,000+ test codebase.
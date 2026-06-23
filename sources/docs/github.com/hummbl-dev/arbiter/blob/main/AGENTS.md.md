# Source: https://github.com/hummbl-dev/arbiter/blob/main/AGENTS.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# AGENTS.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/AGENTS.md)

History

42 lines (28 loc) · 1.63 KB

 main

/

# AGENTS.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

42 lines (28 loc) · 1.63 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/AGENTS.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# AGENTS.md — arbiter

## Project

**arbiter** — Agent-aware code quality scoring for multi-agent codebases. Knows who wrote each line (human or AI) and scores quality accordingly. PyPI-published as `arbiter-score` (CLI command `arbiter`), Python 3.11+, stdlib-only core with optional analyzer extras.

## Scope

- In scope: Code quality scoring (cyclomatic complexity, dependency analysis, test coverage, governance compliance), per-commit agent attribution, agent leaderboards, single-file HTML dashboard, grades repos A through F with evidence-backed findings
- Out of scope: Consumer app features, bus protocol changes, agent orchestration logic

## Setup

```shell
git clone https://github.com/hummbl-dev/arbiter.git && cd arbiter
pip install -e ".[analyzers]"   # core + ruff, radon, vulture, bandit
# core only (stdlib): pip install -e .
```

The Python distribution is `arbiter-score`; the installed CLI command is `arbiter`. Do not install the separate PyPI project named `arbiter` for this tool.

## Testing

```shell
python -m pytest tests/ -v
```

Test extras: `pytest>=9.0.3`. Test paths configured to `tests/`.

## Conventions

- Python 3.11+ required (supports 3.11–3.14)
- Core is stdlib-only; analyzers (ruff, radon, vulture, bandit) are optional `[analyzers]` extras
- Source layout: `src/` package
- Pre-commit config present (`.pre-commit-config.yaml`)
- Commit format: Conventional Commits
- Branch naming: `type/agent/short-desc`
- Apache 2.0 license

## CI

GitHub Actions workflows: `ci.yml` (lint + test), `arbiter-quality-gate.yml` (self-scoring gate), `publish.yml` (PyPI release), `weekly-leaderboard.yml` (agent leaderboard refresh).
# Source: https://github.com/hummbl-dev/arbiter/blob/main/docs/REPO_HEALTH.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# REPO\_HEALTH.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/docs/REPO_HEALTH.md)

History

89 lines (65 loc) · 4.29 KB

 main

/

# REPO\_HEALTH.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

89 lines (65 loc) · 4.29 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/docs/REPO_HEALTH.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Repository Health Contract

## Identity

- **Repository**: `hummbl-dev/arbiter`
- **Canonical URL**: `https://github.com/hummbl-dev/arbiter`
- **Package distribution**: `arbiter-score`
- **CLI**: `arbiter`
- **Owner**: HUMMBL Team
- **Stewardship scope**: Deterministic, agent-aware code quality scoring, PR diff scoring, contribution tracking, analyzer integration, leaderboard reporting, and governance quality gates.

## Lifecycle

- **Status**: Active public repository and PyPI-oriented package.
- **Default branch**: `main`.
- **Current package version**: `0.6.0`.
- **Release posture**: Core scoring logic, analyzer integrations, CLI surfaces, CI templates, and governance-reporting features may continue through reviewed pull requests.
- **Archive trigger**: Archive only if the Arbiter scoring package and reusable quality-gate workflow are superseded by another declared canonical source of truth.

## Source Of Truth

- `pyproject.toml` defines package metadata, optional analyzer dependencies, test dependencies, and the `arbiter` CLI entry point.
- `src/arbiter/` contains the importable package and CLI implementation.
- `tests/` contains the validation suite for scoring, analyzers, CI templates, governance quality, reports, API behavior, and contribution tracking.
- `.github/workflows/ci.yml` is the primary PR and push validation workflow.
- `.github/workflows/arbiter-quality-gate.yml` is the reusable workflow contract for downstream quality gates.
- `docs/CERTIFICATION_REPORT.md`, `docs/PLATFORM_DESIGN.md`, and related docs describe certification and platform behavior.
- `README.md` is the public overview and should stay aligned with package metadata, install commands, analyzer extras, and CLI behavior.

## Required Local Validation

Before merging non-trivial code changes:

```shell
python -m pip install -e ".[test]"
PYTHONPATH=src python -m pytest tests/ -v --ignore=tests/test_api.py
PYTHONPATH=src python -m pytest tests/test_api.py -v
```

Analyzer and quality-gate changes should also run:

```shell
python -m pip install -e ".[analyzers]"
arbiter score . --fail-under 90
arbiter diff . --base main --fail-under 70
```

Documentation-only changes should at minimum pass:

```shell
git diff --check
```

## CI Expectations

Expected GitHub Actions coverage:

- `.github/workflows/ci.yml` runs the test suite on Python 3.11 and 3.12.
- `.github/workflows/ci.yml` runs `tests/test_api.py` separately after the main test pass.
- `.github/workflows/ci.yml` runs a self-grade gate with `arbiter score . --fail-under 90`.
- `.github/workflows/ci.yml` runs PR diff scoring with `arbiter diff . --base origin/main --fail-under 70`.
- `.github/workflows/publish.yml` builds and verifies the package before PyPI publish.
- `.github/workflows/arbiter-quality-gate.yml` provides the reusable downstream diff-score gate.
- `.github/workflows/weekly-leaderboard.yml` runs scheduled leaderboard generation.

## Branch Protection Expectation

`main` should require pull request review and the hosted CI checks that protect tests, API behavior, self-grade threshold, and PR diff-score threshold.

Branch protection is tracked centrally in `hummbl-dev/hummbl-dev#18`; do not overclaim required checks until that audit is updated.

## Operational Notes

- The core package should remain usable without analyzer extras; analyzer-specific integrations belong behind optional extras.
- Public install instructions must match `pyproject.toml` package metadata and published distribution names.
- `arbiter-score` is the intended public distribution name; `arbiter` is only the installed CLI entry point for this repository and should not be documented as the PyPI package.
- Self-grade and reusable quality-gate thresholds are product contracts, not decorative metrics.
- Changes to scoring formulas, analyzer weights, noise thresholds, or agent attribution should include before/after evidence.
- Generated scoring artifacts such as local JSONL audit files should not be treated as source-of-truth documentation unless explicitly committed by design.

## Fleet Scan Classification

Future fleet scans can classify this repository as:

- **Lifecycle**: active public package
- **Visibility**: public
- **Primary function**: deterministic code quality and governance scoring
- **Validation entrypoint**: `pytest` plus Arbiter self-grade
- **Primary metadata owner**: HUMMBL Team
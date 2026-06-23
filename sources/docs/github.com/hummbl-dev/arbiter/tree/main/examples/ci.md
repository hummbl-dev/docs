# Source: https://github.com/hummbl-dev/arbiter/tree/main/examples/ci

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# ci

/

Copy path

## Directory actions

## More options

More options

## Directory actions

## More options

More options

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/examples/ci)

History

 main

/

# ci

/

Copy path

Top

## Folders and files

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

### parent directory

[..](https://github.com/hummbl-dev/arbiter/tree/main/examples) |
| 

[README.md](https://github.com/hummbl-dev/arbiter/blob/main/examples/ci/README.md 'README.md')

 | 

[README.md](https://github.com/hummbl-dev/arbiter/blob/main/examples/ci/README.md 'README.md')

 | 

 | 

 |
| 

[quality-gate.yml](https://github.com/hummbl-dev/arbiter/blob/main/examples/ci/quality-gate.yml 'quality-gate.yml')

 | 

[quality-gate.yml](https://github.com/hummbl-dev/arbiter/blob/main/examples/ci/quality-gate.yml 'quality-gate.yml')

 | 

 | 

 |
| 

View all files

 |

## [README.md](https://github.com/#readme)

Outline

# Arbiter CI Quality Gate

Use Arbiter as an automated PR quality gate in GitHub Actions.

## Quick Start

### Option A: Reusable Workflow (recommended)

Create `.github/workflows/quality-gate.yml` in your repo:

```yaml
name: Code Quality
on: [pull_request]
jobs:
  quality:
    uses: hummbl-dev/arbiter/.github/workflows/arbiter-quality-gate.yml@main
    with:
      fail-under: 70
      noise-threshold: 50
```

This gives you:

- Diff scoring against the base branch
- PR comment with score, grade, and findings count
- Job summary in the Actions UI
- Configurable pass/fail threshold

### Option B: Inline Steps

Copy `quality-gate.yml` from this directory into `.github/workflows/` and customize directly. This is useful when you need to add extra steps or modify the scoring logic.

## Inputs (Reusable Workflow)

| Input | Type | Default | Description |
| --- | --- | --- | --- |
| `fail-under` | number | 70 | Minimum diff score to pass (0-100) |
| `noise-threshold` | number | 50 | Suppress findings below this confidence |
| `python-version` | string | 3.12 | Python version for the runner |
| `arbiter-version` | string | (latest) | Pin a specific Arbiter version |

## How It Works

1. Checks out the repo with full history (`fetch-depth: 0`)
2. Installs Arbiter with analyzer dependencies (ruff, radon, vulture, bandit)
3. Runs `arbiter diff` against the PR's base branch
4. Posts a score summary as a PR comment (updates on re-push)
5. Fails the check if the score is below `fail-under`

## Requirements

- The repo must be checked out with `fetch-depth: 0` so Arbiter can diff against the base branch.
- For the reusable workflow, the calling workflow must grant `pull-requests: write` permission for PR comments.

## Tuning Thresholds

- **fail-under: 70** is a good starting point for most projects.
- **fail-under: 90** for strict quality gates on production repos.
- **noise-threshold: 50** suppresses low-confidence findings. Lower it to see more warnings.

## Local Testing

Run the same check locally before pushing:

```shell
pip install "arbiter-score[analyzers]"
arbiter diff . --base origin/main --fail-under 70 --noise-threshold 50
```
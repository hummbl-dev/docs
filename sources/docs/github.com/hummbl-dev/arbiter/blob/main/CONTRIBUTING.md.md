# Source: https://github.com/hummbl-dev/arbiter/blob/main/CONTRIBUTING.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# CONTRIBUTING.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/CONTRIBUTING.md)

History

56 lines (38 loc) · 1.92 KB

## FilesExpand file tree

 main

/

# CONTRIBUTING.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

56 lines (38 loc) · 1.92 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/CONTRIBUTING.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Contributing to Arbiter

Thanks for your interest in contributing! Here's how to get started.

## Setup

```shell
git clone https://github.com/hummbl-dev/arbiter.git
cd arbiter
python -m venv .venv && source .venv/bin/activate
pip install -e ".[test]"
PYTHONPATH=src python -m pytest tests/ -v
```

**Or with [uv](https://docs.astral.sh/uv/)** (10-100x faster):

```shell
git clone https://github.com/hummbl-dev/arbiter.git
cd arbiter
uv pip install -e ".[test]"
PYTHONPATH=src python -m pytest tests/ -v
```

## Pull Requests

- Branch from `main`
- Keep PRs focused — one fix or feature per PR
- All tests must pass before merge
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages

## Developer Certificate of Origin (DCO)

All contributions require a `Signed-off-by` line in each commit message, certifying that you have the right to submit the work under this project's license.

```
feat: add new analyzer for shellcheck

Signed-off-by: Your Name <your.email@example.com>
```

Add it automatically with `git commit -s`.

By signing off, you agree to the [Developer Certificate of Origin](https://developercertificate.org/):

> I certify that (a) this contribution was created in whole or in part by me and I have the right to submit it under the open source license indicated in the file; or (b) it is based upon previous work that, to the best of my knowledge, is covered under an appropriate open source license and I have the right under that license to submit that work with modifications; or (c) it was provided to me by someone who certified (a) or (b) and I have not modified it.

## Reporting Issues

Open an issue on GitHub. Include steps to reproduce, expected vs actual behavior, and your Python version.

## Code Style

- Python 3.11+
- Lint with [ruff](https://docs.astral.sh/ruff/)
- No third-party runtime dependencies in `src/arbiter/` (stdlib only)
- Test dependencies (pytest, etc.) go in `[test]` extras
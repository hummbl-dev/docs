# Source: https://github.com/hummbl-dev/evidence-gate/blob/main/AGENTS.md

This repository was archived by the owner on Jun 22, 2026. It is now read-only.

[hummbl-dev](https://github.com/hummbl-dev) / **[evidence-gate](https://github.com/hummbl-dev/evidence-gate)** Public archive

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fevidence-gate) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fevidence-gate)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fevidence-gate)
 

 

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

[History](https://github.com/hummbl-dev/evidence-gate/commits/main/AGENTS.md)

History

46 lines (31 loc) · 2.3 KB

 main

/

# AGENTS.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

46 lines (31 loc) · 2.3 KB

[Raw](https://github.com/hummbl-dev/evidence-gate/raw/refs/heads/main/AGENTS.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# AGENTS.md — evidence-gate

## Project

**evidence-gate** — Pre-publish source-verification rule library for HUMMBL governance content. Stdlib-only TOML rules + fixture harness consumed by `hummbl-production/scripts/case_study_verify.py`. Python 3.11+ (uses `tomllib`), zero third-party runtime dependencies.

## Scope

- In scope: 8 ER-NNN TOML rules (`rules/`), surface registry (`_surfaces.toml`), context-tag families (`_families.toml`), stdlib fixture harness (`scripts/run_rule_fixtures.py`), v0.3 schema documentation, append-only review-learning corpus (`contribution_learnings.jsonl`)
- Out of scope: Consumer-side claim finding (lives in `hummbl-production`), publishing readiness judgments (human/agent review), broad content review

## Setup

```shell
git clone https://github.com/hummbl-dev/evidence-gate.git && cd evidence-gate
# No install needed — stdlib only, run scripts directly
```

## Testing

```shell
# Run fixtures locally (32 fixtures across 8 rules)
python scripts/run_rule_fixtures.py

# With explicit loader path (for hummbl-production consumer)
python scripts/run_rule_fixtures.py --rule-loader-path ../hummbl-production

# CI mode (skip missing private loader)
python scripts/run_rule_fixtures.py --skip-missing-loader
```

Full fixture execution depends on the private `hummbl-production/scripts/rule_loader.py` contract. Set `HUMMBL_PRODUCTION_ROOT` or pass `--rule-loader-path`.

## Conventions

- Python 3.11+ required (uses `tomllib`)
- Zero third-party runtime dependencies — no PyYAML; loader is `tomllib`, harness is stdlib `re` + `subprocess` + `pathlib`
- Each rule TOML declares: `[pattern]`, `[severity]` (default/promote\_when/demote\_when), `[canonical_sources]` policy, `[[exceptions]]`, embedded `[[fixtures.positive]]` / `[[fixtures.negative]]`
- Fail-closed contract: rules load + validate but don't yet drive findings (v1 hardcoded patterns still active in consumer)
- Commit format: Conventional Commits
- Branch naming: `type/agent/short-desc`
- Apache 2.0 license

## CI

GitHub Actions (`.github/workflows/`) + Gitea mirror (`.gitea/workflows/`). CI compiles `run_rule_fixtures.py` and parses rule TOML on supported Python versions when rule, script, schema-doc, or workflow files change. Uses `--skip-missing-loader` so public syntax checks run without access to the private loader repository.
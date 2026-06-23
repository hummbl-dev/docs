# Source: https://github.com/hummbl-dev/hummbl-governance

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-governance](https://github.com/hummbl-dev/hummbl-governance)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-governance) You must be signed in to change notification settings
- [Fork 1](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-governance)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-governance)
 

 

 main

[**1** Branch](https://github.com/hummbl-dev/hummbl-governance/branches) [**8** Tags](https://github.com/hummbl-dev/hummbl-governance/tags)

Go to file

Code

Open more actions menu

## Folders and files

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

## Latest commit

![hummbl-dev](https://avatars.githubusercontent.com/u/238336761?v=4&size=40)![devin-ai-integration[bot]](https://avatars.githubusercontent.com/in/811515?v=4&size=40)

[hummbl-dev](https://github.com/hummbl-dev/hummbl-governance/commits?author=hummbl-dev)

and

[devin-ai-integration\[bot\]](https://github.com/hummbl-dev/hummbl-governance/commits?author=devin-ai-integration%5Bbot%5D)

[feat(governance): canonize fleet inventory + init standard v0.1 (](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b) [#85](https://github.com/hummbl-dev/hummbl-governance/pull/85) [)](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b)

Open commit detailspending

Jun 22, 2026

[70fa081](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b) · Jun 22, 2026

## History

[182 Commits](https://github.com/hummbl-dev/hummbl-governance/commits/main/)

Open commit details

182 Commits

 |
| 

[.gitea/workflows](https://github.com/hummbl-dev/hummbl-governance/tree/main/.gitea/workflows 'This path skips through empty directories')

 | 

[.gitea/workflows](https://github.com/hummbl-dev/hummbl-governance/tree/main/.gitea/workflows 'This path skips through empty directories')

 | 

[fix(ci): pin Arbiter governance audit dependency version (](https://github.com/hummbl-dev/hummbl-governance/commit/cd87baaff389f2dd019c4aa6abbcc70646c71351 'fix(ci): pin Arbiter governance audit dependency version (#68)

Fixes #66

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#68](https://github.com/hummbl-dev/hummbl-governance/pull/68) [)](https://github.com/hummbl-dev/hummbl-governance/commit/cd87baaff389f2dd019c4aa6abbcc70646c71351 'fix(ci): pin Arbiter governance audit dependency version (#68)

Fixes #66

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[.githooks](https://github.com/hummbl-dev/hummbl-governance/tree/main/.githooks '.githooks')

 | 

[.githooks](https://github.com/hummbl-dev/hummbl-governance/tree/main/.githooks '.githooks')

 | 

[docs: sync README test count to 1032 (](https://github.com/hummbl-dev/hummbl-governance/commit/1ee443d1a1a01ea98777dca712cbb038c330591b 'docs: sync README test count to 1032 (#60)

* chore: fleet-standard migration

* docs: sync README dedicated test count to 1032 (matching badge)

Line 217 said "1026 dedicated tests" while the badge at line 5
and the package summary at line 10 both say 1032.

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* fix(tests): tolerate experimental laws in atlas; omit build/ from coverage

CI environment has 2 extra experimental laws (SL-EXP003, SL-EXP004)
and some laws use 'ratified' status. The hardcoded 17-law expectation
broke CI on main.

Changes:
- test_all_17_laws_loaded: >= 17 with subset check for canonical IDs
- test_law_ids_present: subset check instead of exact equality
- test_all_laws_have_status: add 'ratified' to valid statuses
- test_kernel_boot_loads_atlas, test_kernel_integration_with_atlas: >= 17
- .coveragerc: omit build/ to prevent test-file pollution from build/lib/

Coverage locally: 83% (was 60% in CI due to build/ artifacts)

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#60](https://github.com/hummbl-dev/hummbl-governance/pull/60) [)](https://github.com/hummbl-dev/hummbl-governance/commit/1ee443d1a1a01ea98777dca712cbb038c330591b 'docs: sync README test count to 1032 (#60)

* chore: fleet-standard migration

* docs: sync README dedicated test count to 1032 (matching badge)

Line 217 said "1026 dedicated tests" while the badge at line 5
and the package summary at line 10 both say 1032.

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* fix(tests): tolerate experimental laws in atlas; omit build/ from coverage

CI environment has 2 extra experimental laws (SL-EXP003, SL-EXP004)
and some laws use 'ratified' status. The hardcoded 17-law expectation
broke CI on main.

Changes:
- test_all_17_laws_loaded: >= 17 with subset check for canonical IDs
- test_law_ids_present: subset check instead of exact equality
- test_all_laws_have_status: add 'ratified' to valid statuses
- test_kernel_boot_loads_atlas, test_kernel_integration_with_atlas: >= 17
- .coveragerc: omit build/ to prevent test-file pollution from build/lib/

Coverage locally: 83% (was 60% in CI due to build/ artifacts)

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 20, 2026

 |
| 

[.github](https://github.com/hummbl-dev/hummbl-governance/tree/main/.github '.github')

 | 

[.github](https://github.com/hummbl-dev/hummbl-governance/tree/main/.github '.github')

 | 

[fix(ci): pin Arbiter governance audit dependency version (](https://github.com/hummbl-dev/hummbl-governance/commit/cd87baaff389f2dd019c4aa6abbcc70646c71351 'fix(ci): pin Arbiter governance audit dependency version (#68)

Fixes #66

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#68](https://github.com/hummbl-dev/hummbl-governance/pull/68) [)](https://github.com/hummbl-dev/hummbl-governance/commit/cd87baaff389f2dd019c4aa6abbcc70646c71351 'fix(ci): pin Arbiter governance audit dependency version (#68)

Fixes #66

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[.governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/.governance '.governance')

 | 

[.governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/.governance '.governance')

 | 

[Feat/gemini/v0.4.0 hardening (](https://github.com/hummbl-dev/hummbl-governance/commit/f63e22904d58d47b65b70d36379a352671c74361 'Feat/gemini/v0.4.0 hardening (#16)

* feat: release hummbl-governance v0.4.0

- Add physical_governor.py (pHRI safety monitor, kinematic governor)\n- Integrate Arbiter code quality checks into eal.py validation\n- Expand ReasoningEngine with systems and recursive models\n- Add comprehensive test coverage for ReasoningEngine (L2 resolution)\n- Add init smoke tests for export validation (L3 resolution)\n- Update AUDIT.md with v0.4.0 metrics

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* docs: formalize project roadmap

- Add ROADMAP.md aligned with RIF v6.0\n- Link to roadmap in CONTRIBUTING.md

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* ci: integrate Arbiter governance audit gate

- Add arbiter-governance job to CI\n- Enforce minimum governance score of 90/100

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden LamportClock for causal integrity

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Update tests and __init__.py for v0.5.0 release

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden CoordinationBus and LamportClock

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Add post_to_bus.py script for bus interaction

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* fix: repair PR 16 CI gates

---------

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude (agent) <claude@agents.hummbl.io>') [#16](https://github.com/hummbl-dev/hummbl-governance/pull/16) [)](https://github.com/hummbl-dev/hummbl-governance/commit/f63e22904d58d47b65b70d36379a352671c74361 'Feat/gemini/v0.4.0 hardening (#16)

* feat: release hummbl-governance v0.4.0

- Add physical_governor.py (pHRI safety monitor, kinematic governor)\n- Integrate Arbiter code quality checks into eal.py validation\n- Expand ReasoningEngine with systems and recursive models\n- Add comprehensive test coverage for ReasoningEngine (L2 resolution)\n- Add init smoke tests for export validation (L3 resolution)\n- Update AUDIT.md with v0.4.0 metrics

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* docs: formalize project roadmap

- Add ROADMAP.md aligned with RIF v6.0\n- Link to roadmap in CONTRIBUTING.md

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* ci: integrate Arbiter governance audit gate

- Add arbiter-governance job to CI\n- Enforce minimum governance score of 90/100

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden LamportClock for causal integrity

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Update tests and __init__.py for v0.5.0 release

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden CoordinationBus and LamportClock

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Add post_to_bus.py script for bus interaction

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* fix: repair PR 16 CI gates

---------

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude (agent) <claude@agents.hummbl.io>')

 | 

Apr 19, 2026

 |
| 

[.vscode](https://github.com/hummbl-dev/hummbl-governance/tree/main/.vscode '.vscode')

 | 

[.vscode](https://github.com/hummbl-dev/hummbl-governance/tree/main/.vscode '.vscode')

 | 

[Add initial project files including settings, workflows, and document…](https://github.com/hummbl-dev/hummbl-governance/commit/15825ee27b8df194c59144e1155cd9fe612d9606 'Add initial project files including settings, workflows, and documentation

- Create .vscode/settings.json for Python environment configuration
- Add dependabot.yml for GitHub Actions dependency updates
- Implement CodeQL analysis workflow in .github/workflows/codeql.yml
- Establish CODE_OF_CONDUCT.md and CONTRIBUTING.md for community guidelines
- Include LICENSE file with MIT License details
- Update README.md with repository purpose and usage instructions
- Define SECURITY.md for vulnerability reporting and supported policies')

 | 

Jan 9, 2026

 |
| 

[\_internal](https://github.com/hummbl-dev/hummbl-governance/tree/main/_internal '_internal')

 | 

[\_internal](https://github.com/hummbl-dev/hummbl-governance/tree/main/_internal '_internal')

 | 

[docs(internal): consolidate CI debugging logs into single post-mortem](https://github.com/hummbl-dev/hummbl-governance/commit/7d49c13a089f6d61c1d36310721ff46939678e6e 'docs(internal): consolidate CI debugging logs into single post-mortem

Create CI-POSTMORTEM-2026-05-30.md covering the full 8-hour incident:

22 commits, 6 root causes, 4 agent sessions, final resolution at run 570.

Archive the 4 superseded session files to _internal/_archive/.')

 | 

May 31, 2026

 |
| 

[\_receipts/krineia](https://github.com/hummbl-dev/hummbl-governance/tree/main/_receipts/krineia 'This path skips through empty directories')

 | 

[\_receipts/krineia](https://github.com/hummbl-dev/hummbl-governance/tree/main/_receipts/krineia 'This path skips through empty directories')

 | 

[feat(governance): canonize fleet inventory + init standard v0.1 (](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b 'feat(governance): canonize fleet inventory + init standard v0.1 (#85)

Adds three canonical documents and a schema:

1. FLEET_INVENTORY_2026-06-22.md — complete inventory of every HUMMBL
 repo, local directory, and dependency across 6 surfaces:
 - Private GitHub + Gitea (mirrored): 6 repos with Gitea mirror
 - Private GitHub-only: 38 repos
 - Public GitHub (promotable): 12 active + 9 archived + 21 forks
 - Gitea-only: 6 repos not on GitHub
 - Local git repos (no remote): 24 repos
 - Local non-git directories: 10 in PROJECTS + 9 in home
 - Complete dependency inventory (Python, TypeScript, infrastructure)
 - Non-stdlib exceptions with justifications

2. HUMMBL_INIT_STANDARD.md — v0.1 of the canonical initialization
 standard. Covers initialization procedures for:
 - Repositories (new and existing, active/archived/fork)
 - Python packages (pyproject.toml, stdlib-only, test extras)
 - TypeScript packages (package.json, .test.mjs, strict tsconfig)
 - Cloudflare Workers (wrangler.toml, bindings, health check)
 - MCP servers (stdlib-only, JSON-RPC over stdio)
 - Skills (SKILL.md structure, evals)
 - ADRs (numbering, structure, status lifecycle)
 - Receipts (genesis, chaining, canonical form)
 - Local directories (git init, deny-by-default .gitignore)
 - Fleet inventory entries
 Principles: determinism, grounding, receipt-first, no blind templating,
 idempotency, single source of truth.

3. ADR-005 — decision record for the init standard, documenting the
 context (inconsistency from ad-hoc scripts), decision, alternatives,
 and consequences.

4. schemas/hummbl-init-manifest.schema.json — JSON Schema for init
 manifests, validating artifact type, classification, file set,
 invariants (3-8), receipt chaining, and validation checks.

5. Genesis receipt appended to _receipts/krineia/primary.jsonl for
 the standard adoption.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#85](https://github.com/hummbl-dev/hummbl-governance/pull/85) [)](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b 'feat(governance): canonize fleet inventory + init standard v0.1 (#85)

Adds three canonical documents and a schema:

1. FLEET_INVENTORY_2026-06-22.md — complete inventory of every HUMMBL
 repo, local directory, and dependency across 6 surfaces:
 - Private GitHub + Gitea (mirrored): 6 repos with Gitea mirror
 - Private GitHub-only: 38 repos
 - Public GitHub (promotable): 12 active + 9 archived + 21 forks
 - Gitea-only: 6 repos not on GitHub
 - Local git repos (no remote): 24 repos
 - Local non-git directories: 10 in PROJECTS + 9 in home
 - Complete dependency inventory (Python, TypeScript, infrastructure)
 - Non-stdlib exceptions with justifications

2. HUMMBL_INIT_STANDARD.md — v0.1 of the canonical initialization
 standard. Covers initialization procedures for:
 - Repositories (new and existing, active/archived/fork)
 - Python packages (pyproject.toml, stdlib-only, test extras)
 - TypeScript packages (package.json, .test.mjs, strict tsconfig)
 - Cloudflare Workers (wrangler.toml, bindings, health check)
 - MCP servers (stdlib-only, JSON-RPC over stdio)
 - Skills (SKILL.md structure, evals)
 - ADRs (numbering, structure, status lifecycle)
 - Receipts (genesis, chaining, canonical form)
 - Local directories (git init, deny-by-default .gitignore)
 - Fleet inventory entries
 Principles: determinism, grounding, receipt-first, no blind templating,
 idempotency, single source of truth.

3. ADR-005 — decision record for the init standard, documenting the
 context (inconsistency from ad-hoc scripts), decision, alternatives,
 and consequences.

4. schemas/hummbl-init-manifest.schema.json — JSON Schema for init
 manifests, validating artifact type, classification, file set,
 invariants (3-8), receipt chaining, and validation checks.

5. Genesis receipt appended to _receipts/krineia/primary.jsonl for
 the standard adoption.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[demo](https://github.com/hummbl-dev/hummbl-governance/tree/main/demo 'demo')

 | 

[demo](https://github.com/hummbl-dev/hummbl-governance/tree/main/demo 'demo')

 | 

[feat: add output\_validator + capability\_fence (OWASP ASI-06/07)](https://github.com/hummbl-dev/hummbl-governance/commit/1941481ea803ddaa87ef66c5f0c8e7d1a345bb79 'feat: add output_validator + capability_fence (OWASP ASI-06/07)

output_validator.py: Rule-based content validation with 5 composable
rules (PII, injection, length bounds, blocklist, provenance). Closes
OWASP ASI-06 (Insufficient Output Validation).

capability_fence.py: Soft sandbox enforcing capability boundaries via
delegation tokens. Allow/deny lists, guard wrapper, audit logging.
Closes OWASP ASI-07 (from NONE to PARTIAL).

76 new tests (49 + 27), 476 total passing. Stdlib-only.
OWASP coverage: 5 FULL, 4 PARTIAL, 1 NONE (was 4/4/2).

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 24, 2026

 |
| 

[docs](https://github.com/hummbl-dev/hummbl-governance/tree/main/docs 'docs')

 | 

[docs](https://github.com/hummbl-dev/hummbl-governance/tree/main/docs 'docs')

 | 

[feat(governance): canonize fleet inventory + init standard v0.1 (](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b 'feat(governance): canonize fleet inventory + init standard v0.1 (#85)

Adds three canonical documents and a schema:

1. FLEET_INVENTORY_2026-06-22.md — complete inventory of every HUMMBL
 repo, local directory, and dependency across 6 surfaces:
 - Private GitHub + Gitea (mirrored): 6 repos with Gitea mirror
 - Private GitHub-only: 38 repos
 - Public GitHub (promotable): 12 active + 9 archived + 21 forks
 - Gitea-only: 6 repos not on GitHub
 - Local git repos (no remote): 24 repos
 - Local non-git directories: 10 in PROJECTS + 9 in home
 - Complete dependency inventory (Python, TypeScript, infrastructure)
 - Non-stdlib exceptions with justifications

2. HUMMBL_INIT_STANDARD.md — v0.1 of the canonical initialization
 standard. Covers initialization procedures for:
 - Repositories (new and existing, active/archived/fork)
 - Python packages (pyproject.toml, stdlib-only, test extras)
 - TypeScript packages (package.json, .test.mjs, strict tsconfig)
 - Cloudflare Workers (wrangler.toml, bindings, health check)
 - MCP servers (stdlib-only, JSON-RPC over stdio)
 - Skills (SKILL.md structure, evals)
 - ADRs (numbering, structure, status lifecycle)
 - Receipts (genesis, chaining, canonical form)
 - Local directories (git init, deny-by-default .gitignore)
 - Fleet inventory entries
 Principles: determinism, grounding, receipt-first, no blind templating,
 idempotency, single source of truth.

3. ADR-005 — decision record for the init standard, documenting the
 context (inconsistency from ad-hoc scripts), decision, alternatives,
 and consequences.

4. schemas/hummbl-init-manifest.schema.json — JSON Schema for init
 manifests, validating artifact type, classification, file set,
 invariants (3-8), receipt chaining, and validation checks.

5. Genesis receipt appended to _receipts/krineia/primary.jsonl for
 the standard adoption.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#85](https://github.com/hummbl-dev/hummbl-governance/pull/85) [)](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b 'feat(governance): canonize fleet inventory + init standard v0.1 (#85)

Adds three canonical documents and a schema:

1. FLEET_INVENTORY_2026-06-22.md — complete inventory of every HUMMBL
 repo, local directory, and dependency across 6 surfaces:
 - Private GitHub + Gitea (mirrored): 6 repos with Gitea mirror
 - Private GitHub-only: 38 repos
 - Public GitHub (promotable): 12 active + 9 archived + 21 forks
 - Gitea-only: 6 repos not on GitHub
 - Local git repos (no remote): 24 repos
 - Local non-git directories: 10 in PROJECTS + 9 in home
 - Complete dependency inventory (Python, TypeScript, infrastructure)
 - Non-stdlib exceptions with justifications

2. HUMMBL_INIT_STANDARD.md — v0.1 of the canonical initialization
 standard. Covers initialization procedures for:
 - Repositories (new and existing, active/archived/fork)
 - Python packages (pyproject.toml, stdlib-only, test extras)
 - TypeScript packages (package.json, .test.mjs, strict tsconfig)
 - Cloudflare Workers (wrangler.toml, bindings, health check)
 - MCP servers (stdlib-only, JSON-RPC over stdio)
 - Skills (SKILL.md structure, evals)
 - ADRs (numbering, structure, status lifecycle)
 - Receipts (genesis, chaining, canonical form)
 - Local directories (git init, deny-by-default .gitignore)
 - Fleet inventory entries
 Principles: determinism, grounding, receipt-first, no blind templating,
 idempotency, single source of truth.

3. ADR-005 — decision record for the init standard, documenting the
 context (inconsistency from ad-hoc scripts), decision, alternatives,
 and consequences.

4. schemas/hummbl-init-manifest.schema.json — JSON Schema for init
 manifests, validating artifact type, classification, file set,
 invariants (3-8), receipt chaining, and validation checks.

5. Genesis receipt appended to _receipts/krineia/primary.jsonl for
 the standard adoption.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[examples](https://github.com/hummbl-dev/hummbl-governance/tree/main/examples 'examples')

 | 

[examples](https://github.com/hummbl-dev/hummbl-governance/tree/main/examples 'examples')

 | 

[fix(lint): resolve all 34 ruff findings for CI green](https://github.com/hummbl-dev/hummbl-governance/commit/d2b28164b51fb8af39a765979abfa39e448e5582 'fix(lint): resolve all 34 ruff findings for CI green

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 26, 2026

 |
| 

[governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/governance 'governance')

 | 

[governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/governance 'governance')

 | 

[chore(governance): pin CAES\_SPEC v1.0.0 (](https://github.com/hummbl-dev/hummbl-governance/commit/42cc6a82c8cf7f87950699b49bb4db75acf153e0 'chore(governance): pin CAES_SPEC v1.0.0 (#3)') [#3](https://github.com/hummbl-dev/hummbl-governance/pull/3) [)](https://github.com/hummbl-dev/hummbl-governance/commit/42cc6a82c8cf7f87950699b49bb4db75acf153e0 'chore(governance): pin CAES_SPEC v1.0.0 (#3)')

 | 

Feb 15, 2026

 |
| 

[hummbl-governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/hummbl-governance 'hummbl-governance')

 | 

[hummbl-governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/hummbl-governance 'hummbl-governance')

 | 

[Remove unused build-mode configuration from CodeQL workflow](https://github.com/hummbl-dev/hummbl-governance/commit/688b7ac51b29ea925ecdf22b2095083232593f9f 'Remove unused build-mode configuration from CodeQL workflow')

 | 

Jan 9, 2026

 |
| 

[hummbl\_governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/hummbl_governance 'hummbl_governance')

 | 

[hummbl\_governance](https://github.com/hummbl-dev/hummbl-governance/tree/main/hummbl_governance 'hummbl_governance')

 | 

[feat(schema): promote evidence-readiness review receipt to governed s…](https://github.com/hummbl-dev/hummbl-governance/commit/e636089baa459963f0fe79ee5493923e785e4fb6 'feat(schema): promote evidence-readiness review receipt to governed surface (#70)

Fixes #67

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[schemas](https://github.com/hummbl-dev/hummbl-governance/tree/main/schemas 'schemas')

 | 

[schemas](https://github.com/hummbl-dev/hummbl-governance/tree/main/schemas 'schemas')

 | 

[feat(governance): canonize fleet inventory + init standard v0.1 (](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b 'feat(governance): canonize fleet inventory + init standard v0.1 (#85)

Adds three canonical documents and a schema:

1. FLEET_INVENTORY_2026-06-22.md — complete inventory of every HUMMBL
 repo, local directory, and dependency across 6 surfaces:
 - Private GitHub + Gitea (mirrored): 6 repos with Gitea mirror
 - Private GitHub-only: 38 repos
 - Public GitHub (promotable): 12 active + 9 archived + 21 forks
 - Gitea-only: 6 repos not on GitHub
 - Local git repos (no remote): 24 repos
 - Local non-git directories: 10 in PROJECTS + 9 in home
 - Complete dependency inventory (Python, TypeScript, infrastructure)
 - Non-stdlib exceptions with justifications

2. HUMMBL_INIT_STANDARD.md — v0.1 of the canonical initialization
 standard. Covers initialization procedures for:
 - Repositories (new and existing, active/archived/fork)
 - Python packages (pyproject.toml, stdlib-only, test extras)
 - TypeScript packages (package.json, .test.mjs, strict tsconfig)
 - Cloudflare Workers (wrangler.toml, bindings, health check)
 - MCP servers (stdlib-only, JSON-RPC over stdio)
 - Skills (SKILL.md structure, evals)
 - ADRs (numbering, structure, status lifecycle)
 - Receipts (genesis, chaining, canonical form)
 - Local directories (git init, deny-by-default .gitignore)
 - Fleet inventory entries
 Principles: determinism, grounding, receipt-first, no blind templating,
 idempotency, single source of truth.

3. ADR-005 — decision record for the init standard, documenting the
 context (inconsistency from ad-hoc scripts), decision, alternatives,
 and consequences.

4. schemas/hummbl-init-manifest.schema.json — JSON Schema for init
 manifests, validating artifact type, classification, file set,
 invariants (3-8), receipt chaining, and validation checks.

5. Genesis receipt appended to _receipts/krineia/primary.jsonl for
 the standard adoption.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#85](https://github.com/hummbl-dev/hummbl-governance/pull/85) [)](https://github.com/hummbl-dev/hummbl-governance/commit/70fa0814737e6a4f920a2df34993f7fbe464d14b 'feat(governance): canonize fleet inventory + init standard v0.1 (#85)

Adds three canonical documents and a schema:

1. FLEET_INVENTORY_2026-06-22.md — complete inventory of every HUMMBL
 repo, local directory, and dependency across 6 surfaces:
 - Private GitHub + Gitea (mirrored): 6 repos with Gitea mirror
 - Private GitHub-only: 38 repos
 - Public GitHub (promotable): 12 active + 9 archived + 21 forks
 - Gitea-only: 6 repos not on GitHub
 - Local git repos (no remote): 24 repos
 - Local non-git directories: 10 in PROJECTS + 9 in home
 - Complete dependency inventory (Python, TypeScript, infrastructure)
 - Non-stdlib exceptions with justifications

2. HUMMBL_INIT_STANDARD.md — v0.1 of the canonical initialization
 standard. Covers initialization procedures for:
 - Repositories (new and existing, active/archived/fork)
 - Python packages (pyproject.toml, stdlib-only, test extras)
 - TypeScript packages (package.json, .test.mjs, strict tsconfig)
 - Cloudflare Workers (wrangler.toml, bindings, health check)
 - MCP servers (stdlib-only, JSON-RPC over stdio)
 - Skills (SKILL.md structure, evals)
 - ADRs (numbering, structure, status lifecycle)
 - Receipts (genesis, chaining, canonical form)
 - Local directories (git init, deny-by-default .gitignore)
 - Fleet inventory entries
 Principles: determinism, grounding, receipt-first, no blind templating,
 idempotency, single source of truth.

3. ADR-005 — decision record for the init standard, documenting the
 context (inconsistency from ad-hoc scripts), decision, alternatives,
 and consequences.

4. schemas/hummbl-init-manifest.schema.json — JSON Schema for init
 manifests, validating artifact type, classification, file set,
 invariants (3-8), receipt chaining, and validation checks.

5. Genesis receipt appended to _receipts/krineia/primary.jsonl for
 the standard adoption.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[scripts](https://github.com/hummbl-dev/hummbl-governance/tree/main/scripts 'scripts')

 | 

[scripts](https://github.com/hummbl-dev/hummbl-governance/tree/main/scripts 'scripts')

 | 

[fix(scripts): add package init for scripts and fix version test asser…](https://github.com/hummbl-dev/hummbl-governance/commit/2068603ad3ed4bdf9995b03a67bd8fbe02635a2f 'fix(scripts): add package init for scripts and fix version test assertion')

 | 

Jun 8, 2026

 |
| 

[tests](https://github.com/hummbl-dev/hummbl-governance/tree/main/tests 'tests')

 | 

[tests](https://github.com/hummbl-dev/hummbl-governance/tree/main/tests 'tests')

 | 

[feat(schema): promote evidence-readiness review receipt to governed s…](https://github.com/hummbl-dev/hummbl-governance/commit/e636089baa459963f0fe79ee5493923e785e4fb6 'feat(schema): promote evidence-readiness review receipt to governed surface (#70)

Fixes #67

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[.coveragerc](https://github.com/hummbl-dev/hummbl-governance/blob/main/.coveragerc '.coveragerc')

 | 

[.coveragerc](https://github.com/hummbl-dev/hummbl-governance/blob/main/.coveragerc '.coveragerc')

 | 

[docs: sync README test count to 1032 (](https://github.com/hummbl-dev/hummbl-governance/commit/1ee443d1a1a01ea98777dca712cbb038c330591b 'docs: sync README test count to 1032 (#60)

* chore: fleet-standard migration

* docs: sync README dedicated test count to 1032 (matching badge)

Line 217 said "1026 dedicated tests" while the badge at line 5
and the package summary at line 10 both say 1032.

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* fix(tests): tolerate experimental laws in atlas; omit build/ from coverage

CI environment has 2 extra experimental laws (SL-EXP003, SL-EXP004)
and some laws use 'ratified' status. The hardcoded 17-law expectation
broke CI on main.

Changes:
- test_all_17_laws_loaded: >= 17 with subset check for canonical IDs
- test_law_ids_present: subset check instead of exact equality
- test_all_laws_have_status: add 'ratified' to valid statuses
- test_kernel_boot_loads_atlas, test_kernel_integration_with_atlas: >= 17
- .coveragerc: omit build/ to prevent test-file pollution from build/lib/

Coverage locally: 83% (was 60% in CI due to build/ artifacts)

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#60](https://github.com/hummbl-dev/hummbl-governance/pull/60) [)](https://github.com/hummbl-dev/hummbl-governance/commit/1ee443d1a1a01ea98777dca712cbb038c330591b 'docs: sync README test count to 1032 (#60)

* chore: fleet-standard migration

* docs: sync README dedicated test count to 1032 (matching badge)

Line 217 said "1026 dedicated tests" while the badge at line 5
and the package summary at line 10 both say 1032.

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* fix(tests): tolerate experimental laws in atlas; omit build/ from coverage

CI environment has 2 extra experimental laws (SL-EXP003, SL-EXP004)
and some laws use 'ratified' status. The hardcoded 17-law expectation
broke CI on main.

Changes:
- test_all_17_laws_loaded: >= 17 with subset check for canonical IDs
- test_law_ids_present: subset check instead of exact equality
- test_all_laws_have_status: add 'ratified' to valid statuses
- test_kernel_boot_loads_atlas, test_kernel_integration_with_atlas: >= 17
- .coveragerc: omit build/ to prevent test-file pollution from build/lib/

Coverage locally: 83% (was 60% in CI due to build/ artifacts)

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 20, 2026

 |
| 

[.env.example](https://github.com/hummbl-dev/hummbl-governance/blob/main/.env.example '.env.example')

 | 

[.env.example](https://github.com/hummbl-dev/hummbl-governance/blob/main/.env.example '.env.example')

 | 

[chore(env): add .env.example documenting all known environment variab…](https://github.com/hummbl-dev/hummbl-governance/commit/47bbfe9c3fe40ee651f07062e3f8f8b1eeb7a803 'chore(env): add .env.example documenting all known environment variables (#63)

Documents state directories, MCP/sandbox paths, signing secrets,
and test overrides used across the codebase. All values are
commented-out with sensitivity markers.

Closes #61

Generated with Devin

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>')

 | 

Jun 20, 2026

 |
| 

[.gitignore](https://github.com/hummbl-dev/hummbl-governance/blob/main/.gitignore '.gitignore')

 | 

[.gitignore](https://github.com/hummbl-dev/hummbl-governance/blob/main/.gitignore '.gitignore')

 | 

[fix(kernel): stabilize governance v1.2.0 health gates (](https://github.com/hummbl-dev/hummbl-governance/commit/4abc2fb18df9c04c78a2b55b4bf8fe585e2b8cc1 'fix(kernel): stabilize governance v1.2.0 health gates (#58)

* fix(kernel): stabilize governance v1.2.0 health gates

Align package metadata with v1.2.0, update law-atlas expectations, keep model registry writes out of package source, remove private registry placeholders, and serialize receipt file access.

Also clears Ruff findings across duplicated kernel test suites so mainline quality gates can run cleanly.

* ci(coverage): omit packaged kernel tests

Keep package-side duplicated test modules out of source coverage accounting so the CI coverage gate measures runtime modules instead of uncollected tests.') [#58](https://github.com/hummbl-dev/hummbl-governance/pull/58) [)](https://github.com/hummbl-dev/hummbl-governance/commit/4abc2fb18df9c04c78a2b55b4bf8fe585e2b8cc1 'fix(kernel): stabilize governance v1.2.0 health gates (#58)

* fix(kernel): stabilize governance v1.2.0 health gates

Align package metadata with v1.2.0, update law-atlas expectations, keep model registry writes out of package source, remove private registry placeholders, and serialize receipt file access.

Also clears Ruff findings across duplicated kernel test suites so mainline quality gates can run cleanly.

* ci(coverage): omit packaged kernel tests

Keep package-side duplicated test modules out of source coverage accounting so the CI coverage gate measures runtime modules instead of uncollected tests.')

 | 

Jun 20, 2026

 |
| 

[.pre-commit-config.yaml](https://github.com/hummbl-dev/hummbl-governance/blob/main/.pre-commit-config.yaml '.pre-commit-config.yaml')

 | 

[.pre-commit-config.yaml](https://github.com/hummbl-dev/hummbl-governance/blob/main/.pre-commit-config.yaml '.pre-commit-config.yaml')

 | 

[docs: sync README test count to 1032 (](https://github.com/hummbl-dev/hummbl-governance/commit/1ee443d1a1a01ea98777dca712cbb038c330591b 'docs: sync README test count to 1032 (#60)

* chore: fleet-standard migration

* docs: sync README dedicated test count to 1032 (matching badge)

Line 217 said "1026 dedicated tests" while the badge at line 5
and the package summary at line 10 both say 1032.

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* fix(tests): tolerate experimental laws in atlas; omit build/ from coverage

CI environment has 2 extra experimental laws (SL-EXP003, SL-EXP004)
and some laws use 'ratified' status. The hardcoded 17-law expectation
broke CI on main.

Changes:
- test_all_17_laws_loaded: >= 17 with subset check for canonical IDs
- test_law_ids_present: subset check instead of exact equality
- test_all_laws_have_status: add 'ratified' to valid statuses
- test_kernel_boot_loads_atlas, test_kernel_integration_with_atlas: >= 17
- .coveragerc: omit build/ to prevent test-file pollution from build/lib/

Coverage locally: 83% (was 60% in CI due to build/ artifacts)

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#60](https://github.com/hummbl-dev/hummbl-governance/pull/60) [)](https://github.com/hummbl-dev/hummbl-governance/commit/1ee443d1a1a01ea98777dca712cbb038c330591b 'docs: sync README test count to 1032 (#60)

* chore: fleet-standard migration

* docs: sync README dedicated test count to 1032 (matching badge)

Line 217 said "1026 dedicated tests" while the badge at line 5
and the package summary at line 10 both say 1032.

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* fix(tests): tolerate experimental laws in atlas; omit build/ from coverage

CI environment has 2 extra experimental laws (SL-EXP003, SL-EXP004)
and some laws use 'ratified' status. The hardcoded 17-law expectation
broke CI on main.

Changes:
- test_all_17_laws_loaded: >= 17 with subset check for canonical IDs
- test_law_ids_present: subset check instead of exact equality
- test_all_laws_have_status: add 'ratified' to valid statuses
- test_kernel_boot_loads_atlas, test_kernel_integration_with_atlas: >= 17
- .coveragerc: omit build/ to prevent test-file pollution from build/lib/

Coverage locally: 83% (was 60% in CI due to build/ artifacts)

Generated with [Devin](https://devin.ai)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 20, 2026

 |
| 

[AGENTS.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/AGENTS.md 'AGENTS.md')

 | 

[AGENTS.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/AGENTS.md 'AGENTS.md')

 | 

[fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (](https://github.com/hummbl-dev/hummbl-governance/commit/74d4479d593dded362c314be6df9e42084b01241 'fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (#69)

Fixes #64, #65

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#69](https://github.com/hummbl-dev/hummbl-governance/pull/69) [)](https://github.com/hummbl-dev/hummbl-governance/commit/74d4479d593dded362c314be6df9e42084b01241 'fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (#69)

Fixes #64, #65

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[AUDIT.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/AUDIT.md 'AUDIT.md')

 | 

[AUDIT.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/AUDIT.md 'AUDIT.md')

 | 

[Feat/gemini/v0.4.0 hardening (](https://github.com/hummbl-dev/hummbl-governance/commit/f63e22904d58d47b65b70d36379a352671c74361 'Feat/gemini/v0.4.0 hardening (#16)

* feat: release hummbl-governance v0.4.0

- Add physical_governor.py (pHRI safety monitor, kinematic governor)\n- Integrate Arbiter code quality checks into eal.py validation\n- Expand ReasoningEngine with systems and recursive models\n- Add comprehensive test coverage for ReasoningEngine (L2 resolution)\n- Add init smoke tests for export validation (L3 resolution)\n- Update AUDIT.md with v0.4.0 metrics

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* docs: formalize project roadmap

- Add ROADMAP.md aligned with RIF v6.0\n- Link to roadmap in CONTRIBUTING.md

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* ci: integrate Arbiter governance audit gate

- Add arbiter-governance job to CI\n- Enforce minimum governance score of 90/100

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden LamportClock for causal integrity

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Update tests and __init__.py for v0.5.0 release

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden CoordinationBus and LamportClock

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Add post_to_bus.py script for bus interaction

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* fix: repair PR 16 CI gates

---------

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude (agent) <claude@agents.hummbl.io>') [#16](https://github.com/hummbl-dev/hummbl-governance/pull/16) [)](https://github.com/hummbl-dev/hummbl-governance/commit/f63e22904d58d47b65b70d36379a352671c74361 'Feat/gemini/v0.4.0 hardening (#16)

* feat: release hummbl-governance v0.4.0

- Add physical_governor.py (pHRI safety monitor, kinematic governor)\n- Integrate Arbiter code quality checks into eal.py validation\n- Expand ReasoningEngine with systems and recursive models\n- Add comprehensive test coverage for ReasoningEngine (L2 resolution)\n- Add init smoke tests for export validation (L3 resolution)\n- Update AUDIT.md with v0.4.0 metrics

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* docs: formalize project roadmap

- Add ROADMAP.md aligned with RIF v6.0\n- Link to roadmap in CONTRIBUTING.md

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* ci: integrate Arbiter governance audit gate

- Add arbiter-governance job to CI\n- Enforce minimum governance score of 90/100

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden LamportClock for causal integrity

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Update tests and __init__.py for v0.5.0 release

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden CoordinationBus and LamportClock

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Add post_to_bus.py script for bus interaction

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* fix: repair PR 16 CI gates

---------

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude (agent) <claude@agents.hummbl.io>')

 | 

Apr 19, 2026

 |
| 

[CHANGELOG.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CHANGELOG.md 'CHANGELOG.md')

 | 

[CHANGELOG.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CHANGELOG.md 'CHANGELOG.md')

 | 

[feat(standards): add HUMMBL Repo Standard v0.1 + manifest schema + AD…](https://github.com/hummbl-dev/hummbl-governance/commit/faee86f9e1ccc6a82b969c56b01f529af02ba1b4 'feat(standards): add HUMMBL Repo Standard v0.1 + manifest schema + ADR-003 (#71)

Defines the global baseline for all hummbl-dev repositories: a 15-item
artifact stack, five repo classes (spec/governance, code/library,
docs/research, fork, archived) with required/prescribed/optional
weightings, a conflict-precedence ladder rooted at the operating-
environment constitution, a machine-readable hummbl.repo.yaml manifest
governed by JSON Schema Draft 2020-12, and a provider-neutrality
constraint on all root governance files.

Routing doctrine: deterministic spine, stochastic muscle. Models
propose, schemas constrain, validators decide, git records, KRINEIA
proves, humans authorize.

ADR-003 records the live 91-repo audit findings (0% KRINEIA.md, 0%
hummbl.repo.yaml, 1% CONSTITUTION.md coverage) and the split-home
choice: canonical standard + schema in hummbl-governance, templates
mirrored in .github.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[CLAUDE.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CLAUDE.md 'CLAUDE.md')

 | 

[CLAUDE.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CLAUDE.md 'CLAUDE.md')

 | 

[fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (](https://github.com/hummbl-dev/hummbl-governance/commit/74d4479d593dded362c314be6df9e42084b01241 'fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (#69)

Fixes #64, #65

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#69](https://github.com/hummbl-dev/hummbl-governance/pull/69) [)](https://github.com/hummbl-dev/hummbl-governance/commit/74d4479d593dded362c314be6df9e42084b01241 'fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (#69)

Fixes #64, #65

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[CODEOWNERS](https://github.com/hummbl-dev/hummbl-governance/blob/main/CODEOWNERS 'CODEOWNERS')

 | 

[CODEOWNERS](https://github.com/hummbl-dev/hummbl-governance/blob/main/CODEOWNERS 'CODEOWNERS')

 | 

[feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (](https://github.com/hummbl-dev/hummbl-governance/commit/edb06889008d7d47695e1b79ced085e62680c439 'feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (#77)

The canonical standard host adopts its own standard. Adds:
- CONSTITUTION.md: 8 protected invariants (zero runtime deps, coverage
 floor, thread safety, MCP tool contract, Apache-2.0, receipt integrity,
 schema stability, canonical standard host)
- KRINEIA.md: repo-local receipt manifest
- hummbl.repo.yaml: machine-readable manifest
- CODEOWNERS: normative files require steward approval
- docs/adr/ADR-004: decision record
- _receipts/krineia/primary.jsonl: genesis receipt
- docs/handoffs/2026-06-22: handoff note

AGENTS.md unchanged.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#77](https://github.com/hummbl-dev/hummbl-governance/pull/77)

 | 

Jun 22, 2026

 |
| 

[CODE\_OF\_CONDUCT.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CODE_OF_CONDUCT.md 'CODE_OF_CONDUCT.md')

 | 

[CODE\_OF\_CONDUCT.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CODE_OF_CONDUCT.md 'CODE_OF_CONDUCT.md')

 | 

[docs(governance): add CODE\_OF\_CONDUCT.md](https://github.com/hummbl-dev/hummbl-governance/commit/17ce72b082551a2799ae145bf5153afa98ca0e8f 'docs(governance): add CODE_OF_CONDUCT.md')

 | 

Jun 20, 2026

 |
| 

[CONSTITUTION.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CONSTITUTION.md 'CONSTITUTION.md')

 | 

[CONSTITUTION.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CONSTITUTION.md 'CONSTITUTION.md')

 | 

[feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (](https://github.com/hummbl-dev/hummbl-governance/commit/edb06889008d7d47695e1b79ced085e62680c439 'feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (#77)

The canonical standard host adopts its own standard. Adds:
- CONSTITUTION.md: 8 protected invariants (zero runtime deps, coverage
 floor, thread safety, MCP tool contract, Apache-2.0, receipt integrity,
 schema stability, canonical standard host)
- KRINEIA.md: repo-local receipt manifest
- hummbl.repo.yaml: machine-readable manifest
- CODEOWNERS: normative files require steward approval
- docs/adr/ADR-004: decision record
- _receipts/krineia/primary.jsonl: genesis receipt
- docs/handoffs/2026-06-22: handoff note

AGENTS.md unchanged.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#77](https://github.com/hummbl-dev/hummbl-governance/pull/77)

 | 

Jun 22, 2026

 |
| 

[CONTRIBUTING.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CONTRIBUTING.md 'CONTRIBUTING.md')

 | 

[CONTRIBUTING.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/CONTRIBUTING.md 'CONTRIBUTING.md')

 | 

[feat: extract Kernel governance OS + docs update for v1.1.0 (](https://github.com/hummbl-dev/hummbl-governance/commit/2a63803e09ce1e4f1d677b8965cafaef6d9f335f 'feat: extract Kernel governance OS + docs update for v1.1.0 (#56)

* docs: add CONTRIBUTING.md with design checklist and PR process

Adds comprehensive contribution guidelines covering:
- Development setup (venv, pip install, pytest with coverage)
- Priority ranking for contributions (bug fixes > docs > new primitives)
- Explicit rejection criteria (no new deps, no UIs, no framework adapters)
- PR process: branch naming, commit format, CI requirements
- Code standards: Python 3.11+, type hints, Google docstrings
- Governance Primitive Design Checklist (8 criteria)
- Security reporting via email (not public issues)

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* security(wargame-fixes): address P1, P2, P4 residuals from adversarial exercise

P1 — Vendor hummbl_library types (CRITICAL supply chain fix):
- Create hummbl_governance/_types.py with all governance primitives:
 KillSwitchMode, CircuitBreakerState, PolicyLevel, AuditEntry,
 ResourceSelector, Caveat, TokenBinding, DelegationToken,
 UsageRecord, BudgetStatus
- Remove try/except ImportError fallback pattern from 6 modules:
 kill_switch, circuit_breaker, coordination_bus, audit_log,
 cost_governor, delegation
- Eliminates supply-chain hijack vector where malicious hummbl_library
 package silently overrides core governance types

P2 — TrustTier Enum + alias cycle detection (HIGH):
- Add TrustTier enum (OWNER, SYSTEM, HIGH, MEDIUM, LOW) with
 from_str() factory that validates and normalizes inputs
- register_agent() now validates trust parameter via TrustTier.from_str()
- add_alias() detects direct and indirect cycles (ValueError)
- canonicalize() / _lookup_alias() bounded to 50 steps to prevent
 infinite loops from corrupted/attacked alias chains
- Export TrustTier from __init__.py

P4 — Schema validator max_depth (HIGH recursion DoS):
- Add depth/max_depth parameters to _validate() and all callees
- Default max_depth=50 prevents RecursionError from deeply nested
 or self-referential schemas submitted via MCP endpoints

Tests: 1028/1028 passed (excluding pre-existing version assertion)

Refs: wargame report hummbl-production/_internal/wargame/hummbl-governance_2026-06-14/

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* feat: extract Kernel governance OS as v1.1.0

Add the HUMMBL Governance Kernel (26th primitive) to hummbl-governance:
- 12 runtime modules: kernel, receipt_engine, law_engine, identity_engine,
 sequence_engine, evidence_engine, authority_engine, schedule_engine,
 invariants, cli, __main__
- 10 test files with 136 tests: adversarial, chaos, edge_cases, fuzzing,
 integration, invariants, law_atlas, performance, properties, race_recovery
- 17 scaling laws loaded from Scaling Law Atlas (SL-01 through SL-17)
- Portable paths via HUMMBL_KERNEL_STATE_DIR and HUMMBL_KERNEL_ATLAS_DIR
- Zero third-party runtime dependencies (stdlib only)
- Full CLI: boot, status, health, inspect, laws, roles

Bump version to 1.1.0, export all Kernel symbols from __init__.py,
update test_init_exports with version assertion and Kernel primitive checks.

All 1032 tests pass (136 kernel + 896 existing) with zero regressions.

Refs: KERNEL_DOCTRINE.md, KERNEL_IaC.md, KERNEL_EXTRACTION_PLAN.md

* docs: update README, CLAUDE, AGENTS for v1.1.0 Kernel primitive

- README: 25→26 primitives, 1031→1032 tests, What's New in v1.1.0 section
- CLAUDE: v0.8.0→v1.1.0, 25→26 primitives, Kernel category added
- AGENTS: v0.8.0→v1.1.0, 1031→1032 tests, Kernel added to scope
- Add ROLLOUT_v1.1.0.md with dependency upgrade guide for 10 repos

Refs: KERNEL_DOCTRINE.md, KERNEL_IaC.md, KERNEL_EXTRACTION_PLAN.md

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#56](https://github.com/hummbl-dev/hummbl-governance/pull/56) [)](https://github.com/hummbl-dev/hummbl-governance/commit/2a63803e09ce1e4f1d677b8965cafaef6d9f335f 'feat: extract Kernel governance OS + docs update for v1.1.0 (#56)

* docs: add CONTRIBUTING.md with design checklist and PR process

Adds comprehensive contribution guidelines covering:
- Development setup (venv, pip install, pytest with coverage)
- Priority ranking for contributions (bug fixes > docs > new primitives)
- Explicit rejection criteria (no new deps, no UIs, no framework adapters)
- PR process: branch naming, commit format, CI requirements
- Code standards: Python 3.11+, type hints, Google docstrings
- Governance Primitive Design Checklist (8 criteria)
- Security reporting via email (not public issues)

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* security(wargame-fixes): address P1, P2, P4 residuals from adversarial exercise

P1 — Vendor hummbl_library types (CRITICAL supply chain fix):
- Create hummbl_governance/_types.py with all governance primitives:
 KillSwitchMode, CircuitBreakerState, PolicyLevel, AuditEntry,
 ResourceSelector, Caveat, TokenBinding, DelegationToken,
 UsageRecord, BudgetStatus
- Remove try/except ImportError fallback pattern from 6 modules:
 kill_switch, circuit_breaker, coordination_bus, audit_log,
 cost_governor, delegation
- Eliminates supply-chain hijack vector where malicious hummbl_library
 package silently overrides core governance types

P2 — TrustTier Enum + alias cycle detection (HIGH):
- Add TrustTier enum (OWNER, SYSTEM, HIGH, MEDIUM, LOW) with
 from_str() factory that validates and normalizes inputs
- register_agent() now validates trust parameter via TrustTier.from_str()
- add_alias() detects direct and indirect cycles (ValueError)
- canonicalize() / _lookup_alias() bounded to 50 steps to prevent
 infinite loops from corrupted/attacked alias chains
- Export TrustTier from __init__.py

P4 — Schema validator max_depth (HIGH recursion DoS):
- Add depth/max_depth parameters to _validate() and all callees
- Default max_depth=50 prevents RecursionError from deeply nested
 or self-referential schemas submitted via MCP endpoints

Tests: 1028/1028 passed (excluding pre-existing version assertion)

Refs: wargame report hummbl-production/_internal/wargame/hummbl-governance_2026-06-14/

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* feat: extract Kernel governance OS as v1.1.0

Add the HUMMBL Governance Kernel (26th primitive) to hummbl-governance:
- 12 runtime modules: kernel, receipt_engine, law_engine, identity_engine,
 sequence_engine, evidence_engine, authority_engine, schedule_engine,
 invariants, cli, __main__
- 10 test files with 136 tests: adversarial, chaos, edge_cases, fuzzing,
 integration, invariants, law_atlas, performance, properties, race_recovery
- 17 scaling laws loaded from Scaling Law Atlas (SL-01 through SL-17)
- Portable paths via HUMMBL_KERNEL_STATE_DIR and HUMMBL_KERNEL_ATLAS_DIR
- Zero third-party runtime dependencies (stdlib only)
- Full CLI: boot, status, health, inspect, laws, roles

Bump version to 1.1.0, export all Kernel symbols from __init__.py,
update test_init_exports with version assertion and Kernel primitive checks.

All 1032 tests pass (136 kernel + 896 existing) with zero regressions.

Refs: KERNEL_DOCTRINE.md, KERNEL_IaC.md, KERNEL_EXTRACTION_PLAN.md

* docs: update README, CLAUDE, AGENTS for v1.1.0 Kernel primitive

- README: 25→26 primitives, 1031→1032 tests, What's New in v1.1.0 section
- CLAUDE: v0.8.0→v1.1.0, 25→26 primitives, Kernel category added
- AGENTS: v0.8.0→v1.1.0, 1031→1032 tests, Kernel added to scope
- Add ROLLOUT_v1.1.0.md with dependency upgrade guide for 10 repos

Refs: KERNEL_DOCTRINE.md, KERNEL_IaC.md, KERNEL_EXTRACTION_PLAN.md

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 17, 2026

 |
| 

[KRINEIA.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/KRINEIA.md 'KRINEIA.md')

 | 

[KRINEIA.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/KRINEIA.md 'KRINEIA.md')

 | 

[feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (](https://github.com/hummbl-dev/hummbl-governance/commit/edb06889008d7d47695e1b79ced085e62680c439 'feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (#77)

The canonical standard host adopts its own standard. Adds:
- CONSTITUTION.md: 8 protected invariants (zero runtime deps, coverage
 floor, thread safety, MCP tool contract, Apache-2.0, receipt integrity,
 schema stability, canonical standard host)
- KRINEIA.md: repo-local receipt manifest
- hummbl.repo.yaml: machine-readable manifest
- CODEOWNERS: normative files require steward approval
- docs/adr/ADR-004: decision record
- _receipts/krineia/primary.jsonl: genesis receipt
- docs/handoffs/2026-06-22: handoff note

AGENTS.md unchanged.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#77](https://github.com/hummbl-dev/hummbl-governance/pull/77)

 | 

Jun 22, 2026

 |
| 

[LICENSE](https://github.com/hummbl-dev/hummbl-governance/blob/main/LICENSE 'LICENSE')

 | 

[LICENSE](https://github.com/hummbl-dev/hummbl-governance/blob/main/LICENSE 'LICENSE')

 | 

[feat: extract governance primitives from founder-mode](https://github.com/hummbl-dev/hummbl-governance/commit/eb6da0916287d6652b9e38be843f23b2ed3833ff 'feat: extract governance primitives from founder-mode

Complete extraction of 7 governance modules from founder-mode into
standalone, stdlib-only package:

- kill_switch.py: Emergency halt with 4 graduated modes (DISENGAGED,
 HALT_NONCRITICAL, HALT_ALL, EMERGENCY), configurable critical tasks,
 HMAC-signed persistence, subscriber notifications
- circuit_breaker.py: 3-state automatic failure detection (CLOSED,
 OPEN, HALF_OPEN) with configurable thresholds and recovery timeout
- cost_governor.py: SQLite-backed budget tracking with ALLOW/WARN/DENY
 decisions, soft/hard caps, provider and model breakdowns
- delegation.py: HMAC-SHA256 signed capability tokens with expiry,
 binding to tasks/contracts, and least-privilege enforcement
- audit_log.py: Append-only JSONL governance log with daily rotation,
 retention enforcement, amendment chains, cross-link queries
- identity.py: Generic agent registry with aliases, trust tiers,
 services, deprecated/retired identities (no hardcoded agents)
- schema_validator.py: Stdlib-only JSON Schema validator (Draft 2020-12
 subset: type, required, properties, enum, pattern, oneOf, anyOf, etc.)

All modules are independently importable, thread-safe, and use zero
third-party runtime dependencies. 157 tests passing.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 23, 2026

 |
| 

[Makefile](https://github.com/hummbl-dev/hummbl-governance/blob/main/Makefile 'Makefile')

 | 

[Makefile](https://github.com/hummbl-dev/hummbl-governance/blob/main/Makefile 'Makefile')

 | 

[feat(errors): FM taxonomy + unified error enum v0.4.0 (](https://github.com/hummbl-dev/hummbl-governance/commit/2fbebffed93be8928955d6e61f0e9c95621ad575 'feat(errors): FM taxonomy + unified error enum v0.4.0 (#11)

* docs: update founder-mode test count 7700 → 14900

founder-mode now has 14,900+ tests (was 7,700+ when this line was
originally written). Keeping the count current so the production-tested
claim stays accurate.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

* feat(errors): migrate FM taxonomy + unified error enum to v0.4.0

- Add errors.py: FailureMode enum (FM1–FM30), HummblError enum
 (14 HG_E_* runtime codes), FM_TO_ERRORS mapping, fm_to_errors()
 helper, and 14 IDP_E_* backward-compat aliases
- Add failure_modes.py: FailureModeRecord + ErrorRecord dataclasses,
 lru_cache loaders for fm.json/err.json/mappings.json, public API
 (all_failure_modes, get_fm, classify_subclass, get_errors_for_fm,
 all_error_records)
- Copy fm.json (30 FMs), err.json (3 error records), mappings.json
 (40 subclass→FM entries) from base120/registries/ into package data/
- Fix reasoning.py: replace Optional/Dict with X|None/dict (PEP 604)
- Fix delegation.py: replace bare E_* string constants with
 HummblError.*.value refs from the new unified enum
- Add 70 tests across test_errors.py + test_failure_modes.py
- Bump version 0.3.0 → 0.4.0

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

* fix(lint): move delegation.py import to top, remove unused pytest import

Fixes two ruff violations blocking CI lint gate:
- E402: `from hummbl_governance.errors import HummblError` was at line 134
 (after class definitions) — moved to module-level imports block
- F401: `import pytest` in test_errors.py was unused — removed

546 tests still pass.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

* chore(quality): add ruff to test extras, Makefile lint target, test conventions

- pyproject.toml: add ruff>=0.4 to [test] extras so `pip install -e.[test]`
 also installs the linter; enables `make lint` locally
- Makefile: add lint + test targets (ruff check . / pytest tests/ -v)
- CONTRIBUTING.md: document test file conventions — only import pytest/stdlib
 modules when actually used; F401 fails the lint gate

Addresses AAR recommendations [HIGH] and [LOW].

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>') [#11](https://github.com/hummbl-dev/hummbl-governance/pull/11) [)](https://github.com/hummbl-dev/hummbl-governance/commit/2fbebffed93be8928955d6e61f0e9c95621ad575 'feat(errors): FM taxonomy + unified error enum v0.4.0 (#11)

* docs: update founder-mode test count 7700 → 14900

founder-mode now has 14,900+ tests (was 7,700+ when this line was
originally written). Keeping the count current so the production-tested
claim stays accurate.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

* feat(errors): migrate FM taxonomy + unified error enum to v0.4.0

- Add errors.py: FailureMode enum (FM1–FM30), HummblError enum
 (14 HG_E_* runtime codes), FM_TO_ERRORS mapping, fm_to_errors()
 helper, and 14 IDP_E_* backward-compat aliases
- Add failure_modes.py: FailureModeRecord + ErrorRecord dataclasses,
 lru_cache loaders for fm.json/err.json/mappings.json, public API
 (all_failure_modes, get_fm, classify_subclass, get_errors_for_fm,
 all_error_records)
- Copy fm.json (30 FMs), err.json (3 error records), mappings.json
 (40 subclass→FM entries) from base120/registries/ into package data/
- Fix reasoning.py: replace Optional/Dict with X|None/dict (PEP 604)
- Fix delegation.py: replace bare E_* string constants with
 HummblError.*.value refs from the new unified enum
- Add 70 tests across test_errors.py + test_failure_modes.py
- Bump version 0.3.0 → 0.4.0

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

* fix(lint): move delegation.py import to top, remove unused pytest import

Fixes two ruff violations blocking CI lint gate:
- E402: `from hummbl_governance.errors import HummblError` was at line 134
 (after class definitions) — moved to module-level imports block
- F401: `import pytest` in test_errors.py was unused — removed

546 tests still pass.

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

* chore(quality): add ruff to test extras, Makefile lint target, test conventions

- pyproject.toml: add ruff>=0.4 to [test] extras so `pip install -e.[test]`
 also installs the linter; enables `make lint` locally
- Makefile: add lint + test targets (ruff check . / pytest tests/ -v)
- CONTRIBUTING.md: document test file conventions — only import pytest/stdlib
 modules when actually used; F401 fails the lint gate

Addresses AAR recommendations [HIGH] and [LOW].

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

---------

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>')

 | 

Apr 14, 2026

 |
| 

[README.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/README.md 'README.md')

 | 

[README.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/README.md 'README.md')

 | 

[feat(schema): promote evidence-readiness review receipt to governed s…](https://github.com/hummbl-dev/hummbl-governance/commit/e636089baa459963f0fe79ee5493923e785e4fb6 'feat(schema): promote evidence-readiness review receipt to governed surface (#70)

Fixes #67

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[ROADMAP.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/ROADMAP.md 'ROADMAP.md')

 | 

[ROADMAP.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/ROADMAP.md 'ROADMAP.md')

 | 

[docs: comprehensive doc accuracy sweep (test count, CI, evidence tabl…](https://github.com/hummbl-dev/hummbl-governance/commit/7c837b9163af406ce78106fec6e0faf49fa1e2ad 'docs: comprehensive doc accuracy sweep (test count, CI, evidence table, Q2 milestones)

CLAUDE.md: expand from 7-primitive stub to full v0.8.0 reference

 - 25 primitives table, 7 MCP servers table, CI section, coverage threshold

REPO_HEALTH.md: document both CI surfaces (GitHub + Gitea) accurately

 - GitHub: ubuntu-latest, Python 3.11/3.12/3.13 matrix

 - Gitea: Windows self-hosted, Python 3.13 only; PYTHON env var pattern

ROADMAP.md: 927 tests -> 1031 tests

PLAN.md: 927->1031, Q2 milestones annotated with MISSED/unknown/upcoming status

TECH-SPEC: replace premature checkmarks with unverified markers for Anthropic

 - ZDR, DPA, region, opt-out, SLA all marked UNVERIFIED per UNVERIFIED-CLAIMS.md

GITEA_MIGRATION_PLAYBOOK.md: replace broken setup-python@v5 example with working pattern

 - Use env: PYTHON + '& env:PYTHON' invocation

 - Remove invalid git remote set-head command

 - Document Windows-specific runner anti-patterns')

 | 

May 31, 2026

 |
| 

[SECURITY.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/SECURITY.md 'SECURITY.md')

 | 

[SECURITY.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/SECURITY.md 'SECURITY.md')

 | 

[fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (](https://github.com/hummbl-dev/hummbl-governance/commit/74d4479d593dded362c314be6df9e42084b01241 'fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (#69)

Fixes #64, #65

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#69](https://github.com/hummbl-dev/hummbl-governance/pull/69) [)](https://github.com/hummbl-dev/hummbl-governance/commit/74d4479d593dded362c314be6df9e42084b01241 'fix(docs): reconcile SECURITY.md and version claims for v1.1.0 (#69)

Fixes #64, #65

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 22, 2026

 |
| 

[api\_server.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/api_server.py 'api_server.py')

 | 

[api\_server.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/api_server.py 'api_server.py')

 | 

[feat: v0.3.0 — ReasoningEngine primitive + ValidationError export](https://github.com/hummbl-dev/hummbl-governance/commit/bb3a871b982daff9d9155619b9624167fabb5e8c 'feat: v0.3.0 — ReasoningEngine primitive + ValidationError export

Adds Base120 ReasoningEngine as a governance primitive, and exports
the pre-existing ValidationError from the top-level package so
downstream consumers (founder-mode) can import both validator and
error types from hummbl_governance directly.

Changes:
- hummbl_governance/reasoning.py (new, 140 LOC): Base120 mental-model
 reasoning kernel with ApplyResult dataclass and system-prompt generation
- hummbl_governance/data/base120_models.json (new, 22KB): 120-model catalog
- hummbl_governance/__init__.py: export ReasoningEngine, ApplyResult,
 ValidationError; bump __version__ to 0.3.0
- pyproject.toml: version 0.2.0 → 0.3.0
- api_server.py: wire /api/v1/apply endpoint for reasoning + kill-switch gating

All additive, backwards-compatible. 476/476 tests pass.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Apr 5, 2026

 |
| 

[arbiter\_data.db](https://github.com/hummbl-dev/hummbl-governance/blob/main/arbiter_data.db 'arbiter_data.db')

 | 

[arbiter\_data.db](https://github.com/hummbl-dev/hummbl-governance/blob/main/arbiter_data.db 'arbiter_data.db')

 | 

[fix: reduce complexity and remove dead code — D→A quality push](https://github.com/hummbl-dev/hummbl-governance/commit/d8b23a8098d76fc5bd501856aacf3336d4669d99 'fix: reduce complexity and remove dead code — D→A quality push

Refactor complex functions in MCP servers and governance modules.
Remove unused imports and variables flagged by vulture.

Score: D (61.9) → A (99.9), all tests pass.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 29, 2026

 |
| 

[governance\_cli.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/governance_cli.py 'governance_cli.py')

 | 

[governance\_cli.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/governance_cli.py 'governance_cli.py')

 | 

[fix: reduce complexity and remove dead code — D→A quality push](https://github.com/hummbl-dev/hummbl-governance/commit/d8b23a8098d76fc5bd501856aacf3336d4669d99 'fix: reduce complexity and remove dead code — D→A quality push

Refactor complex functions in MCP servers and governance modules.
Remove unused imports and variables flagged by vulture.

Score: D (61.9) → A (99.9), all tests pass.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 29, 2026

 |
| 

[hummbl.repo.yaml](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl.repo.yaml 'hummbl.repo.yaml')

 | 

[hummbl.repo.yaml](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl.repo.yaml 'hummbl.repo.yaml')

 | 

[feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (](https://github.com/hummbl-dev/hummbl-governance/commit/edb06889008d7d47695e1b79ced085e62680c439 'feat(governance): adopt HUMMBL Repo Standard v0.1 — self-compliance (#77)

The canonical standard host adopts its own standard. Adds:
- CONSTITUTION.md: 8 protected invariants (zero runtime deps, coverage
 floor, thread safety, MCP tool contract, Apache-2.0, receipt integrity,
 schema stability, canonical standard host)
- KRINEIA.md: repo-local receipt manifest
- hummbl.repo.yaml: machine-readable manifest
- CODEOWNERS: normative files require steward approval
- docs/adr/ADR-004: decision record
- _receipts/krineia/primary.jsonl: genesis receipt
- docs/handoffs/2026-06-22: handoff note

AGENTS.md unchanged.

Generated with [Devin](https://devin.ai)

Co-authored-by: Claude (agent) <238336761+hummbl-dev@users.noreply.github.com>
Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#77](https://github.com/hummbl-dev/hummbl-governance/pull/77)

 | 

Jun 22, 2026

 |
| 

[llms.txt](https://github.com/hummbl-dev/hummbl-governance/blob/main/llms.txt 'llms.txt')

 | 

[llms.txt](https://github.com/hummbl-dev/hummbl-governance/blob/main/llms.txt 'llms.txt')

 | 

[docs: add badges, hummbl.io link, and expand HUMMBL ecosystem (](https://github.com/hummbl-dev/hummbl-governance/commit/ee9e7066bec89426cf65630209bcebf1c428222b 'docs: add badges, hummbl.io link, and expand HUMMBL ecosystem (#50)

* test(governance): update version canonical expectation for v1.0.0

* docs: add llms.txt for LLM discovery

Adds AI-readable index of governance primitives, MCP servers, and compliance mappings for LLM discovery and tool selection.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* docs: add CI badge and last commit badge

Replaces Tests badge with CI workflow badge and adds last commit badge for better README visibility.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* docs: add hummbl.io link

Adds hummbl.io link to README for better discoverability.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* docs: expand HUMMBL ecosystem section with cross-repo links

Adds hummbl-agent and hummbl-bibliography to HUMMBL ecosystem section.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#50](https://github.com/hummbl-dev/hummbl-governance/pull/50) [)](https://github.com/hummbl-dev/hummbl-governance/commit/ee9e7066bec89426cf65630209bcebf1c428222b 'docs: add badges, hummbl.io link, and expand HUMMBL ecosystem (#50)

* test(governance): update version canonical expectation for v1.0.0

* docs: add llms.txt for LLM discovery

Adds AI-readable index of governance primitives, MCP servers, and compliance mappings for LLM discovery and tool selection.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* docs: add CI badge and last commit badge

Replaces Tests badge with CI workflow badge and adds last commit badge for better README visibility.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* docs: add hummbl.io link

Adds hummbl.io link to README for better discoverability.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

* docs: expand HUMMBL ecosystem section with cross-repo links

Adds hummbl-agent and hummbl-bibliography to HUMMBL ecosystem section.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>

---------

Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

Jun 14, 2026

 |
| 

[mcp\_agent\_monitor.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_agent_monitor.py 'mcp_agent_monitor.py')

 | 

[mcp\_agent\_monitor.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_agent_monitor.py 'mcp_agent_monitor.py')

 | 

[fix(lint): resolve 14 ruff errors (](https://github.com/hummbl-dev/hummbl-governance/commit/8c0037419715cc36f7ef0b2308e3a9defe7aa8fd 'fix(lint): resolve 14 ruff errors (#18)

Remove 9 unused imports (F401) and 1 redefined import (F811) across
mcp_agent_monitor.py, mcp_identity.py, and 4 test files. Add noqa: E402
to 4 intentional post-sys.path imports in test files (matching existing
pattern in test_mcp_server.py, test_mcp_sandbox.py, test_mcp_compliance.py).

CI was red for 4 days on this. All checks now pass.

Co-authored-by: opencode <opencode@anvil>') [#18](https://github.com/hummbl-dev/hummbl-governance/pull/18) [)](https://github.com/hummbl-dev/hummbl-governance/commit/8c0037419715cc36f7ef0b2308e3a9defe7aa8fd 'fix(lint): resolve 14 ruff errors (#18)

Remove 9 unused imports (F401) and 1 redefined import (F811) across
mcp_agent_monitor.py, mcp_identity.py, and 4 test files. Add noqa: E402
to 4 intentional post-sys.path imports in test files (matching existing
pattern in test_mcp_server.py, test_mcp_sandbox.py, test_mcp_compliance.py).

CI was red for 4 days on this. All checks now pass.

Co-authored-by: opencode <opencode@anvil>')

 | 

May 9, 2026

 |
| 

[mcp\_compliance.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_compliance.py 'mcp_compliance.py')

 | 

[mcp\_compliance.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_compliance.py 'mcp_compliance.py')

 | 

[fix: reduce complexity and remove dead code — D→A quality push](https://github.com/hummbl-dev/hummbl-governance/commit/d8b23a8098d76fc5bd501856aacf3336d4669d99 'fix: reduce complexity and remove dead code — D→A quality push

Refactor complex functions in MCP servers and governance modules.
Remove unused imports and variables flagged by vulture.

Score: D (61.9) → A (99.9), all tests pass.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 29, 2026

 |
| 

[mcp\_identity.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_identity.py 'mcp_identity.py')

 | 

[mcp\_identity.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_identity.py 'mcp_identity.py')

 | 

[fix(lint): resolve 14 ruff errors (](https://github.com/hummbl-dev/hummbl-governance/commit/8c0037419715cc36f7ef0b2308e3a9defe7aa8fd 'fix(lint): resolve 14 ruff errors (#18)

Remove 9 unused imports (F401) and 1 redefined import (F811) across
mcp_agent_monitor.py, mcp_identity.py, and 4 test files. Add noqa: E402
to 4 intentional post-sys.path imports in test files (matching existing
pattern in test_mcp_server.py, test_mcp_sandbox.py, test_mcp_compliance.py).

CI was red for 4 days on this. All checks now pass.

Co-authored-by: opencode <opencode@anvil>') [#18](https://github.com/hummbl-dev/hummbl-governance/pull/18) [)](https://github.com/hummbl-dev/hummbl-governance/commit/8c0037419715cc36f7ef0b2308e3a9defe7aa8fd 'fix(lint): resolve 14 ruff errors (#18)

Remove 9 unused imports (F401) and 1 redefined import (F811) across
mcp_agent_monitor.py, mcp_identity.py, and 4 test files. Add noqa: E402
to 4 intentional post-sys.path imports in test files (matching existing
pattern in test_mcp_server.py, test_mcp_sandbox.py, test_mcp_compliance.py).

CI was red for 4 days on this. All checks now pass.

Co-authored-by: opencode <opencode@anvil>')

 | 

May 9, 2026

 |
| 

[mcp\_physical.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_physical.py 'mcp_physical.py')

 | 

[mcp\_physical.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_physical.py 'mcp_physical.py')

 | 

[feat: v0.8.0 — four new MCP servers (identity, agent-monitor, reasoni…](https://github.com/hummbl-dev/hummbl-governance/commit/365ff8f89cec033783f20a39ae13f304178810ba 'feat: v0.8.0 — four new MCP servers (identity, agent-monitor, reasoning, physical)

Exposes 15 previously unexposed governance primitives as 32 JSON-RPC tools
via four new stdio MCP servers:

- mcp_identity.py (10 tools): AgentRegistry, DelegationTokenManager, LamportClock
- mcp_agent_monitor.py (11 tools): BehaviorMonitor, ConvergenceDetector, GovernanceLifecycle, EvolutionLineage
- mcp_reasoning.py: ReasoningEngine, SchemaValidator, ContractNetManager
- mcp_physical.py (6 tools): KinematicGovernor, pHRISafetyMonitor

Adds 4 console_scripts: hummbl-identity-mcp, hummbl-agent-monitor-mcp,
hummbl-reasoning-mcp, hummbl-physical-mcp.

143 new tests; total suite: 784 → 927 (all passing).
Total MCP servers: 3 → 7.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

May 4, 2026

 |
| 

[mcp\_reasoning.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_reasoning.py 'mcp_reasoning.py')

 | 

[mcp\_reasoning.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_reasoning.py 'mcp_reasoning.py')

 | 

[feat: v0.8.0 — four new MCP servers (identity, agent-monitor, reasoni…](https://github.com/hummbl-dev/hummbl-governance/commit/365ff8f89cec033783f20a39ae13f304178810ba 'feat: v0.8.0 — four new MCP servers (identity, agent-monitor, reasoning, physical)

Exposes 15 previously unexposed governance primitives as 32 JSON-RPC tools
via four new stdio MCP servers:

- mcp_identity.py (10 tools): AgentRegistry, DelegationTokenManager, LamportClock
- mcp_agent_monitor.py (11 tools): BehaviorMonitor, ConvergenceDetector, GovernanceLifecycle, EvolutionLineage
- mcp_reasoning.py: ReasoningEngine, SchemaValidator, ContractNetManager
- mcp_physical.py (6 tools): KinematicGovernor, pHRISafetyMonitor

Adds 4 console_scripts: hummbl-identity-mcp, hummbl-agent-monitor-mcp,
hummbl-reasoning-mcp, hummbl-physical-mcp.

143 new tests; total suite: 784 → 927 (all passing).
Total MCP servers: 3 → 7.

Generated with [Devin](https://cli.devin.ai/docs)

Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')

 | 

May 4, 2026

 |
| 

[mcp\_sandbox.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_sandbox.py 'mcp_sandbox.py')

 | 

[mcp\_sandbox.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_sandbox.py 'mcp_sandbox.py')

 | 

[fix: reduce complexity and remove dead code — D→A quality push](https://github.com/hummbl-dev/hummbl-governance/commit/d8b23a8098d76fc5bd501856aacf3336d4669d99 'fix: reduce complexity and remove dead code — D→A quality push

Refactor complex functions in MCP servers and governance modules.
Remove unused imports and variables flagged by vulture.

Score: D (61.9) → A (99.9), all tests pass.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 29, 2026

 |
| 

[mcp\_server.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_server.py 'mcp_server.py')

 | 

[mcp\_server.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/mcp_server.py 'mcp_server.py')

 | 

[fix: reduce complexity and remove dead code — D→A quality push](https://github.com/hummbl-dev/hummbl-governance/commit/d8b23a8098d76fc5bd501856aacf3336d4669d99 'fix: reduce complexity and remove dead code — D→A quality push

Refactor complex functions in MCP servers and governance modules.
Remove unused imports and variables flagged by vulture.

Score: D (61.9) → A (99.9), all tests pass.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>')

 | 

Mar 29, 2026

 |
| 

[package.json](https://github.com/hummbl-dev/hummbl-governance/blob/main/package.json 'package.json')

 | 

[package.json](https://github.com/hummbl-dev/hummbl-governance/blob/main/package.json 'package.json')

 | 

[feat(viz): add governance timeline graph with watch mode (](https://github.com/hummbl-dev/hummbl-governance/commit/26a35af7843237ebfe186054998064b5d3f9d83a 'feat(viz): add governance timeline graph with watch mode (#10)

scripts/governance-timeline.js: D3 swimlane timeline for governance JSONL
- Rows = intent sessions (most recent 50), X = time axis
- Dots colored by tuple_type (DCT/DCTX/CONTRACT/EVIDENCE/ATTEST/SYSTEM)
- Click row → detail panel (events by type, timestamps, contracts)
- Filter bar (intent_id, task_id, adapter, event search)
- Zoom controls: Fit All / Last 24h / Last 7d
- Legend with per-type toggle (hide/show)
- Watch mode: --watch flag, 500ms debounce on .jsonl changes
- 22,313 entries / 50 sessions tested against founder-mode governance data
- Self-contained HTML (~2MB, D3 inlined); reports/*.html gitignored
- package.json scripts: governance-timeline, governance-timeline:watch

Co-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>') [#10](https://github.com/hummbl-dev/hummbl-governance/pull/10) [)](https://github.com/hummbl-dev/hummbl-governance/commit/26a35af7843237ebfe186054998064b5d3f9d83a 'feat(viz): add governance timeline graph with watch mode (#10)

scripts/governance-timeline.js: D3 swimlane timeline for governance JSONL
- Rows = intent sessions (most recent 50), X = time axis
- Dots colored by tuple_type (DCT/DCTX/CONTRACT/EVIDENCE/ATTEST/SYSTEM)
- Click row → detail panel (events by type, timestamps, contracts)
- Filter bar (intent_id, task_id, adapter, event search)
- Zoom controls: Fit All / Last 24h / Last 7d
- Legend with per-type toggle (hide/show)
- Watch mode: --watch flag, 500ms debounce on .jsonl changes
- 22,313 entries / 50 sessions tested against founder-mode governance data
- Self-contained HTML (~2MB, D3 inlined); reports/*.html gitignored
- package.json scripts: governance-timeline, governance-timeline:watch

Co-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>')

 | 

Apr 14, 2026

 |
| 

[post\_to\_bus.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/post_to_bus.py 'post_to_bus.py')

 | 

[post\_to\_bus.py](https://github.com/hummbl-dev/hummbl-governance/blob/main/post_to_bus.py 'post_to_bus.py')

 | 

[Feat/gemini/v0.4.0 hardening (](https://github.com/hummbl-dev/hummbl-governance/commit/f63e22904d58d47b65b70d36379a352671c74361 'Feat/gemini/v0.4.0 hardening (#16)

* feat: release hummbl-governance v0.4.0

- Add physical_governor.py (pHRI safety monitor, kinematic governor)\n- Integrate Arbiter code quality checks into eal.py validation\n- Expand ReasoningEngine with systems and recursive models\n- Add comprehensive test coverage for ReasoningEngine (L2 resolution)\n- Add init smoke tests for export validation (L3 resolution)\n- Update AUDIT.md with v0.4.0 metrics

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* docs: formalize project roadmap

- Add ROADMAP.md aligned with RIF v6.0\n- Link to roadmap in CONTRIBUTING.md

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* ci: integrate Arbiter governance audit gate

- Add arbiter-governance job to CI\n- Enforce minimum governance score of 90/100

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden LamportClock for causal integrity

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Update tests and __init__.py for v0.5.0 release

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden CoordinationBus and LamportClock

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Add post_to_bus.py script for bus interaction

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* fix: repair PR 16 CI gates

---------

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude (agent) <claude@agents.hummbl.io>') [#16](https://github.com/hummbl-dev/hummbl-governance/pull/16) [)](https://github.com/hummbl-dev/hummbl-governance/commit/f63e22904d58d47b65b70d36379a352671c74361 'Feat/gemini/v0.4.0 hardening (#16)

* feat: release hummbl-governance v0.4.0

- Add physical_governor.py (pHRI safety monitor, kinematic governor)\n- Integrate Arbiter code quality checks into eal.py validation\n- Expand ReasoningEngine with systems and recursive models\n- Add comprehensive test coverage for ReasoningEngine (L2 resolution)\n- Add init smoke tests for export validation (L3 resolution)\n- Update AUDIT.md with v0.4.0 metrics

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* docs: formalize project roadmap

- Add ROADMAP.md aligned with RIF v6.0\n- Link to roadmap in CONTRIBUTING.md

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* ci: integrate Arbiter governance audit gate

- Add arbiter-governance job to CI\n- Enforce minimum governance score of 90/100

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden LamportClock for causal integrity

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Update tests and __init__.py for v0.5.0 release

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* feat(v0.5.0): harden CoordinationBus and LamportClock

- Add Delta Cap to LamportClock to prevent forward-jump attacks\n- Introduce LamportTimestamp named tuple for type safety\n- Add post_to_bus.py script for bus interaction

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>

* fix: repair PR 16 CI gates

---------

Signed-off-by: Claude (agent) <claude@agents.hummbl.io>
Co-authored-by: Claude (agent) <claude@agents.hummbl.io>')

 | 

Apr 19, 2026

 |
| 

[pyproject.toml](https://github.com/hummbl-dev/hummbl-governance/blob/main/pyproject.toml 'pyproject.toml')

 | 

[pyproject.toml](https://github.com/hummbl-dev/hummbl-governance/blob/main/pyproject.toml 'pyproject.toml')

 | 

[fix(kernel): stabilize governance v1.2.0 health gates (](https://github.com/hummbl-dev/hummbl-governance/commit/4abc2fb18df9c04c78a2b55b4bf8fe585e2b8cc1 'fix(kernel): stabilize governance v1.2.0 health gates (#58)

* fix(kernel): stabilize governance v1.2.0 health gates

Align package metadata with v1.2.0, update law-atlas expectations, keep model registry writes out of package source, remove private registry placeholders, and serialize receipt file access.

Also clears Ruff findings across duplicated kernel test suites so mainline quality gates can run cleanly.

* ci(coverage): omit packaged kernel tests

Keep package-side duplicated test modules out of source coverage accounting so the CI coverage gate measures runtime modules instead of uncollected tests.') [#58](https://github.com/hummbl-dev/hummbl-governance/pull/58) [)](https://github.com/hummbl-dev/hummbl-governance/commit/4abc2fb18df9c04c78a2b55b4bf8fe585e2b8cc1 'fix(kernel): stabilize governance v1.2.0 health gates (#58)

* fix(kernel): stabilize governance v1.2.0 health gates

Align package metadata with v1.2.0, update law-atlas expectations, keep model registry writes out of package source, remove private registry placeholders, and serialize receipt file access.

Also clears Ruff findings across duplicated kernel test suites so mainline quality gates can run cleanly.

* ci(coverage): omit packaged kernel tests

Keep package-side duplicated test modules out of source coverage accounting so the CI coverage gate measures runtime modules instead of uncollected tests.')

 | 

Jun 20, 2026

 |
| 

View all files

 |

## Repository files navigation

# hummbl-governance

[![PyPI](https://camo.githubusercontent.com/16d2504199ee3ef1a17032d6efb0a0d2efb788c7cd75dbbb594286bb68bd939e/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f68756d6d626c2d676f7665726e616e6365)](https://pypi.org/project/hummbl-governance/) [![Python](https://camo.githubusercontent.com/ee73232beb34105ca251f39a141bbc41d7ae3c3e8560a1c9c11ed81b5d5922b4/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f68756d6d626c2d676f7665726e616e6365)](https://pypi.org/project/hummbl-governance/) [![Tests](https://camo.githubusercontent.com/8e31377b8ff85ee9712211b90a1a62ef5ff9d376e97a5fed6e58c18ef1f929d6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f74657374732d3131363825323070617373696e672d627269676874677265656e)](https://github.com/hummbl-dev/hummbl-governance/blob/main) [![License](https://camo.githubusercontent.com/39a434c39c97856247fc55ebc90e8cc1cb9871558a37bf1bf83cbaca3be89d69/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d417061636865253230322e302d626c7565)](https://github.com/hummbl-dev/hummbl-governance/blob/main/LICENSE) [![Dependencies](https://camo.githubusercontent.com/aae95fbaa83bc6a3f4597f3a75da45ea46ec236fc324617f0e5a2f15e07fe750/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646570656e64656e636965732d302d627269676874677265656e)](https://github.com/hummbl-dev/hummbl-governance/blob/main) [![Last commit](https://camo.githubusercontent.com/fb9ae7041e2df8311cf82f43cf227549f7f8437d72fc5e372c85ed64aed7897f/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f68756d6d626c2d6465762f68756d6d626c2d676f7665726e616e63652f6d61696e)](https://github.com/hummbl-dev/hummbl-governance/commits/main)

**hummbl-governance** is a Python library that provides 26 governance primitives for AI agent orchestration, including a governance Kernel (receipts, identity, roles, laws, evidence), kill switch, circuit breaker, cost governor, delegation tokens, reasoning engine, execution assurance, physical-AI safety, and audit logging. It has zero third-party dependencies (stdlib only), 1168 passing tests, and supports Python 3.11 through 3.14.

Learn more at [hummbl.io](https://hummbl.io).

Repository health, validation, and stewardship expectations are tracked in [docs/REPO\_HEALTH.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/docs/REPO_HEALTH.md).

Evidence-readiness review receipt mapping for HUMMBL Legal/Paralegal packet work is tracked in [docs/evidence-readiness-review-receipt.md](https://github.com/hummbl-dev/hummbl-governance/blob/main/docs/evidence-readiness-review-receipt.md), with the governed JSON schema (v1) at [`hummbl_governance/data/evidence_readiness_review_receipt.schema.json`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/data/evidence_readiness_review_receipt.schema.json) (`$id: ...evidence-readiness-review-receipt.v1.json`). The schema is the governed decision surface for evidence-readiness reviews: it records reviewer, date, artifact (packet paths + source manifest hash), verdict, evidence references, claim-honesty checks, and the relay decision.

```shell
pip install hummbl-governance
```

**Or with [uv](https://docs.astral.sh/uv/)** (10-100x faster, 30-43% of new repos use it):

```shell
uv pip install hummbl-governance
```

[![Tested on](https://camo.githubusercontent.com/e21f51b649c8dd5a3075be5a410db3e0a6f6a48bcdc7e1e855a5ec793156b972/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5465737465642532306f6e2d5562756e747525323032342e30342532302543322542372532306d61634f532532304d2d2d73657269657325323025433225423725323057696e646f7773253230313125323025324225323057534c322d626c7565)](https://github.com/hummbl-dev/hummbl-governance/blob/main) [![Architecture](https://camo.githubusercontent.com/9dffd0f0b6c9e9bdb3dd9990c8645a52984709ba4099f4f5fbe802dc8cfceae9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4172636869746563747572652d7838365f5f363425323025374325323041524d36342d627269676874677265656e)](https://github.com/hummbl-dev/hummbl-governance/blob/main)

## Quick Start -- 5 Minutes

Run a complete governance example in 60 seconds:

```shell
pip install hummbl-governance
python -c "
from hummbl_governance import KillSwitch, KillSwitchMode
ks = KillSwitch()
ks.engage(KillSwitchMode.HALT_NONCRITICAL, reason='Demo', triggered_by='user')
print(ks.check_task_allowed('critical_task'))
"
```

Explore all 26 primitives:

```shell
git clone https://github.com/hummbl-dev/hummbl-governance.git
cd hummbl-governance
python examples/kill_switch_modes.py
python examples/circuit_breaker_wrap.py
python examples/cost_governor.py
```

## Architecture

Loading

**Unable to render rich display**

Could not find a suitable point for the given distance 
 
For more information, see https://docs.github.com/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams 

graph TD
 A\[Agent Action\] --> B{KillSwitch}
 B -->|ALLOWED| C{CircuitBreaker}
 C -->|CLOSED| D\[External API\]
 C -->|OPEN| E\[Fast Fail\]
 D --> F{CostGovernor}
 F -->|UNDER BUDGET| G\[Execute\]
 F -->|OVER BUDGET| H\[Block + Audit\]
 G --> I\[AuditLog\]
 H --> I
 I --> J\[ComplianceMapper\]
 J --> K\[SOC2 / GDPR / NIST Report\]

## What's New in v1.1.0

- **Governance Kernel** — the 26th primitive. A minimal, stdlib-only substrate for AI fleet governance: signed receipts, identity registry, role claims, sequence enforcement, evidence grading, authority scoping, schedule tracking, and scaling-law evaluation against the HUMMBL Scaling Law Atlas (17 empirically-tested laws).
 - 12 runtime modules, 10 test files, 136 tests (adversarial, chaos, edge cases, fuzzing, integration, invariants, law atlas, performance, properties, race recovery)
 - Full CLI: `python -m hummbl_governance.kernel boot|status|health|inspect|laws|roles`
 - Portable paths via `HUMMBL_KERNEL_STATE_DIR` and `HUMMBL_KERNEL_ATLAS_DIR`
- **1 new test** — `test_kernel_primitives_exported()` verifying all 11 Kernel symbols in `__all__`
- **1032 total tests** (1031 → 1032)

### v0.8.0 highlights

- **Four new MCP servers** — expose 15 previously unexposed governance primitives as 32 JSON-RPC tools. Zero additional dependencies.
 - `mcp_identity.py` — 10 tools: `identity_register`, `identity_lookup`, `identity_list`, `identity_validate`, `delegation_create`, `delegation_validate`, `delegation_check_op`, `clock_tick`, `clock_receive`, `clock_compare` (wraps `AgentRegistry`, `DelegationTokenManager`, `LamportClock`)
 - `mcp_agent_monitor.py` — 11 tools: `behavior_record`, `behavior_snapshot_baseline`, `behavior_detect_drift`, `convergence_record`, `convergence_check`, `convergence_scores`, `lifecycle_authorize`, `lifecycle_status`, `lineage_record_variant`, `lineage_get`, `lineage_drift` (wraps `BehaviorMonitor`, `ConvergenceDetector`, `GovernanceLifecycle`, `EvolutionLineage`)
 - `mcp_reasoning.py` — reasoning, schema, and contract-net tools (wraps `ReasoningEngine`, `SchemaValidator`, `ContractNetManager`)
 - `mcp_physical.py` — 6 tools: `kinematic_check_motion`, `kinematic_get_limits`, `kinematic_scaled_velocity`, `phri_check_safety`, `phri_get_config`, `phri_batch_check` (wraps `KinematicGovernor`, `pHRISafetyMonitor`)
- **4 new CLI entry points**: `hummbl-identity-mcp`, `hummbl-agent-monitor-mcp`, `hummbl-reasoning-mcp`, `hummbl-physical-mcp`
- **143 new tests** — 927 total (784 → 927)

### v0.7.0 highlights

- **Three MCP servers** -- expose all governance primitives as Model Context Protocol tools via stdio JSON-RPC. Zero additional dependencies.
 - `mcp_server.py` -- 10 tools: `governance_status`, `kill_switch_status/engage/disengage`, `circuit_breaker_status`, `cost_budget_check/record_usage`, `audit_query`, `compliance_report`, `health_check`
 - `mcp_compliance.py` -- 5 tools: `nist_map_controls`, `soc2_assess`, `iso_crosswalk`, `stride_analysis`, `compliance_evidence_export`
 - `mcp_sandbox.py` -- 5 tools: `sandbox_create/check/validate_output/status/destroy`
- **84 new tests** covering all MCP tool handlers and protocol-level JSON-RPC round-trips (30 + 25 + 29)
- **784 total tests** (700 → 784)

### v0.6.0 highlights

- **NIST AI RMF report** (`generate_nist_rmf_report()`) -- Maps governance traces to the four core functions: GOVERN, MAP, MEASURE, MANAGE. Evidence-backed controls aligned to NIST AI 100-1 (2023).
- **EU AI Act report** (`generate_eu_ai_act_report()`) -- Maps governance traces to Articles 9, 10, 12, 13, 14, 17 for High-Risk AI (Annex III). Includes `human_initiated` flag on KILLSWITCH events for Art.14 human oversight evidence.
- **CHANGELOG.md** -- full version history from v0.1.0.
- **673 tests** -- 36 new tests covering all NIST RMF and EU AI Act mappings.

### v0.5.0 highlights

- **LamportClock hardening** -- causal integrity checks for distributed audit logs; epoch-aware state handling across agents.
- **EvolutionLineage** -- in-memory lineage tracking for eAI variants; `VariantRecord`, `ModificationRecord`, `EvolutionDriftReport`.
- **FailureModes catalog** -- structured `FailureModeRecord` and `ErrorRecord` taxonomy; `all_failure_modes()`, `classify_subclass()`, `get_errors_for_fm()`.
- **Errors taxonomy** -- `HummblError`, `FailureMode`, `fm_to_errors()` as top-level exports.

### v0.4.0 highlights

- **KinematicGovernor** -- deterministic motion constraints (velocity, force, jerk) for physical-AI safety.
- **pHRISafetyMonitor** -- graduated pHRI safety modes (NORMAL/CAUTION/EMERGENCY).
- **Execution Assurance Layer (EAL)** -- Arbiter-verified code quality in execution receipts (`E_CODE_QUALITY_FAIL`).
- **ReasoningEngine** -- structured governance reasoning with rule application, conflict detection, and decision tracing.
- **ValidationError** -- top-level export from `hummbl_governance`.

## Usage Example

```python
from hummbl_governance import KillSwitch, KillSwitchMode, CircuitBreaker, CostGovernor

ks = KillSwitch()
ks.engage(KillSwitchMode.HALT_ALL, reason="Budget exceeded", triggered_by="cost_governor")
print(ks.check_task_allowed("data_export"))  # {"allowed": False, ...}

cb = CircuitBreaker(failure_threshold=3, recovery_timeout=10.0)
result = cb.call(my_function, arg1, arg2)  # Opens after 3 failures

gov = CostGovernor(":memory:", soft_cap=50.0, hard_cap=100.0)
gov.record_usage(provider="anthropic", model="claude-4", tokens_in=1000, tokens_out=500, cost=0.015)
status = gov.check_budget_status()  # status.decision in ("ALLOW", "WARN", "DENY")
```

## Features

- **26 governance primitives** covering safety, cost, identity, compliance, reasoning, coordination, physical-AI, execution assurance, and governance Kernel
- **1168 tests** with full coverage across all modules
- **Zero dependencies** -- Python stdlib only, no pip conflicts
- **Thread-safe** -- all modules use appropriate locking primitives
- **Independently importable** -- use only the modules you need
- **Python 3.11 - 3.13** CI-tested. 3.14 tracked.

## All 26 Primitives

| Module | Description |
| --- | --- |
| `kernel` | Governance operating system — receipts, identity, roles, laws, evidence, sequence, authority, schedule |
| `kill_switch` | Emergency halt system with 4 graduated modes (DISENGAGED, HALT\_NONCRITICAL, HALT\_ALL, EMERGENCY) |
| `circuit_breaker` | Automatic failure detection and recovery across 3 states (CLOSED, HALF\_OPEN, OPEN) |
| `cost_governor` | Budget tracking with soft/hard caps and ALLOW/WARN/DENY decisions |
| `delegation` | HMAC-SHA256 signed capability tokens for agent delegation chains |
| `audit_log` | Append-only JSONL governance audit log with rotation and retention |
| `identity` | Agent registry with configurable aliases, trust tiers, and canonicalization |
| `schema_validator` | Stdlib-only JSON Schema validator (Draft 2020-12 subset) with top-level `ValidationError` export |
| `coordination_bus` | Append-only TSV message bus with flock locking and HMAC signing |
| `compliance_mapper` | Map governance traces to SOC2, GDPR, and OWASP controls |
| `health_probe` | Composable health probe framework with latency tracking |
| `output_validator` | Rule-based content validation for agent outputs (PII detection, injection detection, blocklists) |
| `capability_fence` | Soft sandbox enforcing capability boundaries per agent role |
| `stride_mapper` | Map agent interactions to STRIDE threat categories with mitigation suggestions |
| `lifecycle` | NIST AI RMF orchestrator composing kill switch, circuit breaker, cost governor, and audit log |
| `contract_net` | Market-based task allocation protocol for multi-agent systems |
| `convergence_guard` | Detect instrumental convergence patterns in agent behavior |
| `reward_monitor` | Behavioral drift and reward gaming detector |
| `lamport_clock` | Hardened logical clock for causal ordering of distributed agent events (v0.5.0) |
| `reasoning` | Structured governance reasoning engine with rule application, conflict detection, and decision tracing |
| `eal` | Execution Assurance Layer -- Arbiter-verified code quality in execution receipts |
| `physical_governor` | Kinematic constraints and pHRI safety modes for physical-AI deployments |
| `errors` | `HummblError`, `FailureMode`, and `fm_to_errors()` -- typed error taxonomy |
| `failure_modes` | Structured failure mode catalog with classification and error cross-reference |
| `evolution_lineage` | In-memory lineage tracking for eAI variants with drift detection |
| `ValidationError` | Top-level exception for schema validation failures (exported from `schema_validator`) |

## 26 Runnable Examples

Every primitive has a standalone example in `examples/`. Each runs with just `python examples/<name>.py` -- no setup, no config.

| Example | Primitive | What it shows |
| --- | --- | --- |
| `kill_switch_modes.py` | KillSwitch | 4 graduated halt modes |
| `circuit_breaker_wrap.py` | CircuitBreaker | 3-state failure recovery |
| `cost_governor.py` | CostGovernor | Soft/hard budget caps |
| `delegate_task.py` | DelegationToken | HMAC-signed agent delegation |
| `audit_log.py` | AuditLog | Append-only governance log |
| `agent_registry.py` | AgentRegistry | Identity + trust tiers |
| `schema_validator.py` | SchemaValidator | Stdlib JSON Schema validation |
| `compliance_mapper.py` | ComplianceMapper | SOC2/GDPR evidence mapping |
| `health_probe.py` | HealthProbe | Composable health checks |
| `output_validator.py` | OutputValidator | Content safety filtering |
| `capability_fence.py` | CapabilityFence | Role-based capability boundaries |
| `stride_mapper.py` | StrideMapper | STRIDE threat analysis |
| `lifecycle.py` | GovernanceLifecycle | NIST AI RMF orchestration |
| `contract_net.py` | ContractNetManager | Multi-agent task allocation |
| `convergence_guard.py` | ConvergenceGuard | Instrumental convergence detection |
| `behavior_monitor.py` | BehaviorMonitor | Behavioral drift detection |
| `lamport_clock.py` | LamportClock | Distributed causal ordering |
| `reasoning.py` | ReasoningEngine | Structured governance reasoning |
| `eal.py` | EAL | Execution assurance |
| `physical_governor.py` | KinematicGovernor | Physical-AI safety limits |
| `errors.py` | HummblError | Typed error taxonomy |
| `failure_modes.py` | FailureMode | Failure classification |
| `evolution_lineage.py` | EvolutionLineage | eAI variant lineage tracking |
| `agent_runner.py` | \-- | End-to-end agent with governance stack |
| `failure_injection.py` | \-- | Chaos testing with kill switch + circuit breaker |

Run them all:

```shell
for f in examples/*.py; do echo "=== $f ==="; python "$f"; done
```

## Why hummbl-governance?

**No dependency conflicts.** hummbl-governance uses only Python stdlib. It installs in under 1 second and never conflicts with your existing packages. Every governance module is independently importable -- use `KillSwitch` without pulling in `CostGovernor`.

**Built for multi-agent systems.** The library provides primitives that AI orchestration platforms actually need: delegation tokens with HMAC-SHA256 signing, a coordination bus with mutual exclusion, kill switch with 4 graduated halt modes, and circuit breakers wrapping external adapters.

**Compliance-aware by design.** The `compliance_mapper` maps governance events to SOC2, GDPR, and OWASP controls. The `stride_mapper` produces STRIDE threat analysis for agent interactions. These modules generate audit evidence, not just runtime safety.

**Production-tested.** The governance primitives were extracted from [founder-mode](https://github.com/hummbl-dev/founder-mode), a multi-runtime AI orchestration platform with 15,600+ tests and 14 CI workflows across its full surface. The governance layer extracted here has 1168 dedicated tests and runs daily in production.

## hummbl-governance vs Alternatives

| Capability | hummbl-governance | Raw stdlib | LangChain Guardrails | CrewAI Guardrails |
| --- | :-: | :-: | :-: | :-: |
| Zero dependencies | Yes | Yes | No (requires langchain) | No (requires crewai) |
| Kill switch (graduated modes) | 4 modes | DIY | No | No |
| Circuit breaker | 3 states | DIY | No | No |
| Cost governance (budget caps) | Soft + hard caps | DIY | No | No |
| Delegation tokens (HMAC signed) | Yes | DIY | No | No |
| Append-only audit log | Yes | DIY | Partial | No |
| Agent identity registry | Yes | DIY | No | No |
| STRIDE threat mapping | Yes | No | No | No |
| SOC2/GDPR/OWASP compliance mapping | Yes | No | No | No |
| JSON Schema validation (stdlib) | Draft 2020-12 | No | Requires jsonschema | Requires pydantic |
| Governance reasoning engine | Yes | No | No | No |
| Thread-safe | Yes | Varies | Varies | Varies |
| Modules work standalone | Yes | N/A | No (framework lock-in) | No (framework lock-in) |

## OWASP Top 10 for Agentic Applications (2026) Coverage

hummbl-governance addresses all 10 risks in the [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/). Every row below links to the primitive and its test suite.

| OWASP Risk | Primitive(s) | Tests | How |
| --- | --- | --- | --- |
| **ASI01** Agent Goal Hijack | [`KillSwitch`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/kill_switch.py) | [27](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_kill_switch.py) | 4-mode graduated shutdown (DISENGAGED → EMERGENCY). Survives process restart. Stops hijacked agents mid-execution. |
| **ASI02** Tool Misuse | [`CapabilityFence`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/capability_fence.py) | [27](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_capability_fence.py) | Allowlist/blocklist enforcement per tool. Agents cannot invoke tools outside their granted capabilities. |
| **ASI03** Identity & Privilege Abuse | [`DelegationTokenManager`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/delegation.py), [`AgentRegistry`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/identity.py) | [16](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_delegation.py) + [26](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_identity.py) | HMAC-signed scoped tokens with chain-depth limits. Identity registry with trust tiers and alias canonicalization. |
| **ASI04** Supply Chain | Zero dependencies | — | Stdlib-only. No transitive dependencies to compromise. `pip audit` finds nothing because there is nothing to audit. |
| **ASI05** Unexpected Code Execution | [`OutputValidator`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/output_validator.py), [`InjectionDetector`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/output_validator.py) | [49](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_output_validator.py) | Prompt injection detection, blocked-term filtering, and content validation before agent output reaches downstream systems. |
| **ASI06** Memory & Context Poisoning | [`BusWriter`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/coordination_bus.py), [`AuditLog`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/audit_log.py) | [63](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_coordination_bus.py) + [17](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_audit_log.py) | Append-only governance bus with content hashing. Tamper-evident audit log. Poisoned entries are detectable. |
| **ASI07** Insecure Inter-Agent Comms | [`LamportClock`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/lamport_clock.py), [`ContractNetManager`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/contract_net.py) | [20](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_lamport_clock.py) + [19](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_contract_net.py) | Hardened logical clocks for causal ordering. Contract Net protocol for structured multi-agent task allocation with bid verification. |
| **ASI08** Cascading Failures | [`CircuitBreaker`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/circuit_breaker.py), [`HealthProbe`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/health_probe.py) | [17](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_circuit_breaker.py) + [30](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_health_probe.py) | CLOSED/HALF\_OPEN/OPEN state machine isolates failing components. Health probes detect degradation before cascade. |
| **ASI09** Human-Agent Trust Exploitation | [`ReasoningEngine`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/reasoning.py), [`ComplianceMapper`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/compliance_mapper.py) | [7](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_explain.py) + [34](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_compliance_mapper.py) | Structured decision traces explain _why_ a governance decision was made. Compliance mapping to NIST/ISO provides external validation anchor. |
| **ASI10** Rogue Agents | [`BehaviorMonitor`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/reward_monitor.py), [`GovernanceLifecycle`](https://github.com/hummbl-dev/hummbl-governance/blob/main/hummbl_governance/lifecycle.py) | [20](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_reward_monitor.py) + [17](https://github.com/hummbl-dev/hummbl-governance/blob/main/tests/test_lifecycle.py) | Jensen-Shannon divergence detects behavioral drift from baseline. Lifecycle FSM enforces PROVISIONED → ACTIVE → SUSPENDED → DECOMMISSIONED transitions. |

**Total: 1168 tests across 26 primitives + 7 MCP servers. 10/10 OWASP coverage. Zero dependencies.**

For the formal governance primitive underlying all 10 mitigations, see [The Governance Tuple](https://doi.org/10.5281/zenodo.19646940) (Bowlby, 2026).

## Research

The evidence base behind hummbl-governance is documented in the [AI Slop Crisis](https://github.com/hummbl-dev/hummbl-dev/tree/main/docs/research/ai-slop-crisis) research corpus:

- [Why Libraries, Not Platforms](https://github.com/hummbl-dev/hummbl-dev/tree/main/docs/research/ai-slop-crisis#why-libraries-not-platforms) -- the architectural thesis behind stdlib-only, independently importable governance primitives
- [Vendor Comparison Table](https://github.com/hummbl-dev/hummbl-dev/tree/main/docs/research/ai-slop-crisis#vendor-comparison) -- how hummbl-governance compares to platform-locked alternatives across dependency count, modularity, and compliance coverage

## Newsletter

Subscribe to the **HUMMBL Slop Tracker** for monthly AI governance intelligence: [hummbl.substack.com](https://hummbl.substack.com)

Read [Issue #1](https://hummbl.substack.com/p/issue-1) for the inaugural edition.

## FAQ

### How do I add a kill switch to my AI agent system?

Install hummbl-governance and use the `KillSwitch` class. It provides 4 graduated modes: `DISENGAGED` (normal operation), `HALT_NONCRITICAL` (stop non-essential tasks), `HALT_ALL` (stop everything except monitoring), and `EMERGENCY` (immediate full shutdown). Call `ks.check_task_allowed("task_name")` before each agent action.

```python
from hummbl_governance import KillSwitch, KillSwitchMode
ks = KillSwitch()
ks.engage(KillSwitchMode.HALT_NONCRITICAL, reason="High error rate", triggered_by="monitor")
```

### How do I track AI API costs and enforce budget limits?

Use `CostGovernor` with soft and hard caps. Record each API call with `record_usage()`, then call `check_budget_status()` to get an ALLOW, WARN, or DENY decision. The soft cap triggers warnings; the hard cap blocks further spending.

```python
from hummbl_governance import CostGovernor
gov = CostGovernor(":memory:", soft_cap=50.0, hard_cap=100.0)
gov.record_usage(provider="openai", model="gpt-4", tokens_in=500, tokens_out=200, cost=0.02)
```

### How do I implement delegation tokens for multi-agent AI systems?

Use `DelegationTokenManager` to create HMAC-SHA256 signed tokens that grant specific operations to specific agents. Tokens are scoped by issuer, subject, allowed operations, and an optional binding to a task and contract. Validate tokens before executing delegated actions.

```python
from hummbl_governance import DelegationTokenManager
from hummbl_governance.delegation import TokenBinding
mgr = DelegationTokenManager(secret=b"shared-secret")
token = mgr.create_token(issuer="orchestrator", subject="worker", ops_allowed=["read", "write"],
                         binding=TokenBinding("task-1", "contract-1"))
valid, error = mgr.validate_token(token)
```

### Does hummbl-governance work without any third-party packages?

Yes. Every module uses only Python stdlib (3.11+). There are zero entries in the `dependencies` list in `pyproject.toml`. Test dependencies (pytest) are isolated in `[test]` extras. This means no dependency conflicts, no supply chain risk from transitive dependencies, and fast installs.

### How do I generate compliance evidence for SOC2 or GDPR from my AI system?

Use `ComplianceMapper` to map governance audit log entries to compliance framework controls. Pass your `AuditLog` entries through the mapper to produce a `ComplianceReport` that links each governance event to the relevant SOC2, GDPR, or OWASP control. Use `StrideMapper` for threat-level analysis of agent interactions.

```python
from hummbl_governance import ComplianceMapper, AuditLog
mapper = ComplianceMapper()
report = mapper.map_events(audit_entries)  # Returns ComplianceReport with control mappings
```

## Extended Quick Start

```python
from hummbl_governance import (
    KillSwitch, KillSwitchMode,
    CircuitBreaker,
    CostGovernor,
    DelegationToken, DelegationTokenManager,
    AuditLog,
    AgentRegistry,
    SchemaValidator,
)

# Kill Switch
ks = KillSwitch()
ks.engage(KillSwitchMode.HALT_ALL, reason="Budget exceeded", triggered_by="cost_governor")
result = ks.check_task_allowed("data_export")
# result["allowed"] == False

# Circuit Breaker
cb = CircuitBreaker(failure_threshold=3, recovery_timeout=10.0)
result = cb.call(some_function, arg1, arg2)

# Cost Governor
gov = CostGovernor(":memory:", soft_cap=50.0, hard_cap=100.0)
gov.record_usage(provider="anthropic", model="claude-4", tokens_in=1000, tokens_out=500, cost=0.015)
status = gov.check_budget_status()
# status.decision in ("ALLOW", "WARN", "DENY")

# Delegation Tokens
mgr = DelegationTokenManager(secret=b"my-secret")
from hummbl_governance.delegation import TokenBinding
token = mgr.create_token(
    issuer="orchestrator", subject="worker",
    ops_allowed=["read"], binding=TokenBinding("task-1", "contract-1"),
)
valid, error = mgr.validate_token(token)

# Agent Registry
registry = AgentRegistry()
registry.register_agent("orchestrator", trust="high")
registry.add_alias("orch-1", "orchestrator")
registry.canonicalize("orch-1")  # -> "orchestrator"
```

## MCP Servers

hummbl-governance ships three [Model Context Protocol](https://modelcontextprotocol.io/) servers that expose governance primitives as tools to any MCP-compatible client (Claude Code, Claude Desktop, etc.).

### hummbl-governance (core)

```json
{
  "mcpServers": {
    "hummbl-governance": {
      "command": "python",
      "args": ["/path/to/hummbl-governance/mcp_server.py"],
      "env": {
        "GOVERNANCE_STATE_DIR": "/path/to/state"
      }
    }
  }
}
```

**10 tools:** `governance_status`, `kill_switch_status`, `kill_switch_engage`, `kill_switch_disengage`, `circuit_breaker_status`, `cost_budget_check`, `cost_record_usage`, `audit_query`, `compliance_report`, `health_check`

### hummbl-compliance

```json
{
  "mcpServers": {
    "hummbl-compliance": {
      "command": "python",
      "args": ["/path/to/hummbl-governance/mcp_compliance.py"],
      "env": {
        "GOVERNANCE_AUDIT_DIR": "/path/to/audit"
      }
    }
  }
}
```

**5 tools:** `nist_map_controls`, `soc2_assess`, `iso_crosswalk`, `stride_analysis`, `compliance_evidence_export`

### agent-sandbox

```json
{
  "mcpServers": {
    "agent-sandbox": {
      "command": "python",
      "args": ["/path/to/hummbl-governance/mcp_sandbox.py"],
      "env": {
        "SANDBOX_STATE_DIR": "/path/to/sandbox"
      }
    }
  }
}
```

**5 tools:** `sandbox_create`, `sandbox_check`, `sandbox_validate_output`, `sandbox_status`, `sandbox_destroy`

All three servers use stdio JSON-RPC and have zero third-party dependencies.

## Design Principles

- **Zero third-party runtime dependencies** -- stdlib only (Python 3.11+)
- **Thread-safe** -- all modules use appropriate locking
- **Configurable** -- no hardcoded agent names or paths
- **Independently importable** -- each module works standalone

## Development

```shell
python -m venv .venv && source .venv/bin/activate
pip install -e ".[test]"
python -m pytest tests/ -v
```

## HUMMBL Ecosystem

This repo is part of the [HUMMBL](https://github.com/hummbl-dev) cognitive AI architecture. Related repos:

| Repo | Purpose |
| --- | --- |
| [base120](https://github.com/hummbl-dev/base120) | Deterministic cognitive framework -- 120 mental models across 6 transformations |
| [mcp-server](https://github.com/hummbl-dev/mcp-server) | Model Context Protocol server for Base120 integration |
| [arbiter](https://github.com/hummbl-dev/arbiter) | Agent-aware code quality scoring and attribution |
| [hummbl-agent](https://github.com/hummbl-dev/hummbl-agent) | Governed control plane for AI agent systems |
| [hummbl-bibliography](https://github.com/hummbl-dev/hummbl-bibliography) | Bibliography for the HUMMBL cognitive framework |
| [agentic-patterns](https://github.com/hummbl-dev/agentic-patterns) | Stdlib-only safety patterns for agentic AI systems |
| [governed-iac-reference](https://github.com/hummbl-dev/governed-iac-reference) | Reference architecture for governed infrastructure-as-code |

## Links

- [PyPI](https://pypi.org/project/hummbl-governance/)
- [GitHub](https://github.com/hummbl-dev/hummbl-governance)
- [hummbl.io](https://hummbl.io)
- [Linktree](https://linktr.ee/hummbl)
- [HUMMBL Slop Tracker (Substack)](https://hummbl.substack.com)

## License

Apache 2.0. Copyright 2026 HUMMBL, LLC.

## About

Governance runtime for AI agent orchestration — kill switch, circuit breaker, cost governor, delegation tokens, audit log, identity registry, schema validator. Zero dependencies. 1,032 tests. 26 primitives.

[hummbl.io](https://hummbl.io 'https://hummbl.io')

### Topics

[python](https://github.com/topics/python 'Topic: python') [multi-agent](https://github.com/topics/multi-agent 'Topic: multi-agent') [ai-safety](https://github.com/topics/ai-safety 'Topic: ai-safety') [ai-agents](https://github.com/topics/ai-agents 'Topic: ai-agents') [ai-governance](https://github.com/topics/ai-governance 'Topic: ai-governance') [hummbl](https://github.com/topics/hummbl 'Topic: hummbl') [stdlib-only](https://github.com/topics/stdlib-only 'Topic: stdlib-only') [base120](https://github.com/topics/base120 'Topic: base120') [governance-primitives](https://github.com/topics/governance-primitives 'Topic: governance-primitives')

### Resources

[Readme](https://github.com/#readme-ov-file)

### License

[Apache-2.0 license](https://github.com/#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](https://github.com/#coc-ov-file)

### Contributing

[Contributing](https://github.com/#contributing-ov-file)

### Security policy

[Security policy](https://github.com/#security-ov-file)

### Uh oh!

There was an error while loading. [Please reload this page]().

[Activity](https://github.com/hummbl-dev/hummbl-governance/activity)

### Stars

[**0** stars](https://github.com/hummbl-dev/hummbl-governance/stargazers)

### Watchers

[**0** watching](https://github.com/hummbl-dev/hummbl-governance/watchers)

### Forks

[**1** fork](https://github.com/hummbl-dev/hummbl-governance/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fhummbl-dev%2Fhummbl-governance&report=hummbl-dev+%28user%29)

## [Releases 2](https://github.com/hummbl-dev/hummbl-governance/releases)

[v1.0.0 Latest\\ \\ Jun 14, 2026](https://github.com/hummbl-dev/hummbl-governance/releases/tag/v1.0.0)

[\+ 1 release](https://github.com/hummbl-dev/hummbl-governance/releases)

## [Packages 0](https://github.com/users/hummbl-dev/packages?repo_name=hummbl-governance)

No packages published 

### Uh oh!

There was an error while loading. [Please reload this page]().

## [Contributors 5](https://github.com/hummbl-dev/hummbl-governance/graphs/contributors)

- [![@hummbl-dev](https://avatars.githubusercontent.com/u/238336761?s=64&v=4)](https://github.com/hummbl-dev)
- [![@devin-ai-integration[bot]](https://avatars.githubusercontent.com/in/811515?s=64&v=4)](https://github.com/apps/devin-ai-integration)
- [![@claude](https://avatars.githubusercontent.com/u/81847?s=64&v=4)](https://github.com/claude)
- [![@koteshyelamati](https://avatars.githubusercontent.com/u/196373335?s=64&v=4)](https://github.com/koteshyelamati)
- [![@rpbowlby](https://avatars.githubusercontent.com/u/55342340?s=64&v=4)](https://github.com/rpbowlby)

## Languages

- [Python 97.9%](https://github.com/hummbl-dev/hummbl-governance/search?l=python)
- [JavaScript 1.9%](https://github.com/hummbl-dev/hummbl-governance/search?l=javascript)
- Other 0.2%
# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/docs/REPO_HEALTH.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

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

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/docs/REPO_HEALTH.md)

History

95 lines (71 loc) · 5.03 KB

## FilesExpand file tree

 main

/

# REPO\_HEALTH.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

95 lines (71 loc) · 5.03 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/docs/REPO_HEALTH.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Repository Health Contract

## Identity

- **Repository**: `hummbl-dev/hummbl-agent`
- **Canonical URL**: `https://github.com/hummbl-dev/hummbl-agent`
- **Root package**: `hummbl-agent`
- **Owner**: HUMMBL Team
- **Stewardship scope**: Governed AI agent control plane, kernel contracts, policy compilation, skill registry, router, runners, gateway adapters, schemas, and audit-oriented documentation.

## Lifecycle

- **Status**: Active proprietary monorepo.
- **Default branch**: `main`.
- **Current version**: `0.1.1` from `VERSION`.
- **Release posture**: Kernel contracts, control-plane policy behavior, router decisions, skill registry metadata, gateway integrations, runner docs, and schemas may continue through reviewed pull requests.
- **Archive trigger**: Archive only if the governed agent control-plane surface moves to another declared canonical repository and downstream package/workflow references are updated.

## Source Of Truth

- `VERSION` defines the repository version.
- `package.json` defines the root workspace metadata, Node 20+ engine, pnpm package manager, schema validation scripts, and dependency overrides.
- `packages/kernel/` contains core agent, task, tool, state, memory, and Base120 tuple contracts.
- `packages/control-plane/` contains the deterministic policy compiler and evaluator.
- `packages/router/` contains skill-to-runner routing, Base120 binding validation, and router tests.
- `packages/gateway/` contains external service gateway code and should be treated as integration-sensitive.
- `packages/runners/` contains runner capability declarations and runner documentation.
- `skills/` and `skills/MANIFEST.json` are the skill registry surface.
- `schemas/` contains JSON Schema contracts used by validation scripts.
- `docs/` contains operating docs, specs, templates, reports, guides, threat model, and validation checklists.
- `.github/workflows/ci.yml` is the primary path-aware guardrails workflow.
- `.github/workflows/kernel-tuples.yml` validates kernel tuple contracts and tuple-bearing configs.

## Required Local Validation

Before merging code, schema, package, or registry changes:

```shell
corepack enable
pnpm install
pnpm run lint:schemas
pnpm run test:schemas
scripts/e2e-validate.sh --mode offline
```

Package-specific changes should also run the matching package checks, for example:

```shell
cd packages/kernel && npm run build
cd packages/control-plane && npm test
cd packages/router && npm test
```

Documentation-only changes should at minimum pass:

```shell
git diff --check
```

## CI Expectations

Expected GitHub Actions coverage:

- `.github/workflows/ci.yml` always runs `classify` to decide whether a pull request is docs-only or code-bearing.
- `.github/workflows/ci.yml` runs main guardrails on Node 22 as a forward-compatibility lane above the local Node 20+ floor.
- `.github/workflows/ci.yml` skips `code-checks` for docs-only pull requests and relies on the always-running `guardrails` gate.
- `.github/workflows/ci.yml` treats pushes to `main` as code-bearing and runs the full guardrail suite.
- Code-bearing checks include dependency audit, Markdown lint, schema validation, communication and LLM config linting, version validation, skill registry verification, ESM linting, policy/security lints, Base120 checks, router build/tests, package coverage, runner consistency checks, and verify-hummbl artifact generation.
- `.github/workflows/kernel-tuples.yml` runs kernel typechecking, tuple test-vector verification, and tuple config linting on Node 20.
- `.github/workflows/codeql.yml` runs JavaScript/TypeScript CodeQL analysis when present.

## Branch Protection Expectation

`main` should require pull request review and the `guardrails` status check from `.github/workflows/ci.yml`. Do not require the internal `classify` or `code-checks` jobs directly; the workflow README documents `guardrails` as the required aggregate gate.

Branch protection is tracked centrally in `hummbl-dev/hummbl-dev#18`; do not overclaim required checks until that audit is updated.

## Operational Notes

- Canonical local Node version is Node 20+.
- Use `corepack enable` and pnpm 9.14.4 for root and workspace commands.
- Package-local npm commands remain valid inside packages that own `npm` scripts and package locks; do not use root `npm install` for workspace setup.
- Gateway and router dependencies are runtime-sensitive; do not generalize the root zero-runtime-dependency badge across every package without checking package manifests.
- Generated `dist/` artifacts under packages should be treated as committed package artifacts only when the owning package expects them.
- Secrets, LLM configs, communication configs, and runner capability declarations are policy-controlled surfaces.

## Fleet Scan Classification

Future fleet scans can classify this repository as:

- **Lifecycle**: active proprietary monorepo
- **Visibility**: public GitHub repository with proprietary license
- **Primary function**: governed AI agent control plane
- **Validation entrypoint**: path-aware `guardrails` CI plus package tests for code changes
- **Primary metadata owner**: HUMMBL Team
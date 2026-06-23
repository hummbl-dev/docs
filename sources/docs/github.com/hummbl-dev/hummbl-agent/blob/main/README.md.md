# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/README.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

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

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/README.md)

History

153 lines (108 loc) · 6.46 KB

 main

/

# README.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

153 lines (108 loc) · 6.46 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/README.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# hummbl-agent

**A governed control plane for AI agent systems** -- registry-first skill management, deterministic policy routing, and auditable execution across any LLM runner.

Learn more at [hummbl.io](https://hummbl.io).

[![CI](https://github.com/hummbl-dev/hummbl-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/hummbl-dev/hummbl-agent/actions/workflows/ci.yml) [![Node 20+](https://camo.githubusercontent.com/721738b75b531b2182db206f48ee1995a8538bb9eed24a53322a34d5aa556ee5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f64652d32302532422d627269676874677265656e)](https://camo.githubusercontent.com/721738b75b531b2182db206f48ee1995a8538bb9eed24a53322a34d5aa556ee5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f64652d32302532422d627269676874677265656e) [![TypeScript](https://camo.githubusercontent.com/452f8ed87b74dd2902d7af0c0dd16f862f9ce08a52716a9c58b17da96021ca1b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f747970657363726970742d352e782d626c7565)](https://camo.githubusercontent.com/452f8ed87b74dd2902d7af0c0dd16f862f9ce08a52716a9c58b17da96021ca1b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f747970657363726970742d352e782d626c7565) [![License](https://camo.githubusercontent.com/041c000f066b01f3302dfb9ccf11308bf1c45cea8c93dc0110c75b405787aab9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d50726f70726965746172792d6c6967687467726579)](https://camo.githubusercontent.com/041c000f066b01f3302dfb9ccf11308bf1c45cea8c93dc0110c75b405787aab9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d50726f70726965746172792d6c6967687467726579) [![Root runtime deps](https://camo.githubusercontent.com/9a61e18aed16bf322c00b2c736471f52663f693c39750a8c438cf95072cdc9db/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f726f6f745f72756e74696d655f646570732d302d677265656e)](https://camo.githubusercontent.com/9a61e18aed16bf322c00b2c736471f52663f693c39750a8c438cf95072cdc9db/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f726f6f745f72756e74696d655f646570732d302d677265656e) [![Last commit](https://camo.githubusercontent.com/452bf48f3ebb9607037a5c2e47d317d28706f8cb43425ad3b3eeb4b31e82dfa8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6173742d636f6d6d69742f68756d6d626c2d6465762f68756d6d626c2d6167656e742f6d61696e)](https://github.com/hummbl-dev/hummbl-agent/commits/main)

---

Repository health, validation, and stewardship expectations are tracked in [docs/REPO\_HEALTH.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/docs/REPO_HEALTH.md).

> **Dependency scope note**: The root workspace (`package.json`) has zero runtime dependencies. Individual workspace packages under `packages/` declare their own runtime dependencies as needed. See [Dependency Audit](https://github.com/#dependency-audit) for the full matrix.

## Quick start

```shell
git clone https://github.com/hummbl-dev/hummbl-agent.git
cd hummbl-agent
corepack enable
pnpm install
pnpm run lint:schemas          # validate skill schemas
scripts/e2e-validate.sh        # end-to-end validation
```

---

## What it does

Most agent frameworks let LLMs decide what to run and how. hummbl-agent inverts that -- policies decide, agents execute.

| Primitive | What it does | Location |
| --- | --- | --- |
| **Kernel** | Type-safe agent, task, tool, and state definitions | `packages/kernel/` |
| **Control Plane** | JSON policy DSL, deterministic compilation, emits `ControlDecision` | `packages/control-plane/` |
| **Router** | Routes skills to runners based on policy + capability matching | `packages/router/` |
| **Runners** | Adapter layer for 10 LLM backends (Claude, Codex, Gemini, Grok, Ollama, etc.) | `packages/runners/` |
| **Governance** | Policy schemas, compliance claims, audit logs | `packages/governance/` |
| **Skill Registry** | 75+ skills with SHA-256 integrity, CI-validated manifest | `skills/` |
| **Gateway** | Adapters for Anthropic, OpenAI, and communication channels | `packages/gateway/` |
| **Schemas** | JSON Schema definitions for skills, decisions, and inter-agent requests | `schemas/` |

---

## Why this exists

Agent tooling today has a trust problem. Most frameworks give the model full authority over tool selection, execution order, and state mutation. That works for demos. It breaks in production.

hummbl-agent is built on three principles:

1. **Registry-first.** The local `skills/MANIFEST.json` is the only source of truth. No external registries, no dynamic resolution, no ambient authority. Every skill is hash-verified.
 
2. **Policy-bounded.** A JSON policy DSL defines what can run, where, and under what constraints. The control plane compiles policies into deterministic `ControlDecision` objects. No heuristics, no planning, no LLM-in-the-loop for routing.
 
3. **Vendor-agnostic.** Claude Code, Codex, Gemini, Grok, Ollama, and five other runners are interchangeable adapters. Swap the runner, keep the governance. No vendor lock-in at the execution layer.
 

The control plane dispatches. It does not execute. This separation means you can audit every decision, replay any run, and prove what happened.

---

## Install

```shell
# requires Node 20+ and pnpm 9.14.4 via Corepack
corepack enable
pnpm install

# build all packages
pnpm -r build

# run tests
pnpm -r test
```

Individual packages are scoped under `@hummbl/`:

```shell
# Package-local npm commands are valid inside packages that own npm scripts.
cd packages/kernel && npm test
cd packages/control-plane && npm test
cd packages/router && npm test
```

---

## Project structure

```
hummbl-agent/
  packages/
    kernel/           # Core types (agent, task, tool, state, memory)
    control-plane/    # Policy DSL + deterministic evaluation
    router/           # Skill-to-runner routing engine
    runners/          # 10 LLM backend adapters
    runtime/          # Python runtime bridge
    governance/       # Policy schemas + compliance
    gateway/          # External service adapters
    adapters/         # Communication + LLM adapters
    vendor-bridge/    # Vendor path mapping (non-authoritative)
  skills/             # Canonical skill registry + MANIFEST.json
  schemas/            # JSON Schema definitions
  scripts/            # CI + validation scripts
  tests/              # Integration + e2e tests
```

---

## Dependency Audit

The root workspace has zero runtime dependencies. Per-package runtime dependencies:

| Package | Runtime Dependencies | Dev Dependencies |
| --- | --- | --- |
| `packages/kernel` | — | TypeScript build tools |
| `packages/control-plane` | — | TypeScript build tools |
| `packages/router` | `ajv`, `express`, `openai` | TypeScript, `@types/express` |
| `packages/gateway` | `dotenv`, `undici` | `tsx` |
| `packages/governance` | `yaml` | TypeScript, Vitest |
| `packages/runners` | — | TypeScript build tools |

> **Scope clarification**: The "Zero runtime deps" badge applies to the root workspace only. Gateway, router, and governance packages carry runtime dependencies for HTTP, validation, and YAML parsing respectively. This is intentional — each package pays only for what it uses.

---

## Related projects

| Project | Description |
| --- | --- |
| [hummbl-governance](https://github.com/hummbl-dev/hummbl-governance) | Governance framework and policy primitives (`pip install hummbl-governance`) |
| [HUMMBL Research Corpus](https://hummblresearch.substack.com) | Research notes on agent governance, Base120, and multi-agent coordination |
| [hummbl.io](https://hummbl.io) | Company site |
| [base120](https://github.com/hummbl-dev/base120) | 120 mental models for structured reasoning |
| [arbiter](https://github.com/hummbl-dev/arbiter) | Agent-aware code quality scoring and attribution |
| [hummbl-bibliography](https://github.com/hummbl-dev/hummbl-bibliography) | Bibliography for the HUMMBL cognitive framework |

---

## Contributing

See [CONTRIBUTING.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/CONTRIBUTING.md) for branch naming, commit conventions, and PR guidelines.

---

## License

Proprietary. Copyright (c) 2026 Reuben Bowlby and Daniel Matha. All rights reserved. See [LICENSE](https://github.com/hummbl-dev/hummbl-agent/blob/main/LICENSE).
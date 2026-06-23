# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/AGENTS.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

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

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/AGENTS.md)

History

39 lines (24 loc) · 4.27 KB

## FilesExpand file tree

 main

/

# AGENTS.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

39 lines (24 loc) · 4.27 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/AGENTS.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Repository Guidelines

## Project Structure & Module Organization

Runtime code lives in `packages/` (kernel, router, adapters, control-plane, governance, gateway, vendor-bridge, runners) and stays in strict ESM TypeScript. Registries are authoritative only inside `skills/` (plus `skills/MANIFEST.json`) and the Base120 skill folders like `P-perspective/`; agent/command Markdown briefs describe operator interfaces but never source registry data. `_state/` stores dated run logs, prompts, and artifacts, while `docs/` holds canonical workflows plus validation checklists referenced during reviews. Runners are governed by `configs/moltbot`, `configs/engineer-agent`, and `configs/process-policy.*`, and automation plus lint guards live in `scripts/`.

## Build, Test, and Development Commands

- `npm install` installs the shared developer dependencies before any script.
- `node scripts/lint-esm.mjs` (plus targeted guards such as `scripts/lint-router-exports.sh` or `scripts/lint-state.sh`) keeps imports, state, and registries aligned.
- `scripts/orchestrate.sh [--force]` seeds prompt packets and `scripts/run-cmd.sh --runner ai-steward -- <cmd>` captures governed command artifacts in `_state/runs/<date>/`.
- `scripts/e2e-validate.sh --mode offline|live` runs regression plus `scripts/test-network-guard.sh`; finish a status package with `scripts/generate-sitrep.sh && scripts/lint-sitrep.sh`.

## Coding Style & Naming Conventions

Use two-space indentation for TypeScript, Markdown, and YAML, keep `packages/kernel/tsconfig.json` strict settings, and prefer named exports. Skill IDs follow `S.<tier>.T.<domain>.<slug>.vX.Y.Z`, Base120 folders use the `XX-name` prefix, and Markdown agents should keep level-two headings plus fenced `bash`/`typescript` snippets. For configs and registries, alphabetize keys, preserve trailing newlines, and rerun the relevant `scripts/lint-*.sh` guard.

## Testing Guidelines

Unit tests sit next to adapters under `packages/**/tests/*.test.mjs` and rely on Node's built-in test runner; invoke them via `node --test packages/adapters/llm/tests/*.test.mjs` or `rg --files -g '*.test.mjs' | xargs node --test`. Keep filenames descriptive (`provider-action.test.mjs`), document fixtures inline, and clean temporary configs the way `removeLocal()` does in the Anthropics coverage. Before review, execute `scripts/e2e-validate.sh --mode offline` and attach the `_state/runs/.../log` snippet.

**Test Policy (Enforced):**

- **File Extension:** `.test.mjs` only (no `.test.ts` files allowed)
- **Test Runner:** Node's built-in `--test` flag for router, adapters, control-plane, and runners; `packages/governance` runs `vitest run` (see note below)
- **Imports:** Import compiled JS from `dist/` or use CJS `require()` for adapters
- **Prohibited:** Runtime TypeScript loaders (ts-node, tsx, etc.)
- **Build Order:** For packages with TypeScript source, build must precede test execution
- **Guard:** `scripts/lint-no-ts-tests.sh` enforces `.test.mjs` requirement in CI

**Governance Package Exception:** Governance profile/audit tests (`packages/governance/tests/*.test.ts`) depend on Vitest to coordinate shared state in `governance-state-dir`. Run them via `npm --prefix packages/governance run test`, and ensure the suite has exclusive access to that directory (see `vitest.config.ts`). All other packages remain on Node's native runner, and the `.test.mjs` extension rule still applies everywhere.

## Commit & Pull Request Guidelines

Commits follow the Conventional Commits flavor visible in `git log` (`feat(llm): ...`, `fix(communication): ...`) with scopes that map to top-level directories. Every pull request should include a short summary, linked HUMMBL issue or run ID, unit-test plus `scripts/e2e-validate.sh` results, and notes on any registry or config touched. When shipping new commands or skills, mention the exact `_state/` artifacts or SITREPs used to prove validation.

## Security & Configuration Tips

Never commit live API keys—use the `configs/moltbot/*.local.json` templates and run `scripts/lint-secret-scan.sh` plus `scripts/lint-secrets-policy.sh` before pushing. Changes that expand process or network capability must update `configs/process-policy.allowlist`, pass `scripts/lint-network-policy.sh` and `scripts/verify-hummbl.sh`, and document the guardrail delta inside `docs/validation-checklist.md`.
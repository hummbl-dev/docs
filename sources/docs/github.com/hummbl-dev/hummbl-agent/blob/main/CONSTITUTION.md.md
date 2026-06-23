# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/CONSTITUTION.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# CONSTITUTION.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/CONSTITUTION.md)

History

71 lines (52 loc) · 3.68 KB

 main

/

# CONSTITUTION.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

71 lines (52 loc) · 3.68 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/CONSTITUTION.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# CONSTITUTION.md — hummbl-agent

**Status:** v0.1 **Steward:** HUMMBL Research Institute **Approving human:** Reuben Bowlby **Standard:** HUMMBL Repo Standard v0.1 **Source of record:** git

## 1\. Identity

`hummbl-dev/hummbl-agent` — Governed control plane for AI agent systems. Registry-first skill management, deterministic policy routing, and auditable execution across any LLM runner. Strict ESM TypeScript pnpm workspace; root workspace has zero runtime dependencies.

- **Class:** library
- **Visibility:** public
- **License:** Proprietary
- **Validation:** `scripts/e2e-validate.sh --mode offline`

## 2\. Scope

This constitution operates under the HUMMBL Repo Standard (`hummbl-dev/hummbl-governance/docs/standards/HUMMBL_REPO_STANDARD.md`) and the operating-environment constitution on the host machine. This constitution may be stricter than both, never weaker.

## 3\. Protected invariants

These invariants are constitutionally protected. They cannot be changed, weakened, or conditionally suspended without a constitutional amendment (§7), a KRINEIA receipt, and human approval.

1. **Registry-first.** skills/MANIFEST.json is the sole source of truth for skills. Every skill is SHA-256 integrity-verified. No external registry, no dynamic resolution.
2. **Policy-bounded dispatch.** The control plane emits deterministic ControlDecision objects compiled from the JSON policy DSL. No LLM-in-the-loop, no heuristics, no planning.
3. **Vendor-agnostic runners.** Runners are interchangeable adapters. No runner-specific behavior may leak into the kernel, control plane, or router.
4. **Zero root runtime dependencies.** The root package.json declares no runtime dependencies. Per-package deps are documented.
5. **Strict ESM TypeScript.** Runtime code in packages/ stays strict ESM TypeScript; tsconfig.json strict settings preserved.
6. **Test discipline.** Tests use .test.mjs extension and Node --test runner. Runtime TypeScript loaders prohibited. Governance package is sole exception (Vitest).
7. **No live secrets.** Live API keys must never be committed. scripts/lint-secret-scan.sh and scripts/lint-secrets-policy.sh must pass.
8. **Capability expansion is explicit.** Any change expanding process or network capability must update allowlists, pass verification scripts, and document the guardrail delta.
9. **Receipt integrity.** The Krineia chain is append-only and SHA-256-chained. No operator may rewrite history except via documented cut.

## 4\. Normative files

The following files are normative. Edits require steward review (see `CODEOWNERS`):

- `CONSTITUTION.md`
- `KRINEIA.md`
- `hummbl.repo.yaml`
- `CODEOWNERS`
- `skills/MANIFEST.json`
- `packages/kernel/`
- `packages/control-plane/`
- `schemas/`
- `AGENTS.md`

## 5\. Authority

- **Steward:** HUMMBL Research Institute
- **Approving human:** Reuben Bowlby
- **Codeowners:** `CODEOWNERS`
- **Agent operating contract:** `AGENTS.md`
- **Receipt manifest:** `KRINEIA.md`

## 6\. Receipt-triggering changes

The following changes require a KRINEIA receipt before admission:

- Any edit to CONSTITUTION.md, KRINEIA.md, hummbl.repo.yaml, or CODEOWNERS
- Any change to a protected invariant
- Any change to configs/process-policy.allowlist, configs/network-policy.json, or configs/secrets-policy.json
- Any addition, removal, or hash change of a skill in skills/
- Any change to packages/kernel/ type definitions or tsconfig.json strict settings
- Any change to CI workflows that alters invariant enforcement

## 7\. Amendment

Changes to this constitution require: a PR, an ADR under `docs/adr/`, a KRINEIA receipt, and human approval (Reuben Bowlby). Breaking changes bump this constitution's version (SemVer) and trigger a fleet re-audit of all repos consuming this repo's outputs.
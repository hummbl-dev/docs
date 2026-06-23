# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/AUDIT_REPORT.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# AUDIT\_REPORT.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/AUDIT_REPORT.md)

History

249 lines (179 loc) · 8.63 KB

 main

/

# AUDIT\_REPORT.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

249 lines (179 loc) · 8.63 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/AUDIT_REPORT.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Repository Audit Report

**Date**: 2026-04-08 **Scope**: Full monorepo audit — structure, security, dependencies, code quality **Version**: 0.1.1

---

## Executive Summary

HUMMBL-Agent is a policy-driven AI agent orchestration framework built as a TypeScript/ESM monorepo. The codebase demonstrates strong governance, strict security boundaries, and comprehensive CI/CD automation. This audit identified **0 critical**, **2 high**, **5 medium**, and **4 low** priority findings.

| Category | Rating | Notes |
| --- | --- | --- |
| Architecture | **A** | Clean separation, zero-runtime-dep root, registry-first |
| Security | **A-** | Defense-in-depth; 1 hardcoded dev password, 1 moderate CVE |
| CI/CD | **A** | 50+ automated checks, secret scanning, schema validation |
| Code Quality | **B+** | Strict TS, but missing ESLint/Prettier, 3 `any` casts |
| Test Coverage | **B** | Governance excellent (11 suites); control-plane/router gaps |
| Documentation | **A** | Extensive docs, guides, decision records, SECURITY.md |
| Dependency Health | **A-** | Minimal deps, pnpm overrides for CVEs; 1 moderate vuln |
| Monorepo Config | **B-** | Missing pnpm-workspace.yaml; version inconsistency |

---

## 1\. Repository Structure

### Packages (7 core)

| Package | Version | Purpose |
| --- | --- | --- |
| `@hummbl/kernel` | _(none)_ | Type-safe contracts — types only, no runtime |
| `@hummbl/control-plane` | 0.1.0 | Policy DSL, deterministic evaluation |
| `@hummbl/router` | 0.1.0 | Skill-to-runner routing, LLM vendor selection |
| `@hummbl/gateway` | 0.1.0 | External service adapters (Signal, etc.) |
| `@hummbl/governance` | 0.1.0 | Policy schemas, compliance claims, audit logs |
| adapters | — | Governed wrappers (process, LLM, communication) |
| runners | — | 12 LLM backend adapters |

### Additional Components

- **195 skills** in `skills/` with SHA-256 integrity hashes in `MANIFEST.json`
- **60+ scripts** for linting, validation, governance, and monitoring
- **8 JSON schemas** in `schemas/` for skill metadata, decisions, compliance
- **40+ markdown guides** in `docs/`
- **State management** in `_state/` (decisions, evidence, SITREPs)

### CI/CD Pipeline

The `.github/workflows/ci.yml` workflow runs 50+ checks:

- Dependency audit (`pnpm audit --audit-level=high`)
- Schema validation (AJV compile + validate)
- 3-layer secret scanning
- Skill manifest hash verification
- Base120 canonical JSON validation
- ESM import linting
- Network and secrets policy validation
- Router build + tests
- Adapter offline tests
- Runner capability checks
- Evidence log validation
- HUMMBL verification with JSON artifact output

---

## 2\. Security Findings

### 2.1 Vulnerability: smol-toml DoS (MODERATE)

- **CVE**: GHSA-v3rj-xjv7-4jmq
- **Package**: `smol-toml@1.6.0` (transitive via `markdownlint-cli2`)
- **CVSS**: 5.3
- **Impact**: Stack overflow via malicious TOML with consecutive comment lines
- **Fix**: Upgrade `smol-toml` to >= 1.6.1

### 2.2 Hardcoded Gateway Password (LOW)

- **File**: `configs/moltbot/gateway.json:15`
- **Value**: `"password": "hummbl-2025"`
- **Mitigations**: Binds to 127.0.0.1 only; network policy restricts external access
- **Fix**: Move to environment variable or `gateway.local.json`

### 2.3 Security Strengths

- **Process execution**: Allowlist-based (`configs/process-policy.allowlist`), `spawn()` with `shell: false`
- **Network policy**: Default-deny, 7-domain allowlist, rate limiting (60 req/min), response size caps
- **Secrets policy**: Whitelist-based, no-logging/no-persistence enforcement
- **CI gates**: 3-layer secret scanning, dependency audit on every PR
- **Adapter security**: Header scrubbing, HTTPS-only, domain allowlist enforcement, timeout protection
- **No eval()**, no raw SQL, no innerHTML, no command injection vectors found

### 2.4 API Input Validation (NEEDS IMPROVEMENT)

- **File**: `packages/router/src/http/routes/ingest_message.ts`
- No schema validation on `/ingest/message` endpoint
- No request length limits beyond Express default (1MB)
- No per-endpoint rate limiting
- No authentication middleware (acceptable for localhost-only binding)

---

## 3\. Dependency Health

### Root Dependencies

All dependencies use safe semver ranges (`^version`). pnpm overrides patch known CVEs:

```json
"pnpm": {
  "overrides": {
    "fast-json-patch": "^3.1.1",
    "minimatch": ">=3.1.4",
    "picomatch": ">=4.0.2"
  }
}
```

### Package Dependencies (Minimal)

| Package | Production Deps | Notable |
| --- | --- | --- |
| Root | 0 | Zero-runtime-dep policy |
| Router | express@5.2.1, openai@6.32.0 | Latest Express 5 |
| Gateway | dotenv, undici@7.24.0 | Modern HTTP client |
| Governance | yaml@2.8.3 | YAML parsing only |
| Control-plane | ajv@8.18.0 | Schema validation |
| Kernel | 0 | Types-only package |

### License

Proprietary license (Reuben Bowlby and Daniel Matha). All packages marked `"private": true`.

---

## 4\. Code Quality Findings

### 4.1 TypeScript Configuration: GOOD

All packages use `strict: true`, `target: ES2022`, `module: ESNext`.

### 4.2 Type Safety Issues (MEDIUM)

| File | Line | Issue |
| --- | --- | --- |
| `packages/router/src/http/routes/ingest_message.ts` | 16 | `catch (e: any)` |
| `packages/kernel/src/tuples/validate.ts` | 39 | `(tuple as any)` |
| `packages/governance/src/cli.ts` | 139 | `action: action as any` |

### 4.3 Silent Error Handling (MEDIUM)

15+ catch blocks across governance package silently return `null` without logging. Files affected:

- `packages/governance/src/environment.ts` — multiple `catch { return null; }`
- `packages/governance/src/roles.ts` — silent catch
- `packages/governance/src/profile.ts` — multiple silent catches

### 4.4 Missing Linting Tools (MEDIUM)

- **No ESLint** configuration found
- **No Prettier** configuration found
- Markdown linting is well-configured (`.markdownlint.json`, `.markdownlint-cli2.yaml`)

### 4.5 Test Coverage Gaps

| Package | Test Status | Framework |
| --- | --- | --- |
| Governance | 11 test suites | Vitest |
| Router | 20+ baseline/binding tests | Node --test |
| Adapters | Offline LLM tests | Node --test |
| Control-plane | **Placeholder only** (.gitkeep) | — |
| Kernel | **No tests** | — |

### 4.6 Empty/Stub Files

- `/tsx` — 0-byte file at repo root (appears accidental)
- `packages/control-plane/tests/.gitkeep` — test placeholder, no actual tests
- `packages/_state/runs/.gitkeep` — intentional git keep

---

## 5\. Monorepo Configuration Issues

### 5.1 Missing pnpm-workspace.yaml (HIGH)

No workspace configuration file exists despite the multi-package structure. This means:

- No automatic workspace dependency resolution
- Manual dependency management between packages
- Cross-package imports use relative paths instead of workspace protocol

### 5.2 Version Inconsistency (HIGH)

- Root `VERSION` file: **0.1.1**
- All `package.json` files: **0.1.0**
- `@hummbl/kernel`: **no version declared**

### 5.3 Unused/Orphaned Packages (LOW)

- `packages/adapters/*` (anthropic, openai, process) — no internal imports found
- `packages/runtime` (Python) — not integrated with TypeScript build
- `packages/vendor-bridge` — minimal implementation

---

## 6\. Prioritized Recommendations

### Priority 1 — HIGH (Address Soon)

1. **Create `pnpm-workspace.yaml`** declaring all packages under `packages/`
2. **Align versions**: Update all `package.json` to `0.1.1` to match `VERSION`; add version to `@hummbl/kernel`

### Priority 2 — MEDIUM (Next Sprint)

3. **Upgrade smol-toml** to >= 1.6.1 (`pnpm update markdownlint-cli2`)
4. **Add ESLint + Prettier** with TypeScript support
5. **Replace 3 `any` type assertions** with proper types
6. **Add error logging** to silent catch blocks in governance package
7. **Add tests for control-plane** (currently empty test directory)

### Priority 3 — LOW (Backlog)

8. **Move gateway password** to env variable or `.local.json`
9. **Add schema validation** to `/ingest/message` endpoint (ajv is already a dep)
10. **Remove `/tsx`** zero-byte file from repo root
11. **Document adapter package status** — clarify if intentionally unused or planned

---

## Architecture Strengths

- **Registry-first design** with SHA-256 integrity and no external registry coupling
- **Defense-in-depth security** — process allowlist, network deny-by-default, secret scanning
- **Vendor-agnostic routing** — 12 interchangeable LLM backends
- **Deterministic governance** — policy DSL with compliance claims and audit trails
- **Comprehensive CI** — 50+ automated gates prevent regression
- **Base120 mental model integration** — 6 categories, 120 canonical thinking skills
- **Zero runtime deps at root** — minimal attack surface

---

_Generated by repository audit on 2026-04-08._
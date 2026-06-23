# Source: https://github.com/hummbl-dev/arbiter/blob/main/CONSTITUTION.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

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

[History](https://github.com/hummbl-dev/arbiter/commits/main/CONSTITUTION.md)

History

62 lines (43 loc) · 2.65 KB

 main

/

# CONSTITUTION.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

62 lines (43 loc) · 2.65 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/CONSTITUTION.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# CONSTITUTION.md — arbiter

**Status:** v0.1 **Steward:** HUMMBL Research Institute **Approving human:** Reuben Bowlby **Standard:** HUMMBL Repo Standard v0.1 **Source of record:** git

## 1\. Identity

`hummbl-dev/arbiter` — Agent-aware code quality scoring — cyclomatic complexity, dependency analysis, test coverage, governance compliance. Grades repos A through F with evidence-backed findings.

- **Class:** library
- **Visibility:** public
- **License:** See LICENSE file
- **Standard:** HUMMBL Repo Standard v0.1

## 2\. Scope

This constitution operates under the HUMMBL Repo Standard (`hummbl-dev/hummbl-governance/docs/standards/HUMMBL_REPO_STANDARD.md`) and the operating-environment constitution on the host machine. This constitution may be stricter than both, never weaker.

## 3\. Protected invariants

These invariants are constitutionally protected. They cannot be changed, weakened, or conditionally suspended without a constitutional amendment (§7), a KRINEIA receipt, and human approval.

1. **Receipt integrity.** The Krineia chain is append-only and SHA-256-chained. No operator may rewrite history except via documented cut.
2. **No secrets in code.** No API keys, tokens, or credentials may be committed to tracked files.
3. **Standard compliance.** This repo adheres to the HUMMBL Repo Standard v0.1 as declared in hummbl.repo.yaml.
4. **Stdlib-only runtime.** Production code uses only the Python standard library. Third-party dependencies are confined to test/dev extras.
5. **Test gate.** CI must be green before any merge to a protected branch.
6. **Coverage floor.** Test coverage must meet the configured threshold. The floor may be raised but never lowered without amendment.

## 4\. Normative files

The following files are normative. Edits require steward review (see `CODEOWNERS`):

- `CONSTITUTION.md`
- `KRINEIA.md`
- `hummbl.repo.yaml`
- `CODEOWNERS`
- `AGENTS.md`

## 5\. Authority

- **Steward:** HUMMBL Research Institute
- **Approving human:** Reuben Bowlby
- **Codeowners:** `CODEOWNERS`
- **Agent operating contract:** `AGENTS.md`
- **Receipt manifest:** `KRINEIA.md`

## 6\. Receipt-triggering changes

The following changes require a KRINEIA receipt before admission:

- Any edit to `CONSTITUTION.md`, `KRINEIA.md`, `hummbl.repo.yaml`, or `CODEOWNERS`
- Any change to a protected invariant (Section 3)
- Any release or version bump
- Any change to the repo's public contract or API surface

## 7\. Amendment

Changes to this constitution require: a PR, an ADR under `docs/adr/`, a KRINEIA receipt, and human approval (Reuben Bowlby). Breaking changes bump this constitution's version (SemVer) and trigger a fleet re-audit of all repos consuming this repo's outputs.
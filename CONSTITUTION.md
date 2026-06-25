# CONSTITUTION.md - docs

**Status:** v0.1
**Approving human:** Reuben Bowlby
**Steward:** HUMMBL Research Institute

## 1. Purpose

docs is a governed repository under the HUMMBL Repo Standard v0.1.

## 2. Authority

The human Principal Agent (Reuben Bowlby) holds authority over this repository. Delegated software agents may operate within bounds defined by AGENTS.md and the HUMMBL Repo Standard.

## 3. Protected invariants

- Provider neutrality: root governance files must not depend on a specific AI provider
- Receipt integrity: KRINEIA chains are append-only and immutable
- Human authority: no agent may self-authorize durable state changes

## 4. Amendment

Changes to this constitution require:
1. A pull request
2. Review by the code owner
3. Human approval (Reuben Bowlby)
4. A KRINEIA receipt

## 5. Conflict precedence

1. This CONSTITUTION.md
2. KRINEIA.md
3. AGENTS.md
4. Schemas / tests / validators
5. DOCTRINE.md
6. README.md

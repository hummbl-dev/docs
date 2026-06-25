# KRINEIA.md - docs

**Status:** v0.1
**Steward:** HUMMBL Research Institute

## Chain participation

This repo participates in KRINEIA governance as a governed micro-jurisdiction.

## Trust root

Deployment-asserted (separate observer process). See KRINEIA v0.2 roadmap for cryptographic assertion.

## Allowed chain operators

- `append` - add new receipts
- `project` - read-only projection over receipts
- `cut` - produce evidence packs from receipts

## Forbidden operators

- `update` - receipts are immutable
- `delete` - receipts are permanent
- `rewrite` - receipts are append-only
- `summarize_and_replace` - no lossy compression of chain
- `score_and_train` - receipts never enter training

## Receipt-triggering changes

- Changes to CONSTITUTION.md
- Changes to KRINEIA.md
- Changes to hummbl.repo.yaml
- Protected surface modifications
- Governance claim assertions

## Verification

Chain integrity verified by SHA-256 hash linkage. Canonical form: `json.dumps(sort_keys=True, separators=(",",":"))`.

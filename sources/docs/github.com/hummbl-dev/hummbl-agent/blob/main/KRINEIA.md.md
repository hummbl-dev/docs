# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/KRINEIA.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# KRINEIA.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

![hummbl-dev](https://avatars.githubusercontent.com/u/238336761?v=4&size=40)![devin-ai-integration[bot]](https://avatars.githubusercontent.com/in/811515?v=4&size=40)

[hummbl-dev](https://github.com/hummbl-dev/hummbl-agent/commits?author=hummbl-dev)

and

[devin-ai-integration\[bot\]](https://github.com/hummbl-dev/hummbl-agent/commits?author=devin-ai-integration%5Bbot%5D)

[feat(governance): adopt HUMMBL Repo Standard v0.1 (](https://github.com/hummbl-dev/hummbl-agent/commit/97a714521232d2f0e366dba0360a11cde475f90d) [#189](https://github.com/hummbl-dev/hummbl-agent/pull/189) [)](https://github.com/hummbl-dev/hummbl-agent/commit/97a714521232d2f0e366dba0360a11cde475f90d)

Open commit detailsfailure

Jun 22, 2026

[97a7145](https://github.com/hummbl-dev/hummbl-agent/commit/97a714521232d2f0e366dba0360a11cde475f90d) · Jun 22, 2026

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/KRINEIA.md)

Open commit details

History

90 lines (69 loc) · 2.49 KB

·

## FilesExpand file tree

 main

/

# KRINEIA.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

90 lines (69 loc) · 2.49 KB

·

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/KRINEIA.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# KRINEIA.md — hummbl-agent

**krineia\_manifest\_version:** 0.1 **schema:** krineia-manifest@0.1

This is the repo-local KRINEIA manifest for `hummbl-dev/hummbl-agent`. It declares how this repo participates in KRINEIA governance.

---

krineia\_manifest\_version: "0.1" schema: "krineia-manifest@0.1"

repo: full\_name: "hummbl-dev/hummbl-agent" default\_branch: "main" visibility: "public"

authority: steward: "HUMMBL Research Institute" approving\_human: "Reuben Bowlby" source\_of\_record: "git" receipt\_authority: "external\_observer"

governance\_profile: status: "adopted" krineia\_required: true trust\_root\_mode: "deployment\_asserted" receipt\_chain\_required\_for: - "canonical\_docs" - "schema\_changes" - "validator\_changes" - "agent\_handoffs" - "authority\_changes" - "release\_tags"

chains: primary: chain\_id: "hummbl-agent-primary" storage: "\_receipts/krineia/primary.jsonl" genesis\_policy: "repo\_bootstrap" hash\_algorithm: "sha256" canonicalization: "json.dumps(sort\_keys=True,separators=(',',':'))"

operators: allowed: - "append" - "project" - "cut" forbidden: - "update" - "delete" - "rewrite" - "summarize\_and\_replace" - "score\_and\_train"

boundaries: no\_reward\_path\_self\_reference: true external\_analysis\_only: true observed\_agent\_may\_write\_receipts: false receipts\_may\_train\_agents: false

verification: validator: "external" required\_before\_merge: false required\_before\_release: true

related\_docs: readme: "README.md" agents: "AGENTS.md" constitution: "CONSTITUTION.md"

## last\_reviewed: "2026-06-22"

## Notes

### Chain bootstrapping

The primary chain at `_receipts/krineia/primary.jsonl` is bootstrapped with a genesis receipt recording the adoption of this manifest. The genesis receipt has `prev_hash` = 64 ASCII zeros per the KRINEIA receipt schema.

### Trust-root mode

v0.1 uses `deployment_asserted` trust-root mode: a separate observer process writes the chain, and the observed agent has no write path. This satisfies Invariant 5 by process boundary.

### Receipt-triggering changes

Per `CONSTITUTION.md` §6, receipt-triggering changes are listed in that document. Non-triggering changes (routine dependency bumps, docs, test additions that do not alter protected invariants) do not require a receipt.

### Verification

Receipt structure and hash linkage are validated externally. A chain can pass hash validation and still fail KRINEIA if the surrounding system violates any of the five invariants.
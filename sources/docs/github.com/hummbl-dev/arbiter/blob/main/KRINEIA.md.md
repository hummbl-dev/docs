# Source: https://github.com/hummbl-dev/arbiter/blob/main/KRINEIA.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

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

[hummbl-dev](https://github.com/hummbl-dev/arbiter/commits?author=hummbl-dev)

and

[devin-ai-integration\[bot\]](https://github.com/hummbl-dev/arbiter/commits?author=devin-ai-integration%5Bbot%5D)

[feat(governance): adopt HUMMBL Repo Standard v0.1 (](https://github.com/hummbl-dev/arbiter/commit/eb71751976b0a89f710e0d18ee28b3b1408b639b) [#87](https://github.com/hummbl-dev/arbiter/pull/87) [)](https://github.com/hummbl-dev/arbiter/commit/eb71751976b0a89f710e0d18ee28b3b1408b639b)

Open commit detailssuccess

Jun 22, 2026

[eb71751](https://github.com/hummbl-dev/arbiter/commit/eb71751976b0a89f710e0d18ee28b3b1408b639b) · Jun 22, 2026

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/KRINEIA.md)

Open commit details

History

68 lines (53 loc) · 1.6 KB

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
 

68 lines (53 loc) · 1.6 KB

·

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/KRINEIA.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# KRINEIA.md — arbiter

**krineia\_manifest\_version:** 0.1 **schema:** krineia-manifest@0.1

This is the repo-local KRINEIA manifest for `hummbl-dev/arbiter`.

---

krineia\_manifest\_version: "0.1" schema: "krineia-manifest@0.1"

repo: full\_name: "hummbl-dev/arbiter" default\_branch: "main" visibility: "private"

authority: steward: "HUMMBL Research Institute" approving\_human: "Reuben Bowlby" source\_of\_record: "git" receipt\_authority: "external\_observer"

governance\_profile: status: "adopted" krineia\_required: true trust\_root\_mode: "deployment\_asserted" receipt\_chain\_required\_for: - "canonical\_docs" - "schema\_changes" - "authority\_changes" - "release\_tags"

chains: primary: chain\_id: "arbiter-primary" storage: "\_receipts/krineia/primary.jsonl" genesis\_policy: "repo\_bootstrap" hash\_algorithm: "sha256" canonicalization: "json.dumps(sort\_keys=True,separators=(',',':'))"

operators: allowed: \["append", "project", "cut"\] forbidden: \["update", "delete", "rewrite", "summarize\_and\_replace", "score\_and\_train"\]

boundaries: no\_reward\_path\_self\_reference: true external\_analysis\_only: true observed\_agent\_may\_write\_receipts: false receipts\_may\_train\_agents: false

verification: validator: "external" required\_before\_merge: false required\_before\_release: true

related\_docs: readme: "README.md" agents: "AGENTS.md" constitution: "CONSTITUTION.md"

## last\_reviewed: "2026-06-22"

## Notes

### Chain bootstrapping

The primary chain at `_receipts/krineia/primary.jsonl` is bootstrapped with a genesis receipt recording the adoption of this manifest.
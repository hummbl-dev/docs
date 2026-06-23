# Source: https://github.com/hummbl-dev/hummbl-dev/blob/main/docs/MERGE_QUEUE_ISSUE_CLOSURE.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-dev](https://github.com/hummbl-dev/hummbl-dev)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev)
 

 

## FilesExpand file tree

 main

/

# MERGE\_QUEUE\_ISSUE\_CLOSURE.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-dev/commits/main/docs/MERGE_QUEUE_ISSUE_CLOSURE.md)

History

41 lines (30 loc) · 1.77 KB

 main

/

# MERGE\_QUEUE\_ISSUE\_CLOSURE.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

41 lines (30 loc) · 1.77 KB

[Raw](https://github.com/hummbl-dev/hummbl-dev/raw/refs/heads/main/docs/MERGE_QUEUE_ISSUE_CLOSURE.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Merge Queue Issue-Closure Semantics

## Purpose

Prevent completed work from leaving accepted issues open because a PR used non-closing language such as "Addresses #123" when the PR actually satisfied the issue.

## Required Merge Check

Before merging a PR that references an issue, classify the reference:

| Reference | Meaning | Merge action |
| --- | --- | --- |
| `Closes #N`, `Fixes #N`, `Resolves #N` | PR fully satisfies the issue acceptance criteria. | Merge normally; confirm the issue closes after merge. |
| `Addresses #N` | PR materially advances the issue but may not complete all acceptance criteria. | Merge only if the issue should remain open or update the PR/body before merge. |
| `Refs #N`, `Related #N` | Context only. | Do not expect issue closure. |

## Reviewer Checklist

- Identify every issue reference in the PR title, body, and final merge message.
- Compare the PR diff against the issue acceptance criteria.
- If the PR fully satisfies the issue, require closing language before merge.
- If the PR is partial, keep `Addresses`/`Refs` and leave a comment naming the remaining acceptance criteria.
- After merge, verify that the expected issue state matches the reference type.

## Examples From 2026-05-13 Sweep

- `crab#7` completed `crab#5` but needed manual closure because the PR used non-closing language.
- `autoresearch-reports#4` completed `autoresearch-reports#1` but needed manual closure after merge.
- `claude-config#3` intentionally did not close `claude-config#1` because the legacy skill-frontmatter migration remained open and was tracked separately.

## Default Rule

If the merge captain is unsure whether a PR completes the issue, keep the issue open and add a comment that names the unresolved criteria. Do not silently rely on "Addresses" to mean "done."
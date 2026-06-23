# Source: https://github.com/hummbl-dev/arbiter/blob/main/AUDIT_PLAN.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# AUDIT\_PLAN.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/AUDIT_PLAN.md)

History

208 lines (155 loc) · 8.26 KB

 main

/

# AUDIT\_PLAN.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

208 lines (155 loc) · 8.26 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/AUDIT_PLAN.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Arbiter Fleet Audit Plan — 59 Repos (v2)

**Date:** 2026-03-19 (revised after v0.1 lessons) **Target:** All 59 hummbl-dev repositories **Lessons applied:** CI-first validation, real-repo calibration, fleet-first design, infrastructure probing

---

## Pre-Audit: Arbiter v0.2 (required before fleet scan)

v0.1 was built for single-repo demo. Fleet audit needs these changes first.

### Must-fix before audit

| Fix | Why | LOC |
| --- | --- | --- |
| Add `repo_name` to SQLite schema | v0.1 stores file paths but not which repo they belong to — fleet query impossible | ~30 |
| Add `arbiter audit-fleet <dir>` command | Scans all subdirectories, one pass, shared database | ~80 |
| Add `arbiter fleet-report` command | Ranked table of all repos by score | ~40 |
| Add `--exclude-paths` config | v0.1 duplication analyzer produced 128K findings on founder-mode because it scanned vendored/generated code | ~30 |
| Raise duplication minimum body size | 3 statements too low — produces noise. Raise to 5+ | ~5 |
| Add `.gitignore` with `*.db` from day one | v0.1 accidentally committed 4 database files | Already done |

### Must-verify before audit

| Check | How | Why |
| --- | --- | --- |
| CI green on Arbiter | `gh run list --repo hummbl-dev/arbiter --limit 1` | v0.1 went 0/3 on CI; now green |
| Scoring formula calibrated | Run against arbiter + agentic-patterns + founder-mode, verify grades make sense | v0.1 scored itself D before tuning |
| Disk space sufficient | `df -h ~` — need ~500MB for 53 shallow clones | MBP has critically low disk |

---

## Repo Tiers

### Tier 1: Active Product — audit thoroughly, CI gate, ongoing monitoring (9 repos)

| Repo | Language | Size | Last Active |
| --- | --- | --- | --- |
| founder-mode | Python | 10.8MB | Today |
| agentic-patterns | Python | 19KB | Today |
| arbiter | Python | 33KB | Today |
| base120 | Python | 348KB | 2026-02-26 |
| mcp-server | TypeScript | 1.3MB | 2026-03-11 |
| aaa | Python | 190KB | 2026-03-02 |
| hummbl-agent | TypeScript | 1.7MB | 2026-03-16 |
| peptide-checker | Python | 22KB | 2026-03-15 |
| hummbl-governance | Python | 78KB | 2026-03-03 |

### Tier 2: Active Infrastructure — audit once, monthly spot-check (11 repos)

| Repo | Language | Size | Last Active |
| --- | --- | --- | --- |
| hummbl-monorepo | TypeScript | 65MB | 2026-03-17 |
| hummbl-production | HTML | 2.3MB | 2026-03-15 |
| hummbl | Python | 140KB | 2026-03-15 |
| OpenAgent | Python | 3.7MB | 2026-03-01 |
| autoresearch-win-rtx | Python | 499KB | 2026-03-15 |
| governed-iac-reference | Shell | 322KB | 2026-03-09 |
| forge | Python | 46KB | 2026-03-05 |
| hybrid-inference | Python | 65KB | 2026-03-01 |
| hummbl-bibliography | TeX | 279KB | 2026-03-05 |
| init-system | Shell | 37KB | 2026-02-27 |
| agent-os | Python | 106KB | 2026-02-22 |

### Tier 3: Legacy / Reference — baseline score, then ignore (33 repos)

Everything else. No commits in 30+ days or no analyzable code.

### Tier 4: Empty — skip (6 repos)

discovery, docs, god-mode, hummbl-gaas-platform, mirror-agent, rpbx

---

## Execution Plan

### Phase 0: Arbiter v0.2 Upgrades (1 session, before anything else)

1. Add `repo_name` column to all SQLite tables
2. Add `audit-fleet` command that walks a directory of repos
3. Add `fleet-report` command with ranked output
4. Add `--exclude-paths` flag (default: `node_modules,__pycache__,.venv,dist,build`)
5. Raise duplication minimum body to 5 statements
6. **Run against arbiter, agentic-patterns, and founder-mode to calibrate**
7. **Verify CI green before proceeding**

### Phase 1: Clone All Repos (30 min, scripted)

```shell
mkdir -p ~/arbiter-audit/repos
cd ~/arbiter-audit

# Shallow clone all non-empty repos (saves disk)
gh repo list hummbl-dev --limit 100 --json name,diskUsage \
  --jq '.[] | select(.diskUsage > 0) | .name' | \
  while read repo; do
    echo "Cloning $repo..."
    gh repo clone "hummbl-dev/$repo" "repos/$repo" -- --depth 1 --quiet 2>/dev/null
  done

echo "Cloned $(ls repos/ | wc -l) repos"
```

**Pre-check:** `df -h ~` — verify 500MB+ free. If not, clone to Windows Desktop instead.

### Phase 2: Baseline Audit — Python Repos First (automated, ~1 hour)

```shell
cd ~/arbiter-audit
PYTHONPATH=/Users/others/PROJECTS/arbiter/src \
  python -m arbiter audit-fleet repos/ --db fleet.db
```

This scores all 20 Python repos in one pass. TypeScript/Shell/Go repos get a "no analyzer" flag — not scored, not failed.

**Immediately after:** Check scores make sense. If any repo scores 0 or 100 unexpectedly, investigate before proceeding.

### Phase 3: Fleet Report (10 min)

```shell
python -m arbiter fleet-report --db fleet.db
```

Output:

```
HUMMBL Fleet Quality Report — 2026-03-20
========================================

Repo                    Score  Grade  Findings  LOC    Top Agent
----                    -----  -----  --------  ---    ---------
arbiter                 100.0  A           0    2,099  claude
agentic-patterns         89.0  B           9    1,438  claude
aaa                      85.0  B          12    1,200  claude
peptide-checker          ??    ??         ??      ??   ??
...

Fleet Summary: 20 scored | 6 A | 8 B | 4 C | 2 D | 0 F
Agent Leaderboard: claude avg=88, codex avg=82, gemini avg=64, human avg=79
```

### Phase 4: Triage (30 min, human decision)

| Bucket | Criteria | Action |
| --- | --- | --- |
| **Green** (A/B) | Score >= 80 | No action. Add CI gate for Tier 1 repos. |
| **Yellow** (C) | Score 60-79 | Review top 5 findings. Schedule cleanup if active repo. |
| **Red** (D/F) | Score < 60 | Is this repo still needed? If yes: remediate. If no: archive. |
| **Archive** | No commits 90+ days AND score < 70 | `gh repo archive hummbl-dev/<name>` |
| **No Code** | No analyzable language | Flag and skip. |

### Phase 5: Ongoing Monitoring

**Tier 1 (9 repos):** Add Arbiter GitHub Action — runs on every push, blocks merge below threshold.

**Tier 2 (11 repos):** Monthly cron on Windows Desktop:

```shell
cd ~/arbiter-audit && git -C repos/<name> pull && python -m arbiter analyze repos/<name> --db fleet.db
```

**Tier 3 (33 repos):** One-time baseline only. Re-audit only if repo is revived.

---

## Language Coverage

| Language | Repos | Arbiter Status | Gap |
| --- | --- | --- | --- |
| **Python** | 20 | Full (ruff + duplication; radon/bandit/vulture in Docker) | None |
| **TypeScript** | 9 | Not covered | Need eslint analyzer (Phase 2 enhancement) |
| **Shell** | 5 | Not covered | Need shellcheck analyzer (low priority) |
| **JavaScript** | 3 | Not covered | Covered when eslint added |
| **HTML** | 2 | Skip | Not scorable code |
| **Go** | 1 | Not covered | Need go vet (1 repo, low priority) |
| **TeX** | 1 | Skip | Bibliography, not code |
| **none** | 18 | Skip | Config/docs repos |

**Phase 2 audit covers 20 Python repos (34% of fleet, ~90% of active code).** TypeScript coverage (9 repos) is the highest-value gap for a future session.

---

## Risk Mitigations (lessons from v0.1)

| Risk | Mitigation |
| --- | --- |
| CI breaks on new repo setup | Verify CI green after first push before proceeding to audit |
| Scoring formula produces nonsense grades | Calibrate against 3 known repos before fleet scan |
| Disk space insufficient for 53 clones | Shallow clone (`--depth 1`) + check `df -h` first; fallback to Windows Desktop |
| Duplication analyzer produces 100K+ noise | Raise minimum body size + exclude vendored paths |
| `git add -A` commits audit databases | `.gitignore *.db` already in place |
| Stale Tailscale IP breaks nodezero access | Audit runs locally or on Windows Desktop, not nodezero |
| Fleet scan takes too long | Python-only first pass (~1 hour); TypeScript deferred |

---

## Timeline

| Phase | Work | Time | Prerequisite |
| --- | --- | --- | --- |
| 0: Arbiter v0.2 | Multi-repo mode + calibration | 1 session | None |
| 1: Clone repos | Shallow clone 53 repos | 30 min | Disk space check |
| 2: Baseline audit | Score all 20 Python repos | ~1 hour (automated) | Phase 0 + 1 |
| 3: Fleet report | Generate ranked table | 10 min | Phase 2 |
| 4: Triage | Green/Yellow/Red/Archive decisions | 30 min (human) | Phase 3 |
| 5: CI gates | Add GitHub Action to Tier 1 repos | 1 session | Phase 4 |
| 6: TypeScript | Add eslint analyzer | 1 session | Phase 5 (optional) |

**Total: 2 sessions for full Python audit + report. 1 more for TypeScript.**
# Source: https://github.com/hummbl-dev/hummbl-dev/raw/refs/heads/main/docs/research/ai-slop-crisis/README.md

\# AI Slop Crisis Research Corpus

\*\*Purpose\*\*: Evidence backbone for HUMMBL's market positioning, pitch materials, and sales conversations.

\*\*Scope\*\*: 5 research rounds, 12 parallel lanes, ~440K tokens of primary-source analysis and synthesis. Material claims are intended to be source-traceable, but high-stakes reuse should still be rechecked against the cited primary material.

\*\*Period\*\*: April 2026

---

## Evidence posture

This corpus is a \*\*research and positioning surface\*\*, not self-authenticating canon.

- Some documents are closest to primary-source-backed synthesis.
- Some are pitch, conversion, or narrative derivatives built from that synthesis.
- Snapshot numbers, regulatory timing, enforcement dates, and market claims may drift after publication.

Use the repo-level \[Proof and Research Evidence Posture\](../../PROOF\_AND\_RESEARCH\_EVIDENCE\_POSTURE.md) before reusing claims externally.

This corpus is \*\*not legal advice\*\*. Legal, regulatory, insurance, and compliance claims should be rechecked against the primary material before publication, contracts, diligence, or formal counsel-facing use.

---

## Start here

- \*\*For executive summary\*\*: \`06\_round5\_synthesis.md\` (most recent, absorbs prior 4 rounds)
- \*\*For pitch\*\*: \`capability\_brief.md\`, \`one\_pager\_defense\_federal.md\`
- \*\*For narrative hook\*\*: \`01\_round1\_37k\_lines\_of\_slop.md\`
- \*\*For hard numbers\*\*: \`03\_round3\_hard\_data\_sweep.md\`

---

## Full index

### Rounds 1-3: Foundational research (external authorship, synthesized)

| # | Doc | Role | Key content |
|---|-----|------|-------------|
| 01 | \`01\_round1\_37k\_lines\_of\_slop.md\` | Narrative hook | 10-insight qualitative breakdown of the Scott / Ishwar Jha / GStack critique |
| 02 | \`02\_round2\_crisis\_synthesis.md\` | Qualitative argument | 10 sources, tragedy-of-commons, skill atrophy, market convergence |
| 03 | \`03\_round3\_hard\_data\_sweep.md\` | Quantitative evidence | 14 stats, 5 named CVEs, EU AI Act specifics |

### Round 4: Self-identified gap closure (Claude Code swarm, 6 lanes)

| # | Doc | Lane |
|---|-----|------|
| 04 | \`04\_round4\_synthesis.md\` | Master synthesis |
| 04a | \`04a\_round4\_us\_regulatory.md\` | US federal + state + sector + insurance |
| 04b | \`04b\_round4\_competitive\_intel.md\` | 10 governance vendors + white space |
| 04c | \`04c\_round4\_incident\_harvest.md\` | 17 new verified incidents + taxonomy |
| 04d | \`04d\_round4\_devsecops\_analogue.md\` | Historical timing pattern |
| 04e | \`04e\_round4\_mcp\_wedge.md\` | MCP governance wedge validation |
| 04f | \`04f\_round4\_enterprise\_spend.md\` | TAM + pricing + buyers |

### Round 5: Reviewer-identified gap closure (Sonnet-flagged, 6 lanes)

| # | Doc | Lane |
|---|-----|------|
| 05a | \`05a\_round5\_primary\_sources.md\` | METR, Baltes, Stanford, Apiiro, Sonar verified |
| 05b | \`05b\_round5\_steelman\_roi.md\` | Pro-AI case + anti-governance steelman |
| 05c | \`05c\_round5\_legal\_liability.md\` | Liability chain + Moffatt + Mobley |
| 05d | \`05d\_round5\_observability\_analogue.md\` | Pre-Datadog → post-Datadog fully developed |
| 05e | \`05e\_round5\_regulated\_verticals.md\` | Healthcare + finance + defense compound |
| 05f | \`05f\_round5\_buyer\_hiring\_benchmarks.md\` | CTO/CISO voice + labor shifts + SWE-bench inversion |
| 06 | \`06\_round5\_synthesis.md\` | Master synthesis |

### Derived artifacts

| Doc | Purpose |
|-----|---------|
| \`capability\_brief.md\` | HUMMBL capability brief — single-doc pitch reference |
| \`one\_pager\_defense\_federal.md\` | Positioning one-pager for defense / federal buyers (primary wedge) |

---

## Top 10 high-signal findings

1. \*\*42% of code is AI-generated\*\* (Sonar 2026 survey, n=1,100+)
2. \*\*AI code is 2.74× more vulnerable\*\* than human-written (Veracode 2025)
3. \*\*Security pass rate stuck at ~55% for 2 years\*\* despite model improvement (Veracode Spring 2026)
4. \*\*25.1% of AI code samples had confirmed vulnerabilities\*\* (AppSec Santa, 6 LLMs, 534 samples)
5. \*\*SWE-bench is inverted\*\*: Claude Opus 4.6 = 79.3% Verified but 29.2% vulnerable; GPT-5.2 = 19.1% vulnerable
6. \*\*METR RCT\*\*: experienced devs 19% SLOWER with AI, believe they're 20% faster (arxiv 2507.09089)
7. \*\*Moffatt v. Air Canada\*\*: deploying company eats AI chatbot liability
8. \*\*Mobley v. Workday\*\*: vendor-as-agent liability theory certified July 2025
9. \*\*EU AI Act Aug 2 2026\*\*: €35M / 7% global revenue penalties, enforcement live in Finland since Jan 2026
10. \*\*Berkley absolute AI exclusions\*\*: no D&O/E&O coverage for AI-related claims → insurance as de-facto enforcement

---

## Strongest single positioning lines

\*\*For ROI skeptics\*\*: \*"Concede the 40-60% greenfield/junior gain. Governance is about what an agent is allowed to do, not whether it codes correctly. A perfectly-aligned agent with unlimited authority is still a catastrophic-blast-radius risk."\*

\*\*For legal/GC\*\*: \*"Signed delegation tokens and append-only audit logs are a Caremark affirmative defense, a NIST AI RMF conformance record, and a reasonable-care evidence pack, generated at runtime, not reconstructed after the breach."\*

\*\*For defense/federal CISOs\*\*: \*"Commercial AI governance SaaS may not be the right fit for IL4/IL5 profiles. HUMMBL is intended to work where classified workloads can deploy — with stdlib-first posture, air-gap capable options, contract-defined controls, and CMMC-friendly traceability."\*

\*\*For pitch decks\*\*: \*"AI generation is becoming commoditized in many contexts. Differentiation often accrues to the layer that governs output quality, enforces policy, tracks provenance, and maintains accountability. This is the observability argument applied to AI."\*

---

## Methodology notes

- All primary-source citations verified in Round 5 Lane G
- 2 citations corrected in Rounds 1-3 based on verification (see \`06\_round5\_synthesis.md\` Part I)
- Research production: Claude Opus 4.6 (Claude Code) orchestrating 12 parallel general-purpose research agents
- Research authorship: Claude Sonnet 4.6 extended (via claude.ai browser) for Rounds 1-3; Claude Opus 4.6 with swarm agents for Rounds 4-5

---

\*Last updated: 2026-04-05. Next review: quarterly, or when EU AI Act Aug 2 2026 enforcement begins.\*
# Source: https://github.com/hummbl-dev/hummbl-dev/commits/main/CONTRIBUTING.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-dev](https://github.com/hummbl-dev/hummbl-dev)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-dev)
 

 

## Breadcrumbs

History for

on[main](https://github.com/hummbl-dev/hummbl-dev/tree/main)

## User selector

All users

## Datepicker

All time

## Commit History

### Commits on Jun 13, 2026

- #### [docs: finalize hummbl-dev public proof and publish-readiness (](https://github.com/hummbl-dev/hummbl-dev/commit/e774acb7948bacf9db22585431c63775aeac561c 'docs: finalize hummbl-dev public proof and publish-readiness (#31)
 
 * docs: define issue closure merge checks
 
 * docs: add HUMMBL IaC strategic roadmap
 
 * docs: add dependency tier taxonomy for all HUMMBL repos
 
 Defines five tiers (Absolute Stdlib → Unrestricted) with clear
 criteria, indicators in pyproject.toml/README, and an admission
 process for Tier 2. Cross-language equivalents included.
 
 Maps all ~25 active repos to their correct tier and flags gaps:
 - hummbl-bus, hummbl-clp, hummbl-contracts need tier decisions
 before PyPI publish
 - evidence-gate needs admission packet before importing c2pa-python
 - hummbl-crucible should split into Tier 1 core + Tier 3 web
 
 Refs ROADMAP.md §2 Q12-13 (stdlib-first / zero-deps)
 
 Generated with [Devin](https://cli.devin.ai/docs)
 
 Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>
 
 * docs: correct evidence-gate tier and audit table gaps
 
 - evidence-gate is Tier 0 (TOML rule library, no runtime deps),
 not Tier 2; c2pa admission is for a future founder-mode module
 - Fix duplicate mcp-server line in Tier 2 table
 - Update current state audit: crab, hummbl-bus, hummbl-clp,
 hummbl-contracts, hummbl-crucible now have confirmed tiers
 
 Generated with [Devin](https://cli.devin.ai/docs)
 
 Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>
 
 * docs: harden hummbl-dev billboard and proof surfaces
 
 * docs: finalize publish-readiness links and add public checklist
 
 * docs: fix missing internal doc references in mobile standards
 
 * fix: correct archived repo count from 2 to 20
 
 README.md and inventory file had stale archived count (2) vs
 GitHub API (20). Corrected both files and added correction
 note to inventory header.
 
 ---------
 
 Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>') [#31](https://github.com/hummbl-dev/hummbl-dev/pull/31) [)](https://github.com/hummbl-dev/hummbl-dev/commit/e774acb7948bacf9db22585431c63775aeac561c 'docs: finalize hummbl-dev public proof and publish-readiness (#31)
 
 * docs: define issue closure merge checks
 
 * docs: add HUMMBL IaC strategic roadmap
 
 * docs: add dependency tier taxonomy for all HUMMBL repos
 
 Defines five tiers (Absolute Stdlib → Unrestricted) with clear
 criteria, indicators in pyproject.toml/README, and an admission
 process for Tier 2. Cross-language equivalents included.
 
 Maps all ~25 active repos to their correct tier and flags gaps:
 - hummbl-bus, hummbl-clp, hummbl-contracts need tier decisions
 before PyPI publish
 - evidence-gate needs admission packet before importing c2pa-python
 - hummbl-crucible should split into Tier 1 core + Tier 3 web
 
 Refs ROADMAP.md §2 Q12-13 (stdlib-first / zero-deps)
 
 Generated with [Devin](https://cli.devin.ai/docs)
 
 Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>
 
 * docs: correct evidence-gate tier and audit table gaps
 
 - evidence-gate is Tier 0 (TOML rule library, no runtime deps),
 not Tier 2; c2pa admission is for a future founder-mode module
 - Fix duplicate mcp-server line in Tier 2 table
 - Update current state audit: crab, hummbl-bus, hummbl-clp,
 hummbl-contracts, hummbl-crucible now have confirmed tiers
 
 Generated with [Devin](https://cli.devin.ai/docs)
 
 Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>
 
 * docs: harden hummbl-dev billboard and proof surfaces
 
 * docs: finalize publish-readiness links and add public checklist
 
 * docs: fix missing internal doc references in mobile standards
 
 * fix: correct archived repo count from 2 to 20
 
 README.md and inventory file had stale archived count (2) vs
 GitHub API (20). Corrected both files and added correction
 note to inventory header.
 
 ---------
 
 Co-authored-by: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>')
 
 Show description for e774acb
 
 ![hummbl-dev](https://avatars.githubusercontent.com/u/238336761?v=4&size=32)![devin-ai-integration[bot]](https://avatars.githubusercontent.com/in/811515?v=4&size=32)
 
 [hummbl-dev](https://github.com/hummbl-dev/hummbl-dev/commits?author=hummbl-dev)
 
 and
 
 [devin-ai-integration\[bot\]](https://github.com/hummbl-dev/hummbl-dev/commits?author=devin-ai-integration%5Bbot%5D)
 
 authoredJun 13, 2026
 
 [e774acb](https://github.com/hummbl-dev/hummbl-dev/commit/e774acb7948bacf9db22585431c63775aeac561c)
 
 Copy full SHA for e774acb
 

### Commits on Apr 8, 2026

- #### [fix: broken README links, remove sensitive files from public repo (](https://github.com/hummbl-dev/hummbl-dev/commit/07d2730469386bae6ed798f99058eb861485559f 'fix: broken README links, remove sensitive files from public repo (#6)
 
 * fix: broken README links, remove sensitive files from public repo
 
 - Fix 4 broken https://docs.research/ links in README.md intro paragraph
 to use relative paths (docs/research/...)
 - Remove sensitive files from tracking: FINANCIAL_PLAN.md,
 hummbl_productization_summary_v0.1.md, drafts/, job-hunt/
 - Delete orphaned manifest.json (referenced nonexistent dashboard.html)
 - Update .gitignore to prevent re-committing private files
 
 Local copies of removed files are preserved on disk.
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * fix: standardize test counts across public-facing docs
 
 - BUSINESS.md: 7,700+ → 15,000+ (founder-mode platform)
 - case-studies/base120: 7,700+ → 15,000+ (platform tests)
 - case-studies/base120: 8 modules/157 tests → 20 modules/476 tests
 (hummbl-governance current numbers)
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * feat: add tool index page and cross-navigation to all HTML tools
 
 - Create index.html landing page with card-based layout linking
 all 8 tools (5 readiness assessments, 2 reference tools, 1 business)
 - Add nav bar to all 8 HTML tool files with current-page highlighting
 - Nav bar hidden on print via @media print
 - Consistent dark theme, green accent, monospace branding
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * feat: enhance README as org profile billboard
 
 - Add Tools section surfacing all 8 HTML tools with descriptions
 - Replace unverifiable founder-mode test count with governance tools metric
 - Add About section with brief founder bio
 - All additions are publicly verifiable proof points
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * feat: add hummbl-governance case study and CONTRIBUTING.md
 
 - New case study: shipping 20 stdlib-only governance primitives
 covering design constraints, implementation approach, and results
 - Add CONTRIBUTING.md directing code contributions to project repos
 and documenting process for this portfolio repo
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 ---------
 
 Co-authored-by: Claude <noreply@anthropic.com>') [#6](https://github.com/hummbl-dev/hummbl-dev/pull/6) [)](https://github.com/hummbl-dev/hummbl-dev/commit/07d2730469386bae6ed798f99058eb861485559f 'fix: broken README links, remove sensitive files from public repo (#6)
 
 * fix: broken README links, remove sensitive files from public repo
 
 - Fix 4 broken https://docs.research/ links in README.md intro paragraph
 to use relative paths (docs/research/...)
 - Remove sensitive files from tracking: FINANCIAL_PLAN.md,
 hummbl_productization_summary_v0.1.md, drafts/, job-hunt/
 - Delete orphaned manifest.json (referenced nonexistent dashboard.html)
 - Update .gitignore to prevent re-committing private files
 
 Local copies of removed files are preserved on disk.
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * fix: standardize test counts across public-facing docs
 
 - BUSINESS.md: 7,700+ → 15,000+ (founder-mode platform)
 - case-studies/base120: 7,700+ → 15,000+ (platform tests)
 - case-studies/base120: 8 modules/157 tests → 20 modules/476 tests
 (hummbl-governance current numbers)
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * feat: add tool index page and cross-navigation to all HTML tools
 
 - Create index.html landing page with card-based layout linking
 all 8 tools (5 readiness assessments, 2 reference tools, 1 business)
 - Add nav bar to all 8 HTML tool files with current-page highlighting
 - Nav bar hidden on print via @media print
 - Consistent dark theme, green accent, monospace branding
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * feat: enhance README as org profile billboard
 
 - Add Tools section surfacing all 8 HTML tools with descriptions
 - Replace unverifiable founder-mode test count with governance tools metric
 - Add About section with brief founder bio
 - All additions are publicly verifiable proof points
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 * feat: add hummbl-governance case study and CONTRIBUTING.md
 
 - New case study: shipping 20 stdlib-only governance primitives
 covering design constraints, implementation approach, and results
 - Add CONTRIBUTING.md directing code contributions to project repos
 and documenting process for this portfolio repo
 
 https://claude.ai/code/session_01G5tojHxos9u7r8bQ9c11T2
 
 ---------
 
 Co-authored-by: Claude <noreply@anthropic.com>')
 
 Show description for 07d2730
 
 ![hummbl-dev](https://avatars.githubusercontent.com/u/238336761?v=4&size=32)![claude](https://avatars.githubusercontent.com/u/81847?v=4&size=32)
 
 [hummbl-dev](https://github.com/hummbl-dev/hummbl-dev/commits?author=hummbl-dev)
 
 and
 
 [claude](https://github.com/hummbl-dev/hummbl-dev/commits?author=claude)
 
 authoredApr 8, 2026
 
 [07d2730](https://github.com/hummbl-dev/hummbl-dev/commit/07d2730469386bae6ed798f99058eb861485559f)
 
 Copy full SHA for 07d2730
 

Loading
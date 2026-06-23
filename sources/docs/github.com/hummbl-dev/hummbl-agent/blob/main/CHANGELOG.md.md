# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/CHANGELOG.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# CHANGELOG.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/CHANGELOG.md)

History

34 lines (23 loc) · 1.31 KB

 main

/

# CHANGELOG.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

34 lines (23 loc) · 1.31 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/CHANGELOG.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## \[Unreleased\]

### Added

- E2E validation pipeline fixes (.js → .cjs extensions)
- TypeScript test file guard (`scripts/lint-no-ts-tests.sh`)
- Test policy enforcement (`.test.mjs` only, no runtime TS loaders)
- CI workflow updated to enforce test policy
- Comprehensive governance documentation (SECURITY.md, ARCHITECTURE.md, GOVERNANCE.md, CONTRIBUTING.md)
- Enterprise governance modes plan (`docs/plans/2026-02-04-governance-modes-design.md`)
- Operational reports for API integration, mission-critical validation, and runtime tests (`docs/reports/*.md`)

### Changed

- Router tests converted to `.test.mjs` format (skipped pending build infrastructure)
- AGENTS.md updated with explicit test policy enforcement section
- GitHub Actions CI workflow updated to match test policy
- README now links to governance plan and centralized operational reports

### Fixed

- Base120 validator script extensions in `scripts/e2e-validate.sh`
- E2E validation pipeline now passes all checks

## Previous Changes

See git log for detailed history before governance documentation was established.
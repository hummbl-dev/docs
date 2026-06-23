# Source: https://github.com/hummbl-dev/arbiter/blob/main/SECURITY.md

[hummbl-dev](https://github.com/hummbl-dev) / **[arbiter](https://github.com/hummbl-dev/arbiter)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
- [Star 0](https://github.com/login?return_to=%2Fhummbl-dev%2Farbiter)
 

 

## FilesExpand file tree

 main

/

# SECURITY.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/arbiter/commits/main/SECURITY.md)

History

48 lines (34 loc) · 1.71 KB

 main

/

# SECURITY.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

48 lines (34 loc) · 1.71 KB

[Raw](https://github.com/hummbl-dev/arbiter/raw/refs/heads/main/SECURITY.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Security Policy

## Supported Versions

Only released versions of Arbiter receive security fixes. The table below describes the level of support you can expect for each release line.

| Version | Supported | Security Fixes |
| --- | --- | --- |
| 0.6.x | ✅ | Active fixes |
| 0.5.x | ✅ | Critical only |
| < 0.5 | ❌ | No fixes |

"Critical only" means fixes are limited to high-severity issues (e.g. remote code execution, data exposure) and do not include lower-severity hardening. Unsupported versions should upgrade to a supported release to receive fixes.

## Reporting a Vulnerability

If you discover a security issue in Arbiter, email `reuben@hummbl.io` with:

- affected version or commit
- reproduction steps
- expected and observed behavior
- potential impact

Do not open public GitHub issues for suspected vulnerabilities.

## Scope

This policy covers the code and release artifacts in this repository.

## Response SLA

We aim to acknowledge and remediate security reports according to the following targets. These are best-effort commitments, not guarantees, and may vary with report volume and severity.

| Stage | Target |
| --- | --- |
| Acknowledgement of report | Within 48 hours |
| Initial assessment & severity rating | Within 5 business days |
| Remediation (Critical) | Patch or mitigation within 7 days of confirmation |
| Remediation (High) | Patch or mitigation within 30 days of confirmation |
| Remediation (Medium/Low) | Addressed in the next scheduled release |

You will receive status updates at each stage. If a fix requires coordinated disclosure, we will work with you to agree on a publication timeline.
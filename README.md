# HUMMBL Public Documentation

This repository is the **canonical public documentation source-of-record** for HUMMBL AI governance infrastructure. It is built with [Mintlify](https://mintlify.com) and deployed from the default branch.

## What lives here

- Public docs for HUMMBL governance primitives, compliance frameworks, Base120, tools, and REST API
- `docs.json` — Mintlify site configuration (navigation, theme, branding)
- `*.mdx` — documentation source pages
- `docs/adr/` — public architecture decision records

## Local preview

Install the [Mintlify CLI](https://www.npmjs.com/package/mint):

```bash
npm i -g mint
```

Run the dev server from the repo root (where `docs.json` is located):

```bash
mint dev
```

Preview at `http://localhost:3000`.

## Publishing changes

Changes pushed to `main` are deployed to production automatically via the Mintlify GitHub App. **Do not push to `main` without review.** All public-facing claims must pass the claim-evidence policy before publication.

### Validation gate

A CI workflow (`.github/workflows/validate-docs.yml`) runs on every PR and push to `main`:

1. **Navigation integrity** — `python3 scripts/validate_docs.py` checks every `docs.json` page reference resolves to an existing `.mdx` file
2. **Claim-surface check** — `python3 scripts/check_claims.py` flags stale quantitative claims (test counts, primitive counts, compliance frameworks, API endpoints)

Both scripts are reproducible locally by agents. Run them before pushing to `main`.

### Claim-evidence policy

Public docs that make compliance, primitive-count, test-count, or product capability claims must cite the internal evidence ledger or current primary source. See:

- `hummbl-dev/hummbl-governance` — governance primitives source
- `hummbl-dev/founder-mode` — integration testbed and canonical test counts
- `hummbl-dev/claim-evidence-ledger` — claim tracking

## Related surfaces

- [`hummbl-dev/mintlify-docs`](https://github.com/hummbl-dev/mintlify-docs) — staging/experimental docs surface
- [`hummbl-dev/hummbl-dev`](https://github.com/hummbl-dev/hummbl-dev) — org-level README and public metadata
- [`hummbl-dev/hummbl-production`](https://github.com/hummbl-dev/hummbl-production) — production deployment configs

## Contributing

1. Create a branch from `main`.
2. Edit `.mdx` files or `docs.json`.
3. Preview locally with `mint dev`.
4. Open a PR. Ensure no unverified claims are introduced.
5. After review and merge, changes deploy automatically.

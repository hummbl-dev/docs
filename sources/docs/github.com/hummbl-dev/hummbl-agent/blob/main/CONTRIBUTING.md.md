# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/CONTRIBUTING.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# CONTRIBUTING.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/CONTRIBUTING.md)

History

218 lines (155 loc) · 4.58 KB

## FilesExpand file tree

 main

/

# CONTRIBUTING.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

218 lines (155 loc) · 4.58 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/CONTRIBUTING.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# CONTRIBUTING

## Welcome

Thank you for contributing to HUMMBL Agent! This document guides you through the contribution process.

## Getting Started

### Prerequisites

- Node.js 20+
- Corepack-enabled pnpm 9.14.4 for root and workspace commands
- Git
- Familiarity with TypeScript and shell scripting
- Understanding of governed execution concepts

### Setup

```shell
# Clone repository
git clone https://github.com/hummbl-dev/hummbl-agent.git
cd hummbl-agent

# Install dependencies from the workspace root
corepack enable
pnpm install

# Run validation
bash scripts/e2e-validate.sh --mode offline
```

## Contribution Workflow

### 1\. Choose an Issue

- Browse open issues
- Comment to claim an issue
- Ask questions if unclear
- Respect existing assignments

### 2\. Create a Branch

```shell
# Update main
git checkout main
git pull origin main

# Create feature branch
git checkout -b type/agent/short-desc
# or
git checkout -b fix/description
```

**Branch naming:**

- `type/agent/short-desc` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation
- `test/description` - Test additions
- `chore/description` - Maintenance

### 3\. Make Changes

**Follow repository guidelines:** See `AGENTS.md`

**Key rules:**

- Two-space indentation
- Named exports (ESM)
- Tests in `.test.mjs` format only
- Descriptive commit messages
- No secrets committed

### 4\. Test Your Changes

```shell
# From the workspace root
pnpm run lint:schemas
pnpm run test:schemas

# Run lints
node scripts/lint-esm.mjs
bash scripts/lint-secret-scan.sh
bash scripts/lint-no-ts-tests.sh

# Run tests
node --test packages/adapters/llm/tests/*.test.mjs
node --test packages/router/tests/*.test.mjs

# Package-local npm scripts are valid inside packages that own them
cd packages/control-plane && npm test
cd packages/router && npm test

# Full validation
bash scripts/e2e-validate.sh --mode offline
```

**Required:** All checks must pass before PR.

### 5\. Commit Changes

**Commit message format:** Conventional Commits

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `test`: Tests
- `chore`: Maintenance
- `refactor`: Code restructure

**Scopes:** Top-level directories

- `kernel`, `router`, `adapters`, `skills`, `runners`
- `scripts`, `docs`, `configs`
- `llm`, `communication`, `process`

**Examples:**

```shell
git commit -m "feat(llm): add openai adapter with governed guard"
git commit -m "fix(router): correct vendor selection logic"
git commit -m "docs(security): clarify secret management policy"
git commit -m "test(adapters): add communication adapter tests"
```

### 6\. Push and Create PR

```shell
# Push branch
git push origin type/agent/short-desc

# Create PR on GitHub
# Fill out PR template
```

**PR title:** Same format as commit messages

**PR description must include:**

- Summary of changes
- Linked issue (e.g., "Closes #123")
- Test results (paste e2e-validate output)
- Breaking changes (if any)
- Decision doc reference (for Category 2+ changes)

### 7\. Address Review Feedback

- Respond to all comments
- Make requested changes
- Re-run tests after changes
- Push additional commits (no force push during review)
- Request re-review when ready

### 8\. Merge

- Maintainer will merge after approval
- Squash or rebase may be used
- Delete branch after merge

## Common Pitfalls

### Don't

- ❌ Commit secrets or API keys
- ❌ Use `.test.ts` files (use `.test.mjs`)
- ❌ Modify vendor code (read-only)
- ❌ Skip CI checks ("will fix later")
- ❌ Force push during review
- ❌ Mix multiple concerns in one PR
- ❌ Use runtime TypeScript loaders

### Do

- ✅ Run `scripts/e2e-validate.sh` before PR
- ✅ Write descriptive commit messages
- ✅ Update tests with code changes
- ✅ Document significant decisions
- ✅ Ask questions if unclear
- ✅ Respond to review feedback promptly
- ✅ Use governed execution patterns

## Getting Help

### Resources

- **Architecture:** `ARCHITECTURE.md`
- **Governance:** `GOVERNANCE.md`
- **Security:** `SECURITY.md`
- **Repository guidelines:** `AGENTS.md`
- **Validation checklist:** `docs/validation-checklist.md`

### Communication

- **Issues:** Ask questions in issue comments
- **Discussions:** Start GitHub Discussion for proposals
- **PRs:** Use PR comments for code-specific questions
- **Security:** Email [security@hummbl.dev](mailto:security@hummbl.dev) for vulnerabilities

## Recognition

Contributors are recognized in:

- Git commit history
- PR author attribution
- `CHANGELOG.md` (for significant contributions)
- Security advisories (for vulnerability reports)

Thank you for contributing to HUMMBL Agent!
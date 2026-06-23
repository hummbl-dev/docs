# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/TROUBLESHOOTING.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# TROUBLESHOOTING.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/TROUBLESHOOTING.md)

History

511 lines (366 loc) · 13.5 KB

 main

/

# TROUBLESHOOTING.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

511 lines (366 loc) · 13.5 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/TROUBLESHOOTING.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# HUMMBL Troubleshooting Guide

Diagnostic guide for common issues in hummbl-production API and hummbl-agent runtime.

## Quick Diagnosis

```shell
# 1. API Responsive?
curl -s https://hummbl-api.hummbl.workers.dev/health | jq .

# 2. Agents Running?
cd /path/to/hummbl-agent && node dashboard.js

# 3. Recent Errors?
node monitor.js | tail -20

# 4. API Consumption Normal?
node api-monitor.js | head -15
```

---

## API Issues

### API Not Responding (503/Timeout)

**Diagnosis:**

```shell
curl -v https://hummbl-api.hummbl.workers.dev/health
# Expected: HTTP/1.1 200 OK
# If: Connection refused or timeout
```

**Causes & Solutions:**

| Symptom | Cause | Solution |
| --- | --- | --- |
| `curl: (7) Failed to connect` | Cloudflare Workers down or DNS broken | Check Cloudflare status page; verify DNS: `nslookup hummbl-api.hummbl.workers.dev` |
| `HTTP 502 Bad Gateway` | Worker code error or deployment issue | Review recent GitHub Actions; check logs in Cloudflare dashboard |
| `HTTP 503 Service Unavailable` | Worker overloaded or rate limited internally | Check `rate_limit_status` in `/health`; scale workers or increase limits |
| Request timeout (>10s) | Network issue or slow handler | Check handler performance in `api/src/index.ts`; review recent changes |

**Recovery Steps:**

```shell
# 1. Check Cloudflare deployment status
# Go to: https://dash.cloudflare.com -> Workers -> hummbl-api

# 2. Check recent deployments
cd /path/to/hummbl-production
git log --oneline -10

# 3. If recent bad commit, rollback
git revert HEAD
git push origin main

# 4. Verify API recovers
for i in {1..5}; do
  curl -s https://hummbl-api.hummbl.workers.dev/health | jq '.status'
  sleep 2
done
```

---

### API Responding But Endpoints Broken

**Symptoms:**

- `/health` returns 200 but `/v1/models` fails
- Some endpoints work, others return 500
- Inconsistent behavior across endpoints

**Diagnosis:**

```shell
# Test each endpoint
curl https://hummbl-api.hummbl.workers.dev/health | jq '.status'
curl https://hummbl-api.hummbl.workers.dev/v1/models | jq '.models | length'
curl https://hummbl-api.hummbl.workers.dev/v1/transformations | jq '.transformations | length'
curl https://hummbl-api.hummbl.workers.dev/v1/workflows | jq '.workflows | length'
curl -X POST https://hummbl-api.hummbl.workers.dev/v1/recommend -H "Content-Type: application/json" -d '{"problem": "test"}' | jq '.recommended_models'
```

**Common Issues:**

| Endpoint | Error | Cause | Solution |
| --- | --- | --- | --- |
| `/v1/models` | 500 | `base120-canonical.json` malformed | `cd hummbl-production && npm run test:schemas` |
| `/v1/transformations` | 404 | Handler not exported | Check `api/src/handlers/transformations.ts` exists |
| `/v1/recommend` | 400 | Invalid request body | Check: `curl ... -d '{"problem": "text"}'` |
| `/v1/semantic-search` | 503 | Pinecone unavailable | Expected if no PINECONE\_API\_KEY set; should degrade gracefully |

**Fix TypeScript/Schema Issues:**

```shell
cd /path/to/hummbl-production

# 1. Check for TypeScript errors
npm run build

# 2. Validate JSON schemas
npm run test:schemas

# 3. If errors found, review recent commits
git diff HEAD~1

# 4. Fix errors and redeploy
git add .
git commit -m "fix: resolve schema validation errors"
git push origin main
```

---

### Rate Limiting Issues

**Symptoms:**

- HTTP 429 Too Many Requests
- `X-RateLimit-Remaining: 0`
- Agent requests suddenly start failing

**Diagnosis:**

```shell
# 1. Check rate limit status
curl https://hummbl-api.hummbl.workers.dev/health | jq '.rate_limit_status'
# Expected: max_requests_per_minute = 100, active_ips = 1-3

# 2. If hitting limit, check from which IP
node api-monitor.js | grep "Rate Limit"

# 3. Check recent request volume
node api-monitor.js --json | jq '.totalRequests'
```

**Causes & Solutions:**

| Cause | Check | Solution |
| --- | --- | --- |
| Agent batching too many requests | `node dashboard.js | grep "API Calls"` | Reduce concurrency in agent config |
| Multiple agents competing for same IP | `curl https://hummbl-api.hummbl.workers.dev/health | jq '.rate_limit_status.active_ips'` | Deploy agents to separate IPs or throttle |
| Rate limit too low for traffic | Monitor peak traffic times | Increase `MAX_REQUESTS_PER_MINUTE` in `api/src/middleware/rate-limit.ts` |

**Increase Rate Limit:**

```shell
cd /path/to/hummbl-production

# Edit rate limit middleware
vim api/src/middleware/rate-limit.ts
# Change: const MAX_REQUESTS_PER_MINUTE = 100;
#    To:  const MAX_REQUESTS_PER_MINUTE = 250;

# Test and deploy
npm run test:integration
git commit -am "ops: increase rate limit to 250 req/min"
git push origin main
```

---

## Agent Runtime Issues

### Agent Not Executing (No Recent Runs)

**Diagnosis:**

```shell
# 1. Check for any runs at all
ls -lh _state/runs/$(date +%Y-%m-%d)/ 2>/dev/null || echo "No runs today"

# 2. Check if agent process is alive
ps aux | grep -i soma  # For Soma
ps aux | grep -i kimi  # For kimi-code

# 3. Check for errors in process policy
cat config/process-policy.allowlist | head -20
```

**Common Causes:**

| Cause | Check | Fix |
| --- | --- | --- |
| Agent process not started | `ps aux | grep agent` | Start agent: See deployment docs |
| API unreachable from agent network | `ping -c 1 hummbl-api.hummbl.workers.dev` | Verify network policy in `config/network-policy.json` |
| Secrets not loaded | `test -f .local.json && echo "✓" || echo "✗"` | Create `.local.json` with secrets |
| Governance policy violation | `tail -100 _state/runs/*/sitrep-*.json | jq '.errors'` | Review policy in `schemas/` |

**Recovery:**

```shell
# 1. Verify API is reachable
curl https://hummbl-api.hummbl.workers.dev/health

# 2. Check network policy allows API calls
cat config/network-policy.json | jq '.allowed_hosts'

# 3. Test agent manually
# (Restart the agent process or trigger manually)

# 4. Verify run artifacts appear
ls -lh _state/runs/$(date +%Y-%m-%d)/ | tail -5
```

---

### Agent Execution Slow (High Duration\_ms)

**Diagnosis:**

```shell
# 1. Check average duration trend
node monitor.js | grep "Avg Duration"

# 2. Compare recent runs
tail -20 _state/runs/$(date +%Y-%m-%d)//sitrep-*.json | jq '{status, duration_ms, api_calls}'

# 3. Identify slowest runs
find _state/runs -name "sitrep-*.json" -exec jq '{duration_ms}' {} \; | sort -rn | head -5
```

**Common Causes:**

| Cause | Check | Solution |
| --- | --- | --- |
| API response times slow | `node api-monitor.js | grep "Avg Response"` | Production API degradation (see API issues above) |
| Skill execution bottleneck | Check SITREP step timings | Profile individual skills; optimize slow ones |
| Unbounded loops or memory allocation | `jq '.memory_used_mb' _state/runs/.../sitrep-*.json` | Review skill code for leaks |
| Network latency spike | `curl -w "time_total: %{time_total}s\n" https://hummbl-api.hummbl.workers.dev/health` | Investigate network path |

**Profile Slow Execution:**

```shell
# Get latest run
LATEST_RUN=$(ls -t _state/runs/$(date +%Y-%m-%d)/*/ | head -1)

# View execution timeline
cat "$LATEST_RUN/sitrep-*.json" | jq '.execution_timeline'

# Identify slow step
cat "$LATEST_RUN/sitrep-*.json" | jq '.execution_timeline | max_by(.duration_ms)'
```

---

### Agent Execution Failed (Errors in SITREP)

**Diagnosis:**

```shell
# 1. Find failed runs
find _state/runs -name "sitrep-*.json" -exec jq 'select(.status != "success") | {date, errors}' {} \;

# 2. View latest errors
ls -t _state/runs/$(date +%Y-%m-%d)/*/ | head -1 | xargs -I {} cat {}/sitrep-*.json | jq '.errors'

# 3. Check error patterns
node dashboard.js | grep -A 10 "ERROR PATTERNS"
```

**Error Type Handling:**

| Error Type | Meaning | Action |
| --- | --- | --- |
| `SCHEMA_VALIDATION_ERROR` | SITREP doesn't match schema | Check `schemas/sitrep.schema.json`; re-run with `npm run test:schemas` |
| `GOVERNANCE_VIOLATION` | Policy check failed | Review error details; check policy in `schemas/policy.schema.json` |
| `SKILL_EXECUTION_ERROR` | Skill code threw exception | Check skill implementation; review skill logs in SITREP |
| `API_ERROR` | Call to hummbl-api failed | Check API health; verify network reachability |
| `NETWORK_POLICY_ERROR` | Network call blocked by policy | Update `config/network-policy.json` allowlist |

**Fix by Error Type:**

**SCHEMA\_VALIDATION\_ERROR:**

```shell
npm run test:schemas
# Review output for mismatches
# Fix schema or update SITREP generation code
```

**GOVERNANCE\_VIOLATION:**

```shell
# View policy that was violated
cat schemas/policy.schema.json | jq '.rules'

# Adjust policy or skill behavior
vim config/*.json
git commit -am "fix: adjust policy for legitimate use case"
```

**SKILL\_EXECUTION\_ERROR:**

```shell
# Inspect error in SITREP
cat _state/runs/.../sitrep-*.json | jq '.errors[0]'

# Debug skill code
# ... review skill implementation ...
```

---

### Agent Can't Reach Production API

**Diagnosis:**

```shell
# 1. Check network policy
cat config/network-policy.json | jq '.allowed_hosts'

# 2. Verify API is reachable from agent machine
curl https://hummbl-api.hummbl.workers.dev/health

# 3. Check SITREP for network error details
cat _state/runs/.../sitrep-*.json | jq '.errors[] | select(.type == "NETWORK_POLICY_ERROR" or .type == "CONNECTIVITY_ERROR")'
```

**Fix:**

```shell
# 1. Add hummbl-api to network allowlist
cat config/network-policy.json
# Verify "hummbl-api.hummbl.workers.dev" is in allowed_hosts

# 2. If missing, update:
vim config/network-policy.json
# Add: {"host": "hummbl-api.hummbl.workers.dev", "port": 443, "protocol": "https"}

# 3. Restart agent
# (Depends on how agent is deployed)
```

---

### Secrets Not Loading (.local.json)

**Diagnosis:**

```shell
# 1. Check if secrets file exists
test -f .local.json && echo "✓ Found" || echo "✗ Missing"

# 2. Check if readable
ls -l .local.json

# 3. Verify secrets are used in agent startup
grep -r ".local.json" skills/ config/ || echo "No references found"
```

**Fix:**

```shell
# 1. Create .local.json with required secrets
cat > .local.json << 'EOF'
{
  "pinecone_api_key": "pk-...",
  "anthropic_api_key": "sk-ant-...",
  "other_secret": "value"
}
EOF

# 2. Ensure .gitignore prevents accidental commits
echo ".local.json" >> .gitignore

# 3. Verify agent loads secrets on startup
# Check SITREP for "secrets loaded" or similar message
```

---

## MCP Server Issues

### MCP Server Version Mismatch

**Symptoms:**

- Published npm v1.0.2 but source code shows v1.0.0-beta.2
- Unclear which version is actually running
- SDK version differs between npm and GitHub repo

**Diagnosis:**

```shell
# 1. Check npm version
npm view @hummbl/mcp-server version
# Expected output: 1.0.2

# 2. Check GitHub repo version
cd /path/to/mcp-server
cat package.json | jq '.version'
# Expected: Should match npm (1.0.2), but shows 1.0.0-beta.2

# 3. Check SDK version mismatch
cat package.json | jq '.dependencies."@modelcontextprotocol/sdk"'
# npm: ^1.0.0 | GitHub: ^1.25.2
```

**Current Status:**

- ✅ Published npm v1.0.2 is working for users
- ⚠️ GitHub source is out of sync
- 🔴 Cannot trace changes between versions

**Resolution Options:**

**Option A: Commit Missing Source (Recommended)**

```shell
cd /path/to/mcp-server

# 1. Update version to 1.0.2
vim package.json
# "version": "1.0.2"

# 2. Align SDK version
npm install @modelcontextprotocol/sdk@^1.0.0

# 3. Build and verify
npm run build

# 4. Commit and push
git add package.json package-lock.json
git commit -m "chore: align source with published npm v1.0.2

- Update version to 1.0.2 to match npm registry
- Align SDK dependency to ^1.0.0 for consistency
- Ensure source code reflects published package"

git push origin main
```

**Option B: Revert npm to Match Source**

```shell
# 1. Update npm to match source (v1.0.0-beta.2)
npm unpublish @hummbl/mcp-server@1.0.2

# 2. Update version to 1.0.0-beta.2
cd /path/to/mcp-server
vim package.json
# "version": "1.0.0-beta.2"

# 3. Align SDK to ^1.25.2
npm install @modelcontextprotocol/sdk@^1.25.2

# 4. Publish
npm publish

# 5. Commit to GitHub
git add package.json package-lock.json
git commit -m "chore: align npm with source version (v1.0.0-beta.2)"
git push origin main
```

**Option C: Major Version Bump (v2.0.0)**

```shell
cd /path/to/mcp-server

# 1. Update to v2.0.0
vim package.json
# "version": "2.0.0"

# 2. Document breaking changes in CHANGELOG.md

# 3. Build, test, publish
npm run build
npm run test
npm publish

# 4. Tag release
git tag v2.0.0
git push origin main --tags
```

**Recommendation:** Choose **Option A** (commit missing source). It maintains compatibility with existing users on npm v1.0.2 while syncing the source code.

---

## Performance Tuning

### Optimize API Responses

**Current Performance:**

```shell
curl -w "Response time: %{time_total}s\nStatus: %{http_code}\n" https://hummbl-api.hummbl.workers.dev/v1/models -o /dev/null -s
```

**If slow (>200ms):**

1. **Check model data size:**
 
 ```shell
    curl -s https://hummbl-api.hummbl.workers.dev/v1/models | jq '.models | length'
    # If > 500 models, consider pagination
    ```
 
2. **Enable gzip compression** in `api/src/index.ts`
 
3. **Cache models** in Cloudflare KV for faster retrieval
 
4. **Optimize JSON serialization** - use `.toJSON()` methods
 

---

## Getting Help

**Internal Resources:**

- [AGENT\_MONITORING.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/AGENT_MONITORING.md) - Monitoring guide
- [RUNBOOK.md](https://github.com/hummbl-dev/hummbl-agent/blob/main/RUNBOOK.md) - Operational procedures
- [.github/copilot-instructions.md](https://github.com/hummbl-dev/hummbl-agent/blob/.github/copilot-instructions.md) - Development guide

**External Resources:**

- Cloudflare Workers docs: [https://developers.cloudflare.com/workers/](https://developers.cloudflare.com/workers/)
- Hono framework: [https://hono.dev/](https://hono.dev/)
- Model Context Protocol: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)

**Contact:**

- Escalation: See [RUNBOOK.md#escalation](https://github.com/hummbl-dev/hummbl-agent/blob/main/RUNBOOK.md#escalation)
# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/RUNBOOK.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# RUNBOOK.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/RUNBOOK.md)

History

327 lines (236 loc) · 8.59 KB

## FilesExpand file tree

 main

/

# RUNBOOK.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

327 lines (236 loc) · 8.59 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/RUNBOOK.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# HUMMBL Operational Runbook

Operations guide for managing production deployment with Soma and kimi-code agents, plus the production API.

## Table of Contents

1. [Deployment Status](https://github.com/#deployment-status)
2. [Incident Response](https://github.com/#incident-response)
3. [Monitoring & Alerting](https://github.com/#monitoring--alerting)
4. [Common Tasks](https://github.com/#common-tasks)
5. [Troubleshooting](https://github.com/#troubleshooting)
6. [Escalation](https://github.com/#escalation)

---

## Deployment Status

### Current Production Setup

| Component | Status | Location | Endpoint |
| --- | --- | --- | --- |
| **hummbl-api** | 🟢 LIVE | Cloudflare Workers | [https://hummbl-api.hummbl.workers.dev](https://hummbl-api.hummbl.workers.dev) |
| **hummbl.io** | 🟢 LIVE | Cloudflare Pages | [https://hummbl.io](https://hummbl.io) |
| **Soma Agent** | 🟢 DEPLOYED | Runtime | Consuming `/v1/recommend` |
| **kimi-code Agent** | 🟢 DEPLOYED | Runtime | Consuming `/v1/models`, `/v1/transformations` |
| **MCP Server** | 🟢 LIVE | npm Registry | @hummbl/mcp-server@1.0.2 |

### Deployment Verification

Verify all systems are operational:

```shell
# Check API health
curl https://hummbl-api.hummbl.workers.dev/health | jq .

# Verify agents are running (from hummbl-agent root)
node dashboard.js

# Check recent agent runs
node monitor.js
```

Expected output:

- API returns status: "healthy", 120 models available
- Dashboard shows Soma & kimi-code with execution metrics
- No recent failed runs

---

## Incident Response

### Scenario 1: Production API Unresponsive

**Detection:**

- Dashboard shows API errors or red indicators
- Agent requests failing with connection timeouts
- Health check returns error or timeout

**Immediate Actions:**

```shell
# 1. Verify API endpoint
curl -I https://hummbl-api.hummbl.workers.dev/health

# 2. Check rate limiting status
curl https://hummbl-api.hummbl.workers.dev/health | jq '.rate_limit_status'

# 3. Run full health check
node api-monitor.js --check

# 4. Log metrics for analysis
node dashboard.js > /tmp/incident-status.txt
node api-monitor.js --json >> /tmp/incident-metrics.json
```

**Mitigation:**

1. **If rate-limited**: Current limit is 100 requests/minute per IP. Check if agents are overwhelming the API:
 
 ```shell
    node api-monitor.js | grep "Rate Limit"
    ```
 
 Action: Scale agents or increase rate limit in `api/src/middleware/rate-limit.ts`
 
2. **If Cloudflare Workers down**: Wait 5-10 minutes for automatic recovery. If persists:
 
 - Check Cloudflare dashboard status
 - Review recent deployments in GitHub Actions
 - Check `api/` for syntax errors in last commit
3. **If DNS/connectivity**: Check Cloudflare DNS settings for `hummbl-api.hummbl.workers.dev`
 

**Rollback (if deployed bad code):**

```shell
# Go to hummbl-production repo
cd /path/to/hummbl-production

# Identify last working commit
git log --oneline | head -10

# Revert to working version
git revert HEAD
git push origin main

# Or reset if unpushed
git reset --hard <commit-hash>
```

---

### Scenario 2: Agent Execution Failures

**Detection:**

- Dashboard shows failed run count increasing
- Monitor shows errors in "Error Patterns"
- Agent execution times spike or drop to 0

**Immediate Actions:**

```shell
# 1. Check recent agent runs
node monitor.js --watch

# 2. Review error patterns
node dashboard.js | grep -A 10 "ERROR PATTERNS"

# 3. Check agent-specific logs
ls -lh _state/runs/$(date +%Y-%m-%d)/ | tail -20

# 4. Inspect latest SITREP
cat _state/runs/$(date +%Y-%m-%d)/*/sitrep-*.json | jq '.errors'
```

**By Agent:**

**Soma Failures:**

- Check if Soma runtime process is alive
- Verify Soma can reach production API
- Review process policy allowlist in `hummbl-agent/config/process-policy.allowlist`
- Check secrets are loaded: `test -f .local.json && echo "✓ Secrets available"`

**kimi-code Failures:**

- Verify kimi-code environment setup
- Check LLM governance policies in `schemas/policy.schema.json`
- Ensure required mental models are available: `curl https://hummbl-api.hummbl.workers.dev/v1/models | jq '.models | length'`

**Mitigation:**

1. **Schema validation error**: Run schema tests:
 
 ```shell
    npm run test:schemas
    ```
 
2. **API connection error**: Verify agent network policy:
 
 ```shell
    cat config/network-policy.json | grep "api"
    ```
 
3. **Governance violation**: Check SITREP error details and policy logs
 

---

### Scenario 3: Performance Degradation

**Detection:**

- Average agent duration increases significantly
- API response times slow down
- Rate limiting kicks in unexpectedly

**Immediate Actions:**

```shell
# 1. Check current metrics
node dashboard.js

# 2. Compare to baseline (inspect metrics.json)
cat _state/metrics.json | jq '.averageDuration'

# 3. Check API response times
node api-monitor.js | grep "Avg Response"

# 4. Monitor in real-time
node monitor.js --watch
```

**Likely Causes & Solutions:**

| Cause | Check | Solution |
| --- | --- | --- |
| API overloaded | `curl https://hummbl-api.hummbl.workers.dev/health | jq '.rate_limit_status.active_ips'` | Scale agents, increase rate limit, or optimize API queries |
| Agents spawning too many requests | `node api-monitor.js | grep "Total Requests"` | Check agent config for request batching, reduce parallelism |
| Network latency | `curl -w "%{time_total}\n" https://hummbl-api.hummbl.workers.dev/health` | Check network path, consider edge caching |
| Memory leak in agent | Check `_state/runs/*/sitrep-*.json` memory usage over time | Restart agent, check for unbounded loops in skills |

---

## Monitoring & Alerting

### Daily Checks

Add to cron or daily reminders:

```shell
# 8 AM: Morning health check
0 8 * * * cd /path/to/hummbl-agent && node api-monitor.js --check > /tmp/morning-check.log

# 5 PM: End-of-day metrics export
0 17 * * * cd /path/to/hummbl-agent && node dashboard.js > /tmp/eod-status.txt
```

### Manual Monitoring (Real-time)

```shell
# Run in separate terminal for continuous monitoring
cd /path/to/hummbl-agent
node monitor.js --watch    # Shows agent executions
node api-monitor.js        # Shows API consumption
```

### Metrics to Track

**Agent Health:**

- Success rate (target: >95%)
- Average execution duration (baseline: varies by skill)
- Error frequency by type
- API calls per agent per day

**API Health:**

- Endpoint response times (target: <200ms)
- Error rate (target: <1%)
- Rate limit hits (target: 0)
- Active IPs (should be <10 in normal operation)

### Setting Up Alerts (Manual)

Create a script `alert-if-unhealthy.sh`:

```shell
#!/bin/bash
cd /path/to/hummbl-agent

# Check success rate
SUCCESS_RATE=$(node dashboard.js 2>/dev/null | grep "Success Rate" | grep -oE "[0-9]+")
if [ "$SUCCESS_RATE" -lt 80 ]; then
  echo "⚠️ ALERT: Agent success rate is $SUCCESS_RATE% (target: 95%)"
  # TODO: Send Slack/email/PagerDuty
fi

# Check API health
API_STATUS=$(curl -s https://hummbl-api.hummbl.workers.dev/health | jq '.status')
if [ "$API_STATUS" != "healthy" ]; then
  echo "🚨 CRITICAL: Production API is $API_STATUS"
  # TODO: Send Slack/email/PagerDuty
fi
```

Run hourly:

```shell
0 * * * * /path/to/alert-if-unhealthy.sh
```

---

## Common Tasks

### Deploying a New Agent

1. **Prepare agent in hummbl-agent repo**
 
 ```shell
    cd /path/to/hummbl-agent
    # ... add agent code, schemas, skills ...
    ```
 
2. **Test against production API**
 
 ```shell
    # Verify API is reachable
    curl https://hummbl-api.hummbl.workers.dev/health
    
    # Run agent schema validation
    npm run test:schemas
    
    # Test agent locally
    npm run test  # or your test command
    ```
 
3. **Deploy agent**
 
 - Merge to hummbl-agent main branch (CI/CD handles deployment)
 - Or manually start agent process pointing to production API
4. **Monitor deployment**
 
 ```shell
    node dashboard.js  # Should show new agent in metrics
    node monitor.js --watch  # Watch for first executions
    ```
 

### Scaling Agents

If agent throughput is insufficient:

1. **Increase rate limit on API** (if agents are hitting limit):
 
 ```shell
    # Edit hummbl-production
    cd /path/to/hummbl-production
    # Update api/src/middleware/rate-limit.ts: MAX_REQUESTS_PER_MINUTE = 200
    git commit -am "ops: increase rate limit to 200 req/min"
    git push origin main
    ```
 
2. **Spawn multiple agent instances**
 
 - Same agent runtime, different process IDs
 - Monitor tracks each execution independently
3. **Optimize agent skills**
 
 - Review slow SITREP entries
 - Batch API calls where possible
 - Cache frequently-used model data

### Updating Agent Skills

1. **Make skill changes in hummbl-agent/skills/**
2. **Bump version in hummbl-agent/package.json**
3. **Run schema validation**: `npm run test:schemas`
4. **Test locally and push**
5. **Monitor old vs new agent runs** for performance impact

### Updating API Models

1. \*\*Modify [hummbl-production/schemas/base120-canonical.json](https://github.com/hummbl-dev/hummbl-agent/blob/main)
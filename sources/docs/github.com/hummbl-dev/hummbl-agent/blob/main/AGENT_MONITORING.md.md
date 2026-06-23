# Source: https://github.com/hummbl-dev/hummbl-agent/blob/main/AGENT_MONITORING.md

[hummbl-dev](https://github.com/hummbl-dev) / **[hummbl-agent](https://github.com/hummbl-dev/hummbl-agent)** Public

- [Notifications](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent) You must be signed in to change notification settings
- [Fork 0](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
- [Star 2](https://github.com/login?return_to=%2Fhummbl-dev%2Fhummbl-agent)
 

 

## FilesExpand file tree

 main

/

# AGENT\_MONITORING.md

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History](https://github.com/hummbl-dev/hummbl-agent/commits/main/AGENT_MONITORING.md)

History

105 lines (83 loc) · 2.64 KB

 main

/

# AGENT\_MONITORING.md

Copy path

Top

## File metadata and controls

- Preview
 
- Code
 
- Blame
 

105 lines (83 loc) · 2.64 KB

[Raw](https://github.com/hummbl-dev/hummbl-agent/raw/refs/heads/main/AGENT_MONITORING.md)

Copy raw file

Download raw file

Outline

Edit and raw actions

# Agent Monitoring System

Real-time monitoring for deployed agents (Soma, kimi-code) and production API consumption.

## Quick Start

### View Agent Status Dashboard

```shell
node dashboard.js
```

Shows unified view of:

- Agent execution metrics (total runs, success rate, avg duration)
- Per-agent API usage
- Production API health
- Error patterns

### Watch Live Agent Executions

```shell
node monitor.js --watch
```

Real-time dashboard updating every 5 seconds with:

- Recent agent runs
- Success/failure rates
- Error patterns
- Per-agent statistics

### Check API Health

```shell
node api-monitor.js --check
```

Performs health checks against production endpoints:

- `/health` - API status
- `/v1/models` - Model availability
- `/v1/transformations` - Transformation domains
- `/v1/workflows` - Workflow coverage

### View API Consumption Metrics

```shell
node api-monitor.js
```

Shows tracked API consumption:

- Total requests
- Per-endpoint usage patterns
- Response times
- Success rates
- Rate limit hits

## Data Storage

Metrics are persisted in `_state/`:

- `metrics.json` - Agent execution metrics
- `api-consumption.jsonl` - API request log (newline-delimited JSON)

## How Agents Are Tracked

Monitors scan `_state/runs/<DATE>/<RUN_ID>/` directories for:

- `sitrep-*.json` - Execution report with status, duration, errors
- `manifest-*.json` - Agent metadata and configuration
- Other artifacts and logs

## Monitoring Real-time Deployments

### For Soma

1. Soma logs runs to `_state/runs/<date>/`
2. Monitor watches for new SITREP files
3. Parses execution metadata: status, API calls, errors
4. Aggregates metrics per-agent

### For kimi-code

Same flow as Soma - the monitor auto-detects agent name from run manifests

## Integration with CI/CD

Add to GitHub Actions or deployment pipeline:

```shell
# Check deployment health
node api-monitor.js --check --json

# Generate metrics report
node dashboard.js > deployment-status.txt
```

## Alerting Setup (Future)

Current system tracks metrics. To add alerting:

1. Parse `metrics.json` for thresholds
2. Send Slack/PagerDuty on failures
3. Example: Alert if success\_rate < 80%

## Troubleshooting

**No data showing?**

- Ensure agents have executed and written to `_state/runs/`
- Check that `_state/` directory exists and is readable
- Monitor creates `_state/metrics.json` on first run

**API checks failing?**

- Verify production API is accessible: `curl https://hummbl-api.hummbl.workers.dev/health`
- Check your network connection
- Confirm API endpoint hasn't moved

**Dashboard not updating?**

- In watch mode, it scans every 5 seconds
- Check terminal for error messages
- Manually run `node dashboard.js` to see current status
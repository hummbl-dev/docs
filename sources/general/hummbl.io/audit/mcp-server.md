# Source: https://hummbl.io/audit/mcp-server.html

[hummbl-dev/mcp-server](https://github.com/hummbl-dev/mcp-server)

# MCP Server

Model Context Protocol server for HUMMBL Base120 mental models. Provides structured access to 120 validated mental models across 6 transformation types via the MCP standard.

A

## 100.0

Overall Quality Score

Audited: 2026-03-25 Version: v1.0.4 Node.js / TypeScript

120 Models

6 Transformations

Strict TypeScript Mode

0 High Findings

Apache-2.0 License

## Category Breakdown

100

Lint

A

100

Security

A

100

Complexity

A

100

Dead Code

A

100

Duplication

A

## Key Modules

| Module | Purpose | Status |
| --- | --- | --- |
| index.ts | MCP server entry point and tool registration | Pass |
| base120.ts | Complete model database (120 models, 27KB) | Pass |
| workflows.ts | Curated multi-model workflow templates | Pass |
| governance/ | CAES spec v1.0.0 and version pinning | Pass |

## Findings

Info Perfect score

Clean TypeScript with strict mode enabled, no unused exports, no security findings.

Info CAES governance spec pinned

CAES governance spec pinned at v1.0.0 with Section 6 Fork Exclusion Policy.

Want an audit like this for your codebase? Free for open-source repos.

[Request Free Audit](https://cal.com/hummbl/30min)
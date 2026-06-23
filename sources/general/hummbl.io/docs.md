# Source: https://hummbl.io/docs.html

# API Documentation

Complete reference for the HUMMBL Base120 REST API. 120 mental models across 6 transformations, designed for AI agents and human developers alike.

## Getting Started

HUMMBL Base120 is a REST API providing 120 mental models for AI agents. The API is organized around standard HTTP methods and returns JSON responses. No authentication is required during beta.

Beta Free

### Quick Start

Fetch all 120 models with a single request:

bash Copy

curl https://api.hummbl.io/v1/models

Get model recommendations for a specific problem:

bash Copy

curl -X POST https://api.hummbl.io/v1/recommend \\
 -H "Content-Type: application/json" \\
 -d '{"problem": "How do I prioritize features?"}'

## Base URL

All API requests are made to the following base URL:

Base URL https://api.hummbl.io

The API is served over HTTPS from Cloudflare Workers. All endpoints return `application/json` responses with CORS headers enabled for browser access.

## Authentication

No authentication is required during the beta period. All endpoints are publicly accessible. When authentication is introduced, this section will be updated with instructions for API key management.

## Endpoints

GET /health

Health check endpoint. Returns API status, version, model count, rate limit status, and security event summary.

bash Copy

curl https://api.hummbl.io/health

Response 200

json Copy

{
 "status": "healthy",
 "version": "1.0.0",
 "timestamp": "2026-02-25T16:00:26.510Z",
 "models\_count": 120,
 "rate\_limit\_status": {
 "active\_ips": 1,
 "window\_ms": 60000,
 "max\_requests\_per\_minute": 100
 },
 "security": {
 "total\_events": 0,
 "recent\_critical": 0,
 "by\_severity": {}
 }
}

GET /v1/models

List all 120 mental models. Returns the complete Base120 catalog with codes, names, definitions, and priority levels.

bash Copy

curl https://api.hummbl.io/v1/models

Response 200

json Copy

{
 "success": true,
 "data": \[
 {
 "code": "P1",
 "name": "First Principles Framing",
 "definition": "Reduce complex problems to foundational truths that cannot be further simplified",
 "priority": 1
 }
 // ... 119 more models
 \]
}

GET /v1/models/:code

Get a single model by its Base120 code. Codes follow the pattern: P1-P20 (Perspective), IN1-IN20 (Inversion), CO1-CO20 (Composition), DE1-DE20 (Decomposition), RE1-RE20 (Recursion), SY1-SY20 (Systems).

bash Copy

curl https://api.hummbl.io/v1/models/P1

Response 200

json Copy

{
 "success": true,
 "data": {
 "code": "P1",
 "name": "First Principles Framing",
 "definition": "Reduce complex problems to foundational truths that cannot be further simplified",
 "priority": 1
 }
}

Response 404

json Copy

{
 "success": false,
 "error": "Model not found: X99"
}

POST /v1/recommend

Get model recommendations for a problem description. The API analyzes keywords and patterns to suggest the most relevant mental models.

Request Body

json Copy

{
 "problem": "How do I prioritize features?"
}

bash Copy

curl -X POST https://api.hummbl.io/v1/recommend \\
 -H "Content-Type: application/json" \\
 -d '{"problem": "How do I prioritize features?"}'

Response 200

json Copy

{
 "success": true,
 "data": \[
 {
 "code": "P1",
 "name": "First Principles Framing",
 "definition": "Reduce complex problems to foundational truths...",
 "priority": 1
 },
 {
 "code": "P2",
 "name": "Stakeholder Mapping",
 "definition": "Identify all parties with interest, influence, or impact...",
 "priority": 1
 }
 \],
 "meta": {
 "matchedPatterns": \["Decomposition"\],
 "keywordsAnalyzed": 2
 }
}

POST /v1/workflows/match

Find matching workflows for a problem description. Workflows are curated sequences of mental models designed for common scenarios.

Request Body

json Copy

{
 "problem": "How do I prioritize features?"
}

bash Copy

curl -X POST https://api.hummbl.io/v1/workflows/match \\
 -H "Content-Type: application/json" \\
 -d '{"problem": "How do I prioritize features?"}'

Response 200

json Copy

{
 "success": true,
 "data": \[\],
 "count": 0
}

POST /security/validate

Validate and sanitize input. Checks for PII, injection attempts, and other security concerns. Returns sanitized output with a validation report.

Request Body

json Copy

{
 "input": "Hello world"
}

bash Copy

curl -X POST https://api.hummbl.io/security/validate \\
 -H "Content-Type: application/json" \\
 -d '{"input": "Hello world"}'

Response 200

json Copy

{
 "success": true,
 "validation": { "valid": true },
 "sanitized": "Hello world",
 "pii": {
 "found": false,
 "types": \[\],
 "matches": \[\]
 }
}

## Rate Limits

The API enforces rate limits to ensure fair usage and service stability.

| Parameter | Value |
| --- | --- |
| Requests per minute | 100 |
| Window | 60 seconds (sliding) |
| Scope | Per IP address |
| Exceeded response | 429 Too Many Requests |

When the rate limit is exceeded, the API returns a `429` status code. Wait for the current window to expire before retrying. The `/health` endpoint includes live rate limit status in its response.

## Error Handling

The API uses standard HTTP status codes and returns a consistent error format for all failure cases.

json Copy

{
 "success": false,
 "error": "Error description"
}

| Status Code | Meaning |
| --- | --- |
| 200 | Success |
| 400 | Bad request -- invalid or missing parameters |
| 404 | Not found -- resource does not exist |
| 429 | Rate limited -- too many requests |
| 500 | Server error -- unexpected internal failure |

## SDKs & Tools

Multiple ways to integrate with the Base120 API.

MCP Server

Use Base120 models directly from Claude, Cursor, or any MCP-compatible AI client. Install via npm and configure your client.

bash Copy

npm install @hummbl/mcp-server

[View on npm →](https://www.npmjs.com/package/@hummbl/mcp-server)

REST API

Works with any HTTP client. No SDK required. Use curl, fetch, axios, httpx, or your language's built-in HTTP library.

javascript Copy

const res = await fetch('https://api.hummbl.io/v1/models');
const data = await res.json();
console.log(data.data.length); // 120

[Open API →](https://api.hummbl.io)

Playground

Try the API live in your browser. Curated demos, interactive sandbox, and the full safety stack visualization.

[Open Playground →](https://hummbl.io/playground.html)
# Source: https://hummbl.io/primitives/circuit-breaker.html

Resilience

# Circuit Breaker

CLOSED/HALF\_OPEN/OPEN state machine wrapping every external adapter an agent touches. Fails fast when upstream degrades, stops cascading failures, and costs you nothing in the happy path.

$pip install hummbl-governance

## What it does

Every external call — an LLM API, a database, a webhook, a vector store — is wrapped in a breaker. The breaker counts failures over a sliding window. If the failure rate exceeds threshold, it opens: further calls fail instantly without hitting the upstream service.

After a cooldown, it transitions to HALF\_OPEN: it lets one call through. If that succeeds, it closes. If it fails, it opens again with a longer cooldown (exponential backoff).

This prevents the three things that kill agent systems: retry storms that DDoS your own upstream, runaway cost burns from retrying failing paid APIs, and cascading timeouts where one slow dependency drags everything down.

## Use it

```
from hummbl_governance import CircuitBreaker, CircuitBreakerState

cb = CircuitBreaker(
    failure_threshold=5,        # open after 5 failures
    recovery_timeout=30.0,      # seconds before HALF_OPEN probe
)

try:
    result = cb.call(anthropic_client.messages.create, **params)
except Exception:
    # Breaker records the failure; falls back to your handler
    result = fallback_handler()

if cb.state == CircuitBreakerState.OPEN:
    logger.warning("anthropic-api breaker is open")
```

## When to reach for it

- You call any external API from an agent — LLM providers, vector stores, webhooks
- Cost-burn scenarios are a concern (retrying failing calls to paid APIs)
- You have cascading dependency risk (one slow service degrades everything)
- You need adapter-level observability for governance audits

## The contract

```
class CircuitBreakerState(Enum):
    CLOSED    # normal operation
    HALF_OPEN # testing recovery
    OPEN      # failing fast

CircuitBreaker(
    failure_threshold: int = 5,
    recovery_timeout: float = 30.0,
    on_state_change: Callable | None = None,
)

CircuitBreaker.call(fn, *args, **kwargs) -> Any
CircuitBreaker.state -> CircuitBreakerState  # property
CircuitBreaker.failure_count -> int
CircuitBreaker.success_count -> int
CircuitBreaker.reset() -> None
```

All state transitions write to the Governance Bus for post-incident analysis.

## See also

- [Kill Switch](https://hummbl.io/kill-switch.html) — fleet-level halt, complementary to per-adapter breaker
- [Governance Bus](https://hummbl.io/governance-bus.html) — logs trips, transitions, recoveries
- [hummbl-governance SDK](https://hummbl.io/../docs/hummbl-governance.html#circuit-breaker) — full `CircuitBreaker` API reference
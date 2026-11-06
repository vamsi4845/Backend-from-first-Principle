# Week 8 — Errors & fault tolerance (~7 h)

**Manual:** [Error handling](../../src/content/chapters/12-error-handling-and-fault-tolerance.mdx)

## Read (~2 h)

- Fail fast vs retry; circuit breaker idea; timeouts on outbound HTTP.

## Type (~2 h)

- Global handler for unexpected exceptions → **500** without leaking stack traces.
- Fake “notification service” client with timeout + one retry.

## Exercise (~2 h)

1. On task create, call fake notifier; if it fails after retry, still persist task but return warning field (or use outbox pattern note).
2. Add request id middleware; include id in error JSON.

## Done when

- [ ] No raw exception strings in production-shaped responses.
- [ ] Request id visible in logs and error body.

## Commit message idea

`labs: week 8 — global errors and outbound timeout`

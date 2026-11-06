# Week 9 — Caching (~7 h)

**Manual:** [Caching](../../src/content/chapters/09-caching.mdx)

## Read (~2 h)

- Cache-aside; TTL; invalidation on write.

## Type (~2 h)

- Redis via Docker, or in-process cache for local-only.
- Cache `GET /api/v1/tasks/{id}` and list keys scoped by query params.

## Exercise (~2 h)

1. Invalidate cache on PATCH/DELETE.
2. Log cache hit/miss counts (no PII).
3. Document TTL choice in README.

## Done when

- [ ] Second identical GET is served from cache.
- [ ] Update clears stale entries.

## Commit message idea

`labs: week 9 — redis cache-aside for tasks`

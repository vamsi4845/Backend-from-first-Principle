# Week 5 — REST design (part 2) (~7 h)

**Manual:** Continue [API design (REST)](../../src/content/chapters/07-api-design-rest.mdx) (PATCH, errors, idempotency).

## Read (~2 h)

- PUT vs PATCH; when POST is not enough.
- Idempotency keys (conceptual)—optional header on create.

## Type (~2 h)

- `PATCH /api/v1/tasks/{id}` for partial updates.
- Align all errors to one JSON structure `{ "error": { "code", "message", "details" } }`.

## Exercise (~2 h)

1. `DELETE /api/v1/tasks/{id}` → **204**.
2. Return **409** when deleting a task referenced by another entity (fake the relation in memory).
3. Add `If-Match` or updated_at check for optimistic concurrency (stretch).

## Done when

- [ ] Every failing path returns the same error envelope.
- [ ] `API.md` updated with PATCH/DELETE.

## Commit message idea

`labs: week 5 — patch/delete tasks and unified errors`

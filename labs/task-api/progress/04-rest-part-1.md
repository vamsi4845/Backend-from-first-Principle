# Week 4 — REST design (part 1) (~7 h)

**Manual:** [API design (REST)](../../src/content/chapters/07-api-design-rest.mdx)

## Read (~2 h)

- Nouns, plural paths, `/api/v1` versioning.
- List endpoints: pagination (`limit`, `cursor` or `offset`), filtering.

## Type (~2 h)

- Introduce a `tasks` resource (new router) OR rename books → tasks if you prefer one resource.
- Implement `GET /api/v1/tasks` with `limit` (default 20, max 100) and `status` filter.

## Exercise (~2 h)

1. `POST /api/v1/tasks` with body `{ "title", "status" }` where status is an enum.
2. `GET /api/v1/tasks/{id}` with **404** envelope matching chapter examples.
3. Write endpoint list in `labs/task-api/API.md` (method, path, auth: none for now).

## Done when

- [ ] Pagination returns stable ordering documented in `API.md`.
- [ ] Wrong enum status returns **422**.

## Commit message idea

`labs: week 4 — tasks list with pagination and filters`

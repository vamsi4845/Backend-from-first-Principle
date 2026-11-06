# Week 3 — Controllers, services, repositories (~7 h)

**Manual:** [Layers & middleware](../../src/content/chapters/06-controllers-services-and-middlewares.mdx)

## Read (~2 h)

- Handlers parse/validate; services enforce rules; repositories talk to storage.
- Request context via `Depends` (FastAPI) vs passing `Request` everywhere.

## Type (~2 h)

- Move any remaining logic out of `app/routers/books.py`.
- Add logging middleware that logs method, path, and status code (no request bodies).

## Exercise (~2 h)

1. Add `delete_book(id)` in all three layers; return **204** on success.
2. Prevent duplicate titles (case-insensitive) in the **service**, not the router.
3. Swap `InMemoryBookRepository` in tests using `app.dependency_overrides`.

## Done when

- [ ] Routers have no business `if` chains beyond HTTP concerns.
- [ ] One test uses dependency override for an isolated repo.

## Commit message idea

`labs: week 3 — delete book and duplicate title rule`

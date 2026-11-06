# Week 2 — Serialization & validation (~7 h)

**Manual:** [Serialization](../../src/content/chapters/03-serialization-and-deserialization.mdx) · [Validations](../../src/content/chapters/05-validations-and-transformations.mdx)

## Read (~2 h)

- Request/response models vs domain models.
- Validation at the boundary (Pydantic) vs business rules in the service.

## Type (~2 h)

- Add `BookUpdate` with optional fields; use `model_validator` or field validators to strip title whitespace on create.
- Return a single **error envelope** shape for `HTTPException` (middleware or exception handler stub is fine).

## Exercise (~2 h)

1. Reject titles that are only whitespace with a clear **422** or **400** (pick one and stay consistent).
2. Add `published_year: int | None` with range 1000–2100 on create.
3. Document the book schemas in a short comment block mapping JSON field → meaning.

## Done when

- [ ] Invalid `published_year` never reaches the repository.
- [ ] One consistent JSON error body for your hand-rolled 400s.

## Commit message idea

`labs: week 2 — book validation and error envelope`

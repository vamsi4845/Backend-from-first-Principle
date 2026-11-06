# Week 6 — Database (~7 h)

**Manual:** [Databases](../../src/content/chapters/08-databases.mdx)

## Read (~2 h)

- Migrations; one transaction for multi-step writes.
- N+1 problem awareness on list endpoints.

## Type (~2 h)

- Add SQLAlchemy 2.0 + Alembic (or SQLModel if you prefer—pick one and note it in README).
- Implement `PostgresBookRepository` / task repo behind the same interface.

## Exercise (~2 h)

1. Docker Compose with Postgres, or SQLite file for simplicity—document your choice in README.
2. Seed script with enough rows to test pagination.
3. Wrap “create task + default tag” in a transaction (two tables).

## Done when

- [ ] App runs against real DB; in-memory repo still usable in unit tests.
- [ ] One migration checked in under `labs/task-api/alembic/` (or equivalent).

## Commit message idea

`labs: week 6 — postgres repository and migrations`

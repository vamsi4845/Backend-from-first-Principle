# Week 10 — Testing (~7 h)

**Manual:** [Automated testing](../../src/content/chapters/22-automated-testing.mdx)

## Read (~2 h)

- Pyramid: unit vs integration vs e2e.
- `TestClient` vs running server; dependency overrides.

## Type (~2 h)

- Split tests: `tests/unit/` for service rules, `tests/integration/` for HTTP + repo.
- One integration test that uses real DB (mark `@pytest.mark.integration`).

## Exercise (~2 h)

1. Parametrize validation cases for task create.
2. Integration test: create → get → patch → delete happy path.
3. Optional: GitHub Action under `.github/workflows/labs-task-api.yml` running pytest on push.

## Done when

- [ ] ≥10 tests; CI or local `pytest` documented.
- [ ] You can explain what each layer tests without opening files.

## Commit message idea

`labs: week 10 — integration tests and pytest layout`

# task-api

Capstone API for the labs track. Starts as **books** (chapters 1–6) so examples match the manual; rename resources to **tasks / projects / organizations** when you work through REST design (chapter 7).

## Commands

```bash
uvicorn app.main:app --reload --port 8000
pytest
```

## Layout

| Path | Role |
|------|------|
| `app/main.py` | App factory, middleware, router mounts |
| `app/routers/` | HTTP layer only — parse/validate, call services |
| `app/services/` | Business rules |
| `app/repositories/` | Data access (in-memory now, Postgres in week 6) |
| `app/schemas/` | Pydantic request/response models |
| `progress/` | Weekly checklists |

## Environment

Copy `.env.example` to `.env`. Defaults are safe for local dev.

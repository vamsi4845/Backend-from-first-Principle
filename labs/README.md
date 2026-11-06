# Hands-on labs

## Teaching workspace (slower pace)

This folder follows the **[teach](https://github.com/mattpocock/skills)** skill pattern: one small step per session, one win at a time.

| File / folder | Role |
|---------------|------|
| [`teach/MISSION.md`](./teach/MISSION.md) | Why you are here and what “done” means |
| [`teach/NOTES.md`](./teach/NOTES.md) | Pace rules (e.g. Git Bash + venv) for teachers / future you |
| [`teach/RESOURCES.md`](./teach/RESOURCES.md) | Trusted links (Python docs, FastAPI, pytest) |
| [`teach/lessons/0001-run-python-in-this-repo.html`](./teach/lessons/0001-run-python-in-this-repo.html) | **Start here** if running commands feels confusing |
| [`teach/reference/`](./teach/reference/) | Short cheat sheets you reopen later |

**In Cursor:** use **`/teach`** (or the teach skill) from the repo when you want the agent to stay in “one lesson, one win” mode.

---

Your **6–8 hours/week** track lives below. Spend **~3–4 hours once** on [lesson 0 (Python from JavaScript)](./task-api/progress/00-python-from-javascript.md), then one FastAPI app (`task-api/`) grows as you read the chapters in `src/content/chapters/`.

## Fork and keep it private

This upstream repo is public reference material. To own your progress:

1. **Fork** [Backend-from-first-Principle](https://github.com/DsThakurRawat/Backend-from-first-Principle) to your GitHub account (or duplicate the repo in your org).
2. **Settings → General → Danger zone → Change visibility → Private** if you want lab notes and experiments off the public internet.
3. Clone **your** fork locally and treat `labs/` as yours to commit freely; you can still pull upstream chapter updates into `main` when you want fresh docs.

You do not need to publish lab commits upstream unless you want to contribute improvements back.

## How to run the capstone

```bash
cd labs/task-api
python -m venv .venv
# Git Bash on Windows (use forward slashes):
source .venv/Scripts/activate
# PowerShell: .\.venv\Scripts\Activate.ps1
# cmd: .venv\Scripts\activate.bat

pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```

Open `http://127.0.0.1:8000/docs` for interactive OpenAPI (chapter 25 preview).

## Weekly checklists

| Week | Checklist | Chapters |
|------|-----------|----------|
| 0 | [progress/00-python-from-javascript.md](./task-api/progress/00-python-from-javascript.md) + [python-warmup/](./python-warmup/) | — (language baseline) |
| 1 | [progress/01-http-and-routing.md](./task-api/progress/01-http-and-routing.md) | 1–2 |
| 2 | [progress/02-serialization-and-validation.md](./task-api/progress/02-serialization-and-validation.md) | 3, 5 |
| 3 | [progress/03-layers.md](./task-api/progress/03-layers.md) | 5–6 |
| 4 | [progress/04-rest-part-1.md](./task-api/progress/04-rest-part-1.md) | 7 |
| 5 | [progress/05-rest-part-2.md](./task-api/progress/05-rest-part-2.md) | 7 |
| 6 | [progress/06-database.md](./task-api/progress/06-database.md) | 8 |
| 7 | [progress/07-auth.md](./task-api/progress/07-auth.md) | 4 |
| 8 | [progress/08-errors-and-resilience.md](./task-api/progress/08-errors-and-resilience.md) | 12 |
| 9 | [progress/09-caching.md](./task-api/progress/09-caching.md) | 9 |
| 10 | [progress/10-testing.md](./task-api/progress/10-testing.md) | 22 |

Each checklist has **read**, **type**, **exercise**, and **done when** sections sized for ~7 hours.

## Reading the manual locally

From the repo root: `npm install && npm run dev`, then follow links from each progress file to the matching chapter route.

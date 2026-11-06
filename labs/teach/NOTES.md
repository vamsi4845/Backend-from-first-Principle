# Teaching notes (agent + human)

## Pace

- **One tangible win per session** (e.g. “green pytest” or “one new endpoint that returns 404”).
- Do not stack “read two chapters + implement three features + refactor” in a single message; the learner asked for slower steps.
- After each win, name **exactly one** next step—not a menu of five.

## Environment

- **Git Bash on Windows:** always `source .venv/Scripts/activate`, forward slashes (`exercises/values.py`), not `.venv\Scripts\activate` without quoting/sourcing.
- `python values.py` fails if the file is under `exercises/`; teach “path from current directory” explicitly.
- Warmup code is driven by **`pytest`**, not by running `values.py` as a script unless they add `if __name__ == "__main__":`.

## Preferences (update when the user says so)

- Wants to understand **how to run things locally** before “slugify” or FastAPI details.

# Week 0 — Python for JavaScript developers (~3–4 h)

Do this **before** [01-http-and-routing](./01-http-and-routing.md). You already know functions, async, and objects—this lesson is the **syntax and footguns** that show up in every FastAPI codebase.

**Code:** [`labs/python-warmup/`](../../python-warmup/)

## JS mental model → Python

| You know (JS/TS) | Python equivalent |
|------------------|-------------------|
| `null` / `undefined` | `None` (only one) |
| `[]` / `{}` | `list` / `dict` (same mutability traps) |
| `===` | `is` (identity) vs `==` (value); prefer `is None` |
| `const` / `let` | No declarations—names bind to objects |
| `async/await` | Same idea; `asyncio.gather` ≈ `Promise.all` |
| Zod | Pydantic (week 2 in task-api) |
| `npm` / `package.json` | `pip` / `requirements.txt` + **venv** |
| `import x from` | `from module import thing` (no default export) |

Skip for now: metaclasses, deep OOP, numpy/pandas, most of the stdlib. You can learn those when a task requires them.

## Read (~1 h)

Skim in any order:

- [Official tutorial — first 5 sections](https://docs.python.org/3/tutorial/index.html) (if statements, functions, modules)
- Indentation is syntax; `#` comments; no `var`/`const`
- `def` and `async def`; `try` / `except` / `finally`
- f-strings: `f"hello {name}"`
- `for item in items:` and `for key, value in mapping.items():`

## Type (~1 h)

Open `labs/python-warmup/exercises/values.py` and read the implementations. Notice:

- Type hints: `str`, `list[str]`, `dict[str, int]` (like TS, ignored at runtime unless you use a checker)
- List comprehensions instead of `.map().filter()`
- `.get("key", default)` instead of optional chaining on dicts

Run:

```bash
cd labs/python-warmup
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

All tests should pass on the starter code—that is your reference.

## Exercise (~1–2 h)

1. In `values.py`, add `def slugify(title: str) -> str` that lowercases, strips, and replaces spaces with `-`. Add a test in `tests/test_warmup.py` and make it pass.
2. In `gotchas.py`, read `create_page_config`—this is the Python **mutable default argument** trap (`tags=[]` in a parameter). Explain in one sentence why `tags=None` then `safe_tags = [] if tags is None else list(tags)` is the fix (same class of bug as shared mutable state in JS).
3. In `async_intro.py`, add `async def fetch_sequential() -> tuple[str, str]` that awaits one label after the other (slower). Write a test that both return the same tuple but sequential takes longer (optional: assert timing with a loose bound).
4. REPL experiment (5 min each):
   - `python` → `{} is {}` vs `{1:2} == {1:2}`
   - `True`, `False`, and truthy values: `bool("")`, `bool([])`, `bool(0)`

## Done when

- [ ] You can read `app/dependencies.py` in task-api without googling syntax.
- [ ] You know why venv exists (isolated `site-packages`, like local `node_modules` without hoisting confusion).
- [ ] You added `slugify` + test yourself.

## Then

Start [01-http-and-routing](./01-http-and-routing.md). When you see `Depends`, `async def`, and Pydantic models, you are extending week 0—not learning a second language from scratch.

## Optional later (not week 0)

- `pathlib.Path` for file paths
- `dataclasses` / `@classmethod`
- Ruff or mypy on `task-api` once the app grows

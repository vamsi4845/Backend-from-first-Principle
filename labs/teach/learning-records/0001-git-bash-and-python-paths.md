# Git Bash needs `source` for venv; paths are not Node-style backslash

Running `.venv\Scripts\activate` in bash merged into an invalid token; the fix is `source .venv/Scripts/activate`. Running `python values.py` from `labs/python-warmup` failed because the file lives at `exercises/values.py`—Python resolves paths from the **current working directory**, like `node` with a relative path.

This matters so future sessions teach “cd, then path, then interpreter” as one block instead of jumping to exercises.

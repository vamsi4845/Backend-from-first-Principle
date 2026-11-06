# Week 1 — HTTP & routing (~7 h)

**Manual:** [HTTP and CORS](../../src/content/chapters/01-http-and-cors.mdx) · [Routing](../../src/content/chapters/02-routing-in-backend.mdx)  
**Local site:** `npm run dev` → `/01-http-and-cors/` and `/02-routing-in-backend/`

## Read (~2 h)

- Status codes you will use daily: 200, 201, 400, 404, 422, 500.
- CORS: why the browser sends `Origin` and what `Access-Control-Allow-Origin` does.
- Routing key = **HTTP method + path**.

## Type (~2 h)

Run the starter app and trace one request:

```bash
cd labs/task-api
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest -q
```

Follow: `books.router` → `BookService` → `InMemoryBookRepository`.

## Exercise (~2 h)

1. Add `GET /api/v1/books/{book_id}` returning **404** when missing (keep data in the in-memory repo).
2. From a static HTML file or your FE dev server, call `POST /api/v1/books` and confirm CORS headers in DevTools.
3. Send malformed JSON and confirm **422**; send `?sort=invalid` and confirm **400**.

## Done when

- [ ] You can explain 400 vs 422 without looking at notes.
- [ ] `pytest -q` passes.
- [ ] You implemented get-by-id yourself.

## Commit message idea

`labs: week 1 — book detail route and CORS smoke test`

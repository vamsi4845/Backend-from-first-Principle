from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_book_returns_201_and_location() -> None:
    response = client.post("/api/v1/books", json={"title": "Backend from First Principles"})
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Backend from First Principles"
    assert "Location" in response.headers
    assert response.headers["Location"].endswith(f"/api/v1/books/{body['id']}")


def test_invalid_sort_returns_400() -> None:
    response = client.get("/api/v1/books", params={"sort": "price"})
    assert response.status_code == 400


def test_validation_failure_returns_422() -> None:
    response = client.post("/api/v1/books", json={"title": ""})
    assert response.status_code == 422

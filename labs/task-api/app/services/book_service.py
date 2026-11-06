from fastapi import HTTPException, status

from app.repositories.book_repository import BookRepository
from app.schemas.book import BookCreate, BookRead

ALLOWED_SORT = frozenset({"name", "date"})


class BookService:
    def __init__(self, repo: BookRepository) -> None:
        self._repo = repo

    def list_books(self, sort: str | None) -> list[BookRead]:
        normalized = sort or "date"
        if normalized not in ALLOWED_SORT:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="sort must be 'name' or 'date'",
            )
        return self._repo.list_books(normalized)

    def create_book(self, payload: BookCreate) -> BookRead:
        return self._repo.create_book(payload)

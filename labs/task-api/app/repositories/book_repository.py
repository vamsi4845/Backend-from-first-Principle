from abc import ABC, abstractmethod
from datetime import datetime, timezone

from app.schemas.book import BookCreate, BookRead


class BookRepository(ABC):
    @abstractmethod
    def list_books(self, sort: str) -> list[BookRead]:
        raise NotImplementedError

    @abstractmethod
    def create_book(self, payload: BookCreate) -> BookRead:
        raise NotImplementedError


class InMemoryBookRepository(BookRepository):
    def __init__(self) -> None:
        self._books: list[BookRead] = []
        self._next_id = 1

    def list_books(self, sort: str) -> list[BookRead]:
        books = list(self._books)
        if sort == "name":
            books.sort(key=lambda book: book.title.lower())
        else:
            books.sort(key=lambda book: book.created_at, reverse=True)
        return books

    def create_book(self, payload: BookCreate) -> BookRead:
        book = BookRead(
            id=self._next_id,
            title=payload.title.strip(),
            created_at=datetime.now(timezone.utc),
        )
        self._next_id += 1
        self._books.append(book)
        return book

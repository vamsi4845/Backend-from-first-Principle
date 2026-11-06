from functools import lru_cache

from app.repositories.book_repository import InMemoryBookRepository
from app.services.book_service import BookService


@lru_cache
def get_book_repository() -> InMemoryBookRepository:
    return InMemoryBookRepository()


def get_book_service() -> BookService:
    return BookService(get_book_repository())

from fastapi import APIRouter, Depends, Query, Response, status

from app.dependencies import get_book_service
from app.schemas.book import BookCreate, BookRead
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=list[BookRead])
def list_books(
    sort: str | None = Query(default=None),
    service: BookService = Depends(get_book_service),
) -> list[BookRead]:
    return service.list_books(sort)


@router.post("", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_book(
    payload: BookCreate,
    response: Response,
    service: BookService = Depends(get_book_service),
) -> BookRead:
    book = service.create_book(payload)
    response.headers["Location"] = f"/api/v1/books/{book.id}"
    return book

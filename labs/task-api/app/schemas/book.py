from datetime import datetime

from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class BookRead(BaseModel):
    id: int
    title: str
    created_at: datetime

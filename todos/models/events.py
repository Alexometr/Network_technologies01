from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


# 1. Основная модель-таблица. Она будет создавать структуру таблицы в файле БД.
class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str

    tags: List[str] = Field(sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com",
                "description": "We will be discussing the contents of the FastAPI book.",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Hybrid"
            }
        }

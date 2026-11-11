from beanie import Document
from pydantic import BaseModel
from typing import Optional, List

class Event(Document):
    title: str
    image: str
    description: str
    location: str
    tags: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com",
                "description": "We will be discussing the contents of the FastAPI book.",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"
            }
        }

    class Settings:
        name = "events"

class EventUpdate(BaseModel):
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

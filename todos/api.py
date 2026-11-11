from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from todo import todo_router
from event_routes import event_router
from models.events import Event


app.include_router(todo_router)
app.include_router(event_router, prefix="/event")

@app.on_event("startup")
async def on_startup():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(
        database=client.planner_db,
        document_models=[Event]
    )
    print("Успешное асинхронное подключение к MongoDB через Beanie!")
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello world"}
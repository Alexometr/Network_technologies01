from fastapi import FastAPI
from todo import todo_router
from event_routes import event_router
from database.connection import conn

app = FastAPI()

app.include_router(todo_router)
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def Welcome() -> dict:
    return {"message": "Hello world"}




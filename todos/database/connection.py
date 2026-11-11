import os
from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"

connect_args = {"check_same_thread": False}

engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

def conn():
    if not os.path.exists(database_file):
        SQLModel.metadata.create_all(engine_url)
        print("База данных и таблицы успешно созданы с нуля!")
    else:
        print("Файл базы данных найден, пропускаем создание таблиц.")

def get_session():
    with Session(engine_url) as session:
        yield session

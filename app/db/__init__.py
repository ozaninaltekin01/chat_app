from sqlmodel import create_engine, SQLModel
from .models import User

DATABASE_URL = "sqlite:///./chat_app.db"  # SQLite database file
engine = create_engine(DATABASE_URL,echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
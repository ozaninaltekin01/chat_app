from sqlmodel import Session
from . import  engine

def get_session():
    """
    Create a new SQLModel session.
    """
    with Session(engine) as session:
        yield session
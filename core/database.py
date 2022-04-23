from sqlmodel import create_engine, SQLModel

from core.config import settings


engine = create_engine(settings.DATABASE_URI, echo=True, connect_args={"check_same_thread": False})


def create_db():
    SQLModel.metadata.create_all(engine)

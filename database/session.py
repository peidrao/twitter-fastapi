from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlmodel import Session, create_engine, SQLModel

from core.config import settings


# engine = create_engine(settings.DATABASE_URI)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# meta = MetaData()
# connection = engine.connect()
# Base = declarative_base()


engine = create_engine(settings.DATABASE_URI, echo=True, connect_args={"check_same_thread": False})

def create_db():
    SQLModel.metadata.create_all(engine)
from sqlmodel import create_engine, SQLModel
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn


SQLAlCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme='postgresql',
    user='root',
    password='root',
    host='localhost:5434',
    path='/tweet_database'
    )


engine = create_engine(SQLAlCHEMY_DATABASE_URI, pool_pre_ping=True,)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

try:
    db = SessionLocal()
except Exception as e:
    raise e

def create_db():
    SQLModel.metadata.create_all(engine)

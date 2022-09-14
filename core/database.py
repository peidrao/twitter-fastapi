from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn


SQLAlCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme='postgresql',
    user='root',
    password='root',
    host='localhost:5434',
    path='/tweet_database'
    )


engine = create_engine(SQLAlCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

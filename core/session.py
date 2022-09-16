from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn


SQLAlCHEMY_DATABASE_URI = PostgresDsn.build(
    scheme='postgresql',
    user='root',
    password='root',
    host='localhost:5434',
    path='/tweet_database'
    )


engine = create_engine(SQLAlCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

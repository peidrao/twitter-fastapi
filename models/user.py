from sqlalchemy import Column, Integer, String, Boolean, DateTime

from database.session import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    password = Column(String)

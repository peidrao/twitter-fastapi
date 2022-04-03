from datetime import datetime
from enum import unique
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship

# from database.session import Base


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    username: Optional[str] = Field(max_length=120, nullable=False)
    email: Optional[str] = Field(max_length=200, nullable=False)
    password: Optional[str] = Field(max_length=200, nullable=False)
    birthday: Optional[datetime] = Field(nullable=False)

    is_active: Optional[bool] = Field(default=True)
    is_banned: Optional[bool] = Field(default=False)

    created_at: Optional[datetime] = Field(default=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=datetime.utcnow)



# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     username = Column(String, unique=True, nullable=False)
#     email = Column(String, unique=True, nullable=False)
#     password = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True)
#     is_banned = Column(Boolean, default=False)

#     created_at = Column(TIMESTAMP, default=datetime.utcnow())
#     updated_at = Column(TIMESTAMP, default=datetime.utcnow(), onupdate=datetime.utcnow())

#     items = relationship('Tweet', back_populates='user')



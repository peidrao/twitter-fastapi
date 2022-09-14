from datetime import date, datetime
from typing import Optional
from sqlalchemy import Boolean, ForeignKey, Integer, String, Column, DateTime, Date
from core.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, max_length=120, nullable=False)
    username = Column(String, max_length=120, unique=True, nullable=False)
    email = Column(String, max_length=200, nullable=False)
    password= Column(String, max_length=200, nullable=False)
    birthday = Column(Date, nullable=True)

    is_active = Column(Boolean, default=True)
    is_banned = Column(Boolean, default=False)

    created_at= Column(DateTime, default=datetime.utcnow())
    updated_at =  Column(DateTime, default=datetime.utcnow())


class Follow(Base):
    __tablename__ = 'follows'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user_ref_id = Column(Integer, ForeignKey("users.id"))
    is_followed = Column(Boolean, default=False)
    is_muted = Column(Boolean,  default=False)
    is_blocked = Column(Boolean, default=False)
    
    user = relationship(User, back_populates="follows")
    user_ref = relationship(User, back_populates="follows")


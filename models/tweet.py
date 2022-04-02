from turtle import back
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .user import User
from database.session import Base


class Tweet(Base):
    __tablename__ = 'tweet'
    id = Column(Integer, primary_key=True, index=True)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    deleted_at = Column(DateTime, default=None)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, back_populates='items')

from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from database.session import Base



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    password = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow().strftime("%Y-%m-%d" "%H:%M:%S"))

    items = relationship('Tweet', back_populates='user')


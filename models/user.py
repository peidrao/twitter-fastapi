from datetime import datetime
from sqlalchemy import Boolean, ForeignKey, Integer, String, Column, DateTime, Date
from core.base_class import Base
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    username = Column(String(120), unique=True, nullable=False)
    email = Column(String(120), nullable=False)
    password= Column(String(100), nullable=False)
    birthday = Column(Date, nullable=True)

    is_active = Column(Boolean, default=True)
    is_banned = Column(Boolean, default=False)

    created_at= Column(DateTime, default=datetime.utcnow())
    updated_at =  Column(DateTime, default=datetime.utcnow())


class Follow(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user_ref_id = Column(Integer, ForeignKey("user.id"))
    is_followed = Column(Boolean, default=False)
    is_muted = Column(Boolean,  default=False)
    is_blocked = Column(Boolean, default=False)

    created_at= Column(DateTime, default=datetime.utcnow())
    updated_at =  Column(DateTime, default=datetime.utcnow())

    user = relationship("User", back_populates="follow")
    user_ref = relationship("User", back_populates="follow")

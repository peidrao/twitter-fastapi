from datetime import date, datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlmodel import Field, SQLModel
from sqlalchemy.orm import relationship

# from .user import User
# from database.session import Base


class Tweet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str

    is_active: Optional[bool] = Field(default=True)
    created_at: Optional[datetime] = Field(default=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=datetime.utcnow)
    
    user: Optional[int] = Field(default=None, foreign_key="user.id")


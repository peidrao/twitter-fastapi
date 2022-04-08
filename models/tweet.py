from datetime import datetime
from typing import Optional
from xmlrpc.client import boolean
from sqlmodel import Field, SQLModel


class Tweet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    likes: Optional[int]
    is_active: Optional[bool] = Field(default=True)
    created_at: Optional[datetime] = Field(default=datetime.utcnow())
    updated_at: Optional[datetime] = Field(default=datetime.utcnow())
    
    user: Optional[int] = Field(default=None, foreign_key="user.id")


class Like(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    tweet: Optional[int] = Field(default=None, foreign_key="tweet.id")
    user: Optional[int] = Field(default=None, foreign_key="user.id")
    is_active: Optional[boolean] = Field(default=True)


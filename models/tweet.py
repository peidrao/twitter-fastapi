from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Tweet(SQLModel, table=True):
    __tablename__ = 'tweets'
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    likes: Optional[int]
    is_active: Optional[bool] = Field(default=True)
    created_at: Optional[datetime] = Field(default=datetime.utcnow())
    updated_at: Optional[datetime] = Field(default=datetime.utcnow())
    
    user: Optional[int] = Field(default=None, foreign_key="users.id")


class Like(SQLModel, table=True):
    __tablename__ = 'likes'
    id: int = Field(default=None, primary_key=True)
    tweet: Optional[int] = Field(default=None, foreign_key="tweets.id")
    user: Optional[int] = Field(default=None, foreign_key="users.id")
    is_active: Optional[bool] = Field(default=True)


class Retweet(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    comment: Optional[str] = Field(max_length=280)
    tweet: Optional[int] = Field(default=None, foreign_key="tweets.id")
    user: Optional[int] = Field(default=None, foreign_key="users.id")
    is_active: Optional[bool] = Field(default=True)

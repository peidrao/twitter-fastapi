from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TweetBase(BaseModel):
    text: str


class TweetDisplay(BaseModel):
    id: Optional[int]
    likes: Optional[int]
    retweets: Optional[int]
    text: Optional[str]
    user: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True

from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class TweetBase(BaseModel):
    text: str
    user: int


class TweetDisplay(BaseModel):
    text: Optional[str]
    user: Optional[int]
    created_at: datetime

    class Config:
        orm_mode = True


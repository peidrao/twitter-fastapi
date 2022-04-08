from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class LikeBase(BaseModel):
    tweet: int


# class TweetDisplay(BaseModel):
#     text: Optional[str]
#     user: Optional[int]
#     created_at: datetime

#     class Config:
#         orm_mode = True


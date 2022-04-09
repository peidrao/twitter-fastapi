from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class LikeBase(BaseModel):
    tweet: int


class LikeDisplay(BaseModel):
    tweet: int
    username: str

    class Config:
        orm_mode = True
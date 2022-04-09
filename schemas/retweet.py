from pydantic import BaseModel
from typing import Optional


class RetweetBase(BaseModel):
    tweet: int
    comment: Optional[str]


class RetweetDisplay(BaseModel):
    tweet: int
    username: str
    comment: Optional[str]

    class Config:
        orm_mode = True

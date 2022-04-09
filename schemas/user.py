from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    name: str
    birthday: date
    username: str
    email: str
    password: str



class UserDisplay(BaseModel):
    username: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True


class UserProfileDisplay(BaseModel):
    username: Optional[str]
    email: Optional[str]
    birthday: Optional[date]
    name: Optional[str]
    created_at: Optional[datetime]
    tweets_count: Optional[int]

    class Config:
        orm_mode = True



class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

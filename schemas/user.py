from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
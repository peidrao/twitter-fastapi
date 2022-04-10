from pydantic import BaseModel


class LikeBase(BaseModel):
    tweet: int


class LikeDisplay(BaseModel):
    tweet: int
    username: str

    class Config:
        orm_mode = True
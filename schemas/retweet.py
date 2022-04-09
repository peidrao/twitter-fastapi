from pydantic import BaseModel
from typing import Optional


class RetweetBase(BaseModel):
    tweet: int
    comment: Optional[str]

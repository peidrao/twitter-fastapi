from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class LikeBase(BaseModel):
    tweet: int

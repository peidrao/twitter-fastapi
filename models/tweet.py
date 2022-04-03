from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Tweet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str

    is_active: Optional[bool] = Field(default=True)
    created_at: Optional[datetime] = Field(default=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=datetime.utcnow)
    
    user: Optional[int] = Field(default=None, foreign_key="user.id")

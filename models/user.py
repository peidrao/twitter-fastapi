from datetime import date, datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = Field(max_length=120, nullable=False)
    username: Optional[str] = Field(max_length=120, nullable=False)
    email: Optional[str] = Field(max_length=200, nullable=False)
    password: Optional[str] = Field(max_length=200, nullable=False)
    birthday: Optional[date] = Field(nullable=False)

    is_active: Optional[bool] = Field(default=True)
    is_banned: Optional[bool] = Field(default=False)

    created_at: Optional[datetime] = Field(default=datetime.utcnow())
    updated_at: Optional[datetime] = Field(default=datetime.utcnow())


class UserAction(SQLModel, table=True):
    __tablename__ = 'user_actions'
    id: int = Field(default=None, primary_key=True)
    user: Optional[int] = Field(default=None, foreign_key="user.id")
    user_ref: Optional[int] = Field(default=None, foreign_key="user.id")
    is_followed: Optional[bool] = Field(default=False)
    is_muted: Optional[bool] = Field(default=False)
    is_blocked: Optional[bool] = Field(default=False)

    created_at: Optional[datetime] = Field(default=datetime.utcnow())

from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


from .base import Base
from models.user import User
from utils.hash import Hash
from schemas.user import UserBase, UserDisplay


class UserService(Base[User, UserBase]):
    def create(self, db: Session, request: UserBase) -> User:
        user = User(
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password)
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user



user = UserService(User)

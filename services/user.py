from http.client import HTTPException
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
    
    def get_user_by_username(self, db: Session, username: str) -> User:
        user = db.query(User).filter(User.username == username).first()

        if not user:
            raise HTTPException(detail='User not found', status=404)
        
        return user



user = UserService(User)

from http.client import HTTPException
from typing import List, Optional
from fastapi import Response, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


# from .base import Base
from models.user import User
from utils.hash import Hash
from schemas.user import UserBase, UserDisplay


class UserService:
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

    def delete(self, db: Session, id: int) -> User:
        user = db.query(User).filter(User.id == id).first()
        if user: 
            user.is_active= False
            db.commit()  
            db.refresh(user)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    def get_all(self, db: Session) -> User:
        users = db.query(User).filter(User.is_active == True).all()

        return users

    def get_user_by_username(self, db: Session, username: str) -> User:
        user = db.query(User).filter(User.username == username).first()

        if not user:
            raise HTTPException(detail='User not found', status=404)
        
        return user



user = UserService()

from fastapi import Response, status, HTTPException
from sqlmodel import Session
from models.tweet import Tweet
from typing import List

from models import User, Follow
from utils.hash import Hash
from schemas.user import UserAuth, UserBase
from core import engine


class UserService:
    def create(self, request: UserBase) -> User:        
        with Session(engine) as db:
            user = User(name=request.name, birthday=request.birthday,
                        username=request.username,email=request.email,
                        password=Hash.bcrypt(request.password)
            )

            db.add(user)
            db.commit()
            db.refresh(user)
            return user
    
    def get_all(self) -> List[User]:
        with Session(engine) as session:
            users = session.query(User).filter(User.is_active == True).all()

            return users

    def get_profile_by_username(self, username: str) -> User:
        with Session(engine) as session:
            user = session.query(User).filter(User.username == username, User.is_active == True).first()

            if not user:
                raise HTTPException(detail='User not found', status_code=status.HTTP_400_BAD_REQUEST)

            return user
    
    def get_profile_by_id(self, id: int) -> User:
        with Session(engine) as session:
            user = session.query(User).filter(User.id == id, User.is_active == True).first()

            if not user:
                raise HTTPException(detail='User not found', status_code=status.HTTP_400_BAD_REQUEST)
        
        return user

    def get_profile(self, db: Session, username: str) -> User:
        user = db.query(User).filter(User.username == username).first()
        tweet = db.query(Tweet).filter(Tweet.user == user.id).count()
        user = user.dict()
        user.update(tweets_count=tweet)
        return user

    def deactivate_account(self, db: Session, request_user: UserAuth) -> User:
        user = db.query(User).filter(User.id == request_user['id'], User.is_active == True).first()

        if user:
            user.is_active = False
            db.commit()  
            db.refresh(user)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    def me_followers(self, db: Session, username: str) -> User:
        user = db.query(User).filter(User.username == username, User.is_active == True).first()
        user_actions = db.query(Follow).filter(Follow.user_ref == user.id).all()
        json = []
        for user in user_actions:
            data = {}
            user = db.query(User).filter(User.id == user.user, User.is_active == True).first()
            data['id'] = user.id
            data['username'] = user.username
            data['email'] = user.email
            data['name'] = user.name
            json.append(data)
        
        return json
    
    def me_following(self, db: Session, username: str) -> User:
        user = db.query(User).filter(User.username == username, User.is_active == True).first()
        user_actions = db.query(UserAction).filter(UserAction.user == user.id).all()
        json = []
        for user in user_actions:
            data = {}
            user = db.query(User).filter(User.id == user.user_ref, User.is_active == True).first()
            data['id'] = user.id
            data['username'] = user.username
            data['email'] = user.email
            data['name'] = user.name
            json.append(data)
        
        return json


user = UserService()

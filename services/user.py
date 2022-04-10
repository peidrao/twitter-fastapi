from fastapi import Response, status, HTTPException
from requests import request
from sqlmodel import Session
from models.tweet import Tweet

from models.user import User, UserAction
from utils.hash import Hash
from schemas.user import UserAuth, UserBase, UserDisplay


class UserService:
    def create(self, db: Session, request: UserBase) -> User:
        user = User(
            name=request.name,
            birthday=request.birthday,
            username=request.username,
            email=request.email,
            password=Hash.bcrypt(request.password)
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_all(self, db: Session) -> User:
        users = db.query(User).filter(User.is_active == True).all()

        return users

    def get_user_by_username(self, db: Session, username: str) -> User:
        user = db.query(User).filter(User.username == username, User.is_active == True).first()

        if not user:
            raise HTTPException(detail='User not found', status=404)
        
        return user
    
    def get_user_by_id(self, db: Session, id: int) -> User:
        user = db.query(User).filter(User.id == id, User.is_active == True).first()

        if not user:
            return False
        
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
        user_actions = db.query(UserAction).filter(UserAction.user_ref == user.id).all()
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

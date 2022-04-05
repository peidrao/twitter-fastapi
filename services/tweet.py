from typing import List, Optional
from fastapi import Response, status, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from models import Tweet
from schemas.user import UserAuth

from services.user import user as user_service
from schemas.tweet import TweetBase, TweetDisplay


class TweetService:
    def create(self, db: Session, request: TweetBase, request_user: UserAuth) -> Tweet:
        user = user_service.get_user_by_id(db, request_user['id'])
        if user:
            tweet = Tweet(
                text=request.text,
                user=user.id
            )

            db.add(tweet)
            db.commit()
            db.refresh(tweet)
            return tweet
    
        raise HTTPException(detail='User not exists', status_code=404)

    def delete(self, db: Session, id: int, request_user: UserAuth) -> Tweet:
        user = user_service.get_user_by_id(db, request_user['id'])
        tweet = db.query(Tweet).filter(Tweet.id == id).first()
        
        if user.id == tweet.user:
            tweet.is_active = False
            db.commit()  
            db.refresh(user)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    # def get_all(self, db: Session) -> User:
    #     users = db.query(User).filter(User.is_active == True).all()

    #     return users

    # def get_user_by_username(self, db: Session, username: str) -> User:
    #     user = db.query(User).filter(User.username == username).first()

    #     if not user:
    #         raise HTTPException(detail='User not found', status=404)
        
    #     return user



tweet = TweetService()

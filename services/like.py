from typing import List, Optional
from fastapi import Response, status, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from models import Tweet, Like
from schemas.user import UserAuth
from schemas.like import LikeBase

from services.user import user as user_service
# from schemas.tweet import TweetBase, TweetDisplay


class LikeService:
    def create(self, db: Session, request: LikeBase, request_user: UserAuth) -> Like:
        user = user_service.get_user_by_id(db, request_user['id'])
        
        like = db.query(Like).filter(Like.id == request.tweet, Like.user == user.id).first()

        if like:
            if not like.is_active:
                like.is_active = True
            else:
                like.is_active = False
            db.commit()
            db.refresh(like)
            return like

        if user:
            like = Like(
                user=user.id,
                tweet=request.tweet
            )

            db.add(like)
            db.commit()
            db.refresh(like)
            return like
    
        raise HTTPException(detail='User not exists', status_code=404)

    # def delete(self, db: Session, id: int, request_user: UserAuth) -> Tweet:
    #     user = user_service.get_user_by_id(db, request_user['id'])
    #     tweet = db.query(Tweet).filter(Tweet.id == id).first()
        
    #     if user.id == tweet.user:
    #         tweet.is_active = False
    #         db.commit()  
    #         db.refresh(user)
    #         return Response(status_code=status.HTTP_204_NO_CONTENT)

    #     return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    # def get_all(self, db: Session) -> Tweet:
    #     tweets = db.query(Tweet).filter(Tweet.is_active == True).all()

    #     return tweets
    
    # def get_tweet_by_id(self, db: Session, id: int) -> Tweet:
    #     tweet = db.query(Tweet).filter(Tweet.id == id).first()

    #     return tweet


    


like = LikeService()
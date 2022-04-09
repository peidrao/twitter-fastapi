from typing import List, Optional
from fastapi import Response, status, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlmodel import Session

from models import Tweet, Like, Retweet
from schemas.user import UserAuth
from schemas.like import LikeBase

from services.user import user as user_service
from schemas.retweet import RetweetBase


class RetweetService:
    def create(self, db: Session, request: RetweetBase, request_user: UserAuth) -> Like:
        user = user_service.get_user_by_id(db, request_user['id'])
        
        retweet = db.query(Retweet).filter(Retweet.tweet == request.tweet, Retweet.user == user.id).first()

        if retweet:
            if not retweet.is_active:
                retweet.is_active = True
                retweet.comment = request.comment
            else:
                retweet.is_active = False
                retweet.comment = ''
            db.commit()
            db.refresh(retweet)
            return retweet

        if user:
            retweet = Retweet(
                user=user.id,
                tweet=request.tweet,
                comment=request.comment
            )

            db.add(retweet)
            db.commit()
            db.refresh(retweet)
            return retweet
    
        raise HTTPException(detail='User not exists', status_code=404)

retweet = RetweetService()

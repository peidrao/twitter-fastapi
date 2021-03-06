from fastapi import status, HTTPException
from sqlmodel import Session

from models import Retweet
from schemas.user import UserAuth

from services.user import user as user_service
from schemas.tweet import RetweetBase
from utils.tweet_addons import get_tweet_actions


class RetweetService:
    def create(self, db: Session, request: RetweetBase, request_user: UserAuth) -> Retweet:
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
    
        raise HTTPException(detail='User not exists', status_code=status.HTTP_404_NOT_FOUND)

    def get_retweets_by_tweet(self, db: Session, id: int, request_user: UserAuth) -> Retweet:
        retweets = db.query(Retweet).filter(Retweet.tweet == id, Retweet.is_active == True).all()
        return get_tweet_actions(retweets, db)


retweet = RetweetService()

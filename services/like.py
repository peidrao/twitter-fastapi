from fastapi import  HTTPException

from sqlmodel import Session

from models import Like
from schemas.user import UserAuth
from schemas.tweet import LikeBase

from services.user import user as user_service
from utils.tweet_addons import get_tweet_actions


class LikeService:
    def create(self, db: Session, request: LikeBase, request_user: UserAuth) -> Like:
        user = user_service.get_user_by_id(db, request_user['id'])
        
        like = db.query(Like).filter(Like.tweet == request.tweet, Like.user == user.id).first()

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

    def get_likes_by_tweet(self, db: Session, id: int, request_user: UserAuth) -> Like:
        likes = db.query(Like).filter(Like.tweet == id, Like.is_active == True).all()
        return get_tweet_actions(likes, db)


like = LikeService()

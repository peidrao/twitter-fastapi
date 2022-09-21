from fastapi import  HTTPException
from database.session import SessionLocal
from starlette import status
from models import Like
from models.tweet import Tweet
from schemas.user import UserAuth
from services.tweet import tweet as tweet_service
from services.user import user as user_service


class LikeService:
    def create(self, tweet_id: int, request_user: UserAuth) -> Like:
        with SessionLocal() as session:
            user = user_service.get_profile_by_id(request_user['id'])
            tweet =tweet_service.get_tweet_by_id(tweet_id)
            if session.query(Like).filter(Like.tweet_id == tweet_id, Like.user_id == user.id).first():
                raise HTTPException(detail='You already liked this tweet', status_code=status.HTTP_400_BAD_REQUEST)
            like = Like(tweet_id=tweet.id, user_id=user.id, is_active=True)
            
            session.add(like)
            session.commit()
            return like

like = LikeService()

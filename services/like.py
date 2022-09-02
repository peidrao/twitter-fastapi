from fastapi import  HTTPException

from sqlmodel import Session

from models import Like
from schemas.user import UserAuth
from schemas.tweet import LikeBase

from services.user import user as user_service
from core.database import engine


class LikeService:
    def create(self, request: LikeBase, request_user: UserAuth) -> Like:
        with Session(engine) as session:
            user = user_service.get_profile_by_id(request_user.id)
            
            like = session.query(Like).filter(Like.tweet == request.tweet, Like.user == user.id).first()

            if like:
                if not like.is_active:
                    like.is_active = True
                else:
                    like.is_active = False

                session.commit()
                session.refresh(like)
                return like

            if user:
                like = Like(
                    user=user.id,
                    tweet=request.tweet
                )

                session.add(like)
                session.commit()
                session.refresh(like)
                return like
        
            raise HTTPException(detail='User not exists', status_code=404)


like = LikeService()

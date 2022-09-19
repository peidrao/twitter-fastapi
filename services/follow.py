
from fastapi import HTTPException
from sqlalchemy.sql import exists
from starlette import status
from typing import List

from models import Follow, User
from schemas.follow import FollowRequest
from schemas.user import UserAuth

from services.user import user as user_service
from database import SessionLocal


class FollowService:
    def create(self, request: FollowRequest, request_user: UserAuth) -> Follow:
        with SessionLocal() as session:
            user = user_service.get_profile_by_id(request_user['id'])
            user_ref = user_service.get_profile_by_id(request.user_ref)
            if user and user_ref:
                if session.query(exists().where(Follow.user_id == user.id, Follow.user_ref_id == user_ref.id)).scalar():
                    raise HTTPException(detail='you are already following this user', status_code=status.HTTP_200_OK)

                follow  = Follow(user_ref_id=user_ref.id, user_id=user.id, is_followed=True)
                session.add(follow)
                session.commit()
                session.close()

                return follow
    
    def get_followings(self, request: UserAuth) -> List[User]:
        profiles = []
        with SessionLocal() as session:
            followings = session.query(Follow).filter(Follow.user_id == request['id']).all()
            for profile in followings:
                profiles.append(profile.user_ref)
            
        return profiles


follow_service = FollowService()

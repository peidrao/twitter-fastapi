from typing import Dict
from sqlmodel import Session

from models import Follow
from schemas.user import UserAuth

from services.user import user as user_service
from core.deps import engine


class FollowService:
    def create(self, username: str, request_user: Dict) -> Follow:
        with Session(engine) as session:
            user = user_service.get_profile_by_id(request_user['id'])
            user_ref = user_service.get_profile_by_username(username)
            if user and user_ref:
                action  = Follow(user_ref=user_ref.id, user=user.id, is_blocked=False,
                             is_muted=False, is_followed=True)
                session.add(action)
                session.commit()

                return action


follow_service = FollowService()

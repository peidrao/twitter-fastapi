from sqlmodel import Session

from models import Follow
from schemas.user import UserAuth
from schemas.action import UserActionBase

from services.user import user as user_service
from core.database import engine


class FollowService:
    def create(self, request: UserActionBase, request_user: UserAuth) -> Follow:
        with Session(engine) as session:
            user = user_service.get_profile_by_id(request_user.id)
            action  = Follow(user_ref=request.user_ref, user=user.id, is_blocked=False,
                             is_muted=False, is_followed=True)
            session.add(action)

            session.commit()
            return action


follow_service = FollowService

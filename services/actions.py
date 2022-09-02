from sqlmodel import Session

from models import UserAction
from schemas.user import UserAuth
from schemas.action import UserActionBase

from services.user import user as user_service
from core.database import engine


class ActionService:
    def create(self, request: UserActionBase, request_user: UserAuth) -> UserAction:
        with Session(engine) as session:
            user = user_service.get_profile_by_id(request_user.id)

            action = session.query(UserAction).filter(UserAction.user == request_user.id, UserAction.user_ref == request.user_ref).first()

            if action:
                if request.is_blocked:
                    action.is_blocked = True
                elif request.is_followed:     
                    action.is_followed = True
                elif request.is_muted:
                    action.is_muted = True
            else:
                action  = UserAction(user_ref=request.user_ref, user=user.id, is_blocked=request.is_blocked,
                            is_muted=request.is_muted, is_followed=request.is_followed)
                session.add(action)
            
            session.commit()
            session.refresh(action)
            return action


action = ActionService()

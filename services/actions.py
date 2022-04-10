from sqlmodel import Session

from models import UserAction
from schemas.user import UserAuth
from schemas.actions import UserActionBase

from services.user import user as user_service


class ActionService:
    def create(self, db: Session, request: UserActionBase, request_user: UserAuth) -> UserAction:
        user = user_service.get_user_by_id(db, request_user['id'])
        
        action = db.query(UserAction).filter(UserAction.user == request_user['id'], UserAction.user_ref == request.user_ref).first()

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
            db.add(action)
        
        db.commit()
        db.refresh(action)
        return action


action = ActionService()

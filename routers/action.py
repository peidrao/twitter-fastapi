from typing import Any
from fastapi import APIRouter, Depends
from sqlmodel import Session
from authentication.oauth import get_current_user

from schemas.user import UserAuth
from schemas.action import UserActionBase
from services.actions import action
from database.session import engine


router = APIRouter()

@router.post('/follow/')
async def follow(request: UserActionBase, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        return action.create(db=session, request=request, request_user=request_user)
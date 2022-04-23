from typing import Any
from fastapi import APIRouter, Depends
from sqlmodel import Session
from authentication.oauth import get_current_user

from schemas.user import UserAuth
from schemas.retweet import RetweetBase
from services.retweet import retweet
from core.database import engine


router = APIRouter()


@router.post('/', response_model=None)
async def create_retweet(request: RetweetBase, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        object = retweet.create(db=session, request=request, request_user=request_user)
        return object

from typing import Any
from fastapi import APIRouter, Depends
from sqlmodel import Session
from authentication.oauth import get_current_user
from schemas.like import LikeBase

from schemas.user import UserAuth
from services.like import like
from database.session import engine


router = APIRouter()


@router.post('/', response_model=None)
async def create_like(request: LikeBase, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        object = like.create(db=session, request=request, request_user=request_user)
        return object

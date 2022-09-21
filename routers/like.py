from typing import Any
from fastapi import APIRouter, Depends
from sqlmodel import Session
from authentication.oauth import get_current_user
from schemas.tweet import LikeBase
from database import SessionLocal
from schemas.user import UserAuth
from services.like import like


router = APIRouter()


@router.post('/{tweet_id}', response_model=None)
async def create_like(tweet_id: int, request_user: UserAuth = Depends(get_current_user)) -> Any:
    return like.create(tweet_id, request_user=request_user)

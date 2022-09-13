from typing import Any
from fastapi import APIRouter, Depends
from authentication.oauth import get_current_user

from services.follow import follow_service

router = APIRouter()

@router.post('/follow/{username}', dependencies=[Depends(get_current_user)])
def follow(username: str) -> Any:
    action_follow = follow_service.create(username)
    return action_follow
    
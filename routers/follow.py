from typing import Any, List
from fastapi import APIRouter, Depends, Response
from authentication.oauth import get_current_user

from schemas.user import UserAuth, UserProfileResponse
from schemas.follow import FollowRequest, FollowResponse
from services.follow import follow_service


router = APIRouter()

@router.post('/', response_model=FollowResponse)
def follow(request: FollowRequest, request_user: UserAuth = Depends(get_current_user)):
    return follow_service.create(request, request_user)


@router.get('/followings/', response_model=List[UserProfileResponse])
def followings(request_user: UserAuth = Depends(get_current_user)):
    return follow_service.get_followings(request_user)
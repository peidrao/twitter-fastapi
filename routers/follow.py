# from typing import Any
# from fastapi import APIRouter, Depends, Response
# from authentication.oauth import get_current_user
# from schemas.action import FollowDisplay
# from schemas.user import UserAuth

# from services.follow import follow_service

# router = APIRouter()

# @router.post('/{username}')
# def follow(username: str, request_user: UserAuth = Depends(get_current_user)):
#     action = follow_service.create(username, request_user)
#     import pdb; pdb.set_trace()
#     return Response({'user': action.user, 'user_ref': action.user_ref})

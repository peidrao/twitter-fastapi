from typing import Any, List
from fastapi import APIRouter, Depends
# from authentication.oauth import get_current_user

from schemas.user import UserAuth, UserDisplay, UserBase, UserProfileDisplay
from services.user import user
# from core.deps import engine


router = APIRouter()


@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase) -> Any:
    object = user.create(request=request)
    return object


# @router.get('/', response_model=List[UserDisplay])
# def get_profiles() -> Any:
#     users  = user.get_all()
#     return users


# @router.get('/{username}', response_model=UserProfileDisplay)
# def get_profile(username: str) -> Any:
#     return user.get_profile_by_username(username=username)

# @router.patch('/deactivate/')
# async def deactivate(request_user: UserAuth = Depends(get_current_user)) -> Any:
#     with Session(engine) as session:
#         return user.deactivate_account(db=session, request_user=request_user)


# @router.get('/{username}/followers/', response_model=List[UserDisplay])
# async def get_me_followers(username: str) -> Any:
#     with Session(engine) as session:
#         return user.me_followers(db=session, username=username)


# @router.get('/{username}/following/', response_model=List[UserDisplay])
# async def get_me_followers(username: str) -> Any:
#     with Session(engine) as session:
#         return user.me_following(db=session, username=username)

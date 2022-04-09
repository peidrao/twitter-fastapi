from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from authentication.oauth import get_current_user
from schemas.like import LikeBase

from schemas.tweet import TweetDisplay, TweetBase
from schemas.user import UserAuth, UserDisplay
from services.like import like
from database.session import engine


router = APIRouter()


@router.post('/', response_model=None)
async def create_like(request: LikeBase, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        object = like.create(db=session, request=request, request_user=request_user)
        return object

# @router.delete('/{id}', response_model=None)
# async def delete(id: int = id, request_user: UserAuth = Depends(get_current_user)) -> Any:
#     with Session(engine) as session:
#         object = tweet.delete(db=session, id=id, request_user=request_user)
#         return object

# @router.get('/', response_model=List[TweetDisplay])
# async def get_tweets() -> Any:
#     with Session(engine) as session:
#         return tweet.get_all(db=session)

# @router.get('/{id}', response_model=TweetDisplay)
# async def get_tweet(id: int = id) -> Any:
#     with Session(engine) as session:
#         return tweet.get_tweet_by_id(db=session, id=id)
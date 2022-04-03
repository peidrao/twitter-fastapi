from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from schemas.tweet import TweetDisplay, TweetBase
from services.tweet import tweet
from database.session import engine


router = APIRouter()


@router.post('/', response_model=TweetDisplay)
async def create_tweet(request: TweetBase) -> Any:
    with Session(engine) as session:
        object = tweet.create(db=session, request=request)
        return object

# @router.delete('/{id}', response_model=None)
# async def delete(id=id) -> Any:
#     with Session(engine) as session:
#         object = user.delete(db=session, id=id)
#         return object

# @router.get('/', response_model=List[TweetDisplay])
# async def get_users() -> Any:
#     with Session(engine) as session:
#         return user.get_all(db=session)
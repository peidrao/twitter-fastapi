from typing import Any, List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from authentication.oauth import get_current_user
from schemas.like import LikeDisplay
from schemas.retweet import RetweetDisplay

from schemas.tweet import TweetDisplay, TweetBase
from schemas.user import UserAuth

from services.tweet import tweet
from services.retweet import retweet
from services.like import like
from database.session import engine


router = APIRouter()


@router.post('/', response_model=TweetDisplay)
async def create_tweet(request: TweetBase, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        object = tweet.create(db=session, request=request, request_user=request_user)
        return object

@router.delete('/{id}', response_model=None)
async def delete(id: int = id, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        object = tweet.delete(db=session, id=id, request_user=request_user)
        return object

@router.get('/', response_model=List[TweetDisplay])
async def get_tweets(request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        return tweet.get_all(db=session, request_user=request_user)

@router.get('/{id}', response_model=TweetDisplay)
async def get_tweet(id: int = id) -> Any:
    with Session(engine) as session:
        return tweet.get_tweet_by_id(db=session, id=id)


@router.get('/retweets/{id_tweet}', response_model=List[RetweetDisplay])
async def get_retweet_users(id_tweet: int, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        object = retweet.get_retweets_by_tweet(db=session, id=id_tweet, request_user=request_user)
        return object

@router.get('/likes/{id_tweet}', response_model=List[LikeDisplay])
async def get_like_users(id_tweet: int, request_user: UserAuth = Depends(get_current_user)) -> Any:
    with Session(engine) as session:
        object = like.get_likes_by_tweet(db=session, id=id_tweet, request_user=request_user)
        return object
from fastapi import APIRouter

from routers import follow, user, authentication, tweet, like, retweet


api_router = APIRouter()
api_router.include_router(user.router, prefix='/users', tags=['user'])
api_router.include_router(tweet.router, prefix='/tweets', tags=['tweet'])
api_router.include_router(authentication.router, prefix='/login', tags=['login'])
api_router.include_router(like.router, prefix='/likes', tags=['like'])
api_router.include_router(retweet.router, prefix='/retweets', tags=['retweet'])
api_router.include_router(follow.router, prefix='/actions', tags=['action'])

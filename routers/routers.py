from fastapi import APIRouter

from routers import user, authentication, tweet



api_router = APIRouter()
api_router.include_router(user.router, prefix='/users', tags=['user'])
api_router.include_router(tweet.router, prefix='/tweets', tags=['tweet'])
# api_router.include_router(authentication.router, prefix='/login', tags=['login'])
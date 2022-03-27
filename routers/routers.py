from fastapi import APIRouter

from routers import user, authentication



api_router = APIRouter()
api_router.include_router(user.router, prefix='/users', tags=['user'])
api_router.include_router(authentication.router, prefix='/login', tags=['login'])
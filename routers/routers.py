from fastapi import APIRouter

from routers import user


api_router = APIRouter()
api_router.include_router(user.router, prefix='/users', tags=['user'])
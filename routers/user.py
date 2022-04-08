from typing import Any, List, Union
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from schemas.tweet import TweetDisplayCount

from schemas.user import UserDisplay, UserBase, UserProfileDisplay
from services.user import user
from database.session import engine


router = APIRouter()


@router.post('/', response_model=UserDisplay)
async def create_user(request: UserBase) -> Any:
    with Session(engine) as session:
        
        object = user.create(db=session, request=request)
        return object

@router.delete('/{id}', response_model=None)
async def delete(id: int) -> Any:
    with Session(engine) as session:
        object = user.delete(db=session, id=id)
        return object

@router.get('/', response_model=List[UserDisplay])
async def get_users() -> Any:
    with Session(engine) as session:
        return user.get_all(db=session)

@router.get('/{username}', response_model=UserProfileDisplay)
async def get_profile(username: str) -> Any:
    with Session(engine) as session:
        return user.get_profile(db=session, username=username)
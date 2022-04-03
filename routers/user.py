from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.user import UserDisplay, UserBase
from services.user import user
# from database.db import get_db


router = APIRouter()


# @router.post('/', response_model=UserDisplay)
# async def create_user(request: UserBase, db: Session = Depends(get_db)) -> Any:
#     object = user.create(db=db, request=request)
#     return object

# @router.delete('/{id}', response_model=None)
# async def delete(db: Session = Depends(get_db), id=id) -> Any:
#     object = user.delete(db=db, id=id)
#     return object

# @router.get('/', response_model=List[UserDisplay])
# async def get_users(db: Session = Depends(get_db)) -> Any:
#     return user.get_all(db=db)
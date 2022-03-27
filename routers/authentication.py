from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm
from authentication.oauth import create_access_token
from database.db import get_db
from sqlalchemy.orm.session import Session
from models.user import User
from utils.hash import Hash


router = APIRouter()


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()

    if not user:
        raise HTTPException(detail='User not found',
                            status_code=status.HTTP_404_NOT_FOUND)
    if not Hash.verify(user.password, request.password):
        raise HTTPException(detail='Incorrect password',
                            status_code=status.HTTP_404_NOT_FOUND)

    access_token = create_access_token(request={'username': user.username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.username,
        'email': user.email
    }


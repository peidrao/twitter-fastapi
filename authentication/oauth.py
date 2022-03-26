from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional
from jose import jwt, JWTError



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


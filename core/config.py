import secrets

from pydantic.class_validators import validator
from pydantic import BaseSettings



class Settings(BaseSettings):
    API_V1: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = 'TT'
    DATABASE_URI: str = 'sqlite:///./database.db'


settings = Settings()
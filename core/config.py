import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1: str = '/api/v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = 'TT'
    DATABASE_URI: str = 'sqlite:///./database.db'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    PORT: int = 8000
    DEBUG: bool = True
    HOST: str = 'localhost'


settings = Settings()

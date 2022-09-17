from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1: str = '/api/v1'
    SECRET_KEY: str = 'f6db58daedd17dec5f5493456476bed06d83852be22cf3eb9509b5e6cc782aab'
    PROJECT_NAME: str = 'TT'
    # DATABASE_URI: str = 'sqlite:///./database.db'
    DATABASE_URI: str = 'postgresql://root:root@localhost:5434/tweet_database'
    
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    PORT: int = 8000
    DEBUG: bool = True
    HOST: str = 'localhost'


settings = Settings()

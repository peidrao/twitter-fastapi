from fastapi import FastAPI

from core.config import settings
from database.session import Base, engine


Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1}/openapi.json')


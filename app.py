from fastapi import FastAPI

from core.config import settings
from routers.routers import api_router
import models
from core.database import engine


app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1}/openapi.json')

@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(bind=engine)

app.include_router(api_router)

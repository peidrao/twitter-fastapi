from fastapi import FastAPI

from core.config import settings
from database.session import create_db
from routers.routers import api_router


app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f'{settings.API_V1}/openapi.json')

@app.on_event("startup")
def on_startup():
    create_db()

app.include_router(api_router)

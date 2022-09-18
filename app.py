from fastapi import FastAPI
from core.config import settings
from routers.routers import api_router


app = FastAPI(title=settings.PROJECT_NAME, openapi_url=settings.OPEN_API)

app.include_router(api_router)

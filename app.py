from fastapi import FastAPI
from core.config import settings
from routers.routers import api_router
from database import engine, Base
import logging

logger = logging.getLogger(__name__)


app = FastAPI(title=settings.PROJECT_NAME, openapi_url=settings.OPEN_API)

@app.on_event("startup")
async def startup_database():
    logger.info("creating initial data")
    Base.metadata.create_all(bind=engine)
    logger.info("Initial data created")
    


app.include_router(api_router)

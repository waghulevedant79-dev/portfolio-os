from fastapi import FastAPI
from app.api.router import api_router
from app.core.settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(api_router)
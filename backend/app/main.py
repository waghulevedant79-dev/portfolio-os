from fastapi import FastAPI
from app.api.router import api_router
from app.core.settings import settings
from app.core.middleware import LoggingMiddleware
from app.core.exceptions import (AppException, app_exception_handler)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(api_router)
app.add_middleware(LoggingMiddleware)
app.add_exception_handler(AppException, app_exception_handler)
from fastapi import APIRouter

from app.api.routes import root
from app.api.routes import health
from app.api.routes import status
from app.api.routes import version
from app.api.routes import config

api_router = APIRouter()


api_router.include_router(root.router)
api_router.include_router(health.router)
api_router.include_router(status.router)
api_router.include_router(version.router)
api_router.include_router(config.router)
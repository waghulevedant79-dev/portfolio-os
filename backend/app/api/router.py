from fastapi import APIRouter

from app.api.routes import root
from app.api.routes import health
from app.api.routes import status
from app.api.routes import version
from app.api.routes import config
from app.api.routes import exception
from app.api.routes import token
from app.api.routes import verify
from app.api.routes import db_test
from app.api.routes import user
from app.api.routes import llm

api_router = APIRouter()


api_router.include_router(root.router)
api_router.include_router(health.router)
api_router.include_router(status.router)
api_router.include_router(version.router)
api_router.include_router(config.router)
api_router.include_router(exception.router)
api_router.include_router(token.router)
api_router.include_router(db_test.router)
api_router.include_router(user.router)
api_router.include_router(llm.router)

from fastapi import APIRouter
from app.core.settings import settings

router = APIRouter()

@router.get("/config")
def config():
    return {
    "project": settings.PROJECT_NAME,
    "version": settings.PROJECT_VERSION,
    "debug": settings.DEBUG,
    "enviornment" : settings.ENVIRONMENT
}
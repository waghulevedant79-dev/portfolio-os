from fastapi import APIRouter
from app.core.exceptions import AppException

router = APIRouter()

@router.get("/exception")
async def exception():
    raise AppException(
        "Something went wrong",
        400
    )
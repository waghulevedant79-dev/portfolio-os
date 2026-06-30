from fastapi import APIRouter
from app.core.exceptions import AppException

router = APIRouter()

@router.get("/test")
async def test():
    raise AppException(
        "Something went wrong",
        400
    )
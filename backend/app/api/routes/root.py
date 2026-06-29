from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "Message" : "Portfolio os is running"
    }
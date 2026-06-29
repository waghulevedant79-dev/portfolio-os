from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "database" : "not connected",
        "ai" : "not integrated",
        "server" : "healthy"
    }
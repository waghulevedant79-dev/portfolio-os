from fastapi import APIRouter
from app.services.llm_service import ask_llm

router = APIRouter()

@router.get("/test-llm")
def test_llm():
    response = ask_llm("Hello! Who are you?")
    
    return {
        "Response": response
    }
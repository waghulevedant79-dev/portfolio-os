from fastapi import APIRouter
from app.services.llm_service import ask_llm
from fastapi.responses import StreamingResponse
from app.services.llm_service import stream_llm
from app.schemas.llm import PromptRequest

router = APIRouter()

@router.get("/test-llm")
def test_llm():
    response = ask_llm("Hello! Who are you?")
    
    return {
        "Response": response
    }
    
# here we are hardcoding the prompt 
"""
@router.get("/stream")
def stream():
    
    generator = stream_llm("Explain FastAPI in simple words?")
    
    return StreamingResponse(
        generator,
        media_type="text/plain"
    )
"""

# here we are get prompt from user 
@router.post("/stream")
def stream(request: PromptRequest):
    
    generator = stream_llm(request.prompt)
    
    return StreamingResponse(
        generator,
        media_type="text/plain"
    )
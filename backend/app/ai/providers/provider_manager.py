from app.core.settings import settings
from app.ai.providers.gemini import ask_gemini, stream_gemini

def ask_provider(prompt: str) -> str:
    
    if settings.LLM_PROVIDER == "gemini":
        return ask_gemini(prompt)
    
    raise ValueError("Unsupported Provider")

def stream_provider(prompt: str) -> str:
    
    if settings.LLM_PROVIDER == "gemini":
        return stream_gemini(prompt)
    
    raise ValueError("Unsupported Provider")
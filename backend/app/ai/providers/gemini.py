from google import genai
from app.core.settings import settings
from app.ai.config import generation_config

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def ask_gemini(prompt: str) -> str:
    
    response = client.models.generate_content(
        model=settings.LLM_MODEL,
        contents=prompt,
        config=generation_config
    )
    
    return response.text

def stream_gemini(prompt: str):
    
    response = client.models.generate_content_stream(
        model=settings.LLM_MODEL,
        contents=prompt,
        config=generation_config
    )
    
    for chunk in response:
        
        if chunk.text:
            
            yield chunk.text
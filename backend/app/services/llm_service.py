from app.ai.providers.provider_manager import ask_provider, stream_provider

def ask_llm(prompt: str) -> str:
    return ask_provider(prompt)

def stream_llm(prompt: str) -> str:
    return stream_provider(prompt)
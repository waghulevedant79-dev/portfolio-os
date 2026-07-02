from google.genai import types
from app.ai.prompts.system_prompt import SYSTEM_PROMPT

generation_config = types.GenerateContentConfig(
    
    system_instruction=SYSTEM_PROMPT,
    temperature=0.2,
    max_output_tokens=1024
)
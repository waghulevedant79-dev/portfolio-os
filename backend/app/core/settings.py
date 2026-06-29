from pydantic_settings import  BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME:str
    PROJECT_VERSION:str

    HOST:str
    PORT:int

    DEBUG:bool
    ENVIRONMENT:str
    
    class Config:
        env_file = ".env"
        
settings = Settings()
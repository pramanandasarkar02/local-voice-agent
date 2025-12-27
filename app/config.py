from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ollama_model: str
    whisper_model: str
    piper_voice: str

    class Config:
        env_file = ".env"

settings = Settings()

from pathlib import Path
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "RAG Agent"
    API_KEY: str
    BASE_URL: str
    MODEL_NAME: str
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 100
    VECTOR_DB: str = "data/faiss"
    DOCUMENT_PATH: str = "documents"
    class Config:
        env_file = ".env"

    Path("documents").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    Path("data").mkdir(exist_ok=True)
    Path("data/faiss").mkdir(parents=True, exist_ok=True)

    TOP_K: int = 5
    MIN_SCORE: float = 0.65
    TEMPERATURE: float = 0.0

settings = Settings()
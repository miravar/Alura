from functools import lru_cache
from app.rag import RAGService

@lru_cache
def get_rag():
    return RAGService()
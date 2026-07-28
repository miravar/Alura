from pathlib import Path
from langchain_community.vectorstores import FAISS
from app.embeddings import get_embeddings
from app.config import settings
from functools import lru_cache

class VectorStore:
    def __init__(self):
        self.embeddings = get_embeddings()
        self.path = Path(settings.VECTOR_DB)

    def create(self, chunks):
        db = FAISS.from_documents(
            chunks,
            self.embeddings
        )
        db.save_local(str(self.path))
        return db

    def load(self):
        return FAISS.load_local(
            str(self.path),
            self.embeddings,
            allow_dangerous_deserialization=True
        )
    
    @lru_cache
    def get_vectorstore():
        return VectorStore().load()
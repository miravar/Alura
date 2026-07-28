from app.vectorstore import VectorStore
from app.config import settings

class RetrievalService:
    def __init__(self):
        self.db = VectorStore().load()

    def search(self, question: str):
        results = self.db.similarity_search_with_score(
            question,
            k=settings.TOP_K
        )

        documents = []

        for doc, score in results:
            if score > settings.MAX_DISTANCE:
                continue
            documents.append(doc)

        return documents
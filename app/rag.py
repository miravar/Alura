from app.vectorstore import VectorStore
from app.llm import LLMClient
from app.prompts import USER_TEMPLATE

class RAGService:
    def __init__(self):
        self.db = VectorStore().load()
        self.llm = LLMClient()

    def ask(self, question: str):
        docs = self.db.similarity_search(
            question,
            k=4
        )
        context = ""
        sources = []

        for doc in docs:
            context += doc.page_content + "\n\n"
            source = f"{doc.metadata.get('source')} " \
                     f"(página {doc.metadata.get('page')})"
            if source not in sources:
                sources.append(source)

        prompt = USER_TEMPLATE.format(
            context=context,
            question=question
        )

        answer = self.llm.ask(prompt)

        return {
            "answer": answer,
            "sources": sources
        }
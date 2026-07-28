from app.prompts import USER_TEMPLATE
from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService
from app.services.memory_service import MemoryService
from app.logger import logger
import time

class RAGService:
    def __init__(self):
        self.retriever = RetrievalService()
        self.llm = LLMService()
        self.memory = MemoryService()

    def ask(self, question, session_id="default"):
        start = time.perf_counter()
        docs = self.retriever.search(question)
        context = ""
        sources = []

        for doc in docs:
            context += doc.page_content + "\n\n"
            source = (
                f"{doc.metadata['source']} "
                f"(página {doc.metadata['page']})"
            )

            if source not in sources:
                sources.append(source)

        history = ""

        for message in self.memory.history(session_id):
            history += f"{message['role']}: {message['content']}\n"

        prompt = USER_TEMPLATE.format(
            context=context,
            history=history,
            question=question
        )

        answer = self.llm.generate(prompt)
        self.memory.add(session_id, "Usuario", question)
        self.memory.add(session_id, "Asistente", answer)
        elapsed = time.perf_counter() - start

        logger.info(
            f"Tiempo respuesta: {elapsed:.2f}s"
        )

        return {
            "answer": answer,
            "sources": sources
        }
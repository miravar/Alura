from app.loader import DocumentLoader
from app.splitter import Splitter
from app.vectorstore import VectorStore
from app.config import settings
from app.logger import logger

class IndexService:
    def rebuild(self):
        logger.info("Reconstruyendo índice...")
        loader = DocumentLoader(settings.DOCUMENT_PATH)
        docs = loader.load()
        splitter = Splitter()
        chunks = splitter.split(docs)
        VectorStore().create(chunks)
        logger.info(
            f"Índice reconstruido ({len(chunks)} chunks)"
        )

        return len(chunks)
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from app.loader import DocumentLoader
from app.splitter import Splitter
from app.vectorstore import VectorStore
from app.config import settings

print("Leyendo documentos...")
loader = DocumentLoader(settings.DOCUMENT_PATH)
docs = loader.load()
print(f"Documentos cargados: {len(docs)}")
splitter = Splitter()
chunks = splitter.split(docs)
print(f"Chunks generados: {len(chunks)}")
store = VectorStore()
store.create(chunks)
print("Índice FAISS creado correctamente.")
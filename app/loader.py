from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)

SUPPORTED = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
    ".docx": Docx2txtLoader
}

class DocumentLoader:
    def __init__(self, folder: str):
        self.folder = Path(folder)

    def load(self):
        documents = []
        for file in self.folder.iterdir():
            if file.suffix.lower() not in SUPPORTED:
                continue
            loader = SUPPORTED[file.suffix.lower()](str(file))
            docs = loader.load()
            for doc in docs:
                doc.metadata["source"] = file.name
                documents.append(doc)
        return documents
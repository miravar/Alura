from fastapi import APIRouter
from app.models import QuestionRequest
from app.rag import RAGService

router = APIRouter()
rag = RAGService()

@router.post("/ask")

def ask(request: QuestionRequest):
    return rag.ask(request.question)
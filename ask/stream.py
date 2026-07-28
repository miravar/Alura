from fastapi.responses import StreamingResponse

@router.post("/ask/stream")
def ask_stream(request: QuestionRequest):
    return StreamingResponse(
        rag.stream(
            request.question,
            request.session_id
        ),
        media_type="text/plain"
    )
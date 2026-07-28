from fastapi import FastAPI
from app.config import settings
from app.api import router
from app.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="RAG Agent"
)

app.include_router(router)

@app.get("/")

def home():
    logger.info("Health Check")
    return {
        "application": settings.APP_NAME,
        "status": "running"
    }
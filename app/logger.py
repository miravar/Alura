from pathlib import Path
from loguru import logger

LOG_PATH = Path("logs")
LOG_PATH.mkdir(exist_ok=True)

logger.add(
    LOG_PATH / "rag.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
    enqueue=True
)
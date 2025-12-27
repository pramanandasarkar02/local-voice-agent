from loguru import logger

logger.add(
    "agent.log",
    rotation="10 MB",
    level="INFO",
)

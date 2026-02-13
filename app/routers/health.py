from fastapi import APIRouter

from app.config import Settings, get_settings
from app.logging_config import get_logger

router: APIRouter = APIRouter()
logger = get_logger(__name__)


@router.get("/health")
def health() -> dict[str, str]:
    settings: Settings = get_settings()

    logger.info("health_check_called")
    return {"status": "ok", "env": settings.app_env}

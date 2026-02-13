from fastapi import APIRouter, Depends

from app.config import Settings, get_settings
from app.dependencies import get_ping_service
from app.logging_config import get_logger
from app.services.ping_service import PingService

router: APIRouter = APIRouter()
logger = get_logger(__name__)


@router.get("/health")
def health(service: PingService = Depends(get_ping_service)) -> dict[str, str]:
    settings: Settings = get_settings()

    logger.info("health_check_called")
    return {"status": "ok", "env": settings.app_env, "ping": service.execute()}

from fastapi import APIRouter

from app.config import Settings, get_settings

router: APIRouter = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    settings: Settings = get_settings()

    return {"status": "ok", "env": settings.app_env}

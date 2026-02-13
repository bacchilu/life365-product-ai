from fastapi import FastAPI

from app.config import Settings, get_settings
from app.logging_config import configure_logging
from app.routers.health import router as health_router

configure_logging()

settings: Settings = get_settings()


app: FastAPI = FastAPI(title=settings.app_name)
app.include_router(health_router)

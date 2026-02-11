from fastapi import FastAPI

from app.config import Settings, get_settings
from app.routers.health import router as health_router

settings: Settings = get_settings()


app: FastAPI = FastAPI(title=settings.app_name)
app.include_router(health_router)

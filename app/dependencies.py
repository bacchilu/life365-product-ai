from app.services.ping_service import PingService


def get_ping_service() -> PingService:
    return PingService()

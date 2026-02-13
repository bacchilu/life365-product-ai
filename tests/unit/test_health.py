import pytest
from fastapi.testclient import TestClient
from httpx import Response

from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_health(client: TestClient):
    res: Response = client.get("/health")

    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_ping_service(client: TestClient):
    res: Response = client.get("/health")

    assert res.status_code == 200
    assert res.json()["ping"] == "pong"

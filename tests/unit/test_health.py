from fastapi.testclient import TestClient
from httpx import Response

from app.main import app

client: TestClient = TestClient(app)


def test_health():
    res: Response = client.get("/health")

    assert res.status_code == 200
    assert res.json()["status"] == "ok"

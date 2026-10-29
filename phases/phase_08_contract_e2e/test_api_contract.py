from fastapi.testclient import TestClient
from practice.api_app import app


def test_health_response_contract():
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    body = response.json()
    assert set(body) == {"status"}
    assert isinstance(body["status"], str)

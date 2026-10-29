from fastapi.testclient import TestClient
from practice.api_app import app


def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_customer_returns_contract():
    client = TestClient(app)
    response = client.post("/customers", json={"name": "Test Store"})
    assert response.status_code == 201
    body = response.json()
    assert isinstance(body["id"], int)
    assert body["name"] == "Test Store"


def test_customer_name_validation():
    client = TestClient(app)
    response = client.post("/customers", json={"name": "X"})
    assert response.status_code == 422

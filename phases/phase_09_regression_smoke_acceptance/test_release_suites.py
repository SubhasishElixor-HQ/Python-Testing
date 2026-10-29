import pytest
from fastapi.testclient import TestClient
from practice.api_app import app


@pytest.mark.smoke
def test_health_smoke():
    response = TestClient(app).get("/health")
    assert response.status_code == 200


@pytest.mark.regression
def test_customer_creation_regression():
    response = TestClient(app).post("/customers", json={"name": "Regression Shop"})
    assert response.status_code == 201
    assert response.json()["name"] == "Regression Shop"


@pytest.mark.acceptance
def test_customer_workflow_acceptance():
    client = TestClient(app)
    created = client.post("/customers", json={"name": "Acceptance Shop"})
    assert created.status_code == 201
    customer_id = created.json()["id"]

    retrieved = client.get(f"/customers/{customer_id}")
    assert retrieved.status_code == 200
    assert retrieved.json()["name"] == "Acceptance Shop"

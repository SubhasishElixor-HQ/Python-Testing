from fastapi import FastAPI, Header, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()
CUSTOMERS = {
    1: {"id": 1, "organization_id": "org-a", "name": "A Store"},
    2: {"id": 2, "organization_id": "org-b", "name": "B Store"},
}


def get_customer_for_organization(customer_id: int, organization_id: str):
    customer = CUSTOMERS.get(customer_id)
    if customer is None or customer["organization_id"] != organization_id:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@app.get("/customers/{customer_id}")
def read_customer(customer_id: int, x_organization_id: str = Header(default="")):
    if not x_organization_id:
        raise HTTPException(status_code=401, detail="Missing organization identity")
    return get_customer_for_organization(customer_id, x_organization_id)


client = TestClient(app)


def test_same_organization_can_read_customer():
    response = client.get("/customers/1", headers={"X-Organization-Id": "org-a"})
    assert response.status_code == 200


def test_cross_organization_customer_is_not_disclosed():
    response = client.get("/customers/2", headers={"X-Organization-Id": "org-a"})
    assert response.status_code == 404


def test_missing_identity_is_rejected():
    response = client.get("/customers/1")
    assert response.status_code == 401

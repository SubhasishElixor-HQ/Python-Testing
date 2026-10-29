from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class CustomerCreateRequest(BaseModel):
    name: str = Field(min_length=2)


class CustomerResponse(BaseModel):
    id: int
    name: str


_CUSTOMERS: dict[int, CustomerResponse] = {}
_NEXT_ID = 1


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/customers", status_code=201, response_model=CustomerResponse)
def create_customer(payload: CustomerCreateRequest) -> CustomerResponse:
    global _NEXT_ID
    customer = CustomerResponse(id=_NEXT_ID, name=payload.name)
    _CUSTOMERS[_NEXT_ID] = customer
    _NEXT_ID += 1
    return customer


@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int) -> CustomerResponse:
    customer = _CUSTOMERS.get(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

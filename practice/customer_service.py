class CustomerNotFoundError(LookupError):
    pass


class InMemoryCustomerRepository:
    def __init__(self) -> None:
        self._customers: dict[int, dict[str, object]] = {}

    def add(self, customer_id: int, name: str) -> None:
        self._customers[customer_id] = {"id": customer_id, "name": name}

    def get(self, customer_id: int) -> dict[str, object]:
        customer = self._customers.get(customer_id)
        if customer is None:
            raise CustomerNotFoundError(f"Customer {customer_id} not found")
        return customer

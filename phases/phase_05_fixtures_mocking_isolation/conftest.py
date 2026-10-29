import pytest
from practice.customer_service import InMemoryCustomerRepository


@pytest.fixture
def customer_repository():
    # A new repository for every test keeps test state isolated.
    return InMemoryCustomerRepository()

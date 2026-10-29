from unittest.mock import Mock
import pytest
from practice.customer_service import CustomerNotFoundError


def test_fixture_provides_isolated_repository(customer_repository):
    customer_repository.add(1, "Test Store")
    assert customer_repository.get(1) == {"id": 1, "name": "Test Store"}


def test_missing_customer_raises_domain_error(customer_repository):
    with pytest.raises(CustomerNotFoundError):
        customer_repository.get(404)


def test_mock_external_notification_service():
    notifier = Mock()
    notifier.send("Customer created")

    notifier.send.assert_called_once_with("Customer created")

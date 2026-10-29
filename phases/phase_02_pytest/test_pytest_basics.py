import pytest


@pytest.mark.smoke
def test_pytest_assertion_basics():
    assert "testing".upper() == "TESTING"


@pytest.mark.parametrize(
    ("value", "expected"),
    [(1, True), (100, True), (0, False), (101, False)],
)
def test_parametrized_cases(value, expected):
    from practice.math_rules import is_valid_quantity

    assert is_valid_quantity(value) is expected

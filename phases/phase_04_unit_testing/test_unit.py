import pytest
from practice.math_rules import apply_discount, add


def test_add():
    assert add(4, 6) == 10


@pytest.mark.parametrize(
    ("price", "discount", "expected"),
    [(1000, 0, 1000), (1000, 10, 900), (999, 100, 0)],
)
def test_apply_discount(price, discount, expected):
    assert apply_discount(price, discount) == expected


@pytest.mark.parametrize(
    ("price", "discount"),
    [(-1, 10), (100, -1), (100, 101), (True, 10), (100, True)],
)
def test_apply_discount_rejects_invalid_values(price, discount):
    with pytest.raises(ValueError):
        apply_discount(price, discount)

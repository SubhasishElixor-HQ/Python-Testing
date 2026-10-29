import pytest

from practice.math_rules import is_valid_quantity


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, False),       # below lower boundary
        (1, True),        # lower boundary
        (50, True),      # typical valid value
        (100, True),     # upper boundary
        (101, False),    # above upper boundary
        (True, False),   # bool is a subclass of int, but not accepted here
        ("10", False),   # wrong type
        (None, False),   # missing value
    ],
)
def test_quantity_boundary_and_invalid_cases(value, expected):
    assert is_valid_quantity(value) is expected

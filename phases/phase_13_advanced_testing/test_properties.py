from hypothesis import given
from hypothesis import strategies as st

from practice.math_rules import is_valid_quantity


@given(st.integers())
def test_quantity_property_for_all_generated_integers(value):
    assert is_valid_quantity(value) is (1 <= value <= 100)


@given(st.one_of(st.text(), st.floats(allow_nan=True), st.none(), st.booleans()))
def test_non_integer_values_are_rejected(value):
    assert is_valid_quantity(value) is False

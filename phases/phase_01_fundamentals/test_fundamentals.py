from practice.math_rules import add


def test_add_two_positive_numbers():
    # Arrange
    left = 2
    right = 3

    # Act
    result = add(left, right)

    # Assert
    assert result == 5

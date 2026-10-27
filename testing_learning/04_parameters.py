import pytest
import sys

@pytest.mark.parametrize(
    "username, password",
    [
        ("user1", "python"),
        ("user2", "pytest"),
        ("user3", "automation"),
        ("user4", "testing"),
    ]
)       
def test_login(username, password):
    print(f"Testing login functionality for {username} with password {password}...")
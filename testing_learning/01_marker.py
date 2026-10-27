# custom markers in pytest
import pytest

@pytest.mark.smoke
def test_login():
    print("This is a test login function.")

@pytest.mark.regression
def test_add_to_cart():
    print("This is a test add to cart function.")
@pytest.mark.regression
def test_checkout():
    print("This is a test checkout function.")
@pytest.mark.smoke
def test_logout():
    print("This is a test logout function.")    
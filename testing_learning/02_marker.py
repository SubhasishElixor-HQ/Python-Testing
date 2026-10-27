import pytest

@pytest.mark.skip
def test_skip():
    print("This is a test skip function.")

@pytest.mark.skipif(1==1, reason="Skipping this test because the condition is True")
def test_skipif():
    print("This is a test skipif function.")

@pytest.mark.xfail
def test_xfail():
    print("This is a test xfail function.")
    assert 1 == 2, "This test is expected to fail."

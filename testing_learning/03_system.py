import sys

import pytest

print(sys.version_info)


@pytest.mark.skipif(sys.version_info < (3, 6), reason="Skipping this test because Python version is less than 3.6")
def test_skipif():
    print("This is a test skipif function.")


@pytest.mark.xfail
def test_xfail():
    assert True
    assert False, "This test is expected to fail."
    print("This is a test xfail function.")

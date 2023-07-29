import pytest


@pytest.fixture()
def setup():
    print("once before every method")

def testMethodFirst(setup):
    print("this is first method")

def testMethodTwo():
     print("this is second method")

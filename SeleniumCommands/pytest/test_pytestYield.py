import pytest


@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once after every test method")

def testMethodOne(setup):
    print("this is method one")

def testMethosTwo(setup):
    print("this is test method two")
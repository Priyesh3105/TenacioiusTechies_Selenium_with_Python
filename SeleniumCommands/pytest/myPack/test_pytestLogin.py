import pytest


@pytest.yield_fixture()
def setup():
    print("opening url to login")
    yield
    print("closing browser after login")

def test_loginByEmail(setup):
    print("this is login by email test")

def test_loginByFcebook(setup):
    print("this is login by facebook test")
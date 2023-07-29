import pytest


@pytest.fixture()
def setup():
    print("opening url to sign up")
    yield
    print("closing browser after sign up")

def test_signUpByEmail(setup):
    print("this is signUp by email test")

def test_signUpByFcebook(setup):
    print("this is signUp by facebook test")
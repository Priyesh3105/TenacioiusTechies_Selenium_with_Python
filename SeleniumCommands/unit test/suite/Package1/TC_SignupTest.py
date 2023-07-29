import unittest

class SignupTest(unittest.TestCase):
    def test_SignupByEmail(self):
        print("This Signup by email test")
        self.assertTrue(True)

    def test_SignupByFacebook(self):
        print("This Signup by Facebook test")
        self.assertTrue(True)

    def test_SignupByTwitter(self):
        print("This Signup by Twitter test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
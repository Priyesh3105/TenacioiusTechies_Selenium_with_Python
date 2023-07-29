import unittest

class PaymentTest(unittest.TestCase):
    def test_PaymentInDollor(self):
        print("This PaymentInDollor test")
        self.assertTrue(True)

    def test_PaymentInRupees(self):
        print("This PaymentInRupees test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
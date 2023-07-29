import unittest

class SearchEnginesTest(unittest.TestCase):

    def test_greater(self):
        self.assertGreater(100,10)

    def test_greater_equal(self):
        self.assertGreaterEqual(100,100)

    def test_lesser(self):
        self.assertLess(10,100)

    def test_lesser_equal(self):
        self.assertLessEqual(100,100)

if __name__ == "__main__":
    unittest.main()
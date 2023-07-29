import unittest

class SearchEnginesTest(unittest.TestCase):

    def test_none(self):
        list = ["a", "b", "c", "d", "e"]
        self.assertIn("a", list)

    def test_not_none(self):
        list = ["a", "b", "c", "d", "e"]
        self.assertNotIn("f", list)

if __name__ == "__main__":
    unittest.main()
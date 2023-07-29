import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")

    def tearDown(self):
        self.driver.quit()

    def test_Google(self):
        self.driver.get("https://www.google.com/")
        self.assertIn("Google", self.driver.title)

    def test_being(self):
        self.driver.get("https://bing.com/")
        self.assertIn("Bing", self.driver.title)

if __name__ == "__main__":
    unittest.main()
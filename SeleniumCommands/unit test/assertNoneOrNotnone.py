import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    def test_none(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        driver.get("https://www.google.com/")
        pageTitle1 = None
        self.assertIsNone(pageTitle1)
        driver.quit()
    def test_not_none(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        driver.get("https://www.google.com/")
        pageTitle2 = driver.title
        self.assertIsNotNone(pageTitle2)
        driver.quit()

if __name__ == "__main__":
    unittest.main()
import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    def test_equal(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        driver.get("https://www.google.com/")
        pageTitle1 = driver.title
        self.assertTrue(pageTitle1 == "Google")
        driver.quit()
    def test_not_equal(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        driver.get("https://www.google.com/")
        pageTitle2 = driver.title
        self.assertFalse(pageTitle2 == "Google123")
        driver.quit()

if __name__ == "__main__":
    unittest.main()
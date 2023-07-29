import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):

    def test_equal(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        driver.get("https://www.google.com/")
        pageTitle1 = driver.title
        self.assertEqual("Google", pageTitle1, "webpage title is not same")
        driver.quit()
    def test_not_equal(self):
        driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        driver.get("https://www.google.com/")
        pageTitle2 = driver.title
        self.assertNotEqual("Google123", pageTitle2, "webpage title is not same")
        driver.quit()

if __name__ == "__main__":
    unittest.main()
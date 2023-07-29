from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

class FoodChowTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homepageTitle(self):
        self.driver.get("https://www.foodchow.com/RestaurantLogin")
        self.assertEqual("RestaurantLog-in or Sign-up|FoodChow: An Online Food Ordering" ,self.driver.title,"webpage title is not matching")

    def test_login(self):
        self.driver.find_element(By.NAME, 'Email_Id').send_keys("ravatrohit670@gmail.com")
        self.driver.find_element(By.NAME, 'Password').send_keys("1234567")
        self.driver.find_element(By.XPATH, "//button[@class ='btn btn-primary btn-raised']").click()
        self.assertEqual("foodchowpizzahut Restaurant Admin", self.driver.title,"webpage title is not matching")

    #def test_anything(self):
        #self.driver.find_element(By.NAME, 'Email_Id')
        #self.driver.find_element(By.XPATH, "//button[@class ='btn btn-primary btn-raised']").click()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = '..\\reports'))
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestFoodchowLogin():

    @pytest.fixture()
    def setup(self):
        global driver
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homepageTitle(self,setup):
        self.driver.get("https://www.foodchow.com/RestaurantLogin")
        assert self.driver.title == "RestaurantLog-in or Sign-up|FoodChow: An Online Food Ordering"

    def test_login(self,setup):
        self.driver.get("https://www.foodchow.com/RestaurantLogin")
        self.driver.find_element(By.NAME, 'Email_Id').send_keys("ravatrohit670@gmail.com")
        self.driver.find_element(By.NAME, 'Password').send_keys("1234567")
        self.driver.find_element(By.XPATH, "//button[@class ='btn btn-primary btn-raised']").click()
        assert self.driver.title == "foodchowpizzahut Restaurant Admin"

    def test_anything(self,setup):
        self.driver.find_element(By.NAME, 'Email_Id')
        self.driver.find_element(By.XPATH, "//button[@class ='btn btn-primary btn-raised']").click()

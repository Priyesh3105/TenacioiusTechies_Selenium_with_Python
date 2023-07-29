from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

print("simple test case started")
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.foodchow.com/RestaurantLogin")
print(driver.title)
time.sleep(2)
driver.find_element(By.NAME, 'Email_Id').send_keys("android@tenacioustechies.com")
time.sleep(2)
driver.find_element(By.NAME, 'Password').send_keys("123456")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn btn-primary btn-raised']").click()
time.sleep(2)
driver.close()
print("test succesfull")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("simple test case started")

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open tenacious techies website
driver.get("https://www.foodchow.com")
print(driver.title)
time.sleep(2)

#opening food chow web site
driver.get("https://www.foodchow.com/foodchowdemoindia")
print(driver.title)
time.sleep(2)

#go backward
driver.back()
print(driver.title)
time.sleep(2)
#go farword
driver.forward()
print(driver.title)
time.sleep(2)

time.sleep(2)
driver.quit()
print("test succesfull")
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("simple test case started")

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open the foodchowdemoindia page
driver.get("https://www.foodchow.com/foodchowdemoindia/order-online")
print(driver.title)
time.sleep(2)

#define the element
cate_ele= driver.find_element(By.XPATH, "//*[@id='men_8']/a")
time.sleep(2)

#use the conditional commands
print(cate_ele.is_displayed())
time.sleep(2)
print(cate_ele.is_enabled())
time.sleep(2)

#select the category
cate_ele.click()
time.sleep(2)

#check that cate_ele is selected or not
print(cate_ele.is_selected())
time.sleep(2)

#close the driver
driver.close()

#print test succesful
print("Test succesfull")
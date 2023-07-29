from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("simple test case started")

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")

#open the foodchow page
driver.get("https://www.foodchow.com/foodchowdemoindia")
print(driver.title)
time.sleep(2)

#click on order online page
ord_ele =driver.find_element(By.XPATH, "//a[@class ='nav-link btn']")
#make drivar wait for pages to load
driver.implicitly_wait(10)
ord_ele.click()
print(driver.title)
time.sleep(2)

#define the element
cate_ele= driver.find_element(By.XPATH, "//*[@id='men_8']/a")
time.sleep(2)

#use the conditional commands
print(cate_ele.is_displayed())
time.sleep(2)

#close the driver
driver.close()

#print test succesful
print("Test succesfull")
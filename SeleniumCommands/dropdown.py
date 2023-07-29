from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

print("simple test case started")
#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open the form pageviewform
driver.get("https://the-internet.herokuapp.com/dropdown")
print(driver.title)
time.sleep(2)

#find the dropdown menu
ele = driver.find_element(By.XPATH, "//*[@id='dropdown']")
drp = Select(ele)

#select by visible text
drp.select_by_visible_text("Option 1")
time.sleep(2)
print("Selected option using Select class: ", drp.first_selected_option.text)
time.sleep(2)

#select by index
drp.select_by_index(2)
time.sleep(2)
print("Selected option using Select class: ", drp.first_selected_option.text)
time.sleep(2)

#slect by value(in this from value is not given so this will not work
drp.select_by_value("1")
time.sleep(2)
print("Selected option using Select class: ", drp.first_selected_option.text)
time.sleep(2)

#close the driver
driver.close()

#print test succesful
print("Test succesfull")
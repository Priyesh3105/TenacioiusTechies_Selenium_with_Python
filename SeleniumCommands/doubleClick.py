from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the nested frames page
driver.get("https://www.wikipedia.org/")
time.sleep(2)

# print title
print(driver.title)

# find user 1 element
lang_1 = driver.find_element(By.XPATH, "//*[@id='js-link-box-en']/small")

# use action chains
actions = ActionChains(driver)

actions.double_click(lang_1).perform()

# print title
print(driver.title)

time.sleep(2)
driver.close()
print("test succesfull")
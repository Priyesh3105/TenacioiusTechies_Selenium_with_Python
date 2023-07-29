from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the nested frames page
driver.get("https://demoqa.com/buttons")
time.sleep(2)

# print title
print(driver.title)

# find user 1 element
ryt = driver.find_element(By.XPATH, "//*[@id='rightClickBtn']")

# use action chains
actions = ActionChains(driver)

actions.context_click(ryt).perform()

# Get the text from the bottom frame
result = driver.find_element(By.TAG_NAME, "p").text
print(result)
time.sleep(2)


time.sleep(2)
driver.close()
print("test succesfull")
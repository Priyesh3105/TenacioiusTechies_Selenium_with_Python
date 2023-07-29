from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the nested frames page
driver.get("https://demoqa.com/droppable")
time.sleep(2)

# find user 1 element
src_ele = driver.find_element(By.ID, "draggable")
tgt_ele = driver.find_element(By.ID, "droppable")


# use action chains
actions = ActionChains(driver)

actions.drag_and_drop(src_ele, tgt_ele).perform()


time.sleep(2)
driver.close()
print("test succesfull")
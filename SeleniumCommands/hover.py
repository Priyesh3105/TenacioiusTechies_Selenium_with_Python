from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the nested frames page
driver.get("https://the-internet.herokuapp.com/hovers")
time.sleep(2)

# find user 1 element
user_1 = driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/img")
view = driver.find_element(By.XPATH, "//*[@id='content']/div/div[1]/div/a")

# use action chains
actions = ActionChains(driver)

actions.move_to_element(user_1).move_to_element(view).click().perform()

time.sleep(2)
driver.close()
print("test succesfull")



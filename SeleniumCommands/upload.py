from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the nested frames page
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(2)

# find and upload
driver.find_element(By.XPATH, "//*[@id='file-upload']").send_keys("C://Users//HP//Pictures//Screenshot 2022-07-30 153737.png")
driver.find_element(By.XPATH, "//*[@id='file-submit']").click()
time.sleep(2)

# print the uploaded file
print(driver.find_element(By.XPATH,"//*[@id='uploaded-files']").text)
time.sleep(2)
driver.close()
print("test succesfull")
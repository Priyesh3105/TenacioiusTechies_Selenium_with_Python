from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("simple test case started")
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("tenacious techies")
time.sleep(5)
driver.find_element(By.NAME, 'btnK').send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH,"//h3[@class ='LC20lb MBeuO DKV0Md']").click()
time.sleep(5)
links = driver.find_elements(By.TAG_NAME, 'a')

for link in links:
    print(link.get_attribute('href'))
time.sleep(5)

buttons = driver.find_elements(By.TAG_NAME, 'button')
for button in buttons:
    print(button.get_attribute('id'))
driver.close()
print("test succesfull")
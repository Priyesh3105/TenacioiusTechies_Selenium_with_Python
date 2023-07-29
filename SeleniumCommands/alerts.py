from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("simple test case started")
# opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()

# open the page for alert
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
print(driver.title)
time.sleep(2)

# find the dropdown menu
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button").click()
time.sleep(2)

# handle the alert
driver.switch_to.alert.accept()
time.sleep(2)
result = driver.find_element(By.XPATH , "//*[@id='result']")
print(result.text)
time.sleep(2)

# find the dropdown menu
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button").click()
time.sleep(2)

# handle the alert
driver.switch_to.alert.dismiss()
time.sleep(2)
result = driver.find_element(By.XPATH , "//*[@id='result']")
print(result.text)
time.sleep(2)

# find the dropdown menu
driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(2)

# handle the alert
driver.switch_to.alert.send_keys("This is a test message by priyesh")
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
result = driver.find_element(By.XPATH , "//*[@id='result']")
print(result.text)
time.sleep(2)

# close the driver
driver.close()

# print test succesful
print("Test succesfull")
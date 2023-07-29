from selenium import webdriver
import time

# starting the test
print("simple test case started")

# start the driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.foodchow.com")
print(driver.title)
time.sleep(2)

# take screen shot by method save_screenshot()
driver.save_screenshot("C:\\Users\\HP\\Pictures\\Screenshots\\one.png")

# by another method
driver.get_screenshot_as_file("C:\\Users\\HP\Pictures\\Screenshots\\second.png")

#close the driver
driver.close()

#print test succesful
print("Test succesfull")


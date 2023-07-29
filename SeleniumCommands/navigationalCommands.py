from selenium import webdriver
import time

print("simple test case started")

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open the foodchowdemoindia page
driver.get("https://www.foodchow.com/foodchowdemoindia")
print(driver.title)
time.sleep(2)

#open foodchow website
driver.get("https://www.foodchow.com")
print(driver.title)
time.sleep(2)

#click on bcakward button
driver.back()
time.sleep(2)
print(driver.title)

#click on bcakward button
driver.forward()
time.sleep(2)
print(driver.title)

#close the driver
driver.close()

#print test succesful
print("Test succesfull")

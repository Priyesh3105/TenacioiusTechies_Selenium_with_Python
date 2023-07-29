import XLUnits
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# starting the test
print("simple test case started")

# start the driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.foodchow.com/RestaurantLogin")
print(driver.title)
time.sleep(2)

# read the data
path = "C://Users/HP/Documents/login.xlsx"
rows = XLUnits.getRowCount(path, 'Sheet1')

# test starts here
for r in  range(2, rows+1) :
    username = XLUnits.readData(path, 'Sheet1',r,1)
    password = XLUnits.readData(path, 'Sheet1',r,2)

    driver.find_element(By.NAME, 'Email_Id').clear()
    driver.find_element(By.NAME, 'Email_Id').send_keys(username)
    time.sleep(2)
    driver.find_element(By.NAME, 'Password').clear()
    driver.find_element(By.NAME, 'Password').send_keys(password)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class ='btn btn-primary btn-raised']").click()
    time.sleep(2)

    if driver.title == "foodchowdemoindia Restaurant Admin" :
        print("pass")
        XLUnits.writeData(path, "Sheet1", r, 3, "pass")
    else:
        print("fail")
        XLUnits.writeData(path, "Sheet1", r, 3, "fail")
        errMsg = driver.find_element(By.XPATH, "//*[@id='message-result']").text
        XLUnits.writeData(path, "Sheet1", r, 4, errMsg)
    driver.back()

#close the driver
driver.close()

#print test succesful
print("Test succesfull")

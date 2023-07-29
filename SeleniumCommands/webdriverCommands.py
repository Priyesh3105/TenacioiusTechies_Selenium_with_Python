from selenium import webdriver
import time

print("simple test case started")

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open foodchow website
driver.get("https://www.foodchow.com")
print(driver.title)
time.sleep(2)

#print the cuurent page url
print(driver.current_url)
time.sleep(2)

driver.close()
#driver.quit() is useful when two or more windows are open


#print test succesful
print("Test succesfull")

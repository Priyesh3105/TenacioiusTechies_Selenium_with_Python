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

# get and print the cookies
cookies = driver.get_cookies()

print(len(cookies))

print(cookies)

# add a new cookie in your browser
cookie = {'name': 'mariCookie', 'value': '3487475523237'}
driver.add_cookie(cookie)

# get and print the cookies
cookies = driver.get_cookies()

print(len(cookies))

print(cookies)

# delete the cookie
driver.delete_cookie('mariCookie')

# get and print the cookies
cookies = driver.get_cookies()

print(len(cookies))

print(cookies)

#close the driver
driver.close()

#print test succesful
print("Test succesfull")



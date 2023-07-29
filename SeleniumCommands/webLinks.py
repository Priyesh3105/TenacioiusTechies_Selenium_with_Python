from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("simple test case started")

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open the foodchow page
driver.get("https://www.foodchow.com/foodchowdemoindia")
print(driver.title)
time.sleep(2)

#find  all the links present in the page
links = driver.find_elements(By.TAG_NAME, "a")
time.sleep(2)

#print the number of links present in the page
print("here is the number of links present in the page : ",len(links))
time.sleep(2)

#print the text asociated with the links present in the page
for link in links:
    print(link.text)

#close the browser
driver.close()

#print test succesfull
print("test succesfull")


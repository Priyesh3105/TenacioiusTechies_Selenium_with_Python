from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("simple test case started")

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open the foodchow page
driver.get("https://www.foodchow.com/foodchowdemoindia")
print(driver.title)
time.sleep(2)

#scroll the page
driver.execute_script("window.scrollBy(0,1000)")

# scrolling by another method
flag = driver.find_element(By.XPATH,"/html/body/section[6]/div/div/div[1]/div/form/div/div[1]/input")
driver.execute_script("arguments[0].scrollIntoView();", flag)

#anothe method
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")


time.sleep(2)
driver.close()
print("test succesfull")

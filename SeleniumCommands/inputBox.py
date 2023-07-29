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

#make drivar wait for pages to load
driver.implicitly_wait(3)
#click on order online page
driver.find_element(By.XPATH, "//a[@class ='nav-link btn']").click()
print(driver.title)
time.sleep(2)

#find how many input boxes are there
inputBoxes = driver.find_elements(By.TAG_NAME, "input")
print(len(inputBoxes))

#search item and add to cart
driver.find_element(By.XPATH, '//*[@id="main-menu-section"]/div/div[2]/div[2]/div[1]/div/div/input').send_keys("Handi Biryani")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="24746"]/div[2]/div/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)

#close the driver
driver.close()

#print test succesful
print("Test succesfull")
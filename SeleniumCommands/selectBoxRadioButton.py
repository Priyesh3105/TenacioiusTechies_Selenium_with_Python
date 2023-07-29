from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("simple test case started")
#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open the form page
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdyYHa4nTQ3qZH34LF2sxfWZOf1u8CUWNF3fTBhz2nWnAPfFw/viewform")
print(driver.title)
time.sleep(2)

#find radio buttons and check whether they are selected or not.if not then select an option
button_ele = driver.find_element(By.XPATH, "//*[@id='i5']/div[3]/div")
if not button_ele.is_selected():
    button_ele.click()
    print("radio button is selected")
else:
    print("radio button was already selected")
time.sleep(2)

#find radio buttons and check whether they are selected or not.if not then select an option
button_ele = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/label")
if not button_ele.is_selected():
    button_ele.click()
    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/label").click()
    driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/label").click()
    print("select box is selected")
else:
    print("select box was already selected")
time.sleep(2)


#close the driver
driver.close()

#print test succesful
print("Test succesfull")

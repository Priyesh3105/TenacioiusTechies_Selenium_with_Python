from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("simple test case started")

# opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

# open the foodchow page
driver.get("https://www.foodchow.com/foodchowdemoindia")
print(driver.title)
time.sleep(2)

# click on restaurant login
driver.find_element(By.XPATH, "/html/body/header/nav[1]/div/div[2]/ul/li[2]/a").click()
time.sleep(5)

# print window handel
print(driver.current_window_handle)
time.sleep(2)

handles = driver.window_handles  # get all the handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

time.sleep(2)
driver.quit()
print("test succesfull")
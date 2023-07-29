from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("Simple test case started")

# Opening the WebDriver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

# Open the table page
driver.get("https://the-internet.herokuapp.com/tables")
print(driver.title)
time.sleep(2)

rows = len(driver.find_elements(By.XPATH, "//*[@id='table1']/tbody/tr"))
cols = len(driver.find_elements(By.XPATH, "//*[@id='table1']/tbody/tr[1]/td"))

# Get the table heading
heading_row = driver.find_elements(By.XPATH, "//*[@id='table1']/thead/tr/th")
for heading in heading_row:
    print(heading.text, end='    ')
print()

for r in range(1, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element(By.XPATH, "//*[@id='table1']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(value, end='     ')
    print()

time.sleep(2)
driver.quit()
print("Test successful")
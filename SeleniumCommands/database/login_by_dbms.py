from selenium import webdriver
import cx-Oracle
import os
import time
os.environ['PATH'] ='E:\\app\OracleHomeUser\\instantclient_18_3'

#opening web driver
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()

#open the foodchow page
driver.get("https://www.foodchow.com/RestaurantLogin")
print(driver.title)
time.sleep(2)

# Establish connection to the database

con=cx-Oracle.connect("hr","hr","localhost/pdborcl")

cur = con.cursor()

query1="select * From users"

cur.execute(query1)

for cols in cur:
    driver.find_element(By.NAME, 'Email_Id').send_keys(cols[0])
    time.sleep(2)
    driver.find_element(By.NAME, 'Password').send_keys(cols[1])
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class ='btn btn-primary btn-raised']").click()
    time.sleep(2)

    #validation
    if driver .title == "foodchowpizzahut Restaurant Admin":
        print("test passed")
    else:
        print("test failed")
    driver.back()

cur.close()
con.commit()
con.close()

print("completed!!!")
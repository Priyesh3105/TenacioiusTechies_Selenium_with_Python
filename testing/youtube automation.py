from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("simple test case started")
driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.find_element(By.NAME, 'q').send_keys("YouTube")
time.sleep(2)
driver.find_element(By.NAME, 'btnK').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH,"//h3[@class ='LC20lb MBeuO DKV0Md']").click()
time.sleep(2)
driver.find_element(By.NAME, 'search_query').send_keys("gec surat")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class ='style-scope ytd-searchbox']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//ytd-video-renderer[@class ='style-scope ytd-item-section-renderer']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@class ='yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start ']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//button[@class ='yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--segmented-end ']").click()
time.sleep(5)
driver.close()
print("test succesfull")
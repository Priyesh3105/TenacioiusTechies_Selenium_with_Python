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

#make drivar wait for pages to load
driver.implicitly_wait(3)
#click on order online page
driver.find_element(By.XPATH, "//a[@class ='nav-link btn']").click()
print(driver.title)
time.sleep(2)

#search item and add to cart
driver.find_element(By.XPATH, '//*[@id="main-menu-section"]/div/div[2]/div[2]/div[1]/div/div/input').send_keys("Handi Biryani")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="24746"]/div[2]/div/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)

#clear filter
driver.find_element(By.XPATH, '//*[@id="main-menu-section"]/div/div[2]/div[2]/div[1]/div/div/input').clear()
time.sleep(2)

#choose the category - south indian
driver.find_element(By.XPATH, "//*[@id='men_0']/a").send_keys(Keys.DOWN)
driver.find_element(By.XPATH, "//*[@id='men_0']/a").click()
time.sleep(2)
#add item - masala dosa
driver.find_element(By.XPATH, "//*[@id='24655']/div[2]/div/div[2]/div/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)

#add item - idali sambhar
driver.find_element(By.XPATH, "//*[@id='24655']/div[3]/div/div[2]/div/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)

#choose the category - milk product
driver.find_element(By.XPATH, "//*[@id='men_4']/a").click()
time.sleep(2)


#add item - cold coffe
driver.find_element(By.XPATH, "//*[@id='24745']/div[6]/div/div[2]/div/div[2]/button").send_keys(Keys.DOWN)
driver.find_element(By.XPATH, "//*[@id='24745']/div[6]/div/div[2]/div/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)


#add item - butter
driver.find_element(By.XPATH, "//*[@id='24745']/div[4]/div/div[2]/div/div[2]/button").send_keys(Keys.UP)
driver.find_element(By.XPATH, "//*[@id='24745']/div[4]/div/div[2]/div/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)


#choose the category - desert
driver.find_element(By.XPATH, "//*[@id='men_8']/a").click()
time.sleep(2)


#add item - tc ice cream
driver.find_element(By.XPATH, "//*[@id='24742']/div[6]/div/div[2]/div/div[2]/button").send_keys(Keys.DOWN)
driver.find_element(By.XPATH, "//*[@id='24742']/div[6]/div/div[2]/div/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)


#add item - orange juice
driver.find_element(By.XPATH, "//*[@id='24742']/div[2]/div/div[2]/div/div[2]/button").send_keys(Keys.UP)
driver.find_element(By.XPATH, "//*[@id='24742']/div[2]/div/div[2]/div/div[2]/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class ='btn modal-btn']").click()
time.sleep(2)

#increase any item
driver.find_element(By.XPATH, '//*[@id="item-list-cart"]/div/div[1]/div/table/tbody/tr[1]/td[3]/div/div/span[2]').click()
time.sleep(2)

#decrease any item
driver.find_element(By.XPATH, '//*[@id="item-list-cart"]/div/div[1]/div/table/tbody/tr[1]/td[3]/div/div/span[1]').click()
time.sleep(2)

#come out of cart
driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]').click()
time.sleep(2)

#reach end
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
time.sleep(2)

#proceed to check out
driver.find_element(By.XPATH, "//*[@id='item-list-cart']/div/div[4]/button").click()
print(driver.title)
time.sleep(2)

#delete an item before proceed
driver.find_element(By.XPATH, '//*[@id="checkout-section"]/div/div/div[3]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/div/i').click()
time.sleep(2)

#enter your name
driver.find_element(By.XPATH, "//*[@id='txt_user_name_signup_guest']").send_keys("priyesh")
time.sleep(2)

#enter your mobile number
driver.find_element(By.XPATH, "//*[@id='user_mobile_number_guest']").send_keys("7143143143")
time.sleep(2)

#select dine in or take away
driver.find_element(By.XPATH, '//*[@id="card1"]/div[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="od_1"]/div/div/label').click()
time.sleep(2)

# select payment method
driver.find_element(By.XPATH, '//*[@id="online-label"]').click()
time.sleep(2)

time.sleep(2)
driver.close()
print("test succesfull")


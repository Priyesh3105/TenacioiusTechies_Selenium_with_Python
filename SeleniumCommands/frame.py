from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the nested frames page
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switch to the top frame
driver.switch_to.frame(0)
time.sleep(2)

# Switch to the left frame
driver.switch_to.frame(0)
time.sleep(2)

# Get the text from the left frame
left_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("Text from the left frame:")
print(left_frame_text)
time.sleep(2)


# Switch back to the top frame
driver.switch_to.default_content()
time.sleep(2)

# Switch to the top frame
driver.switch_to.frame(0)
time.sleep(2)

# Switch to the middle frame
driver.switch_to.frame(1)
time.sleep(2)

# Get the text from the middle frame
middle_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("Text from the middle frame:")
print(middle_frame_text)
time.sleep(2)


# Switch back to the top frame
driver.switch_to.default_content()
time.sleep(2)

# Switch to the top frame
driver.switch_to.frame(0)
time.sleep(2)

# Switch to the right frame
driver.switch_to.frame(2)
time.sleep(2)

# Get the text from the right frame
right_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("Text from the right frame:")
print(right_frame_text)
time.sleep(2)

# Switch back to the top frame
driver.switch_to.default_content()
time.sleep(2)

# Switch to the bottom frame
driver.switch_to.frame(1)
time.sleep(2)

# Get the text from the bottom frame
bottom_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("Text from the bottom frame:")
print(bottom_frame_text)
time.sleep(2)

# Switch back to the default content (main page)
driver.switch_to.default_content()
time.sleep(2)

# Close the browser window
driver.quit()
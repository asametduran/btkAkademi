from selenium import webdriver
import time
driver = webdriver.Edge()

url = "https://github.com"
driver.get(url)

time.sleep(2)

print(driver.title)
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com,homepage.png")
driver.close()
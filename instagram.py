from instagramUserInfo import email, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Instagram:
    def __init__(self, email, password):
        self.browser = webdriver.Edge()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        
        # Update to Selenium 4 syntax
        emailInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)


instagram = Instagram(email, password)
instagram.signIn()

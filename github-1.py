from githubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Edge()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get('https://github.com/login') 
        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH, "//*[@id='password']").send_keys(self.password)

        time.sleep(2)

        self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/input[13]").click()

    def getFollowers(self):
        self.browser.get("https://github.com/asametduran?tab=followers")
        time.sleep(2)

        items = self.browser.finl


# Doğru şekilde username ve password değerlerini gönderin
github = Github(username="asametdurann@gmail.com",password="169031010668ab?")
github.signIn()
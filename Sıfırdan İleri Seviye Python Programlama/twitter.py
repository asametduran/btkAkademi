from twitterUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Twitter:

    def __init__(self, username, password):
        self.browserProfile = webdriver.EdgeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Edge('msedgedriver.exe',edge_options = self.browserProfile)
        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get('https://twitter.com/i/flow/login')
        time.sleep(3)
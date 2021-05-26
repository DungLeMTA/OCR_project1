import argparse
import sys
from random import randint
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'https://www.facebook.com/'


class FacebookLogin():
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome("B:\PycharmProjects\OCR_project\chromedriver.exe")
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load



    def login(self):
        email_element = self.driver.find_element_by_id('email')
        email_element.send_keys(self.email) # Give keyboard input

        password_element = self.driver.find_element_by_id('pass')
        password_element.send_keys(self.password) # Give password as input too

        login_button = self.driver.find_element_by_id('loginbutton')
        login_button.click() # Send mouse click

        time.sleep(2) # Wait for 2 seconds for the page to show up


if __name__ == '__main__':
    # Enter your login credentials here
    fb_login = FacebookLogin(email='sample@example.com', password='PASSWORD', browser='Chrome')
    fb_login.login()



from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# options = Options()
# options.add_argument("--headless")

# driver = webdriver.Chrome("B:\PycharmProjects\OCR_project\chromedriver.exe",options=options)
driver = webdriver.Chrome("B:\PycharmProjects\OCR_project\chromedriver.exe")

def Auto_LoginVMF(URL,user, password):
    driver.get(URL)
    time.sleep(1)

    btnLogin = driver.find_element_by_id("sign_in2")
    btnLogin.click()
    try:
        tbUser = driver.find_element_by_id("ips_username")
        print("tbUser success")
    except:
        tbUser = None
        print("tbUser failed")
    tbPass = driver.find_element_by_id("ips_password")
    btnConfirm = driver.find_element_by_class_name("input_submit")

    tbUser.send_keys(user)
    time.sleep(1)
    tbPass.send_keys(password)
    time.sleep(1)
    btnConfirm.click()

def Webscraping(URL,domain_name):
    driver.get(URL)
    try:
        tbInput = driver.find_element_by_id("regularInput")
        print("tbInput success...")
    except:
        tbInput = None
        print("tbInput failed...")
    btnSearchAll = driver.find_elements_by_class_name("btn")
    btnSearch = btnSearchAll[0]

    tbInput.send_keys(domain_name)
    time.sleep(1)
    btnSearch.click()

if __name__ == '__main__':

    URL = "https://dnsdumpster.com/"
    domain = "ttnn.mta.edu.vn"
    # Auto_LoginVMF(URL,"DUNG DU DUONG","23/11/1999")
    Webscraping(URL,domain)

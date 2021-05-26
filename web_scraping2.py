from random import randint
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome("B:\PycharmProjects\OCR_project\chromedriver.exe")

def Auto_LoginVMF(URL,user, password):
    driver.get(URL)
    time.sleep(1)

    # btnLogin = driver.find_element_by_id("sign_in2")
    # btnLogin = driver.find_element_by_css_selector("#sign_in2")
    # print(btnLogin.text)
    # btnLogin.click()

    # tbUser = driver.find_element_by_id("ips_username")
    tbUser = driver.find_element_by_css_selector("#login_account")
    tbPass = driver.find_element_by_css_selector("#login_pwd")
    btnConfirm = driver.find_element_by_css_selector("#frmLogin > div.zidfbot > a")

    tbUser.send_keys(user)
    time.sleep(1)
    tbPass.send_keys(password)
    time.sleep(1)
    btnConfirm.click()


if __name__ == '__main__':
    URL = "https://id.zing.vn/v2/login?apikey=92140c0e46c54994812403f564787c14&data=AdSHRgHSjUYBN-W-dw"
    Auto_LoginVMF(URL,"dunglemta","Zi123456")

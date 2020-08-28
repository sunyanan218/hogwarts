from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage():
    def __init__(self):
        option=Options()
        option.debugger_address="localhost:9222"
        driver=webdriver.Chrome(options=option)
        driver.get("www.baidu.com")
        driver.implicitly_wait(3)
    def hello(self):
        print("hello")





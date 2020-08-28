from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    def __init__(self, driver:WebDriver):
        self.option=Options()
        self.option.debugger_address="localhost:9222"
        self.driver=webdriver.Chrome(options=self.option)
        self.driver.get("www.baidu.com")
        self.driver.implicitly_wait(3)




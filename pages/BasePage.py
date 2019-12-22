from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        driver = webdriver.chrome("C:\Users\Baris\PycharmProjects\n11TestAutomationPython\drivers\chromedriver.exe")
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30


from selenium.webdriver.common.by import By


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30


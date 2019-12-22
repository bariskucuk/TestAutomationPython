from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    email = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/form/div[1]/input')
    password = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/form/div[2]/input')
    loginError = (By.XPATH, '//*[@id="loginForm"]/div[2]/div[2]/div')
    submitButton = (By.XPATH, '//*[@id="loginButton"]')

    def set_email(self, email):
        emailElement = self.driver.find_element(*LoginPage.email)
        emailElement.send_keys(email)

    def login_error_displayed(self):
        notifcationElement = self.driver.find_element(*LoginPage.loginError)
        return notifcationElement.is_displayed()

    def set_password(self, password):
        pwordElement = self.driver.find_element(*LoginPage.password)
        pwordElement.send_keys(password)

    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPage.submitButton)
        submitBttn.click()

    def login(self, email="baris.kucuk.atilim@gmail.com", password="baris201371200"):
        self.set_password(password)
        self.set_email(email)
        self.click_submit()

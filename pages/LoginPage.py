from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    email = (By.ID, 'email')
    password = (By.ID, 'password')
    loginError = (By.XPATH, '//*[@id="loginForm"]/div[2]/div[2]/div')
    submitButton = (By.ID, 'loginButton')

    def set_email(self, email):
        emailElement = self.driver.find_element(*LoginPage.email)
        emailElement.send_keys(email)

    def login_error_displayed(self):
        notifcationElement = self.driver.find_element(*LoginPage.loginError)
        return notifcationElement.is_displayed()

    def set_password(self, password='baris201371200'):
        pwordElement = self.driver.find_element(*LoginPage.password)
        pwordElement.send_keys(password)

    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPage.submitButton)
        submitBttn.click()

    def login(self, email='*', password='*'):
        LoginPage.set_email(self, email)
        LoginPage.set_password(self, password)
        LoginPage.click_submit(self)

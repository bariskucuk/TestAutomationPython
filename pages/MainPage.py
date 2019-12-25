from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    loginButton = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[2]/div[2]/div/div/a[1]')
    searchTextBox = (By.XPATH, '//*[@id="searchData"]')
    searchButton = (By.XPATH, "//a[@class='searchBtn']")
    usernameLinkName = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[2]/div[2]/div[1]/a[2]')
    sepetimButton = (By.XPATH, '//*[@id="header"]/div/div/div[2]/div[2]/div[4]/a')

    def click_login_button(self):
        lgnButton = self.driver.find_element(*MainPage.loginButton)
        lgnButton.click()

    def enter_search_text(self, searchtext):
        srcButton = self.driver.find_element(*MainPage.searchTextBox)
        srcButton.send_keys(searchtext)

    def click_search_button(self):
        srcButton = self.driver.find_element(*MainPage.searchButton)
        srcButton.click()

    def click_sepetim(self):
        sepetimButton = self.driver.find_element(*MainPage.sepetimButton)
        sepetimButton.click()

    def get_username(self):
        username = self.driver.find_element(*MainPage.usernameLinkName)
        return username.get_attribute("text")

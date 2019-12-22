from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class AramaPage(BasePage):

    secondPageLink = (By.XPATH, '//*[@id="contentListing"]/div/div/div[2]/div[4]/a[2]')


    def click_second_page(self):
        secondpagelnk= self.driver.find_element(*AramaPage.secondPageLink)
        secondpagelnk.click()

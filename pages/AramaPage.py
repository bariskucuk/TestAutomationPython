from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AramaPage(BasePage):
    secondPageLink = (By.XPATH, '//*[@id="contentListing"]/div/div/div[2]/div[4]/a[2]')
    secondPageLinkActive = (By.XPATH, '//*[@id="contentListing"]/div/div/div[2]/div[4]/a[3]')
    UrunLink = (By.XPATH, '//*[@id="view"]/ul/li[3]/div[1]/div[1]/a')

    def click_second_page(self):
        secondpagelnk = self.driver.find_element(*AramaPage.secondPageLink)
        secondpagelnk.click()

    def click_urun_link(self):
        urunlnk = self.driver.find_element(*AramaPage.UrunLink)
        urunlnk.click()

    def is_second_page_link_active(self):
        isactive = self.driver.find_element(*AramaPage.secondPageLinkActive)
        return isactive.get_attribute("Class")

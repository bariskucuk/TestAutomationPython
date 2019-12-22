from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class AramaPage(BasePage):
    secondPageLink = (By.XPATH, '//*[@id="contentListing"]/div/div/div[2]/div[4]/a[2]')
    UrunLink= (By.XPATH,'//*[@id="p-391032147"]/div[1]/a')
    def click_second_page(self):
        secondpagelnk = self.driver.find_element(*AramaPage.secondPageLink)
        secondpagelnk.click()

    def click_urun_link(self):
        urunlnk = self.driver.find_element(*AramaPage.UrunLink)
        urunlnk.click()
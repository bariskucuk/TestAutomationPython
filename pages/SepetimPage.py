

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class SepetimPage(BasePage):

    UrunPrice = (By.XPATH,'//*[@id="newCheckout"]/div/div[1]/div[2]/div[1]/section/table[2]/tbody/tr/td[3]/div[2]/div/span')
    UrunSayisiArtirmaLink = (By.XPATH,'//*[@id="newCheckout"]/div/div[1]/div[2]/div[1]/section/table[2]/tbody/tr/td[3]/div[1]/div/span[1]')

    def get_urun_price(self):
        urunprice = self.driver.find_element(*SepetimPage.UrunPrice)
        return urunprice.text

    def click_urun_sayisi_artirma(self):
        urunartirBttn = self.driver.find_element(*SepetimPage.UrunSatisiArtırmaLink)
        urunartirBttn.click()


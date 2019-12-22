from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class SepetimPage(BasePage):
    UrunPrice = (
    By.XPATH, '//*[@id="newCheckout"]/div/div[1]/div[2]/div[1]/section/table[2]/tbody/tr/td[3]/div[2]/div')
    UrunSayisiArtirmaLink = (
    By.XPATH, '//*[@id="newCheckout"]/div/div[1]/div[2]/div[1]/section/table[2]/tbody/tr/td[3]/div[1]/div/span[1]')
    UrunSil = (
    By.XPATH, '//*[@id="newCheckout"]/div/div[1]/div[2]/div[1]/section/table[2]/tbody/tr/td[1]/div[3]/div[2]/span[1]')

    SepetBosHeader = (By.XPATH, '//*[@id="wrapper"]/div[2]/div/div[1]/div[1]/h2')

    def get_urun_price(self):
        urunprice = self.driver.find_element(*SepetimPage.UrunPrice)
        return urunprice.text

    def click_urun_sayisi_artirma(self):
        urunartirBttn = self.driver.find_element(*SepetimPage.UrunSatisiArtırmaLink)
        urunartirBttn.click()

    def click_urun_sil(self):
        urunsilBttn = self.driver.find_element(*SepetimPage.UrunSil)
        urunsilBttn.click()

    def sepet_bos_exists(self):
        sepetbos = self.driver.find_element(*SepetimPage.UrunPrice).isEmpty()
        return sepetbos



from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    urunname=""
    urunprice=""
    UrunAdiLabel = (By.XPATH, '//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div/h1')
    UrunPrice=(By.XPATH,'//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/ins')
    def get_urun_title(self):
        urunadi = self.driver.find_element(*MainPage.UrunAdiLabel)
        return urunadi.text

    def get_urun_price(self):
        urunprice = self.driver.find_element(*MainPage.UrunPrice)
        return urunprice.text

    def write_urn_name_price_textfile(self,urun_name,urun_price):
        urunFile = open("urunnameandprice.txt", "w")
        urunFile.write(urun_name+"\n"+urun_price)
        urunFile.close()  # to change file access modes
    def read_urn_name_price_textfile(self):
        urunFile = open("urunnameandprice.txt", "r")
        urunname=urunFile.readlines().pop()
        urunprice=urunFile.readline().pop()
        urunFile.close()  # to change file access modes

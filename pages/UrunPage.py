from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class UrunPage(BasePage):
    urunname=""
    urunprice=""

    UrunAdiLabel = (By.XPATH, '//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div/h1')
    UrunPrice=(By.XPATH,'//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/ins')
    SepeteEkle=(By.XPATH,'//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[4]/div[2]/div[2]/a')


    def get_urun_title(self):
        urunadi = self.driver.find_element(*UrunPage.UrunAdiLabel)
        return urunadi.text

    def get_urun_price(self):
        urunprice = self.driver.find_element(*UrunPage.UrunPrice)
        return urunprice.text

    def click_sepete_ekle(self):
        sepeteekleBttn = self.driver.find_element(*UrunPage.SepeteEkle)
        sepeteekleBttn.click()

    def write_urn_name_price_textfile(self,urun_name,urun_price):
        urunFile = open("urunnameandprice.txt", "w")
        urunFile.write(urun_name+"\n"+urun_price)
        urunFile.close()
    #TODO split name and price into two methods
    def read_urn_name_price_textfile(self):
        urunFile = open("urunnameandprice.txt", "r")
        urunname=urunFile.readlines().pop()
        urunprice=urunFile.readlines().pop()
        urunFile.close()

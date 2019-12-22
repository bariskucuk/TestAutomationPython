from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class UrunPage(BasePage):
    urunname=""
    urunprice=""

    UrunAdiLabel = (By.XPATH, '//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[1]/div[1]/div/h1')
    UrunPrice=(By.XPATH,'//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/ins')
    SepeteEkle=(By.XPATH,'//*[@id="unf-p-id"]/div/div[4]/div[1]/div[1]/div[2]/div[4]/div[2]/div[2]/a')


    def get_urun_title(self):
        UrunPage.urunname = self.driver.find_element(*UrunPage.UrunAdiLabel)
        return UrunPage.urunname

    def get_urun_price(self):
        UrunPage.urunprice = self.driver.find_element(*UrunPage.UrunPrice)
        return UrunPage.urunprice

    def click_sepete_ekle(self):
        sepeteekleBttn = self.driver.find_element(*UrunPage.SepeteEkle)
        sepeteekleBttn.click()

    def write_urn_name_price_textfile(self):
        urunfile = open("urunnameandprice.txt", "w")
        urunfile.write(UrunPage.get_urun_title(self)+"\n"+UrunPage.get_urun_price(self))
        urunfile.close()
    #TODO split name and price into two methods
    def read_urn_name_price_textfile(self):
        urunfile = open("urunnameandprice.txt", "r")
        urunname=urunfile.readlines().pop()
        urunprice=urunfile.readlines().pop()
        urunfile.close()

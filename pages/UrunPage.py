from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import os
my_path = os.path.abspath(os.path.dirname(os.path.abspath("urunnameandprice.txt")))


class UrunPage(BasePage):
    UrunAdiLabel = (By.XPATH, '//*[@id="contentProDetail"]/div/div[4]/div[2]/div[1]/div/h1')
    UrunPrice = (By.XPATH, '//*[@id="contentProDetail"]/div/div[4]/div[2]/div[3]/div[2]/div/div[1]/div/ins')
    SepeteEkle = (By.XPATH, '//*[@id="contentProDetail"]/div/div[4]/div[2]/div[3]/div[3]/a[2]')

    def get_urun_title(self):
        urunname = self.driver.find_element(*UrunPage.UrunAdiLabel)
        return urunname.text

    def get_urun_price(self):
        urunprice = self.driver.find_element(*UrunPage.UrunPrice)
        return urunprice.text

    def click_sepete_ekle(self):
        sepeteekleBttn = self.driver.find_element(*UrunPage.SepeteEkle)
        sepeteekleBttn.click()

    def write_urn_name_price_textfile(self):
        urunfile = open(my_path + r"\urunnameandprice.txt", "w")
        urunfile.write(UrunPage.get_urun_title(self))
        urunfile.write("\n")
        urunfile.write(UrunPage.get_urun_price(self))
        urunfile.close()

    def read_urn_price_from_textfile(self):
        urunfile = open(my_path + r"\urunnameandprice.txt", "r")
        price = urunfile.readlines()
        urunfile.close()
        return price[1]

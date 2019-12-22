from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import pages
import time


class CommonMethods(BasePage):
    def login_and_search(self):
        pages.MainPage.MainPage.click_login_button(self)
        pages.LoginPage.LoginPage.login(self)
        pages.MainPage.MainPage.enter_search_text(self, "bilgisayar")
        pages.MainPage.MainPage.click_search_button(self)
        time.sleep(2)
        pages.AramaPage.AramaPage.click_second_page(self)

    def add_a_bilgisayar_to_sepetim(self):
        pages.CommonMethods.login_and_search(self)
        pages.AramaPage.AramaPage.click_urun_link(self)
        time.sleep(3)
        pages.UrunPage.UrunPage.write_urn_name_price_textfile(self)
        pages.UrunPage.UrunPage.click_sepete_ekle(self)
        pages.MainPage.MainPage.click_sepetim(self)

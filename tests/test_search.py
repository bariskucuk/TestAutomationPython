import unittest
from selenium import webdriver
import pages
import time

from pages.BasePage import BasePage


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Baris\PycharmProjects\chromedriver.exe")
        pageUrl = "https://www.n11.com/"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        time.sleep(5)
    def login_and_search(self):
        pages.MainPage.MainPage.click_login_button(self)
        pages.LoginPage.LoginPage.login(self)
        pages.MainPage.MainPage.enter_search_text(self, "bilgisayar")
        pages.MainPage.MainPage.click_search_button(self)
        pages.AramaPage.AramaPage.click_second_page(self)

    def test_login(self):
        pages.MainPage.MainPage.click_login_button(self)
        pages.LoginPage.LoginPage.login(self,'baris.kucuk.atilim@gmail.com','baris201371200')
        assert pages.MainPage.MainPage.get_username(self) == "Barış Küçük"
    def test_search(self):
        MyTestCase.login_and_search(self)
        assert pages.AramaPage.AramaPage.is_second_page_link_active(self)== "active "

    def test_price_in_sepetim(self):
        MyTestCase.login_and_search(self)
        pages.AramaPage.AramaPage.click_urun_link(self)
        time.sleep(3)
        pages.UrunPage.UrunPage.write_urn_name_price_textfile(self)
        pages.UrunPage.UrunPage.click_sepete_ekle(self)
        #price = pages.SepetimPage.SepetimPage.get_urun_price()
        #assert pages.AramaPage.AramaPage.is_second_page_link_active(self)== price

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

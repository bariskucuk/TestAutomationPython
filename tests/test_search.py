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

    def test_login(self):
        pages.MainPage.MainPage.click_login_button(self)
        pages.LoginPage.LoginPage.login(self, 'baris.kucuk.atilim@gmail.com', 'baris201371200')
        assert pages.MainPage.MainPage.get_username(self) == "Barış Küçük"

    def test_search(self):
        pages.CommonMethods.CommonMethods.login_and_search(self)
        assert pages.AramaPage.AramaPage.is_second_page_link_active(self) == "active "

    def test_price_in_sepetim(self):
        pages.CommonMethods.CommonMethods.add_a_bilgisayar_to_sepetim(self)
        price = pages.SepetimPage.SepetimPage.get_urun_price(self)
        assert pages.UrunPage.UrunPage.read_urn_price_from_textfile(self) == price

    def test_increment_item_count_to_two(self):
        pages.CommonMethods.CommonMethods.add_a_bilgisayar_to_sepetim(self)
        quantity= pages.SepetimPage.SepetimPage.click_urun_sayisi_artirma(self)
        assert quantity == '2'
        pages.SepetimPage.SepetimPage.click_urun_sil(self)

    def test_sepetim_bos(self):
        pages.CommonMethods.CommonMethods.add_a_bilgisayar_to_sepetim(self)
        time.sleep(3)
        pages.SepetimPage.SepetimPage.click_urun_sil(self)
        assert pages.SepetimPage.SepetimPage.sepet_bos_exists(self) == "Sepetiniz Boş"

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

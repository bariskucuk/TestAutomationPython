import unittest
from selenium import webdriver
import pages
import time

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
        pages.LoginPage.LoginPage.login(self,"baris.kucuk.atilim@gmail.com","baris201371200")
        assert pages.MainPage.MainPage.usernameLinkName.Text == "Barış Küçük"
    def test_search(self):
        pages.MainPage.MainPage.click_login_button()
        pages.LoginPage.LoginPage.login(self)
        pages.MainPage.MainPage.enter_search_text(self,"bilgisayar")
        pages.AramaPage.AramaPage.click_second_page(self)
        assert pages.AramaPage.AramaPage.secondPageLinkActive.get_attribute("class") == 'active'

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

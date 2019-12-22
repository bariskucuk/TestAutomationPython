import unittest
from selenium import webdriver
import pages

driver = webdriver.chrome("C:\Users\Baris\PycharmProjects\chromedriver.exe")


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver.implicitly_wait(20)

    def test_something(self):
        driver.get("https://www.n11.com/")
        pages.MainPage.click_login_button()
        pages.LoginPage.set_email("baris.kucuk.atilim@gmail.com")
        pages.LoginPage.set_password("baris201371200")

    if __name__ == '__main__':
        unittest.main()

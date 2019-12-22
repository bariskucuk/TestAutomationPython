import unittest
from selenium import webdriver
import pages
import time



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Baris\PycharmProjects\chromedriver.exe")
    def test_something(self):
        pageUrl = "https://www.n11.com/"
        driver = self.driver
        driver.maximize_window()
        driver.get(pageUrl)
        time.sleep(5)
        pages.MainPage.click_login_button()
        pages.LoginPage.set_email("baris.kucuk.atilim@gmail.com")
        pages.LoginPage.set_password("baris201371200")

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

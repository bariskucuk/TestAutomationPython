import unittest
from selenium import webdriver
import pages

driver=webdriver.chrome("C:\Users\Baris\PycharmProjects\n11TestAutomationPython\drivers\chromedriver.exe")

driver.get("https://www.n11.com/")
class MyTestCase(unittest.TestCase):

    def test_something(self):
        MainPage.click_login_button()
        LoginPage.set_email("baris.kucuk.atilim@gmail.com")
        LoginPage.set_password("baris201371200")
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()

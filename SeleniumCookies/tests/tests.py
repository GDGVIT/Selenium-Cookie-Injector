import unittest
from SeleniumCookies.wrapper import *

try:
    from selenium import webdriver
except Exception as e:
    print('[!]', e)
    print('[*] pip install selenium')
    exit(1)


class TestSel(unittest.TestCase):
    def test_pathSetup(self):
        try:
            self.driver = webdriver.Chrome(
                '/home/kush/Desktop/github/Selenium-Cookie-Injector/chromedriver')
            self.driver.quit()
        except Exception as e:
            print('[!]', e)
            self.assertEqual(
                "Chrome Driver", "Not Found"), "[+] Chromedriver not found"

    def test_createCookie(self):
        self.assertEqual(str(type(create_cookie(
            'kush', '/', 'false', 10, 'hola', '121'))),
            "<class 'http.cookiejar.Cookie'>"), "Return Type not http.cookiejar.Cookie"

    def test_loadCookie(self):
        self.assertNotEqual(load, None), "[!] No Cookie to Load"


if __name__ == "__main__":
    unittest.main()

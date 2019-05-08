# coding:utf-8

import unittest

from selenium import webdriver


class F1(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://www.baidu.com")
    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_baidu_001(self):
        self.driver.find_element_by_link_text("新闻").click()
        #self.driver.back()

    def test_baidu_002(self):
        self.driver.find_element_by_partial_link_text("图").click()
        #self.driver.back()

if __name__ == "__main__":
    unittest.main(verbosity=2)

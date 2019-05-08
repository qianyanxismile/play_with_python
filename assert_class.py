# coding:utf-8
import unittest

from selenium import webdriver


# 类方法
class F1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_news(self):
        """百度首页链接测试：验证新闻的链接"""
        self.driver.find_element_by_link_text("新闻").click()
        self.driver.back()

    def test_baidu_map(self):
        """百度首页链接测试：验证地图的链接"""
        self.driver.find_element_by_partial_link_text("图").click()
        self.driver.back()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(F1("test_baidu_news"))
    suite.addTest(F1("test_baidu_map"))
    unittest.TextTestRunner(verbosity=2).run(suite)

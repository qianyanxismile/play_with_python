# coding:utf-8

import unittest
import time
import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class webtourtest(unittest.TestCase):
#class webtourtest(object):
    @classmethod
    def setUpClass(cls):
        # 初始化测试环境
        cls.url = url
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def testLogin(self):
        """
        用户登陆：
        1.点击账号密码登陆
        2.取消勾选10天登陆
        3.填写用户名，密码
        4.点击登陆
        """
        self.username = un
        self.password = pd
        base_login = self.driver.find_element_by_partial_link_text("账号密码登录")
        base_login.click()
        time.sleep(5)
        username = self.driver.find_element_by_id("loginform-username")
        password = self.driver.find_element_by_id("loginform-password")
        loginform_rememberme = self.driver.find_element_by_id('loginform-rememberme')
        submitbut = self.driver.find_element_by_name("login-button")
        #print "ready to click, ", loginform_rememberme, submitbut
        loginform_rememberme.click()
        #print "after click"
        username.send_keys(un)
        password.send_keys(pd)
        submitbut.click()
        self.assertEquals(self.driver.title, u"51CTO技术家园")
        time.sleep(5)
        return "access succes"


    def testSign(self):
        # 找到签到元素，点击签到
        singn_btn = self.driver.find_element_by_class_name('signbtn')
        singn_btn.click()
        time.sleep(10)
        asl = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[3]/div[2]/div[1]').get_attribute(
            "/html/body/div[6]/div[1]/div/div[3]/div[2]/div[1]")
        #asl.get_attribute("连续签到")
        self.assertIn("连续签到","asl")
            #assert 'sign success'

        # assert aResult.contains("连续签到")
        #time.sleep(5)
        #return 'sign success'

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.driver.quit()

if __name__ == "__main__":

    url = "https://edu.51cto.com/user/login.html"
    un = "18873242028"
    pd = "asdzxc123"

    # unittest.main()
    # 定义测试集
    test = unittest.TestSuite()
    #unittest.TextTestRunner(verbosity=2).run(suite)
    # 加载测试用例
    test.addTest(webtourtest("testLogin"))
    test.addTest(webtourtest("testSign"))
    # 设定文件路径
    file_result = open("D:\\test.html", "wb")
    # 调用报告生成程序，1.数据流2.标题3.用例描述 （为防止乱码，转换字符集）
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result, title=u"webtour测试",description=u"用例执行情况")
    # 运行
    runner.run(test)
    # 释放资源
    file_result.close()

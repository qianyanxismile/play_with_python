# coding:utf-8

import requests
from selenium import webdriver #加载webdriver 方法
import time #导入time包
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome() #创建chrome对象，调用chrome浏览器
loginurl = "https://qa-applet.dodoca.com" 
username = ""
password = ""
driver.get("https://qa-applet.dodoca.com") #在chrome中输入需访问的url路径
time.sleep(5) #页面加载后停留5秒
driver.maximize_window()#设置全屏
driver.set_window_size(800,600)#设置为固定分辨率大小
driver.get_screenshot_as_file("c:\\test.png")
driver.refresh() #刷新页面
time.sleep(2)

# web元素定位
driver.find_element_by_id("uername").send_keys("")

driver.find_elements_by_name("username").send_keys("")

driver.find_element_by_class_name("username").send_keys("")
driver.find_elements_by_class_name("username")[0].send_keys("")
#超链接查找
driver.find_element_by_link_text("").click()  #单击
ActionChains(driver).move_to_element().context_click().perform()#右键 
ActionChains(driver).move_to_element().double_click().perform()#双击
#鼠标拖拽,aa拖拽至bb
aa = driver.find_element_by_name("name")
bb = driver.find_element_by_name("pwd")
ActionChains(driver).drag_and_drop(aa,bb).perform()

driver.find_element_by_xpath("").send_keys()#相对路径，绝对路径


cblist = driver.find_elements_by_xpath("")
print ("total number:%d"%(len(cblist)))
for cb in cblist:
    cd.click()


#键盘操作
from selenium.webdriver.common.keys import Keys
send.keys()#输入
send.keys(Keys.ENTER) #回车
#全选，回车
send.keys(Keys.CONTROL,"a")
send.keys(Keys.BACKSPACE)


import unittest
import HTMLTestRunner
class webtourtest(unittest.TestCase):
    def setUp(self):
        #初始化测试环境
        self.driver = webdriver.Chrome()
        self.driver.get("")
    def testLogin(self):
        #测试主体部分
        self.driver.switch_to.frame("body")
        self.driver.switch_to.frame("navbar")
        username = self.driver.find_element_by_xpath("")
        password = self.driver.find_element_by_xpath("")
        submitbut = self.river.find_element_by_xpath("")
        username.sendkeys("")
        password.send_keys("")
        submitbut.click()
        time.sleep(3)
    def tearDown(self):
        #收尾
        self.driver.quit()

if __name__ == "__main__":
    #unittest.main()
    #定义测试集
    test = unittest.TestSuite()
    #加载测试用例
    test.addTest(webtourtest("testLogin"))
    #设定文件路径
    file_result = open("c:\\test.html","wb")
    #调用报告生成程序，1.数据流2.标题3.用例描述 （为防止乱码，转换字符集）
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u"webtour测试",description=u"用例执行情况")
   #运行
    runner.run(test)
    #释放资源
    file_result.close()

#访问登陆
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
submitbut = driver.find_element_by_name("login")
submitbut.click()
#通过属性方式未定位到元素时，换为xpath方式定位
#xpath 仍未定位到元素时，考虑框架问题(说明存在frame情况))，通过显示定位
driver.switch_to.frame("body")
driver.switch_to.frame("navbar")
username = driver.find_element_by_xpath("")
password = driver.find_element_by_xpath("")
submitbut = driver.find_element_by_xpath("")
username.sendkeys("")
password.send_keys("")
submitbut.click()




driver.quit() 

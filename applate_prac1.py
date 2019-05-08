#coding=utf-8

import requests
import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains类

driver = webdriver.Chrome() #构建浏览器
loginurl = "https://tsso.dodoca.com/account/index"
account = "Qaadmin"
password = "Dodoca2014qa"
driver.get(loginurl) #进入登陆页面

#浏览器全屏设置
driver.maximize_window()
driver.find_element_by_name("account").send_keys(account)#输入用户名
driver.find_element_by_name("password").send_keys(password)#输入密码
driver.get_screenshot_as_file("c:\\est.png")
time.sleep(10) #手动输入验证码
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[2]/form/div[5]/div/button").click() #点击登陆
time.sleep(10) 

#pdb.set_trace()

time.sleep(10)
#关闭新手指导
for i in range(2):
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/dl/img").click()


#定位要悬停的元素
#pdb.set_trace()

yingxiao = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[1]/div/ul/div[2]/li[6]/div")
yingxiao.click()
time.sleep(2) 
yingxiao_fabugoods = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[1]/ul/li[4]/ul/li[1]")
yingxiao_fabugoods.click()


#对定位到的元素执行悬停操作

#ActionChains(driver).move_to_element(yingxiao).perform()


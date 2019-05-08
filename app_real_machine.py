#! /usr/bin/env python
# coding=utf-8
import os
import time
#import unittest
from selenium import webdriver
#from lib2to3.pgen2.driver import Driver
#from lib2to3.tests.support import driver

#PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '80SQBDQC2263N'
desired_caps['automationName'] = "Appium"
#desired_caps['app'] = PATH('.\\weixin.apk')
# 如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之
desired_caps['appPackage'] = "com.meizu.media.reader"
desired_caps['appActivity'] = ".ReaderMainActivity"
desired_caps['appWaitActivity'] = ".app"
desired_caps['app'] = ".ReaderMainActivity"
#desired_caps['chromeOptions'] = {'androidProcess': 'com.meizu.media.reader'}

# 启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(100)
driver.find_element_by_class("android.widget.TextView").click()
#print driver.text()

#time.sleep(100)

driver.quit()
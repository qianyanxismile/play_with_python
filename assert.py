#coding:utf-8

import unittest

def div(a, b):
    return a / b

class TestDiv(unittest.TestCase):

    def setUp(self): #selenium 启动浏览器
        print "before every test case"

    def test_1_div_1(self):
        self.assertEqual(div(1, 1), 1 / 1)

    def test_3_div_1(self):
        self.assertEqual(div(3, 4), 3 / 4)

    def test_2_div_0(self):
        self.assertRaises(ZeroDivisionError, div, 3, 0)

    def tearDown(self): #selenium 关闭浏览器等等
        print "after every test case"

if __name__==" __main__":
    unittest.main()

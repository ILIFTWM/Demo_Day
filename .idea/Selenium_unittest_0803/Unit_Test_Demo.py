#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 0:02
# @Author  : WM
# @File    : UnitTest.py
import importlib
import unittest
class UserTestCase(unittest.TestCase):
    def setUp(self):
        print("==调用setup==")
        self.name = "xiaoD"
        self.age = 28

    def tearDown(self):
        print("==调用tearDown==")

    def test_name(self):
        print("==调用test_name==")
        #断言是否相同
        self.assertEqual(self.name,"xiaoD",msg="名字不对")

    def test_isupper(self):
        print("==调用test_isupper==")
        #断言是否为true,msg是断言错误的提示信息
        self.assertFalse("xdclass".isupper(),msg="不是大写")

    def test_age(self):
        print("==调用test_age==")
        #断言是否相同
        self.assertEqual(self.age,28)


if __name__ == '__main__':
        unittest.main()#调用以“test”开头的方法

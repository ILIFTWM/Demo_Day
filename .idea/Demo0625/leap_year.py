#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 23:19
# @Author  : WM
# @File    : leap_year.py
# 输入年份判断是否是闰年.
year = int(input("请输入年份(例如:1995):"))
if ( year%400 == 0 ) or ( year%4 == 0 and year%100 !=0):
    print("输入的年份%d是闰年"%year)
else:
    print("输入的年份%d不是闰年"%year)
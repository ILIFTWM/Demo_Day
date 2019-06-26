#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 22:33
# @Author  : WM
# @File    : Temperature.py

#华氏温度转换成摄氏温度: c = 5/9(f-32).
#input函数.

f = float(input("请输入华氏温度:"))

c = round(5/9*(f-32),2)
print("对应的摄氏温度为%d",c);



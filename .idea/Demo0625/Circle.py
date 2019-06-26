#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/26 22:57
# @Author  : WM
# @File    : Circle.py
#输入圆的半径计算周长和面积..

import math
radius = float(input("请输入圆的半径："))
circumference = 2*math.pi*radius
area = math.pi*(radius**2)
area1=math.pi*radius*radius
print("圆的周长是：%.2f,,,圆的面积是：%.2f"%(circumference,area1))

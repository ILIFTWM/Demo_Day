#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 15:52
# @Author  : WM
# @File    : thorey.py

# 1、自动化测试实战之ActionChains模拟用户行为
#     简介：讲解使用selenium里面的ActionChains模拟用户的行为
#
#     需求：
#         需要模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽
#
#     解决：selenium提供了一个类来处理这类事件
#     from selenium.webdriver.common.action_chains.ActionCharins(driver)
#
#     脚本：
# from selenium.webdriver.common.action_chains import ActionChains
#
#     执行原理：
#          调用ActionChains的方法时不会立即执行，会将所有的操作按顺序存放在一个队列里，当调用perform（）方法时，队列中的事件会依次执行
#
#     支持链式写法或者分步写法
#     ActionChains(driver).click(ele).perform()


# 键盘和鼠标方法列表：
# perform() 执行链中所有操作
# click(on_element=None) 单击鼠标左键
# context_click(on_element-None) 点击鼠标右键
# double_click(on_element=None) 双击鼠标左键
# move_to_element(to_element) 鼠标移到某个元素
# ele.send_keys(keys_to_send) 发送某个词到当前焦点元素

#*****不常用*****
# click_and_hold(on_element_None) 点击鼠标左键不松开
# release(on_element=None) 在某个元素位置松开鼠标左键
# key_down(value,element=None) 松开某个键盘上的键
# key_up(valus,element-None) 松开某个键
# drag_and_drop(source,target) 拖拽到某个元素然后松开
# drag_and_drop_by_offset(source,xoffset,yoffset) 拖拽到某个坐标然后松开
# move_by_offset(xoffset,yoffset) 鼠标从当前位置移动到某个坐标
# move_to_element_with_offset(to_element,xoffset,yoffset) 移动到距某个元素（左上角坐标）多少距离的位置
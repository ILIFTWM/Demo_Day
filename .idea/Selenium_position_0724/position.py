#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 0:20
# @Author  : WM
# @File    : position.py
'''
# 1.selenium基础实战之定位网页元素技巧
#   简介：讲解使用selenium定位网页元素
#   find_element_by_id,find_element_by_name,find_element_by_class_name
#
#   1.打开浏览器
#     brower = webdriver。Firefox()
#   2.打开网页
#     brower.get("http://www.baidu.com")
#     使用python判断是否正确
#     brower.title 或者 brower.current_url

#   3.定位元素的8种方法,(一定要唯一！！！)
#     id：find_element_by_id()  采用id属性进行定位
#     name：find_element_by_name()  定位方式和id类似，id，name和class一般在网页中至少会有其中一种
#     class name：find_element_by_class_name() 定位方式和id类似，id，name和class一般在网页中至少会有其中一种
#     tag name: find_element_by_tag_name()  通过标签名去定位，用的少，如find_element_by_tag_nmae("div")
#     link test: find_element_by_link_text() 超链接定位
#     partial link text：find_element_by_partial_link_text() 超链接定位模糊查询，和link text查询类似

#     使用最多的方法：
#     css selector：find_element_by_css_selector()
#     根据css定位属性，class用.标记，id用#标记，定位方式也会比xpath快
#     如 find_element_by_css_selecctor("复制css选择器的内容")
#     技巧：通过查看元素拷贝css路径
#     路径：鼠标右键——>审查元素——>右键——>复制——>css选择器

#     xpath语法：
#       http://www.w3school.com.cn/xpath/xpath_functions.asp
#     注意：“//”是全部的意思，“/”是相邻的意思，“*”所有元素，“..”元素的父节点，“.”当前节点
#       xpath：find_element_by_xpath()  xpath是XML路径语言，通过元素路径查找元素，HTML是XML的一种实现
#              绝对路径定位：从<html>标签开始依次往下进行查找，（固定的路径）
#              相对路径定位：利用元素属性进行xpath定位（）
#       技巧：通过查看元素拷贝css路径
#       绝对路径：鼠标右键——>审查元素——>右键——>复制——>xpath
'''
'''
selenium定位元素的8中方法
     id： find_element_by_id() ##使用id属性进行定位
     name：  find_element_by_id()##使用name属性进行定位
     class name： find_element_by_class_name() ##使用类名称进行定位
     tag name:  find_element_by_tag_name()##通过标签名去确定
     link text： find_element_by_link_text()##超链接内容定位，元素内容
     partial link text:  find_element_by_partial_link_text() ##模糊方式超链接内容定位
     css selector:  find_element_by_css_selector('元素【属性=值】') ##css属性定位
     xpath： find_element_by_xpath()  ##xpath是xml路径语言，通过元素路径来查找元素
selenium中的方法
     clear（） //清空
     send_keys()  //输入
     back（）  //后退页面
     maximize_window() //最大化窗口
     click（） //点击事件，点击按钮，超链接
     submit（） //提交表单

#   4.定位到元素后的方法
#     clear()  清空
#     send_keys()  输入
#     back()  后退页面
#     maximize_window  最大化窗口
#     click()  点击事件 点击按钮，超链接
#     submit  提交表单

#   5.定位到元素后的属性
#     tag_name  标签名
#     text  文本内容
#     title  标题

#   6.定位元素报错，原因如下：
#       1.根据定位取不到
#       2.多个元素下标超出范围，没有0，从1开始
#       解决办法：换其他定位方法
'''
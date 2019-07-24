#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 0:26
# @Author  : WM
# @File    : location.py
from selenium import webdriver
from time import sleep
#拿到driver
driver = webdriver.Firefox()
driver.get("http://news.baidu.com/")
''''''

#跳转网页
#driver.get("https://www.baidu.com")
#print(driver.title)
#选中输入框，发送所要查的信息
#driver.find_element_by_id('kw').send_keys('课堂')#id定位
#driver.find_element_by_name('wd').send_keys('课堂--腾讯')#name定位
#driver.find_element_by_class_name('s_ipt').send_keys('课堂--网易云')#class定位，不常用，一般不唯一
#定位出提交的id
#driver.find_element_by_id('su').click()

''''''
#链接定位
#睡眠时间,先睡眠再跳转
#sleep(3)
#driver.find_element_by_link_text('视频').click()#图片与js需要先先加载进来，所以需要一个睡眠时间
#driver.find_element_by_partial_link_text('频').click()#链接模糊查询

''''''
''''''
#css样式定位
#driver.find_element_by_css_selector(".li_5 > a:nth-child(1)").click()
#print(driver.title)

''''''
#xpath定位
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/div/div[2]/ul/li[6]/a").click()
print(driver.title)

#关闭浏览器
sleep(10)
driver.quit()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 20:36
# @Author  : WM
# @File    : Sing_Selection.py
'''
################radio####################
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("file:///D:/Demo_Day/.idea/Selenium_practice_0731/radio.html")
print(driver.title)
print("默认为Male,2秒之后自动选中female")
sleep(2)
driver.find_element_by_id("female").click()
'''

'''
# 2.自动化测试值页面常见弹窗处理
#   简介：讲解selenium处理页面弹窗。alert和comfirm
#   弹窗常用方法(需要先切换窗口 switch_to_alert())
#     accept()
#     dismiss()

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("file:///D:/Demo_Day/.idea/Selenium_practice_0731/alert.html")
print(driver.title)
#睡眠2秒
sleep(2)
driver.find_element_by_id("alert").click()
#切换窗口后才能关闭
win = driver.switch_to.alert #切换,需要赋值
sleep(2)
win.accept()#关闭弹出窗

driver.find_element_by_id("confirm").click()
confirm_ele= driver.switch_to.alert
sleep(2)
#取消弹出窗
confirm_ele.dismiss()

'''

'''
# 3、自动化测试之验证码常用验证方案
#     1、破解验证码（不建议）
#       OCR识别：tesseract-ocr开源组件安装破解
#       AI机器学习：  tenssorflow 破解验证码，
#     2、绕过
#       1、让开发人员临时关闭验证码（安全性需要保密，一般再开发测试环境使用）
#       2、提供一个万能验证码（安全性需要保密，一般再开发测试环境使用）
#       3、使用cookie（登录主要目的是拿cookie，获取登录凭证）

###############使用cookie登录，进行下单##########################
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("https://xdclass.net/#/index")##1.进入页面，driver指向此网页的地址
print(driver.title)
#睡眠时间3秒
sleep(3)

driver.add_cookie({"name":"name","value":"jack"})
driver.add_cookie({"name":"token","value":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvMjEuanBlZyIsImlkIjoxMTcwOCwibmFtZSI6IuS4jeivrSIsImlhdCI6MTU2NDU4MTgzMywiZXhwIjoxNTY1MTg2NjMzfQ.kmspWlk81ESnswq5SU5p6aE_JiMWgLYRw7nj-u9i4kM"})
sleep(5)
video_ele = driver.find_element_by_css_selector(".recommendcourse > div:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)")
video_ele.click()#2.此为打开driver内的另一个地址，driver仍为“https://xdclass.net/#/index”，此仅为打开

sleep(2)
print("准备下单")
#3.获取第二个页面，让driver指向新打开的窗口
driver.switch_to.window(driver.window_handles[1])
#选择下单按钮
buy_btn_ele = driver.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)")#4.此刻driver并不是指向“https://xdclass.net/#/index”
#buy_btn_ele = video_ele.find_element_by_css_selector(".buy_tolearn > a:nth-child(1)")#video_ele单独使用也不能定位到元素，因不是webdriver的实例化
buy_btn_ele.click()
sleep(2)
print("进入下单界面")

'''

'''

'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from time import strftime, localtime
#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("https://xdclass.net/#/index")
print(driver.title)
sleep(3)

#查找登陆框
login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
#触发点击事件,ActionChains(driver).click(ele).perform()模拟鼠标操作才能进行的情况，比如单击、双击、点击鼠标右键、拖拽
ActionChains(driver).click(login_ele).perform()
#捕捉抓不到元素异常
sleep(3)
try:
    driver.find_element_by_css_selector(".mobienum > input:nth-child(1)-1").click()
except:
    driver.get_screenshot_as_file("./error.png")

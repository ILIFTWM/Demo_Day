#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 14:45
# @Author  : WM
# @File    : EventHanding.py
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 鼠标事件实战之hover菜单栏弹出
'''
#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("https://xdclass.net/#/index")
#睡眠时间
sleep(2)
#定位鼠标移动到上面的元素
menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
ActionChains(driver).move_to_element(menu_ele).perform()

#选中子菜单
sub_menu_ele = driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(1)")
sleep(2)
sub_menu_ele.click()
'''


#模拟网页登陆
'''
#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("https://xdclass.net/#/index")
print(driver.title)
#睡眠时间3秒
sleep(3)

#登陆框
login_ele = driver.find_element_by_css_selector(".login > span:nth-child(2)")
#触发点击事件
ActionChains(driver).click(login_ele).perform()

#查找输入框，输入账户密码，输入框需要提前清理
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".mobienum > input:nth-child(1)").send_keys("13636026394")

driver.find_element_by_css_selector(".psw > input:nth-child(1)").clear()
driver.find_element_by_css_selector(".psw > input:nth-child(1)").send_keys("zql12345+")

#查找登录按钮
login_btn_ele = driver.find_element_by_css_selector(".btn")
#触发点击事件
login_btn_ele.click()

#判断是否登陆成功，鼠标移动上面，判断弹窗字符
user_info_ele = driver.find_element_by_css_selector(".avatar_img")
sleep(3)
#触发hover事件
ActionChains(driver).move_to_element(user_info_ele).perform()
sleep(5)
#获取用户名的元素
user_name_ele = driver.find_element_by_css_selector(".username")
print(user_name_ele.text)
name = user_name_ele.text
sleep(5)
print("----测试结果----")

if name == u"不语":
   print("登陆成功！")
else:
   print("登陆失败！")
'''


#driver.quit()


####################################################################################################
#自动化测试实战之网页等待时间
# 自动化测试实战之网页等待时间简介：讲解自动化测试的等待时间
#
#  1.为什么需要等待时间--》等系统稳定
#      网页需要加载对应的资源文件，页面渲染，窗口处理等等
#  2.自动化测试常用的等待时间
#    强制等待（自己调试代码看效果）：
#         from time import sleep
#         sleep(5)#强制等待5秒再执行下一步，缺陷是不管资源是不是完成，都必须等待
#    隐性等待：
#         driver.implicitly_wait(10) #隐性等待，最长等10秒
#         #设置了一个最长等待时间，如果再规定时间内网页加载完成，再执行下一步，否则一直等到时间截至，然后执行下一步，
#         弊端就是程序会一直等待真个页面加载完成，到浏览器标签栏那个加载圈不再转
#         注意：对driver起作用，所以只要设置一次即可，没有必要到处设置
#    显性等待：
#        WebDriverWait 需要配合
#        until和until_not,程序每隔N秒检查一次，如果成功，则执行下一步，否则继续等待，知道超过设置的最长时间
#        from selenium.webdriver.support.wait import WebDriverWait
#        语法：WebDriver(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
#
#       from selenium.webdriver.commom.by impory By
#       from selenium.webdriver.support.ui import WebDriverWait

#结论：隐性等待和显性等待可以同时用，等待的最长时间取两者之中的较大者

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#拿到driver
driver = webdriver.Firefox()
#跳转网页
driver.get("https://www.baidu.com/")
#睡眠时间
#sleep(2)
#driver.implicitly_wait(5) #隐性等待，最长等待5秒
try:
    ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
    #显性等待，每隔0.5秒检查一次，最长等待时间为5秒，检查是否页面能找到ID为“kw”的元素
    ele.send_keys("哇哈哈")
    print(driver.title)
    print("资源加载成功")
except:
    print("资源加载失败，发送报警邮件")
finally:
    print("不管有没有成功，都打印，用于资源清除")
    #退出浏览器
    driver.quit()

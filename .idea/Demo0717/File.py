#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 21:04
# @Author  : WM
# @File    : File.py

'''
学习内容：
读文件 - 读取整个文件 / 逐行读取 / 文件路径
写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件

'''
# 读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：标示符'r'表示读
# f = open('D:/test.txt', 'r')#文件不存在的报错情况：No such file or directory:
# #调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
# print(f.read())
# print(type(f))#<class '_io.TextIOWrapper'>
# #调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
# 文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
'''
try:
    f = open(open('D:/test.txt', 'r'),'r')
    print(f.read())
finally:
    if f:
     f.close()
#两者意思相同，python中with语句自动引用close（）方法
with open('/path/to/file', 'r') as f:
    print(f.read())

'''
# read()会一次性读取文件的全部内容，防止内存爆满，要反复调用read(size)方法，设置每次最多读取size个字节的内容
# readline()可以每次读取一行内容
# readlines()一次读取所有内容并按行返回list
# f = open('D:/test.txt', 'r')
# for line in f.readlines():
#     print(line.strip())
# with open('D:/test.txt', 'r') as f:
#    for line in f.readlines():
#          print(line.strip())
'''
# 文件路径：
import os
print(os.getcwd())#获得当前路径
#os.makedirs('d:/home/')#FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'd:/home/'
print(os.path.abspath('.'))#)返回参数的绝对路径的字符串
print(os.path.isabs('.'))#返回一个布尔值，判断是否是相对路径
print(os.path.dirname('D:\Demo_Day\.idea\Demo0717'))#返回一个字符串，包含path参数中最后一个斜杠之前的所有内容;#D:\Demo_Day\.idea
print(os.path.basename('D:\Demo_Day\.idea\Demo0717'))#返回path参数中最后一个斜杠之后的所有内容
print(os.path.split('D:\Demo_Day\.idea\Demo0717\test.txt'))#返回两个字符串的元组，包含路径的目录名称和基本名称) #('D:\\Demo_Day\\.idea', 'Demo0717\test.txt')
#os.path.getsize(path)和os.listdir()可以计算文件夹下所有文件的大小
print(os.path.exists('/home/xiaobai'))#检测路径有效性
'''



#
# 文件标识符（文本文件）：
# 读模式 r ：（1）只能读，不能写；（2）文件不存在时会报错。
# 读写模式 r+：1）文件不存在时会报错；（2）可以读，也可以写，是覆盖写，会把文件最前面的内容覆盖
# 写模式 w ：1）只能写，不能读；（2）写的时候会把原来文件的内容清空；（3）当文件不存在时，会创建新文件。
# 写读模式 w+：（1）可以写，也可以读；（2）写的时候会把原来文件的内容清空；（3）当文件不存在时，会创建新文件。
# 追加模式a：1）不能读；（2）可以写，是追加写，即在原内容末尾添加新内容；（3）当文件不存在时，创建新文件。
# 追加读模式a+：1）可读可写；（2）写的时候是追加写，即在原内容末尾添加新内容；（3）当文件不存在时，创建新文件。

# 二进制文本标识符：
# 打开二进制文件以读取数据：rb
# 打开二进制文件以写入数据：wb
# 打开二进制文件以添加数据：ab
# 打开二进制文件以读取和写入数据：rb+
# 打开二进制文件以写入和读取数据：wb+
# 打开二进制文件以t添加和读取数据：ab+


#r:读取模式  w: 写入模式 a：附加模式  r+:写入和读取模式
with open('D:/test.txt','w',encoding='utf-8') as file_object:#覆盖原文件内容，或者创建新的文件
    file_object.write('hhhhhhhh\n')## 写多行文件 为了是每一行的写入都占据一行，就在后面加上回车符 '\n'
    file_object.write('第二行\n')

with open('D:/test.txt','a',encoding='utf-8') as file_object:#追加写入
    file_object.write('追加内容--1\n')
    file_object.write('追加内容--2\n')
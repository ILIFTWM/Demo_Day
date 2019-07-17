#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 23:50
# @Author  : WM
# @File    : Data_persistence.py
'''数据持久化 - CSV文件概述 / csv模块的应用 / JSON数据格式 / json模块的应用'''

# csv模块还定义了
# 一些类：DictReader、DictWriter、Dialect等，DictReader和DictWriter类似于reader和writer。
# 一些常量：QUOTE_ALL、QUOTE_MINIMAL、.QUOTE_NONNUMERIC等，这些常量可以作为Dialects and Formatting Parameters的值。

# reader(csvfile, dialect='excel', **fmtparams)
# csvfile，必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象，如果是文件对象，打开时需要加"b"标志参数。
# dialect，编码风格，默认为excel的风格，也就是用逗号（,）分隔，
# fmtparam，格式化参数，用来覆盖之前dialect对象指定的编码风格
'''
import csv
with open('data.csv','a+',encoding='utf-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    # 写入一行
    writer.writerow(['1','2','3','4','5','5','6'])
    # 写入多行
    writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])

with open('data.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # 读取出的内容是列表格式的
        print(row,type(row),row[1])

'''

# json.dump(序列化对象，文件对象)
# json.dumps(序列化对象)，返回值是一个字符串，需要手动将这个字符串写入到文件中
#
#     encoding：把一个python对象编码转换成Json字符串。
#     decoding：把json格式字符串编码转换成python对象。
#
# 　　json提供四个功能：json.loads 　json.dumps    json.load    json.dump。loads跟dumps是用来处理字符串的，load跟dump是用来处理文件的。
#
#     loads：把json转换成其他格式，字符串或文件相关的
#     dumps：把其他对象或格式转换为json格式
#     load：将文件的内容转换成为json数据
#     dump：把json数据写入到文件中

import json
print("------json序列化--------")
import time
info={
    'date':time.localtime(),
    'name':'hhh'
}
f = open("test.json","w",encoding='utf-8')
# print("---------dump---------")
# json.dump(info,f)
# f.close()
print("---------dumps，---------")
#json.dumps(obj*, sort_keys=True, indent=4, ensure_ascii=False)
f.write(json.dumps(info,ensure_ascii=False))
f.close()

f = open("test.json",'r')
#a=json.loads(f)
b=json.loads(f.readlines())
print(a)#  问题点：TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper
f.close()
'''
data = [1,2,3,4,5]
with open('user_info.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)

with open('user_info.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    print(type(data))
    print(data)
'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 23:03
# @Author  : WM
# @File    : Exceptional.py
'''异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 / 内置异常类型 / 异常栈 / raise语句
'''
#
# try:
#    print(aa)
# except IOError: #NameError: name 'aa' is not defined
#     pass
'''
try:
   print(aa)
except NameError as msg:#定义一个变量msg用于接收具体错误信息, 然后将msg接收的错误信息打印。
    print(msg)
#try...finally...#我们不管线捕捉到的是什么错误，无论错误是不是发生，这些代码“必须”运行，比如文件关闭，释放锁，把数据库连接返还给连接池等。
import time
try:
    f = open('D:/test.txt','r',encoding='utf-8')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        #time.sleep(2)
        print(line)
finally:
    f.close()
    print('Cleaning up...closed the file')


filename = input('please input file name:')
if filename=='hello':
    raise NameError('input file name error !')#人为的通过raise来抛出一个异常

# for...else...会使得代码很简洁，注意else中的代码块仅仅是在for循环中没有执行break语句的时候执行
# 只有当 while 环运行完毕时，也就是说 while 的循环条件为假而退出，没有关键字 break 来终止循环 while 循环，else 中的代码块才能够运行。
# 只有当 try 块中的代码没有捕获到任何一种异常时，才执行 else 块中的代码
# try:
#     < Code1 >
# except < name > ：
# < Code2 >
# else:
# < Code3 >
'''
#---异常栈
import traceback
import sys
try:
    1 / 0
except Exception as e:
    #traceback.format_exc()
    print('------------------------------------------------')
    #traceback.print_exc()
    print(sys.exc_info()[0:2])# 打印错误类型，错误值
    print(traceback.extract_tb(sys.exc_info()[2])) #出错位置


# 内置异常类型
# 内置异常的层次结构
#
# BaseException             所有异常的基类
#  +-- SystemExit              解释器请求退出
#  +-- KeyboardInterrupt          用户中断执行(通常是输入^C)
#  +-- GeneratorExit            生成器(generator)发生异常来通知退出
#  +-- Exception               常规错误的基类
#       +-- StopIteration              迭代器没有更多值
#       +-- StopAsyncIteration              必须通过异步迭代器对象的__anext__()方法引发以停止迭代
#       +-- ArithmeticError                 所有数值计算错误的基类
#       |    +-- FloatingPointError             浮点计算错误
#       |    +-- OverflowError                  数值运算超出最大限制
#       |    +-- ZeroDivisionError              除(或取模)零 (所有数据类型
#       +-- AssertionError                  断言语句失败
#       +-- AttributeError                  对象没有这个属性
#       +-- BufferError                    与缓冲区相关的操作时引发
#       +-- EOFError                        没有内建输入,到达EOF 标记
#       +-- ImportError                     导入失败
#       |    +-- ModuleNotFoundError        找不到模块
#       +-- LookupError                     无效数据查询的基类
#       |    +-- IndexError                      序列中没有此索引(index)
#       |    +-- KeyError                        映射中没有这个键
#       +-- MemoryError                     内存溢出错误
#       +-- NameError                       未声明、初始化对象
#       |    +-- UnboundLocalError              访问未初始化的本地变量
#       +-- OSError                         操作系统错误，
#       |    +-- BlockingIOError               操作将阻塞对象设置为非阻塞操作
#       |    +-- ChildProcessError             子进程上的操作失败
#       |    +-- ConnectionError               与连接相关的异常的基类
#       |    |    +-- BrokenPipeError             在已关闭写入的套接字上写入
#       |    |    +-- ConnectionAbortedError      连接尝试被对等方中止
#       |    |    +-- ConnectionRefusedError      连接尝试被对等方拒绝
#       |    |    +-- ConnectionResetError        连接由对等方重置
#       |    +-- FileExistsError               创建已存在的文件或目录
#       |    +-- FileNotFoundError             请求不存在的文件或目录
#       |    +-- InterruptedError              系统调用被输入信号中断
#       |    +-- IsADirectoryError             在目录上请求文件操作
#       |    +-- NotADirectoryError            在不是目录的事物上请求目录操作
#       |    +-- PermissionError              在没有访问权限的情况下运行操作
#       |    +-- ProcessLookupError            进程不存在
#       |    +-- TimeoutError                  系统函数在系统级别超时
#       +-- ReferenceError                弱引用试图访问已经垃圾回收了的对象
#       +-- RuntimeError                  一般的运行时错误
#       |    +-- NotImplementedError      尚未实现的方法
#       |    +-- RecursionError           解释器检测到超出最大递归深度
#       +-- SyntaxError                   Python 语法错误
#       |    +-- IndentationError         缩进错误
#       |         +-- TabError          Tab 和空格混用
#       +-- SystemError              一般的解释器系统错误
#       +-- TypeError               对类型无效的操作
#       +-- ValueError              传入无效的参数
#       |    +-- UnicodeError             Unicode 相关的错误
#       |         +-- UnicodeDecodeError     Unicode 解码时的错误
#       |         +-- UnicodeEncodeError     Unicode 编码时错误
#       |         +-- UnicodeTranslateError  Unicode 转换时错误
#       +-- Warning                       警告的基类
#            +-- DeprecationWarning          关于被弃用的特征的警告
#            +-- PendingDeprecationWarning   关于构造将来语义会有改变的警告
#            +-- RuntimeWarning           可疑的运行行为的警告
#            +-- SyntaxWarning            可疑的语法的警告
#            +-- UserWarning              用户代码生成的警告
#            +-- FutureWarning            有关已弃用功能的警告的基类
#            +-- ImportWarning            模块导入时可能出错的警告的基类
#            +-- UnicodeWarning           与Unicode相关的警告的基类
#            +-- BytesWarning             bytes和bytearray相关的警告的基类
#            +-- ResourceWarning           与资源使用相关的警告的基类。。
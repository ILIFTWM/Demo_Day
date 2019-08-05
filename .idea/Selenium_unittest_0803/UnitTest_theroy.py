#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/3 20:47
# @Author  : WM
# @File    : UnitTest_theroy.py

# 自动化测试必备框架 unittest 单元测试框架实战
#
# 1、什么是单元测试unittest
#     简介：讲解什么是单元测试，使用场景和unittest介绍
#     1、单元测试：
#      是指对软件中的最小可测试单元进行检查和验证。对于单元测试中单元的含义，一般来说，要根据实际情况去判定其具体含义
#      如C语言中单元指一个函数。
#
#   function add(int a ,int b){
#     return a + b
# }
# JAVA里单元指一个类，图形化的软件中可以指一个窗口或一个菜单等。
# 总的来说，单元就是认为规定的最小的被测功能模块。单元测试是在软件开发过程中要进行的最低级别的测试活动，软件的独立单元将在
# 与程序的其他部分相隔离的情况下进行测试
#
# 2、unittest 框架是python的单元测试框架，Java--》Juint
#  官网：http://docs.python.org/2/library/unittest.html
#
# 3、unittest = TestCase + TestResult  执行+结果
#
# 二、单元测试框架unittest入门
# 1、导入模块
# 2、测试的类都继承于TestCase类
# 3、setUp() 测试前的初始工作  testDown()测试后的清除工作（在每个测试方法运行时被调用这2个方法）
# 注意：
# 	1、所有类中方法的入参为self,定义方法的变量也要“self.”变量
# 	2、定义测试用例，以“test”开头命名的方法，入参为self
# 	3、unittest.main()方法会搜索该模块下面所有以test开头的测试用例方法，并自动执行它们
# 	4、py文件不能以unittest命名，不然找不到TestCae
# 	成功是输出 . 失败是F


# 三、测试套件TestSuite介绍
# 简介：讲解测试套件TestSuite的基本介绍和使用场景
# 需求：
#    1、利用unittest执行流程测试而非单元测试
#    2、控制unitest的执行顺序


# 1、unitest.TestSuite()类表示一个测试用例集
#   (1)用来确定测试用例的顺序，哪个先执行哪个后执行
#   (2)如果一个class中有四个test开头的方法，则加载到suite中时则有四个测试用例
#   (3)由TestLoader加载TestCase到TestSuite
#   (4)verbosity参数可以控制执行结果的输出，0是简单报告 1是一般报告 2是详细报告
#      默认1 会在每个成功的用例前面加个"." 每个失败的用例前面有个"F"
#  2、TextTestRunner() 文本测试用例运行器
#  3、run()方法是运行测试套件的测试用例，入参为suite测试套件

# 4、高级实战系列之测试套件TestSuite生成测试报告
#    简介:HTMLTestRunner介绍
#
#    1、HTMLTestRunner介绍
#    HTMLTestRunner 是Python 标准库的unittest 模块的一个扩展，它可以生成HTML的测试报告，无法通过pip安装
#    首先要下 HTMLTestRunner.py 文件，将下载的文件放入...\python\Lib目录下（或者同个路径）
#
#    注意点：
#    python2和python3，语法不一样，导致HTMLTestRunner在python3不兼容
#    解决办法：导入课程资料里面修改好的HTMLTestRunner.py

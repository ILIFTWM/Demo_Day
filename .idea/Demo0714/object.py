#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 18:12
# @Author  : WM
# @File    : object.py
'''
使用对象 - 创建对象 / 给对象发消息
面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 /
'''
# 对象是类的实例化
# 定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）
# 子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：当然，也可以对子类增加一些方法，比如Dog类：
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型,判断一个变量是否是某个类型可以用isinstance()判断：

'''
class Animal(object):
    def run(self):
        print ('Animal is running...')
class People(object):
    def run(self):
        print ('People is running...')
class Man(Animal,People):
     pass
# Man类按照这样的继承顺序来写。 因为python新式类的继承用了新的MRO方法，
# 处理多重继承的时候，继承的属性、方法等是按照（P1，P2）从左往右搜索的，比如说run()，
# 如果在P1中搜索到了此方法，那么子类Man的run()就会调用P1的
#Man().run()      #Animal is running...
'''
class Animal(object):
    def run(self):
        print ('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')#方法重写
    def eat(self):
        print ('Eating meat...')
class Cat(Animal):
    pass
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
Cat().run()#调用父类方法


# 类是从一堆对象中抽取相同的内容而来的，那么抽象类就是从一堆类中抽取相同的内容而来的，内容包括数据属性和函数属性
# 抽象类的本质还是类，指的是一组类的相似性，包括数据属性（如all_type）和函数属性（如read、write），而接口只强调函数属性的相似性.
'''
import abc  #利用abc模块实现抽象类
class Animal(metaclass=abc.ABCMeta):  # 抽象类只能被继承,不能被实例化
    all_type = 'amimal'
    @abc.abstractmethod  # 继承后,加装饰器的,必须遵循类的方法
    def run(self):
        pass
    @abc.abstractmethod  # 继承后,加装饰器的,必须遵循类的方法
    def eat(self):
        pass
class People(Animal):
    def run(self):
        print('people is walking')
    def eat(self):
        print('people is eating')
People().run()
'''
 # 封装数据属性:明确的区分内外, 控制外部对影藏的属性的操作行为
# 广义上面向对象的封装 ：代码的保护，面向对象的思想本身就是一种
#  只让自己的对象能调用自己类中的方法 # 狭义上的封装 —— 面向对象的三大特性之一
#  属性 和 方法都藏起来 不让你看见
class Person:
    __key = 123 #  私有静态属性
    def __init__(self,name,passwd):
        self.name = name
        self.__passwd = passwd  # 私有属性
    def __get_pwd(self): # 私有方法,所有的私有 都是在变量的左边加上双下划线
        print('私有方法')
        return self.__passwd   #只要在类的内部使用私有属性，就会自动的带上_类名
    def login(self): # 正常的方法调用私有的方法
        self.__get_pwd()
alex = Person('alex','alex3714')
#print(alex._Person__passwd)  # _类名__属性名 #alex3714
alex.login()
    #  所有的私有 都是在变量的左边加上双下划綫
    # 对象的私有属性
    # 类中的私有方法
    #  类中的静态私有属性
    #  所有的私有的 都不能在类的外部使用

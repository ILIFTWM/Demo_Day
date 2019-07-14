#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 14:05
# @Author  : WM
# @File    : class.py
'''
学习内容：
类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / __str__方法
属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用__slots__
类中的方法 - 实例方法 / 类方法 / 静态方法

'''
# 对象：一个对象有自己的状态，行为和唯一的标识；所有的相同类型的对象所具有的结构和行为在他们共同的类中被定义
# 状态：包含这个对象已有属性（通常是类里面已经定义好的）在加上对象具有的当前属性值
# 行为：是指一个对象如何影响外界及被外界影响，表现为对象自身状态的改变和纤细的传递
# 标识：是指一个对象所具有的区别于所有对象的属性（本质上指内存中所创建的对象的地址）

# 属性是一个对象做具体的特性
# 方法就是对象能够做什么
# 任何一个对象都要包括2个部分：属性（是什么）和方法（能做什么
# 类是对某一群具有同样属性和方法的对象的抽象
# 要定义类，就要抽象，找出共同的方面
'''
class aa:#class来声明，后面定义的是一个类
    pass
a = aa()#类名+()；a是一个实例，也是一个对象，每个对象都有__class__属性，用于显示它的类型
print(type(aa))#<class 'type'>
print(a.__class__)
print(type(a))#<class '__main__.aa'>可以看出a是类aa的实例
print(a)#<__main__.aa object at 0x000002889EAD2320>;0x000002889EAD2320为内存地址，object对象
'''
# 类的构造器:
# __init__ 构造函数，在生成对象时调用.
# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

# __init__与__new__这两个魔法方法组成了Python类对象的构造器，在Python类实例化时，其实最先调用的不是__init__而是__new__。
# __new__是负责实例化对象的，而__init__是初始化操作。
# __del__是析构器，当Python对象的所有引用都不存在了（被del了），就会自动触发__del__执行
#当要销毁一个对象时，__del__()就会被调用
'''
class Student(object):
    def __init__(self, name, score):# 特殊方法“init”前后有两个下划线！注意到__init__方法的第一个参数永远是self，
                                    # 表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
        self.name = name
        self.score = score
bart = Student('Bart Simpson', 59)#必须传入与__init__方法匹配的参数，但self不需要传，在创建实例的时候，就不能传入空的参数

class CapStr(str):
    def __new__(cls, string):   #此时string = 'i love you';-- cls是CapStr这个类对象,cls也可以以self命名
        string = string.upper()
        return str.__new__(cls, string)
#对象的引用完后会调用__del__()；返回cls类带string参数的实例化的对象,但是这里为什么不直接return string ？看下面的代码段,   #I LOVE YOU；__del__析构方法被调用了！
#str.__new__(cls, string)的实际意思是str(string)，使用工厂函数str()将参数强制转换成str类型，然后再变成str的子类型CapStr,  <class '__main__.CapStr'>
        #return string  #I LOVE YOU,对象引用后不会调用__del__(),<class 'str'>
    def __del__(self):
        print('__del__析构方法被调用了！')
a = CapStr('i love you')
#del a # __del__析构方法被调用了！
print(type(a))
print(a)
'''
# __init__ 和 __new__ 最主要的区别在于：
# 1.__init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后，它是实例级别的方法。
# 2.__new__ 通常用于控制生成一个新实例的过程，它是类级别的方法


# 类的内置方法：
# __init__(self,...) 	 初始化对象，在创建新对象时调用
#  __del__(self) 	 释放对象，在对象被删除之前调用
#  __new__(cls,*args,**kwd) 	 实例的生成操作
#  __str__(self) 	 在使用print语句时被调用
#  __getitem__(self,key) 	 获取序列的索引key对应的值，等价于seq[key]
#  __len__(self) 	 在调用内联函数len()时被调用
#  __cmp__(stc,dst) 	 比较两个对象src和dst
#  __getattr__(s,name) 	 获取属性的值
#  __setattr__(s,name,value) 	 设置属性的值
#  __delattr__(s,name) 	 删除name属性
#  __getattribute__() 	 __getattribute__()功能与__getattr__()类似
#  __gt__(self,other) 	 判断self对象是否大于other对象
#  __lt__(slef,other) 	 判断self对象是否小于other对象
#  __ge__(slef,other) 	 判断self对象是否大于或者等于other对象
#  __le__(slef,other) 	 判断self对象是否小于或者等于other对象
#  __eq__(slef,other) 	 判断self对象是否等于other对象
#  __call__(self,*args) 	 把实例对象作为函数调用
'''class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):#即为self.name
        print('Hello, my name is', self.name)

p = Person('hhh')
p.sayHi()
'''

class Fruit:
    '''Fruit类'''               #为Fruit类定义了文档字符串
    def __str__(self):          # 定义对象的字符串表示,就是展示类的定义（文档说明）
        return self.__doc__
#print(__name__)
if __name__ == "__main__":  #if __name__=='__main__'说白了就是判断__name__变量是不是等于__main__，当执行文件本身时候__name__变量等于main，此时判断成立并执行判断语句中的代码，
                            # 当调用该模块的时候__name__并不等于__main__条件不成立，不执行判断下面的语句，可以认为为了调试模块，因为在模块导入的时候并不执行if下面的语句。
    fruit = Fruit()
   # print(str(fruit))# 调用内置函数str()发__str__()方法，输出结果为:Fruit类
   # print(fruit)   #直接输出对象fruit,返回__str__()方法的值，输出结果为:Fruit类


#  __getattr__(s,name) 	 获取属性的值
#  __setattr__(s,name,value) 	 设置属性的值
#  __delattr__(s,name) 	 删除name属性
#  __getattribute__() 	 __getattribute__()功能与__getattr__()类似
'''
class C(object):
    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        return object.__getattribute__(self, *args, **kwargs)

    #        return "haha"
    def __getattr__(self, name):
        print("__getattr__() is called ")
        return name + " from getattr"

    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return self

    def __getitem__(self, item):
        print('__getitem__ call')
        return object.__getattribute__(self, item)

    def foo(self, x):
        print(x)


class C2(object):
    d = C()


if __name__ == '__main__':
    c = C()
    c2 = C2()
    print(c.a)  #__getattribute__() is called
                # abc
    print(c.zzzzzzzz) #__getattribute__() is called
                      # __getattr__() is called
                      # zzzzzzzz from getattr
    c2.d
    print(c2.d.a) #__get__() is called <__main__.C2 object at 0x00000217F1B15438> <class '__main__.C2'>
                  #__get__() is called <__main__.C2 object at 0x00000217F1B15438> <class '__main__.C2'>
                  #__getattribute__() is called
                  #abc

    print(c['a']) #__getitem__ call
                  # abc
'''
#使用__slots__
'''

class Student(object):
       pass
s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
     self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果,25
'''
'''
#想要限制class的属性:在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
class Student(object):
     __slots__ = ('name') # 用tuple定义允许绑定的属性名称,__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
                          #除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__
s = Student()
s.name = 'Michael'
s.age = 25
print(s.name)#AttributeError: 'Student' object has no attribute 'age'
'''

#类中的方法 - 实例方法 / 类方法 / 静态方法
# 静态方法和类方法都需要使用修饰器，分别使用的是staticmethod和classmethod,调用静态方法使用实例和不使用实例都是可以的。
# 类方法中，把类作为第一个参数传递进来，这个参数就是类本身，类方法也可以不需要实例而直接使用类调用。
# 类方法是可以替代静态方法的。静态方法不能在继承中修改。

class Test:
    def normal_function():
        print('我是普通函数！')
    @staticmethod
    def static_method():
        print('我是静态方法！')
    @classmethod
    def class_method(cls):
        print('我是{cls}的类方法！')
    def instance_method(self):
        print('我是{self}的实例方法！')
t = Test()
# 普通函数：只能通过类名调用，不用手动传参
#t.normal_function()#报以下错误
'''
# Traceback (most recent call last):
#   File "test.py", line 19, in <module>
#     t.normal_function()
# TypeError: normal_function() takes 0 positional arguments but 1 was given
# '''
Test.normal_function()# 我是普通函数！
# 静态方法：可以通过实例和类名调用，不用手动传参
t.static_method()
Test.static_method()
"""
# 我是静态方法！
# 我是静态方法！
"""
# 类方法：可以通过实例和类名调用，自动传递类给 cls 形参
# 注意：即使通过实例调用类方法，Python 自动传递的也是类，而不是实例
t.class_method()#我是{cls}的类方法！
Test.class_method()#我是{cls}的类方法！
# 实例方法：
# 通过实例调用，自动传递实例给 self 形参
# 通过类调用，需要手动传递一个实例给 self 形参
t.instance_method()#我是{self}的实例方法！
Test.instance_method(t)#我是{self}的实例方法！
# 通过类调用，如果不手动传递实例给 self 形参，会缺少参数的错误
Test.instance_method()#TypeError: instance_method() missing 1 required positional argument: 'self'


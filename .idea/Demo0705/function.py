#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 0:09
# @Author  : WM
# @File    : function.py
'''
学习内容：
函数的作用 - 代码的坏味道 / 用函数封装功能模块
定义函数 - def语句 / 函数名 / 参数列表 / return语句 / 调用自定义函数
调用函数 - Python内置函数 / 导入模块和函数
函数的参数 - 默认参数 / 可变参数 / 关键字参数 / 命名关键字参数
函数的返回值 - 没有返回值 / 返回单个值 / 返回多个值
作用域问题 - 局部作用域 / 嵌套作用域 / 全局作用域 / 内置作用域 / 和作用域相关的关键字
用模块管理函数 - 模块的概念 / 用自定义模块管理函数 / 命名冲突的时候会怎样（同一个模块和不同的模块）
'''
'''

#变量本质:占位符(标签)
#def  add (a,b): #函数的声明，开始
#if _name =="main":
#def 函数名(变量1，变量2，…):#可有参数，也可无参数，参数可以无参数类型
    # 函数体(语句块)

#参数与变量本质相同，只有建立变量与对象关系时，对象才有类型。
#多态:pyhon为对象编写接口，而不是为数据类型。
'''
def my_fun():
    '''
    This is function,函数说明文档
    :return:
    '''
    print("I am coding.")
    return  #return—— 1.返回函数值，2.结束正在执行的函数，类似break
    prirnt("I finished.")

if __name__ == "__main__":
    my_fun()

#形参(参数)车位，实参(值，数据，对象)车，一个停车位可以在不同时间停放不同的汽车。
#赋值是将占位符指向变量。

def add(x): #x是参水，准确点说是形参
    a = 10  #as是变量
    return a+x #x就是那个形参作为变量，其本质是要传递赋给这个函数的值

#局部变量:函数体内(某个范围内)起作用的变量。
#全局变量:有局部，就有对应的全部。global声明为全局变量。
#命名空间:处于该作用域内的标识符，且本身也用标识符表示。
#输入函数的参数不确定，其它参数全部通过*args(以元组的形式)，**kwargs(以dict类型的数据，传值时说明"键"与"值")由arg收集起来。
def func(x,*args):
    print(x)
    result = x
    print(args)#args是元组tuple里面，(2, 3, 4, 5, 6)
    for i in args:
        result += i
        return result
print(func(1,2,3,4,5,6))

def foo(**kwargs):#以dict类型的数据
    print(kwargs)
foo(a=1,b=2,c=3)
#递归函数
def fib(n):
    '''
    :param n:
    :return: this is Fibonacci by recursion
    '''
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else :
        return fib(n-1)+fib(n-2)
f =fib(10)
print(f)
'''
wrong coding
meno = {0:0,1:1}
def fib2(n):
    if not n in meno:

       meno[n] = fib2(n-1)+fib2(n-2)#unsupported operand type(s) for +: 'NoneType' and 'NoneType'
       type(meno[n])
       return meno[n]
f = fib2(10)
print(f)
'''
#Python支持多种范型的语言，可以进行所谓的函数式编程，突出的体现有:filter,map,,lambda,yield
lam =lambda x:x+3
print(lam(3))
#lambda arg1,arg2,...:表达式（表达式计算结果就是本函数的返回值）
'''lambda函数不能包含命令，包含的表达式不能超过一个，不要试图向lambda函数中塞太多的东西，如果需要更复杂的东西，
应该定义一个普通函数'''
numbers = [0,1,2,3]
map(lambda x:x+3,numbers)#[x+3 for x in numbers]

#map(func,seq)
'''func 是一个函数，seq是一个序列对象，在执行的时候，序列对象中每个元素，按照从左到右的顺序，依次被取出来，
并塞入到func那个函数里面，并将func的返回至依次存到list中'''

x = iter(range(1,10))
for a in zip(x,x,x):
    print(a)
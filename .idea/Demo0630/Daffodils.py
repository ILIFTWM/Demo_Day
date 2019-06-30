#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/30 21:00
# @Author  : WM
# @File    : Daffodils.py
'''
水仙花数是各立方和等于这个数的本身的数
如：153 = 1**3 + 5**3 + 3**3

'''
for num in range(100,1000): #num在[100,1000)范围内依次循环取值，第一次100，第二次101，最后一次999
     unit =  num % 10     #得到个位上的数字
     hundreds = num // 100  #对100取整，得到百位数字；//为取整符号，
     decade = num // 100 % 10
     if num == (unit**3 + hundreds**3 +decade**3):
         print(num, end=' ，')  #end = ' '使得输出的数不换行，以空格隔开同行输出

'''
判断一个数是不是完美数：完全数（Perfect number），
又称完美数或完备数，如果一个数恰好等于它的因子之和，则称该数为“完全数”
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
除自身外真约数之和
'''
for i in range(1,10000):
    s = 0
    for k in range(1,i):
        if i % k == 0:
            s = s + k
    if i == s:
        print("%d是完美数"%i)


'''Fibonacci数列为：0、1、1、2、3、5、8、13、21......
数列第一项为0，第二项为1，从第三项开始，每一项为相邻前两项之和
'''
def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)
for i in range(1,20):
    print(fib(i),end= ',')
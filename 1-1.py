#!/usr/bin/python3

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)

var1='hello python'
print("更新var1字符段：",var1[:6]+"world!")

i,j=0,1
while j<10:
    print(j,end=";")
    i,j=j,i+j

import time;  # 引入time模块

ticks = time.asctime(time.localtime(time.time()))
print("当前时间戳为:", ticks)

import calendar

cal = calendar.month(2018, 8)
print("以下输出2018年8月份的日历:")
print(cal)
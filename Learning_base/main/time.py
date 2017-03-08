#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import time
#1、时间戳    1970年1月1日之后的秒
#2、元组 包含了：年、日、星期等... time.struct_time
#3、格式化的字符串    2014-11-11 11:11

#当前时间的三种表示方式
print time.time()  #时间戳
print time.gmtime()   #元组形式
print time.strftime("%Y-%m-%d %H:%M:%S")   #格式化字符串

print '\n'

#三种方式相互转换(不能时间戳转格式化字符串，或者格式化字符串转时间戳，要通过中间元组形式转换)
print time.strptime('2016-11-25', "%Y-%m-%d")  #格式化字符串  转  元组形式
print time.localtime(time.time())  #时间戳转元组形式
print time.mktime(time.localtime()) #元组形式  转  时间戳
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #元组形式  转 格式化字符串 

print '\n'

print time.asctime()  #asctime([t])，接收一个时间元组，返回可读形式“Sun Jan 22 17:36:00 2017”24个字符的字符串
print time.asctime(time.localtime()) 
print time.ctime(time.time())  #把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式

#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import time
#1、时间戳    1970年1月1日之后的秒
#3、元组 包含了：年、日、星期等... time.struct_time
#4、格式化的字符串    2014-11-11 11:11

#当前时间的三种表示方式
print time.time()  #时间戳
print time.gmtime()   #元组形式
print time.strftime("%Y-%m-%d %H:%M:%S")   #格式化字符串

#三种方式相互转换
print time.strptime('2016-11-25', "%Y-%m-%d")  #格式化字符串  转  元组形式
print time.localtime(time.time())  #时间戳转元组形式
print time.mktime(time.localtime()) #元组形式  转  时间戳
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #元组形式  转 格式化字符串 

print time.asctime()
print time.asctime(time.localtime()) 
print time.ctime(time.time())

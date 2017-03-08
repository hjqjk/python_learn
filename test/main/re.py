#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#正则表达式模块
import re

str1 = 'sjfl23jdslfj3334jfsdj21jfs323'
str2 = 'sjlfjdljfwerio23ierjwoerwi235'
str3 = 'sdfwer236564gasdagfdg23234223'

result1 = re.match('\d+', str1)  #只在字符串的头部匹配，匹配不上返回None，匹配上就返回match object
if result1:
    print result1.group()  #找到就打印出来
else:
    print 'noting'

result2 = re.search('\d+', str1) #在整个字符串找，匹配到一个就不继续了
if result2:
    print result2.group()
else:
    print 'noting'
    
result3 = re.findall('\d+', str1) #在整个字符串找，贪婪匹配，返回列表
print  result3

com = re.compile('\d+')  #一次编译，可以多次对不同的字符串进行匹配，效率会比上边的高
print com.findall(str1)
print com.findall(str2)
print com.findall(str3)


result4 = re.search('(\d+)\w*(\d+)', str1)
print result4.group()   #获取整个正则匹配的内容
print result4.groups()  #只获取分组匹配的内容

'''
正则表达式常用格式：
字符：
    \d : 数字
    \w : 数字、字母、_、-
    \t : 制表符
    . : 除了回车符以外的所有字符
次数：
    * : 大于等于0
    + : 大于等于1
    ? : 0 或 1
    {m} : m 次 
    {m,n} : m <= x <= n

'''
#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib
import re
import collections
import string
import webbrowser as web

# 寻找相对而言，较为稀少的字母。

# 方法一
# response = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html") # 利用urllib 的 urlopen 方法,抓取网页内容
# html = response.read()  # 读取网页内容
#
# diff = html.split("--")  # 用'--'字符串分割该网页内容。返回列表。
# str1 = ''.join(diff[3])  # 找到我们需要的那部分内容,将列表转为字符串。
# result = re.findall('[a-z]', str1)   # 找到一堆字符串中的字母,贪婪搜索。
#
# base_url = ''.join(result)

# 方法二
# 将ocr.html源码中的rare characters字符串,复制到files/L2.txt中用于以后的处理
# s = ''.join([line.rstrip() for line in open('files/L2.txt')])  # 读取文件的内容并转为字符串。注意匿名函数的写法。列表生成式
# OCCURRENCES = collections.OrderedDict()  # 保持key顺序。key会按插入的顺序排列,而不是key本身排序。
#
# for c in s:  # 以字符为key,出现的次数为value。
#     OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1  # OCCURRENCES.get(c, 0),有这个key,则返回对应的value,否则返回0
# avgOC = len(s) // len(OCCURRENCES)  #求得字符的平均值
#
# base_url =  ''.join([c for c in OCCURRENCES if OCCURRENCES[c] < avgOC])  # 如果字符出现的次数少于平均值,则输出该字符。注意输出字符的顺序。


# 方法三
s = ''.join([line.rstrip() for line in open('files/L2.txt')])
base_url = filter(lambda x:x in string.letters, s)  # 利用内置函数filter，将字母筛选出来。匿名函数


path_url = "http://www.pythonchallenge.com/pc/def/"

print "\nNext level: "
print "%s%s.html" % (path_url, base_url)
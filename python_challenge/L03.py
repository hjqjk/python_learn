#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib2
import string
import re

response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
html = response.read()

contents = html.split('--')[1]  # 获取要匹配的内容文本

# 方法一
# result = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', contents)  # 正则匹配，只获取分组()中的匹配内容
# # result = re.findall("(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])", contents) # ?<= exp ,匹配exp后边的位置。?= exp, 匹配exp前面的位置
# base_url = ''.join(result)

# 方法二
# 循环判断每个字母，符合 xXXXxXXXx 形式的，才会输出
base_url = "".join([contents[i+3] for i in range(len(contents)-7) \
                    if contents[i+3].islower() and \
                    False not in [ not contents[i-1].isupper(), contents[i].isupper(), contents[i+1].isupper(), contents[i+2].isupper(),\
                                   contents[i+4].isupper(), contents[i+5].isupper(), contents[i+6].isupper(), not contents[i+7].isupper()]])


path_url = "http://www.pythonchallenge.com/pc/def/"

print "\nNext level: "
print "%s%s.html" % (path_url, base_url)





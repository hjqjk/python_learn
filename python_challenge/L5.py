#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import urllib2
import pickle

# 读取banner.p的序列化数据，并将其反序列化。
# 题意：[(' ', 95)] 表示输出95个空格字符。

html = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()

result = pickle.loads(html)  # 将序列化的数据反序列化

# 方法一
# for row in result:  # 循环列表中的每个元素
#     output_str = ''
#     for i in row:
#         output_str += i[0] * i[1]  # 将当前列表元素中的字符串拼接成一个字符串
#     print output_str

# 方法二
# for row in result:
#     print ''.join(map(lambda i:i[0]*i[1], row))  # 用map函数 + 匿名函数

# 方法三

for row in result:
    print ''.join([c * count for c, count in row])  # 列表生成式


#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import zipfile
import re
import urllib
from StringIO import StringIO

# 方法一
# channel = zipfile.ZipFile('files/channel.zip', 'r')  # 创建一个zipfile对象，以只读方式打开指定的zip文档
# # channel.extractall(path='files/L6')  # 将zip文档解压到指定的目录
#
# next_nothing = '90052' # 根据readme.txt的提示，这里是开始
# comments = []  # 记录每个被匹配到的文件的文档说明
#
# while True:
#     contents = channel.read('%s.txt' % next_nothing)  # 读取zip文档中指定文件的内容
#     match = re.search('nothing is (\d+)', contents)  # 正则表达式，匹配数字
#     if match:  # 匹配上
#         next_nothing = ''.join(match.groups())  # 获取下一个文件名
#         letter = channel.getinfo('%s.txt' % next_nothing).comment  # getinfo()获取文件详细信息，comment表示文档说明
#         comments.append(letter)
#     else:  # 匹配失败，则跳出循环
#         print contents
#         break
#
# channel.close()  # 关闭zipfile对象
# print ''.join(comments)

# hockey不是最终答案。注意看打印出的字符串，每个组合字母都是由一个单一字母重复组成的。

# 方法二 ：不手动下载zip文档
zobj = StringIO()  # 创建一个StringIO对象
zobj.write(urllib.urlopen("http://pythonchallenge.com/pc/def/channel.zip").read()) # 通过url读取内容，并像文件一样写入内存
z = zipfile.ZipFile(zobj)  # 传入StringIO对象，创建一个zipfile对象

filenum = '90052'
lcomment = []

while True:
    if filenum.isdigit(): # 匹配上
        filename = filenum + '.txt'  # 加上后缀名
        lcomment.append(z.getinfo(filename).comment)  # 收集每个文件的文档说明
        info = z.read(filename)
        filenum = info.split(' ')[-1]
    else:  # 没匹配上，则退出
        break

z.close()
print ''.join(lcomment)

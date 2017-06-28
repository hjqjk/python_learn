#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib2
import re

first_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

nothing = '12345'
base_url = ''

for i in range(400):  # 最多循环400次
    html = urllib2.urlopen(first_url % nothing).read()  # 获取网页内容
    print html   # 打印当前获取的网页内容
    match = re.search('and the next nothing is (\d+)', html)  # 匹配，获取下次跳转的nothing值
    if match :
        nothing = ''.join(match.groups())  # 将下次的跳转值赋给nothing变量
    elif 'Divide' in html:
        nothing = str(int(nothing) / 2)  # 出题者故意设计的陷阱，得看他给的提示来重新计算下一次跳转值
    else:
        base_url = html   # 获取下一层的跳转
        break

# base_url = 'peak.html'  #这一层要经过大量的访问，速度很慢的，这个是结果
path_url = "http://www.pythonchallenge.com/pc/def/"

print "\nNext level: "
print "%s%s" % (path_url, base_url)
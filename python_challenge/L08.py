#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib2
import re
import bz2

# 方法一

# un 和 pw 的字符串，都是加密过来的，观察可知'BZh91AY'为 bz2算法 的特征，这些数据是被bz2压缩过的。
# 'PK\x03\x04' 是 zip算法 的特征
# '\x25\xD5\b\b' 是 gzip算法 的特征
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print 'Username is: ' + bz2.decompress(un)  # 用bz2的解压缩函数。decompress() 不能接受str类型的参数，在字符串前加b,转为字节形式
print 'Password is: ' + bz2.decompress(pw)


# 方法二
html = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").read()

un = ''.join(re.findall('un.*', html)).split("\'")[1]  # 获取内容
pw = ''.join(re.findall('pw.*', html)).split("\'")[1]

print 'Username is: ' + un.decode("string_escape").decode("bz2")
print 'Password is: ' + pw.decode("string_escape").decode("bz2")


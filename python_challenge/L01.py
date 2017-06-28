#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 破译给定的字符串
# 映射关系: a -> c , b -> d ... k -> m , o -> q , e -> g ... y -> a , z -> b

from string import maketrans
import string

str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# 方法一
# l1 = []
#
# for i in str1:
#     if i.isalpha():  #是英文字母的,才会映射
#         if i == 'y':
#             i = 'a'
#         elif i == 'z':
#             i =  'b'
#         else:
#             i = chr(ord(i)+2)
#
#     l1.append(i)  #映射后,加入列表
#
# print ''.join(l1)  #将列表以字符串形式打印


# 方法二
# intab = 'abcdefghijklmnopqrstuvwxyz'
# outtab = 'cdefghijklmnopqrstuvwxyzab'
#
# trantab = maketrans(intab,outtab)
#
# print str1.translate(trantab)


# 方法三
trantab = string.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
print str1.translate(trantab)

# 获取下一层的路径
str2 = 'map'

base_url = str2.translate(trantab)
path_url = "http://www.pythonchallenge.com/pc/def/"

print "\nNext level: "
print "%s%s.html" % (path_url,base_url)

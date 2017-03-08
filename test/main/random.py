#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#随机数模块
import random

print random.random()
print random.randint(1,6)
print random.randrange(1,3)

print '\n'

#随机验证码生成
checkcode = []
for i in range(0,6):
    if i == random.randint(1,6):
        checkcode.append(str(random.randint(1,9)))
    else:
        checkcode.append(chr(random.randint(65,90)))

print ''.join(checkcode)     #用join拼接字符串，比用+=效率更高    
        
#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#随机数模块
import random

print random.random()  #返回随机生成的一个实数，它在[0,1)范围内。
print random.randint(1,6)  #用于生成一个指定范围内的整数，1 <= 该整数 <= 6
print random.randrange(0,10,2)  #从[0,2,4,6,8]中获取一个随机数，2为递增数，该数要小于10

print '\n'

#随机验证码生成
checkcode = []
#共生成6个字符
for i in range(0,6): #列表：[0, 1, 2, 3, 4, 5]
    if i == random.randint(1,6): #判断随机数等于列表中的某个值的情况
        checkcode.append(str(random.randint(1,9)))  #生成随机数，添加到chekcode列表中
    else:
        checkcode.append(chr(random.randint(65,90)))  #生成随机数，并根据ASCII码表转为对应的字母形式，添加到列表中


print ''.join(checkcode)     #用join拼接字符串，比用+=效率更高    
        
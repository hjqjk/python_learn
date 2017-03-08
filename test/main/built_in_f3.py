#!/usr/bin/env python
#_*_ coding:utf-8 _*_

###map函数

##初级版
l1 = [11,22,33]
temp = []
for item in l1:
    temp.append(item+100)
print temp

#升级版(函数)
def add(avg):
    return avg+100

l1 = [11,22,33]
temp = []
for item in l1:
    temp.append(add(item))
print temp

#超升级版（map函数）
def add1(avg):
    return avg+100

l1 = [11,22,33]
print map(add1,l1)

#超级版（匿名函数）
l1 = [11,22,33]
print map(lambda avg:avg+100,l1)


### filter函数
print filter(lambda x:x>11, [11,22,33]) #列表里的元素逐一判断，大于11的才返回

### reduce函数
print reduce(lambda x,y:x+y,[11,22,33]) #列表里的元素累加，得出结果
# reduce(function,list)，function必须为两个参数


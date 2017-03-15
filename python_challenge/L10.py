#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 描述性列表：a = [1,11,21,1211] 根据前一个元素，通过描述，得出后一个元素。
# a[0] = 1 ； a[1]=11 表示前一个元素有1个1 ； a[2]=21 表示前一个元素有2个1 ；a[3]=1211 表示前一个元素有1个2，1个1
a = [1,11,21,1211,111221]
# a = [1,11,21]

for i in range(3,5):
    nextnumber = 0
    count = 0
    tmp = 1
    s = str(a[i-1])
    for j in range(len(s)):
        if s[j] == s[j+1]:
            tmp += 1
            if tmp >= 2 and tmp > count:
                count = tmp
        else:
            tmp = 1
            count = 0

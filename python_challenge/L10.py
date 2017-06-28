#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 描述性列表：a = [1,11,21,1211] 根据前一个元素，通过描述，得出后一个元素。
# a[0] = 1 ； a[1]=11 表示前一个元素有1个1 ； a[2]=21 表示前一个元素有2个1 ；a[3]=1211 表示前一个元素有1个2，1个1
# a = [1, 11, 21]
#
# for i in range(3, 31):
#     prev_num = str(a[i-1])
#     next_num = []  # 用列表存下一个数值
#     count = 1
#     loop = 0
#
#     while loop < len(prev_num)-1:
#         if prev_num[loop] == prev_num[loop+1]:
#             count += 1  # 相同的数字，单独统计
#         else:
#             next_num.append(str(count))  # 先加入统计count，注意转换为str类型
#             next_num.append(prev_num[loop])  # 加入当前字符
#             count = 1
#         loop += 1
#
#     next_num.append(str(count))  # 必须在while循环跳出后，再加入一遍
#     next_num.append(prev_num[loop])
#
#     a.append(int(''.join(next_num)))  # 将下一个数值，添加到a列表中
#
# next_level = len(str(a[30]))  # 数值类型的变量，不能使用len()函数，需要转换为str类型
#
#
# base_url = str(next_level) + '.html'
# path_url = "http://www.pythonchallenge.com/pc/return/"
#
# print "\nNext level: "
# print "%s%s" % (path_url, base_url)



import re
def describe(s):
    for m in re.finditer(r"(\d)\1*", s):
        print m.group(0),m.group(1)

    print [str(len(m.group(0))) + m.group(1)
                    for m in re.finditer(r"(\d)\1*", s)]
    return "".join([str(len(m.group(0))) + m.group(1)
                    for m in re.finditer(r"(\d)\1*", s)])
s = "1"
for dummy in range(5):
    s = describe(s)
print len(s)  # prints 5808
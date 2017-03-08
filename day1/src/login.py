#!/usr/bin/evn python
#_*_ coding:utf8 _*_

"""
编写登录接口：
- 输入用户名和密码
- 认证成功后显示欢迎信息
- 输错三次后锁定账号
"""

# 用户认证，用户密码都对返回'11'
def auth(username,password): 
    f1 = open("../file/account.txt",'r')  #打开文件

    for value in f1.readlines():  #读取文件内容，每次读取一行
        v1,v2 = value.split()  #以空格为分割符，分割字符串，分别赋值
        if username == v1 and password == v2:   #用户名和密码都正确，则跳出循环，不继续判断
            flag = '11'
            break
        elif username == v1 or password == v2:  #用户名或者密码正确
            flag = '1'
            break
        else:   #用户名和密码都不正确
            flag = '0'
    f1.close()   #记得要关闭文件
    return flag  #返回值被用做判断登录状态

# 判断账号是否被锁定，锁定则返回1
def locked(username):
    f2 = open("../file/account_lock.txt",'r')
    flag = 0   #考虑到锁文件内容为空的情况，就不会进入以下的for循环，必须得声明flag变量
    for value in f2.readlines():
        if username == value.strip('\n'):  #strip() 方法用于移除字符串头尾指定的字符（默认为空格）
            flag = 1
            break
        else:
            flag = 0
    f2.close()
    return flag



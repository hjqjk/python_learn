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
    f1 = open("../file/account.txt",'r')

    for value in f1.readlines():
        v1,v2 = value.split()
        if username == v1 and password == v2:
            flag = '11'
            break
        elif username == v1 or password == v2:
            flag = '1'
            break
        else:
            flag = '0'
    f1.close()
    return flag

# 判断账号是否被锁定，锁定则返回1
def lock(username):
    f2 = open("../file/account_lock.txt",'r')
    flag = 0
    for value in f2.readlines():
        if username == value.strip('\n'):
            flag = 1
            break
        else:
            flag = 0
    f2.close()
    return flag

uname = raw_input("\033[32;1musername: \033[0m")
error_count = 0
count = 0

while error_count < 3 and count < 10:
    passwd = raw_input("password: ")
    # 先判断该用户是否被锁了，如果被锁就返回错误提示并退出
    if lock(uname) == 1:
        print "the user:%s is locked" % uname
        break
    # 用户认证环节，分三种情况：用户不存在，用户存在密码输错，用户密码都输对
    mark = auth(uname,passwd)
    if mark == '0':
        print 'not find the user:',uname
        uname = raw_input('username: ')
    elif mark == '11':
        print 'Welcome ~~~'
        break
    else:
        print 'Your password is wrong,plz input again.'
        error_count += 1
        # 如果密码输错三次，则将该账号写进锁文件中
        if error_count == 3:
            f3 = open('../file/account_lock.txt','a+')
            f3.write(uname)
            f3.write("\n")
            f3.close()
           
    count += 1       

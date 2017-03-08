#!/usr/bin/evn python
# *_ coding:utf8 _*_

import login

if __name__ == '__main__':
    uname = raw_input("\033[32;1musername: \033[0m")
    error_count = 0  # 错误次数
    count = 0  # 用于控制提供用户名和密码输入口的重复次数
    
    while error_count < 3 and count < 10:
        passwd = raw_input("password: ")
        
        # 先判断该用户是否被锁了，如果被锁就返回错误提示并退出
        if login.locked(uname) == 1:
            print "the user:%s is locked" % uname
            break
        
        # 用户认证环节，分三种情况：用户不存在，用户密码都输对，用户存在但密码输错
        mark = login.auth(uname,passwd)
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
                f3.write("%s\n" % uname)  # 将被锁的用户写入锁文件
                f3.close()   
                
        count += 1       
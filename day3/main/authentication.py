#!/usr/bin/env python
#_*_ coding:utf-8 _*_

def auth(account,card_number,card_password): 
    error_count = 0 #输错密码的次数
    # 用户认证环节，分四种情况：用户不存在，用户被锁了，用户存在密码输错，用户密码都输对
    while account.has_key(card_number):  #用户存在
        if account[card_number]['locked'] == 1:  #用户被锁
            print "卡号 :%s 已经被锁了，请先去柜台解锁" % card_number
            return 0
            break  #退出
        elif account[card_number]['password'] == card_password: #用户和密码都正确
            print '欢迎登录本系统 ~~~'
            return 1
            break
        else:
            if error_count == 2:  # 如果密码输错三次，则锁住该用户
                print "你的卡号:%s，因输错三次密码被锁！" % card_number
                account[card_number]['locked'] = 1  
                return 0
                break
            else:
                print '你的密码输错了，请再次输入!'
                card_password = raw_input("你的卡号密码：")     
                error_count += 1   
    else:  #用户不存在
        print '卡号:%s 不存在，请确认该卡的有效性!' % card_number
        return 0

    
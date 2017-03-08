#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import pickle
import hashlib

def md5_password(password): #对密码进行hash，避免以明文方式存储密码
    hashmd5 = hashlib.md5() #生成一个MD5对象
    hashmd5.update(password) #hash化
    return hashmd5.hexdigest() #返回32位的16进制字符串

if __name__ == '__main__':
    #初始化用户数据（字典）
    account = {'100001':{'name':'jk','password':md5_password('123456'),'money':15000,'balance':15000,'locked':0},
               '100002':{'name':'hjq','password':md5_password('234567'),'money':15000,'balance':15000,'locked':0},
               '100003':{'name':'hjq123','password':md5_password('345678'),'money':15000,'balance':15000,'locked':0}}
    f1 = open('../db/account.db', 'w+')
    pickle.dump(account,f1) #将初始化的用户信息序列化存到文件中
    f1.close()
    
    #初始化商品信息（列表）
    goods = [{'name':'iphone6S','price':5400,'inventory':6},
             {'name':'python学习手册','price':119,'inventory':12},
             {'name':'移动硬盘','price':630,'inventory':20},
             {'name':'键盘','price':60,'inventory':30},
             {'name':'内存条','price':230,'inventory':100},
             {'name':'boss耳机','price':2300,'inventory':3},
             {'name':'手表','price':300,'inventory':6}]
    f2 = open('../db/goods.db','w+')
    pickle.dump(goods,f2) #序列化数据
    f2.close()
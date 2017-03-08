#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import pickle
from atm import md5_password  #对密码hash，避免明文方式存储密码

if __name__ == '__main__':
    #初始化用户数据
    account = {'100001':{'name':'jk','password':md5_password('123456'),'money':15000,'balance':15000,'locked':0},
               '100002':{'name':'hjq','password':md5_password('234567'),'money':15000,'balance':15000,'locked':0},
               '100003':{'name':'hjq123','password':md5_password('345678'),'money':15000,'balance':15000,'locked':0}}
    f1 = open('../db/account.db', 'w+')
    pickle.dump(account,f1) #将用户信息初始化并序列化存到文件中
    f1.close()
    
    #初始化商品信息
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
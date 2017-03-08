#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import hashlib
import pickle 

def md5_password(password): #对密码进行hash计算
    hashmd5 = hashlib.md5() #生成一个md5对象
    hashmd5.update(password) #hash化
    return hashmd5.hexdigest()  #返回32位的16进制字符串

def save_uid(uid,path): #利用pickle，实例化保存uid
    return pickle.dump(uid,open(path,'w'))  #将uid变量实例化存到文件中
    
def get_uid(path):
    return pickle.load(open(path,'r'))  #从文件中提取出实例化的uid变量                  

def show_menu(): #显示登录页面的菜单
    print "\t 1:  聊天"
    print "\t 2:  查看聊天记录"
    print "\t 3:  上传文件"
    print "\t 4:  退出系统"
    while True:
        operation = input("请选择操作(1/2/3/4)：")
        if operation in [1,2,3,4]:
            return operation
            break
        else:
            print "输入错误，请重新输入。"

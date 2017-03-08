#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from model import admin

def main():
    uname = raw_input("输入名字：")
    password = raw_input("输入密码：")
    
    admin.checkLogin(uname, password)

if __name__ == '__main__':
    main()
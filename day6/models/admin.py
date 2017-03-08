#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from utility.sql_helper import MySQLHelper
from lib.common import md5_password

def check_login(): #验证用户名和密码的正确性
    error_count = 0
    sql_helper = MySQLHelper() 
    while error_count < 3: #最多只能输入三次
        user = raw_input('输入用户名：')
        password = md5_password(raw_input('输入密码：'))
        sql = 'select * from admin where uname=%s and password=%s;'
        params = (user,password)
        result = sql_helper.get_all(sql, params)  #接收sql语句查询的结果
        if result:
            print '登录成功'
            return result[0]['uid'] #返回登录uid
            break
        else:
            print '用户名或者密码输错，请重新输入.'
            error_count += 1
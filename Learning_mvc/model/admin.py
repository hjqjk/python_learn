#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#业务逻辑层
from utility.sql_helper import MySQLHelper

def checkLogin(uname,password):
    sqlHelper = MySQLHelper()
    sql = 'select * from admin where uname=%s and password=%s;'
    params = (uname,password)
    
    reCount = sqlHelper.GetOne(sql, params) 
    if not reCount:
        print "用户名或密码输错，又或者没有这个用户"
    else:
        print "认证成功"


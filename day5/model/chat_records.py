#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#chat_records表

from utility.sql_helper import MySQLHelper

def insert_mesg(uid,speaker,chat_text):  #插入聊天信息到数据库
    sql = 'insert into chat_records(uid,speaker,chat_text) values(%s,%s,%s);'
    params = (uid,speaker,chat_text)
    sql_helper = MySQLHelper()
    sql_helper.insert(sql, params)  #插入数据

def select_mesg(uid):  #查询指定用户的聊天信息
    sql = 'select * from chat_records where uid=%s;'
    params = (uid,)
    sql_helper = MySQLHelper()
    return sql_helper.get_all(sql, params) #查询数据
    
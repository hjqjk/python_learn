#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb
from conf import conf_dic

class MySQLHelper():
    def get_all(self,sql,params):
        conn = MySQLdb.connect(**conf_dic)  #建立连接，注意要加**
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)  #建立游标，输出结果是字典形式
        cur.execute(sql,params)  #执行sql语句
        data = cur.fetchall()  #提取所有结果
        
        cur.close() #关闭游标
        conn.close() #关闭连接
        return data

    def insert(self,sql,params):
        conn = MySQLdb.connect(**conf_dic)  #建立连接，注意要加**
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)  #建立游标，输出结果是字典形式
        reCount = cur.execute(sql,params)  #执行sql语句，结果为影响了多少行
        conn.commit() #提交到数据库
        
        cur.close() #关闭游标
        conn.close() #关闭连接
        return reCount
    

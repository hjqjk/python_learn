#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb
from conf import conf_dic

class MySQLHelper():
    def get_all(self,sql,params):
        conn = MySQLdb.connect(**conf_dic)  #建立连接
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)  #建立游标
        cur.execute(sql,params) #执行sql语句
        data = cur.fetchall() #提取所有结果
        
        cur.close()
        conn.close()
        return data
    
    def modify(self,sql,params):  #insert、update、delete
        conn = MySQLdb.connect(**conf_dic) 
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        reCount = cur.execute(sql,params) #影响了多少行
        conn.commit()  #涉及到修改数据，必须提交
        
        cur.close()
        conn.close()
        return reCount
        
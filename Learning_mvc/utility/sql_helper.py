#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import MySQLdb
import conf

#数据层
class MySQLHelper():
    def GetAll(self,sql,params):
        conn = MySQLdb.connect(**conf.conn_dic) #conf.conn_dic是个字典类型，不能直接传入，需要通过 **conf.conn_dic 将其解析成 key1=value1,key2=value2形式
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) #输出结果是字典形式，更便于查看数据库的结构
        
        cur.execute(sql,params)  #执行
        data = cur.fetchall()
        
        cur.close()  #关闭游标
        conn.close() #关闭连接
        return data
    
    def GetOne(self,sql,params):
        conn = MySQLdb.connect(**conf.conn_dic)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) #输出结果是字典形式，更便于查看数据库的结构
        
        cur.execute(sql,params)  #执行
        data = cur.fetchone()
        
        cur.close()  #关闭游标
        conn.close() #关闭连接
        return data

 
    
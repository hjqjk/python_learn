#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb  #导入模块，该模块非Python自带，需要另外安装

#建立连接
conn = MySQLdb.connect(host='192.168.1.135',user='root',passwd='123456',db='testpy')

#创建游标
cur = conn.cursor()

#执行
#insert
# sql = "insert into t1(name,age) values(%s,%s);"
# params = ('hjqjk',25)
# reCount = cur.execute(sql,params)  #执行sql语句

#update
# sql = "update t1 set name=%s where id=%s;"
# params = ('JK',5)
# reCount = cur.execute(sql,params)  #执行sql语句

#delete
# sql = "delete from t1 where id=%s;"
# params = (5,)
# reCount = cur.execute(sql,params)  #执行sql语句

#batch_insert，批量插入
li = [('junqiH',18),('john',20)]
sql = "insert into t1(name,age) values(%s,%s);"
reCount = cur.executemany(sql,li)  #执行sql语句

conn.commit()  #insert、update、delete操作都需要提交，不然无法真正修改到数据库里边。

cur.close()  #关闭游标
conn.close() #关闭连接

print reCount  #影响多少行

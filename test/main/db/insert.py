#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb  #导入模块，该模块非Python自带，需要另外安装

#建立连接
conn = MySQLdb.connect(host='192.168.1.135',user='root',passwd='123456',db='testpy')

#创建游标
cur = conn.cursor()

#执行
sql = "insert into t1(name,age) values(%s,%s);"
params = ('hjq',26)
reCount = cur.execute(sql,params)  #执行sql语句
conn.commit()  #insert、update、delete操作都需要提交，不然无法真正修改到数据库里边。

cur.close()  #关闭游标
conn.close() #关闭连接

print reCount  #影响多少行

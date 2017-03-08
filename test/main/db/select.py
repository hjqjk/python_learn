#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb  #导入模块，该模块非Python自带，需要另外安装

#建立连接
conn = MySQLdb.connect(host='192.168.1.135',user='root',passwd='123456',db='testpy')

#创建游标
cur = conn.cursor()

#执行
reCount = cur.execute('select * from t1;')
data = cur.fetchall()

cur.close()  #关闭游标
conn.close() #关闭连接

print reCount
print data
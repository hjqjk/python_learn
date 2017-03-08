#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb  #导入模块，该模块非Python自带，需要另外安装

#建立连接
conn = MySQLdb.connect(host='192.168.1.135',user='root',passwd='123456',db='testpy')

#创建游标
cur = conn.cursor()  #输出结果是元组形式

#执行
#reCount = cur.execute('create table t2(id int primary key auto_increment,file varchar(25));')
cur.execute("insert into t2(file) values('/usr/local/tmp.txt');")
conn.commit() #提交
print cur.lastrowid  #提交后，利用lastrowid属性获取上条语句的自增id

reCount = cur.execute('select * from t2;')
data = cur.fetchall()
print data

cur.close()  #关闭游标
conn.close() #关闭连接

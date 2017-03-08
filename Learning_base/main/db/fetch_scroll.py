#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb  #导入模块，该模块非Python自带，需要另外安装

#建立连接
conn = MySQLdb.connect(host='192.168.1.135',user='root',passwd='123456',db='testpy')

#创建游标
cur = conn.cursor()  #输出结果是元组形式

#执行
reCount = cur.execute('select * from t1;')

dataone = cur.fetchone() #只取从当前指针开始的一行数据
print dataone
dataone = cur.fetchone()
print dataone

data = cur.fetchall()  #取得从当前指针开始到最后的所有结果
print data

cur.scroll(0,mode='absolute')  #绝对定位，回到最初
data = cur.fetchall()
print '全部行：',data

cur.scroll(-1,mode='relative')  #相对定位，-1 表示往回退一行
dataone = cur.fetchone()
print dataone

cur.close()  #关闭游标
conn.close() #关闭连接

#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb
import time
import getpass

password = getpass.getpass("root's password: ")
tid = input("tid(int): ")
dt = raw_input("dateline(%Y-%m-%d %H:%M:%S): ")
fid_array = [172,268,189,173,48,269,267,49,137,182,266,78,79,281,44,45,46] #广告区的fid列表
count = 0

def datetime_timestamp(dt):
    #dt为字符串，转换为时间戳的中间过程，一般都需要将字符串转化为时间数组
    dt_array = time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    #将"%Y-%m-%d %H:%M:%S"转化为时间戳，返回的时间戳为浮点数
    s = time.mktime(dt_array)
    #将浮点数转换为整数
    return int(s)

#打开数据库连接
db = MySQLdb.connect(host="localhost",user="root",passwd=password,db="tigtag_bbs",unix_socket="/data/mysql/mysql.sock")
#使用cursor()方法获取操作游标
cursor = db.cursor()
#使用execute方法执行SQL语句
cursor.execute("use tigtag_bbs;")
#查询指定帖子的fid，并将结果存到result列表中
cursor.execute("select fid from tig_forum_thread where tid=%d;" % tid)
result = cursor.fetchone()  
if result[0] in fid_array: #如果是广告区的帖子，则允许修改发帖时间
    cursor.execute("update tig_forum_thread set dateline=%d where tid=%d;" % (datetime_timestamp(dt),tid))
    #影响了多少行
    count = cursor.rowcount
    print "修改成功,影响了多少行"
else:
    print "这是非广告区的帖子，不能通过修改发帖时间来置顶"

if count == 1:
    print "修改成功"
else:
    print "发生异常"

#关闭数据库连接
db.close()

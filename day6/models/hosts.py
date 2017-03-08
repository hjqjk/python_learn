#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from utility.sql_helper import MySQLHelper

class Hosts(object):
    def __init__(self):
        self.sqlhelper = MySQLHelper()
        self.ip = ''
        self.port = 0
        self.user = ''
        self.password = ''
        self.gid = 0
        
    def get_all(self,gid):  #获取指定gid的所有主机
        self.gid = gid 
        sql = 'select * from hosts where gid=%s;'
        params = (self.gid,)
        
        result = self.sqlhelper.get_all(sql, params)
        return result    
        
    def select_group_host(self,gid): #查询指定组的主机ip
        self.gid = gid 
        sql = 'select ip from hosts where gid=%s;'
        params = (self.gid,)
        
        result = self.sqlhelper.get_all(sql, params)
        return result
        
    def add_host(self,ip,port,user,password,gid):  #增加主机
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password
        self.gid = gid
        
        sql = 'insert into hosts(ip,port,user,password,gid) values(%s,%s,%s,%s,%s);'
        params = (self.ip,self.port,self.user,self.password,self.gid)
        
        result = self.sqlhelper.modify(sql, params)
        return result
     
    def del_host(self,ip,gid): #根据ip和gid,删除指定主机
        self.ip = ip
        self.gid = gid 
        
        sql = 'delete from hosts where ip=%s and gid=%s;'
        params = (self.ip,self.gid)
        
        result = self.sqlhelper.modify(sql, params)
        return result
    
    
#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from  utility.sql_helper import MySQLHelper


class Groups_host(object):
    
    def __init__(self,uid):
        self.uid = uid
        self.sqlhelper = MySQLHelper()
        self.gname = ''
        self.gnew_name = ''
    
    def get_group(self): #查询指定uid的主机组
        
        sql = 'select * from groups_host where uid=%s;'
        params = (self.uid,)
        
        result = self.sqlhelper.get_all(sql, params) 
        return result   #返回结果
    
    def select_group(self,gname): #查询指定组名的主机组
        self.gname = gname
        sql = 'select * from groups_host where gname=%s;'
        params = (self.gname,)
        
        result = self.sqlhelper.get_all(sql, params) 
        return result   #返回结果
    
    def add_group(self,gname):  #添加新主机组
        self.gname = gname
        sql = 'insert into groups_host(gname,uid) values(%s,%s);'
        params = (self.gname,self.uid)
        
        result = self.sqlhelper.modify(sql, params)  #修改
        return result
    
    def del_group(self,gname): #删除指定主机组
        self.gname = gname
        sql = 'delete from groups_host where gname=%s;'
        params = (self.gname,)
        
        result = self.sqlhelper.modify(sql, params)  #修改
        return result
    
    def rename_group(self,gname,gnew_name): #修改主机组的组名
        self.gname = gname
        self.gnew_name = gnew_name
        sql = 'update groups_host set gname=%s where gname=%s;'
        params = (self.gnew_name,self.gname)
        
        result = self.sqlhelper.modify(sql, params)
        return result


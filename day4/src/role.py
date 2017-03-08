#!/usr/bin/env python
#_*_ coding:utf8 _*_

class Role(object): #角色类
    def __init__(self,name,age,sex,work,social_status,assets):
        self.name = name  #姓名
        self.age = age  #年龄
        self.sex = sex  #性别
        self.work = work  #工作
        self.social_status = social_status  #社会地位
        self.assets = assets  #资产

    
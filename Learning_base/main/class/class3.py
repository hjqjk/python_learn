#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#只读特性和只写特性

class People(object): #继承object类
    
    def __init__(self,name,age,state): #初始化
        self.Name = name  #动态字段，属于对象
        self.Age = age
        self.__private_var = state  #私有字段（'__'两个下划线开头），只能内部访问
    
    
    def Show(self):
        print self.__private_var #内部函数引用私有字段，这样外部通过访问函数就能访问到私有字段
       
    #只读特性 
    @property
    def Private_var(self):  #可通过将函数转为特性
        return self.__private_var
    
    #只写特性,Private_var的先定义
    @Private_var.setter
    def Private_var(self,value):
        self.__private_var = value
    
user1 = People('hjq',25,'中国')  #创建对象，实例化。每创建一个对象，就都得开辟一次内存空间
print user1.Private_var  
user1.Private_var = 'china'  #可写
print user1.Private_var






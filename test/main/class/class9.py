#!/usr/bin/env python
#_*_ coding:utf-8 _*_

class People:
    
    def __init__(self,name,age,state): #初始化
        self.Name = name  #动态字段，属于对象
        self.Age = age
        self.__private_var = state  #私有字段（'__'两个下划线开头），只能内部访问
    
    def Show(self):
        print self.__private_var #内部函数引用私有字段，这样外部通过访问函数就能访问到私有字段
        
    @property
    def Private_var(self):  #可通过将函数转为特性
        return self.__private_var
    
    def __PrivateFunc(self):  #私有方法（'__'两个下划线开头）
        print '私有方法'
        
    def Show2(self):  #通过公有方法访问私有方法，提供对外访问
        self.__PrivateFunc()
        
user1 = People('hjq',25,'中国')
print user1.__dict__  #利用python的__dict__属性，一次查出对象的所有字段和字段值（字典形式输出）
print dir(user1)  #输出对象的属性名、方法名、Python自带的一些东西




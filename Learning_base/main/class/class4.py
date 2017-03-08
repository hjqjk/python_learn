#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#只读特性和只写特性

class People1:  #经典类中的特性全部都是可读可写（没有只读）
    def __init__(self,name,age,state): #初始化
        self.Name = name  #动态字段，属于对象
        self.Age = age
        self.__private_var = state  #私有字段（'__'两个下划线开头），只能内部访问

    @property
    def show(self):  #可通过将函数转为特性
        return self.__private_var

class People2(object):   #继承object类
    def __init__(self,name,age,state): #初始化
        self.Name = name  #动态字段，属于对象
        self.Age = age
        self.__private_var = state  #私有字段（'__'两个下划线开头），只能内部访问

    @property
    def show(self):  #可通过将函数转为特性
        return self.__private_var

class People3(object): #继承object类
    def __init__(self,name,age,state): #初始化
        self.Name = name  #动态字段，属于对象
        self.Age = age
        self.__private_var = state  #私有字段（'__'两个下划线开头），只能内部访问

    @property
    def show(self):  #可通过将函数转为特性
        return self.__private_var
    
    #继承了object类，要想私有字段可写，必须加上下面的装饰器
    @show.setter
    def show(self,value):  #可通过将函数转为特性
        self.__private_var  = value


p1 = People1('hjq',25,'中国')
print p1.show
p1.show = 'china'  #可修改。没有继承object类，则特性可读可写
print p1.show

p2 = People2('jk123',20,'澳洲')
print p2.show
#p2.show = 'UE'  #报错，不可修改
print p2.show

p3 = People3('jk',18,'美国')
print p2.show
p2.show = 'UA'   #继承object类，则特性@property可读，要加@xxx.setter才可写
print p2.show




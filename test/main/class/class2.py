#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#私有字段和私有方法

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
        
    
user1 = People('hjq',25,'中国')  #创建对象，实例化。每创建一个对象，就都得开辟一次内存空间
user2 = People('jk',18,'美国')

#print user1.__private_var  #会报错。外部不能访问私有字段
user1.Show() 
print user1.Private_var  #类似于外部对象访问私有字段
#user1.__PrivateFunc()  #报错。外部不能直接访问私有方法
user1.Show2()  
 
user1._People__PrivateFunc()  #python中可通过:_类名__私有方法名()，显式调用私有方法，但不建议这么用




